#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript shipBuilder
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script

from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    # You probably want to uncomment on of these two lines
    # @transaction.atomic  # Django 1.6
    # @transaction.commit_on_success  # Django <1.6
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        #you will probably want to call this method from save_or_locate()
        #example:
        #new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        #You may change this function to do specific lookup for specific objects
        #
        #original_class class of the django orm's object that needs to be located
        #original_pk_name the primary key of original_class
        #the_class      parent class of original_class which contains obj_content
        #pk_name        the primary key of original_class
        #pk_value       value of the primary_key
        #obj_content    content of the object which was not exported.
        #
        #you should use obj_content to locate the object on the target db
        #
        #and example where original_class and the_class are different is
        #when original_class is Farmer and
        #the_class is Person. The table may refer to a Farmer but you will actually
        #need to locate Person in order to instantiate that Farmer
        #
        #example:
        #if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #    pk_name="name"
        #    pk_value=obj_content[pk_name]
        #if the_class == StaffGroup:
        #    pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        #change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    #we need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    #has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    if str(e) == "No module named import_helper":
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    #initial imports

    #Processing model: Manufacturer

    from shipBuilder.models import Manufacturer

    shipBuilder_manufacturer_1 = Manufacturer()
    shipBuilder_manufacturer_1.name = u'Origin Jumpworks'
    shipBuilder_manufacturer_1.description = u''
    shipBuilder_manufacturer_1 = importer.save_or_locate(shipBuilder_manufacturer_1)

    shipBuilder_manufacturer_2 = Manufacturer()
    shipBuilder_manufacturer_2.name = u'Behring'
    shipBuilder_manufacturer_2.description = u''
    shipBuilder_manufacturer_2 = importer.save_or_locate(shipBuilder_manufacturer_2)

    shipBuilder_manufacturer_3 = Manufacturer()
    shipBuilder_manufacturer_3.name = u'Klaus & Werner'
    shipBuilder_manufacturer_3.description = u''
    shipBuilder_manufacturer_3 = importer.save_or_locate(shipBuilder_manufacturer_3)

    shipBuilder_manufacturer_4 = Manufacturer()
    shipBuilder_manufacturer_4.name = u'Talon'
    shipBuilder_manufacturer_4.description = u''
    shipBuilder_manufacturer_4 = importer.save_or_locate(shipBuilder_manufacturer_4)

    shipBuilder_manufacturer_5 = Manufacturer()
    shipBuilder_manufacturer_5.name = u'A&R'
    shipBuilder_manufacturer_5.description = u''
    shipBuilder_manufacturer_5 = importer.save_or_locate(shipBuilder_manufacturer_5)

    shipBuilder_manufacturer_6 = Manufacturer()
    shipBuilder_manufacturer_6.name = u'Roberts Space Industries'
    shipBuilder_manufacturer_6.description = u''
    shipBuilder_manufacturer_6 = importer.save_or_locate(shipBuilder_manufacturer_6)

    shipBuilder_manufacturer_7 = Manufacturer()
    shipBuilder_manufacturer_7.name = u'Tyler D-Tech'
    shipBuilder_manufacturer_7.description = u''
    shipBuilder_manufacturer_7 = importer.save_or_locate(shipBuilder_manufacturer_7)

    shipBuilder_manufacturer_8 = Manufacturer()
    shipBuilder_manufacturer_8.name = u'Dragon Stellar'
    shipBuilder_manufacturer_8.description = u''
    shipBuilder_manufacturer_8 = importer.save_or_locate(shipBuilder_manufacturer_8)

    shipBuilder_manufacturer_9 = Manufacturer()
    shipBuilder_manufacturer_9.name = u'Gorgon Defender'
    shipBuilder_manufacturer_9.description = u''
    shipBuilder_manufacturer_9 = importer.save_or_locate(shipBuilder_manufacturer_9)

    shipBuilder_manufacturer_10 = Manufacturer()
    shipBuilder_manufacturer_10.name = u'ACOM'
    shipBuilder_manufacturer_10.description = u''
    shipBuilder_manufacturer_10 = importer.save_or_locate(shipBuilder_manufacturer_10)

    shipBuilder_manufacturer_11 = Manufacturer()
    shipBuilder_manufacturer_11.name = u'Hammer Propulsion'
    shipBuilder_manufacturer_11.description = u''
    shipBuilder_manufacturer_11 = importer.save_or_locate(shipBuilder_manufacturer_11)

    shipBuilder_manufacturer_12 = Manufacturer()
    shipBuilder_manufacturer_12.name = u'Wei-Tek'
    shipBuilder_manufacturer_12.description = u''
    shipBuilder_manufacturer_12 = importer.save_or_locate(shipBuilder_manufacturer_12)

    shipBuilder_manufacturer_13 = Manufacturer()
    shipBuilder_manufacturer_13.name = u'Gangleri'
    shipBuilder_manufacturer_13.description = u''
    shipBuilder_manufacturer_13 = importer.save_or_locate(shipBuilder_manufacturer_13)

    shipBuilder_manufacturer_14 = Manufacturer()
    shipBuilder_manufacturer_14.name = u'Alliance Startech'
    shipBuilder_manufacturer_14.description = u''
    shipBuilder_manufacturer_14 = importer.save_or_locate(shipBuilder_manufacturer_14)

    shipBuilder_manufacturer_15 = Manufacturer()
    shipBuilder_manufacturer_15.name = u'Juno Starwerk'
    shipBuilder_manufacturer_15.description = u''
    shipBuilder_manufacturer_15 = importer.save_or_locate(shipBuilder_manufacturer_15)

    shipBuilder_manufacturer_16 = Manufacturer()
    shipBuilder_manufacturer_16.name = u'Ace Astrogation'
    shipBuilder_manufacturer_16.description = u''
    shipBuilder_manufacturer_16 = importer.save_or_locate(shipBuilder_manufacturer_16)

    shipBuilder_manufacturer_17 = Manufacturer()
    shipBuilder_manufacturer_17.name = u'Groupe Nouveau Paradigme'
    shipBuilder_manufacturer_17.description = u''
    shipBuilder_manufacturer_17 = importer.save_or_locate(shipBuilder_manufacturer_17)

    shipBuilder_manufacturer_18 = Manufacturer()
    shipBuilder_manufacturer_18.name = u'Lightning'
    shipBuilder_manufacturer_18.description = u''
    shipBuilder_manufacturer_18 = importer.save_or_locate(shipBuilder_manufacturer_18)

    shipBuilder_manufacturer_19 = Manufacturer()
    shipBuilder_manufacturer_19.name = u'X-Forge'
    shipBuilder_manufacturer_19.description = u''
    shipBuilder_manufacturer_19 = importer.save_or_locate(shipBuilder_manufacturer_19)

    shipBuilder_manufacturer_20 = Manufacturer()
    shipBuilder_manufacturer_20.name = u'OKB Voshkod'
    shipBuilder_manufacturer_20.description = u''
    shipBuilder_manufacturer_20 = importer.save_or_locate(shipBuilder_manufacturer_20)

    shipBuilder_manufacturer_21 = Manufacturer()
    shipBuilder_manufacturer_21.name = u'ArcCorp'
    shipBuilder_manufacturer_21.description = u''
    shipBuilder_manufacturer_21 = importer.save_or_locate(shipBuilder_manufacturer_21)

    shipBuilder_manufacturer_22 = Manufacturer()
    shipBuilder_manufacturer_22.name = u'Seal'
    shipBuilder_manufacturer_22.description = u''
    shipBuilder_manufacturer_22 = importer.save_or_locate(shipBuilder_manufacturer_22)

    shipBuilder_manufacturer_23 = Manufacturer()
    shipBuilder_manufacturer_23.name = u'Beijing'
    shipBuilder_manufacturer_23.description = u''
    shipBuilder_manufacturer_23 = importer.save_or_locate(shipBuilder_manufacturer_23)

    shipBuilder_manufacturer_24 = Manufacturer()
    shipBuilder_manufacturer_24.name = u'Stor-All'
    shipBuilder_manufacturer_24.description = u''
    shipBuilder_manufacturer_24 = importer.save_or_locate(shipBuilder_manufacturer_24)

    shipBuilder_manufacturer_25 = Manufacturer()
    shipBuilder_manufacturer_25.name = u'J-Span'
    shipBuilder_manufacturer_25.description = u''
    shipBuilder_manufacturer_25 = importer.save_or_locate(shipBuilder_manufacturer_25)

    shipBuilder_manufacturer_26 = Manufacturer()
    shipBuilder_manufacturer_26.name = u'Tarsus'
    shipBuilder_manufacturer_26.description = u''
    shipBuilder_manufacturer_26 = importer.save_or_locate(shipBuilder_manufacturer_26)

    shipBuilder_manufacturer_27 = Manufacturer()
    shipBuilder_manufacturer_27.name = u'Anvil Aerospace'
    shipBuilder_manufacturer_27.description = u''
    shipBuilder_manufacturer_27 = importer.save_or_locate(shipBuilder_manufacturer_27)

    shipBuilder_manufacturer_28 = Manufacturer()
    shipBuilder_manufacturer_28.name = u'L-Sys'
    shipBuilder_manufacturer_28.description = u''
    shipBuilder_manufacturer_28 = importer.save_or_locate(shipBuilder_manufacturer_28)

    shipBuilder_manufacturer_29 = Manufacturer()
    shipBuilder_manufacturer_29.name = u'Greycat Industrial'
    shipBuilder_manufacturer_29.description = u''
    shipBuilder_manufacturer_29 = importer.save_or_locate(shipBuilder_manufacturer_29)

    shipBuilder_manufacturer_30 = Manufacturer()
    shipBuilder_manufacturer_30.name = u'Max Ox'
    shipBuilder_manufacturer_30.description = u''
    shipBuilder_manufacturer_30 = importer.save_or_locate(shipBuilder_manufacturer_30)

    shipBuilder_manufacturer_31 = Manufacturer()
    shipBuilder_manufacturer_31.name = u'Gallenson Tactical'
    shipBuilder_manufacturer_31.description = u''
    shipBuilder_manufacturer_31 = importer.save_or_locate(shipBuilder_manufacturer_31)

    shipBuilder_manufacturer_32 = Manufacturer()
    shipBuilder_manufacturer_32.name = u'KnightBridge Arms'
    shipBuilder_manufacturer_32.description = u''
    shipBuilder_manufacturer_32 = importer.save_or_locate(shipBuilder_manufacturer_32)

    shipBuilder_manufacturer_33 = Manufacturer()
    shipBuilder_manufacturer_33.name = u'Aegis Dynamics'
    shipBuilder_manufacturer_33.description = u''
    shipBuilder_manufacturer_33 = importer.save_or_locate(shipBuilder_manufacturer_33)

    shipBuilder_manufacturer_34 = Manufacturer()
    shipBuilder_manufacturer_34.name = u'MISC'
    shipBuilder_manufacturer_34.description = u''
    shipBuilder_manufacturer_34 = importer.save_or_locate(shipBuilder_manufacturer_34)

    shipBuilder_manufacturer_35 = Manufacturer()
    shipBuilder_manufacturer_35.name = u'Kruger Intergalactic'
    shipBuilder_manufacturer_35.description = u''
    shipBuilder_manufacturer_35 = importer.save_or_locate(shipBuilder_manufacturer_35)

    #Processing model: ItemCategory

    from shipBuilder.models import ItemCategory

    shipBuilder_itemcategory_1 = ItemCategory()
    shipBuilder_itemcategory_1.description = u'Gun'
    shipBuilder_itemcategory_1 = importer.save_or_locate(shipBuilder_itemcategory_1)

    shipBuilder_itemcategory_2 = ItemCategory()
    shipBuilder_itemcategory_2.description = u'Missile Launcher'
    shipBuilder_itemcategory_2 = importer.save_or_locate(shipBuilder_itemcategory_2)

    shipBuilder_itemcategory_3 = ItemCategory()
    shipBuilder_itemcategory_3.description = u'Utility'
    shipBuilder_itemcategory_3 = importer.save_or_locate(shipBuilder_itemcategory_3)

    shipBuilder_itemcategory_4 = ItemCategory()
    shipBuilder_itemcategory_4.description = u'Hull Mod'
    shipBuilder_itemcategory_4 = importer.save_or_locate(shipBuilder_itemcategory_4)

    shipBuilder_itemcategory_5 = ItemCategory()
    shipBuilder_itemcategory_5.description = u'Engine Mod'
    shipBuilder_itemcategory_5 = importer.save_or_locate(shipBuilder_itemcategory_5)

    shipBuilder_itemcategory_6 = ItemCategory()
    shipBuilder_itemcategory_6.description = u'Main Thruster'
    shipBuilder_itemcategory_6 = importer.save_or_locate(shipBuilder_itemcategory_6)

    shipBuilder_itemcategory_7 = ItemCategory()
    shipBuilder_itemcategory_7.description = u'Powerplant'
    shipBuilder_itemcategory_7 = importer.save_or_locate(shipBuilder_itemcategory_7)

    shipBuilder_itemcategory_8 = ItemCategory()
    shipBuilder_itemcategory_8.description = u'Cargo Expansion'
    shipBuilder_itemcategory_8 = importer.save_or_locate(shipBuilder_itemcategory_8)

    shipBuilder_itemcategory_9 = ItemCategory()
    shipBuilder_itemcategory_9.description = u'Shield'
    shipBuilder_itemcategory_9 = importer.save_or_locate(shipBuilder_itemcategory_9)

    shipBuilder_itemcategory_10 = ItemCategory()
    shipBuilder_itemcategory_10.description = u'Turret'
    shipBuilder_itemcategory_10 = importer.save_or_locate(shipBuilder_itemcategory_10)

    #Processing model: ItemType

    from shipBuilder.models import ItemType

    shipBuilder_itemtype_1 = ItemType()
    shipBuilder_itemtype_1.name = u'Weapons'
    shipBuilder_itemtype_1.hardpoint_type = True
    shipBuilder_itemtype_1 = importer.save_or_locate(shipBuilder_itemtype_1)

    shipBuilder_itemtype_2 = ItemType()
    shipBuilder_itemtype_2.name = u'Utility Items'
    shipBuilder_itemtype_2.hardpoint_type = True
    shipBuilder_itemtype_2 = importer.save_or_locate(shipBuilder_itemtype_2)

    shipBuilder_itemtype_3 = ItemType()
    shipBuilder_itemtype_3.name = u'Hull Mod'
    shipBuilder_itemtype_3.hardpoint_type = False
    shipBuilder_itemtype_3 = importer.save_or_locate(shipBuilder_itemtype_3)

    shipBuilder_itemtype_4 = ItemType()
    shipBuilder_itemtype_4.name = u'Engine Mod'
    shipBuilder_itemtype_4.hardpoint_type = False
    shipBuilder_itemtype_4 = importer.save_or_locate(shipBuilder_itemtype_4)

    #Processing model: WeaponData

    from shipBuilder.models import WeaponData

    shipBuilder_weapondata_1 = WeaponData()
    shipBuilder_weapondata_1.rate_of_fire = 0.0
    shipBuilder_weapondata_1.explosive_radius = 0.0
    shipBuilder_weapondata_1.missile_count = 2L
    shipBuilder_weapondata_1.damage = 0.0
    shipBuilder_weapondata_1.velocity = 0.0
    shipBuilder_weapondata_1 = importer.save_or_locate(shipBuilder_weapondata_1)

    shipBuilder_weapondata_2 = WeaponData()
    shipBuilder_weapondata_2.rate_of_fire = 0.0
    shipBuilder_weapondata_2.explosive_radius = 0.0
    shipBuilder_weapondata_2.missile_count = 4L
    shipBuilder_weapondata_2.damage = 0.0
    shipBuilder_weapondata_2.velocity = 0.0
    shipBuilder_weapondata_2 = importer.save_or_locate(shipBuilder_weapondata_2)

    shipBuilder_weapondata_3 = WeaponData()
    shipBuilder_weapondata_3.rate_of_fire = 0.0
    shipBuilder_weapondata_3.explosive_radius = 0.0
    shipBuilder_weapondata_3.missile_count = 4L
    shipBuilder_weapondata_3.damage = 0.0
    shipBuilder_weapondata_3.velocity = 0.0
    shipBuilder_weapondata_3 = importer.save_or_locate(shipBuilder_weapondata_3)

    shipBuilder_weapondata_4 = WeaponData()
    shipBuilder_weapondata_4.rate_of_fire = 0.0
    shipBuilder_weapondata_4.explosive_radius = 0.0
    shipBuilder_weapondata_4.missile_count = 2L
    shipBuilder_weapondata_4.damage = 0.0
    shipBuilder_weapondata_4.velocity = 0.0
    shipBuilder_weapondata_4 = importer.save_or_locate(shipBuilder_weapondata_4)

    shipBuilder_weapondata_5 = WeaponData()
    shipBuilder_weapondata_5.rate_of_fire = 0.0
    shipBuilder_weapondata_5.explosive_radius = 0.0
    shipBuilder_weapondata_5.missile_count = 8L
    shipBuilder_weapondata_5.damage = 0.0
    shipBuilder_weapondata_5.velocity = 0.0
    shipBuilder_weapondata_5 = importer.save_or_locate(shipBuilder_weapondata_5)

    #Processing model: PowerplantData

    from shipBuilder.models import PowerplantData

    shipBuilder_powerplantdata_1 = PowerplantData()
    shipBuilder_powerplantdata_1.powerplant_class = 2L
    shipBuilder_powerplantdata_1.power_rating = 100.0
    shipBuilder_powerplantdata_1 = importer.save_or_locate(shipBuilder_powerplantdata_1)

    shipBuilder_powerplantdata_2 = PowerplantData()
    shipBuilder_powerplantdata_2.powerplant_class = 2L
    shipBuilder_powerplantdata_2.power_rating = 150.0
    shipBuilder_powerplantdata_2 = importer.save_or_locate(shipBuilder_powerplantdata_2)

    shipBuilder_powerplantdata_3 = PowerplantData()
    shipBuilder_powerplantdata_3.powerplant_class = 1L
    shipBuilder_powerplantdata_3.power_rating = 75.0
    shipBuilder_powerplantdata_3 = importer.save_or_locate(shipBuilder_powerplantdata_3)

    shipBuilder_powerplantdata_4 = PowerplantData()
    shipBuilder_powerplantdata_4.powerplant_class = 2L
    shipBuilder_powerplantdata_4.power_rating = 200.0
    shipBuilder_powerplantdata_4 = importer.save_or_locate(shipBuilder_powerplantdata_4)

    shipBuilder_powerplantdata_5 = PowerplantData()
    shipBuilder_powerplantdata_5.powerplant_class = 3L
    shipBuilder_powerplantdata_5.power_rating = 300.0
    shipBuilder_powerplantdata_5 = importer.save_or_locate(shipBuilder_powerplantdata_5)

    shipBuilder_powerplantdata_6 = PowerplantData()
    shipBuilder_powerplantdata_6.powerplant_class = 3L
    shipBuilder_powerplantdata_6.power_rating = 375.0
    shipBuilder_powerplantdata_6 = importer.save_or_locate(shipBuilder_powerplantdata_6)

    shipBuilder_powerplantdata_7 = PowerplantData()
    shipBuilder_powerplantdata_7.powerplant_class = 3L
    shipBuilder_powerplantdata_7.power_rating = 350.0
    shipBuilder_powerplantdata_7 = importer.save_or_locate(shipBuilder_powerplantdata_7)

    shipBuilder_powerplantdata_8 = PowerplantData()
    shipBuilder_powerplantdata_8.powerplant_class = 4L
    shipBuilder_powerplantdata_8.power_rating = 425.0
    shipBuilder_powerplantdata_8 = importer.save_or_locate(shipBuilder_powerplantdata_8)

    shipBuilder_powerplantdata_9 = PowerplantData()
    shipBuilder_powerplantdata_9.powerplant_class = 4L
    shipBuilder_powerplantdata_9.power_rating = 400.0
    shipBuilder_powerplantdata_9 = importer.save_or_locate(shipBuilder_powerplantdata_9)

    shipBuilder_powerplantdata_10 = PowerplantData()
    shipBuilder_powerplantdata_10.powerplant_class = 5L
    shipBuilder_powerplantdata_10.power_rating = 500.0
    shipBuilder_powerplantdata_10 = importer.save_or_locate(shipBuilder_powerplantdata_10)

    shipBuilder_powerplantdata_11 = PowerplantData()
    shipBuilder_powerplantdata_11.powerplant_class = 6L
    shipBuilder_powerplantdata_11.power_rating = 600.0
    shipBuilder_powerplantdata_11 = importer.save_or_locate(shipBuilder_powerplantdata_11)

    shipBuilder_powerplantdata_12 = PowerplantData()
    shipBuilder_powerplantdata_12.powerplant_class = 1L
    shipBuilder_powerplantdata_12.power_rating = 25.0
    shipBuilder_powerplantdata_12 = importer.save_or_locate(shipBuilder_powerplantdata_12)

    shipBuilder_powerplantdata_13 = PowerplantData()
    shipBuilder_powerplantdata_13.powerplant_class = 4L
    shipBuilder_powerplantdata_13.power_rating = 400.0
    shipBuilder_powerplantdata_13 = importer.save_or_locate(shipBuilder_powerplantdata_13)

    #Processing model: ThrusterData

    from shipBuilder.models import ThrusterData

    shipBuilder_thrusterdata_1 = ThrusterData()
    shipBuilder_thrusterdata_1.thrust_generated = 300.0
    shipBuilder_thrusterdata_1.thrust_rating = 3L
    shipBuilder_thrusterdata_1 = importer.save_or_locate(shipBuilder_thrusterdata_1)

    shipBuilder_thrusterdata_2 = ThrusterData()
    shipBuilder_thrusterdata_2.thrust_generated = 325.0
    shipBuilder_thrusterdata_2.thrust_rating = 3L
    shipBuilder_thrusterdata_2 = importer.save_or_locate(shipBuilder_thrusterdata_2)

    shipBuilder_thrusterdata_3 = ThrusterData()
    shipBuilder_thrusterdata_3.thrust_generated = 400.0
    shipBuilder_thrusterdata_3.thrust_rating = 4L
    shipBuilder_thrusterdata_3 = importer.save_or_locate(shipBuilder_thrusterdata_3)

    shipBuilder_thrusterdata_4 = ThrusterData()
    shipBuilder_thrusterdata_4.thrust_generated = 200.0
    shipBuilder_thrusterdata_4.thrust_rating = 2L
    shipBuilder_thrusterdata_4 = importer.save_or_locate(shipBuilder_thrusterdata_4)

    shipBuilder_thrusterdata_5 = ThrusterData()
    shipBuilder_thrusterdata_5.thrust_generated = 500.0
    shipBuilder_thrusterdata_5.thrust_rating = 5L
    shipBuilder_thrusterdata_5 = importer.save_or_locate(shipBuilder_thrusterdata_5)

    shipBuilder_thrusterdata_6 = ThrusterData()
    shipBuilder_thrusterdata_6.thrust_generated = 100.0
    shipBuilder_thrusterdata_6.thrust_rating = 1L
    shipBuilder_thrusterdata_6 = importer.save_or_locate(shipBuilder_thrusterdata_6)

    #Processing model: ShieldData

    from shipBuilder.models import ShieldData

    shipBuilder_shielddata_1 = ShieldData()
    shipBuilder_shielddata_1.absorption = 100.0
    shipBuilder_shielddata_1 = importer.save_or_locate(shipBuilder_shielddata_1)

    shipBuilder_shielddata_2 = ShieldData()
    shipBuilder_shielddata_2.absorption = 600.0
    shipBuilder_shielddata_2 = importer.save_or_locate(shipBuilder_shielddata_2)

    shipBuilder_shielddata_3 = ShieldData()
    shipBuilder_shielddata_3.absorption = 500.0
    shipBuilder_shielddata_3 = importer.save_or_locate(shipBuilder_shielddata_3)

    shipBuilder_shielddata_4 = ShieldData()
    shipBuilder_shielddata_4.absorption = 400.0
    shipBuilder_shielddata_4 = importer.save_or_locate(shipBuilder_shielddata_4)

    shipBuilder_shielddata_5 = ShieldData()
    shipBuilder_shielddata_5.absorption = 300.0
    shipBuilder_shielddata_5 = importer.save_or_locate(shipBuilder_shielddata_5)

    shipBuilder_shielddata_6 = ShieldData()
    shipBuilder_shielddata_6.absorption = 400.0
    shipBuilder_shielddata_6 = importer.save_or_locate(shipBuilder_shielddata_6)

    #Processing model: EngineIntakeData

    from shipBuilder.models import EngineIntakeData


    #Processing model: Ship

    from shipBuilder.models import Ship

    shipBuilder_ship_1 = Ship()
    shipBuilder_ship_1.name = u'300i'
    shipBuilder_ship_1.description = u"If you're going to travel the stars... why not do it in style? The 300i is Origin Jumpworks' premiere luxury spacecraft. It is a sleek, silver killer that sends as much of a message with its silhouette as it does with its weaponry."
    shipBuilder_ship_1.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_ship_1.maximum_crew = 1L
    shipBuilder_ship_1.empty_mass = 20000L
    shipBuilder_ship_1.length = 24.0
    shipBuilder_ship_1.width = 16.0
    shipBuilder_ship_1.height = 7.0
    shipBuilder_ship_1.upgrade_capacity = 6L
    shipBuilder_ship_1.memory_capacity = 0L
    shipBuilder_ship_1.main_thruster_count = 1L
    shipBuilder_ship_1.main_thruster_max_rating = 4L
    shipBuilder_ship_1.control_thruster_count = 12L
    shipBuilder_ship_1.control_thruster_max_rating = 1L
    shipBuilder_ship_1.powerplant_class_max = 3L
    shipBuilder_ship_1.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/300i.jpg'
    shipBuilder_ship_1.available = True
    shipBuilder_ship_1.ship_class = 1L
    shipBuilder_ship_1 = importer.save_or_locate(shipBuilder_ship_1)

    shipBuilder_ship_2 = Ship()
    shipBuilder_ship_2.name = u'Aurora'
    shipBuilder_ship_2.description = u"The Aurora is the modern day descendant of the Roberts Space Industries X-7 spacecraft which tested the very first jump engines. Utilitarian to a T, the Aurora is the perfect beginner's ship: what it lacks in style it makes up for in ample room for upgrade modules."
    shipBuilder_ship_2.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_ship_2.maximum_crew = 1L
    shipBuilder_ship_2.empty_mass = 15000L
    shipBuilder_ship_2.length = 18.5
    shipBuilder_ship_2.width = 9.0
    shipBuilder_ship_2.height = 5.0
    shipBuilder_ship_2.upgrade_capacity = 4L
    shipBuilder_ship_2.memory_capacity = 0L
    shipBuilder_ship_2.main_thruster_count = 1L
    shipBuilder_ship_2.main_thruster_max_rating = 3L
    shipBuilder_ship_2.control_thruster_count = 6L
    shipBuilder_ship_2.control_thruster_max_rating = 1L
    shipBuilder_ship_2.powerplant_class_max = 2L
    shipBuilder_ship_2.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/auroraes.jpg'
    shipBuilder_ship_2.available = True
    shipBuilder_ship_2.ship_class = 1L
    shipBuilder_ship_2 = importer.save_or_locate(shipBuilder_ship_2)

    shipBuilder_ship_3 = Ship()
    shipBuilder_ship_3.name = u'Constellation'
    shipBuilder_ship_3.description = u"The Constellation, a multi-person freighter, is the most popular ship in RSI's current production array.  Constellations are beloved by smugglers and merchants alike because they are modular, high powered... and just downright iconic-looking."
    shipBuilder_ship_3.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_ship_3.maximum_crew = 4L
    shipBuilder_ship_3.empty_mass = 75000L
    shipBuilder_ship_3.length = 51.0
    shipBuilder_ship_3.width = 23.0
    shipBuilder_ship_3.height = 13.0
    shipBuilder_ship_3.upgrade_capacity = 20L
    shipBuilder_ship_3.memory_capacity = 0L
    shipBuilder_ship_3.main_thruster_count = 4L
    shipBuilder_ship_3.main_thruster_max_rating = 6L
    shipBuilder_ship_3.control_thruster_count = 8L
    shipBuilder_ship_3.control_thruster_max_rating = 3L
    shipBuilder_ship_3.powerplant_class_max = 6L
    shipBuilder_ship_3.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/constellation.jpg'
    shipBuilder_ship_3.available = True
    shipBuilder_ship_3.ship_class = 1L
    shipBuilder_ship_3 = importer.save_or_locate(shipBuilder_ship_3)

    shipBuilder_ship_4 = Ship()
    shipBuilder_ship_4.name = u'350r'
    shipBuilder_ship_4.description = u"The combination of a Gangleri BP 707 Standard powerplant with a 300i fuselate re-engineered to accommodate twin Hammer Propulsion HM 4.3 thrusters makes the 350r the fastest personal craft you'll ever call your own."
    shipBuilder_ship_4.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_ship_4.maximum_crew = 1L
    shipBuilder_ship_4.empty_mass = 17000L
    shipBuilder_ship_4.length = 24.0
    shipBuilder_ship_4.width = 16.0
    shipBuilder_ship_4.height = 7.0
    shipBuilder_ship_4.upgrade_capacity = 6L
    shipBuilder_ship_4.memory_capacity = 0L
    shipBuilder_ship_4.main_thruster_count = 2L
    shipBuilder_ship_4.main_thruster_max_rating = 4L
    shipBuilder_ship_4.control_thruster_count = 12L
    shipBuilder_ship_4.control_thruster_max_rating = 1L
    shipBuilder_ship_4.powerplant_class_max = 4L
    shipBuilder_ship_4.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/350r.jpg'
    shipBuilder_ship_4.available = True
    shipBuilder_ship_4.ship_class = 1L
    shipBuilder_ship_4 = importer.save_or_locate(shipBuilder_ship_4)

    shipBuilder_ship_5 = Ship()
    shipBuilder_ship_5.name = u'F7C Hornet'
    shipBuilder_ship_5.description = u"To the enemy, it is a weapon never to be underestimated. To allies, it's a savior. The F7C Hornet is the same dependable and resilient multi-purpose fighter that has become the face of the UEE Navy. The F7C is the foundation to build on and meet whatever requirements you have in mind."
    shipBuilder_ship_5.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_ship_5.maximum_crew = 1L
    shipBuilder_ship_5.empty_mass = 20000L
    shipBuilder_ship_5.length = 24.0
    shipBuilder_ship_5.width = 22.0
    shipBuilder_ship_5.height = 7.0
    shipBuilder_ship_5.upgrade_capacity = 6L
    shipBuilder_ship_5.memory_capacity = 0L
    shipBuilder_ship_5.main_thruster_count = 1L
    shipBuilder_ship_5.main_thruster_max_rating = 4L
    shipBuilder_ship_5.control_thruster_count = 8L
    shipBuilder_ship_5.control_thruster_max_rating = 2L
    shipBuilder_ship_5.powerplant_class_max = 3L
    shipBuilder_ship_5.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/hornet.jpg'
    shipBuilder_ship_5.available = False
    shipBuilder_ship_5.ship_class = 2L
    shipBuilder_ship_5 = importer.save_or_locate(shipBuilder_ship_5)

    shipBuilder_ship_6 = Ship()
    shipBuilder_ship_6.name = u'Avenger'
    shipBuilder_ship_6.description = u'The Aegis Avenger has had a long and storied life as the standard patrol craft of the UEE Advocacy. Although aging, the Avenger features a sturdy, reliable hull and the capacity for larger-than-expected engine mounts and a front-mounted cannon guaranteed to strike fear into your opponents.'
    shipBuilder_ship_6.manufacturer = shipBuilder_manufacturer_33
    shipBuilder_ship_6.maximum_crew = 1L
    shipBuilder_ship_6.empty_mass = 32000L
    shipBuilder_ship_6.length = 21.0
    shipBuilder_ship_6.width = 18.0
    shipBuilder_ship_6.height = 7.0
    shipBuilder_ship_6.upgrade_capacity = 4L
    shipBuilder_ship_6.memory_capacity = 0L
    shipBuilder_ship_6.main_thruster_count = 1L
    shipBuilder_ship_6.main_thruster_max_rating = 5L
    shipBuilder_ship_6.control_thruster_count = 8L
    shipBuilder_ship_6.control_thruster_max_rating = 1L
    shipBuilder_ship_6.powerplant_class_max = 3L
    shipBuilder_ship_6.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/avenger.jpg'
    shipBuilder_ship_6.available = True
    shipBuilder_ship_6.ship_class = 1L
    shipBuilder_ship_6 = importer.save_or_locate(shipBuilder_ship_6)

    shipBuilder_ship_7 = Ship()
    shipBuilder_ship_7.name = u'Freelancer'
    shipBuilder_ship_7.description = u'Freelancers are used as long haul merchant ships by major corporations, but they are just as frequently repurposed as dedicated exploration vessels by independent captains who want to operate on the fringes of the galaxy.'
    shipBuilder_ship_7.manufacturer = shipBuilder_manufacturer_34
    shipBuilder_ship_7.maximum_crew = 2L
    shipBuilder_ship_7.empty_mass = 55000L
    shipBuilder_ship_7.length = 32.0
    shipBuilder_ship_7.width = 15.0
    shipBuilder_ship_7.height = 8.0
    shipBuilder_ship_7.upgrade_capacity = 10L
    shipBuilder_ship_7.memory_capacity = 0L
    shipBuilder_ship_7.main_thruster_count = 2L
    shipBuilder_ship_7.main_thruster_max_rating = 5L
    shipBuilder_ship_7.control_thruster_count = 8L
    shipBuilder_ship_7.control_thruster_max_rating = 2L
    shipBuilder_ship_7.powerplant_class_max = 1L
    shipBuilder_ship_7.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/freelancer.jpg'
    shipBuilder_ship_7.available = True
    shipBuilder_ship_7.ship_class = 3L
    shipBuilder_ship_7 = importer.save_or_locate(shipBuilder_ship_7)

    shipBuilder_ship_8 = Ship()
    shipBuilder_ship_8.name = u'P-52'
    shipBuilder_ship_8.description = u'Coming standard with the Constellation, the P52 is a versatile short-range fighter designed to offer support in combat situations as well as reconnaissance.'
    shipBuilder_ship_8.manufacturer = shipBuilder_manufacturer_35
    shipBuilder_ship_8.maximum_crew = 1L
    shipBuilder_ship_8.empty_mass = 5500L
    shipBuilder_ship_8.length = 10.0
    shipBuilder_ship_8.width = 8.0
    shipBuilder_ship_8.height = 3.0
    shipBuilder_ship_8.upgrade_capacity = 1L
    shipBuilder_ship_8.memory_capacity = 0L
    shipBuilder_ship_8.main_thruster_count = 3L
    shipBuilder_ship_8.main_thruster_max_rating = 2L
    shipBuilder_ship_8.control_thruster_count = 8L
    shipBuilder_ship_8.control_thruster_max_rating = 1L
    shipBuilder_ship_8.powerplant_class_max = 1L
    shipBuilder_ship_8.thumbnail = u'http://www.stantonspacebarn.com/static/images/ship_thumbnails/p52.jpg'
    shipBuilder_ship_8.available = True
    shipBuilder_ship_8.ship_class = 1L
    shipBuilder_ship_8 = importer.save_or_locate(shipBuilder_ship_8)

    #Processing model: Image

    from shipBuilder.models import Image

    shipBuilder_image_1 = Image()
    shipBuilder_image_1.url = u'http://www.stantonspacebarn.com/static/images/300i_top.png'
    shipBuilder_image_1.name = u'300i Top Isometric'
    shipBuilder_image_1.ship = shipBuilder_ship_1
    shipBuilder_image_1 = importer.save_or_locate(shipBuilder_image_1)

    shipBuilder_image_2 = Image()
    shipBuilder_image_2.url = u'http://www.stantonspacebarn.com/static/images/300i_bottom.png'
    shipBuilder_image_2.name = u'300i Ventral Isometric'
    shipBuilder_image_2.ship = shipBuilder_ship_1
    shipBuilder_image_2 = importer.save_or_locate(shipBuilder_image_2)

    shipBuilder_image_3 = Image()
    shipBuilder_image_3.url = u'http://www.stantonspacebarn.com/static/images/aurora_front_side.png'
    shipBuilder_image_3.name = u'Aurora Side View'
    shipBuilder_image_3.ship = shipBuilder_ship_2
    shipBuilder_image_3 = importer.save_or_locate(shipBuilder_image_3)

    shipBuilder_image_4 = Image()
    shipBuilder_image_4.url = u'http://www.stantonspacebarn.com/static/images/aurora_top_back.png'
    shipBuilder_image_4.name = u'Aurora Top Back'
    shipBuilder_image_4.ship = shipBuilder_ship_2
    shipBuilder_image_4 = importer.save_or_locate(shipBuilder_image_4)

    shipBuilder_image_5 = Image()
    shipBuilder_image_5.url = u'http://www.stantonspacebarn.com/static/images/rsi_constellation_top.png'
    shipBuilder_image_5.name = u'Constellation Top'
    shipBuilder_image_5.ship = shipBuilder_ship_3
    shipBuilder_image_5 = importer.save_or_locate(shipBuilder_image_5)

    shipBuilder_image_6 = Image()
    shipBuilder_image_6.url = u'http://www.stantonspacebarn.com/static/images/300i_top.png'
    shipBuilder_image_6.name = u'350r Top Isometric'
    shipBuilder_image_6.ship = shipBuilder_ship_4
    shipBuilder_image_6 = importer.save_or_locate(shipBuilder_image_6)

    shipBuilder_image_7 = Image()
    shipBuilder_image_7.url = u'http://www.stantonspacebarn.com/static/images/300i_bottom.png'
    shipBuilder_image_7.name = u'350r Ventral Isometric'
    shipBuilder_image_7.ship = shipBuilder_ship_4
    shipBuilder_image_7 = importer.save_or_locate(shipBuilder_image_7)

    shipBuilder_image_8 = Image()
    shipBuilder_image_8.url = u'http://www.stantonspacebarn.com/static/images/rsi_constellation_bottom.png'
    shipBuilder_image_8.name = u'Constellation Bottom'
    shipBuilder_image_8.ship = shipBuilder_ship_3
    shipBuilder_image_8 = importer.save_or_locate(shipBuilder_image_8)

    shipBuilder_image_9 = Image()
    shipBuilder_image_9.url = u'http://www.stantonspacebarn.com/static/images/rsi_constellation_top_flipped.png'
    shipBuilder_image_9.name = u'Constellation Top Flipped'
    shipBuilder_image_9.ship = shipBuilder_ship_3
    shipBuilder_image_9 = importer.save_or_locate(shipBuilder_image_9)

    shipBuilder_image_10 = Image()
    shipBuilder_image_10.url = u'http://www.stantonspacebarn.com/static/images/Avenger_Front.png'
    shipBuilder_image_10.name = u'Avenger Front'
    shipBuilder_image_10.ship = shipBuilder_ship_6
    shipBuilder_image_10 = importer.save_or_locate(shipBuilder_image_10)

    shipBuilder_image_11 = Image()
    shipBuilder_image_11.url = u'http://www.stantonspacebarn.com/static/images/Avenger_Side.png'
    shipBuilder_image_11.name = u'Avenger Side'
    shipBuilder_image_11.ship = shipBuilder_ship_6
    shipBuilder_image_11 = importer.save_or_locate(shipBuilder_image_11)

    shipBuilder_image_12 = Image()
    shipBuilder_image_12.url = u'http://www.stantonspacebarn.com/static/images/Freelancer_Front.png'
    shipBuilder_image_12.name = u'Freelancer Front'
    shipBuilder_image_12.ship = shipBuilder_ship_7
    shipBuilder_image_12 = importer.save_or_locate(shipBuilder_image_12)

    shipBuilder_image_13 = Image()
    shipBuilder_image_13.url = u'http://www.stantonspacebarn.com/static/images/Freelancer_Bottom.png'
    shipBuilder_image_13.name = u'Freelancer Bottom'
    shipBuilder_image_13.ship = shipBuilder_ship_7
    shipBuilder_image_13 = importer.save_or_locate(shipBuilder_image_13)

    shipBuilder_image_14 = Image()
    shipBuilder_image_14.url = u'http://www.stantonspacebarn.com/static/images/p52.png'
    shipBuilder_image_14.name = u'P52 Top'
    shipBuilder_image_14.ship = shipBuilder_ship_8
    shipBuilder_image_14 = importer.save_or_locate(shipBuilder_image_14)

    #Processing model: CargoModData

    from shipBuilder.models import CargoModData

    shipBuilder_cargomoddata_1 = CargoModData()
    shipBuilder_cargomoddata_1.cargo_capacity = 5L
    shipBuilder_cargomoddata_1 = importer.save_or_locate(shipBuilder_cargomoddata_1)

    shipBuilder_cargomoddata_1.supported_ships.add(shipBuilder_ship_1)
    shipBuilder_cargomoddata_1.supported_ships.add(shipBuilder_ship_2)
    shipBuilder_cargomoddata_1.supported_ships.add(shipBuilder_ship_3)
    shipBuilder_cargomoddata_1.supported_ships.add(shipBuilder_ship_4)

    shipBuilder_cargomoddata_2 = CargoModData()
    shipBuilder_cargomoddata_2.cargo_capacity = 10L
    shipBuilder_cargomoddata_2 = importer.save_or_locate(shipBuilder_cargomoddata_2)

    shipBuilder_cargomoddata_2.supported_ships.add(shipBuilder_ship_1)
    shipBuilder_cargomoddata_2.supported_ships.add(shipBuilder_ship_2)
    shipBuilder_cargomoddata_2.supported_ships.add(shipBuilder_ship_3)
    shipBuilder_cargomoddata_2.supported_ships.add(shipBuilder_ship_4)

    shipBuilder_cargomoddata_3 = CargoModData()
    shipBuilder_cargomoddata_3.cargo_capacity = 4L
    shipBuilder_cargomoddata_3 = importer.save_or_locate(shipBuilder_cargomoddata_3)

    shipBuilder_cargomoddata_3.supported_ships.add(shipBuilder_ship_5)

    #Processing model: Hardpoint

    from shipBuilder.models import Hardpoint

    shipBuilder_hardpoint_1 = Hardpoint()
    shipBuilder_hardpoint_1.name = u'Nose'
    shipBuilder_hardpoint_1.hardpoint_class = 2L
    shipBuilder_hardpoint_1.overlay_location_x = -50L
    shipBuilder_hardpoint_1.overlay_location_y = 219L
    shipBuilder_hardpoint_1.tag_location_x = 129L
    shipBuilder_hardpoint_1.tag_location_y = 117L
    shipBuilder_hardpoint_1.ship = shipBuilder_ship_1
    shipBuilder_hardpoint_1.image = shipBuilder_image_2
    shipBuilder_hardpoint_1 = importer.save_or_locate(shipBuilder_hardpoint_1)

    shipBuilder_hardpoint_2 = Hardpoint()
    shipBuilder_hardpoint_2.name = u'Port Inner Wing'
    shipBuilder_hardpoint_2.hardpoint_class = 3L
    shipBuilder_hardpoint_2.overlay_location_x = 300L
    shipBuilder_hardpoint_2.overlay_location_y = 350L
    shipBuilder_hardpoint_2.tag_location_x = 610L
    shipBuilder_hardpoint_2.tag_location_y = 156L
    shipBuilder_hardpoint_2.ship = shipBuilder_ship_1
    shipBuilder_hardpoint_2.image = shipBuilder_image_1
    shipBuilder_hardpoint_2 = importer.save_or_locate(shipBuilder_hardpoint_2)

    shipBuilder_hardpoint_3 = Hardpoint()
    shipBuilder_hardpoint_3.name = u'Starboard Inner Wing'
    shipBuilder_hardpoint_3.hardpoint_class = 3L
    shipBuilder_hardpoint_3.overlay_location_x = 200L
    shipBuilder_hardpoint_3.overlay_location_y = -50L
    shipBuilder_hardpoint_3.tag_location_x = 400L
    shipBuilder_hardpoint_3.tag_location_y = 72L
    shipBuilder_hardpoint_3.ship = shipBuilder_ship_1
    shipBuilder_hardpoint_3.image = shipBuilder_image_1
    shipBuilder_hardpoint_3 = importer.save_or_locate(shipBuilder_hardpoint_3)

    shipBuilder_hardpoint_4 = Hardpoint()
    shipBuilder_hardpoint_4.name = u'Starboard Outer Wing'
    shipBuilder_hardpoint_4.hardpoint_class = 1L
    shipBuilder_hardpoint_4.overlay_location_x = 50L
    shipBuilder_hardpoint_4.overlay_location_y = 350L
    shipBuilder_hardpoint_4.tag_location_x = 361L
    shipBuilder_hardpoint_4.tag_location_y = 319L
    shipBuilder_hardpoint_4.ship = shipBuilder_ship_1
    shipBuilder_hardpoint_4.image = shipBuilder_image_2
    shipBuilder_hardpoint_4 = importer.save_or_locate(shipBuilder_hardpoint_4)

    shipBuilder_hardpoint_5 = Hardpoint()
    shipBuilder_hardpoint_5.name = u'Port Outer Wing'
    shipBuilder_hardpoint_5.hardpoint_class = 1L
    shipBuilder_hardpoint_5.overlay_location_x = 500L
    shipBuilder_hardpoint_5.overlay_location_y = 50L
    shipBuilder_hardpoint_5.tag_location_x = 583L
    shipBuilder_hardpoint_5.tag_location_y = 210L
    shipBuilder_hardpoint_5.ship = shipBuilder_ship_1
    shipBuilder_hardpoint_5.image = shipBuilder_image_2
    shipBuilder_hardpoint_5 = importer.save_or_locate(shipBuilder_hardpoint_5)

    shipBuilder_hardpoint_6 = Hardpoint()
    shipBuilder_hardpoint_6.name = u'Port Nose'
    shipBuilder_hardpoint_6.hardpoint_class = 1L
    shipBuilder_hardpoint_6.overlay_location_x = -50L
    shipBuilder_hardpoint_6.overlay_location_y = 25L
    shipBuilder_hardpoint_6.tag_location_x = 99L
    shipBuilder_hardpoint_6.tag_location_y = 268L
    shipBuilder_hardpoint_6.ship = shipBuilder_ship_2
    shipBuilder_hardpoint_6.image = shipBuilder_image_3
    shipBuilder_hardpoint_6 = importer.save_or_locate(shipBuilder_hardpoint_6)

    shipBuilder_hardpoint_7 = Hardpoint()
    shipBuilder_hardpoint_7.name = u'Dorsal Center'
    shipBuilder_hardpoint_7.hardpoint_class = 3L
    shipBuilder_hardpoint_7.overlay_location_x = 200L
    shipBuilder_hardpoint_7.overlay_location_y = 0L
    shipBuilder_hardpoint_7.tag_location_x = 509L
    shipBuilder_hardpoint_7.tag_location_y = 135L
    shipBuilder_hardpoint_7.ship = shipBuilder_ship_2
    shipBuilder_hardpoint_7.image = shipBuilder_image_4
    shipBuilder_hardpoint_7 = importer.save_or_locate(shipBuilder_hardpoint_7)

    shipBuilder_hardpoint_8 = Hardpoint()
    shipBuilder_hardpoint_8.name = u'Starboard Nose'
    shipBuilder_hardpoint_8.hardpoint_class = 1L
    shipBuilder_hardpoint_8.overlay_location_x = 250L
    shipBuilder_hardpoint_8.overlay_location_y = 350L
    shipBuilder_hardpoint_8.tag_location_x = 181L
    shipBuilder_hardpoint_8.tag_location_y = 284L
    shipBuilder_hardpoint_8.ship = shipBuilder_ship_2
    shipBuilder_hardpoint_8.image = shipBuilder_image_3
    shipBuilder_hardpoint_8 = importer.save_or_locate(shipBuilder_hardpoint_8)

    shipBuilder_hardpoint_9 = Hardpoint()
    shipBuilder_hardpoint_9.name = u'Starboard Dorsal'
    shipBuilder_hardpoint_9.hardpoint_class = 3L
    shipBuilder_hardpoint_9.overlay_location_x = 250L
    shipBuilder_hardpoint_9.overlay_location_y = -20L
    shipBuilder_hardpoint_9.tag_location_x = 260L
    shipBuilder_hardpoint_9.tag_location_y = 90L
    shipBuilder_hardpoint_9.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_9.image = shipBuilder_image_5
    shipBuilder_hardpoint_9 = importer.save_or_locate(shipBuilder_hardpoint_9)

    shipBuilder_hardpoint_10 = Hardpoint()
    shipBuilder_hardpoint_10.name = u'Port Dorsal'
    shipBuilder_hardpoint_10.hardpoint_class = 3L
    shipBuilder_hardpoint_10.overlay_location_x = -50L
    shipBuilder_hardpoint_10.overlay_location_y = 150L
    shipBuilder_hardpoint_10.tag_location_x = 190L
    shipBuilder_hardpoint_10.tag_location_y = 120L
    shipBuilder_hardpoint_10.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_10.image = shipBuilder_image_5
    shipBuilder_hardpoint_10 = importer.save_or_locate(shipBuilder_hardpoint_10)

    shipBuilder_hardpoint_11 = Hardpoint()
    shipBuilder_hardpoint_11.name = u'Starboard Dorsal Fixed'
    shipBuilder_hardpoint_11.hardpoint_class = 2L
    shipBuilder_hardpoint_11.overlay_location_x = 650L
    shipBuilder_hardpoint_11.overlay_location_y = 150L
    shipBuilder_hardpoint_11.tag_location_x = 445L
    shipBuilder_hardpoint_11.tag_location_y = 153L
    shipBuilder_hardpoint_11.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_11.image = shipBuilder_image_9
    shipBuilder_hardpoint_11 = importer.save_or_locate(shipBuilder_hardpoint_11)

    shipBuilder_hardpoint_12 = Hardpoint()
    shipBuilder_hardpoint_12.name = u'Engine Two'
    shipBuilder_hardpoint_12.hardpoint_class = 2L
    shipBuilder_hardpoint_12.overlay_location_x = 50L
    shipBuilder_hardpoint_12.overlay_location_y = 100L
    shipBuilder_hardpoint_12.tag_location_x = 195L
    shipBuilder_hardpoint_12.tag_location_y = 254L
    shipBuilder_hardpoint_12.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_12.image = shipBuilder_image_8
    shipBuilder_hardpoint_12 = importer.save_or_locate(shipBuilder_hardpoint_12)

    shipBuilder_hardpoint_13 = Hardpoint()
    shipBuilder_hardpoint_13.name = u'Port Dorsal Fixed'
    shipBuilder_hardpoint_13.hardpoint_class = 2L
    shipBuilder_hardpoint_13.overlay_location_x = 400L
    shipBuilder_hardpoint_13.overlay_location_y = 10L
    shipBuilder_hardpoint_13.tag_location_x = 255L
    shipBuilder_hardpoint_13.tag_location_y = 152L
    shipBuilder_hardpoint_13.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_13.image = shipBuilder_image_5
    shipBuilder_hardpoint_13 = importer.save_or_locate(shipBuilder_hardpoint_13)

    shipBuilder_hardpoint_14 = Hardpoint()
    shipBuilder_hardpoint_14.name = u'Engine Four'
    shipBuilder_hardpoint_14.hardpoint_class = 2L
    shipBuilder_hardpoint_14.overlay_location_x = 400L
    shipBuilder_hardpoint_14.overlay_location_y = 400L
    shipBuilder_hardpoint_14.tag_location_x = 413L
    shipBuilder_hardpoint_14.tag_location_y = 353L
    shipBuilder_hardpoint_14.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_14.image = shipBuilder_image_8
    shipBuilder_hardpoint_14 = importer.save_or_locate(shipBuilder_hardpoint_14)

    shipBuilder_hardpoint_15 = Hardpoint()
    shipBuilder_hardpoint_15.name = u'Port Outer Wing'
    shipBuilder_hardpoint_15.hardpoint_class = 1L
    shipBuilder_hardpoint_15.overlay_location_x = 500L
    shipBuilder_hardpoint_15.overlay_location_y = 50L
    shipBuilder_hardpoint_15.tag_location_x = 583L
    shipBuilder_hardpoint_15.tag_location_y = 210L
    shipBuilder_hardpoint_15.ship = shipBuilder_ship_4
    shipBuilder_hardpoint_15.image = shipBuilder_image_7
    shipBuilder_hardpoint_15 = importer.save_or_locate(shipBuilder_hardpoint_15)

    shipBuilder_hardpoint_16 = Hardpoint()
    shipBuilder_hardpoint_16.name = u'Starboard Outer Wing'
    shipBuilder_hardpoint_16.hardpoint_class = 1L
    shipBuilder_hardpoint_16.overlay_location_x = 50L
    shipBuilder_hardpoint_16.overlay_location_y = 350L
    shipBuilder_hardpoint_16.tag_location_x = 361L
    shipBuilder_hardpoint_16.tag_location_y = 319L
    shipBuilder_hardpoint_16.ship = shipBuilder_ship_4
    shipBuilder_hardpoint_16.image = shipBuilder_image_7
    shipBuilder_hardpoint_16 = importer.save_or_locate(shipBuilder_hardpoint_16)

    shipBuilder_hardpoint_17 = Hardpoint()
    shipBuilder_hardpoint_17.name = u'Starboard Inner Wing'
    shipBuilder_hardpoint_17.hardpoint_class = 3L
    shipBuilder_hardpoint_17.overlay_location_x = 200L
    shipBuilder_hardpoint_17.overlay_location_y = -50L
    shipBuilder_hardpoint_17.tag_location_x = 400L
    shipBuilder_hardpoint_17.tag_location_y = 72L
    shipBuilder_hardpoint_17.ship = shipBuilder_ship_4
    shipBuilder_hardpoint_17.image = shipBuilder_image_6
    shipBuilder_hardpoint_17 = importer.save_or_locate(shipBuilder_hardpoint_17)

    shipBuilder_hardpoint_18 = Hardpoint()
    shipBuilder_hardpoint_18.name = u'Port Inner Wing'
    shipBuilder_hardpoint_18.hardpoint_class = 3L
    shipBuilder_hardpoint_18.overlay_location_x = 300L
    shipBuilder_hardpoint_18.overlay_location_y = 350L
    shipBuilder_hardpoint_18.tag_location_x = 610L
    shipBuilder_hardpoint_18.tag_location_y = 156L
    shipBuilder_hardpoint_18.ship = shipBuilder_ship_4
    shipBuilder_hardpoint_18.image = shipBuilder_image_6
    shipBuilder_hardpoint_18 = importer.save_or_locate(shipBuilder_hardpoint_18)

    shipBuilder_hardpoint_19 = Hardpoint()
    shipBuilder_hardpoint_19.name = u'Nose'
    shipBuilder_hardpoint_19.hardpoint_class = 2L
    shipBuilder_hardpoint_19.overlay_location_x = -50L
    shipBuilder_hardpoint_19.overlay_location_y = 219L
    shipBuilder_hardpoint_19.tag_location_x = 129L
    shipBuilder_hardpoint_19.tag_location_y = 117L
    shipBuilder_hardpoint_19.ship = shipBuilder_ship_4
    shipBuilder_hardpoint_19.image = shipBuilder_image_7
    shipBuilder_hardpoint_19 = importer.save_or_locate(shipBuilder_hardpoint_19)

    shipBuilder_hardpoint_20 = Hardpoint()
    shipBuilder_hardpoint_20.name = u'Dorsal Turret'
    shipBuilder_hardpoint_20.hardpoint_class = 5L
    shipBuilder_hardpoint_20.overlay_location_x = 50L
    shipBuilder_hardpoint_20.overlay_location_y = -50L
    shipBuilder_hardpoint_20.tag_location_x = 125L
    shipBuilder_hardpoint_20.tag_location_y = 60L
    shipBuilder_hardpoint_20.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_20.image = shipBuilder_image_5
    shipBuilder_hardpoint_20 = importer.save_or_locate(shipBuilder_hardpoint_20)

    shipBuilder_hardpoint_21 = Hardpoint()
    shipBuilder_hardpoint_21.name = u'Ventral Turrent'
    shipBuilder_hardpoint_21.hardpoint_class = 5L
    shipBuilder_hardpoint_21.overlay_location_x = 200L
    shipBuilder_hardpoint_21.overlay_location_y = -50L
    shipBuilder_hardpoint_21.tag_location_x = 565L
    shipBuilder_hardpoint_21.tag_location_y = 140L
    shipBuilder_hardpoint_21.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_21.image = shipBuilder_image_8
    shipBuilder_hardpoint_21 = importer.save_or_locate(shipBuilder_hardpoint_21)

    shipBuilder_hardpoint_22 = Hardpoint()
    shipBuilder_hardpoint_22.name = u'Starboard Small Missile '
    shipBuilder_hardpoint_22.hardpoint_class = 3L
    shipBuilder_hardpoint_22.overlay_location_x = 590L
    shipBuilder_hardpoint_22.overlay_location_y = 300L
    shipBuilder_hardpoint_22.tag_location_x = 464L
    shipBuilder_hardpoint_22.tag_location_y = 230L
    shipBuilder_hardpoint_22.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_22.image = shipBuilder_image_9
    shipBuilder_hardpoint_22 = importer.save_or_locate(shipBuilder_hardpoint_22)

    shipBuilder_hardpoint_23 = Hardpoint()
    shipBuilder_hardpoint_23.name = u'Starboard Large Missle'
    shipBuilder_hardpoint_23.hardpoint_class = 3L
    shipBuilder_hardpoint_23.overlay_location_x = 190L
    shipBuilder_hardpoint_23.overlay_location_y = 360L
    shipBuilder_hardpoint_23.tag_location_x = 390L
    shipBuilder_hardpoint_23.tag_location_y = 270L
    shipBuilder_hardpoint_23.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_23.image = shipBuilder_image_9
    shipBuilder_hardpoint_23 = importer.save_or_locate(shipBuilder_hardpoint_23)

    shipBuilder_hardpoint_24 = Hardpoint()
    shipBuilder_hardpoint_24.name = u'Port Small Missile'
    shipBuilder_hardpoint_24.hardpoint_class = 3L
    shipBuilder_hardpoint_24.overlay_location_x = 0L
    shipBuilder_hardpoint_24.overlay_location_y = 290L
    shipBuilder_hardpoint_24.tag_location_x = 240L
    shipBuilder_hardpoint_24.tag_location_y = 230L
    shipBuilder_hardpoint_24.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_24.image = shipBuilder_image_5
    shipBuilder_hardpoint_24 = importer.save_or_locate(shipBuilder_hardpoint_24)

    shipBuilder_hardpoint_25 = Hardpoint()
    shipBuilder_hardpoint_25.name = u'Port Large Missile'
    shipBuilder_hardpoint_25.hardpoint_class = 3L
    shipBuilder_hardpoint_25.overlay_location_x = 215L
    shipBuilder_hardpoint_25.overlay_location_y = 388L
    shipBuilder_hardpoint_25.tag_location_x = 312L
    shipBuilder_hardpoint_25.tag_location_y = 270L
    shipBuilder_hardpoint_25.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_25.image = shipBuilder_image_5
    shipBuilder_hardpoint_25 = importer.save_or_locate(shipBuilder_hardpoint_25)

    shipBuilder_hardpoint_26 = Hardpoint()
    shipBuilder_hardpoint_26.name = u'Nose'
    shipBuilder_hardpoint_26.hardpoint_class = 1L
    shipBuilder_hardpoint_26.overlay_location_x = 620L
    shipBuilder_hardpoint_26.overlay_location_y = 60L
    shipBuilder_hardpoint_26.tag_location_x = 528L
    shipBuilder_hardpoint_26.tag_location_y = 214L
    shipBuilder_hardpoint_26.ship = shipBuilder_ship_6
    shipBuilder_hardpoint_26.image = shipBuilder_image_11
    shipBuilder_hardpoint_26 = importer.save_or_locate(shipBuilder_hardpoint_26)

    shipBuilder_hardpoint_27 = Hardpoint()
    shipBuilder_hardpoint_27.name = u'Starboard Wingtip'
    shipBuilder_hardpoint_27.hardpoint_class = 1L
    shipBuilder_hardpoint_27.overlay_location_x = -20L
    shipBuilder_hardpoint_27.overlay_location_y = 50L
    shipBuilder_hardpoint_27.tag_location_x = 68L
    shipBuilder_hardpoint_27.tag_location_y = 232L
    shipBuilder_hardpoint_27.ship = shipBuilder_ship_6
    shipBuilder_hardpoint_27.image = shipBuilder_image_10
    shipBuilder_hardpoint_27 = importer.save_or_locate(shipBuilder_hardpoint_27)

    shipBuilder_hardpoint_28 = Hardpoint()
    shipBuilder_hardpoint_28.name = u'Port Wingtip'
    shipBuilder_hardpoint_28.hardpoint_class = 1L
    shipBuilder_hardpoint_28.overlay_location_x = 650L
    shipBuilder_hardpoint_28.overlay_location_y = 50L
    shipBuilder_hardpoint_28.tag_location_x = 638L
    shipBuilder_hardpoint_28.tag_location_y = 228L
    shipBuilder_hardpoint_28.ship = shipBuilder_ship_6
    shipBuilder_hardpoint_28.image = shipBuilder_image_10
    shipBuilder_hardpoint_28 = importer.save_or_locate(shipBuilder_hardpoint_28)

    shipBuilder_hardpoint_29 = Hardpoint()
    shipBuilder_hardpoint_29.name = u'Starboard Underwing'
    shipBuilder_hardpoint_29.hardpoint_class = 3L
    shipBuilder_hardpoint_29.overlay_location_x = 70L
    shipBuilder_hardpoint_29.overlay_location_y = 280L
    shipBuilder_hardpoint_29.tag_location_x = 209L
    shipBuilder_hardpoint_29.tag_location_y = 193L
    shipBuilder_hardpoint_29.ship = shipBuilder_ship_6
    shipBuilder_hardpoint_29.image = shipBuilder_image_10
    shipBuilder_hardpoint_29 = importer.save_or_locate(shipBuilder_hardpoint_29)

    shipBuilder_hardpoint_30 = Hardpoint()
    shipBuilder_hardpoint_30.name = u'Port Underwing'
    shipBuilder_hardpoint_30.hardpoint_class = 3L
    shipBuilder_hardpoint_30.overlay_location_x = 600L
    shipBuilder_hardpoint_30.overlay_location_y = 280L
    shipBuilder_hardpoint_30.tag_location_x = 514L
    shipBuilder_hardpoint_30.tag_location_y = 193L
    shipBuilder_hardpoint_30.ship = shipBuilder_ship_6
    shipBuilder_hardpoint_30.image = shipBuilder_image_10
    shipBuilder_hardpoint_30 = importer.save_or_locate(shipBuilder_hardpoint_30)

    shipBuilder_hardpoint_31 = Hardpoint()
    shipBuilder_hardpoint_31.name = u'Starboard Missile'
    shipBuilder_hardpoint_31.hardpoint_class = 3L
    shipBuilder_hardpoint_31.overlay_location_x = 36L
    shipBuilder_hardpoint_31.overlay_location_y = 415L
    shipBuilder_hardpoint_31.tag_location_x = 116L
    shipBuilder_hardpoint_31.tag_location_y = 320L
    shipBuilder_hardpoint_31.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_31.image = shipBuilder_image_13
    shipBuilder_hardpoint_31 = importer.save_or_locate(shipBuilder_hardpoint_31)

    shipBuilder_hardpoint_32 = Hardpoint()
    shipBuilder_hardpoint_32.name = u'Port Missile'
    shipBuilder_hardpoint_32.hardpoint_class = 3L
    shipBuilder_hardpoint_32.overlay_location_x = 620L
    shipBuilder_hardpoint_32.overlay_location_y = 70L
    shipBuilder_hardpoint_32.tag_location_x = 470L
    shipBuilder_hardpoint_32.tag_location_y = 100L
    shipBuilder_hardpoint_32.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_32.image = shipBuilder_image_13
    shipBuilder_hardpoint_32 = importer.save_or_locate(shipBuilder_hardpoint_32)

    shipBuilder_hardpoint_33 = Hardpoint()
    shipBuilder_hardpoint_33.name = u'Rear Turret'
    shipBuilder_hardpoint_33.hardpoint_class = 5L
    shipBuilder_hardpoint_33.overlay_location_x = 45L
    shipBuilder_hardpoint_33.overlay_location_y = 80L
    shipBuilder_hardpoint_33.tag_location_x = 284L
    shipBuilder_hardpoint_33.tag_location_y = 175L
    shipBuilder_hardpoint_33.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_33.image = shipBuilder_image_13
    shipBuilder_hardpoint_33 = importer.save_or_locate(shipBuilder_hardpoint_33)

    shipBuilder_hardpoint_34 = Hardpoint()
    shipBuilder_hardpoint_34.name = u'Starboard Upper Cannon'
    shipBuilder_hardpoint_34.hardpoint_class = 2L
    shipBuilder_hardpoint_34.overlay_location_x = -50L
    shipBuilder_hardpoint_34.overlay_location_y = 100L
    shipBuilder_hardpoint_34.tag_location_x = 218L
    shipBuilder_hardpoint_34.tag_location_y = 173L
    shipBuilder_hardpoint_34.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_34.image = shipBuilder_image_12
    shipBuilder_hardpoint_34 = importer.save_or_locate(shipBuilder_hardpoint_34)

    shipBuilder_hardpoint_35 = Hardpoint()
    shipBuilder_hardpoint_35.name = u'Starboard Lower Cannon'
    shipBuilder_hardpoint_35.hardpoint_class = 2L
    shipBuilder_hardpoint_35.overlay_location_x = -20L
    shipBuilder_hardpoint_35.overlay_location_y = 375L
    shipBuilder_hardpoint_35.tag_location_x = 218L
    shipBuilder_hardpoint_35.tag_location_y = 242L
    shipBuilder_hardpoint_35.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_35.image = shipBuilder_image_12
    shipBuilder_hardpoint_35 = importer.save_or_locate(shipBuilder_hardpoint_35)

    shipBuilder_hardpoint_36 = Hardpoint()
    shipBuilder_hardpoint_36.name = u'Port Upper Cannon'
    shipBuilder_hardpoint_36.hardpoint_class = 2L
    shipBuilder_hardpoint_36.overlay_location_x = 600L
    shipBuilder_hardpoint_36.overlay_location_y = 20L
    shipBuilder_hardpoint_36.tag_location_x = 478L
    shipBuilder_hardpoint_36.tag_location_y = 154L
    shipBuilder_hardpoint_36.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_36.image = shipBuilder_image_12
    shipBuilder_hardpoint_36 = importer.save_or_locate(shipBuilder_hardpoint_36)

    shipBuilder_hardpoint_37 = Hardpoint()
    shipBuilder_hardpoint_37.name = u'Port Lower Cannon'
    shipBuilder_hardpoint_37.hardpoint_class = 2L
    shipBuilder_hardpoint_37.overlay_location_x = 600L
    shipBuilder_hardpoint_37.overlay_location_y = 278L
    shipBuilder_hardpoint_37.tag_location_x = 478L
    shipBuilder_hardpoint_37.tag_location_y = 197L
    shipBuilder_hardpoint_37.ship = shipBuilder_ship_7
    shipBuilder_hardpoint_37.image = shipBuilder_image_12
    shipBuilder_hardpoint_37 = importer.save_or_locate(shipBuilder_hardpoint_37)

    shipBuilder_hardpoint_38 = Hardpoint()
    shipBuilder_hardpoint_38.name = u'Starboard Wing'
    shipBuilder_hardpoint_38.hardpoint_class = 1L
    shipBuilder_hardpoint_38.overlay_location_x = 250L
    shipBuilder_hardpoint_38.overlay_location_y = -50L
    shipBuilder_hardpoint_38.tag_location_x = 305L
    shipBuilder_hardpoint_38.tag_location_y = 140L
    shipBuilder_hardpoint_38.ship = shipBuilder_ship_8
    shipBuilder_hardpoint_38.image = shipBuilder_image_14
    shipBuilder_hardpoint_38 = importer.save_or_locate(shipBuilder_hardpoint_38)

    shipBuilder_hardpoint_39 = Hardpoint()
    shipBuilder_hardpoint_39.name = u'Port Wing'
    shipBuilder_hardpoint_39.hardpoint_class = 1L
    shipBuilder_hardpoint_39.overlay_location_x = 500L
    shipBuilder_hardpoint_39.overlay_location_y = 415L
    shipBuilder_hardpoint_39.tag_location_x = 493L
    shipBuilder_hardpoint_39.tag_location_y = 250L
    shipBuilder_hardpoint_39.ship = shipBuilder_ship_8
    shipBuilder_hardpoint_39.image = shipBuilder_image_14
    shipBuilder_hardpoint_39 = importer.save_or_locate(shipBuilder_hardpoint_39)

    shipBuilder_hardpoint_40 = Hardpoint()
    shipBuilder_hardpoint_40.name = u'Nose Cannon'
    shipBuilder_hardpoint_40.hardpoint_class = 1L
    shipBuilder_hardpoint_40.overlay_location_x = 20L
    shipBuilder_hardpoint_40.overlay_location_y = 150L
    shipBuilder_hardpoint_40.tag_location_x = 235L
    shipBuilder_hardpoint_40.tag_location_y = 257L
    shipBuilder_hardpoint_40.ship = shipBuilder_ship_8
    shipBuilder_hardpoint_40.image = shipBuilder_image_14
    shipBuilder_hardpoint_40 = importer.save_or_locate(shipBuilder_hardpoint_40)

    #Processing model: BuildHardpoint

    from shipBuilder.models import BuildHardpoint


    #Processing model: BuildEngineMod

    from shipBuilder.models import BuildEngineMod


    #Processing model: BuildHullMod

    from shipBuilder.models import BuildHullMod


    #Processing model: Build

    from shipBuilder.models import Build


    #Processing model: Item

    from shipBuilder.models import Item

    shipBuilder_item_1 = Item()
    shipBuilder_item_1.name = u'KS-9'
    shipBuilder_item_1.rating = 1L
    shipBuilder_item_1.size = 0L
    shipBuilder_item_1.description = u''
    shipBuilder_item_1.manufacturer = shipBuilder_manufacturer_14
    shipBuilder_item_1.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_1.hardpoint_class = 0L
    shipBuilder_item_1.mass = 0.0
    shipBuilder_item_1.item_type = shipBuilder_itemtype_4
    shipBuilder_item_1.power = 0.0
    shipBuilder_item_1.energy = 0.0
    shipBuilder_item_1.memory = 0.0
    shipBuilder_item_1.upgrade_slots = 1L
    shipBuilder_item_1.weapon_data = None
    shipBuilder_item_1.cargo_mod_data = None
    shipBuilder_item_1.powerplant_data = shipBuilder_powerplantdata_1
    shipBuilder_item_1.thruster_data = None
    shipBuilder_item_1.shield_data = None
    shipBuilder_item_1.engine_intake_data = None
    shipBuilder_item_1 = importer.save_or_locate(shipBuilder_item_1)

    shipBuilder_item_2 = Item()
    shipBuilder_item_2.name = u'KS-9 Enhanced'
    shipBuilder_item_2.rating = 1L
    shipBuilder_item_2.size = 0L
    shipBuilder_item_2.description = u''
    shipBuilder_item_2.manufacturer = shipBuilder_manufacturer_14
    shipBuilder_item_2.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_2.hardpoint_class = 0L
    shipBuilder_item_2.mass = 0.0
    shipBuilder_item_2.item_type = shipBuilder_itemtype_4
    shipBuilder_item_2.power = 0.0
    shipBuilder_item_2.energy = 0.0
    shipBuilder_item_2.memory = 0.0
    shipBuilder_item_2.upgrade_slots = 1L
    shipBuilder_item_2.weapon_data = None
    shipBuilder_item_2.cargo_mod_data = None
    shipBuilder_item_2.powerplant_data = shipBuilder_powerplantdata_2
    shipBuilder_item_2.thruster_data = None
    shipBuilder_item_2.shield_data = None
    shipBuilder_item_2.engine_intake_data = None
    shipBuilder_item_2 = importer.save_or_locate(shipBuilder_item_2)

    shipBuilder_item_3 = Item()
    shipBuilder_item_3.name = u'Endurance 300'
    shipBuilder_item_3.rating = 1L
    shipBuilder_item_3.size = 0L
    shipBuilder_item_3.description = u''
    shipBuilder_item_3.manufacturer = shipBuilder_manufacturer_15
    shipBuilder_item_3.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_3.hardpoint_class = 0L
    shipBuilder_item_3.mass = 0.0
    shipBuilder_item_3.item_type = shipBuilder_itemtype_4
    shipBuilder_item_3.power = 0.0
    shipBuilder_item_3.energy = 0.0
    shipBuilder_item_3.memory = 0.0
    shipBuilder_item_3.upgrade_slots = 1L
    shipBuilder_item_3.weapon_data = None
    shipBuilder_item_3.cargo_mod_data = None
    shipBuilder_item_3.powerplant_data = shipBuilder_powerplantdata_3
    shipBuilder_item_3.thruster_data = None
    shipBuilder_item_3.shield_data = None
    shipBuilder_item_3.engine_intake_data = None
    shipBuilder_item_3 = importer.save_or_locate(shipBuilder_item_3)

    shipBuilder_item_4 = Item()
    shipBuilder_item_4.name = u'LR-5 MAX Overdrive'
    shipBuilder_item_4.rating = 1L
    shipBuilder_item_4.size = 0L
    shipBuilder_item_4.description = u''
    shipBuilder_item_4.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_item_4.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_4.hardpoint_class = 0L
    shipBuilder_item_4.mass = 0.0
    shipBuilder_item_4.item_type = shipBuilder_itemtype_4
    shipBuilder_item_4.power = 0.0
    shipBuilder_item_4.energy = 0.0
    shipBuilder_item_4.memory = 0.0
    shipBuilder_item_4.upgrade_slots = 1L
    shipBuilder_item_4.weapon_data = None
    shipBuilder_item_4.cargo_mod_data = None
    shipBuilder_item_4.powerplant_data = shipBuilder_powerplantdata_4
    shipBuilder_item_4.thruster_data = None
    shipBuilder_item_4.shield_data = None
    shipBuilder_item_4.engine_intake_data = None
    shipBuilder_item_4 = importer.save_or_locate(shipBuilder_item_4)

    shipBuilder_item_5 = Item()
    shipBuilder_item_5.name = u'StarHeart III'
    shipBuilder_item_5.rating = 1L
    shipBuilder_item_5.size = 0L
    shipBuilder_item_5.description = u''
    shipBuilder_item_5.manufacturer = shipBuilder_manufacturer_10
    shipBuilder_item_5.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_5.hardpoint_class = 0L
    shipBuilder_item_5.mass = 0.0
    shipBuilder_item_5.item_type = shipBuilder_itemtype_4
    shipBuilder_item_5.power = 0.0
    shipBuilder_item_5.energy = 0.0
    shipBuilder_item_5.memory = 0.0
    shipBuilder_item_5.upgrade_slots = 1L
    shipBuilder_item_5.weapon_data = None
    shipBuilder_item_5.cargo_mod_data = None
    shipBuilder_item_5.powerplant_data = shipBuilder_powerplantdata_5
    shipBuilder_item_5.thruster_data = None
    shipBuilder_item_5.shield_data = None
    shipBuilder_item_5.engine_intake_data = None
    shipBuilder_item_5 = importer.save_or_locate(shipBuilder_item_5)

    shipBuilder_item_6 = Item()
    shipBuilder_item_6.name = u'L3S-9'
    shipBuilder_item_6.rating = 1L
    shipBuilder_item_6.size = 0L
    shipBuilder_item_6.description = u''
    shipBuilder_item_6.manufacturer = shipBuilder_manufacturer_14
    shipBuilder_item_6.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_6.hardpoint_class = 0L
    shipBuilder_item_6.mass = 0.0
    shipBuilder_item_6.item_type = shipBuilder_itemtype_4
    shipBuilder_item_6.power = 0.0
    shipBuilder_item_6.energy = 0.0
    shipBuilder_item_6.memory = 0.0
    shipBuilder_item_6.upgrade_slots = 1L
    shipBuilder_item_6.weapon_data = None
    shipBuilder_item_6.cargo_mod_data = None
    shipBuilder_item_6.powerplant_data = shipBuilder_powerplantdata_6
    shipBuilder_item_6.thruster_data = None
    shipBuilder_item_6.shield_data = None
    shipBuilder_item_6.engine_intake_data = None
    shipBuilder_item_6 = importer.save_or_locate(shipBuilder_item_6)

    shipBuilder_item_7 = Item()
    shipBuilder_item_7.name = u'VHT2 Plus'
    shipBuilder_item_7.rating = 1L
    shipBuilder_item_7.size = 0L
    shipBuilder_item_7.description = u''
    shipBuilder_item_7.manufacturer = shipBuilder_manufacturer_12
    shipBuilder_item_7.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_7.hardpoint_class = 0L
    shipBuilder_item_7.mass = 0.0
    shipBuilder_item_7.item_type = shipBuilder_itemtype_4
    shipBuilder_item_7.power = 0.0
    shipBuilder_item_7.energy = 0.0
    shipBuilder_item_7.memory = 0.0
    shipBuilder_item_7.upgrade_slots = 1L
    shipBuilder_item_7.weapon_data = None
    shipBuilder_item_7.cargo_mod_data = None
    shipBuilder_item_7.powerplant_data = shipBuilder_powerplantdata_7
    shipBuilder_item_7.thruster_data = None
    shipBuilder_item_7.shield_data = None
    shipBuilder_item_7.engine_intake_data = None
    shipBuilder_item_7 = importer.save_or_locate(shipBuilder_item_7)

    shipBuilder_item_8 = Item()
    shipBuilder_item_8.name = u'BP 707 Standard'
    shipBuilder_item_8.rating = 1L
    shipBuilder_item_8.size = 0L
    shipBuilder_item_8.description = u''
    shipBuilder_item_8.manufacturer = shipBuilder_manufacturer_13
    shipBuilder_item_8.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_8.hardpoint_class = 0L
    shipBuilder_item_8.mass = 0.0
    shipBuilder_item_8.item_type = shipBuilder_itemtype_4
    shipBuilder_item_8.power = 0.0
    shipBuilder_item_8.energy = 0.0
    shipBuilder_item_8.memory = 0.0
    shipBuilder_item_8.upgrade_slots = 1L
    shipBuilder_item_8.weapon_data = None
    shipBuilder_item_8.cargo_mod_data = None
    shipBuilder_item_8.powerplant_data = shipBuilder_powerplantdata_8
    shipBuilder_item_8.thruster_data = None
    shipBuilder_item_8.shield_data = None
    shipBuilder_item_8.engine_intake_data = None
    shipBuilder_item_8 = importer.save_or_locate(shipBuilder_item_8)

    shipBuilder_item_9 = Item()
    shipBuilder_item_9.name = u'StarHeart IV'
    shipBuilder_item_9.rating = 1L
    shipBuilder_item_9.size = 0L
    shipBuilder_item_9.description = u''
    shipBuilder_item_9.manufacturer = shipBuilder_manufacturer_10
    shipBuilder_item_9.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_9.hardpoint_class = 0L
    shipBuilder_item_9.mass = 0.0
    shipBuilder_item_9.item_type = shipBuilder_itemtype_4
    shipBuilder_item_9.power = 0.0
    shipBuilder_item_9.energy = 0.0
    shipBuilder_item_9.memory = 0.0
    shipBuilder_item_9.upgrade_slots = 1L
    shipBuilder_item_9.weapon_data = None
    shipBuilder_item_9.cargo_mod_data = None
    shipBuilder_item_9.powerplant_data = shipBuilder_powerplantdata_9
    shipBuilder_item_9.thruster_data = None
    shipBuilder_item_9.shield_data = None
    shipBuilder_item_9.engine_intake_data = None
    shipBuilder_item_9 = importer.save_or_locate(shipBuilder_item_9)

    shipBuilder_item_10 = Item()
    shipBuilder_item_10.name = u'FusionPro 3H III'
    shipBuilder_item_10.rating = 1L
    shipBuilder_item_10.size = 0L
    shipBuilder_item_10.description = u''
    shipBuilder_item_10.manufacturer = shipBuilder_manufacturer_16
    shipBuilder_item_10.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_10.hardpoint_class = 0L
    shipBuilder_item_10.mass = 0.0
    shipBuilder_item_10.item_type = shipBuilder_itemtype_4
    shipBuilder_item_10.power = 0.0
    shipBuilder_item_10.energy = 0.0
    shipBuilder_item_10.memory = 0.0
    shipBuilder_item_10.upgrade_slots = 1L
    shipBuilder_item_10.weapon_data = None
    shipBuilder_item_10.cargo_mod_data = None
    shipBuilder_item_10.powerplant_data = shipBuilder_powerplantdata_9
    shipBuilder_item_10.thruster_data = None
    shipBuilder_item_10.shield_data = None
    shipBuilder_item_10.engine_intake_data = None
    shipBuilder_item_10 = importer.save_or_locate(shipBuilder_item_10)

    shipBuilder_item_11 = Item()
    shipBuilder_item_11.name = u'Etoile-00'
    shipBuilder_item_11.rating = 1L
    shipBuilder_item_11.size = 0L
    shipBuilder_item_11.description = u''
    shipBuilder_item_11.manufacturer = shipBuilder_manufacturer_17
    shipBuilder_item_11.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_11.hardpoint_class = 0L
    shipBuilder_item_11.mass = 0.0
    shipBuilder_item_11.item_type = shipBuilder_itemtype_4
    shipBuilder_item_11.power = 0.0
    shipBuilder_item_11.energy = 0.0
    shipBuilder_item_11.memory = 0.0
    shipBuilder_item_11.upgrade_slots = 1L
    shipBuilder_item_11.weapon_data = None
    shipBuilder_item_11.cargo_mod_data = None
    shipBuilder_item_11.powerplant_data = shipBuilder_powerplantdata_10
    shipBuilder_item_11.thruster_data = None
    shipBuilder_item_11.shield_data = None
    shipBuilder_item_11.engine_intake_data = None
    shipBuilder_item_11 = importer.save_or_locate(shipBuilder_item_11)

    shipBuilder_item_12 = Item()
    shipBuilder_item_12.name = u'HFR2 Plus'
    shipBuilder_item_12.rating = 1L
    shipBuilder_item_12.size = 0L
    shipBuilder_item_12.description = u''
    shipBuilder_item_12.manufacturer = shipBuilder_manufacturer_12
    shipBuilder_item_12.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_12.hardpoint_class = 0L
    shipBuilder_item_12.mass = 0.0
    shipBuilder_item_12.item_type = shipBuilder_itemtype_4
    shipBuilder_item_12.power = 0.0
    shipBuilder_item_12.energy = 0.0
    shipBuilder_item_12.memory = 0.0
    shipBuilder_item_12.upgrade_slots = 1L
    shipBuilder_item_12.weapon_data = None
    shipBuilder_item_12.cargo_mod_data = None
    shipBuilder_item_12.powerplant_data = shipBuilder_powerplantdata_11
    shipBuilder_item_12.thruster_data = None
    shipBuilder_item_12.shield_data = None
    shipBuilder_item_12.engine_intake_data = None
    shipBuilder_item_12 = importer.save_or_locate(shipBuilder_item_12)

    shipBuilder_item_13 = Item()
    shipBuilder_item_13.name = u'Starlight II'
    shipBuilder_item_13.rating = 1L
    shipBuilder_item_13.size = 0L
    shipBuilder_item_13.description = u''
    shipBuilder_item_13.manufacturer = shipBuilder_manufacturer_10
    shipBuilder_item_13.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_13.hardpoint_class = 0L
    shipBuilder_item_13.mass = 0.0
    shipBuilder_item_13.item_type = shipBuilder_itemtype_4
    shipBuilder_item_13.power = 0.0
    shipBuilder_item_13.energy = 0.0
    shipBuilder_item_13.memory = 0.0
    shipBuilder_item_13.upgrade_slots = 1L
    shipBuilder_item_13.weapon_data = None
    shipBuilder_item_13.cargo_mod_data = None
    shipBuilder_item_13.powerplant_data = shipBuilder_powerplantdata_12
    shipBuilder_item_13.thruster_data = None
    shipBuilder_item_13.shield_data = None
    shipBuilder_item_13.engine_intake_data = None
    shipBuilder_item_13 = importer.save_or_locate(shipBuilder_item_13)

    shipBuilder_item_14 = Item()
    shipBuilder_item_14.name = u'Powerbolt'
    shipBuilder_item_14.rating = 1L
    shipBuilder_item_14.size = 0L
    shipBuilder_item_14.description = u''
    shipBuilder_item_14.manufacturer = shipBuilder_manufacturer_18
    shipBuilder_item_14.item_category = shipBuilder_itemcategory_7
    shipBuilder_item_14.hardpoint_class = 0L
    shipBuilder_item_14.mass = 0.0
    shipBuilder_item_14.item_type = shipBuilder_itemtype_4
    shipBuilder_item_14.power = 0.0
    shipBuilder_item_14.energy = 0.0
    shipBuilder_item_14.memory = 0.0
    shipBuilder_item_14.upgrade_slots = 1L
    shipBuilder_item_14.weapon_data = None
    shipBuilder_item_14.cargo_mod_data = None
    shipBuilder_item_14.powerplant_data = shipBuilder_powerplantdata_5
    shipBuilder_item_14.thruster_data = None
    shipBuilder_item_14.shield_data = None
    shipBuilder_item_14.engine_intake_data = None
    shipBuilder_item_14 = importer.save_or_locate(shipBuilder_item_14)

    shipBuilder_item_15 = Item()
    shipBuilder_item_15.name = u'STC Blue'
    shipBuilder_item_15.rating = 1L
    shipBuilder_item_15.size = 0L
    shipBuilder_item_15.description = u''
    shipBuilder_item_15.manufacturer = shipBuilder_manufacturer_8
    shipBuilder_item_15.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_15.hardpoint_class = 0L
    shipBuilder_item_15.mass = 0.0
    shipBuilder_item_15.item_type = shipBuilder_itemtype_4
    shipBuilder_item_15.power = 30.0
    shipBuilder_item_15.energy = 0.0
    shipBuilder_item_15.memory = 0.0
    shipBuilder_item_15.upgrade_slots = 1L
    shipBuilder_item_15.weapon_data = None
    shipBuilder_item_15.cargo_mod_data = None
    shipBuilder_item_15.powerplant_data = None
    shipBuilder_item_15.thruster_data = shipBuilder_thrusterdata_4
    shipBuilder_item_15.shield_data = None
    shipBuilder_item_15.engine_intake_data = None
    shipBuilder_item_15 = importer.save_or_locate(shipBuilder_item_15)

    shipBuilder_item_16 = Item()
    shipBuilder_item_16.name = u'STC Red'
    shipBuilder_item_16.rating = 1L
    shipBuilder_item_16.size = 0L
    shipBuilder_item_16.description = u''
    shipBuilder_item_16.manufacturer = shipBuilder_manufacturer_8
    shipBuilder_item_16.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_16.hardpoint_class = 0L
    shipBuilder_item_16.mass = 0.0
    shipBuilder_item_16.item_type = shipBuilder_itemtype_4
    shipBuilder_item_16.power = 30.0
    shipBuilder_item_16.energy = 0.0
    shipBuilder_item_16.memory = 0.0
    shipBuilder_item_16.upgrade_slots = 1L
    shipBuilder_item_16.weapon_data = None
    shipBuilder_item_16.cargo_mod_data = None
    shipBuilder_item_16.powerplant_data = None
    shipBuilder_item_16.thruster_data = shipBuilder_thrusterdata_2
    shipBuilder_item_16.shield_data = None
    shipBuilder_item_16.engine_intake_data = None
    shipBuilder_item_16 = importer.save_or_locate(shipBuilder_item_16)

    shipBuilder_item_17 = Item()
    shipBuilder_item_17.name = u'P/S2-80'
    shipBuilder_item_17.rating = 1L
    shipBuilder_item_17.size = 0L
    shipBuilder_item_17.description = u''
    shipBuilder_item_17.manufacturer = shipBuilder_manufacturer_19
    shipBuilder_item_17.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_17.hardpoint_class = 0L
    shipBuilder_item_17.mass = 0.0
    shipBuilder_item_17.item_type = shipBuilder_itemtype_4
    shipBuilder_item_17.power = 0.0
    shipBuilder_item_17.energy = 0.0
    shipBuilder_item_17.memory = 0.0
    shipBuilder_item_17.upgrade_slots = 1L
    shipBuilder_item_17.weapon_data = None
    shipBuilder_item_17.cargo_mod_data = None
    shipBuilder_item_17.powerplant_data = None
    shipBuilder_item_17.thruster_data = shipBuilder_thrusterdata_1
    shipBuilder_item_17.shield_data = None
    shipBuilder_item_17.engine_intake_data = None
    shipBuilder_item_17 = importer.save_or_locate(shipBuilder_item_17)

    shipBuilder_item_18 = Item()
    shipBuilder_item_18.name = u'Energia IV'
    shipBuilder_item_18.rating = 1L
    shipBuilder_item_18.size = 0L
    shipBuilder_item_18.description = u''
    shipBuilder_item_18.manufacturer = shipBuilder_manufacturer_20
    shipBuilder_item_18.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_18.hardpoint_class = 0L
    shipBuilder_item_18.mass = 0.0
    shipBuilder_item_18.item_type = shipBuilder_itemtype_4
    shipBuilder_item_18.power = 30.0
    shipBuilder_item_18.energy = 0.0
    shipBuilder_item_18.memory = 0.0
    shipBuilder_item_18.upgrade_slots = 1L
    shipBuilder_item_18.weapon_data = None
    shipBuilder_item_18.cargo_mod_data = None
    shipBuilder_item_18.powerplant_data = None
    shipBuilder_item_18.thruster_data = shipBuilder_thrusterdata_2
    shipBuilder_item_18.shield_data = None
    shipBuilder_item_18.engine_intake_data = None
    shipBuilder_item_18 = importer.save_or_locate(shipBuilder_item_18)

    shipBuilder_item_19 = Item()
    shipBuilder_item_19.name = u'HE 5.3'
    shipBuilder_item_19.rating = 1L
    shipBuilder_item_19.size = 0L
    shipBuilder_item_19.description = u''
    shipBuilder_item_19.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_item_19.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_19.hardpoint_class = 0L
    shipBuilder_item_19.mass = 0.0
    shipBuilder_item_19.item_type = shipBuilder_itemtype_4
    shipBuilder_item_19.power = 30.0
    shipBuilder_item_19.energy = 0.0
    shipBuilder_item_19.memory = 0.0
    shipBuilder_item_19.upgrade_slots = 1L
    shipBuilder_item_19.weapon_data = None
    shipBuilder_item_19.cargo_mod_data = None
    shipBuilder_item_19.powerplant_data = None
    shipBuilder_item_19.thruster_data = shipBuilder_thrusterdata_2
    shipBuilder_item_19.shield_data = None
    shipBuilder_item_19.engine_intake_data = None
    shipBuilder_item_19 = importer.save_or_locate(shipBuilder_item_19)

    shipBuilder_item_20 = Item()
    shipBuilder_item_20.name = u'STC Silver'
    shipBuilder_item_20.rating = 1L
    shipBuilder_item_20.size = 0L
    shipBuilder_item_20.description = u''
    shipBuilder_item_20.manufacturer = shipBuilder_manufacturer_8
    shipBuilder_item_20.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_20.hardpoint_class = 0L
    shipBuilder_item_20.mass = 0.0
    shipBuilder_item_20.item_type = shipBuilder_itemtype_4
    shipBuilder_item_20.power = 40.0
    shipBuilder_item_20.energy = 0.0
    shipBuilder_item_20.memory = 0.0
    shipBuilder_item_20.upgrade_slots = 1L
    shipBuilder_item_20.weapon_data = None
    shipBuilder_item_20.cargo_mod_data = None
    shipBuilder_item_20.powerplant_data = None
    shipBuilder_item_20.thruster_data = shipBuilder_thrusterdata_3
    shipBuilder_item_20.shield_data = None
    shipBuilder_item_20.engine_intake_data = None
    shipBuilder_item_20 = importer.save_or_locate(shipBuilder_item_20)

    shipBuilder_item_21 = Item()
    shipBuilder_item_21.name = u'HM 4.3'
    shipBuilder_item_21.rating = 1L
    shipBuilder_item_21.size = 0L
    shipBuilder_item_21.description = u''
    shipBuilder_item_21.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_item_21.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_21.hardpoint_class = 0L
    shipBuilder_item_21.mass = 0.0
    shipBuilder_item_21.item_type = shipBuilder_itemtype_4
    shipBuilder_item_21.power = 30.0
    shipBuilder_item_21.energy = 0.0
    shipBuilder_item_21.memory = 0.0
    shipBuilder_item_21.upgrade_slots = 1L
    shipBuilder_item_21.weapon_data = None
    shipBuilder_item_21.cargo_mod_data = None
    shipBuilder_item_21.powerplant_data = None
    shipBuilder_item_21.thruster_data = shipBuilder_thrusterdata_1
    shipBuilder_item_21.shield_data = None
    shipBuilder_item_21.engine_intake_data = None
    shipBuilder_item_21 = importer.save_or_locate(shipBuilder_item_21)

    shipBuilder_item_22 = Item()
    shipBuilder_item_22.name = u'HM 4.4'
    shipBuilder_item_22.rating = 1L
    shipBuilder_item_22.size = 0L
    shipBuilder_item_22.description = u''
    shipBuilder_item_22.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_item_22.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_22.hardpoint_class = 0L
    shipBuilder_item_22.mass = 0.0
    shipBuilder_item_22.item_type = shipBuilder_itemtype_4
    shipBuilder_item_22.power = 40.0
    shipBuilder_item_22.energy = 0.0
    shipBuilder_item_22.memory = 0.0
    shipBuilder_item_22.upgrade_slots = 1L
    shipBuilder_item_22.weapon_data = None
    shipBuilder_item_22.cargo_mod_data = None
    shipBuilder_item_22.powerplant_data = None
    shipBuilder_item_22.thruster_data = shipBuilder_thrusterdata_3
    shipBuilder_item_22.shield_data = None
    shipBuilder_item_22.engine_intake_data = None
    shipBuilder_item_22 = importer.save_or_locate(shipBuilder_item_22)

    shipBuilder_item_23 = Item()
    shipBuilder_item_23.name = u'Arc Duo 400'
    shipBuilder_item_23.rating = 1L
    shipBuilder_item_23.size = 0L
    shipBuilder_item_23.description = u''
    shipBuilder_item_23.manufacturer = shipBuilder_manufacturer_21
    shipBuilder_item_23.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_23.hardpoint_class = 0L
    shipBuilder_item_23.mass = 0.0
    shipBuilder_item_23.item_type = shipBuilder_itemtype_4
    shipBuilder_item_23.power = 40.0
    shipBuilder_item_23.energy = 0.0
    shipBuilder_item_23.memory = 0.0
    shipBuilder_item_23.upgrade_slots = 1L
    shipBuilder_item_23.weapon_data = None
    shipBuilder_item_23.cargo_mod_data = None
    shipBuilder_item_23.powerplant_data = None
    shipBuilder_item_23.thruster_data = shipBuilder_thrusterdata_3
    shipBuilder_item_23.shield_data = None
    shipBuilder_item_23.engine_intake_data = None
    shipBuilder_item_23 = importer.save_or_locate(shipBuilder_item_23)

    shipBuilder_item_24 = Item()
    shipBuilder_item_24.name = u'HE 5.5'
    shipBuilder_item_24.rating = 1L
    shipBuilder_item_24.size = 0L
    shipBuilder_item_24.description = u''
    shipBuilder_item_24.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_item_24.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_24.hardpoint_class = 0L
    shipBuilder_item_24.mass = 0.0
    shipBuilder_item_24.item_type = shipBuilder_itemtype_4
    shipBuilder_item_24.power = 50.0
    shipBuilder_item_24.energy = 0.0
    shipBuilder_item_24.memory = 0.0
    shipBuilder_item_24.upgrade_slots = 1L
    shipBuilder_item_24.weapon_data = None
    shipBuilder_item_24.cargo_mod_data = None
    shipBuilder_item_24.powerplant_data = None
    shipBuilder_item_24.thruster_data = shipBuilder_thrusterdata_5
    shipBuilder_item_24.shield_data = None
    shipBuilder_item_24.engine_intake_data = None
    shipBuilder_item_24 = importer.save_or_locate(shipBuilder_item_24)

    shipBuilder_item_25 = Item()
    shipBuilder_item_25.name = u'HM 4.1'
    shipBuilder_item_25.rating = 1L
    shipBuilder_item_25.size = 0L
    shipBuilder_item_25.description = u''
    shipBuilder_item_25.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_item_25.item_category = shipBuilder_itemcategory_6
    shipBuilder_item_25.hardpoint_class = 0L
    shipBuilder_item_25.mass = 0.0
    shipBuilder_item_25.item_type = shipBuilder_itemtype_4
    shipBuilder_item_25.power = 10.0
    shipBuilder_item_25.energy = 0.0
    shipBuilder_item_25.memory = 0.0
    shipBuilder_item_25.upgrade_slots = 1L
    shipBuilder_item_25.weapon_data = None
    shipBuilder_item_25.cargo_mod_data = None
    shipBuilder_item_25.powerplant_data = None
    shipBuilder_item_25.thruster_data = shipBuilder_thrusterdata_6
    shipBuilder_item_25.shield_data = None
    shipBuilder_item_25.engine_intake_data = None
    shipBuilder_item_25 = importer.save_or_locate(shipBuilder_item_25)

    shipBuilder_item_26 = Item()
    shipBuilder_item_26.name = u'INK-1'
    shipBuilder_item_26.rating = 1L
    shipBuilder_item_26.size = 0L
    shipBuilder_item_26.description = u''
    shipBuilder_item_26.manufacturer = shipBuilder_manufacturer_22
    shipBuilder_item_26.item_category = shipBuilder_itemcategory_9
    shipBuilder_item_26.hardpoint_class = 0L
    shipBuilder_item_26.mass = 0.0
    shipBuilder_item_26.item_type = shipBuilder_itemtype_3
    shipBuilder_item_26.power = 0.0
    shipBuilder_item_26.energy = 0.0
    shipBuilder_item_26.memory = 0.0
    shipBuilder_item_26.upgrade_slots = 1L
    shipBuilder_item_26.weapon_data = None
    shipBuilder_item_26.cargo_mod_data = None
    shipBuilder_item_26.powerplant_data = None
    shipBuilder_item_26.thruster_data = None
    shipBuilder_item_26.shield_data = shipBuilder_shielddata_1
    shipBuilder_item_26.engine_intake_data = None
    shipBuilder_item_26 = importer.save_or_locate(shipBuilder_item_26)

    shipBuilder_item_27 = Item()
    shipBuilder_item_27.name = u'6S7A'
    shipBuilder_item_27.rating = 1L
    shipBuilder_item_27.size = 0L
    shipBuilder_item_27.description = u''
    shipBuilder_item_27.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_27.item_category = shipBuilder_itemcategory_9
    shipBuilder_item_27.hardpoint_class = 0L
    shipBuilder_item_27.mass = 0.0
    shipBuilder_item_27.item_type = shipBuilder_itemtype_3
    shipBuilder_item_27.power = 0.0
    shipBuilder_item_27.energy = 0.0
    shipBuilder_item_27.memory = 0.0
    shipBuilder_item_27.upgrade_slots = 1L
    shipBuilder_item_27.weapon_data = None
    shipBuilder_item_27.cargo_mod_data = None
    shipBuilder_item_27.powerplant_data = None
    shipBuilder_item_27.thruster_data = None
    shipBuilder_item_27.shield_data = shipBuilder_shielddata_2
    shipBuilder_item_27.engine_intake_data = None
    shipBuilder_item_27 = importer.save_or_locate(shipBuilder_item_27)

    shipBuilder_item_28 = Item()
    shipBuilder_item_28.name = u'GH-146m'
    shipBuilder_item_28.rating = 1L
    shipBuilder_item_28.size = 0L
    shipBuilder_item_28.description = u''
    shipBuilder_item_28.manufacturer = shipBuilder_manufacturer_23
    shipBuilder_item_28.item_category = shipBuilder_itemcategory_9
    shipBuilder_item_28.hardpoint_class = 0L
    shipBuilder_item_28.mass = 0.0
    shipBuilder_item_28.item_type = shipBuilder_itemtype_3
    shipBuilder_item_28.power = 0.0
    shipBuilder_item_28.energy = 0.0
    shipBuilder_item_28.memory = 0.0
    shipBuilder_item_28.upgrade_slots = 1L
    shipBuilder_item_28.weapon_data = None
    shipBuilder_item_28.cargo_mod_data = None
    shipBuilder_item_28.powerplant_data = None
    shipBuilder_item_28.thruster_data = None
    shipBuilder_item_28.shield_data = shipBuilder_shielddata_3
    shipBuilder_item_28.engine_intake_data = None
    shipBuilder_item_28 = importer.save_or_locate(shipBuilder_item_28)

    shipBuilder_item_29 = Item()
    shipBuilder_item_29.name = u'AllStop FR'
    shipBuilder_item_29.rating = 1L
    shipBuilder_item_29.size = 0L
    shipBuilder_item_29.description = u''
    shipBuilder_item_29.manufacturer = shipBuilder_manufacturer_9
    shipBuilder_item_29.item_category = shipBuilder_itemcategory_9
    shipBuilder_item_29.hardpoint_class = 0L
    shipBuilder_item_29.mass = 0.0
    shipBuilder_item_29.item_type = shipBuilder_itemtype_3
    shipBuilder_item_29.power = 0.0
    shipBuilder_item_29.energy = 0.0
    shipBuilder_item_29.memory = 0.0
    shipBuilder_item_29.upgrade_slots = 1L
    shipBuilder_item_29.weapon_data = None
    shipBuilder_item_29.cargo_mod_data = None
    shipBuilder_item_29.powerplant_data = None
    shipBuilder_item_29.thruster_data = None
    shipBuilder_item_29.shield_data = shipBuilder_shielddata_4
    shipBuilder_item_29.engine_intake_data = None
    shipBuilder_item_29 = importer.save_or_locate(shipBuilder_item_29)

    shipBuilder_item_30 = Item()
    shipBuilder_item_30.name = u'AllStop'
    shipBuilder_item_30.rating = 1L
    shipBuilder_item_30.size = 0L
    shipBuilder_item_30.description = u''
    shipBuilder_item_30.manufacturer = shipBuilder_manufacturer_9
    shipBuilder_item_30.item_category = shipBuilder_itemcategory_9
    shipBuilder_item_30.hardpoint_class = 0L
    shipBuilder_item_30.mass = 0.0
    shipBuilder_item_30.item_type = shipBuilder_itemtype_3
    shipBuilder_item_30.power = 0.0
    shipBuilder_item_30.energy = 0.0
    shipBuilder_item_30.memory = 0.0
    shipBuilder_item_30.upgrade_slots = 1L
    shipBuilder_item_30.weapon_data = None
    shipBuilder_item_30.cargo_mod_data = None
    shipBuilder_item_30.powerplant_data = None
    shipBuilder_item_30.thruster_data = None
    shipBuilder_item_30.shield_data = shipBuilder_shielddata_5
    shipBuilder_item_30.engine_intake_data = None
    shipBuilder_item_30 = importer.save_or_locate(shipBuilder_item_30)

    shipBuilder_item_31 = Item()
    shipBuilder_item_31.name = u'ForceWall'
    shipBuilder_item_31.rating = 1L
    shipBuilder_item_31.size = 0L
    shipBuilder_item_31.description = u''
    shipBuilder_item_31.manufacturer = shipBuilder_manufacturer_9
    shipBuilder_item_31.item_category = shipBuilder_itemcategory_9
    shipBuilder_item_31.hardpoint_class = 0L
    shipBuilder_item_31.mass = 0.0
    shipBuilder_item_31.item_type = shipBuilder_itemtype_3
    shipBuilder_item_31.power = 0.0
    shipBuilder_item_31.energy = 0.0
    shipBuilder_item_31.memory = 0.0
    shipBuilder_item_31.upgrade_slots = 1L
    shipBuilder_item_31.weapon_data = None
    shipBuilder_item_31.cargo_mod_data = None
    shipBuilder_item_31.powerplant_data = None
    shipBuilder_item_31.thruster_data = None
    shipBuilder_item_31.shield_data = shipBuilder_shielddata_6
    shipBuilder_item_31.engine_intake_data = None
    shipBuilder_item_31 = importer.save_or_locate(shipBuilder_item_31)

    shipBuilder_item_32 = Item()
    shipBuilder_item_32.name = u'Mini'
    shipBuilder_item_32.rating = 1L
    shipBuilder_item_32.size = 0L
    shipBuilder_item_32.description = u''
    shipBuilder_item_32.manufacturer = shipBuilder_manufacturer_24
    shipBuilder_item_32.item_category = shipBuilder_itemcategory_8
    shipBuilder_item_32.hardpoint_class = 0L
    shipBuilder_item_32.mass = 0.0
    shipBuilder_item_32.item_type = shipBuilder_itemtype_3
    shipBuilder_item_32.power = 0.0
    shipBuilder_item_32.energy = 0.0
    shipBuilder_item_32.memory = 0.0
    shipBuilder_item_32.upgrade_slots = 1L
    shipBuilder_item_32.weapon_data = None
    shipBuilder_item_32.cargo_mod_data = shipBuilder_cargomoddata_1
    shipBuilder_item_32.powerplant_data = None
    shipBuilder_item_32.thruster_data = None
    shipBuilder_item_32.shield_data = None
    shipBuilder_item_32.engine_intake_data = None
    shipBuilder_item_32 = importer.save_or_locate(shipBuilder_item_32)

    shipBuilder_item_33 = Item()
    shipBuilder_item_33.name = u'Big Box (Model A)'
    shipBuilder_item_33.rating = 1L
    shipBuilder_item_33.size = 0L
    shipBuilder_item_33.description = u''
    shipBuilder_item_33.manufacturer = shipBuilder_manufacturer_24
    shipBuilder_item_33.item_category = shipBuilder_itemcategory_8
    shipBuilder_item_33.hardpoint_class = 0L
    shipBuilder_item_33.mass = 0.0
    shipBuilder_item_33.item_type = shipBuilder_itemtype_3
    shipBuilder_item_33.power = 0.0
    shipBuilder_item_33.energy = 0.0
    shipBuilder_item_33.memory = 0.0
    shipBuilder_item_33.upgrade_slots = 1L
    shipBuilder_item_33.weapon_data = None
    shipBuilder_item_33.cargo_mod_data = shipBuilder_cargomoddata_2
    shipBuilder_item_33.powerplant_data = None
    shipBuilder_item_33.thruster_data = None
    shipBuilder_item_33.shield_data = None
    shipBuilder_item_33.engine_intake_data = None
    shipBuilder_item_33 = importer.save_or_locate(shipBuilder_item_33)

    shipBuilder_item_34 = Item()
    shipBuilder_item_34.name = u'Omni-Cool Reduction Bar'
    shipBuilder_item_34.rating = 1L
    shipBuilder_item_34.size = 0L
    shipBuilder_item_34.description = u''
    shipBuilder_item_34.manufacturer = shipBuilder_manufacturer_25
    shipBuilder_item_34.item_category = shipBuilder_itemcategory_4
    shipBuilder_item_34.hardpoint_class = 0L
    shipBuilder_item_34.mass = 0.0
    shipBuilder_item_34.item_type = shipBuilder_itemtype_3
    shipBuilder_item_34.power = 0.0
    shipBuilder_item_34.energy = 0.0
    shipBuilder_item_34.memory = 0.0
    shipBuilder_item_34.upgrade_slots = 1L
    shipBuilder_item_34.weapon_data = None
    shipBuilder_item_34.cargo_mod_data = None
    shipBuilder_item_34.powerplant_data = None
    shipBuilder_item_34.thruster_data = None
    shipBuilder_item_34.shield_data = None
    shipBuilder_item_34.engine_intake_data = None
    shipBuilder_item_34 = importer.save_or_locate(shipBuilder_item_34)

    shipBuilder_item_35 = Item()
    shipBuilder_item_35.name = u'AT Jump Scanner'
    shipBuilder_item_35.rating = 1L
    shipBuilder_item_35.size = 0L
    shipBuilder_item_35.description = u''
    shipBuilder_item_35.manufacturer = shipBuilder_manufacturer_26
    shipBuilder_item_35.item_category = shipBuilder_itemcategory_4
    shipBuilder_item_35.hardpoint_class = 0L
    shipBuilder_item_35.mass = 0.0
    shipBuilder_item_35.item_type = shipBuilder_itemtype_3
    shipBuilder_item_35.power = 0.0
    shipBuilder_item_35.energy = 0.0
    shipBuilder_item_35.memory = 0.0
    shipBuilder_item_35.upgrade_slots = 1L
    shipBuilder_item_35.weapon_data = None
    shipBuilder_item_35.cargo_mod_data = None
    shipBuilder_item_35.powerplant_data = None
    shipBuilder_item_35.thruster_data = None
    shipBuilder_item_35.shield_data = None
    shipBuilder_item_35.engine_intake_data = None
    shipBuilder_item_35 = importer.save_or_locate(shipBuilder_item_35)

    shipBuilder_item_36 = Item()
    shipBuilder_item_36.name = u'Jump Engine'
    shipBuilder_item_36.rating = 1L
    shipBuilder_item_36.size = 0L
    shipBuilder_item_36.description = u''
    shipBuilder_item_36.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_item_36.item_category = shipBuilder_itemcategory_5
    shipBuilder_item_36.hardpoint_class = 0L
    shipBuilder_item_36.mass = 0.0
    shipBuilder_item_36.item_type = shipBuilder_itemtype_4
    shipBuilder_item_36.power = 0.0
    shipBuilder_item_36.energy = 0.0
    shipBuilder_item_36.memory = 0.0
    shipBuilder_item_36.upgrade_slots = 1L
    shipBuilder_item_36.weapon_data = None
    shipBuilder_item_36.cargo_mod_data = None
    shipBuilder_item_36.powerplant_data = None
    shipBuilder_item_36.thruster_data = None
    shipBuilder_item_36.shield_data = None
    shipBuilder_item_36.engine_intake_data = None
    shipBuilder_item_36 = importer.save_or_locate(shipBuilder_item_36)

    shipBuilder_item_37 = Item()
    shipBuilder_item_37.name = u'Big Box (Model H)'
    shipBuilder_item_37.rating = 1L
    shipBuilder_item_37.size = 0L
    shipBuilder_item_37.description = u''
    shipBuilder_item_37.manufacturer = shipBuilder_manufacturer_24
    shipBuilder_item_37.item_category = shipBuilder_itemcategory_4
    shipBuilder_item_37.hardpoint_class = 0L
    shipBuilder_item_37.mass = 0.0
    shipBuilder_item_37.item_type = shipBuilder_itemtype_3
    shipBuilder_item_37.power = 0.0
    shipBuilder_item_37.energy = 0.0
    shipBuilder_item_37.memory = 0.0
    shipBuilder_item_37.upgrade_slots = 1L
    shipBuilder_item_37.weapon_data = None
    shipBuilder_item_37.cargo_mod_data = shipBuilder_cargomoddata_3
    shipBuilder_item_37.powerplant_data = None
    shipBuilder_item_37.thruster_data = None
    shipBuilder_item_37.shield_data = None
    shipBuilder_item_37.engine_intake_data = None
    shipBuilder_item_37 = importer.save_or_locate(shipBuilder_item_37)

    shipBuilder_item_38 = Item()
    shipBuilder_item_38.name = u'Leaper Jump Engine'
    shipBuilder_item_38.rating = 1L
    shipBuilder_item_38.size = 0L
    shipBuilder_item_38.description = u''
    shipBuilder_item_38.manufacturer = shipBuilder_manufacturer_26
    shipBuilder_item_38.item_category = shipBuilder_itemcategory_5
    shipBuilder_item_38.hardpoint_class = 0L
    shipBuilder_item_38.mass = 0.0
    shipBuilder_item_38.item_type = shipBuilder_itemtype_4
    shipBuilder_item_38.power = 0.0
    shipBuilder_item_38.energy = 0.0
    shipBuilder_item_38.memory = 0.0
    shipBuilder_item_38.upgrade_slots = 1L
    shipBuilder_item_38.weapon_data = None
    shipBuilder_item_38.cargo_mod_data = None
    shipBuilder_item_38.powerplant_data = None
    shipBuilder_item_38.thruster_data = None
    shipBuilder_item_38.shield_data = None
    shipBuilder_item_38.engine_intake_data = None
    shipBuilder_item_38 = importer.save_or_locate(shipBuilder_item_38)

    shipBuilder_item_39 = Item()
    shipBuilder_item_39.name = u'Mark III Tractor'
    shipBuilder_item_39.rating = 1L
    shipBuilder_item_39.size = 0L
    shipBuilder_item_39.description = u''
    shipBuilder_item_39.manufacturer = shipBuilder_manufacturer_28
    shipBuilder_item_39.item_category = shipBuilder_itemcategory_3
    shipBuilder_item_39.hardpoint_class = 0L
    shipBuilder_item_39.mass = 0.0
    shipBuilder_item_39.item_type = shipBuilder_itemtype_2
    shipBuilder_item_39.power = 0.0
    shipBuilder_item_39.energy = 0.0
    shipBuilder_item_39.memory = 0.0
    shipBuilder_item_39.upgrade_slots = 1L
    shipBuilder_item_39.weapon_data = None
    shipBuilder_item_39.cargo_mod_data = None
    shipBuilder_item_39.powerplant_data = None
    shipBuilder_item_39.thruster_data = None
    shipBuilder_item_39.shield_data = None
    shipBuilder_item_39.engine_intake_data = None
    shipBuilder_item_39 = importer.save_or_locate(shipBuilder_item_39)

    shipBuilder_item_40 = Item()
    shipBuilder_item_40.name = u'M3A Laser'
    shipBuilder_item_40.rating = 1L
    shipBuilder_item_40.size = 0L
    shipBuilder_item_40.description = u''
    shipBuilder_item_40.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_40.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_40.hardpoint_class = 1L
    shipBuilder_item_40.mass = 0.0
    shipBuilder_item_40.item_type = shipBuilder_itemtype_1
    shipBuilder_item_40.power = 0.0
    shipBuilder_item_40.energy = 0.0
    shipBuilder_item_40.memory = 0.0
    shipBuilder_item_40.upgrade_slots = 1L
    shipBuilder_item_40.weapon_data = None
    shipBuilder_item_40.cargo_mod_data = None
    shipBuilder_item_40.powerplant_data = None
    shipBuilder_item_40.thruster_data = None
    shipBuilder_item_40.shield_data = None
    shipBuilder_item_40.engine_intake_data = None
    shipBuilder_item_40 = importer.save_or_locate(shipBuilder_item_40)

    shipBuilder_item_41 = Item()
    shipBuilder_item_41.name = u'Bulldog Repeater'
    shipBuilder_item_41.rating = 1L
    shipBuilder_item_41.size = 0L
    shipBuilder_item_41.description = u''
    shipBuilder_item_41.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_41.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_41.hardpoint_class = 1L
    shipBuilder_item_41.mass = 0.0
    shipBuilder_item_41.item_type = shipBuilder_itemtype_1
    shipBuilder_item_41.power = 0.0
    shipBuilder_item_41.energy = 0.0
    shipBuilder_item_41.memory = 0.0
    shipBuilder_item_41.upgrade_slots = 1L
    shipBuilder_item_41.weapon_data = None
    shipBuilder_item_41.cargo_mod_data = None
    shipBuilder_item_41.powerplant_data = None
    shipBuilder_item_41.thruster_data = None
    shipBuilder_item_41.shield_data = None
    shipBuilder_item_41.engine_intake_data = None
    shipBuilder_item_41 = importer.save_or_locate(shipBuilder_item_41)

    shipBuilder_item_42 = Item()
    shipBuilder_item_42.name = u'Marksman HS 4-Pack'
    shipBuilder_item_42.rating = 1L
    shipBuilder_item_42.size = 0L
    shipBuilder_item_42.description = u''
    shipBuilder_item_42.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_42.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_42.hardpoint_class = 3L
    shipBuilder_item_42.mass = 0.0
    shipBuilder_item_42.item_type = shipBuilder_itemtype_1
    shipBuilder_item_42.power = 0.0
    shipBuilder_item_42.energy = 0.0
    shipBuilder_item_42.memory = 0.0
    shipBuilder_item_42.upgrade_slots = 1L
    shipBuilder_item_42.weapon_data = shipBuilder_weapondata_2
    shipBuilder_item_42.cargo_mod_data = None
    shipBuilder_item_42.powerplant_data = None
    shipBuilder_item_42.thruster_data = None
    shipBuilder_item_42.shield_data = None
    shipBuilder_item_42.engine_intake_data = None
    shipBuilder_item_42 = importer.save_or_locate(shipBuilder_item_42)

    shipBuilder_item_43 = Item()
    shipBuilder_item_43.name = u'Omnisky VI'
    shipBuilder_item_43.rating = 1L
    shipBuilder_item_43.size = 0L
    shipBuilder_item_43.description = u''
    shipBuilder_item_43.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_item_43.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_43.hardpoint_class = 1L
    shipBuilder_item_43.mass = 0.0
    shipBuilder_item_43.item_type = shipBuilder_itemtype_1
    shipBuilder_item_43.power = 0.0
    shipBuilder_item_43.energy = 0.0
    shipBuilder_item_43.memory = 0.0
    shipBuilder_item_43.upgrade_slots = 1L
    shipBuilder_item_43.weapon_data = None
    shipBuilder_item_43.cargo_mod_data = None
    shipBuilder_item_43.powerplant_data = None
    shipBuilder_item_43.thruster_data = None
    shipBuilder_item_43.shield_data = None
    shipBuilder_item_43.engine_intake_data = None
    shipBuilder_item_43 = importer.save_or_locate(shipBuilder_item_43)

    shipBuilder_item_44 = Item()
    shipBuilder_item_44.name = u'Sure Grip Tractor'
    shipBuilder_item_44.rating = 1L
    shipBuilder_item_44.size = 0L
    shipBuilder_item_44.description = u''
    shipBuilder_item_44.manufacturer = shipBuilder_manufacturer_29
    shipBuilder_item_44.item_category = shipBuilder_itemcategory_3
    shipBuilder_item_44.hardpoint_class = 2L
    shipBuilder_item_44.mass = 0.0
    shipBuilder_item_44.item_type = shipBuilder_itemtype_2
    shipBuilder_item_44.power = 0.0
    shipBuilder_item_44.energy = 0.0
    shipBuilder_item_44.memory = 0.0
    shipBuilder_item_44.upgrade_slots = 1L
    shipBuilder_item_44.weapon_data = None
    shipBuilder_item_44.cargo_mod_data = None
    shipBuilder_item_44.powerplant_data = None
    shipBuilder_item_44.thruster_data = None
    shipBuilder_item_44.shield_data = None
    shipBuilder_item_44.engine_intake_data = None
    shipBuilder_item_44 = importer.save_or_locate(shipBuilder_item_44)

    shipBuilder_item_45 = Item()
    shipBuilder_item_45.name = u'Mass Driver'
    shipBuilder_item_45.rating = 1L
    shipBuilder_item_45.size = 0L
    shipBuilder_item_45.description = u''
    shipBuilder_item_45.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_45.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_45.hardpoint_class = 2L
    shipBuilder_item_45.mass = 0.0
    shipBuilder_item_45.item_type = shipBuilder_itemtype_1
    shipBuilder_item_45.power = 0.0
    shipBuilder_item_45.energy = 0.0
    shipBuilder_item_45.memory = 0.0
    shipBuilder_item_45.upgrade_slots = 1L
    shipBuilder_item_45.weapon_data = None
    shipBuilder_item_45.cargo_mod_data = None
    shipBuilder_item_45.powerplant_data = None
    shipBuilder_item_45.thruster_data = None
    shipBuilder_item_45.shield_data = None
    shipBuilder_item_45.engine_intake_data = None
    shipBuilder_item_45 = importer.save_or_locate(shipBuilder_item_45)

    shipBuilder_item_46 = Item()
    shipBuilder_item_46.name = u'Stalker IR Twin'
    shipBuilder_item_46.rating = 1L
    shipBuilder_item_46.size = 0L
    shipBuilder_item_46.description = u''
    shipBuilder_item_46.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_item_46.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_46.hardpoint_class = 3L
    shipBuilder_item_46.mass = 0.0
    shipBuilder_item_46.item_type = shipBuilder_itemtype_1
    shipBuilder_item_46.power = 0.0
    shipBuilder_item_46.energy = 0.0
    shipBuilder_item_46.memory = 0.0
    shipBuilder_item_46.upgrade_slots = 1L
    shipBuilder_item_46.weapon_data = shipBuilder_weapondata_1
    shipBuilder_item_46.cargo_mod_data = None
    shipBuilder_item_46.powerplant_data = None
    shipBuilder_item_46.thruster_data = None
    shipBuilder_item_46.shield_data = None
    shipBuilder_item_46.engine_intake_data = None
    shipBuilder_item_46 = importer.save_or_locate(shipBuilder_item_46)

    shipBuilder_item_47 = Item()
    shipBuilder_item_47.name = u'Omnisky III'
    shipBuilder_item_47.rating = 1L
    shipBuilder_item_47.size = 0L
    shipBuilder_item_47.description = u''
    shipBuilder_item_47.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_item_47.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_47.hardpoint_class = 1L
    shipBuilder_item_47.mass = 0.0
    shipBuilder_item_47.item_type = shipBuilder_itemtype_1
    shipBuilder_item_47.power = 0.0
    shipBuilder_item_47.energy = 0.0
    shipBuilder_item_47.memory = 0.0
    shipBuilder_item_47.upgrade_slots = 1L
    shipBuilder_item_47.weapon_data = None
    shipBuilder_item_47.cargo_mod_data = None
    shipBuilder_item_47.powerplant_data = None
    shipBuilder_item_47.thruster_data = None
    shipBuilder_item_47.shield_data = None
    shipBuilder_item_47.engine_intake_data = None
    shipBuilder_item_47 = importer.save_or_locate(shipBuilder_item_47)

    shipBuilder_item_48 = Item()
    shipBuilder_item_48.name = u'NN-13 Neutron'
    shipBuilder_item_48.rating = 1L
    shipBuilder_item_48.size = 0L
    shipBuilder_item_48.description = u''
    shipBuilder_item_48.manufacturer = shipBuilder_manufacturer_30
    shipBuilder_item_48.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_48.hardpoint_class = 1L
    shipBuilder_item_48.mass = 0.0
    shipBuilder_item_48.item_type = shipBuilder_itemtype_1
    shipBuilder_item_48.power = 0.0
    shipBuilder_item_48.energy = 0.0
    shipBuilder_item_48.memory = 0.0
    shipBuilder_item_48.upgrade_slots = 1L
    shipBuilder_item_48.weapon_data = None
    shipBuilder_item_48.cargo_mod_data = None
    shipBuilder_item_48.powerplant_data = None
    shipBuilder_item_48.thruster_data = None
    shipBuilder_item_48.shield_data = None
    shipBuilder_item_48.engine_intake_data = None
    shipBuilder_item_48 = importer.save_or_locate(shipBuilder_item_48)

    shipBuilder_item_49 = Item()
    shipBuilder_item_49.name = u'Mantis GT-220'
    shipBuilder_item_49.rating = 1L
    shipBuilder_item_49.size = 0L
    shipBuilder_item_49.description = u''
    shipBuilder_item_49.manufacturer = shipBuilder_manufacturer_31
    shipBuilder_item_49.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_49.hardpoint_class = 2L
    shipBuilder_item_49.mass = 0.0
    shipBuilder_item_49.item_type = shipBuilder_itemtype_1
    shipBuilder_item_49.power = 0.0
    shipBuilder_item_49.energy = 0.0
    shipBuilder_item_49.memory = 0.0
    shipBuilder_item_49.upgrade_slots = 1L
    shipBuilder_item_49.weapon_data = None
    shipBuilder_item_49.cargo_mod_data = None
    shipBuilder_item_49.powerplant_data = None
    shipBuilder_item_49.thruster_data = None
    shipBuilder_item_49.shield_data = None
    shipBuilder_item_49.engine_intake_data = None
    shipBuilder_item_49 = importer.save_or_locate(shipBuilder_item_49)

    shipBuilder_item_50 = Item()
    shipBuilder_item_50.name = u'Dominator FF'
    shipBuilder_item_50.rating = 1L
    shipBuilder_item_50.size = 0L
    shipBuilder_item_50.description = u''
    shipBuilder_item_50.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_item_50.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_50.hardpoint_class = 3L
    shipBuilder_item_50.mass = 0.0
    shipBuilder_item_50.item_type = shipBuilder_itemtype_1
    shipBuilder_item_50.power = 0.0
    shipBuilder_item_50.energy = 0.0
    shipBuilder_item_50.memory = 0.0
    shipBuilder_item_50.upgrade_slots = 1L
    shipBuilder_item_50.weapon_data = shipBuilder_weapondata_3
    shipBuilder_item_50.cargo_mod_data = None
    shipBuilder_item_50.powerplant_data = None
    shipBuilder_item_50.thruster_data = None
    shipBuilder_item_50.shield_data = None
    shipBuilder_item_50.engine_intake_data = None
    shipBuilder_item_50 = importer.save_or_locate(shipBuilder_item_50)

    shipBuilder_item_51 = Item()
    shipBuilder_item_51.name = u'CF-117 Badger'
    shipBuilder_item_51.rating = 1L
    shipBuilder_item_51.size = 0L
    shipBuilder_item_51.description = u''
    shipBuilder_item_51.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_51.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_51.hardpoint_class = 2L
    shipBuilder_item_51.mass = 0.0
    shipBuilder_item_51.item_type = shipBuilder_itemtype_1
    shipBuilder_item_51.power = 0.0
    shipBuilder_item_51.energy = 0.0
    shipBuilder_item_51.memory = 0.0
    shipBuilder_item_51.upgrade_slots = 1L
    shipBuilder_item_51.weapon_data = None
    shipBuilder_item_51.cargo_mod_data = None
    shipBuilder_item_51.powerplant_data = None
    shipBuilder_item_51.thruster_data = None
    shipBuilder_item_51.shield_data = None
    shipBuilder_item_51.engine_intake_data = None
    shipBuilder_item_51 = importer.save_or_locate(shipBuilder_item_51)

    shipBuilder_item_52 = Item()
    shipBuilder_item_52.name = u'Mk VI Laser'
    shipBuilder_item_52.rating = 1L
    shipBuilder_item_52.size = 3L
    shipBuilder_item_52.description = u''
    shipBuilder_item_52.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_52.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_52.hardpoint_class = 1L
    shipBuilder_item_52.mass = 0.0
    shipBuilder_item_52.item_type = shipBuilder_itemtype_1
    shipBuilder_item_52.power = 0.0
    shipBuilder_item_52.energy = 0.0
    shipBuilder_item_52.memory = 0.0
    shipBuilder_item_52.upgrade_slots = 1L
    shipBuilder_item_52.weapon_data = None
    shipBuilder_item_52.cargo_mod_data = None
    shipBuilder_item_52.powerplant_data = None
    shipBuilder_item_52.thruster_data = None
    shipBuilder_item_52.shield_data = None
    shipBuilder_item_52.engine_intake_data = None
    shipBuilder_item_52 = importer.save_or_locate(shipBuilder_item_52)

    shipBuilder_item_53 = Item()
    shipBuilder_item_53.name = u'Executioner Twin'
    shipBuilder_item_53.rating = 1L
    shipBuilder_item_53.size = 0L
    shipBuilder_item_53.description = u''
    shipBuilder_item_53.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_53.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_53.hardpoint_class = 3L
    shipBuilder_item_53.mass = 0.0
    shipBuilder_item_53.item_type = shipBuilder_itemtype_1
    shipBuilder_item_53.power = 0.0
    shipBuilder_item_53.energy = 0.0
    shipBuilder_item_53.memory = 0.0
    shipBuilder_item_53.upgrade_slots = 1L
    shipBuilder_item_53.weapon_data = shipBuilder_weapondata_4
    shipBuilder_item_53.cargo_mod_data = None
    shipBuilder_item_53.powerplant_data = None
    shipBuilder_item_53.thruster_data = None
    shipBuilder_item_53.shield_data = None
    shipBuilder_item_53.engine_intake_data = None
    shipBuilder_item_53 = importer.save_or_locate(shipBuilder_item_53)

    shipBuilder_item_54 = Item()
    shipBuilder_item_54.name = u'M5A Twin Turret'
    shipBuilder_item_54.rating = 1L
    shipBuilder_item_54.size = 0L
    shipBuilder_item_54.description = u''
    shipBuilder_item_54.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_54.item_category = shipBuilder_itemcategory_10
    shipBuilder_item_54.hardpoint_class = 5L
    shipBuilder_item_54.mass = 0.0
    shipBuilder_item_54.item_type = shipBuilder_itemtype_1
    shipBuilder_item_54.power = 0.0
    shipBuilder_item_54.energy = 0.0
    shipBuilder_item_54.memory = 0.0
    shipBuilder_item_54.upgrade_slots = 1L
    shipBuilder_item_54.weapon_data = None
    shipBuilder_item_54.cargo_mod_data = None
    shipBuilder_item_54.powerplant_data = None
    shipBuilder_item_54.thruster_data = None
    shipBuilder_item_54.shield_data = None
    shipBuilder_item_54.engine_intake_data = None
    shipBuilder_item_54 = importer.save_or_locate(shipBuilder_item_54)

    shipBuilder_item_55 = Item()
    shipBuilder_item_55.name = u'M4A Laser'
    shipBuilder_item_55.rating = 1L
    shipBuilder_item_55.size = 0L
    shipBuilder_item_55.description = u''
    shipBuilder_item_55.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_55.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_55.hardpoint_class = 2L
    shipBuilder_item_55.mass = 0.0
    shipBuilder_item_55.item_type = shipBuilder_itemtype_1
    shipBuilder_item_55.power = 0.0
    shipBuilder_item_55.energy = 0.0
    shipBuilder_item_55.memory = 0.0
    shipBuilder_item_55.upgrade_slots = 1L
    shipBuilder_item_55.weapon_data = None
    shipBuilder_item_55.cargo_mod_data = None
    shipBuilder_item_55.powerplant_data = None
    shipBuilder_item_55.thruster_data = None
    shipBuilder_item_55.shield_data = None
    shipBuilder_item_55.engine_intake_data = None
    shipBuilder_item_55 = importer.save_or_locate(shipBuilder_item_55)

    shipBuilder_item_56 = Item()
    shipBuilder_item_56.name = u'Marksman HS 8-Pack'
    shipBuilder_item_56.rating = 1L
    shipBuilder_item_56.size = 0L
    shipBuilder_item_56.description = u''
    shipBuilder_item_56.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_56.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_56.hardpoint_class = 3L
    shipBuilder_item_56.mass = 0.0
    shipBuilder_item_56.item_type = shipBuilder_itemtype_1
    shipBuilder_item_56.power = 0.0
    shipBuilder_item_56.energy = 0.0
    shipBuilder_item_56.memory = 0.0
    shipBuilder_item_56.upgrade_slots = 1L
    shipBuilder_item_56.weapon_data = shipBuilder_weapondata_5
    shipBuilder_item_56.cargo_mod_data = None
    shipBuilder_item_56.powerplant_data = None
    shipBuilder_item_56.thruster_data = None
    shipBuilder_item_56.shield_data = None
    shipBuilder_item_56.engine_intake_data = None
    shipBuilder_item_56 = importer.save_or_locate(shipBuilder_item_56)

    shipBuilder_item_57 = Item()
    shipBuilder_item_57.name = u'CF-227 Panther Twin Turret'
    shipBuilder_item_57.rating = 1L
    shipBuilder_item_57.size = 0L
    shipBuilder_item_57.description = u''
    shipBuilder_item_57.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_57.item_category = shipBuilder_itemcategory_10
    shipBuilder_item_57.hardpoint_class = 5L
    shipBuilder_item_57.mass = 0.0
    shipBuilder_item_57.item_type = shipBuilder_itemtype_1
    shipBuilder_item_57.power = 0.0
    shipBuilder_item_57.energy = 0.0
    shipBuilder_item_57.memory = 0.0
    shipBuilder_item_57.upgrade_slots = 1L
    shipBuilder_item_57.weapon_data = None
    shipBuilder_item_57.cargo_mod_data = None
    shipBuilder_item_57.powerplant_data = None
    shipBuilder_item_57.thruster_data = None
    shipBuilder_item_57.shield_data = None
    shipBuilder_item_57.engine_intake_data = None
    shipBuilder_item_57 = importer.save_or_locate(shipBuilder_item_57)

    shipBuilder_item_58 = Item()
    shipBuilder_item_58.name = u'M3C ASA Turret'
    shipBuilder_item_58.rating = 1L
    shipBuilder_item_58.size = 0L
    shipBuilder_item_58.description = u''
    shipBuilder_item_58.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_58.item_category = shipBuilder_itemcategory_10
    shipBuilder_item_58.hardpoint_class = 5L
    shipBuilder_item_58.mass = 0.0
    shipBuilder_item_58.item_type = shipBuilder_itemtype_1
    shipBuilder_item_58.power = 0.0
    shipBuilder_item_58.energy = 0.0
    shipBuilder_item_58.memory = 0.0
    shipBuilder_item_58.upgrade_slots = 1L
    shipBuilder_item_58.weapon_data = None
    shipBuilder_item_58.cargo_mod_data = None
    shipBuilder_item_58.powerplant_data = None
    shipBuilder_item_58.thruster_data = None
    shipBuilder_item_58.shield_data = None
    shipBuilder_item_58.engine_intake_data = None
    shipBuilder_item_58 = importer.save_or_locate(shipBuilder_item_58)

    shipBuilder_item_59 = Item()
    shipBuilder_item_59.name = u'M5C STS Turret'
    shipBuilder_item_59.rating = 1L
    shipBuilder_item_59.size = 0L
    shipBuilder_item_59.description = u''
    shipBuilder_item_59.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_59.item_category = shipBuilder_itemcategory_10
    shipBuilder_item_59.hardpoint_class = 6L
    shipBuilder_item_59.mass = 0.0
    shipBuilder_item_59.item_type = shipBuilder_itemtype_1
    shipBuilder_item_59.power = 0.0
    shipBuilder_item_59.energy = 0.0
    shipBuilder_item_59.memory = 0.0
    shipBuilder_item_59.upgrade_slots = 1L
    shipBuilder_item_59.weapon_data = None
    shipBuilder_item_59.cargo_mod_data = None
    shipBuilder_item_59.powerplant_data = None
    shipBuilder_item_59.thruster_data = None
    shipBuilder_item_59.shield_data = None
    shipBuilder_item_59.engine_intake_data = None
    shipBuilder_item_59 = importer.save_or_locate(shipBuilder_item_59)

    shipBuilder_item_60 = Item()
    shipBuilder_item_60.name = u'Plowshare Anti-Ship Missile'
    shipBuilder_item_60.rating = 1L
    shipBuilder_item_60.size = 0L
    shipBuilder_item_60.description = u''
    shipBuilder_item_60.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_item_60.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_60.hardpoint_class = 6L
    shipBuilder_item_60.mass = 0.0
    shipBuilder_item_60.item_type = shipBuilder_itemtype_1
    shipBuilder_item_60.power = 0.0
    shipBuilder_item_60.energy = 0.0
    shipBuilder_item_60.memory = 0.0
    shipBuilder_item_60.upgrade_slots = 1L
    shipBuilder_item_60.weapon_data = None
    shipBuilder_item_60.cargo_mod_data = None
    shipBuilder_item_60.powerplant_data = None
    shipBuilder_item_60.thruster_data = None
    shipBuilder_item_60.shield_data = None
    shipBuilder_item_60.engine_intake_data = None
    shipBuilder_item_60 = importer.save_or_locate(shipBuilder_item_60)

    shipBuilder_item_61 = Item()
    shipBuilder_item_61.name = u'Zestroyer Rail Gun'
    shipBuilder_item_61.rating = 1L
    shipBuilder_item_61.size = 0L
    shipBuilder_item_61.description = u''
    shipBuilder_item_61.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_61.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_61.hardpoint_class = 7L
    shipBuilder_item_61.mass = 0.0
    shipBuilder_item_61.item_type = shipBuilder_itemtype_1
    shipBuilder_item_61.power = 0.0
    shipBuilder_item_61.energy = 0.0
    shipBuilder_item_61.memory = 0.0
    shipBuilder_item_61.upgrade_slots = 1L
    shipBuilder_item_61.weapon_data = None
    shipBuilder_item_61.cargo_mod_data = None
    shipBuilder_item_61.powerplant_data = None
    shipBuilder_item_61.thruster_data = None
    shipBuilder_item_61.shield_data = None
    shipBuilder_item_61.engine_intake_data = None
    shipBuilder_item_61 = importer.save_or_locate(shipBuilder_item_61)

    shipBuilder_item_62 = Item()
    shipBuilder_item_62.name = u'9-Series Longsword'
    shipBuilder_item_62.rating = 1L
    shipBuilder_item_62.size = 0L
    shipBuilder_item_62.description = u''
    shipBuilder_item_62.manufacturer = shipBuilder_manufacturer_32
    shipBuilder_item_62.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_62.hardpoint_class = 1L
    shipBuilder_item_62.mass = 0.0
    shipBuilder_item_62.item_type = shipBuilder_itemtype_1
    shipBuilder_item_62.power = 0.0
    shipBuilder_item_62.energy = 0.0
    shipBuilder_item_62.memory = 0.0
    shipBuilder_item_62.upgrade_slots = 1L
    shipBuilder_item_62.weapon_data = None
    shipBuilder_item_62.cargo_mod_data = None
    shipBuilder_item_62.powerplant_data = None
    shipBuilder_item_62.thruster_data = None
    shipBuilder_item_62.shield_data = None
    shipBuilder_item_62.engine_intake_data = None
    shipBuilder_item_62 = importer.save_or_locate(shipBuilder_item_62)

    shipBuilder_item_63 = Item()
    shipBuilder_item_63.name = u'11-Series Broadsword'
    shipBuilder_item_63.rating = 1L
    shipBuilder_item_63.size = 0L
    shipBuilder_item_63.description = u''
    shipBuilder_item_63.manufacturer = shipBuilder_manufacturer_32
    shipBuilder_item_63.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_63.hardpoint_class = 1L
    shipBuilder_item_63.mass = 0.0
    shipBuilder_item_63.item_type = shipBuilder_itemtype_1
    shipBuilder_item_63.power = 0.0
    shipBuilder_item_63.energy = 0.0
    shipBuilder_item_63.memory = 0.0
    shipBuilder_item_63.upgrade_slots = 1L
    shipBuilder_item_63.weapon_data = None
    shipBuilder_item_63.cargo_mod_data = None
    shipBuilder_item_63.powerplant_data = None
    shipBuilder_item_63.thruster_data = None
    shipBuilder_item_63.shield_data = None
    shipBuilder_item_63.engine_intake_data = None
    shipBuilder_item_63 = importer.save_or_locate(shipBuilder_item_63)

    #Re-processing model: CargoModData




    #Re-processing model: Hardpoint

    #Re-processing model: BuildHardpoint

    #Re-processing model: BuildEngineMod

    #Re-processing model: BuildHullMod

    #Re-processing model: Build

    #Re-processing model: Item
































































