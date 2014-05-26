import os
import json
import pprint
from collections import OrderedDict
from shipBuilder.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

IMAGE_WIDTH = 1000.0
IMAGE_HEIGHT = 1000.0
MARKER_RADIUS = 10.0
CORNER_RADIUS = 10.0

def process(rawData):
    try:
        vehicleData = Vehicle.objects.get(name__iexact=rawData["vehicleName"])
        ports = vehicleData.ports.all()
    except ObjectDoesNotExist:
        print "No Vehicle matching name=%s" % rawData["vehicleName"]
        return
    print "Importing DataTags for Vehicle %s" % rawData["vehicleName"]
    try:
        image = vehicleData.vehicleimage_set.get(name__iexact=rawData["imageName"], ship=vehicleData)
        image.ship = vehicleData
        image.url = "https://www.stantonspacebarn.com/static/images/orthos/" + rawData["vehicleName"].lower() + "/" + rawData["imageName"].lower() + ".png"
        image.save()        
    except ObjectDoesNotExist:
        print "VehicleImage %s does not exist.  Creating." % (rawData["imageName"])
        image = VehicleImage(name=rawData["imageName"], ship=vehicleData, url="https://www.stantonspacebarn.com/static/images/orthos/" + rawData["vehicleName"].lower() + "/" + rawData["imageName"].lower() + ".png")
        image.save()
    HardpointTag.objects.filter(parentImage=image).delete()
    for key in rawData["hardpoints"]:
        hardpoint = None
        for port in ports:
            if port.name == key:
                hardpoint = port
        if not hardpoint:
            print "Failed to find matching ItemPort for %s.  Skipping." % key
            continue
        tag = HardpointTag(parentImage=image, disabled=False, hardpoint=hardpoint)
        tagX = ((int(rawData["hardpoints"][key]["tag"][0])-MARKER_RADIUS) / IMAGE_WIDTH) * 100.0
        tagY = ((int(rawData["hardpoints"][key]["tag"][1])) / IMAGE_HEIGHT) * 100.0
        datablockX = ((int(rawData["hardpoints"][key]["datablock"][0])-CORNER_RADIUS) / IMAGE_WIDTH) * 100.0
        datablockY = ((int(rawData["hardpoints"][key]["datablock"][1])) / IMAGE_HEIGHT) * 100.0
        tag.tagX = tagX
        tag.tagY = tagY
        tag.datablockX = datablockX
        tag.datablockY = datablockY
        print "Creating Hardpoint Tag for hardpoint %s at %.2f,%.2f" % (hardpoint.name, tagX, tagY)
        print "Datablock at %.2f,%.2f" % (datablockX, datablockY)
        tag.save()





def readData(path, dataFile):
    with open(os.path.join(path, dataFile), 'r') as f:
            data = json.load(f)
    return data

def run(*script_args):
    DATA_PATH = script_args[0]
    try:
        DATA_FILE = script_args[1]
    except:
        DATA_FILE = None

    if DATA_FILE:
        if os.path.splitext(DATA_FILE)[-1] == '.json':
            try:
                rawData = readData(DATA_PATH, DATA_FILE)
            except:
                print "Error parsing file"
            process(rawData)
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
                process(rawData)
