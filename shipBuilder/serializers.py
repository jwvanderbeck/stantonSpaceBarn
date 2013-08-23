from rest_framework import serializers
from shipBuilder.models import *

class WithPkMixin(object):
    def get_pk_field(self, model_field):
        return self.get_field(model_field)

class ManufacturerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Manufacturer

class HardpointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hardpoint

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item

class ItemCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemCategory

class ShipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ship

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image

class BuildSerializer(serializers.ModelSerializer):
	class Meta:
		model = Build
