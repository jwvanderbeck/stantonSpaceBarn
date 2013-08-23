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


class HardpointList(generics.ListAPIView):
	queryset = Hardpoint.objects.all()
	serializer_class = HardpointSerializer

class HardpointDetail(generics.RetrieveAPIView):
	queryset = Hardpoint.objects.all()
	serializer_class = HardpointSerializer

class ItemList(generics.ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemCategoryList(generics.ListAPIView):
	queryset = ItemCategory.objects.all()
	serializer_class = ItemCategorySerializer

class ItemCategoryDetail(generics.RetrieveAPIView):
	queryset = ItemCategory.objects.all()
	serializer_class = ItemCategorySerializer

class ShipList(generics.ListAPIView):
	queryset = Ship.objects.all()
	serializer_class = ShipSerializer

class ShipDetail(generics.RetrieveAPIView):
	queryset = Ship.objects.all()
	serializer_class = ShipSerializer


class ImageList(generics.ListAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveAPIView):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer

class BuildList(generics.ListAPIView):
	queryset = Build.objects.all()
	serializer_class = BuildSerializer

class BuildDetail(generics.RetrieveAPIView):
	queryset = Build.objects.all()
	serializer_class = BuildSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'manufacturers': reverse('manufacturer-list', request=request, format=format),
        'hardpoints': reverse('hardpoint-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format),
        'itemcategories': reverse('itemcategory-list', request=request, format=format),
        'ships': reverse('ship-list', request=request, format=format),
        'images': reverse('image-list', request=request, format=format),
        'builds': reverse('build-list', request=request, format=format),
    })


@api_view(['GET'])
def hardpointListByClass(request, hardpoint_class, format=None):
	if request.method == 'GET':
		hardpoints = Hardpoint.objects.filter(hardpoint_class__exact=hardpoint_class)
		serializer = HardpointSerializer(hardpoints, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def itemsForHardpoint(request, hardpoint_id, format=None):
	if request.method == 'GET':
		hardpoint_class = Hardpoint.objects.get(pk=hardpoint_id).hardpoint_class
		items = Item.objects.filter(hardpoint_class__gte=hardpoint_class)
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data)


# @api_view(['GET'])
# def manufacturer_detail(request, pk, format=None):
# 	try:
# 		manufacturer = Manufacturer.objects.get(pk=pk)
# 	except Manufacturer.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = ManufacturerSerializer(manufacturer)
# 		return Response(serializer.data)
