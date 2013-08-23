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
    shipBuilder_manufacturer_1.name = u'Origin Jumpworks, GmbH.'
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

    #Processing model: ItemType

    from shipBuilder.models import ItemType

    shipBuilder_itemtype_1 = ItemType()
    shipBuilder_itemtype_1.description = u'Weapon'
    shipBuilder_itemtype_1 = importer.save_or_locate(shipBuilder_itemtype_1)

    #Processing model: ItemCategory

    from shipBuilder.models import ItemCategory

    shipBuilder_itemcategory_1 = ItemCategory()
    shipBuilder_itemcategory_1.description = u'Gun'
    shipBuilder_itemcategory_1 = importer.save_or_locate(shipBuilder_itemcategory_1)

    shipBuilder_itemcategory_2 = ItemCategory()
    shipBuilder_itemcategory_2.description = u'Missile Launcher'
    shipBuilder_itemcategory_2 = importer.save_or_locate(shipBuilder_itemcategory_2)

    #Processing model: ThrusterType

    from shipBuilder.models import ThrusterType

    shipBuilder_thrustertype_1 = ThrusterType()
    shipBuilder_thrustertype_1.name = u'Twin'
    shipBuilder_thrustertype_1 = importer.save_or_locate(shipBuilder_thrustertype_1)

    shipBuilder_thrustertype_2 = ThrusterType()
    shipBuilder_thrustertype_2.name = u'Standard'
    shipBuilder_thrustertype_2 = importer.save_or_locate(shipBuilder_thrustertype_2)

    #Processing model: PowerplantType

    from shipBuilder.models import PowerplantType

    shipBuilder_powerplanttype_1 = PowerplantType()
    shipBuilder_powerplanttype_1.name = u'Fusion'
    shipBuilder_powerplanttype_1 = importer.save_or_locate(shipBuilder_powerplanttype_1)

    #Processing model: Ship

    from shipBuilder.models import Ship

    shipBuilder_ship_1 = Ship()
    shipBuilder_ship_1.name = u'300i'
    shipBuilder_ship_1.description = u''
    shipBuilder_ship_1.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_ship_1.maximum_crew = 1L
    shipBuilder_ship_1.empty_mass = 0L
    shipBuilder_ship_1.length = 0.0
    shipBuilder_ship_1.width = 0.0
    shipBuilder_ship_1.height = 0.0
    shipBuilder_ship_1.upgrade_capacity = 1L
    shipBuilder_ship_1.memory_capactiy = 0L
    shipBuilder_ship_1.main_thruster_count = 1L
    shipBuilder_ship_1.main_thruster_max_rating = 1L
    shipBuilder_ship_1.main_thruster_type = shipBuilder_thrustertype_2
    shipBuilder_ship_1.control_thruster_count = 8L
    shipBuilder_ship_1.control_thruster_max_rating = 1L
    shipBuilder_ship_1.control_thruster_type = shipBuilder_thrustertype_2
    shipBuilder_ship_1.powerplant_type_max = shipBuilder_powerplanttype_1
    shipBuilder_ship_1 = importer.save_or_locate(shipBuilder_ship_1)

    shipBuilder_ship_2 = Ship()
    shipBuilder_ship_2.name = u'Aurora'
    shipBuilder_ship_2.description = u''
    shipBuilder_ship_2.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_ship_2.maximum_crew = 1L
    shipBuilder_ship_2.empty_mass = 0L
    shipBuilder_ship_2.length = 0.0
    shipBuilder_ship_2.width = 0.0
    shipBuilder_ship_2.height = 0.0
    shipBuilder_ship_2.upgrade_capacity = 1L
    shipBuilder_ship_2.memory_capactiy = 0L
    shipBuilder_ship_2.main_thruster_count = 1L
    shipBuilder_ship_2.main_thruster_max_rating = 3L
    shipBuilder_ship_2.main_thruster_type = shipBuilder_thrustertype_2
    shipBuilder_ship_2.control_thruster_count = 8L
    shipBuilder_ship_2.control_thruster_max_rating = 1L
    shipBuilder_ship_2.control_thruster_type = shipBuilder_thrustertype_2
    shipBuilder_ship_2.powerplant_type_max = shipBuilder_powerplanttype_1
    shipBuilder_ship_2 = importer.save_or_locate(shipBuilder_ship_2)

    shipBuilder_ship_3 = Ship()
    shipBuilder_ship_3.name = u'Constellation'
    shipBuilder_ship_3.description = u''
    shipBuilder_ship_3.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_ship_3.maximum_crew = 3L
    shipBuilder_ship_3.empty_mass = 0L
    shipBuilder_ship_3.length = 0.0
    shipBuilder_ship_3.width = 0.0
    shipBuilder_ship_3.height = 0.0
    shipBuilder_ship_3.upgrade_capacity = 1L
    shipBuilder_ship_3.memory_capactiy = 0L
    shipBuilder_ship_3.main_thruster_count = 4L
    shipBuilder_ship_3.main_thruster_max_rating = 1L
    shipBuilder_ship_3.main_thruster_type = shipBuilder_thrustertype_2
    shipBuilder_ship_3.control_thruster_count = 8L
    shipBuilder_ship_3.control_thruster_max_rating = 1L
    shipBuilder_ship_3.control_thruster_type = shipBuilder_thrustertype_2
    shipBuilder_ship_3.powerplant_type_max = shipBuilder_powerplanttype_1
    shipBuilder_ship_3 = importer.save_or_locate(shipBuilder_ship_3)

    #Processing model: Image

    from shipBuilder.models import Image

    shipBuilder_image_1 = Image()
    shipBuilder_image_1.url = u'http://www.stantonspacebarn.com/static/images/Origin_300i_glamour_shot.png'
    shipBuilder_image_1.name = u'300i Top Isometric'
    shipBuilder_image_1.ship = shipBuilder_ship_1
    shipBuilder_image_1 = importer.save_or_locate(shipBuilder_image_1)

    shipBuilder_image_2 = Image()
    shipBuilder_image_2.url = u'http://www.stantonspacebarn.com/static/images/Origin_300i_ventral.png'
    shipBuilder_image_2.name = u'300i Ventral Isometric'
    shipBuilder_image_2.ship = shipBuilder_ship_1
    shipBuilder_image_2 = importer.save_or_locate(shipBuilder_image_2)

    shipBuilder_image_3 = Image()
    shipBuilder_image_3.url = u'http://www.stantonspacebarn.com/static/images/aurora_side.png'
    shipBuilder_image_3.name = u'Aurora Side View'
    shipBuilder_image_3.ship = shipBuilder_ship_2
    shipBuilder_image_3 = importer.save_or_locate(shipBuilder_image_3)

    shipBuilder_image_4 = Image()
    shipBuilder_image_4.url = u'http://www.stantonspacebarn.com/static/images/aurora_top_back.png'
    shipBuilder_image_4.name = u'Aurora Top Back'
    shipBuilder_image_4.ship = shipBuilder_ship_2
    shipBuilder_image_4 = importer.save_or_locate(shipBuilder_image_4)

    shipBuilder_image_5 = Image()
    shipBuilder_image_5.url = u'http://www.stantonspacebarn.com/static/images/rsi_constellation_top_iso.jpg'
    shipBuilder_image_5.name = u'Constellation Top'
    shipBuilder_image_5.ship = shipBuilder_ship_3
    shipBuilder_image_5 = importer.save_or_locate(shipBuilder_image_5)

    #Processing model: Icon

    from shipBuilder.models import Icon

    shipBuilder_icon_1 = Icon()
    shipBuilder_icon_1.url = u'http://www.stantonspacebarn.com/static/images/talon_twin_ir_stalker.png'
    shipBuilder_icon_1.name = u'Stalker IR Twin'
    shipBuilder_icon_1 = importer.save_or_locate(shipBuilder_icon_1)

    shipBuilder_icon_2 = Icon()
    shipBuilder_icon_2.url = u'http://www.stantonspacebarn.com/static/images/kw_mass_driver_cannon.png'
    shipBuilder_icon_2.name = u'K&W Mass Driver Cannon'
    shipBuilder_icon_2 = importer.save_or_locate(shipBuilder_icon_2)

    shipBuilder_icon_3 = Icon()
    shipBuilder_icon_3.url = u'http://www.stantonspacebarn.com/static/images/300series_brochure_17-3.png'
    shipBuilder_icon_3.name = u'Omnisky III'
    shipBuilder_icon_3 = importer.save_or_locate(shipBuilder_icon_3)

    shipBuilder_icon_4 = Icon()
    shipBuilder_icon_4.url = u'http://www.stantonspacebarn.com/static/images/1000px-300series_brochure_14-2.png'
    shipBuilder_icon_4.name = u'Omnisky IV'
    shipBuilder_icon_4 = importer.save_or_locate(shipBuilder_icon_4)

    shipBuilder_icon_5 = Icon()
    shipBuilder_icon_5.url = u'http://www.stantonspacebarn.com/static/images/no-image-icon.jpg'
    shipBuilder_icon_5.name = u'No Image Icon'
    shipBuilder_icon_5 = importer.save_or_locate(shipBuilder_icon_5)

    #Processing model: Build

    from shipBuilder.models import Build


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
    shipBuilder_hardpoint_9.overlay_location_x = -325L
    shipBuilder_hardpoint_9.overlay_location_y = 150L
    shipBuilder_hardpoint_9.tag_location_x = 260L
    shipBuilder_hardpoint_9.tag_location_y = 90L
    shipBuilder_hardpoint_9.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_9.image = shipBuilder_image_5
    shipBuilder_hardpoint_9 = importer.save_or_locate(shipBuilder_hardpoint_9)

    shipBuilder_hardpoint_10 = Hardpoint()
    shipBuilder_hardpoint_10.name = u'Port Dorsal'
    shipBuilder_hardpoint_10.hardpoint_class = 3L
    shipBuilder_hardpoint_10.overlay_location_x = -325L
    shipBuilder_hardpoint_10.overlay_location_y = 200L
    shipBuilder_hardpoint_10.tag_location_x = 190L
    shipBuilder_hardpoint_10.tag_location_y = 120L
    shipBuilder_hardpoint_10.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_10.image = shipBuilder_image_5
    shipBuilder_hardpoint_10 = importer.save_or_locate(shipBuilder_hardpoint_10)

    shipBuilder_hardpoint_11 = Hardpoint()
    shipBuilder_hardpoint_11.name = u'Engine One'
    shipBuilder_hardpoint_11.hardpoint_class = 2L
    shipBuilder_hardpoint_11.overlay_location_x = 520L
    shipBuilder_hardpoint_11.overlay_location_y = 0L
    shipBuilder_hardpoint_11.tag_location_x = 445L
    shipBuilder_hardpoint_11.tag_location_y = 95L
    shipBuilder_hardpoint_11.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_11.image = shipBuilder_image_5
    shipBuilder_hardpoint_11 = importer.save_or_locate(shipBuilder_hardpoint_11)

    shipBuilder_hardpoint_12 = Hardpoint()
    shipBuilder_hardpoint_12.name = u'Engine Two'
    shipBuilder_hardpoint_12.hardpoint_class = 2L
    shipBuilder_hardpoint_12.overlay_location_x = 615L
    shipBuilder_hardpoint_12.overlay_location_y = 270L
    shipBuilder_hardpoint_12.tag_location_x = 360L
    shipBuilder_hardpoint_12.tag_location_y = 135L
    shipBuilder_hardpoint_12.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_12.image = shipBuilder_image_5
    shipBuilder_hardpoint_12 = importer.save_or_locate(shipBuilder_hardpoint_12)

    shipBuilder_hardpoint_13 = Hardpoint()
    shipBuilder_hardpoint_13.name = u'Engine Three'
    shipBuilder_hardpoint_13.hardpoint_class = 2L
    shipBuilder_hardpoint_13.overlay_location_x = 513L
    shipBuilder_hardpoint_13.overlay_location_y = 387L
    shipBuilder_hardpoint_13.tag_location_x = 265L
    shipBuilder_hardpoint_13.tag_location_y = 180L
    shipBuilder_hardpoint_13.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_13.image = shipBuilder_image_5
    shipBuilder_hardpoint_13 = importer.save_or_locate(shipBuilder_hardpoint_13)

    shipBuilder_hardpoint_14 = Hardpoint()
    shipBuilder_hardpoint_14.name = u'Engine Four'
    shipBuilder_hardpoint_14.hardpoint_class = 2L
    shipBuilder_hardpoint_14.overlay_location_x = 200L
    shipBuilder_hardpoint_14.overlay_location_y = 450L
    shipBuilder_hardpoint_14.tag_location_x = 135L
    shipBuilder_hardpoint_14.tag_location_y = 235L
    shipBuilder_hardpoint_14.ship = shipBuilder_ship_3
    shipBuilder_hardpoint_14.image = shipBuilder_image_5
    shipBuilder_hardpoint_14 = importer.save_or_locate(shipBuilder_hardpoint_14)

    #Processing model: Item

    from shipBuilder.models import Item

    shipBuilder_item_1 = Item()
    shipBuilder_item_1.name = u'Fixed M3A Laser Cannon'
    shipBuilder_item_1.description = u''
    shipBuilder_item_1.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_item_1.item_type = shipBuilder_itemtype_1
    shipBuilder_item_1.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_1.build = None
    shipBuilder_item_1.hardpoint = None
    shipBuilder_item_1.icon = shipBuilder_icon_5
    shipBuilder_item_1.rate_of_fire = 0.0
    shipBuilder_item_1.hardpoint_class = 1L
    shipBuilder_item_1 = importer.save_or_locate(shipBuilder_item_1)

    shipBuilder_item_2 = Item()
    shipBuilder_item_2.name = u'Bulldog Repeater'
    shipBuilder_item_2.description = u''
    shipBuilder_item_2.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_2.item_type = shipBuilder_itemtype_1
    shipBuilder_item_2.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_2.build = None
    shipBuilder_item_2.hardpoint = None
    shipBuilder_item_2.icon = shipBuilder_icon_5
    shipBuilder_item_2.rate_of_fire = 0.0
    shipBuilder_item_2.hardpoint_class = 1L
    shipBuilder_item_2 = importer.save_or_locate(shipBuilder_item_2)

    shipBuilder_item_3 = Item()
    shipBuilder_item_3.name = u'IR4 Stalker'
    shipBuilder_item_3.description = u''
    shipBuilder_item_3.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_item_3.item_type = shipBuilder_itemtype_1
    shipBuilder_item_3.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_3.build = None
    shipBuilder_item_3.hardpoint = None
    shipBuilder_item_3.icon = shipBuilder_icon_5
    shipBuilder_item_3.rate_of_fire = 0.0
    shipBuilder_item_3.hardpoint_class = 3L
    shipBuilder_item_3 = importer.save_or_locate(shipBuilder_item_3)

    shipBuilder_item_4 = Item()
    shipBuilder_item_4.name = u'Omnisky IV'
    shipBuilder_item_4.description = u''
    shipBuilder_item_4.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_item_4.item_type = shipBuilder_itemtype_1
    shipBuilder_item_4.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_4.build = None
    shipBuilder_item_4.hardpoint = None
    shipBuilder_item_4.icon = shipBuilder_icon_4
    shipBuilder_item_4.rate_of_fire = 0.0
    shipBuilder_item_4.hardpoint_class = 1L
    shipBuilder_item_4 = importer.save_or_locate(shipBuilder_item_4)

    shipBuilder_item_5 = Item()
    shipBuilder_item_5.name = u'Omnisky III'
    shipBuilder_item_5.description = u''
    shipBuilder_item_5.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_item_5.item_type = shipBuilder_itemtype_1
    shipBuilder_item_5.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_5.build = None
    shipBuilder_item_5.hardpoint = None
    shipBuilder_item_5.icon = shipBuilder_icon_3
    shipBuilder_item_5.rate_of_fire = 0.0
    shipBuilder_item_5.hardpoint_class = 1L
    shipBuilder_item_5 = importer.save_or_locate(shipBuilder_item_5)

    shipBuilder_item_6 = Item()
    shipBuilder_item_6.name = u'Mass Driver Cannon'
    shipBuilder_item_6.description = u''
    shipBuilder_item_6.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_item_6.item_type = shipBuilder_itemtype_1
    shipBuilder_item_6.item_category = shipBuilder_itemcategory_1
    shipBuilder_item_6.build = None
    shipBuilder_item_6.hardpoint = None
    shipBuilder_item_6.icon = shipBuilder_icon_2
    shipBuilder_item_6.rate_of_fire = 0.0
    shipBuilder_item_6.hardpoint_class = 2L
    shipBuilder_item_6 = importer.save_or_locate(shipBuilder_item_6)

    shipBuilder_item_7 = Item()
    shipBuilder_item_7.name = u'Stalker IR Twin'
    shipBuilder_item_7.description = u''
    shipBuilder_item_7.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_item_7.item_type = shipBuilder_itemtype_1
    shipBuilder_item_7.item_category = shipBuilder_itemcategory_2
    shipBuilder_item_7.build = None
    shipBuilder_item_7.hardpoint = None
    shipBuilder_item_7.icon = shipBuilder_icon_1
    shipBuilder_item_7.rate_of_fire = 0.0
    shipBuilder_item_7.hardpoint_class = 3L
    shipBuilder_item_7 = importer.save_or_locate(shipBuilder_item_7)

