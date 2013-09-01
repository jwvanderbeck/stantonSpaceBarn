import os, sys, json

from shipBuilder.models import VehicleItem, VehicleItemParams, VehicleItemPower, VehicleItemHeat, VehicleItemAvionics
from shipBuilder.models import Manufacturer

# This script reads in the JSON files produced from scraping the Star Citizen game data, and creates 
# or updates the data in the shipBuilder database

DATA_PATH = "/Users/john/Documents/SSB/Parsed Data"
# Ingest Weapons
allFiles = os.listdir(DATA_PATH)
for dataFile in allFiles:
	if os.path.splitext(dataFile)[-1] == '.json':
		try:
			with open(os.path.join(DATA_PATH, dataFile), 'r') as f:
				data = json.load(f)
		except:
			continue

		if not "itemtype" in data:
			continue
		if data['itemtype'] != "Weapon":
			continue

		if not "pipes" in data:
			continue
		if not "itemstats" in data:
			continue

		if len(data['itemstats']) == 0:
			continue

		print "Processing %s" % dataFile	
		# Look for the manufacturer
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
		itemName = data['name']
		items = VehicleItem.objects.filter(name__iexact=itemName)
		save = False
		if len(items) == 0:
			# No item with this name exists, so we need to create a new one
			print "\tCreating new entry for %s" % itemName
			# Basic Item Details
			item = VehicleItem()
			save = False
		else:
			# This item already exists, so update its stats
			print "\tUpdating stats on %s" % itemName
			item = items[0]
			save = False

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
		item.itemType = data['itemtype']
		item.itemSubType = data['itemsubtype']
		item.manufacturer = manufacturer
		item.itemSize = data['size']
		item.save()
		# Item Params
		params = data['itemstats']
		for key in params:
			itemParam = VehicleItemParams()
			itemParam.name = key
			itemParam.value = params[key]
			itemParam.save()
			item.itemStats.add(itemParam)
		# Power
		powerBase = data['pipes']['Power']
		for state in powerBase:
			powerEntry = VehicleItemPower()
			powerEntry.state = state
			powerEntry.value = powerBase[state]
			powerEntry.save()
			item.power.add(powerEntry)
		# Heat
		heatBase = data['pipes']['Heat']
		for state in heatBase:
			heatEntry = VehicleItemHeat()
			heatEntry.state = state
			heatEntry.value = heatBase[state]
			heatEntry.save()
			item.heat.add(heatEntry)
		# Avionics
		avionicsBase = data['pipes']['Avionics']
		for state in avionicsBase:
			avionicsEntry = VehicleItemAvionics()
			avionicsEntry.state = state
			avionicsEntry.value = avionicsBase[state]
			avionicsEntry.save()
			item.avionics.add(avionicsEntry)
		
		# DEBUG
		print item