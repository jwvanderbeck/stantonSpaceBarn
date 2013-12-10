import os
import json
from shipBuilder.models import *
from django.core.exceptions import ObjectDoesNotExist

DATA_PATH = "/Users/john/Documents/SSB/Parsed Data"
dataFile = "Anvil_Hornet_F7C.json"

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
        print "Saving", newEntry
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
    
#################################################################################################################   
class ItemPortData(object):
        """
        Provides functions for ingesting an 
        ItemPort data object from the game 
        into the database, as well as recording
        any changes made from the last time the
        same object was ingested
        """
        BASIC_PROPERTIES = {
            "name" : "name",
            "displayname" : "displayName",
            "flags" : "flags",
            "minsize" : "minSize",
            "maxsize" : "maxSize"
        }
        def __init__(self, gameUpdate, parentType, parent, parentName):
            self.newModel = False
            self.gameUpdate = gameUpdate
                # "item" or "vehicle"
            self.parentType = parentType.lower()
            self.parent = parent
            self.parentName = parentName
            self.properties = {}

        def parse(self, jsonData):
            self.rawData = jsonData
            key = "name"
            if key not in self.rawData:
                return False
            # Parse all the basic properties (IE simple ones)
            for key in self.BASIC_PROPERTIES:
                if key in self.rawData:
                    self.properties[key] = self.rawData[key]
            # Some one-off code to create displayName if it isn't set
            if not self.properties["displayname"]:
                self.properties["displayname"] = self.properties["name"].replace("hardpoint_", "").replace("_", " ").title()
            # Parse more complex properties
            self.parseSupportedTypes()
            # Find existing ItemPort model object if one exists
            try:
                if self.parentType == "item":
                    self._existingModel = ItemPort.objects.get(name__iexact=self.properties["name"],parentItem__exact=self.parent)
                elif self.parentType == "vehicle":
                    self._existingModel = ItemPort.objects.get(name__iexact=self.properties["name"],parentVehicle__exact=self.parent)
            except ObjectDoesNotExist:
                self._existingModel = ItemPort()
                self.newModel = True

            return True


        def parseSupportedTypes(self):
                types = []
                for supportedType in self.rawData['types']:
                        baseName = supportedType['type'].lower()
                        if len(supportedType['subtypes']) > 0:
                                for subtype in supportedType['subtypes']:
                                        name = baseName + ":" + subtype.lower()
                                        # Look to see if this type already exists and make it if not
                                        try:
                                            typeGroup = VehicleItemType.objects.get(name__iexact=name)
                                        except ObjectDoesNotExist:
                                            typeGroup = VehicleItemType(name=name, typeName=baseName, subTypeName=subtype)
                                            typeGroup.save()
                                        types.append(typeGroup)
                        else:
                                try:
                                    typeGroup = VehicleItemType.objects.get(name__iexact=baseName)
                                except ObjectDoesNotExist:
                                    typeGroup = VehicleItemType(name=baseName, typeName=baseName)
                                    typeGroup.save()
                                types.append(typeGroup)
                self._supportedTypes = types


        def checkChanges(self, record = False):
            """
            Looks at all properties in the Data object and compares
            them against the existing saved record for any changes.
            If record = True then GameUpdate logs are recorded for the changes
            """
            # If this is a brand new ItemPort then we don't want to create
            # entries for each property
            if self.newModel:
                # Brand new ItemPort
                changeDescription = "ADDED: New ItemPort '%s'" % self.properties["displayname"]
                if record and self.gameUpdate:
                    self.gameUpdate.saveChanges(self.parentName, changeDescription)
                else:
                    print changeDescription
                return                
            # Record any individual property changes for existing ItemPort
            # Simple properties
            for key in self.properties:
                modelKey = self.BASIC_PROPERTIES[key]
                modelValue = self._existingModel.__getattribute__(modelKey)
                value = self.properties[key]
                if value != modelValue:
                    changeDescription = "CHANGED: ItemPort %s: %s changed from '%s' to '%s'" % (self.properties["displayname"], key, modelValue, value)
                    if record and self.gameUpdate:
                        self.gameUpdate.saveChanges(self.parentName, changeDescription)
                    else:
                        print changeDescription
            # Complex properties
            # Supported Types
            modelTypes = []
            currentTypes = []
            for entry in self._supportedTypes:
                currentTypes.append(entry.name)
            for entry in self._existingModel.supportedTypes.all():
                modelTypes.append(entry.name)

            currentTypes.sort()
            modelTypes.sort()
            currentStringified = ",".join(currentTypes)
            modelStringified = ",".join(modelTypes)
            if currentStringified != modelStringified:
                changeDescription = "CHANGED: ItemPort %s: supportedTypes changed from '%s' to '%s'" % (self.properties["displayname"], modelStringified, currentStringified)
                if record and self.gameUpdate:
                    self.gameUpdate.saveChanges(self.parentName, changeDescription)
                else:
                    print changeDescription



        def saveChanges(self):
            # Save parent for this port, which varies based on type
            if self.parentType == "item":
                self._existingModel.parentItem = self.parent
            elif self.parentType == "vehicle":
                self._existingModel.parentVehicle = self.parent
            # Basic properties
            for key in self.properties:
                modelKey = self.BASIC_PROPERTIES[key]
                value = self.properties[key]
                self._existingModel.__setattr__(modelKey, value)
            # Complex properties
            # Supported Types
            self._existingModel.save()
            self._existingModel.supportedTypes.clear()
            for entry in self._supportedTypes:
                self._existingModel.supportedTypes.add(entry)
            self._existingModel.save()


        def pprint(self):
            for key in self.properties:
                print key, self.properties[key]
            currentTypes = []
            for entry in self._supportedTypes:
                currentTypes.append(entry.name)
            currentTypes.sort()
            currentStringified = ",".join(currentTypes)
            print "supportedTypes", currentStringified


#################################################################################################################
class VehicleData(object):
        """
        Provides functions for ingesting a
        Vehicle data object from the game 
        into the database, as well as recording
        any changes made from the last time the
        same object was ingested
        """
        BASIC_PROPERTIES = {
            "name" : "name",
            "displayname" : "displayName",
            "class" : "vehicleClass",
            "category" : "category"
        }
        def __init__(self, gameUpdate):
            self.newModel = False
            self.gameUpdate = gameUpdate
            self.properties = {}

        def parse(self, jsonData):
            self.rawData = jsonData
            key = "name"
            if key not in self.rawData:
                return False
            # Parse all the basic properties (IE simple ones)
            for key in self.BASIC_PROPERTIES:
                if key in self.rawData:
                    self.properties[key] = self.rawData[key]
            # Find existing Vehicle model object if one exists
            try:
                self._existingModel = Vehicle.objects.get(name__iexact=self.properties["name"])
            except ObjectDoesNotExist:
                self._existingModel = Vehicle()
                self.newModel = True
            # Parse more complex properties, like ItemPorts
            self._itemPorts = []
            ips = self.rawData["ports"]
            for ip in ips:
                    # gameUpdate, parentType, parent, parentName
                    newItemPort = ItemPortData(self.gameUpdate, "vehicle", self._existingModel, self.properties["name"])
                    newItemPort.parse(ip)
                    self._itemPorts.append(newItemPort)

            return True


        def checkChanges(self, record = False):
            """
            Looks at all properties in the Data object and compares
            them against the existing saved record for any changes.
            If record = True then GameUpdate logs are recorded for the changes
            """
            # If this is a brand new Vehicle then we don't want to create
            # entries for each property
            if self.newModel:
                # Brand new Vehicle
                changeDescription = "ADDED: New Vehicle '%s'" % self.properties["displayname"]
                if record and self.gameUpdate:
                    self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                else:
                    print changeDescription
                return                
            # Record any individual property changes for existing Vehicle
            # Simple Properties
            for key in self.properties:
                modelKey = self.BASIC_PROPERTIES[key]
                modelValue = self._existingModel.__getattribute__(modelKey)
                value = self.properties[key]
                if value != modelValue:
                    changeDescription = "CHANGED: %s changed from '%s' to '%s'" % (key, modelValue, value)
                    if record and self.gameUpdate:
                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                    else:
                        print changeDescription
            # Complex properties
            # ItemPorts
            for port in self._itemPorts:
                port.checkChanges(record)


        def saveChanges(self):
            for key in self.properties:
                modelKey = self.BASIC_PROPERTIES[key]
                value = self.properties[key]
                self._existingModel.__setattr__(modelKey, value)
            self._existingModel.save()
            for port in self._itemPorts:
                port.saveChanges()
            self._existingModel.save()


        def pprint(self):
            for key in self.properties:
                print key, self.properties[key]
            for port in self._itemPorts:
                port.pprint()

#################################################################################################################
class VehicleItemData(object):
        """
        Provides functions for ingesting a
        VehicleItem data object from the game 
        into the database, as well as recording
        any changes made from the last time the
        same object was ingested
        """
        BASIC_PROPERTIES = {
            "name" : "name",
            "displayname" : "displayName",
            "class" : "itemClass",
            "description" : "description",
            "size" : "itemSize"
        }
        def __init__(self, gameUpdate):
            self.newModel = False
            self.gameUpdate = gameUpdate
            self.properties = {}

        def parse(self, jsonData):
            self.rawData = jsonData
            key = "name"
            if key not in self.rawData:
                return False
            # Parse all the basic properties (IE simple ones)
            for key in self.BASIC_PROPERTIES:
                if key in self.rawData:
                    self.properties[key] = self.rawData[key]
            # Some one-off code to create displayName if it isn't set
            if not self.properties["displayname"]:
                self.properties["displayname"] = self.properties["name"].replace("_", " ").title()
            # Find existing VehicleItem model object if one exists
            try:
                self._existingModel = VehicleItem.objects.get(name__iexact=self.properties["name"])
            except ObjectDoesNotExist:
                self._existingModel = VehicleItem()
                self.newModel = True
            # Parse more complex properties
            # Manufacturer
            self.manufacturer = self.rawData["manufacturer"]
            # ItemPorts
            if "ports" in self.rawData:
                self._itemPorts = []
                ips = self.rawData["ports"]
                for ip in ips:
                        # gameUpdate, parentType, parent, parentName
                        newItemPort = ItemPortData(self.gameUpdate, "item", self._existingModel, self.properties["name"])
                        newItemPort.parse(ip)
                        self._itemPorts.append(newItemPort)
            else:
                self._itemPorts = None
            # Type and Subtype
            self.typeGroup = self.rawData["itemtype"].lower()
            if "itemsubtype" in self.rawData and self.rawData["itemsubtype"] and self.rawData["itemsubtype"] != "":
                self.typeGroup = self.typeGroup + ":" + self.rawData["itemsubtype"].lower()
            # ItemStats
            if "itemstats" in self.rawData:
                self.itemstats = self.rawData["itemstats"]
            else:
                self.itemstats = None
            # Pipes
            # NOTE
            # Currently we are using the old system with hard coded pipes
            # for Power, Heat, and Avionics
            if "pipes" in self.rawData:
                self.pipes = {}
                pipes = self.rawData["pipes"]
                for pipe in pipes:
                    self.pipes[pipe] = pipes[pipe]
            else:
                self.pipes = None
            return True


        def checkChanges(self, record = False):
            """
            Looks at all properties in the Data object and compares
            them against the existing saved record for any changes.
            If record = True then GameUpdate logs are recorded for the changes
            """
            # If this is a brand new VehicleItem then we don't want to create
            # entries for each property
            if self.newModel:
                # Brand new VehicleItem
                changeDescription = "ADDED: New VehicleItem '%s'" % self.properties["displayname"]
                if record and self.gameUpdate:
                    self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                else:
                    print changeDescription
                return                
            # Record any individual property changes for existing VehicleItem
            # Simple Properties
            for key in self.properties:
                modelKey = self.BASIC_PROPERTIES[key]
                modelValue = self._existingModel.__getattribute__(modelKey)
                value = self.properties[key]
                if value != modelValue:
                    changeDescription = "CHANGED: %s changed from '%s' to '%s'" % (key, modelValue, value)
                    if record and self.gameUpdate:
                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                    else:
                        print changeDescription
            # Complex properties
            # Manufacturer
            try:
                modelManufacturer = Manufacturer.objects.get(name__iexact = self.manufacturer)
            except ObjectDoesNotExist:
                changeDescription = "ADDED: Manufacturer '%s'" % (self.manufacturer)
                if record and self.gameUpdate:
                    self.gameUpdate.saveChanges(None, changeDescription)
                else:
                    print changeDescription
            # ItemPorts
            if self._itemPorts:
                for port in self._itemPorts:
                    port.checkChanges(record)
            # ItemStats
            if self.itemstats:
                # check for any REMOVED stats
                modelStats = self._existingModel.vehicleitemparams_set.all()
                for stat in modelStats:
                    if stat.name not in self.itemstats:
                        changeDescription = "REMOVED: itemstat '%s' with a value of '%.02f'" % (stat.name, stat.value)
                        if record and self.gameUpdate:
                            self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                        else:
                            print changeDescription
                # check for any ADDED stats
                modelStats = self._existingModel.vehicleitemparams_set.all()
                modelStatsList = []
                for stat in modelStats:
                    modelStatsList.append(stat.name)
                for stat in self.itemstats:
                    if stat not in modelStatsList:
                        changeDescription = "ADDED: itemstat '%s' with a value of '%.02f'" % (stat, float(self.itemstats[stat]))
                        if record and self.gameUpdate:
                            self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                        else:
                            print changeDescription
                # check for CHANGED stats
                for stat in self.itemstats:
                    try:
                        modelStat = self._existingModel.vehicleitemparams_set.get(name__iexact=stat)
                    except ObjectDoesNotExist:
                        continue
                    if float(self.itemstats[stat]) != modelStat.value:
                        changeDescription = "CHANGED: itemstat %s changed from '%.02f' to '%.02f'" % (stat, modelStat.value, float(self.itemstats[stat]))
                        if record and self.gameUpdate:
                            self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                        else:
                            print changeDescription
            # TypeGroup
            if self.typeGroup != self._existingModel.itemType.name:
                changeDescription = "CHANGED: itemType changed from '%s' to '%s'" % (self._existingModel.itemType.name, self.typeGroup)
                if record and self.gameUpdate:
                    self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                else:
                    print changeDescription
            # Pipes are a real pain!
            # For each PIPE we need to see if its new, or removed and in each pipe we need to check
            # the STATES for added, removed, or changed
            # Check for removed pipes
            # This bit is pretty hard coded for now until switch to the new generic system (if that happens!)
            # Power
            if self.pipes:
                modelPowerObjects = VehicleItemPower.objects.filter(parentItem__exact = self._existingModel)
                if len(modelPowerObjects) > 0 and "Power" not in self.pipes:
                    changeDescription = "REMOVED: VehicleItemPipe 'Power'"
                    if record and self.gameUpdate:
                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                    else:
                        print changeDescription
                # Heat
                modelHeatObjects = VehicleItemHeat.objects.filter(parentItem__exact = self._existingModel)
                if len(modelHeatObjects) > 0 and "Heat" not in self.pipes:
                    changeDescription = "REMOVED: VehicleItemPipe 'Heat'"
                    if record and self.gameUpdate:
                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                    else:
                        print changeDescription
                # Avionics
                modelAvionicsObjects = VehicleItemAvionics.objects.filter(parentItem__exact = self._existingModel)
                if len(modelAvionicsObjects) > 0 and "Avionics" not in self.pipes:
                    changeDescription = "REMOVED: VehicleItemPipe 'Avionics'"
                    if record and self.gameUpdate:
                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                    else:
                        print changeDescription

                for pipe in self.pipes:
                    if pipe.lower() == "power":
                        modelPowerObjects = VehicleItemPower.objects.filter(parentItem__exact = self._existingModel)
                        if len(modelPowerObjects) == 0:
                            changeDescription = "ADDED: VehicleItemPipe '%s'" % (pipe)
                            if record and self.gameUpdate:
                                self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                            else:
                                print changeDescription
                        else:
                            # The pipe is in the old model, so we need to check STATES for new, removed, changed
                            modelStates = []
                            for entry in modelPowerObjects:
                                modelStates.append(entry.state)
                                if entry.state not in self.pipes[pipe]:
                                    # State exists in the model but not the new data, so this is REMOVED
                                    changeDescription = "REMOVED: VehicleItemPipe '%s' state '%s'" % (pipe, entry.state)
                                    if record and self.gameUpdate:
                                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                    else:
                                        print changeDescription
                                else:
                                    # State is in both the old model and the new data, look to see
                                    # if it is different
                                    modelValue = entry.value
                                    dataValue = self.pipes[pipe][entry.state]
                                    if modelValue != dataValue:
                                        changeDescription = "CHANGED: VehicleItemPipe '%s' state '%s' changed from '%s' to '%s'" % (pipe, entry.state, modelValue, dataValue)
                                        if record and self.gameUpdate:
                                            self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                        else:
                                            print changeDescription
                            modelStates.sort()
                            for state in self.pipes[pipe]:
                                if state not in modelStates:
                                    changeDescription = "ADDED: VehicleItemPipe '%s' state '%s'" % (self.pipes[pipe], state)
                                    if record and self.gameUpdate:
                                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                    else:
                                        print changeDescription
                    if pipe.lower() == "heat":
                        modelPowerObjects = VehicleItemHeat.objects.filter(parentItem__exact = self._existingModel)
                        if len(modelPowerObjects) == 0:
                            changeDescription = "ADDED: VehicleItemPipe '%s'" % (pipe)
                            if record and self.gameUpdate:
                                self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                            else:
                                print changeDescription
                        else:
                            # The pipe is in the old model, so we need to check STATES for new, removed, changed
                            modelStates = []
                            for entry in modelPowerObjects:
                                modelStates.append(entry.state)
                                if entry.state not in self.pipes[pipe]:
                                    # State exists in the model but not the new data, so this is REMOVED
                                    changeDescription = "REMOVED: VehicleItemPipe '%s' state '%s'" % (pipe, entry.state)
                                    if record and self.gameUpdate:
                                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                    else:
                                        print changeDescription
                                else:
                                    # State is in both the old model and the new data, look to see
                                    # if it is different
                                    modelValue = entry.value
                                    dataValue = self.pipes[pipe][entry.state]
                                    if modelValue != dataValue:
                                        changeDescription = "CHANGED: VehicleItemPipe '%s' state '%s' changed from '%s' to '%s'" % (pipe, entry.state, modelValue, dataValue)
                                        if record and self.gameUpdate:
                                            self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                        else:
                                            print changeDescription
                            modelStates.sort()
                            for state in self.pipes[pipe]:
                                if state not in modelStates:
                                    changeDescription = "ADDED: VehicleItemPipe '%s' state '%s'" % (self.pipes[pipe], state)
                                    if record and self.gameUpdate:
                                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                    else:
                                        print changeDescription
                    if pipe.lower() == "avionics":
                        modelPowerObjects = VehicleItemAvionics.objects.filter(parentItem__exact = self._existingModel)
                        if len(modelPowerObjects) == 0:
                            changeDescription = "ADDED: VehicleItemPipe '%s'" % (pipe)
                            if record and self.gameUpdate:
                                self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                            else:
                                print changeDescription
                        else:
                            # The pipe is in the old model, so we need to check STATES for new, removed, changed
                            modelStates = []
                            for entry in modelPowerObjects:
                                modelStates.append(entry.state)
                                if entry.state not in self.pipes[pipe]:
                                    # State exists in the model but not the new data, so this is REMOVED
                                    changeDescription = "REMOVED: VehicleItemPipe '%s' state '%s'" % (pipe, entry.state)
                                    if record and self.gameUpdate:
                                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                    else:
                                        print changeDescription
                                else:
                                    # State is in both the old model and the new data, look to see
                                    # if it is different
                                    modelValue = entry.value
                                    dataValue = self.pipes[pipe][entry.state]
                                    if modelValue != dataValue:
                                        changeDescription = "CHANGED: VehicleItemPipe '%s' state '%s' changed from '%s' to '%s'" % (pipe, entry.state, modelValue, dataValue)
                                        if record and self.gameUpdate:
                                            self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                        else:
                                            print changeDescription
                            modelStates.sort()
                            for state in self.pipes[pipe]:
                                if state not in modelStates:
                                    changeDescription = "ADDED: VehicleItemPipe '%s' state '%s'" % (self.pipes[pipe], state)
                                    if record and self.gameUpdate:
                                        self.gameUpdate.saveChanges(self.properties["name"], changeDescription)
                                    else:
                                        print changeDescription


        def saveChanges(self):
            for key in self.properties:
                modelKey = self.BASIC_PROPERTIES[key]
                value = self.properties[key]
                self._existingModel.__setattr__(modelKey, value)
            self._existingModel.save()
            # Manufacturer
            try:
                modelManufacturer = Manufacturer.objects.get(name__iexact = self.manufacturer)
            except ObjectDoesNotExist:
                modelManufacturer = Manufacturer(name = self.manufacturer)
                modelManufacturer.save()
            # ItemPorts
            if self._itemPorts:
                for port in self._itemPorts:
                    port.saveChanges()
                self._existingModel.save()
            # ItemStats
            if self.itemstats:
                for stat in self.itemstats:
                    try:
                        param = self._existingModel.vehicleitemparams_set.get(name__iexact=stat)
                        param.value = self.itemstats[stat]
                        param.save()
                    except ObjectDoesNotExist:
                        param = VehicleItemParams(name = stat, value = self.itemstats[stat], parentItem = self._existingModel)
                        param.save()
                for param in self._existingModel.vehicleitemparams_set.all():
                    if param.name not in self.itemstats:
                        param.delete()
            # TypeGroup
            try:
                itemType, itemSubType = self.typeGroup.split(":")
            except ValueError:
                itemType = self.typeGroup
                itemSubType = ""
            try:
                typeGroup = VehicleItemType.objects.get(name__iexact = self.typeGroup)
            except ObjectDoesNotExist:
                typeGroup = VehicleItemType(name = self.typeGroup, typeName = itemType, subTypeName = itemSubType)
                typeGroup.save()
            self._existingModel.itemType = typeGroup
            self._existingModel.save()
            # Pipes
            # This isn't the best way to do this, as it will cause long term
            # database fragmentation, but pipes are such a pain in the ass to
            # do properly, so i'm being lazy.  In the grand scheme of things
            # I don't think it will be a huge problem.  And if it is I can
            # revist this
            if self.pipes:
                self._existingModel.vehicleitempower_set.all().delete()
                self._existingModel.vehicleitemheat_set.all().delete()
                self._existingModel.vehicleitemavionics_set.all().delete()
                for pipe in self.pipes:
                    if pipe.lower() == "power":
                        for state in self.pipes[pipe]:
                            stateEntry = VehicleItemPower(parentItem = self._existingModel, state = state, value = self.pipes[pipe][state])
                            stateEntry.save()
                    elif pipe.lower() == "heat":
                        for state in self.pipes[pipe]:
                            stateEntry = VehicleItemHeat(parentItem = self._existingModel, state = state, value = self.pipes[pipe][state])
                            stateEntry.save()
                    elif pipe.lower() == "avionics":
                        for state in self.pipes[pipe]:
                            stateEntry = VehicleItemAvionics(parentItem = self._existingModel, state = state, value = self.pipes[pipe][state])
                            stateEntry.save()




        def pprint(self):
            for key in self.properties:
                print key, self.properties[key]
            for port in self._itemPorts:
                port.pprint()


#################################################################################################################
def readData(path, dataFile):
    try:
        with open(os.path.join(path, dataFile), 'r') as f:
                data = json.load(f)
    except:
        print "ERROR: Failed to parse file %s" % os.path.join(path, dataFile)
        data = None

    return data
