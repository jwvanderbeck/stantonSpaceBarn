
# The basic concept here is that we have an Update method which sits between the Django model and the JSON data from Star Citizen.
# All data changes go through the Update method, and it determines what changes are being made and logs them
# This greatly simplifies hundreds of lines of code, and makes it all much more manageable

import os
import json
import pprint
from collections import OrderedDict
from shipBuilder.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

PROCESSED_MODEL = {}
# CLASS_LOOKUP allows us to associate a json key with the actual model class
CLASS_LOOKUP = {
    "ammoData": "Ammo",
    "vehicleDamageParam": "VehicleDamageParam",
    "itemType" : "VehicleItemType",
    "manufacturer" : "Manufacturer",
    "itemStats" : "ItemStat",
    "weaponData" : "Weapon",
    "fireModes": "Firemode",
    "supportedAmmo": "Ammo",
    "turretData": "Turret",
    "ports": "ItemPort",
    "supportedTypes": "VehicleItemType",
    "pipeHeat": "VehicleItemHeat",
    "pipePower": "VehicleItemPower",
    "pipeAvionics": "VehicleItemAvionics",
    "thrusterData": "Thruster",
    "gimbalData": "Gimbal",
    "armorData": "Armor",
    "batteryData": "Battery",
    "radarData": "Radar",
    "shieldData": "Shield",
    "vehicleMissileParam": "VehicleMissileParam",
    "vehicleMissileGuidanceParam": "VehicleMissileGuidanceParam",
    "ammo": "Ammo",
    "signatures": "Signature",
    "damageMultipliers": "DamageMultiplier"
}


#################################################################################################################
class GameChanges(object):
    """
    Helper class used by the ingestion classes 
    to record any changes into the GameUpdate log.
    """
    def __init__(self, module, build):
        self._module = module
        self._build = build
        # Look for existing GameUpdate for this module and build, or make a new one if neccesary
        updateName = "%s Module - Build %s" % (module, build)
        try:
            self._record = GameUpdate.objects.get(name__iexact=updateName)
        except:
            self._record = GameUpdate(name=updateName, module=module, build=build)
            self._record.save()
            print "Creating new GameUpdate", self._record

    def saveChanges(self, entity, description):
        update = self._record
        newEntry = GameUpdateChange(description=description, entityName=entity, update=update)
        print description
        newEntry.save()

    @property
    def record(self):
        return self._record
    @record.setter
    def record(self, value):
        self._record = value
    
    @property
    def module(self):
        return self._module
    @module.setter
    def module(self, value):
        self._module = value

    @property
    def build(self):
        return self._build
    @build.setter
    def build(self, value):
        self._build = value

def readData(path, dataFile):
    with open(os.path.join(path, dataFile), 'r') as f:
            data = json.load(f)
    return data

def tabOut(depth):
    for i in range(0, depth):
        print "\t",

def recordDelete(path, name, modelName, gameUpdate):
    description = "REMOVED: %s %s removed existing instance of %s"  % (" -> ".join(path), name, modelName)
    gameUpdate.saveChanges(name, description)

def recordCreate(path, name, modelName, gameUpdate):
    description = "ADDED: %s %s added instance of %s"  % (" -> ".join(path), name, modelName)
    gameUpdate.saveChanges(name, description)

def recordChange(path, name, attributeName, oldValue, newValue, gameUpdate):
    description = "CHANGED: %s %s attribute %s. OLD: %s, NEW: %s" % (" -> ".join(path), name, attributeName, oldValue, newValue)
    gameUpdate.saveChanges(name, description)

def updateModelInstance(dataset, attributeName, rootModel, path, name, gameUpdate):
    # Setup
    if not attributeName:
        try:
            attributeName = dataset["_modelname"]
        except:
            return
    modelName = CLASS_LOOKUP[attributeName]
    if not dataset or len(dataset) == 0:
        noData = True
    else:
        noData = False
    if rootModel.__getattribute__(attributeName) == None:
        noModel = True
    else:
        noModel = False
    # print "[DEBUG]attributeName is %s of type %s" % (attributeName, type(rootModel.__getattribute__(attributeName)))
    if noModel:
        modelType = "m2o"
    elif isinstance(rootModel.__getattribute__(attributeName), models.manager.Manager):
        modelType = "m2m"
    else:
        modelType = "m2o"
    # CASE 1: No data in either place.  Early drop out.
    if noData and noModel:
        # print "CASE 1"
        return None
    # CASE 2: Data exists in both places, so we are all set
    if modelType == "m2o" and not noData and not noModel:
        # print "CASE 2"
        if "_reuse" in dataset and dataset["_reuse"]:
            searchField = dataset["_searchfield"]
            if rootModel.__getattribute__(attributeName).__getattribute__(searchField) != dataset[searchField]:
                recordCreate(path, name, modelName, gameUpdate)
                newInstance = globals()[modelName]()
                newInstance.save()
                rootModel.__setattr__(attributeName, newInstance)
                rootModel.save()
        return rootModel.__getattribute__(attributeName)
    elif modelType == "m2m":
        # print "CASE 2"
        # print "[DEBUG]Looking for M2M model instance"
        allObjects = rootModel.__getattribute__(attributeName).all()
        searchField = dataset["_searchfield"]
        if allObjects:
            for obj in allObjects:
                if obj.__getattribute__(searchField) == dataset[searchField]:
                    # print "[DEBUG]Returning M2M Instance:", obj
                    return obj
    # CASE 3: Underlying data in Databse, but not in JSON - Delete Database entries
    if noData:
        # print "CASE 3"
        if modelType == "m2m":
            rootModel.__getattribute__(attributeName).all().delete()
            rootModel.__getattribute__(attributeName).clear()
        elif modelType == "m2o":
            rootModel.__getattribute__(attributeName).delete()
            rootModel.__setattr__(attributeName, None)
            recordDelete(path, name, modelName, gameUpdate)
            return None
    # CASE 4: No data in underlying Database, but data is in JSON - Create neccesary entries
    createNew = True
    if modelType == "m2o":
        allObjects = globals()[modelName].objects.all()
    elif modelType == "m2m":
        if "_global" in dataset and dataset["_global"]:
            allObjects = globals()[modelName].objects.all()
        else:
            allObjects = rootModel.__getattribute__(attributeName).all()
    if "_reuse" in dataset and dataset["_reuse"]:
        # print "CASE 4"
        searchField = dataset["_searchfield"]
        print "[DEBUG]Attempting to reuse model with key %s of %s" % (searchField, dataset[searchField])
        if allObjects:
            for obj in allObjects:
                # print "%s=%s" % (obj.__getattribute__(searchField), dataset[searchField])
                if obj.__getattribute__(searchField) == dataset[searchField]:
                    instance = obj
                    createNew = False
                    break
    if createNew:
        # print "CASE 4"
        recordCreate(path, name, modelName, gameUpdate)
        instance = globals()[modelName]()
        instance.save()
    if modelType == "m2o":
        # print "CASE 4"
        rootModel.__setattr__(attributeName, instance)
    elif modelType == "m2m":
        # print "CASE 4"
        rootModel.__getattribute__(attributeName).add(instance)
    rootModel.save()
    return instance

def updateValue(dataset, attributeName, rootModel, path, name, gameUpdate):
    attributeValue = rootModel.__getattribute__(attributeName)
    if attributeValue != dataset:
        # print "[DEBUG]Updating Value for model %s %s" % (type(rootModel), rootModel)
        # print dataset
        recordChange(path, name, attributeName, attributeValue, dataset, gameUpdate)
        rootModel.__setattr__(attributeName, dataset)
        rootModel.save()

def processModel(node, rootModel, name, path, gameUpdate):
    # print "Processing model", " -> ".join(path)
    # print "RootModel: %s, of type %s" % (rootModel, type(rootModel))
    if isinstance(node, dict):
        for key in node:
            if isinstance(node[key], dict): 
                newPath = path[:]
                m2m = False
                try:
                    m2m = node[key]["_m2m"]
                    print "M2M = True"
                except:
                    m2m = False
                if not m2m:
                    newPath.append(key)
                newRootModel = updateModelInstance(node[key], key, rootModel, newPath, name, gameUpdate)
                if newRootModel:
                    processModel(node[key], newRootModel, name, newPath, gameUpdate)
            elif isinstance(node[key], list):
                newPath = path[:]
                # newRootModel = updateModelInstance(node[key], key, rootModel, newPath, name, gameUpdate)
                processModel(node[key], rootModel, name, newPath, gameUpdate)
            else:
                if key.startswith("_"):
                    continue
                updateValue(node[key], key, rootModel, path, name, gameUpdate)
    elif isinstance(node, list):
        for key in node:
            if isinstance(key, dict):
                if "_m2m" in key:
                    newPath = path[:]
                    newPath.append(key["_modelname"])
                    newRootModel = updateModelInstance(key, key["_modelname"], rootModel, newPath, name, gameUpdate)
                    processModel(key, newRootModel, name, newPath, gameUpdate)


def run(*script_args):
    gameUpdate = GameChanges(script_args[0], script_args[1])
    DATA_PATH = script_args[2]
    if len(script_args) == 4:
        dataFile = script_args[3]
        print dataFile
        if os.path.splitext(dataFile)[-1] == '.json':
            try:
                rawData = readData(DATA_PATH, dataFile)
            except:
                print "Error parsing file"

            if "itemType" in rawData:
                try:
                    model = VehicleItem.objects.get(name__iexact=rawData["name"])
                except ObjectDoesNotExist:
                    model = VehicleItem(name=rawData["name"])
                    model.save()
                # print "Processing VehicleItem %s" % rawData["name"]
                processModel(rawData, model, rawData["name"], ["VehicleItem"], gameUpdate)

            else:
                try:
                    model = Vehicle.objects.get(name__iexact=rawData["name"])
                except ObjectDoesNotExist:
                    model = Vehicle(name=rawData["name"])
                    model.save()
                # print "Processing Vehicle %s" % rawData["name"]
                processModel(rawData, model, rawData["name"], ["Vehicle"], gameUpdate)
    else:
        allFiles = os.listdir(DATA_PATH)
        for dataFile in allFiles:
            print dataFile
            if os.path.splitext(dataFile)[-1] == '.json':
                try:
                    rawData = readData(DATA_PATH, dataFile)
                except:
                    print "Error parsing file"
                    continue

                if "itemType" in rawData:
                    try:
                        model = VehicleItem.objects.get(name__iexact=rawData["name"])
                    except ObjectDoesNotExist:
                        model = VehicleItem(name=rawData["name"])
                        model.save()
                    # print "Processing VehicleItem %s" % rawData["name"]
                    processModel(rawData, model, rawData["name"], ["VehicleItem"], gameUpdate)

                else:
                    try:
                        model = Vehicle.objects.get(name__iexact=rawData["name"])
                    except ObjectDoesNotExist:
                        model = Vehicle(name=rawData["name"])
                        model.save()
                    # print "Processing Vehicle %s" % rawData["name"]
                    processModel(rawData, model, rawData["name"], ["Vehicle"], gameUpdate)





