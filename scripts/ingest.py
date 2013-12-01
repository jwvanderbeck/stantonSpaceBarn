import os, sys, json, argparse

from shipBuilder.models import VehicleItem
from shipBuilder.models import VehicleItemParams, VehicleItemPower, VehicleItemHeat, VehicleItemAvionics
from shipBuilder.models import VehicleItemType, VehicleItemSubType
from shipBuilder.models import Manufacturer
from shipBuilder.models import Vehicle, ItemPort, VehicleCategory

# This script reads in the JSON files produced from scraping the Star Citizen game data, and creates 
# or updates the data in the shipBuilder database

# parser = argparse.ArgumentParser()
# parser.add_argument('source')
# args = parser.parse_args()
# if args.source:
# 	DATA_PATH = args.source
# else:
DATA_PATH = "/Users/john/Documents/SSB/Parsed Data"
# DATA_PATH = "/home/jwvanderbeck/sc_parsed_data"

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

def ingestItem(dataFile, data):
	# Look for the manufacturer
	if not data['manufacturer']:
		return False
	manufacturerName = data['manufacturer'].replace('_', ' ').replace('and', '&')
	manufacturers = Manufacturer.objects.filter(name__iexact=manufacturerName)
	if len(manufacturers) == 1:
		manufacturer = manufacturers[0]
	elif len(manufacturers) == 0:
		print"\tCreating %s" % manufacturerName
		manufacturer = Manufacturer(name=manufacturerName)
		manufacturer.save()
	# Look to see if this item exists already
	itemName = data['name'].replace("&", "_and_")
	items = VehicleItem.objects.filter(name__iexact=itemName)
	if len(items) == 0:
		# No item with this name exists, so we need to create a new one
		print "\tCreating new entry for %s" % itemName
		# Basic Item Details
		item = VehicleItem()
	else:
		# This item already exists, so update its stats
		item = items[0]

	item.name = itemName
	item.itemClass = data['class']
	if data['description']:
		item.description = data['description']
	else:
		item.description = ''
	if data['displayname']:
		item.displayName = data['displayname']
	else:
		item.displayName = ''
	# Look to see if the type exists already
	itemTypeName = data['itemtype']
	if itemTypeName:
		itemTypes = VehicleItemType.objects.filter(typeName__iexact=itemTypeName)
		if len(itemTypes) == 0:
			# Doesn't existm, create new item type
			itemType = VehicleItemType(typeName = itemTypeName)
			itemType.save()
		else:
			# Already existsm, use this one
			itemType = itemTypes[0]
		item.itemType = itemType
	# Look to see if the subtype exists already
	itemSubTypeName = data['itemsubtype']
	if itemSubTypeName:
		itemSubTypes = VehicleItemSubType.objects.filter(subTypeName__iexact=itemSubTypeName, parent__exact=itemType)
		if len(itemSubTypes) == 0:
			# Doesn't existm, create new item type
			itemSubType = VehicleItemSubType(subTypeName = itemSubTypeName, parent = itemType)
			itemSubType.save()
		else:
			# Already existsm, use this one
			itemSubType = itemSubTypes[0]
		item.itemSubType = itemSubType

	item.manufacturer = manufacturer
	item.itemSize = data['size']
	item.save()
	# Item Params
	try:
		params = data['itemstats']
	except:
		params = None
	if params:
		itemParams = item.itemStats.all().delete()
		for key in params:
			itemParam = VehicleItemParams()
			itemParam.name = key
			itemParam.value = params[key]
			itemParam.save()
			item.itemStats.add(itemParam)

	# ItemPorts
	if "ports" in data:
		portNames = []
		for port in data['ports']:
			portNames.append(port['name'].lower())

		currentPorts = ItemPort.objects.filter(parentItem__exact=item)
		for port in currentPorts:
			if not port.name.lower() in portNames:
				print "Found stale port %s.  Removing." % port.name

		ports = data["ports"]
		for port in ports:
			try:
				itemPort = ItemPort.objects.get(name__iexact=port["name"], parentItem__exact=item)
			except:
				itemPort = ItemPort(name = port["name"])
			itemPort.displayName = port["displayname"]
			itemPort.flags = port["flags"]
			itemPort.minSize = int(port["minsize"])
			itemPort.maxSize = int(port["maxsize"])
			itemPort.name = port["name"]
			itemPort.parentItem = item
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
			ingestItem(dataFile, data)
		else:
			ingestVehicle(dataFile, data)
