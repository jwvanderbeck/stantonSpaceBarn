from django.contrib import admin

# Register your models here.
from shipBuilder.models import *

admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemType)
admin.site.register(Manufacturer)
admin.site.register(Ship)
admin.site.register(Hardpoint)
admin.site.register(Build)
admin.site.register(Image)
admin.site.register(BuildHardpoint)
admin.site.register(BuildHullMod)
admin.site.register(BuildEngineMod)
admin.site.register(WeaponData)
admin.site.register(CargoModData)
admin.site.register(PowerplantData)
admin.site.register(ThrusterData)
admin.site.register(ShieldData)
admin.site.register(EngineIntakeData)