from rest_framework import serializers
from shipBuilder.models import *

class WithPkMixin(object):
    def get_pk_field(self, model_field):
        return self.get_field(model_field)

class ManufacturerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Manufacturer
		
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        
class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant

class ItemPortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPort

class VehicleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleItem
