from django.contrib import admin

# Register your models here.
from shipBuilder.models import *

admin.site.register(Manufacturer)

admin.site.register(VehicleItem)
admin.site.register(VehicleItemParams)
admin.site.register(VehicleItemPower)
admin.site.register(VehicleItemHeat)
admin.site.register(VehicleItemAvionics)
admin.site.register(Vehicle)
admin.site.register(ItemPort)
admin.site.register(VehicleCategory)
admin.site.register(VehicleItemType)
admin.site.register(VehicleImage)
admin.site.register(HardpointTag)

admin.site.register(GameUpdate)
admin.site.register(GameUpdateChange)
