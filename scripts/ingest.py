import os, sys, json, argparse

from shipBuilder.models import Vehicle, VehicleItem
import scripts.ingestion as ingestion


def run(*script_args):
	items = []
	vehicles = []
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
				items.append(data["name"])
				newItem = ingestion.VehicleItemData(gameUpdate)
				newItem.parse(data)
				newItem.checkChanges(record = True)
				newItem.saveChanges()
				# ingestItem(dataFile, data)
			else:
				vehicles.append(data["name"])
				newVehicle = ingestion.VehicleData(gameUpdate)
				newVehicle.parse(data)
				newVehicle.checkChanges(record = True)
				newVehicle.saveChanges()
				# ingestVehicle(dataFile, data)
	for itemData in VehicleItem.objects.filter(disabled__exact=False):
		if itemData.name not in items:
			print "Found stale item named %s.  Marking as disabled." % itemData.name
			itemData.disabled = True
			itemData.save()
	for vehicleData in Vehicle.objects.filter(available=True):
		if vehicleData.name not in vehicles:
			print "Found stale vehicle named %s.  Marking as disabled." % vehicleData.name
			vehicleData.available = False
			vehicleData.save()
