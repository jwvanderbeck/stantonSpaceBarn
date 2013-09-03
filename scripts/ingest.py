import os, sys, json, argparse

from shipBuilder.models import VehicleItem
from shipBuilder.models import VehicleItemParams, VehicleItemPower, VehicleItemHeat, VehicleItemAvionics
from shipBuilder.models import VehicleItemType, VehicleItemSubType
from shipBuilder.models import Manufacturer

# This script reads in the JSON files produced from scraping the Star Citizen game data, and creates 
# or updates the data in the shipBuilder database

# parser = argparse.ArgumentParser()
# parser.add_argument('source')
# args = parser.parse_args()
# if args.source:
# 	DATA_PATH = args.source
# else:
DATA_PATH = "/Users/john/Documents/SSB/Parsed Data"
# DATA_PATH = "/home/jwvanderbecks/sc_parsed_data"

# Ingest Weapons
allFiles = os.listdir(DATA_PATH)
for dataFile in allFiles:
	# print dataFile
	if os.path.splitext(dataFile)[-1] == '.json':
		try:
			with open(os.path.join(DATA_PATH, dataFile), 'r') as f:
				data = json.load(f)
		except:
			continue

		if not "itemtype" in data:
			continue
		# if data['itemtype'] != "Weapon":
		# 	continue

		# Look for the manufacturer
		if not data['manufacturer']:
			continue
		print "Processing %s" % dataFile	
		manufacturerName = data['manufacturer'].replace('_', ' ').replace('and', '&')
		manufacturers = Manufacturer.objects.filter(name__iexact=manufacturerName)
		if len(manufacturers) == 1:
			print "\tFound %s" % manufacturerName
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
			print "\tUpdating stats on %s" % itemName
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

