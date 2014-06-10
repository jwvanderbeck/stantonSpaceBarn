# Scrapes the game's XML data for use in SSB's database

import os, sys
import argparse
import json
from xml.etree import ElementTree


ENTITIES_PATH = "Entities/"
SHIPS_PATH = "Vehicles/Implementations/Xml/"
ITEMS_PATH = "Items/Xml/Spaceships/"
INVALID_ITEMTYPES = [
    "seat",
    "aimodule",
    "debris",
    "display",
    "light",
    "avionics",
    "ammobox",
    "visor"
]

def getAttribute(element, attributeName):
    return element.get(attributeName, "")

def getIntAttribute(element, attributeName):
    try:
        return int(element.get(attributeName, None))
    except:
        return 0

def getFloatAttribute(element, attributeName):
    try:
        return float(element.get(attributeName, None))
    except:
        return 0.0

def getBooleanAttribute(element, attributeName):
    try:
        val = element.get(attributeName, None)
        if val.lower() == "true":
            return True
        elif val.lower() == "false":
            return False
        elif val == "1":
            return True
        elif val == "0":
            return False
        else:
            return False
    except:
        return False

def getParam(root, paramName):
    try:
        return root.find("param[@name='" + paramName + "']").get('value')
    except:
        return None

def getIntParam(root, paramName):
    try:
        return int(root.find("param[@name='" + paramName + "']").get('value'))
    except:
        return 0

def getFloatParam(root, paramName):
    try:
        return float(root.find("param[@name='" + paramName + "']").get('value'))
    except:
        return 0.0
def getBooleanParam(root, paramName, default):
    try:
        val = root.find("param[@name='" + paramName + "']").get('value')
        if val.lower() == "true":
            return True
        elif val.lower() == "false":
            return False
        elif val == "1":
            return True
        elif val == "0":
            return False
        else:
            return default
    except:
        return default

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args(["/Users/john/Documents/SSB/Star Citizen Data/Scripts_Patch_12_1", "/Users/john/Documents/SSB/Parsed Data/Patch_12_1"])

    print "Working on %s" % args.source
    entitiesPath = os.path.join(args.source, ENTITIES_PATH)
    if not os.path.isdir(entitiesPath):
        print "\t[ERROR] Couldn't find entities!"
        sys.exit(1)
    # Ships
    shipsPath = os.path.join(entitiesPath, SHIPS_PATH)
    if not os.path.isdir(shipsPath):
        print "\t[WARNING] Unable to find ships data.  Skipping."
    else:
        print "\tScanning ship data..."
        filesToParse = os.listdir(shipsPath)
        for xmlFile in filesToParse:
            try:
                ext = os.path.splitext(xmlFile)[1]
            except:
                ext = '.'
            if ext.lower() != ".xml":
                continue
            print "\t\t%s" % xmlFile
            xmlDoc = ElementTree.parse(os.path.join(shipsPath, xmlFile))
            if not xmlDoc:
                print "\t\t\t[ERROR] Failed to properly read in XML data. Skipping."
                continue
            root = xmlDoc.getroot()
            # Basic ship data
            # CIG Changed how variants work.  Originally there was a separate XML definition for ach variant
            # but now it is one XML definition for the entire line.  IE 300 line, or Hornet line.  At the end
            # of that file is a section <Modifications> that defines all the variants.
            # To work with this new system we first build up a "base" definition, then iterate through each
            # "Modification" and make a definition for that modification.  We then save that out as a separate
            # file.
            # This still feels unfinished on CIGs part, so will need to keep an eye on how things shake out
            shipData = {}
            shipData['name'] = root.attrib['name']
            shipData['category'] = getAttribute(root, 'category')
            shipData['displayName'] = getAttribute(root, 'displayname')
            shipData['empty_mass'] = 0.0
            partsWithMass = root.findall('.//Part[@mass]')
            if len(partsWithMass) > 0:
                for partWithMass in partsWithMass:
                    mass = float(partWithMass.attrib['mass'])
                    shipData['empty_mass'] = shipData['empty_mass'] + mass
            print "Ship Mass: %f" % shipData['empty_mass']
            if 'classname' in root.attrib:
                classname = root.attrib['classname']
                try:
                    shipData['vehicleClass'] = int(classname.split(' ')[-1])
                except:
                    pass
            # "Ports", which really means attachment points
            # These apparently are not just hardpoints but also PowerPlant, Thruster, Cargo, etc
            # I wonder if they are moving to a more generic system with this than the original ship planning?
            try:
                ports = root.findall(".//Part[@class='ItemPort']")
                if len(ports) == 0:
                    ports = None
            except:
                ports = None

            if not ports:
                print "\t\t\t[WARNING] Either no ports were found, or the XML data for ports was not parsed properly.  Skipping this ship."
                shipData = None
                continue

            if ports:
                shipData['ports'] = []
                for port in ports:
                    itemPort = port.find('ItemPort')
                    # if "invisible" in itemPort.attrib['flags']:
                    #     continue
                    portData = {
                        "_reuse": True,
                        "_searchfield": "name",
                        "_m2m": True,
                        "_modelname": "ports"
                    }
                    portData['name'] = getAttribute(port, 'name')
                    # print "Found port %s" % portData['name']
                    # Display name
                    portData['displayName'] = getAttribute(itemPort, 'display_name')
                    if not portData['displayName']:
                        portData['displayName'] = getAttribute(itemPort, 'displayname')
                    # Sizes
                    portData['minSize'] = getIntAttribute(itemPort, 'minsize')
                    portData['maxSize'] = getIntAttribute(itemPort, 'maxsize')
                    # Flags
                    portData['flags'] = getAttribute(itemPort, 'flags')
                    # Types and subtypes
                    parentTypes = itemPort.find("Types")
                    if not parentTypes:
                        print "Unable to find Types for item port!"
                        print portData
                        continue
                    types = itemPort.find("Types").findall("Type")
                    if len(types) == 0:
                        print "\t\t\t[WARNING] This port has no types associated with it"
                        continue
                    validType = False
                    for itemType in types:
                        typeName = getAttribute(itemType, 'type')
                        if not typeName.lower() in INVALID_ITEMTYPES:
                            validType = True
                            break
                    if not validType:
                        continue
                    portData['supportedTypes'] = []
                    for itemType in types:
                        typeName = getAttribute(itemType, 'type')
                        if typeName.lower() in INVALID_ITEMTYPES:
                            continue
                        subtypes = getAttribute(itemType, 'subtypes')
                        if subtypes:
                            subTypeNames = subtypes.split(',')
                            for subTypeName in subTypeNames:
                                itemTypeData = {
                                    "_m2m": True,
                                    "_modelname": "supportedTypes",
                                    "_reuse": True,
                                    "_searchfield": "name",
                                    "name": "%s:%s" % (typeName, subTypeName),
                                    "typeName": typeName,
                                    "subTypeName": subTypeName
                                }
                                portData['supportedTypes'].append(itemTypeData)
                        else:
                            itemTypeData = {
                                "_m2m": True,
                                "_modelname": "supportedTypes",
                                "_reuse": True,
                                "_searchfield": "name",
                                "name": typeName,
                                "typeName": typeName
                            }
                            portData['supportedTypes'].append(itemTypeData)
                    shipData['ports'].append(portData)
            # print shipData
            # Now that we have a base definition, we need to loop through all the modifications for the actual ship data
            # If there are no modifications, then the base definition is used as the only ship variant
            modifications = root.find("Modifications")
            if modifications is not None and len(modifications) > 0:
                print "\t\t\t[DEBUG] Modifications found for this ship.  Iterating through all variants"
                for modification in modifications:
                    print "\t\t\t[DEBUG] Processing Variant: %s" % modification.attrib['name']
                    outputFile = os.path.join(args.destination, shipData["name"] + "_mod_" + modification.attrib['name'] + ".json")
                    # We make a copy of the origina base ship data and now modify it as needed based on the
                    # Modification definition
                    modData = dict(shipData)
                    modData['ports'] = shipData['ports'][:]
                    # Change the displayname
                    displaynames = modification.findall(".//Elem[@name='displayname']")
                    if len(displaynames) > 0:
                        print displaynames[0].attrib
                        modData["displayName"] = displaynames[0].attrib["value"]
                    # Change the internal name
                    mainpart = modification.findall(".//Elem[@idRef='idMainPart']")
                    if len(mainpart) == 0:
                        mainpart = modification.findall(".//Elem[@idRef='idHullPartName']")
                    if len(mainpart) > 0:
                        modData["name"] = mainpart[0].attrib["value"]
                    # Alter mass if neccesary
                    partsWithMassChanges = modification.findall(".//Elem[@name='mass']")
                    if len(partsWithMassChanges) > 0:
                        print "*** NOTE Modification changes mass! ***"
                        for partWithMassChange in partsWithMassChanges:
                            newMass = partWithMassChange.attrib['value']
                            partID = partWithMassChange.attrib['idRef']
                            # Find the part with that ID
                            part = root.findall(".//ItemPort[@id='%s']" % part)
                            if part:
                                oldMass = part.attrib['mass']
                                if oldMass:
                                    difference = oldMass - newMass
                                    modData['mass'] = modData['mass'] - difference
                        print "New Mass: %f" % modData['mass']
                    # Disable any itemports that should be disabled.
                    # This is a bit trickier, due to the way the game does it, and i'm not sure but I think
                    # this will change in the future.  It doesn't seem like it will work for all situations
                    # but we will see.  Anyway the way CIG does it is that the modification elements point to other
                    # entries in the base definition through "id".  It basically specifies the id of the element
                    # to modify, the name of that element's attribute that is to be changed, and finally the new
                    # value.  This will, currently, lead us to a "SharedItem" or "SharedAutoWeapon" entry in the
                    # base definition.  But that isn't enough.  THAT entry though will lead us back to an actual
                    # itemport, and that is the itemport we need to remove if the original modification value is ""
                    #
                    # In summary, if there is a modification entry with name = part, and value = "", then we find
                    # the correlating itemport and remove it.
                    partmods = modification.findall(".//Elem[@name='part']")
                    # print partmods
                    if len(partmods) > 0:
                        for partmod in partmods:
                            # print partmod.attrib
                            if partmod.attrib['value'] == "":
                                itemportroot = root.findall(".//ItemPort[@id='%s']" % partmod.attrib['idRef'])
                                # print itemportroot
                                if len(itemportroot) > 0:
                                    portname = itemportroot[0].attrib['part']
                                    removeport = -1
                                    for i,port in enumerate(modData['ports']):
                                        # print port
                                        if port['name'] == portname:
                                            # print "\t\t\t[DEBUG] Variant removes port", port
                                            removeport = i
                                    if removeport > -1:
                                        modData['ports'].pop(removeport)
                    jsonData = json.dumps(modData, sort_keys=True, indent=4, separators=(',', ':'))
                    with open(outputFile, "w") as f:
                        f.write(jsonData)
            else:
                print "\t\t\t[DEBUG] No modifications found for this ship.  Scraping base data"
                outputFile = os.path.join(args.destination, shipData['name'] + ".json")
                jsonData = json.dumps(shipData, sort_keys=True, indent=4, separators=(',', ':'))
                with open(outputFile, "w") as f:
                    f.write(jsonData)
    # Items - Weapons
    itemsPath = os.path.join(entitiesPath, ITEMS_PATH) #, "Weapons")
    if not os.path.isdir(itemsPath):
        print "\t[WARNING] Unable to find Item data.  Skipping."
    else:
        print "\tScanning Item data..."
        for path, dirs, files in os.walk(itemsPath):
            print "\t\t", os.path.basename(path)
            filesToParse = files
            for xmlFile in filesToParse:
                try:
                    ext = os.path.splitext(xmlFile)[1]
                except:
                    ext = '.'
                if ext.lower() != ".xml":
                    continue
                print "\t\t\t%s" % xmlFile
                xmlDoc = ElementTree.parse(os.path.join(path, xmlFile))
                if not xmlDoc:
                    print "\t\t\t\t[ERROR] Failed to properly read in XML data. Skipping."
                    continue
                root = xmlDoc.getroot()
                # Basic weapon data
                itemData = {}
                itemData['name'] = getAttribute(root, 'name')
                params = root.find("params")
                # Display name
                itemData['displayName'] = getParam(params, "display_name")
                if not itemData['displayName']:
                    itemData['displayName'] = getParam(params, "displayname")
                if not itemData["displayName"]:
                    itemData["displayName"] = itemData["name"]
                # ItemType
                itemData['itemType'] = {
                    "_global": True,
                    "_reuse" : True,
                    "_searchfield": "name"
                }
                typeName = getParam(params, 'vehicleItemType')
                if not typeName:
                    typeName = getParam(params, 'itemType')
                subTypeName = getParam(params, 'vehicleItemSubType')
                if not subTypeName:
                    subTypeName = getParam(params, 'itemSubType')
                if not typeName:
                    # Unfortunately most of the ammo currently has no ItemType so we need to try and detect that manually before giving up!
                    if getAttribute(root, 'class').lower() == "laserbolt":
                        typeName = 'Ordinance'
                        subTypeName = 'LaserBolt'
                    elif getAttribute(root, 'class').lower() == "vehiclemissile":
                        typeName = 'Ordinance'
                        subTypeName = 'Missile'
                    else:
                        print "\t\t\t\t[ERROR] No item type found!"
                        continue
                itemData['itemType']["typeName"] = typeName.lower()
                if subTypeName:
                    subTypeName = subTypeName.lower()
                itemData['itemType']["subTypeName"] = subTypeName
                if not subTypeName:
                    itemData['itemType']["name"] = typeName.lower()
                else:
                    itemData['itemType']["name"] = "%s:%s" % (typeName.lower(), subTypeName.lower())
                # Currently we skip certain item types as they don't seem like things
                # we really want to deal with in the website, and they just make things
                # cluttered
                if typeName.lower() in INVALID_ITEMTYPES:
                    print "\t\t\t\t[WARNING] Skipping undesired ItemType %s" % typeName
                    continue
                # Size
                itemData['itemSize'] = getIntParam(params, 'vehicleItemSize')
                if not itemData['itemSize']:
                    itemData['itemSize'] = getIntParam(params, 'itemSize')
                itemData['itemClass'] = getIntParam(params, 'vehicleItemClass')
                if not itemData['itemClass']:
                    itemData['itemClass'] = getIntParam(params, 'itemClass')
                # Manufacturer
                manufacturer = getParam(params, 'vehicleItemManufactor')
                if not manufacturer:
                    manufacturer = getParam(params, 'itemManufactor')
                if manufacturer:
                    itemData['manufacturer'] = {
                        "_global": True,
                        "_reuse" : True,
                        "_searchfield" : "name",
                        "name" : manufacturer
                    }
                # Description
                itemData['description'] = getParam(params, 'vehicleItemDescription')
                if not itemData['description']:
                    itemData['description'] = getParam(params, 'itemDescription')
                # Item Mass
                mass = getFloatParam(params, 'mass')
                if not mass:
                    itemData['mass'] = 0.0
                else:
                    itemData['mass'] = mass
                hitpoints = getFloatParam(params, 'hitpoints')
                if not hitpoints:
                    itemData['hitpoints'] = 0.0
                else:
                    itemData['hitpoints'] = hitpoints
                # Item Stats
                # Where the actual specific item stats are stored in the XML is a real bitch and varies by item type and subtype
                # There are two types of data being worked with here
                # 1) Is the Item Stats - these are generic (ish) stats that some items have.  Generally seems to be used for display
                # purposes in the UI.  These are handled the same on all item types and stored in the ItemStat model
                # 2) ItemType specific data.  Some ItemTypes have very specific data (with some overlap!) that is stored
                # in models designed specifically for that purpose.

                itemData['itemStats'] = []
                # Generic ItemStats -- I think these might be removed in the future by CIG
                stats = params.find('itemStats')
                if stats is not None:
                    for stat in stats:
                        try:
                            value = float(stat.attrib['value'])
                            if value > 100:
                                print "\t\t\t\t[OVER_VALUE] Detected over 100 value. %s : %f" % (stat.tag, value)
                            statData = {
                                "_m2m": True,
                                "_modelname": "itemStats",
                                "_reuse" : True,
                                "_searchfield": "name",
                                "name" : stat.tag,
                                "value" : value
                            }
                            itemData['itemStats'].append(statData)
                        except:
                            pass

                # ItemType specific data
                itemType = typeName
                itemSubType = subTypeName
                if itemType.lower() == "weapon":
                    itemData["weaponData"] = {}
                    itemData["weaponData"]['fireModes'] = []
                    itemData["weaponData"]['supportedAmmo'] = []
                    # Get all support ammo names - we only store the name here
                    ammos = root.find('ammos')
                    if ammos is not None:
                        for ammo in ammos:
                            ammoData = {
                                "_global": True,
                                "_m2m": True,
                                "_modelname": "supportedAmmo",
                                "_reuse": True,
                                "_searchfield": "name",
                                "name": ammo.attrib["name"]
                            }
                            itemData["weaponData"]['supportedAmmo'].append(ammoData)
                    # Get all FireModes and the data we want on them
                    firemodes = root.find('firemodes')
                    if firemodes is not None:
                        for firemode in firemodes:
                            firemodeData = {
                                "_m2m": True,
                                "_modelname": "fireModes",
                                "_searchfield": "name"
                            }
                            name = getAttribute(firemode, 'name')
                            fireParams = firemode.find('fire')
                            if fireParams is not None:
                                firemodeData["name"] = name
                                if getParam(fireParams, "ammo_type"):
                                    firemodeData["ammo_type"] = getParam(fireParams, "ammo_type")
                                    firemodeData["ammo"] = {
                                        "_global": True,
                                        "_nocreate": True,
                                        "_reuse": True,
                                        "_searchfield": "name",
                                        "name": getParam(fireParams, "ammo_type")
                                    }
                                firemodeData["rate"] = getFloatParam(fireParams, "rate")
                                print "RATE", getFloatParam(fireParams, "rate")
                                firemodeData["damage"] = getFloatParam(fireParams, "damage")
                                print firemodeData
                                itemData["weaponData"]['fireModes'].append(firemodeData)
                    stats = root.find("turretParams")
                    if stats is not None:
                        yawMin = 0.0
                        yawMax = 0.0
                        yawSpeed = 0.0
                        pitchMin = 0.0
                        pitchMax = 0.0
                        pitchSpeed = 0.0
                        rollMin = 0.0
                        rollMax = 0.0
                        rollSpeed = 0.0
                        yawData = stats.find("yaw")
                        if yawData is not None:
                            if "limits" in yawData.attrib:
                                yaw = yawData.attrib["limits"]
                                yawSplit = yaw.split(",")
                                yaw1 = float(yawSplit[0])
                                yaw2 = float(yawSplit[1])
                                if yaw1 < yaw2:
                                    yawMin = yaw1
                                    yawMax = yaw2
                                else:
                                    yawMin = yaw2
                                    yawMax = yaw1
                            if "speed" in yawData.attrib:
                                yawSpeed = float(yawData.attrib['speed'])
                        pitchData = stats.find("pitch")
                        if pitchData is not None:
                            if "limits" in pitchData.attrib:
                                pitch = pitchData.attrib["limits"]
                                pitchSplit = pitch.split(",")
                                pitch1 = float(pitchSplit[0])
                                pitch2 = float(pitchSplit[1])
                                if pitch1 < pitch2:
                                    pitchMin = pitch1
                                    pitchMax = pitch2
                                else:
                                    pitchMin = pitch2
                                    pitchMax = pitch1
                            if "speed" in pitchData.attrib:
                                pitchSpeed = float(pitchData.attrib['speed'])
                        rollData = stats.find("roll")
                        if rollData is not None:
                            if "limits" in rollData.attrib:
                                roll = rollData.attrib["limits"]
                                rollSplit = roll.split(",")
                                roll1 = float(rollSplit[0])
                                roll2 = float(rollSplit[1])
                                if roll1 < roll2:
                                    rollMin = roll1
                                    rollMax = roll2
                                else:
                                    rollMin = roll2
                                    rollMax = roll1
                            if "speed" in rollData.attrib:
                                rollSpeed = float(rollData.attrib['speed'])
                        itemData['turretData'] = {
                            "yaw_min" : yawMin,
                            "yaw_max" : yawMax,
                            "yaw_speed": yawSpeed,
                            "pitch_min" : pitchMin,
                            "pitch_max" : pitchMax,
                            "pitch_speed": pitchSpeed,
                            "roll_min" : rollMin,
                            "roll_max" : rollMax,
                            "roll_speed": rollSpeed,
                        }
                elif itemType.lower() == "radar":
                    # Radar (Radar, Signatures)
                    stats = root.find('radar')
                    if stats is not None:
                        itemData['radarData'] = {
                            "radar_type" : getParam(stats, "radar_type"),
                            "search_radius" : getFloatParam(stats, "search_radius"),
                            "grid_size" : getFloatParam(stats, "grid_size"),
                            "signal_range_modifier" : getFloatParam(stats, "signal_range_modifier"),
                            "signal_antenna_gain" : getFloatParam(stats, "signal_antenna_gain"),
                            "signal_transmit_power" : getFloatParam(stats, "signal_transmit_power")
                        }
                    signatures = stats.find('Signatures')
                    if signatures is not None:
                        itemData["radarData"]['signatures'] = []
                        for signature in signatures:
                            signatureData = {
                                "_reuse": False,
                                "_searchfield": "name",
                                "name": signature.attrib['name'],
                                "threshold": signature.attrib['threshold']
                            }
                            itemData["radarData"]['signatures'].append(signatureData)
                elif itemType.lower() == "battery":
                    stats = root.find('battery')
                    if stats is not None:
                        itemData['batteryData'] = {
                            "dynamicPipe" : getFloatParam(stats, "dynamicPipe"),
                            "capacity" : getFloatParam(stats, "capacity"),
                            "chargeRate" : getFloatParam(stats, "chargeRate"),
                            "output" : getFloatParam(stats, "output")
                        }
                elif itemType.lower() == "armor":
                    # Armor
                    # Armor seems a bit unfinished right now, so there is a good chance CIG is going to change
                    # how this works, as its very messy right now.
                    stats = root.find('armor')
                    itemData["armorData"] = {}
                    if stats is not None:
                        itemData["armorData"]["signatures"] = []
                        if getFloatParam(stats, "crossSectionSignature") != 0:
                            signatureData = {
                                "_m2m": True,
                                "_modelname": "signatures",
                                "_reuse": False,
                                "_searchfield": "name",
                                "name": "CrossSection",
                                "value": getFloatParam(stats, "crossSectionSignature")
                            }
                            itemData["armorData"]["signatures"].append(signatureData)
                        if getFloatParam(stats, "infraredSignature") != 0:
                            signatureData = {
                                "_m2m": True,
                                "_modelname": "signatures",
                                "_reuse": False,
                                "_searchfield": "name",
                                "name": "Infrared",
                                "value": getFloatParam(stats, "infraredSignature")
                            }
                            itemData["armorData"]["signatures"].append(signatureData)
                        if getFloatParam(stats, "electromagneticSignature") != 0:
                            signatureData = {
                                "_m2m": True,
                                "_modelname": "signatures",
                                "_reuse": False,
                                "_searchfield": "name",
                                "name": "Electromagnetic",
                                "value": getFloatParam(stats, "electromagneticSignature")
                            }
                            itemData["armorData"]["signatures"].append(signatureData)
                    stats = root.find('damageMultipliers')
                    if stats is not None:
                        itemData["armorData"]['damageMultipliers'] = []
                        for stat in stats:
                            damageData = {
                                "_m2m": True,
                                "_modelname": "damageMultipliers",
                                "_reuse": False,
                                "_searchfield": "damagetype",
                                "damagetype": stat.attrib['damageType'],
                                "multiplier": stat.attrib['multiplier']
                            }
                            itemData["armorData"]['damageMultipliers'].append(damageData)
                elif itemType.lower() == "thruster" or itemType.lower() == "mainthruster":
                    # Thrusters
                    # Thrusters have two main models.
                    # "Thruster" is the main thruster data including maxThrust.  However for vectoring thrusters it also includes yaw/pitch/roll data
                    # "Gimbal" stores the data on how much a thruster can move in yaw/pitch/roll for manuevering thrusters
                    # Why the information is in two formats is beyond me.  Maybe CIG will clean this up in the future
                    stats = root.find("thruster")
                    if stats is not None:
                        maxThrust = 0
                        speed = 0
                        acceleration = 0
                        yawMin = 0
                        yawMax = 0
                        yawSpeed = 0
                        yawAcceleration = 0
                        pitchMin = 0
                        pitchMax = 0
                        pitchSpeed = 0
                        pitchAcceleration = 0
                        rollMin = 0
                        rollMax = 0
                        rollSpeed = 0
                        rollAcceleration = 0
                        if "maxThrust" in stats.attrib:
                            maxThrust = stats.attrib['maxThrust']
                        if "speed" in stats.attrib:
                            speed = stats.attrib['speed']
                        if "acceleration" in stats.attrib:
                            acceleration = stats.attrib['acceleration']
                        yawData = stats.find("Yaw")
                        if yawData is not None:
                            yawMin = yawData.attrib['min']
                            yawMax = yawData.attrib['max']
                            if "speed" in yawData.attrib:
                                yawSpeed = yawData.attrib['speed']
                            else:
                                yawSpeed = speed
                            if "accel" in yawData.attrib:
                                yawAcceleration = yawData.attrib['accel']
                            else:
                                yawAcceleration = acceleration
                        pitchData = stats.find("Pitch")
                        if pitchData is not None:
                            pitchMin = pitchData.attrib['min']
                            pitchMax = pitchData.attrib['max']
                            if "speed" in pitchData.attrib:
                                pitchSpeed = pitchData.attrib['speed']
                            else:
                                pitchSpeed = speed
                            if "accel" in pitchData.attrib:
                                pitchAcceleration = pitchData.attrib['accel']
                            else:
                                pitchAcceleration = acceleration
                        rollData = stats.find("Roll")
                        if rollData is not None:
                            rollMin = rollData.attrib['min']
                            rollMax = rollData.attrib['max']
                            if "speed" in rollData.attrib:
                                rollSpeed = rollData.attrib['speed']
                            else:
                                rollSpeed = speed
                            if "accel" in rollData.attrib:
                                rollAcceleration = rollData.attrib['accel']
                            else:
                                rollAcceleration = acceleration
                        itemData['thrusterData'] = {
                            "maxthrust" : float(maxThrust),
                            "yaw_min" : float(yawMin),
                            "yaw_max" : float(yawMax),
                            "yaw_speed": float(yawSpeed),
                            "yaw_acceleration" : float(yawAcceleration),
                            "pitch_min" : float(pitchMin),
                            "pitch_max" : float(pitchMax),
                            "pitch_speed": float(pitchSpeed),
                            "pitch_acceleration" : float(pitchAcceleration),
                            "roll_min" : float(rollMin),
                            "roll_max" : float(rollMax),
                            "roll_speed": float(rollSpeed),
                            "roll_acceleration" : float(rollAcceleration)
                        }
                    stats = root.find("gimbal")
                    if stats is not None:
                        yawMin = 0
                        yawMax = 0
                        yawSpeed = 0
                        yawAcceleration = 0
                        pitchMin = 0
                        pitchMax = 0
                        pitchSpeed = 0
                        pitchAcceleration = 0
                        rollMin = 0
                        rollMax = 0
                        rollSpeed = 0
                        rollAcceleration = 0
                        yawData = stats.find("yaw")
                        if yawData is not None:
                            yawMin = yawData.attrib['min']
                            yawMax = yawData.attrib['max']
                            if "speed" in yawData.attrib:
                                yawSpeed = yawData.attrib['speed']
                            else:
                                yawSpeed = 0
                            if "accel" in yawData.attrib:
                                yawAcceleration = yawData.attrib['accel']
                            else:
                                yawAcceleration = 0
                        pitchData = stats.find("pitch")
                        if pitchData is not None:
                            pitchMin = pitchData.attrib['min']
                            pitchMax = pitchData.attrib['max']
                            if "speed" in pitchData.attrib:
                                pitchSpeed = pitchData.attrib['speed']
                            else:
                                pitchSpeed = 0
                            if "accel" in pitchData.attrib:
                                pitchAcceleration = pitchData.attrib['accel']
                            else:
                                pitchAcceleration = 0
                        rollData = stats.find("roll")
                        if rollData is not None:
                            rollMin = rollData.attrib['min']
                            rollMax = rollData.attrib['max']
                            if "speed" in rollData.attrib:
                                rollSpeed = rollData.attrib['speed']
                            else:
                                rollSpeed = 0
                            if "accel" in rollData.attrib:
                                rollAcceleration = rollData.attrib['accel']
                            else:
                                rollAcceleration = 0
                        itemData['gimbalData'] = {
                            "yaw_min" : float(yawMin),
                            "yaw_max" : float(yawMax),
                            "yaw_speed": float(yawSpeed),
                            "yaw_acceleration" : float(yawAcceleration),
                            "pitch_min" : float(pitchMin),
                            "pitch_max" : float(pitchMax),
                            "pitch_speed": float(pitchSpeed),
                            "pitch_acceleration" : float(pitchAcceleration),
                            "roll_min" : float(rollMin),
                            "roll_max" : float(rollMax),
                            "roll_speed": float(rollSpeed),
                            "roll_acceleration" : float(rollAcceleration)
                        }
                elif itemType.lower() == "ordinance":
                    stats = root.find("physics")
                    if stats is not None:
                        pierceability = getFloatParam(stats, "pierceability")
                    if pierceability == 0:
                        pierceability = 15
                    itemData["ammoData"] = {
                        "_global": True,
                        "_reuse": True,
                        "_searchfield": "name",
                        "name" : itemData["name"],
                        "displayName" : itemData["displayName"],
                        "pierceability" : pierceability
                    }
                    vehicleDamageParams = root.find("VehicleDamageParams")
                    if vehicleDamageParams is not None:
                        itemData["ammoData"]['vehicleDamageParam'] = {
                            "damage" : getFloatParam(vehicleDamageParams, "damage"),
                            "damage_drop_min_distance" : getFloatParam(vehicleDamageParams, "damage_drop_min_distance"),
                            "damage_drop_per_meter" : getFloatParam(vehicleDamageParams, "damage_drop_per_meter"),
                            "damage_drop_min_damage" : getFloatParam(vehicleDamageParams, "damage_drop_min_damage")
                        }
                    vehicleMissileGuidanceParams = root.find("VehicleMissileGuidanceParams")
                    if vehicleMissileGuidanceParams is not None:
                        itemData["ammoData"]['vehicleMissileGuidanceParam'] = {
                            "min_tracking_angle" : getFloatParam(vehicleMissileGuidanceParams, "min_tracking_angle"),
                            "max_tracking_angle" : getFloatParam(vehicleMissileGuidanceParams, "max_tracking_angle"),
                            "min_tracking_distance" : getFloatParam(vehicleMissileGuidanceParams, "min_tracking_distance"),
                            "max_tracking_distance" : getFloatParam(vehicleMissileGuidanceParams, "max_tracking_distance"),
                            "guidance_type" : getParam(vehicleMissileGuidanceParams, "guidance_type"),
                            "signal_range_modifier" : getFloatParam(vehicleMissileGuidanceParams, "signal_range_modifier"),
                            "signal_antenna_gain" : getFloatParam(vehicleMissileGuidanceParams, "signal_antenna_gain"),
                            "signal_transmit_power" : getFloatParam(vehicleMissileGuidanceParams, "signal_transmit_power"),
                        }
                        signatures = vehicleMissileGuidanceParams.find("Signatures")
                        if signatures is not None:
                            itemData["ammoData"]['vehicleMissileGuidanceParam']['signatures'] = []
                            for signature in signatures:
                                signatureData = {
                                    "_reuse": False,
                                    "_searchfield": "name",
                                    "_m2m": True,
                                    "_modelname": "signatures",
                                    "name": signature.attrib["name"],
                                    "threshold": float(signature.attrib["threshold"])
                                }
                                itemData["ammoData"]['vehicleMissileGuidanceParam']['signatures'].append(signatureData)
                    vehicleMissileParams = root.find("VehicleMissileParams")
                    if vehicleMissileParams is not None:
                        itemData["ammoData"]['vehicleMissileParam'] = {
                            "turn_speed" : getFloatParam(vehicleMissileParams, "turn_speed"),
                            "turn_lazyness" : getFloatParam(vehicleMissileParams, "turn_lazyness"),
                            "max_speed" : getFloatParam(vehicleMissileParams, "max_speed"),
                            "accel" : getFloatParam(vehicleMissileParams, "accel"),
                            "maneuver_accel" : getFloatParam(vehicleMissileParams, "maneuver_accel"),
                            "initial_delay" : getFloatParam(vehicleMissileParams, "initial_delay"),
                            "detonation_radius" : getFloatParam(vehicleMissileParams, "detonation_radius"),
                            "damage" : getFloatParam(vehicleMissileParams, "damage"),
                            "category" : getParam(vehicleMissileParams, "category"),
                            "ammolive" : getBooleanParam(vehicleMissileParams, "ammoLive", False),
                        }


                # ItemPorts - As of Patch 4, Items now can have ItemPorts on them which complicates things a bit
                try:
                    ports = root.findall(".//ItemPort")
                    if len(ports) == 0:
                        ports = None
                except:
                    ports = None
                if ports:
                    itemData['ports'] = []
                    for port in ports:
                        itemPort = port
                        portData = {
                            "_reuse": True,
                            "_searchfield": "name",
                            "_m2m": True,
                            "_modelname": "ports"
                        }
                        portData['name'] = getAttribute(port, 'name')
                        # print "Found port %s" % portData['name']
                        # Display name
                        portData['displayName'] = getAttribute(itemPort, 'display_name')
                        if not portData['displayName']:
                            portData['displayName'] = getAttribute(itemPort, 'displayname')
                        # Sizes
                        portData['minSize'] = getIntAttribute(itemPort, 'minsize')
                        portData['maxSize'] = getIntAttribute(itemPort, 'maxsize')
                        # Flags
                        portData['flags'] = getAttribute(itemPort, 'flags')
                        # Types and subtypes
                        types = itemPort.find("Types").findall("Type")
                        if len(types) == 0:
                            print "\t\t\t[WARNING] This port has no types associated with it"
                            continue
                        portData['supportedTypes'] = []
                        for itemType in types:
                            typeName = getAttribute(itemType, 'type')
                            subtypes = getAttribute(itemType, 'subtypes')
                            if subtypes:
                                subTypeNames = subtypes.split(',')
                                for subTypeName in subTypeNames:
                                    itemTypeData = {
                                        "_global": True,
                                        "_reuse": True,
                                        "_m2m": True,
                                        "_modelname": "supportedTypes",
                                        "_searchfield": "name",
                                        "name": "%s:%s" % (typeName, subTypeName),
                                        "typeName": typeName,
                                        "subTypeName": subTypeName
                                    }
                                portData['supportedTypes'].append(itemTypeData)
                            else:
                                itemTypeData = {
                                    "_m2m": True,
                                    "_modelname": "supportedTypes",
                                    "_reuse": True,
                                    "_searchfield": "name",
                                    "name": typeName,
                                    "typeName": typeName
                                }
                                portData['supportedTypes'].append(itemTypeData)
                        itemData['ports'].append(portData)

                # New pipe model based on Arena Commander data (SC Patch 12)
                pipes = root.find('Pipes')
                if pipes is not None:
                    itemData["pipes"] = []
                    for pipe in pipes:
                        # <Pipe class="Power">
                        pipeClass = pipe.attrib['class']
                        if not pipeClass or pipeClass == "":
                            continue
                        pipeData = {
                            "_m2m": True,
                            "_modelname": "pipes",
                            "_reuse": True,
                            "_searchfield": "pipeClass",
                            "pipeClass": pipeClass
                        }
                        # <StateLevels>
                        stateLevels = pipe.find('StateLevels')
                        if stateLevels:
                            warning = stateLevels.find('Warning')
                            if warning is not None:
                                pipeData['levelWarning'] = getFloatAttribute(warning, "value")
                            critical = stateLevels.find('Critical')
                            if critical is not None:
                                pipeData['levelCritical'] = getFloatAttribute(critical, 'value')
                            fail = stateLevels.find('Fail')
                            if fail is not None:
                                pipeData['levelFail'] = getFloatAttribute(fail, 'value')
                        # </StateLevels>
                        # <Signature name="Infrared" multiplier="1">
                        sigs = pipe.findall('Signature')
                        if sigs and len(sigs) > 0:
                            pipeData['pipeSignatures'] = []
                            for sig in sigs:
                                sigData = {
                                    "_m2m": True,
                                    "_modelname": "pipeSignatures",
                                    "_reuse": True,
                                    "_searchfield": "name",
                                    "name": sig.attrib['name'],
                                    "multiplier": float(sig.attrib['multiplier'])
                                }
                                pipeData['pipeSignatures'].append(sigData)
                        # </Signature>
                        # <Pool type="Residual" capacity="800" rate="80" critical="1" allInPipe="1">
                        pool = pipe.find('Pool')
                        if pool is not None:
                            pipeData['pool'] = {
                                "_reuse": False
                            }
                            poolType = getAttribute(pool, "type")
                            if poolType:
                                pipeData['pool']['poolType'] = poolType
                            capacity = getFloatAttribute(pool, "capacity")
                            if capacity:
                                pipeData['pool']['capacity'] = capacity
                            rate = getFloatAttribute(pool, "rate")
                            if rate:
                                pipeData['pool']['rate'] = rate
                            critical = getBooleanAttribute(pool, "critical")
                            if critical:
                                pipeData['pool']['critical'] = critical
                            allInPipe = getBooleanAttribute(pool, "allInPipe")
                            if allInPipe:
                                pipeData['pool']['allInPipe'] = allInPipe
                        # </Pool>
                        # <States>
                        states = pipe.find('States')
                        if states is not None:
                            pipeData['states'] = []
                            for state in states:
                                # <State state="Default">
                                stateName = getAttribute(state, "state")
                                if not stateName:
                                    continue
                                stateData = {
                                    "_m2m": True,
                                    "_modelname": "states",
                                    "_reuse": True,
                                    "_searchfield": "name"
                                }
                                transition = getFloatAttribute(state, "transition")
                                stateData["transition"] = transition
                                # State state data will contain one or more Value tags
                                values = state.findall('Value')
                                if values and len(values) > 0:
                                    for pipeStateValue in values:
                                        dymVar = getAttribute(pipeStateValue, "dymVar")
                                        value = getFloatAttribute(pipeStateValue, "value")
                                        if not dymVar:
                                            if not "values" in stateData:
                                                stateData["values"] = []
                                            stateValueData = {
                                                "_m2m": True,
                                                "_modelname": "values",
                                                "_reuse": True,
                                                "_searchfield": "value",
                                                "value": value,
                                                "delay": getFloatAttribute(pipeStateValue, "delay")
                                            }
                                            stateData["values"].append(stateValueData)
                                        else:
                                            if not "dynamicValues" in stateData:
                                                stateData["dynamicValues"] = []
                                            stateData["dynamicValues"].append({
                                                    "_m2m": True,
                                                    "_modelname": "dynamicValues",
                                                    "_reuse": True,
                                                    "_searchfield": "dymVar",
                                                    "dymVar" : dymVar,
                                                    "value" : value
                                                })
                                # The state data may also contain one or more "Variable" tags
                                variables = state.findall('Variable')
                                if variables and len(variables) > 0:
                                    for variable in variables:
                                        if not "variableValues" in stateData:
                                            stateData["variableValues"] = []
                                        name = getAttribute(variable, "name")
                                        value = getFloatAttribute(variable, "value")
                                        stateData["variableValues"].append({
                                                "_m2m": True,
                                                "_modelname": "variableValues",
                                                "_reuse": True,
                                                "_searchfield": "name",
                                                "name": name,
                                                "value": value
                                            })
                                if "," in stateName:
                                    for y in stateName.split(","):
                                        stateData["name"] = y
                                        pipeData['states'].append(stateData)
                                else:
                                    stateData["name"] = stateName
                                    pipeData['states'].append(stateData)
                                # </State>
                        # </States>
                        itemData["pipes"].append(pipeData)
                        # </Pipe>

                # Pipes - These are basically resources
                # pipes = root.find('Pipes')
                # if pipes is not None:
                #     for pipe in pipes:
                #         itemData["pipe"+ pipe.attrib['class']] = []
                #         # itemData['pipes'][pipe.attrib['class']] = {}
                #         basePipe = itemData["pipe" + pipe.attrib['class']]
                #         states = pipe.find("States")
                #         if states:
                #             for state in states:
                #                 stateDescriptor = state.attrib['state']
                #                 print "Found state", stateDescriptor
                #                 if "," in stateDescriptor:
                #                     # Multiple states use these values
                #                     stateNames = stateDescriptor.split(",")
                #                     for stateName in stateNames:
                #                         stateData = {
                #                             "_reuse": True,
                #                             "_searchfield": "state",
                #                             "_m2m": True,
                #                             "_modelname": "pipe" + pipe.attrib['class']
                #                         }
                #                         values = state.findall("Value")
                #                         if len(values) == 1:
                #                             # Only a single value per second
                #                             # basePipe[stateName] = values[0].attrib['value']
                #                             stateData["state"] = stateName
                #                             stateData["value"] = values[0].attrib['value']
                #                             print "State %s=%s" % (stateName, values[0].attrib['value'])
                #                         elif len(values) > 1:
                #                             # Multiple values, which means a curve over time
                #                             valueStrings = []
                #                             for value in values:
                #                                 valueStrings.append("%d:%d" % (int(value.attrib['delay']), int(value.attrib['value'])))
                #                             data = ",".join(valueStrings)
                #                             stateData["state"] = stateName
                #                             stateData["value"] = data
                #                             print "State %s=%s" % (stateName, data)
                #                         else:
                #                             # No values, skip it
                #                             continue
                #                         basePipe.append(stateData)
                #                 else:
                #                     # Single state uses these values
                #                     values = state.findall("Value")
                #                     stateData = {
                #                         "_reuse": True,
                #                         "_searchfield": "state",
                #                         "_m2m": True,
                #                         "_modelname": "pipe" + pipe.attrib['class']
                #                     }
                #                     if len(values) == 1:
                #                         # Only a single value per second
                #                         # basePipe[stateDescriptor] = values[0].attrib['value']
                #                         stateData["state"] = stateDescriptor
                #                         stateData["value"] = values[0].attrib['value']
                #                         print "State %s=%s" % (stateDescriptor, values[0].attrib['value'])
                #                     elif len(values) > 1:
                #                         # Multiple values, which means a curve over time
                #                         valueStrings = []
                #                         for value in values:
                #                             valueStrings.append("%d:%d" % (int(value.attrib['delay']), int(value.attrib['value'])))
                #                         data = ",".join(valueStrings)
                #                         stateData["state"] = stateDescriptor
                #                         stateData["value"] = data
                #                         print "State %s=%s" % (stateDescriptor, data)
                #                     else:
                #                         # No values, skip it
                #                         continue
                #                     basePipe.append(stateData)
                # print itemData
                outputFile = os.path.join(args.destination, itemData['name'] + ".json")
                jsonData = json.dumps(itemData, sort_keys=True, indent=4, separators=(',',':'))
                print "\t\t\t\tSaving..."
                with open(outputFile, "w") as f:
                    f.write(jsonData)

    sys.exit(0)