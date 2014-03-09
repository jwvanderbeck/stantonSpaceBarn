from shipBuilder.models import *
from shipBuilder.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse

class ManufacturerList(generics.ListAPIView):
	queryset = Manufacturer.objects.all()
	serializer_class = ManufacturerSerializer

class ManufacturerDetail(generics.RetrieveAPIView):
	queryset = Manufacturer.objects.all()
	serializer_class = ManufacturerSerializer
	
# class VehicleList(generics.ListAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer
# 
# class VehicleDetail(generics.RetrieveAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer

class VehicleItemList(generics.ListAPIView):
    queryset = VehicleItem.objects.all()
    serializer_class = VehicleItemSerializer

class VehicleItemDetail(generics.RetrieveAPIView):
    queryset = VehicleItem.objects.all()
    serializer_class = VehicleItemSerializer

# class ItemPortList(generics.ListAPIView):
#     queryset = ItemPort.objects.all()
#     serializer_class = ItemPortSerializer
# 
# class ItemPortDetail(generics.RetrieveAPIView):
#     queryset = ItemPort.objects.all()
#     serializer_class = ItemPortSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'manufacturers': reverse('manufacturer-list', request=request, format=format),
    })


# @api_view(('GET',))
# def vehicleItemList(request, format=None):
#     if request.method == 'GET':
#         vehicleItems = VehicleItem.objects.all()
#         data = []
#         for vehicleItem in vehicleItems:
#             vehicleItemData = {
#                 "id" : vehicleItem.id,
#                 "itemClass" : vehicleItem.itemClass,
#                 "name" : vehicleItem.name,
#                 "displayName" : vehicleItem.displayName,
#                 "itemSize" : vehicleItem.itemSize,
#                 "description" : vehicleItem.description
#             }
#             if vehicleItem.manufacturer:
#                 vehicleItemData['manufacturer'] = vehicleItem.manufacturer.name
#             if vehicleItem.itemType:
#                 vehicleItemData['itemType'] = vehicleItem.itemType.name

#             stats = VehicleItemParams.objects.filter(parentItem__exact=vehicleItem)
#             vehicleItemData["itemStats"] = []
#             for stat in stats:
#                 vehicleItemData["itemStats"].append( {stat.name : stat.value} )
            
#             data.append(vehicleItemData)
#         return Response(data)

@api_view(('GET',))
def vehicleItemList(request, format=None):
    # provider_key = '9e875d96b2e006b1a4b6066beb6bd88a'
    # app_id = '744b4bbf'
    # app_key = '5332ca71f6c95528aa4cebf4d776d313'
    if request.method == 'GET':
        # client = ThreeScalePY.ThreeScaleAuthRep(provider_key)
        # if client.authrep(app_id, app_key):
        vehicleItems = VehicleItem.objects.all()
        data = []
        for vehicleItem in vehicleItems:
            vehicleItemData = {
                "id" : vehicleItem.id,
                # "itemClass" : vehicleItem.itemClass,
                "name" : vehicleItem.name,
                "displayName" : vehicleItem.displayName,
                # "itemSize" : vehicleItem.itemSize,
                "description" : vehicleItem.description
            }
            # if vehicleItem.manufacturer:
            #     vehicleItemData['manufacturer'] = vehicleItem.manufacturer.name
            # if vehicleItem.itemType:
            #     vehicleItemData['itemType'] = vehicleItem.itemType.typeName
            # if vehicleItem.itemSubType:
            #     vehicleItemData['itemSubType'] = vehicleItem.itemSubType.subTypeName

            # stats = vehicleItem.itemStats.all()
            # vehicleItemData["itemStats"] = []
            # for stat in stats:
            #     vehicleItemData["itemStats"].append( {stat.name : stat.value} )

            data.append(vehicleItemData)
        return Response(data)
        # else:
        #     return Response({"reason" : client.build_response().get_reason()}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(('GET',))
def vehicleItemDetail(request, pk, format=None):
    if request.method == 'GET':
        vehicleItem = VehicleItem.objects.get(pk=pk)
        vehicleItemData = {
            "id" : vehicleItem.id,
            "itemClass" : vehicleItem.itemClass,
            "name" : vehicleItem.name,
            "displayName" : vehicleItem.displayName,
            "itemSize" : vehicleItem.itemSize,
            "description" : vehicleItem.description
        }
        if vehicleItem.manufacturer:
            vehicleItemData['manufacturer'] = vehicleItem.manufacturer.name
        if vehicleItem.itemType:
            vehicleItemData['itemType'] = vehicleItem.itemType.name

            stats = VehicleItemParams.objects.filter(parentItem__exact=vehicleItem)
        vehicleItemData["itemStats"] = []
        for stat in stats:
            vehicleItemData["itemStats"].append( {stat.name : stat.value} )
            
        return Response(vehicleItemData)


@api_view(('GET',))
def vehicleList(request, format=None):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        data = []
        for vehicle in vehicles:
            vehicleData = {
                "id" : vehicle.id,
                # "vehicleClass" : vehicle.vehicleClass,
                "name" : vehicle.name,
                "displayName" : vehicle.displayName,
                # "upgradeSlots" : vehicle.upgradeSlots,
                # "maximumCrew" : vehicle.maximum_crew,
                # "emptyMass" : vehicle.empty_mass,
                # "length" : vehicle.length,
                # "width" : vehicle.width,
                # "height" : vehicle.height
            }
            # if vehicle.category:
            #     vehicleData['category'] = vehicle.category
            # if vehicle.manufacturer:
            #     vehicleData['manufacturer'] = vehicle.manufacturer.name
            
            data.append(vehicleData)
        return Response(data)
@api_view(('GET',))
def vehicleDetail(request, pk, format=None):
    if request.method == 'GET':
        vehicle = Vehicle.objects.get(pk=pk)
        vehicleData = {
            "id" : vehicle.id,
            "vehicleClass" : vehicle.vehicleClass,
            "name" : vehicle.name,
            "displayName" : vehicle.displayName,
            "upgradeSlots" : vehicle.upgradeSlots,
            "maximumCrew" : vehicle.maximum_crew,
            "emptyMass" : vehicle.empty_mass,
            "length" : vehicle.length,
            "width" : vehicle.width,
            "height" : vehicle.height
        }
        if vehicle.category:
            vehicleData['category'] = vehicle.category
        if vehicle.manufacturer:
            vehicleData['manufacturer'] = vehicle.manufacturer.name

        return Response(vehicleData)

@api_view(('GET',))
def itemPortList(request, format=None):
    if request.method == 'GET':
        itemPorts = ItemPort.objects.all()
        data = []
        for itemPort in itemPorts:
            port = {}
            port["id"] = itemPort.id
            port["displayName"] = itemPort.displayName
            port["name"] = itemPort.name
            # port["maxSize"] = itemPort.maxSize
            # port["minSize"] = itemPort.minSize
            # port["portClass"] = itemPort.portClass
            # port['supportedTypes'] = []
            # for itemType in itemPort.supportedTypes.all():
            #     port['supportedTypes'].append(itemType.name)
            data.append(port)
        return Response(data)
@api_view(('GET',))
def itemPortDetail(request, pk, format=None):
    if request.method == 'GET':
        itemPort = ItemPort.objects.get(pk=pk)
        port = {}
        port["id"] = itemPort.id
        port["displayName"] = itemPort.displayName
        port["name"] = itemPort.name
        port["maxSize"] = itemPort.maxSize
        port["minSize"] = itemPort.minSize
        port["portClass"] = itemPort.portClass
        port['supportedTypes'] = []
        for itemType in itemPort.supportedTypes.all():
            port['supportedTypes'].append(itemType.name)
        return Response(port)

@api_view(('GET',))
def itemPortListByVehicle(request, pk, format=None):
    if request.method == 'GET':
        itemPorts = ItemPort.objects.filter(parentVehicle__exact=pk)
        data = []
        for itemPort in itemPorts:
            port = {}
            port["id"] = itemPort.id
            port["displayName"] = itemPort.displayName
            port["name"] = itemPort.name
            port["maxSize"] = itemPort.maxSize
            port["minSize"] = itemPort.minSize
            port["portClass"] = itemPort.portClass
            port['supportedSubTypes'] = []
            supported = []
            # For each supported ItemType
            for itemType in itemPort.supportedTypes.all():
                # Look for supported ItemSubType with that parent, and add those found
                supportedSubTypes = itemPort.supportedSubTypes.all().filter(parent__exact=itemType)
                if len(supportedSubTypes) == 0:
                    # if none found, add ALL itemSubType with that parent
                    supportedSubTypes = VehicleItemSubType.objects.all().filter(parent__exact=itemType)
                supported.extend(supportedSubTypes)
            for subType in supported:
                port['supportedSubTypes'].append(subType.subTypeName)
            data.append(port)
        return Response(data)        


@api_view(('GET',))
def itemTypeList(request, format=None):
    if request.method == 'GET':
        itemTypes = VehicleItemType.objects.all()
        data = []
        for itemType in itemTypes:
            typeData = {}
            typeData["id"] = itemType.id
            typeData["name"] = itemType.name
            typeData["typeName"] = itemType.typeName
            typeData["subTypeName"] = itemType.subTypeName
            data.append(typeData)
        return Response(data)

# @api_view(['GET'])
# def hardpointListByClass(request, hardpoint_class, format=None):
#   if request.method == 'GET':
#       hardpoints = Hardpoint.objects.filter(hardpoint_class__exact=hardpoint_class)
#       serializer = HardpointSerializer(hardpoints, many=True)
#       return Response(serializer.data)
# 
# @api_view(['GET'])
# def itemsForHardpoint(request, hardpoint_id, format=None):
#   if request.method == 'GET':
#       hardpoint_class = Hardpoint.objects.get(pk=hardpoint_id).hardpoint_class
#       items = Item.objects.filter(hardpoint_class__gte=hardpoint_class)
#       serializer = ItemSerializer(items, many=True)
#       return Response(serializer.data)


# @api_view(['GET'])
# def manufacturer_detail(request, pk, format=None):
# 	try:
# 		manufacturer = Manufacturer.objects.get(pk=pk)
# 	except Manufacturer.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = ManufacturerSerializer(manufacturer)
# 		return Response(serializer.data)
