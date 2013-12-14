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
	args = parser.parse_args(["/Users/john/Documents/SSB/Star Citizen Data/Scripts_Patch_9", "/Users/john/Documents/SSB/Parsed Data/Patch_9"])

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
			outputFile = os.path.join(args.destination, shipData['name'] + ".json")
			jsonData = json.dumps(shipData, sort_keys=True, indent=4, separators=(',',':'))
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
					continue
				itemData['itemsubtype'] = getParam(params, 'vehicleItemSubType')
				# Size
				itemData['size'] = getIntParam(params, 'vehicleItemSize')
				itemData['class'] = getIntParam(params, 'vehicleItemClass')
				# Manufacturer (We try two params because it looks like RSI mispelled this!)
				itemData['manufacturer'] = getParam(params, 'vehicleItemManufactor')
				if not itemData['manufacturer']:
					itemData['manufacturer'] = getParam(params, 'vehicleItemManufacturer')
				# Description
				itemData['description'] = getParam(params, 'vehicleItemDescription')
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
						print "Found port %s" % portData['name']
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
				with open(outputFile, "w") as f:
					f.write(jsonData)

	sys.exit(0)