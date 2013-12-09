import os, sys, json, argparse

# from shipBuilder.models import VehicleItem
# from shipBuilder.models import VehicleItemParams, VehicleItemPower, VehicleItemHeat, VehicleItemAvionics
# from shipBuilder.models import VehicleItemType, VehicleItemSubType
# from shipBuilder.models import Manufacturer
# from shipBuilder.models import Vehicle, ItemPort, VehicleCategory
# from shipBuilder.models import GameUpdate, GameUpdateChange, GameUpdateEntity
import scripts.ingestion as ingestion

# This script reads in the JSON files produced from scraping the Star Citizen game data, and creates 
# or updates the data in the shipBuilder database

# parser = argparse.ArgumentParser()
# parser.add_argument('module')
# parser.add_argument('build')
# parser.add_argument('source')
# args = parser.parse_args()
# if args.source:
# 	DATA_PATH = args.source
# else:
# 	DATA_PATH = "/Users/john/Documents/SSB/Parsed Data/Patch_0"
# 	# DATA_PATH = "/home/jwvanderbeck/sc_parsed_data"

# if not args.module:
# 	args.module = "Hangar"

# if not args.build:
# 	args.build = "124.0000"


def addGameUpdateEntry(entity, entryType, message):
	build = args.build
	module = args.module
	name = "%s Module Build %s" % (module, build)
	gameUpdate = GameUpdate.objects.get(name__iexact=name)
	if not gameUpdate:
		gameUpdate = GameUpdate(name = name, build = build, module = module)
		gameUpdate.save()

	if entryType == "changed":
		description = "CHANGED: %s" % message
	elif entryType == "new":
		description = "NEW: %s" % message
	elif entryType == "removed":
		description = "REMOVED: %s" % message

	# This update is attached to an entity such as a vehicle or item
	entry = GameUpdateChange(entity = entity, update = gameUpdate, description = description)
	entry.save()

# Ingest vehicles
def ingestVehicle(dataFile, data):
	if not "category" in data:
		return False
	if not data['category']:
		return False
	if not "name" in data:
		return False
	if not data["name"]:
		return False

	# Find or create VehicleCategory
	try:
		category = VehicleCategory.objects.get(name__iexact=data["category"])
	except:
		category = VehicleCategory(name=data["category"])
		category.save()
		print "Created new VehicleCategory %s" % data["category"]

	vehicleName = data["name"].replace("&", "_and_")

	try:
		vehicle = Vehicle.objects.get(name__iexact=vehicleName)
	except:
		vehicle = Vehicle(name=vehicleName)
		print "Creating new vehicle %s" % vehicleName

	vehicle.vehicleClass = int(data["class"])
	vehicle.displayName = data["displayname"]
	vehicle.category = category
	vehicle.save()
	# ItemPorts
	portNames = []
	for port in data['ports']:
		portNames.append(port['name'].lower())

	currentPorts = ItemPort.objects.filter(parentVehicle__exact=vehicle)
	for port in currentPorts:
		if not port.name.lower() in portNames:
			print "Found stale port %s.  Removing." % port.name
			port.delete()

	ports = data["ports"]
	for port in ports:
		try:
			itemPort = ItemPort.objects.get(name__iexact=port["name"], parentVehicle__exact=vehicle)
		except:
			itemPort = ItemPort(name = port["name"])
		itemPort.displayName = port["displayname"]
		itemPort.flags = port["flags"]
		itemPort.minSize = int(port["minsize"])
		itemPort.maxSize = int(port["maxsize"])
		itemPort.name = port["name"]
		itemPort.parentVehicle = vehicle
		itemPort.save()
		for supportedType in port["types"]:
			supportedItemType = supportedType["type"]
			supportedItemSubTypes = supportedType["subtypes"]
			try:
				itemType = VehicleItemType.objects.get(typeName__iexact=supportedItemType)
			except:
				itemType = VehicleItemType(typeName=supportedItemType)
				itemType.save()
				print "Created new VehicleItemType %s" % supportedItemType
			itemPort.supportedTypes.add(itemType)
			if len(supportedItemSubTypes) > 0:
				for supportedSubType in supportedItemSubTypes:
					try:
						itemSubType = VehicleItemSubType.objects.get(subTypeName__iexact=supportedSubType)
					except:
						itemSubType = VehicleItemSubType(subTypeName = supportedSubType, parent = itemType)
						itemSubType.save()
						print "Created new VehicleItemSubType %s" % supportedSubType
					itemPort.supportedSubTypes.add(itemSubType)
			else:
				# No supported subtypes for this type, so we add all known subtypes
				allSubTypes = VehicleItemSubType.objects.filter(parent__typeName__iexact=itemType)
				for subType in allSubTypes:
					itemPort.supportedSubTypes.add(subType)					

def saveItemAttribute(item, attribute, value, newItem):
	if newItem:
		item[attribute] = value
		return

	if not value or value == '':
		return

	oldValue = item[attribute]
	if not oldValue or oldValue == '':
		addGameUpdateEntry(item, "new", "'%s' = '%s'" % (attribute, str(newValue)))
		item[attribute] = value
		return

	addGameUpdateEntry(item, "changed", "%s changed from '%s' to '%s'" % (attribute, str(newValue), str(newValue)))
	item[attribute] = value


def saveItemPortAttribute(item, itemPort, attribute, value, newPort):
	if newPort:
		itemPort[attribute] = value
		return

	if not value or value == '':
		return

	oldValue = itemPort[attribute]
	if not oldValue or oldValue == '':
		addGameUpdateEntry(item, "new", "ItemPort '%s' '%s' = '%s'" % (itemPort.name, attribute, str(newValue)))
		itemPort[attribute] = value
		return

	addGameUpdateEntry(item, "changed", "ItemPort '%s' %s changed from '%s' to '%s'" % (itemPort.name, attribute, str(newValue), str(newValue)))
	itemPort[attribute] = value


def ingestItem(dataFile, data):
	# Look for the manufacturer
	if not data['manufacturer']:
		return False
	manufacturerName = data['manufacturer'].replace('_', ' ').replace('and', '&')
	manufacturers = Manufacturer.objects.filter(name__iexact=manufacturerName)
	if len(manufacturers) == 1:
		manufacturer = manufacturers[0]
	elif len(manufacturers) == 0:
		addGameUpdateEntry(None, "new", "Manufacturer '%s'" % manufacturerName)
		print"\tCreating %s" % manufacturerName
		manufacturer = Manufacturer(name=manufacturerName)
		manufacturer.save()
	# Look to see if this item exists already
	itemName = data['name'].replace("&", "_and_")
	items = VehicleItem.objects.filter(name__iexact=itemName)
	newItem = False
	if len(items) == 0:
		# No item with this name exists, so we need to create a new one
		print "\tCreating new entry for %s" % itemName
		# Basic Item Details
		item = VehicleItem(name = itemName)
		newItem = True
	else:
		# This item already exists, so update its stats
		item = items[0]

	saveItemAttribute(item, 'itemClass', data['class'], newItem)
	# item.itemClass = data['class']
	if data['description']:
		saveItemAttribute(item, 'description', data['description'], newItem)
		# item.description = data['description']
	else:
		saveItemAttribute(item, 'description', '', newItem)
		# item.description = ''
	if data['displayname']:
		saveItemAttribute(item, 'displayName', data['displayname'], newItem)
		# item.displayName = data['displayname']
	else:
		saveItemAttribute(item, 'displayName', '', newItem)
		# item.displayName = ''
	# Look to see if the type exists already
	itemTypeName = data['itemtype']
	if itemTypeName:
		itemTypes = VehicleItemType.objects.filter(typeName__iexact=itemTypeName)
		if len(itemTypes) == 0:
			# Doesn't exist, create new item type
			itemType = VehicleItemType(typeName = itemTypeName)
			itemType.save()
			addGameUpdateEntry(None, "new", "ItemType '%s'" % itemTypeName)
		else:
			# Already existsm, use this one
			itemType = itemTypes[0]
		saveItemAttribute(item, 'itemType', itemType, newItem)
		# item.itemType = itemType
	# Look to see if the subtype exists already
	itemSubTypeName = data['itemsubtype']
	if itemSubTypeName:
		itemSubTypes = VehicleItemSubType.objects.filter(subTypeName__iexact=itemSubTypeName, parent__exact=itemType)
		if len(itemSubTypes) == 0:
			# Doesn't existm, create new item type
			itemSubType = VehicleItemSubType(subTypeName = itemSubTypeName, parent = itemType)
			itemSubType.save()
			addGameUpdateEntry(None, "new", "ItemSubType '%s'" % itemSubTypeName)
		else:
			# Already existsm, use this one
			itemSubType = itemSubTypes[0]
		saveItemAttribute(item, 'itemSubType', itemSubType, newItem)
		# item.itemSubType = itemSubType

	saveItemAttribute(item, 'manufacturer', manufacturer, newItem)
	saveItemAttribute(item, 'itemSize', data['size'], newItem)
	# item.manufacturer = manufacturer
	# item.itemSize = data['size']
	item.save()
	if newItem:
		if item.displayName != '':
			itemName = item.displayName
		else:
			itemName = item.name
		addGameUpdateEntry(item, "new", "VehicleItem '%s'" % itemName)

	# Item Params
	# Item Params take a bit more work.  For each param we need to:
	# See if the param already exists based on its NAME
	#	If it does exist, update its VALUE if needed
	#	If it does not exist, add it
	# Then, for each existing Param we need to REMOVE the ones that are no longer valid
	try:
		params = data['itemstats']
	except:
		params = None
	# Look for stale params first
	if params:
		currentParams = item.itemStats.all()
		for param in currentParams:
			if param.name not in params:
				# Found stale param
				addGameUpdateEntry(item, "removed", "VehicleItemParam '%s'" % param.name)
				print "Removing stale VehicleItemParam %s" % param.name
				param.delete()
	# Update / Add Params
	if params:
		for param in params:
			try:
				itemParam = item.ItemStats.get(name__iexact=param)
				if itemParam.value != params[param]:
					addGameUpdateEntry(item, "changed", "VehicleItemParam '%s' changed from '%s' to '%s'" % (param, str(itemParam.value), str(params[param])))
					itemParam.value = params[param]			
					itemParam.save()
			except:
				addGameUpdateEntry(item, "new", "VehicleItemParam '%s'" % param)
				itemParam = VehicleItemParam(parentItem = item, name = param, value = params[param])
				itemParam.save()

	# ItemPorts
	if "ports" in data:
		portNames = []
		for port in data['ports']:
			portNames.append(port['name'].lower())

		currentPorts = ItemPort.objects.filter(parentItem__exact=item)
		for port in currentPorts:
			if not port.name.lower() in portNames:
				print "Found stale port %s.  Removing." % port.name
				addGameUpdateEntry(item, "removed", "ItemPort '%s'" % port.name)

		ports = data["ports"]
		newPort = False
		for port in ports:
			try:
				itemPort = ItemPort.objects.get(name__iexact=port["name"], parentItem__exact=item)
			except:
				itemPort = ItemPort(name = port["name"])
				newPort = True
				addGameUpdateEntry(item, "new", "ItemPort '%s'" % port["name"])

			saveItemPortAttribute(item, itemPort, 'displayName', port["displayname"], newPort)
			saveItemPortAttribute(item, itemPort, 'flags', port["flags"], newPort)
			saveItemPortAttribute(item, itemPort, 'minSize', port["minsize"], newPort)
			saveItemPortAttribute(item, itemPort, 'maxSize', port["maxsize"], newPort)
			saveItemPortAttribute(item, itemPort, 'name', port["name"], newPort)
			# itemPort.displayName = port["displayname"]
			# itemPort.flags = port["flags"]
			# itemPort.minSize = int(port["minsize"])
			# itemPort.maxSize = int(port["maxsize"])
			# itemPort.name = port["name"]
			itemPort.parentItem = item
			itemPort.save()

			# ItemPort supported types and subtypes
			# This should probably be broken out into its own methods
			# Maybe the whole lot of these things need to be turned into classes

			# This builds up a list of type:subtype names.  If there is no specified
			# subtype, then only the type is used and this means "all" subtypes should be
			# supported.
			types = []
			for supportedType in port['types']:
				baseName = supportedType['type']
				if len(supportedType['subtypes']) > 0:
					for subtype in supportedType['subtypes']:
						name = baseName + ":" + subtype
						types.append(name)
				else:
					types.append(baseName)


			# First we need to prune out any old supported types that aren't valid anymore
			currentSupportedTypes = itemPort.supportedTypes.all()
			for supportedType in currentSupportedTypes:
				if supportedType.typeName not in port["types"]:
					# Stale supported type!
					itemPort.supportedTypes.remove(supportedType)
					addGameUpdateEntry(item, "removed", "ItemPort '%s' supportedType '%s'" % (itemPort.name, supportedType.typeName))

			for supportedType in port["types"]:
				supportedItemType = supportedType["type"]
				supportedItemSubTypes = supportedType["subtypes"]
				try:
					itemType = VehicleItemType.objects.get(typeName__iexact=supportedItemType)
				except:
					itemType = VehicleItemType(typeName=supportedItemType)
					itemType.save()
					print "Created new VehicleItemType %s" % supportedItemType
					addGameUpdateEntry(None, "new", "VehicleItemType '%s'" % supportedItemType)
				itemPort.supportedTypes.add(itemType)
				if len(supportedItemSubTypes) > 0:
					for supportedSubType in supportedItemSubTypes:
						try:
							itemSubType = VehicleItemSubType.objects.get(subTypeName__iexact=supportedSubType)
						except:
							itemSubType = VehicleItemSubType(subTypeName = supportedSubType, parent = itemType)
							itemSubType.save()
							print "Created new VehicleItemSubType %s" % supportedSubType
						itemPort.supportedSubTypes.add(itemSubType)
				else:
					# No supported subtypes for this type, so we add all known subtypes
					allSubTypes = VehicleItemSubType.objects.filter(parent__typeName__iexact=itemType)
					for subType in allSubTypes:
						itemPort.supportedSubTypes.add(subType)					
	# Power
	try:
		powerBase = data['pipes']['Power']
	except:
		powerBase = None
	if powerBase:
		itemPower = item.power.all().delete()
		for state in powerBase:
			powerEntry = VehicleItemPower()
			powerEntry.state = state
			powerEntry.value = powerBase[state]
			powerEntry.save()
			item.power.add(powerEntry)
	# Heat
	try:
		heatBase = data['pipes']['Heat']
	except:
		heatBase = None
	if heatBase:
		itemHeat = item.heat.all().delete()
		for state in heatBase:
			heatEntry = VehicleItemHeat()
			heatEntry.state = state
			heatEntry.value = heatBase[state]
			heatEntry.save()
			item.heat.add(heatEntry)
	# Avionics
	try:
		avionicsBase = data['pipes']['Avionics']
	except:
		avionicsBase = None
	if avionicsBase:
		itemAvionics = item.avionics.all().delete()
		for state in avionicsBase:
			avionicsEntry = VehicleItemAvionics()
			avionicsEntry.state = state
			avionicsEntry.value = avionicsBase[state]
			avionicsEntry.save()
			item.avionics.add(avionicsEntry)
def run(*script_args):
	gameUpdate = ingestion.GameChanges(script_args[0], script_args[1])
	DATA_PATH = script_args[2]
	allFiles = os.listdir(DATA_PATH)
	for dataFile in allFiles:
		print dataFile
		if os.path.splitext(dataFile)[-1] == '.json':
			try:
				with open(os.path.join(DATA_PATH, dataFile), 'r') as f:
					data = json.load(f)
			except:
				continue

			if "itemtype" in data:
				newItem = ingestion.VehicleItemData(gameUpdate)
				newItem.parse(data)
				newItem.checkChanges(record = True)
				newItem.saveChanges()
				# ingestItem(dataFile, data)
			else:
				newVehicle = ingestion.VehicleData(gameUpdate)
				newVehicle.parse(data)
				newVehicle.checkChanges(record = True)
				newVehicle.saveChanges()
				# ingestVehicle(dataFile, data)
