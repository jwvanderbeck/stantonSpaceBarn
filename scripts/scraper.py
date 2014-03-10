# Scrapes the game's XML data for use in SSB's database

import os, sys
import argparse
import json
from xml.etree import ElementTree


ENTITIES_PATH = "Entities/"
SHIPS_PATH = "Vehicles/Implementations/Xml/"
ITEMS_PATH = "Items/Xml/Spaceships/"

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args(["/Users/john/Documents/SSB/Star Citizen Data/Scripts_Patch_11", "/Users/john/Documents/SSB/Parsed Data/Patch_11.1"])

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
            shipData['displayname'] = getAttribute(root, 'displayname')
            if 'classname' in root.attrib:
                classname = root.attrib['classname']
                try:
                    shipData['class'] = int(classname.split(' ')[-1])
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
            shipData['ports'] = []
            for port in ports:
                itemPort = port.find('ItemPort')
                if "invisible" in itemPort.attrib['flags']:
                    continue
                portData = {}
                portData['name'] = getAttribute(port, 'name')
                # Display name
                portData['displayname'] = getAttribute(itemPort, 'display_name')
                if not portData['displayname']:
                    portData['displayname'] = getAttribute(itemPort, 'displayname')
                # Sizes
                portData['minsize'] = getIntAttribute(itemPort, 'minsize')
                portData['maxsize'] = getIntAttribute(itemPort, 'maxsize')
                # Flags
                portData['flags'] = getAttribute(itemPort, 'flags')
                # Types and subtypes
                types = itemPort.find("Types").findall("Type")
                if len(types) == 0:
                    print "\t\t\t[WARNING] This port has no types associated with it"
                    continue
                portData['types'] = []
                for itemType in types:
                    itemTypeData = {}
                    itemTypeData['type'] = getAttribute(itemType, 'type')
                    subtypes = getAttribute(itemType, 'subtypes')
                    if subtypes:
                        itemTypeData['subtypes'] = subtypes.split(',')
                    else:
                        itemTypeData['subtypes'] = []
                    portData['types'].append(itemTypeData)
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
                        modData["displayname"] = displaynames[0].attrib["value"]
                    # Change the internal name
                    mainpart = modification.findall(".//Elem[@idRef='idMainPart']")
                    if len(mainpart) == 0:
                        mainpart = modification.findall(".//Elem[@idRef='idHullPartName']")
                    if len(mainpart) > 0:
                        modData["name"] = mainpart[0].attrib["value"]
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
        print "\t[WARNING] Unable to find Weapon data.  Skipping."
    else:
        print "\tScanning Weapon data..."
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
                itemData['displayname'] = getParam(params, "display_name")
                if not itemData['displayname']:
                    itemData['displayname'] = getParam(params, "displayname")
                # ItemType
                itemData['itemtype'] = getParam(params, 'vehicleItemType')
                if not itemData['itemtype']:
                    itemData['itemtype'] = getParam(params, 'itemType')
                if not itemData['itemtype']:
                    print "\t\t\t\t[ERROR] No item type found!"
                    continue
                itemData['itemsubtype'] = getParam(params, 'vehicleItemSubType')
                if not itemData['itemsubtype']:
                    itemData['itemsubtype'] = getParam(params, 'itemSubType')
                # Size
                itemData['size'] = getIntParam(params, 'vehicleItemSize')
                if not itemData['size']:
                    itemData['size'] = getIntParam(params, 'itemSize')
                itemData['class'] = getIntParam(params, 'vehicleItemClass')
                if not itemData['class']:
                    itemData['class'] = getIntParam(params, 'itemClass')
                itemData['manufacturer'] = getParam(params, 'vehicleItemManufactor')
                if not itemData['manufacturer']:
                    itemData['manufacturer'] = getParam(params, 'itemManufactor')
                # Description
                itemData['description'] = getParam(params, 'vehicleItemDescription')
                if not itemData['description']:
                    itemData['description'] = getParam(params, 'itemDescription')
                # Item Stats
                itemData['itemstats'] = {}
                itemType = itemData['itemtype']
                itemSubType = itemData['itemsubtype']
                if itemType.lower() == "weapon":
                    # Weapons are handled in a different manner
                    stats = params.find('vehicleItemStats')
                    if stats is not None:
                        for stat in stats:
                            try:
                                value = float(stat.attrib['value'])
                                if value > 100:
                                    print "\t\t\t\t[OVER_VALUE] Detected over 100 value. %s : %f" % (stat.tag, value)
                                itemData['itemstats'][stat.tag] = value
                            except:
                                pass
                        stats = None
                elif itemType.lower() == "radar":
                    stats = root.find('radar')
                elif itemType.lower() == "cooler":
                    stats = None
                elif itemType.lower() == "battery":
                    stats = root.find('battery')
                elif itemType.lower() == "avionics":
                    if itemSubType.lower() == "signaturereductor":
                        stats = root.find("signatureReductor")
                    else:
                        stats = root.find('targetSelector')
                elif itemType.lower() == "container":
                    stats = None
                elif itemType.lower() == "display":
                    stats = root.find('display_radar')
                elif itemType.lower() == "powerplant":
                    stats = None
                elif itemType.lower() == "thruster":
                    # Thrusters are handled in a different manner
                    stats = root.find("thruster")
                    if stats is not None:
                        if "maxThrust" in stats.attrib:
                            itemData['itemstats']['maxThrust'] = stats.attrib['maxThrust']
                        if "speed" in stats.attrib:
                            itemData['itemstats']['speed'] = stats.attrib['speed']
                        if "acceleration" in stats.attrib:
                            itemData['itemstats']['acceleration'] = stats.attrib['acceleration']
                        yawData = stats.find("Yaw")
                        if yawData is not None:
                            itemData['itemstats']['yawMin'] = yawData.attrib['min']
                            itemData['itemstats']['yawMax'] = yawData.attrib['max']
                            if "speed" in yawData.attrib:
                                itemData['itemstats']['yawSpeed'] = yawData.attrib['speed']
                            if "accel" in yawData.attrib:
                                itemData['itemstats']['yawAcceleration'] = yawData.attrib['accel']
                        pitchData = stats.find("Pitch")
                        if pitchData is not None:
                            itemData['itemstats']['pitchMin'] = pitchData.attrib['min']
                            itemData['itemstats']['pitchMax'] = pitchData.attrib['max']
                            if "speed" in pitchData.attrib:
                                itemData['itemstats']['pitchSpeed'] = pitchData.attrib['speed']
                            if "accel" in pitchData.attrib:
                                itemData['itemstats']['pitchAcceleration'] = pitchData.attrib['accel']
                        rollData = stats.find("Roll")
                        if rollData is not None:
                            itemData['itemstats']['rollMin'] = rollData.attrib['min']
                            itemData['itemstats']['rollMax'] = rollData.attrib['max']
                            if "speed" in rollData.attrib:
                                itemData['itemstats']['rollSpeed'] = rollData.attrib['speed']
                            if "accel" in rollData.attrib:
                                itemData['itemstats']['rollAcceleration'] = rollData.attrib['accel']
                    stats = None
                elif itemType.lower() == "ordinance":
                    stats = None
                elif itemType.lower() == "ammobox":
                    stats = None
                elif itemType.lower() == "aimodule":
                    stats = None
                if stats is not None:
                    for stat in stats:
                        try:
                            value = float(stat.attrib['value'])
                            name = stat.attrib['name']
                            if value > 100:
                                print "\t\t\t\t[OVER_VALUE] Detected over 100 value. %s : %f" % (name, value)
                            itemData['itemstats'][name] = value
                        except:
                            pass
                    stats = None
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
                        portData = {}
                        portData['name'] = getAttribute(port, 'name')
                        # print "Found port %s" % portData['name']
                        # Display name
                        portData['displayname'] = getAttribute(itemPort, 'display_name')
                        if not portData['displayname']:
                            portData['displayname'] = getAttribute(itemPort, 'displayname')
                        # Sizes
                        portData['minsize'] = getIntAttribute(itemPort, 'minsize')
                        portData['maxsize'] = getIntAttribute(itemPort, 'maxsize')
                        # Flags
                        portData['flags'] = getAttribute(itemPort, 'flags')
                        # Types and subtypes
                        types = itemPort.find("Types").findall("Type")
                        if len(types) == 0:
                            print "\t\t\t[WARNING] This port has no types associated with it"
                            continue
                        portData['types'] = []
                        for itemType in types:
                            itemTypeData = {}
                            itemTypeData['type'] = getAttribute(itemType, 'type')
                            subtypes = getAttribute(itemType, 'subtypes')
                            if subtypes:
                                itemTypeData['subtypes'] = subtypes.split(',')
                            else:
                                itemTypeData['subtypes'] = []
                            portData['types'].append(itemTypeData)
                        itemData['ports'].append(portData)
                # Pipes - These are basically resources
                pipes = root.find('Pipes')
                if pipes is not None:
                    itemData['pipes'] = {}
                    for pipe in pipes:
                        itemData['pipes'][pipe.attrib['class']] = {}
                        basePipe = itemData['pipes'][pipe.attrib['class']]
                        states = pipe.findall("State")
                        for state in states:
                            stateDescriptor = state.attrib['state']
                            if "," in stateDescriptor:
                                # Multiple states use these values
                                stateNames = stateDescriptor.split(",")
                                for stateName in stateNames:
                                    values = state.findall("Value")
                                    if len(values) == 1:
                                        # Only a single value per second
                                        basePipe[stateName] = values[0].attrib['value']
                                    elif len(values) > 1:
                                        # Multiple values, which means a curve over time
                                        valueStrings = []
                                        for value in values:
                                            valueStrings.append("%d:%d" % (int(value.attrib['delay']), int(value.attrib['value'])))
                                        basePipe[stateName] = ",".join(valueStrings)
                                    else:
                                        # No values, skip it
                                        continue
                            else:
                                # Single state uses these values
                                values = state.findall("Value")
                                if len(values) == 1:
                                    # Only a single value per second
                                    basePipe[stateDescriptor] = values[0].attrib['value']
                                elif len(values) > 1:
                                    # Multiple values, which means a curve over time
                                    valueStrings = []
                                    for value in values:
                                        valueStrings.append("%d:%d" % (int(value.attrib['delay']), int(value.attrib['value'])))
                                    basePipe[stateDescriptor] = ",".join(valueStrings)
                                else:
                                    # No values, skip it
                                    continue
                # print itemData
                outputFile = os.path.join(args.destination, itemData['name'] + ".json")
                jsonData = json.dumps(itemData, sort_keys=True, indent=4, separators=(',',':'))
                print "\t\t\t\tSaving..."
                with open(outputFile, "w") as f:
                    f.write(jsonData)

    sys.exit(0)