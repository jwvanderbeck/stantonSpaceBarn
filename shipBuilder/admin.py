from django.contrib import admin

# Register your models here.
from shipBuilder.models import *

admin.site.register(Manufacturer)

admin.site.register(VehicleItem)

admin.site.register(Weapon)
admin.site.register(Ammo)
admin.site.register(Armor)
admin.site.register(Battery)
admin.site.register(Radar)
admin.site.register(Shield)
admin.site.register(Gimbal)
admin.site.register(Thruster)
admin.site.register(Turret)

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

admin.site.register(VehicleDamageParam)
admin.site.register(VehicleMissileParam)
admin.site.register(VehicleMissileGuidanceParam)


admin.site.register(GameUpdate)
admin.site.register(GameUpdateChange)

admin.site.register(Variant)
admin.site.register(VariantItem)

