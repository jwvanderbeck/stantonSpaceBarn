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
# manage.py dumpscript
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

    #Processing model: Permission

    from django.contrib.auth.models import Permission

    auth_permission_1 = Permission()
    auth_permission_1.name = u'Can add log entry'
    auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_1.codename = u'add_logentry'
    auth_permission_1 = importer.save_or_locate(auth_permission_1)

    auth_permission_2 = Permission()
    auth_permission_2.name = u'Can change log entry'
    auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_2.codename = u'change_logentry'
    auth_permission_2 = importer.save_or_locate(auth_permission_2)

    auth_permission_3 = Permission()
    auth_permission_3.name = u'Can delete log entry'
    auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    auth_permission_3.codename = u'delete_logentry'
    auth_permission_3 = importer.save_or_locate(auth_permission_3)

    auth_permission_4 = Permission()
    auth_permission_4.name = u'Can add group'
    auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_4.codename = u'add_group'
    auth_permission_4 = importer.save_or_locate(auth_permission_4)

    auth_permission_5 = Permission()
    auth_permission_5.name = u'Can change group'
    auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_5.codename = u'change_group'
    auth_permission_5 = importer.save_or_locate(auth_permission_5)

    auth_permission_6 = Permission()
    auth_permission_6.name = u'Can delete group'
    auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    auth_permission_6.codename = u'delete_group'
    auth_permission_6 = importer.save_or_locate(auth_permission_6)

    auth_permission_7 = Permission()
    auth_permission_7.name = u'Can add permission'
    auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_7.codename = u'add_permission'
    auth_permission_7 = importer.save_or_locate(auth_permission_7)

    auth_permission_8 = Permission()
    auth_permission_8.name = u'Can change permission'
    auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_8.codename = u'change_permission'
    auth_permission_8 = importer.save_or_locate(auth_permission_8)

    auth_permission_9 = Permission()
    auth_permission_9.name = u'Can delete permission'
    auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="permission")
    auth_permission_9.codename = u'delete_permission'
    auth_permission_9 = importer.save_or_locate(auth_permission_9)

    auth_permission_10 = Permission()
    auth_permission_10.name = u'Can add user'
    auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_10.codename = u'add_user'
    auth_permission_10 = importer.save_or_locate(auth_permission_10)

    auth_permission_11 = Permission()
    auth_permission_11.name = u'Can change user'
    auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_11.codename = u'change_user'
    auth_permission_11 = importer.save_or_locate(auth_permission_11)

    auth_permission_12 = Permission()
    auth_permission_12.name = u'Can delete user'
    auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    auth_permission_12.codename = u'delete_user'
    auth_permission_12 = importer.save_or_locate(auth_permission_12)

    auth_permission_13 = Permission()
    auth_permission_13.name = u'Can add content type'
    auth_permission_13.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_13.codename = u'add_contenttype'
    auth_permission_13 = importer.save_or_locate(auth_permission_13)

    auth_permission_14 = Permission()
    auth_permission_14.name = u'Can change content type'
    auth_permission_14.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_14.codename = u'change_contenttype'
    auth_permission_14 = importer.save_or_locate(auth_permission_14)

    auth_permission_15 = Permission()
    auth_permission_15.name = u'Can delete content type'
    auth_permission_15.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    auth_permission_15.codename = u'delete_contenttype'
    auth_permission_15 = importer.save_or_locate(auth_permission_15)

    auth_permission_16 = Permission()
    auth_permission_16.name = u'Can add session'
    auth_permission_16.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_16.codename = u'add_session'
    auth_permission_16 = importer.save_or_locate(auth_permission_16)

    auth_permission_17 = Permission()
    auth_permission_17.name = u'Can change session'
    auth_permission_17.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_17.codename = u'change_session'
    auth_permission_17 = importer.save_or_locate(auth_permission_17)

    auth_permission_18 = Permission()
    auth_permission_18.name = u'Can delete session'
    auth_permission_18.content_type = ContentType.objects.get(app_label="sessions", model="session")
    auth_permission_18.codename = u'delete_session'
    auth_permission_18 = importer.save_or_locate(auth_permission_18)

    auth_permission_19 = Permission()
    auth_permission_19.name = u'Can add build'
    auth_permission_19.content_type = ContentType.objects.get(app_label="shipBuilder", model="build")
    auth_permission_19.codename = u'add_build'
    auth_permission_19 = importer.save_or_locate(auth_permission_19)

    auth_permission_20 = Permission()
    auth_permission_20.name = u'Can change build'
    auth_permission_20.content_type = ContentType.objects.get(app_label="shipBuilder", model="build")
    auth_permission_20.codename = u'change_build'
    auth_permission_20 = importer.save_or_locate(auth_permission_20)

    auth_permission_21 = Permission()
    auth_permission_21.name = u'Can delete build'
    auth_permission_21.content_type = ContentType.objects.get(app_label="shipBuilder", model="build")
    auth_permission_21.codename = u'delete_build'
    auth_permission_21 = importer.save_or_locate(auth_permission_21)

    auth_permission_22 = Permission()
    auth_permission_22.name = u'Can add build engine mod'
    auth_permission_22.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildenginemod")
    auth_permission_22.codename = u'add_buildenginemod'
    auth_permission_22 = importer.save_or_locate(auth_permission_22)

    auth_permission_23 = Permission()
    auth_permission_23.name = u'Can change build engine mod'
    auth_permission_23.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildenginemod")
    auth_permission_23.codename = u'change_buildenginemod'
    auth_permission_23 = importer.save_or_locate(auth_permission_23)

    auth_permission_24 = Permission()
    auth_permission_24.name = u'Can delete build engine mod'
    auth_permission_24.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildenginemod")
    auth_permission_24.codename = u'delete_buildenginemod'
    auth_permission_24 = importer.save_or_locate(auth_permission_24)

    auth_permission_25 = Permission()
    auth_permission_25.name = u'Can add build hardpoint'
    auth_permission_25.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildhardpoint")
    auth_permission_25.codename = u'add_buildhardpoint'
    auth_permission_25 = importer.save_or_locate(auth_permission_25)

    auth_permission_26 = Permission()
    auth_permission_26.name = u'Can change build hardpoint'
    auth_permission_26.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildhardpoint")
    auth_permission_26.codename = u'change_buildhardpoint'
    auth_permission_26 = importer.save_or_locate(auth_permission_26)

    auth_permission_27 = Permission()
    auth_permission_27.name = u'Can delete build hardpoint'
    auth_permission_27.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildhardpoint")
    auth_permission_27.codename = u'delete_buildhardpoint'
    auth_permission_27 = importer.save_or_locate(auth_permission_27)

    auth_permission_28 = Permission()
    auth_permission_28.name = u'Can add build hull mod'
    auth_permission_28.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildhullmod")
    auth_permission_28.codename = u'add_buildhullmod'
    auth_permission_28 = importer.save_or_locate(auth_permission_28)

    auth_permission_29 = Permission()
    auth_permission_29.name = u'Can change build hull mod'
    auth_permission_29.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildhullmod")
    auth_permission_29.codename = u'change_buildhullmod'
    auth_permission_29 = importer.save_or_locate(auth_permission_29)

    auth_permission_30 = Permission()
    auth_permission_30.name = u'Can delete build hull mod'
    auth_permission_30.content_type = ContentType.objects.get(app_label="shipBuilder", model="buildhullmod")
    auth_permission_30.codename = u'delete_buildhullmod'
    auth_permission_30 = importer.save_or_locate(auth_permission_30)

    auth_permission_31 = Permission()
    auth_permission_31.name = u'Can add cargo mod data'
    auth_permission_31.content_type = ContentType.objects.get(app_label="shipBuilder", model="cargomoddata")
    auth_permission_31.codename = u'add_cargomoddata'
    auth_permission_31 = importer.save_or_locate(auth_permission_31)

    auth_permission_32 = Permission()
    auth_permission_32.name = u'Can change cargo mod data'
    auth_permission_32.content_type = ContentType.objects.get(app_label="shipBuilder", model="cargomoddata")
    auth_permission_32.codename = u'change_cargomoddata'
    auth_permission_32 = importer.save_or_locate(auth_permission_32)

    auth_permission_33 = Permission()
    auth_permission_33.name = u'Can delete cargo mod data'
    auth_permission_33.content_type = ContentType.objects.get(app_label="shipBuilder", model="cargomoddata")
    auth_permission_33.codename = u'delete_cargomoddata'
    auth_permission_33 = importer.save_or_locate(auth_permission_33)

    auth_permission_34 = Permission()
    auth_permission_34.name = u'Can add engine intake data'
    auth_permission_34.content_type = ContentType.objects.get(app_label="shipBuilder", model="engineintakedata")
    auth_permission_34.codename = u'add_engineintakedata'
    auth_permission_34 = importer.save_or_locate(auth_permission_34)

    auth_permission_35 = Permission()
    auth_permission_35.name = u'Can change engine intake data'
    auth_permission_35.content_type = ContentType.objects.get(app_label="shipBuilder", model="engineintakedata")
    auth_permission_35.codename = u'change_engineintakedata'
    auth_permission_35 = importer.save_or_locate(auth_permission_35)

    auth_permission_36 = Permission()
    auth_permission_36.name = u'Can delete engine intake data'
    auth_permission_36.content_type = ContentType.objects.get(app_label="shipBuilder", model="engineintakedata")
    auth_permission_36.codename = u'delete_engineintakedata'
    auth_permission_36 = importer.save_or_locate(auth_permission_36)

    auth_permission_37 = Permission()
    auth_permission_37.name = u'Can add hardpoint'
    auth_permission_37.content_type = ContentType.objects.get(app_label="shipBuilder", model="hardpoint")
    auth_permission_37.codename = u'add_hardpoint'
    auth_permission_37 = importer.save_or_locate(auth_permission_37)

    auth_permission_38 = Permission()
    auth_permission_38.name = u'Can change hardpoint'
    auth_permission_38.content_type = ContentType.objects.get(app_label="shipBuilder", model="hardpoint")
    auth_permission_38.codename = u'change_hardpoint'
    auth_permission_38 = importer.save_or_locate(auth_permission_38)

    auth_permission_39 = Permission()
    auth_permission_39.name = u'Can delete hardpoint'
    auth_permission_39.content_type = ContentType.objects.get(app_label="shipBuilder", model="hardpoint")
    auth_permission_39.codename = u'delete_hardpoint'
    auth_permission_39 = importer.save_or_locate(auth_permission_39)

    auth_permission_40 = Permission()
    auth_permission_40.name = u'Can add image'
    auth_permission_40.content_type = ContentType.objects.get(app_label="shipBuilder", model="image")
    auth_permission_40.codename = u'add_image'
    auth_permission_40 = importer.save_or_locate(auth_permission_40)

    auth_permission_41 = Permission()
    auth_permission_41.name = u'Can change image'
    auth_permission_41.content_type = ContentType.objects.get(app_label="shipBuilder", model="image")
    auth_permission_41.codename = u'change_image'
    auth_permission_41 = importer.save_or_locate(auth_permission_41)

    auth_permission_42 = Permission()
    auth_permission_42.name = u'Can delete image'
    auth_permission_42.content_type = ContentType.objects.get(app_label="shipBuilder", model="image")
    auth_permission_42.codename = u'delete_image'
    auth_permission_42 = importer.save_or_locate(auth_permission_42)

    auth_permission_43 = Permission()
    auth_permission_43.name = u'Can add item'
    auth_permission_43.content_type = ContentType.objects.get(app_label="shipBuilder", model="item")
    auth_permission_43.codename = u'add_item'
    auth_permission_43 = importer.save_or_locate(auth_permission_43)

    auth_permission_44 = Permission()
    auth_permission_44.name = u'Can change item'
    auth_permission_44.content_type = ContentType.objects.get(app_label="shipBuilder", model="item")
    auth_permission_44.codename = u'change_item'
    auth_permission_44 = importer.save_or_locate(auth_permission_44)

    auth_permission_45 = Permission()
    auth_permission_45.name = u'Can delete item'
    auth_permission_45.content_type = ContentType.objects.get(app_label="shipBuilder", model="item")
    auth_permission_45.codename = u'delete_item'
    auth_permission_45 = importer.save_or_locate(auth_permission_45)

    auth_permission_46 = Permission()
    auth_permission_46.name = u'Can add item category'
    auth_permission_46.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemcategory")
    auth_permission_46.codename = u'add_itemcategory'
    auth_permission_46 = importer.save_or_locate(auth_permission_46)

    auth_permission_47 = Permission()
    auth_permission_47.name = u'Can change item category'
    auth_permission_47.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemcategory")
    auth_permission_47.codename = u'change_itemcategory'
    auth_permission_47 = importer.save_or_locate(auth_permission_47)

    auth_permission_48 = Permission()
    auth_permission_48.name = u'Can delete item category'
    auth_permission_48.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemcategory")
    auth_permission_48.codename = u'delete_itemcategory'
    auth_permission_48 = importer.save_or_locate(auth_permission_48)

    auth_permission_49 = Permission()
    auth_permission_49.name = u'Can add item port'
    auth_permission_49.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    auth_permission_49.codename = u'add_itemport'
    auth_permission_49 = importer.save_or_locate(auth_permission_49)

    auth_permission_50 = Permission()
    auth_permission_50.name = u'Can change item port'
    auth_permission_50.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    auth_permission_50.codename = u'change_itemport'
    auth_permission_50 = importer.save_or_locate(auth_permission_50)

    auth_permission_51 = Permission()
    auth_permission_51.name = u'Can delete item port'
    auth_permission_51.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    auth_permission_51.codename = u'delete_itemport'
    auth_permission_51 = importer.save_or_locate(auth_permission_51)

    auth_permission_52 = Permission()
    auth_permission_52.name = u'Can add item type'
    auth_permission_52.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemtype")
    auth_permission_52.codename = u'add_itemtype'
    auth_permission_52 = importer.save_or_locate(auth_permission_52)

    auth_permission_53 = Permission()
    auth_permission_53.name = u'Can change item type'
    auth_permission_53.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemtype")
    auth_permission_53.codename = u'change_itemtype'
    auth_permission_53 = importer.save_or_locate(auth_permission_53)

    auth_permission_54 = Permission()
    auth_permission_54.name = u'Can delete item type'
    auth_permission_54.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemtype")
    auth_permission_54.codename = u'delete_itemtype'
    auth_permission_54 = importer.save_or_locate(auth_permission_54)

    auth_permission_55 = Permission()
    auth_permission_55.name = u'Can add manufacturer'
    auth_permission_55.content_type = ContentType.objects.get(app_label="shipBuilder", model="manufacturer")
    auth_permission_55.codename = u'add_manufacturer'
    auth_permission_55 = importer.save_or_locate(auth_permission_55)

    auth_permission_56 = Permission()
    auth_permission_56.name = u'Can change manufacturer'
    auth_permission_56.content_type = ContentType.objects.get(app_label="shipBuilder", model="manufacturer")
    auth_permission_56.codename = u'change_manufacturer'
    auth_permission_56 = importer.save_or_locate(auth_permission_56)

    auth_permission_57 = Permission()
    auth_permission_57.name = u'Can delete manufacturer'
    auth_permission_57.content_type = ContentType.objects.get(app_label="shipBuilder", model="manufacturer")
    auth_permission_57.codename = u'delete_manufacturer'
    auth_permission_57 = importer.save_or_locate(auth_permission_57)

    auth_permission_58 = Permission()
    auth_permission_58.name = u'Can add powerplant data'
    auth_permission_58.content_type = ContentType.objects.get(app_label="shipBuilder", model="powerplantdata")
    auth_permission_58.codename = u'add_powerplantdata'
    auth_permission_58 = importer.save_or_locate(auth_permission_58)

    auth_permission_59 = Permission()
    auth_permission_59.name = u'Can change powerplant data'
    auth_permission_59.content_type = ContentType.objects.get(app_label="shipBuilder", model="powerplantdata")
    auth_permission_59.codename = u'change_powerplantdata'
    auth_permission_59 = importer.save_or_locate(auth_permission_59)

    auth_permission_60 = Permission()
    auth_permission_60.name = u'Can delete powerplant data'
    auth_permission_60.content_type = ContentType.objects.get(app_label="shipBuilder", model="powerplantdata")
    auth_permission_60.codename = u'delete_powerplantdata'
    auth_permission_60 = importer.save_or_locate(auth_permission_60)

    auth_permission_61 = Permission()
    auth_permission_61.name = u'Can add shield data'
    auth_permission_61.content_type = ContentType.objects.get(app_label="shipBuilder", model="shielddata")
    auth_permission_61.codename = u'add_shielddata'
    auth_permission_61 = importer.save_or_locate(auth_permission_61)

    auth_permission_62 = Permission()
    auth_permission_62.name = u'Can change shield data'
    auth_permission_62.content_type = ContentType.objects.get(app_label="shipBuilder", model="shielddata")
    auth_permission_62.codename = u'change_shielddata'
    auth_permission_62 = importer.save_or_locate(auth_permission_62)

    auth_permission_63 = Permission()
    auth_permission_63.name = u'Can delete shield data'
    auth_permission_63.content_type = ContentType.objects.get(app_label="shipBuilder", model="shielddata")
    auth_permission_63.codename = u'delete_shielddata'
    auth_permission_63 = importer.save_or_locate(auth_permission_63)

    auth_permission_64 = Permission()
    auth_permission_64.name = u'Can add ship'
    auth_permission_64.content_type = ContentType.objects.get(app_label="shipBuilder", model="ship")
    auth_permission_64.codename = u'add_ship'
    auth_permission_64 = importer.save_or_locate(auth_permission_64)

    auth_permission_65 = Permission()
    auth_permission_65.name = u'Can change ship'
    auth_permission_65.content_type = ContentType.objects.get(app_label="shipBuilder", model="ship")
    auth_permission_65.codename = u'change_ship'
    auth_permission_65 = importer.save_or_locate(auth_permission_65)

    auth_permission_66 = Permission()
    auth_permission_66.name = u'Can delete ship'
    auth_permission_66.content_type = ContentType.objects.get(app_label="shipBuilder", model="ship")
    auth_permission_66.codename = u'delete_ship'
    auth_permission_66 = importer.save_or_locate(auth_permission_66)

    auth_permission_67 = Permission()
    auth_permission_67.name = u'Can add thruster data'
    auth_permission_67.content_type = ContentType.objects.get(app_label="shipBuilder", model="thrusterdata")
    auth_permission_67.codename = u'add_thrusterdata'
    auth_permission_67 = importer.save_or_locate(auth_permission_67)

    auth_permission_68 = Permission()
    auth_permission_68.name = u'Can change thruster data'
    auth_permission_68.content_type = ContentType.objects.get(app_label="shipBuilder", model="thrusterdata")
    auth_permission_68.codename = u'change_thrusterdata'
    auth_permission_68 = importer.save_or_locate(auth_permission_68)

    auth_permission_69 = Permission()
    auth_permission_69.name = u'Can delete thruster data'
    auth_permission_69.content_type = ContentType.objects.get(app_label="shipBuilder", model="thrusterdata")
    auth_permission_69.codename = u'delete_thrusterdata'
    auth_permission_69 = importer.save_or_locate(auth_permission_69)

    auth_permission_70 = Permission()
    auth_permission_70.name = u'Can add vehicle'
    auth_permission_70.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    auth_permission_70.codename = u'add_vehicle'
    auth_permission_70 = importer.save_or_locate(auth_permission_70)

    auth_permission_71 = Permission()
    auth_permission_71.name = u'Can change vehicle'
    auth_permission_71.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    auth_permission_71.codename = u'change_vehicle'
    auth_permission_71 = importer.save_or_locate(auth_permission_71)

    auth_permission_72 = Permission()
    auth_permission_72.name = u'Can delete vehicle'
    auth_permission_72.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    auth_permission_72.codename = u'delete_vehicle'
    auth_permission_72 = importer.save_or_locate(auth_permission_72)

    auth_permission_73 = Permission()
    auth_permission_73.name = u'Can add vehicle category'
    auth_permission_73.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehiclecategory")
    auth_permission_73.codename = u'add_vehiclecategory'
    auth_permission_73 = importer.save_or_locate(auth_permission_73)

    auth_permission_74 = Permission()
    auth_permission_74.name = u'Can change vehicle category'
    auth_permission_74.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehiclecategory")
    auth_permission_74.codename = u'change_vehiclecategory'
    auth_permission_74 = importer.save_or_locate(auth_permission_74)

    auth_permission_75 = Permission()
    auth_permission_75.name = u'Can delete vehicle category'
    auth_permission_75.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehiclecategory")
    auth_permission_75.codename = u'delete_vehiclecategory'
    auth_permission_75 = importer.save_or_locate(auth_permission_75)

    auth_permission_76 = Permission()
    auth_permission_76.name = u'Can add vehicle image'
    auth_permission_76.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleimage")
    auth_permission_76.codename = u'add_vehicleimage'
    auth_permission_76 = importer.save_or_locate(auth_permission_76)

    auth_permission_77 = Permission()
    auth_permission_77.name = u'Can change vehicle image'
    auth_permission_77.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleimage")
    auth_permission_77.codename = u'change_vehicleimage'
    auth_permission_77 = importer.save_or_locate(auth_permission_77)

    auth_permission_78 = Permission()
    auth_permission_78.name = u'Can delete vehicle image'
    auth_permission_78.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleimage")
    auth_permission_78.codename = u'delete_vehicleimage'
    auth_permission_78 = importer.save_or_locate(auth_permission_78)

    auth_permission_79 = Permission()
    auth_permission_79.name = u'Can add vehicle item'
    auth_permission_79.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitem")
    auth_permission_79.codename = u'add_vehicleitem'
    auth_permission_79 = importer.save_or_locate(auth_permission_79)

    auth_permission_80 = Permission()
    auth_permission_80.name = u'Can change vehicle item'
    auth_permission_80.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitem")
    auth_permission_80.codename = u'change_vehicleitem'
    auth_permission_80 = importer.save_or_locate(auth_permission_80)

    auth_permission_81 = Permission()
    auth_permission_81.name = u'Can delete vehicle item'
    auth_permission_81.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitem")
    auth_permission_81.codename = u'delete_vehicleitem'
    auth_permission_81 = importer.save_or_locate(auth_permission_81)

    auth_permission_82 = Permission()
    auth_permission_82.name = u'Can add vehicle item avionics'
    auth_permission_82.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemavionics")
    auth_permission_82.codename = u'add_vehicleitemavionics'
    auth_permission_82 = importer.save_or_locate(auth_permission_82)

    auth_permission_83 = Permission()
    auth_permission_83.name = u'Can change vehicle item avionics'
    auth_permission_83.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemavionics")
    auth_permission_83.codename = u'change_vehicleitemavionics'
    auth_permission_83 = importer.save_or_locate(auth_permission_83)

    auth_permission_84 = Permission()
    auth_permission_84.name = u'Can delete vehicle item avionics'
    auth_permission_84.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemavionics")
    auth_permission_84.codename = u'delete_vehicleitemavionics'
    auth_permission_84 = importer.save_or_locate(auth_permission_84)

    auth_permission_85 = Permission()
    auth_permission_85.name = u'Can add vehicle item heat'
    auth_permission_85.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemheat")
    auth_permission_85.codename = u'add_vehicleitemheat'
    auth_permission_85 = importer.save_or_locate(auth_permission_85)

    auth_permission_86 = Permission()
    auth_permission_86.name = u'Can change vehicle item heat'
    auth_permission_86.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemheat")
    auth_permission_86.codename = u'change_vehicleitemheat'
    auth_permission_86 = importer.save_or_locate(auth_permission_86)

    auth_permission_87 = Permission()
    auth_permission_87.name = u'Can delete vehicle item heat'
    auth_permission_87.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemheat")
    auth_permission_87.codename = u'delete_vehicleitemheat'
    auth_permission_87 = importer.save_or_locate(auth_permission_87)

    auth_permission_88 = Permission()
    auth_permission_88.name = u'Can add vehicle item params'
    auth_permission_88.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemparams")
    auth_permission_88.codename = u'add_vehicleitemparams'
    auth_permission_88 = importer.save_or_locate(auth_permission_88)

    auth_permission_89 = Permission()
    auth_permission_89.name = u'Can change vehicle item params'
    auth_permission_89.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemparams")
    auth_permission_89.codename = u'change_vehicleitemparams'
    auth_permission_89 = importer.save_or_locate(auth_permission_89)

    auth_permission_90 = Permission()
    auth_permission_90.name = u'Can delete vehicle item params'
    auth_permission_90.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemparams")
    auth_permission_90.codename = u'delete_vehicleitemparams'
    auth_permission_90 = importer.save_or_locate(auth_permission_90)

    auth_permission_91 = Permission()
    auth_permission_91.name = u'Can add vehicle item power'
    auth_permission_91.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitempower")
    auth_permission_91.codename = u'add_vehicleitempower'
    auth_permission_91 = importer.save_or_locate(auth_permission_91)

    auth_permission_92 = Permission()
    auth_permission_92.name = u'Can change vehicle item power'
    auth_permission_92.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitempower")
    auth_permission_92.codename = u'change_vehicleitempower'
    auth_permission_92 = importer.save_or_locate(auth_permission_92)

    auth_permission_93 = Permission()
    auth_permission_93.name = u'Can delete vehicle item power'
    auth_permission_93.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitempower")
    auth_permission_93.codename = u'delete_vehicleitempower'
    auth_permission_93 = importer.save_or_locate(auth_permission_93)

    auth_permission_94 = Permission()
    auth_permission_94.name = u'Can add vehicle item sub type'
    auth_permission_94.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemsubtype")
    auth_permission_94.codename = u'add_vehicleitemsubtype'
    auth_permission_94 = importer.save_or_locate(auth_permission_94)

    auth_permission_95 = Permission()
    auth_permission_95.name = u'Can change vehicle item sub type'
    auth_permission_95.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemsubtype")
    auth_permission_95.codename = u'change_vehicleitemsubtype'
    auth_permission_95 = importer.save_or_locate(auth_permission_95)

    auth_permission_96 = Permission()
    auth_permission_96.name = u'Can delete vehicle item sub type'
    auth_permission_96.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemsubtype")
    auth_permission_96.codename = u'delete_vehicleitemsubtype'
    auth_permission_96 = importer.save_or_locate(auth_permission_96)

    auth_permission_97 = Permission()
    auth_permission_97.name = u'Can add vehicle item type'
    auth_permission_97.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemtype")
    auth_permission_97.codename = u'add_vehicleitemtype'
    auth_permission_97 = importer.save_or_locate(auth_permission_97)

    auth_permission_98 = Permission()
    auth_permission_98.name = u'Can change vehicle item type'
    auth_permission_98.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemtype")
    auth_permission_98.codename = u'change_vehicleitemtype'
    auth_permission_98 = importer.save_or_locate(auth_permission_98)

    auth_permission_99 = Permission()
    auth_permission_99.name = u'Can delete vehicle item type'
    auth_permission_99.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicleitemtype")
    auth_permission_99.codename = u'delete_vehicleitemtype'
    auth_permission_99 = importer.save_or_locate(auth_permission_99)

    auth_permission_100 = Permission()
    auth_permission_100.name = u'Can add weapon data'
    auth_permission_100.content_type = ContentType.objects.get(app_label="shipBuilder", model="weapondata")
    auth_permission_100.codename = u'add_weapondata'
    auth_permission_100 = importer.save_or_locate(auth_permission_100)

    auth_permission_101 = Permission()
    auth_permission_101.name = u'Can change weapon data'
    auth_permission_101.content_type = ContentType.objects.get(app_label="shipBuilder", model="weapondata")
    auth_permission_101.codename = u'change_weapondata'
    auth_permission_101 = importer.save_or_locate(auth_permission_101)

    auth_permission_102 = Permission()
    auth_permission_102.name = u'Can delete weapon data'
    auth_permission_102.content_type = ContentType.objects.get(app_label="shipBuilder", model="weapondata")
    auth_permission_102.codename = u'delete_weapondata'
    auth_permission_102 = importer.save_or_locate(auth_permission_102)

    auth_permission_103 = Permission()
    auth_permission_103.name = u'Can add migration history'
    auth_permission_103.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_103.codename = u'add_migrationhistory'
    auth_permission_103 = importer.save_or_locate(auth_permission_103)

    auth_permission_104 = Permission()
    auth_permission_104.name = u'Can change migration history'
    auth_permission_104.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_104.codename = u'change_migrationhistory'
    auth_permission_104 = importer.save_or_locate(auth_permission_104)

    auth_permission_105 = Permission()
    auth_permission_105.name = u'Can delete migration history'
    auth_permission_105.content_type = ContentType.objects.get(app_label="south", model="migrationhistory")
    auth_permission_105.codename = u'delete_migrationhistory'
    auth_permission_105 = importer.save_or_locate(auth_permission_105)

    #Processing model: Group

    from django.contrib.auth.models import Group


    #Processing model: User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = u'pbkdf2_sha256$10000$qb2UGaB4nTAF$6aaxxmYGlFok9IHlAPTWtWmfZJUoP8KsKdNhXG1wFbo='
    auth_user_1.last_login = datetime.datetime(2013, 9, 4, 14, 9, 59, tzinfo=<UTC>)
    auth_user_1.is_superuser = True
    auth_user_1.username = u'agathorn'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'jwvanderbeck@gmail.com'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = datetime.datetime(2013, 9, 4, 14, 1, 47, tzinfo=<UTC>)
    auth_user_1 = importer.save_or_locate(auth_user_1)

    #Processing model: Session

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'1yd5p2vd1r30u6qc5t6tlw1e1xcr3mcm'
    django_session_1.session_data = u'YWIxNWIzZWFiYTc3N2U1YWQ2ZTkyYWIzNTkwZDI0MjA5N2Q1YzRiMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg=='
    django_session_1.expire_date = datetime.datetime(2013, 9, 18, 14, 9, 59, tzinfo=<UTC>)
    django_session_1 = importer.save_or_locate(django_session_1)

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

    shipBuilder_manufacturer_36 = Manufacturer()
    shipBuilder_manufacturer_36.name = u'A & R'
    shipBuilder_manufacturer_36.description = u''
    shipBuilder_manufacturer_36 = importer.save_or_locate(shipBuilder_manufacturer_36)

    shipBuilder_manufacturer_37 = Manufacturer()
    shipBuilder_manufacturer_37.name = u'Ageis Dynamics'
    shipBuilder_manufacturer_37.description = u''
    shipBuilder_manufacturer_37 = importer.save_or_locate(shipBuilder_manufacturer_37)

    shipBuilder_manufacturer_38 = Manufacturer()
    shipBuilder_manufacturer_38.name = u'RSI'
    shipBuilder_manufacturer_38.description = u''
    shipBuilder_manufacturer_38 = importer.save_or_locate(shipBuilder_manufacturer_38)

    shipBuilder_manufacturer_39 = Manufacturer()
    shipBuilder_manufacturer_39.name = u'Sakura Sun'
    shipBuilder_manufacturer_39.description = u''
    shipBuilder_manufacturer_39 = importer.save_or_locate(shipBuilder_manufacturer_39)

    shipBuilder_manufacturer_40 = Manufacturer()
    shipBuilder_manufacturer_40.name = u'KDK'
    shipBuilder_manufacturer_40.description = u''
    shipBuilder_manufacturer_40 = importer.save_or_locate(shipBuilder_manufacturer_40)

    shipBuilder_manufacturer_41 = Manufacturer()
    shipBuilder_manufacturer_41.name = u'Dragon STC'
    shipBuilder_manufacturer_41.description = u''
    shipBuilder_manufacturer_41 = importer.save_or_locate(shipBuilder_manufacturer_41)

    shipBuilder_manufacturer_42 = Manufacturer()
    shipBuilder_manufacturer_42.name = u'V&uul Tech'
    shipBuilder_manufacturer_42.description = u''
    shipBuilder_manufacturer_42 = importer.save_or_locate(shipBuilder_manufacturer_42)

    shipBuilder_manufacturer_43 = Manufacturer()
    shipBuilder_manufacturer_43.name = u'VOLT'
    shipBuilder_manufacturer_43.description = u''
    shipBuilder_manufacturer_43 = importer.save_or_locate(shipBuilder_manufacturer_43)

    shipBuilder_manufacturer_44 = Manufacturer()
    shipBuilder_manufacturer_44.name = u'KnightBridge'
    shipBuilder_manufacturer_44.description = u''
    shipBuilder_manufacturer_44 = importer.save_or_locate(shipBuilder_manufacturer_44)

    shipBuilder_manufacturer_45 = Manufacturer()
    shipBuilder_manufacturer_45.name = u'Lightning Power ltd.'
    shipBuilder_manufacturer_45.description = u''
    shipBuilder_manufacturer_45 = importer.save_or_locate(shipBuilder_manufacturer_45)

    shipBuilder_manufacturer_46 = Manufacturer()
    shipBuilder_manufacturer_46.name = u'XForge'
    shipBuilder_manufacturer_46.description = u''
    shipBuilder_manufacturer_46 = importer.save_or_locate(shipBuilder_manufacturer_46)

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
    shipBuilder_ship_1.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_ship_1.description = u"If you're going to travel the stars... why not do it in style? The 300i is Origin Jumpworks' premiere luxury spacecraft. It is a sleek, silver killer that sends as much of a message with its silhouette as it does with its weaponry."
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
    shipBuilder_ship_2.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_ship_2.description = u"The Aurora is the modern day descendant of the Roberts Space Industries X-7 spacecraft which tested the very first jump engines. Utilitarian to a T, the Aurora is the perfect beginner's ship: what it lacks in style it makes up for in ample room for upgrade modules."
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
    shipBuilder_ship_3.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_ship_3.description = u"The Constellation, a multi-person freighter, is the most popular ship in RSI's current production array.  Constellations are beloved by smugglers and merchants alike because they are modular, high powered... and just downright iconic-looking."
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
    shipBuilder_ship_4.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_ship_4.description = u"The combination of a Gangleri BP 707 Standard powerplant with a 300i fuselate re-engineered to accommodate twin Hammer Propulsion HM 4.3 thrusters makes the 350r the fastest personal craft you'll ever call your own."
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
    shipBuilder_ship_5.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_ship_5.description = u"To the enemy, it is a weapon never to be underestimated. To allies, it's a savior. The F7C Hornet is the same dependable and resilient multi-purpose fighter that has become the face of the UEE Navy. The F7C is the foundation to build on and meet whatever requirements you have in mind."
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
    shipBuilder_ship_6.manufacturer = shipBuilder_manufacturer_33
    shipBuilder_ship_6.description = u'The Aegis Avenger has had a long and storied life as the standard patrol craft of the UEE Advocacy. Although aging, the Avenger features a sturdy, reliable hull and the capacity for larger-than-expected engine mounts and a front-mounted cannon guaranteed to strike fear into your opponents.'
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
    shipBuilder_ship_7.manufacturer = shipBuilder_manufacturer_34
    shipBuilder_ship_7.description = u'Freelancers are used as long haul merchant ships by major corporations, but they are just as frequently repurposed as dedicated exploration vessels by independent captains who want to operate on the fringes of the galaxy.'
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
    shipBuilder_ship_8.manufacturer = shipBuilder_manufacturer_35
    shipBuilder_ship_8.description = u'Coming standard with the Constellation, the P52 is a versatile short-range fighter designed to offer support in combat situations as well as reconnaissance.'
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

    #Processing model: VehicleItemType

    from shipBuilder.models import VehicleItemType

    shipBuilder_vehicleitemtype_1 = VehicleItemType()
    shipBuilder_vehicleitemtype_1.typeName = u'Container'
    shipBuilder_vehicleitemtype_1 = importer.save_or_locate(shipBuilder_vehicleitemtype_1)

    shipBuilder_vehicleitemtype_2 = VehicleItemType()
    shipBuilder_vehicleitemtype_2.typeName = u'Weapon'
    shipBuilder_vehicleitemtype_2 = importer.save_or_locate(shipBuilder_vehicleitemtype_2)

    shipBuilder_vehicleitemtype_3 = VehicleItemType()
    shipBuilder_vehicleitemtype_3.typeName = u'Thruster'
    shipBuilder_vehicleitemtype_3 = importer.save_or_locate(shipBuilder_vehicleitemtype_3)

    shipBuilder_vehicleitemtype_4 = VehicleItemType()
    shipBuilder_vehicleitemtype_4.typeName = u'PowerPlant'
    shipBuilder_vehicleitemtype_4 = importer.save_or_locate(shipBuilder_vehicleitemtype_4)

    shipBuilder_vehicleitemtype_5 = VehicleItemType()
    shipBuilder_vehicleitemtype_5.typeName = u'Radar'
    shipBuilder_vehicleitemtype_5 = importer.save_or_locate(shipBuilder_vehicleitemtype_5)

    shipBuilder_vehicleitemtype_6 = VehicleItemType()
    shipBuilder_vehicleitemtype_6.typeName = u'Display'
    shipBuilder_vehicleitemtype_6 = importer.save_or_locate(shipBuilder_vehicleitemtype_6)

    shipBuilder_vehicleitemtype_7 = VehicleItemType()
    shipBuilder_vehicleitemtype_7.typeName = u'Visor'
    shipBuilder_vehicleitemtype_7 = importer.save_or_locate(shipBuilder_vehicleitemtype_7)

    shipBuilder_vehicleitemtype_8 = VehicleItemType()
    shipBuilder_vehicleitemtype_8.typeName = u'Cooler'
    shipBuilder_vehicleitemtype_8 = importer.save_or_locate(shipBuilder_vehicleitemtype_8)

    shipBuilder_vehicleitemtype_9 = VehicleItemType()
    shipBuilder_vehicleitemtype_9.typeName = u'Avionics'
    shipBuilder_vehicleitemtype_9 = importer.save_or_locate(shipBuilder_vehicleitemtype_9)

    shipBuilder_vehicleitemtype_10 = VehicleItemType()
    shipBuilder_vehicleitemtype_10.typeName = u'Battery'
    shipBuilder_vehicleitemtype_10 = importer.save_or_locate(shipBuilder_vehicleitemtype_10)

    #Processing model: VehicleItemSubType

    from shipBuilder.models import VehicleItemSubType

    shipBuilder_vehicleitemsubtype_1 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_1.subTypeName = u'Cargo'
    shipBuilder_vehicleitemsubtype_1.parent = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitemsubtype_1 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_1)

    shipBuilder_vehicleitemsubtype_2 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_2.subTypeName = u'Gun'
    shipBuilder_vehicleitemsubtype_2.parent = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitemsubtype_2 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_vehicleitemsubtype_3 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_3.subTypeName = u'VectorThruster'
    shipBuilder_vehicleitemsubtype_3.parent = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitemsubtype_3 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_3)

    shipBuilder_vehicleitemsubtype_4 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_4.subTypeName = u'MissileTurret'
    shipBuilder_vehicleitemsubtype_4.parent = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitemsubtype_4 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_4)

    shipBuilder_vehicleitemsubtype_5 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_5.subTypeName = u'Power'
    shipBuilder_vehicleitemsubtype_5.parent = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitemsubtype_5 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_vehicleitemsubtype_6 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_6.subTypeName = u'MissileRack'
    shipBuilder_vehicleitemsubtype_6.parent = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitemsubtype_6 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_vehicleitemsubtype_7 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_7.subTypeName = u'GunTurret'
    shipBuilder_vehicleitemsubtype_7.parent = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitemsubtype_7 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_7)

    shipBuilder_vehicleitemsubtype_8 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_8.subTypeName = u'FlexThruster'
    shipBuilder_vehicleitemsubtype_8.parent = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitemsubtype_8 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_8)

    shipBuilder_vehicleitemsubtype_9 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_9.subTypeName = u'MidRangeRadar'
    shipBuilder_vehicleitemsubtype_9.parent = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitemsubtype_9 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_9)

    shipBuilder_vehicleitemsubtype_10 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_10.subTypeName = u'JointThruster'
    shipBuilder_vehicleitemsubtype_10.parent = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitemsubtype_10 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_10)

    shipBuilder_vehicleitemsubtype_11 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_11.subTypeName = u'FixedThruster'
    shipBuilder_vehicleitemsubtype_11.parent = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitemsubtype_11 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_vehicleitemsubtype_12 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_12.subTypeName = u'Weapon'
    shipBuilder_vehicleitemsubtype_12.parent = shipBuilder_vehicleitemtype_6
    shipBuilder_vehicleitemsubtype_12 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_12)

    shipBuilder_vehicleitemsubtype_13 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_13.subTypeName = u'Tagging'
    shipBuilder_vehicleitemsubtype_13.parent = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitemsubtype_13 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_13)

    shipBuilder_vehicleitemsubtype_14 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_14.subTypeName = u'Heat'
    shipBuilder_vehicleitemsubtype_14.parent = shipBuilder_vehicleitemtype_8
    shipBuilder_vehicleitemsubtype_14 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_14)

    shipBuilder_vehicleitemsubtype_15 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_15.subTypeName = u'Radar'
    shipBuilder_vehicleitemsubtype_15.parent = shipBuilder_vehicleitemtype_6
    shipBuilder_vehicleitemsubtype_15 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_vehicleitemsubtype_16 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_16.subTypeName = u'TargetingComputer'
    shipBuilder_vehicleitemsubtype_16.parent = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitemsubtype_16 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_16)

    shipBuilder_vehicleitemsubtype_17 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_17.subTypeName = u'LongRangeRadar'
    shipBuilder_vehicleitemsubtype_17.parent = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitemsubtype_17 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_17)

    shipBuilder_vehicleitemsubtype_18 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_18.subTypeName = u'Power'
    shipBuilder_vehicleitemsubtype_18.parent = shipBuilder_vehicleitemtype_10
    shipBuilder_vehicleitemsubtype_18 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_18)

    shipBuilder_vehicleitemsubtype_19 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_19.subTypeName = u'ShortRangeRadar'
    shipBuilder_vehicleitemsubtype_19.parent = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitemsubtype_19 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_19)

    #Processing model: VehicleItemParams

    from shipBuilder.models import VehicleItemParams

    shipBuilder_vehicleitemparams_1 = VehicleItemParams()
    shipBuilder_vehicleitemparams_1.name = u'acceleration'
    shipBuilder_vehicleitemparams_1.value = 20.0
    shipBuilder_vehicleitemparams_1 = importer.save_or_locate(shipBuilder_vehicleitemparams_1)

    shipBuilder_vehicleitemparams_2 = VehicleItemParams()
    shipBuilder_vehicleitemparams_2.name = u'pitchMax'
    shipBuilder_vehicleitemparams_2.value = 10.0
    shipBuilder_vehicleitemparams_2 = importer.save_or_locate(shipBuilder_vehicleitemparams_2)

    shipBuilder_vehicleitemparams_3 = VehicleItemParams()
    shipBuilder_vehicleitemparams_3.name = u'maxThrust'
    shipBuilder_vehicleitemparams_3.value = 2600000.0
    shipBuilder_vehicleitemparams_3 = importer.save_or_locate(shipBuilder_vehicleitemparams_3)

    shipBuilder_vehicleitemparams_4 = VehicleItemParams()
    shipBuilder_vehicleitemparams_4.name = u'pitchMin'
    shipBuilder_vehicleitemparams_4.value = -10.0
    shipBuilder_vehicleitemparams_4 = importer.save_or_locate(shipBuilder_vehicleitemparams_4)

    shipBuilder_vehicleitemparams_5 = VehicleItemParams()
    shipBuilder_vehicleitemparams_5.name = u'yawMin'
    shipBuilder_vehicleitemparams_5.value = -10.0
    shipBuilder_vehicleitemparams_5 = importer.save_or_locate(shipBuilder_vehicleitemparams_5)

    shipBuilder_vehicleitemparams_6 = VehicleItemParams()
    shipBuilder_vehicleitemparams_6.name = u'yawMax'
    shipBuilder_vehicleitemparams_6.value = 10.0
    shipBuilder_vehicleitemparams_6 = importer.save_or_locate(shipBuilder_vehicleitemparams_6)

    shipBuilder_vehicleitemparams_7 = VehicleItemParams()
    shipBuilder_vehicleitemparams_7.name = u'speed'
    shipBuilder_vehicleitemparams_7.value = 40.0
    shipBuilder_vehicleitemparams_7 = importer.save_or_locate(shipBuilder_vehicleitemparams_7)

    shipBuilder_vehicleitemparams_8 = VehicleItemParams()
    shipBuilder_vehicleitemparams_8.name = u'Speed'
    shipBuilder_vehicleitemparams_8.value = 80.0
    shipBuilder_vehicleitemparams_8 = importer.save_or_locate(shipBuilder_vehicleitemparams_8)

    shipBuilder_vehicleitemparams_9 = VehicleItemParams()
    shipBuilder_vehicleitemparams_9.name = u'Warhead'
    shipBuilder_vehicleitemparams_9.value = 51.43
    shipBuilder_vehicleitemparams_9 = importer.save_or_locate(shipBuilder_vehicleitemparams_9)

    shipBuilder_vehicleitemparams_10 = VehicleItemParams()
    shipBuilder_vehicleitemparams_10.name = u'Radius'
    shipBuilder_vehicleitemparams_10.value = 66.67
    shipBuilder_vehicleitemparams_10 = importer.save_or_locate(shipBuilder_vehicleitemparams_10)

    shipBuilder_vehicleitemparams_11 = VehicleItemParams()
    shipBuilder_vehicleitemparams_11.name = u'Concuss'
    shipBuilder_vehicleitemparams_11.value = 66.67
    shipBuilder_vehicleitemparams_11 = importer.save_or_locate(shipBuilder_vehicleitemparams_11)

    shipBuilder_vehicleitemparams_12 = VehicleItemParams()
    shipBuilder_vehicleitemparams_12.name = u'acceleration'
    shipBuilder_vehicleitemparams_12.value = 40.0
    shipBuilder_vehicleitemparams_12 = importer.save_or_locate(shipBuilder_vehicleitemparams_12)

    shipBuilder_vehicleitemparams_13 = VehicleItemParams()
    shipBuilder_vehicleitemparams_13.name = u'maxThrust'
    shipBuilder_vehicleitemparams_13.value = 300000.0
    shipBuilder_vehicleitemparams_13 = importer.save_or_locate(shipBuilder_vehicleitemparams_13)

    shipBuilder_vehicleitemparams_14 = VehicleItemParams()
    shipBuilder_vehicleitemparams_14.name = u'speed'
    shipBuilder_vehicleitemparams_14.value = 80.0
    shipBuilder_vehicleitemparams_14 = importer.save_or_locate(shipBuilder_vehicleitemparams_14)

    shipBuilder_vehicleitemparams_15 = VehicleItemParams()
    shipBuilder_vehicleitemparams_15.name = u'pitchMin'
    shipBuilder_vehicleitemparams_15.value = -45.0
    shipBuilder_vehicleitemparams_15 = importer.save_or_locate(shipBuilder_vehicleitemparams_15)

    shipBuilder_vehicleitemparams_16 = VehicleItemParams()
    shipBuilder_vehicleitemparams_16.name = u'pitchMax'
    shipBuilder_vehicleitemparams_16.value = 45.0
    shipBuilder_vehicleitemparams_16 = importer.save_or_locate(shipBuilder_vehicleitemparams_16)

    shipBuilder_vehicleitemparams_17 = VehicleItemParams()
    shipBuilder_vehicleitemparams_17.name = u'Speed'
    shipBuilder_vehicleitemparams_17.value = 75.5
    shipBuilder_vehicleitemparams_17 = importer.save_or_locate(shipBuilder_vehicleitemparams_17)

    shipBuilder_vehicleitemparams_18 = VehicleItemParams()
    shipBuilder_vehicleitemparams_18.name = u'Warhead'
    shipBuilder_vehicleitemparams_18.value = 71.43
    shipBuilder_vehicleitemparams_18 = importer.save_or_locate(shipBuilder_vehicleitemparams_18)

    shipBuilder_vehicleitemparams_19 = VehicleItemParams()
    shipBuilder_vehicleitemparams_19.name = u'Radius'
    shipBuilder_vehicleitemparams_19.value = 23.33
    shipBuilder_vehicleitemparams_19 = importer.save_or_locate(shipBuilder_vehicleitemparams_19)

    shipBuilder_vehicleitemparams_20 = VehicleItemParams()
    shipBuilder_vehicleitemparams_20.name = u'Concuss'
    shipBuilder_vehicleitemparams_20.value = 9.33
    shipBuilder_vehicleitemparams_20 = importer.save_or_locate(shipBuilder_vehicleitemparams_20)

    shipBuilder_vehicleitemparams_21 = VehicleItemParams()
    shipBuilder_vehicleitemparams_21.name = u'gridSize'
    shipBuilder_vehicleitemparams_21.value = 5.0
    shipBuilder_vehicleitemparams_21 = importer.save_or_locate(shipBuilder_vehicleitemparams_21)

    shipBuilder_vehicleitemparams_22 = VehicleItemParams()
    shipBuilder_vehicleitemparams_22.name = u'radius'
    shipBuilder_vehicleitemparams_22.value = 3000.0
    shipBuilder_vehicleitemparams_22 = importer.save_or_locate(shipBuilder_vehicleitemparams_22)

    shipBuilder_vehicleitemparams_23 = VehicleItemParams()
    shipBuilder_vehicleitemparams_23.name = u'identifyTime'
    shipBuilder_vehicleitemparams_23.value = 0.5
    shipBuilder_vehicleitemparams_23 = importer.save_or_locate(shipBuilder_vehicleitemparams_23)

    shipBuilder_vehicleitemparams_24 = VehicleItemParams()
    shipBuilder_vehicleitemparams_24.name = u'radarTime'
    shipBuilder_vehicleitemparams_24.value = 1.0
    shipBuilder_vehicleitemparams_24 = importer.save_or_locate(shipBuilder_vehicleitemparams_24)

    shipBuilder_vehicleitemparams_25 = VehicleItemParams()
    shipBuilder_vehicleitemparams_25.name = u'radarType'
    shipBuilder_vehicleitemparams_25.value = 1.0
    shipBuilder_vehicleitemparams_25 = importer.save_or_locate(shipBuilder_vehicleitemparams_25)

    shipBuilder_vehicleitemparams_26 = VehicleItemParams()
    shipBuilder_vehicleitemparams_26.name = u'RoF'
    shipBuilder_vehicleitemparams_26.value = 3.0
    shipBuilder_vehicleitemparams_26 = importer.save_or_locate(shipBuilder_vehicleitemparams_26)

    shipBuilder_vehicleitemparams_27 = VehicleItemParams()
    shipBuilder_vehicleitemparams_27.name = u'Range'
    shipBuilder_vehicleitemparams_27.value = 90.0
    shipBuilder_vehicleitemparams_27 = importer.save_or_locate(shipBuilder_vehicleitemparams_27)

    shipBuilder_vehicleitemparams_28 = VehicleItemParams()
    shipBuilder_vehicleitemparams_28.name = u'Damage'
    shipBuilder_vehicleitemparams_28.value = 2.5
    shipBuilder_vehicleitemparams_28 = importer.save_or_locate(shipBuilder_vehicleitemparams_28)

    shipBuilder_vehicleitemparams_29 = VehicleItemParams()
    shipBuilder_vehicleitemparams_29.name = u'Power'
    shipBuilder_vehicleitemparams_29.value = 19.5
    shipBuilder_vehicleitemparams_29 = importer.save_or_locate(shipBuilder_vehicleitemparams_29)

    shipBuilder_vehicleitemparams_30 = VehicleItemParams()
    shipBuilder_vehicleitemparams_30.name = u'acceleration'
    shipBuilder_vehicleitemparams_30.value = 40.0
    shipBuilder_vehicleitemparams_30 = importer.save_or_locate(shipBuilder_vehicleitemparams_30)

    shipBuilder_vehicleitemparams_31 = VehicleItemParams()
    shipBuilder_vehicleitemparams_31.name = u'maxThrust'
    shipBuilder_vehicleitemparams_31.value = 300000.0
    shipBuilder_vehicleitemparams_31 = importer.save_or_locate(shipBuilder_vehicleitemparams_31)

    shipBuilder_vehicleitemparams_32 = VehicleItemParams()
    shipBuilder_vehicleitemparams_32.name = u'speed'
    shipBuilder_vehicleitemparams_32.value = 80.0
    shipBuilder_vehicleitemparams_32 = importer.save_or_locate(shipBuilder_vehicleitemparams_32)

    shipBuilder_vehicleitemparams_33 = VehicleItemParams()
    shipBuilder_vehicleitemparams_33.name = u'pitchMin'
    shipBuilder_vehicleitemparams_33.value = -40.0
    shipBuilder_vehicleitemparams_33 = importer.save_or_locate(shipBuilder_vehicleitemparams_33)

    shipBuilder_vehicleitemparams_34 = VehicleItemParams()
    shipBuilder_vehicleitemparams_34.name = u'pitchMax'
    shipBuilder_vehicleitemparams_34.value = 40.0
    shipBuilder_vehicleitemparams_34 = importer.save_or_locate(shipBuilder_vehicleitemparams_34)

    shipBuilder_vehicleitemparams_35 = VehicleItemParams()
    shipBuilder_vehicleitemparams_35.name = u'acceleration'
    shipBuilder_vehicleitemparams_35.value = 40.0
    shipBuilder_vehicleitemparams_35 = importer.save_or_locate(shipBuilder_vehicleitemparams_35)

    shipBuilder_vehicleitemparams_36 = VehicleItemParams()
    shipBuilder_vehicleitemparams_36.name = u'maxThrust'
    shipBuilder_vehicleitemparams_36.value = 300000.0
    shipBuilder_vehicleitemparams_36 = importer.save_or_locate(shipBuilder_vehicleitemparams_36)

    shipBuilder_vehicleitemparams_37 = VehicleItemParams()
    shipBuilder_vehicleitemparams_37.name = u'speed'
    shipBuilder_vehicleitemparams_37.value = 80.0
    shipBuilder_vehicleitemparams_37 = importer.save_or_locate(shipBuilder_vehicleitemparams_37)

    shipBuilder_vehicleitemparams_38 = VehicleItemParams()
    shipBuilder_vehicleitemparams_38.name = u'pitchMin'
    shipBuilder_vehicleitemparams_38.value = -45.0
    shipBuilder_vehicleitemparams_38 = importer.save_or_locate(shipBuilder_vehicleitemparams_38)

    shipBuilder_vehicleitemparams_39 = VehicleItemParams()
    shipBuilder_vehicleitemparams_39.name = u'pitchMax'
    shipBuilder_vehicleitemparams_39.value = 45.0
    shipBuilder_vehicleitemparams_39 = importer.save_or_locate(shipBuilder_vehicleitemparams_39)

    shipBuilder_vehicleitemparams_40 = VehicleItemParams()
    shipBuilder_vehicleitemparams_40.name = u'RoF'
    shipBuilder_vehicleitemparams_40.value = 20.0
    shipBuilder_vehicleitemparams_40 = importer.save_or_locate(shipBuilder_vehicleitemparams_40)

    shipBuilder_vehicleitemparams_41 = VehicleItemParams()
    shipBuilder_vehicleitemparams_41.name = u'Range'
    shipBuilder_vehicleitemparams_41.value = 90.0
    shipBuilder_vehicleitemparams_41 = importer.save_or_locate(shipBuilder_vehicleitemparams_41)

    shipBuilder_vehicleitemparams_42 = VehicleItemParams()
    shipBuilder_vehicleitemparams_42.name = u'Damage'
    shipBuilder_vehicleitemparams_42.value = 3.5
    shipBuilder_vehicleitemparams_42 = importer.save_or_locate(shipBuilder_vehicleitemparams_42)

    shipBuilder_vehicleitemparams_43 = VehicleItemParams()
    shipBuilder_vehicleitemparams_43.name = u'Power'
    shipBuilder_vehicleitemparams_43.value = 23.1
    shipBuilder_vehicleitemparams_43 = importer.save_or_locate(shipBuilder_vehicleitemparams_43)

    shipBuilder_vehicleitemparams_44 = VehicleItemParams()
    shipBuilder_vehicleitemparams_44.name = u'acceleration'
    shipBuilder_vehicleitemparams_44.value = 20.0
    shipBuilder_vehicleitemparams_44 = importer.save_or_locate(shipBuilder_vehicleitemparams_44)

    shipBuilder_vehicleitemparams_45 = VehicleItemParams()
    shipBuilder_vehicleitemparams_45.name = u'pitchMax'
    shipBuilder_vehicleitemparams_45.value = 10.0
    shipBuilder_vehicleitemparams_45 = importer.save_or_locate(shipBuilder_vehicleitemparams_45)

    shipBuilder_vehicleitemparams_46 = VehicleItemParams()
    shipBuilder_vehicleitemparams_46.name = u'maxThrust'
    shipBuilder_vehicleitemparams_46.value = 2600000.0
    shipBuilder_vehicleitemparams_46 = importer.save_or_locate(shipBuilder_vehicleitemparams_46)

    shipBuilder_vehicleitemparams_47 = VehicleItemParams()
    shipBuilder_vehicleitemparams_47.name = u'pitchMin'
    shipBuilder_vehicleitemparams_47.value = -10.0
    shipBuilder_vehicleitemparams_47 = importer.save_or_locate(shipBuilder_vehicleitemparams_47)

    shipBuilder_vehicleitemparams_48 = VehicleItemParams()
    shipBuilder_vehicleitemparams_48.name = u'yawMin'
    shipBuilder_vehicleitemparams_48.value = -10.0
    shipBuilder_vehicleitemparams_48 = importer.save_or_locate(shipBuilder_vehicleitemparams_48)

    shipBuilder_vehicleitemparams_49 = VehicleItemParams()
    shipBuilder_vehicleitemparams_49.name = u'yawMax'
    shipBuilder_vehicleitemparams_49.value = 10.0
    shipBuilder_vehicleitemparams_49 = importer.save_or_locate(shipBuilder_vehicleitemparams_49)

    shipBuilder_vehicleitemparams_50 = VehicleItemParams()
    shipBuilder_vehicleitemparams_50.name = u'speed'
    shipBuilder_vehicleitemparams_50.value = 40.0
    shipBuilder_vehicleitemparams_50 = importer.save_or_locate(shipBuilder_vehicleitemparams_50)

    shipBuilder_vehicleitemparams_51 = VehicleItemParams()
    shipBuilder_vehicleitemparams_51.name = u'RoF'
    shipBuilder_vehicleitemparams_51.value = 60.0
    shipBuilder_vehicleitemparams_51 = importer.save_or_locate(shipBuilder_vehicleitemparams_51)

    shipBuilder_vehicleitemparams_52 = VehicleItemParams()
    shipBuilder_vehicleitemparams_52.name = u'Range'
    shipBuilder_vehicleitemparams_52.value = 60.0
    shipBuilder_vehicleitemparams_52 = importer.save_or_locate(shipBuilder_vehicleitemparams_52)

    shipBuilder_vehicleitemparams_53 = VehicleItemParams()
    shipBuilder_vehicleitemparams_53.name = u'Damage'
    shipBuilder_vehicleitemparams_53.value = 1.0
    shipBuilder_vehicleitemparams_53 = importer.save_or_locate(shipBuilder_vehicleitemparams_53)

    shipBuilder_vehicleitemparams_54 = VehicleItemParams()
    shipBuilder_vehicleitemparams_54.name = u'Power'
    shipBuilder_vehicleitemparams_54.value = 27.0
    shipBuilder_vehicleitemparams_54 = importer.save_or_locate(shipBuilder_vehicleitemparams_54)

    shipBuilder_vehicleitemparams_55 = VehicleItemParams()
    shipBuilder_vehicleitemparams_55.name = u'acceleration'
    shipBuilder_vehicleitemparams_55.value = 20.0
    shipBuilder_vehicleitemparams_55 = importer.save_or_locate(shipBuilder_vehicleitemparams_55)

    shipBuilder_vehicleitemparams_56 = VehicleItemParams()
    shipBuilder_vehicleitemparams_56.name = u'maxThrust'
    shipBuilder_vehicleitemparams_56.value = 2600000.0
    shipBuilder_vehicleitemparams_56 = importer.save_or_locate(shipBuilder_vehicleitemparams_56)

    shipBuilder_vehicleitemparams_57 = VehicleItemParams()
    shipBuilder_vehicleitemparams_57.name = u'speed'
    shipBuilder_vehicleitemparams_57.value = 40.0
    shipBuilder_vehicleitemparams_57 = importer.save_or_locate(shipBuilder_vehicleitemparams_57)

    shipBuilder_vehicleitemparams_58 = VehicleItemParams()
    shipBuilder_vehicleitemparams_58.name = u'Speed'
    shipBuilder_vehicleitemparams_58.value = 74.0
    shipBuilder_vehicleitemparams_58 = importer.save_or_locate(shipBuilder_vehicleitemparams_58)

    shipBuilder_vehicleitemparams_59 = VehicleItemParams()
    shipBuilder_vehicleitemparams_59.name = u'Warhead'
    shipBuilder_vehicleitemparams_59.value = 64.28
    shipBuilder_vehicleitemparams_59 = importer.save_or_locate(shipBuilder_vehicleitemparams_59)

    shipBuilder_vehicleitemparams_60 = VehicleItemParams()
    shipBuilder_vehicleitemparams_60.name = u'Radius'
    shipBuilder_vehicleitemparams_60.value = 20.0
    shipBuilder_vehicleitemparams_60 = importer.save_or_locate(shipBuilder_vehicleitemparams_60)

    shipBuilder_vehicleitemparams_61 = VehicleItemParams()
    shipBuilder_vehicleitemparams_61.name = u'Concuss'
    shipBuilder_vehicleitemparams_61.value = 8.0
    shipBuilder_vehicleitemparams_61 = importer.save_or_locate(shipBuilder_vehicleitemparams_61)

    shipBuilder_vehicleitemparams_62 = VehicleItemParams()
    shipBuilder_vehicleitemparams_62.name = u'acceleration'
    shipBuilder_vehicleitemparams_62.value = 20.0
    shipBuilder_vehicleitemparams_62 = importer.save_or_locate(shipBuilder_vehicleitemparams_62)

    shipBuilder_vehicleitemparams_63 = VehicleItemParams()
    shipBuilder_vehicleitemparams_63.name = u'maxThrust'
    shipBuilder_vehicleitemparams_63.value = 2600000.0
    shipBuilder_vehicleitemparams_63 = importer.save_or_locate(shipBuilder_vehicleitemparams_63)

    shipBuilder_vehicleitemparams_64 = VehicleItemParams()
    shipBuilder_vehicleitemparams_64.name = u'speed'
    shipBuilder_vehicleitemparams_64.value = 40.0
    shipBuilder_vehicleitemparams_64 = importer.save_or_locate(shipBuilder_vehicleitemparams_64)

    shipBuilder_vehicleitemparams_65 = VehicleItemParams()
    shipBuilder_vehicleitemparams_65.name = u'pitchMax'
    shipBuilder_vehicleitemparams_65.value = 90.0
    shipBuilder_vehicleitemparams_65 = importer.save_or_locate(shipBuilder_vehicleitemparams_65)

    shipBuilder_vehicleitemparams_66 = VehicleItemParams()
    shipBuilder_vehicleitemparams_66.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_66.value = 40.0
    shipBuilder_vehicleitemparams_66 = importer.save_or_locate(shipBuilder_vehicleitemparams_66)

    shipBuilder_vehicleitemparams_67 = VehicleItemParams()
    shipBuilder_vehicleitemparams_67.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_67.value = 40.0
    shipBuilder_vehicleitemparams_67 = importer.save_or_locate(shipBuilder_vehicleitemparams_67)

    shipBuilder_vehicleitemparams_68 = VehicleItemParams()
    shipBuilder_vehicleitemparams_68.name = u'maxThrust'
    shipBuilder_vehicleitemparams_68.value = 350000.0
    shipBuilder_vehicleitemparams_68 = importer.save_or_locate(shipBuilder_vehicleitemparams_68)

    shipBuilder_vehicleitemparams_69 = VehicleItemParams()
    shipBuilder_vehicleitemparams_69.name = u'yawMax'
    shipBuilder_vehicleitemparams_69.value = 0.0
    shipBuilder_vehicleitemparams_69 = importer.save_or_locate(shipBuilder_vehicleitemparams_69)

    shipBuilder_vehicleitemparams_70 = VehicleItemParams()
    shipBuilder_vehicleitemparams_70.name = u'pitchMin'
    shipBuilder_vehicleitemparams_70.value = -90.0
    shipBuilder_vehicleitemparams_70 = importer.save_or_locate(shipBuilder_vehicleitemparams_70)

    shipBuilder_vehicleitemparams_71 = VehicleItemParams()
    shipBuilder_vehicleitemparams_71.name = u'yawMin'
    shipBuilder_vehicleitemparams_71.value = -90.0
    shipBuilder_vehicleitemparams_71 = importer.save_or_locate(shipBuilder_vehicleitemparams_71)

    shipBuilder_vehicleitemparams_72 = VehicleItemParams()
    shipBuilder_vehicleitemparams_72.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_72.value = 80.0
    shipBuilder_vehicleitemparams_72 = importer.save_or_locate(shipBuilder_vehicleitemparams_72)

    shipBuilder_vehicleitemparams_73 = VehicleItemParams()
    shipBuilder_vehicleitemparams_73.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_73.value = 80.0
    shipBuilder_vehicleitemparams_73 = importer.save_or_locate(shipBuilder_vehicleitemparams_73)

    shipBuilder_vehicleitemparams_74 = VehicleItemParams()
    shipBuilder_vehicleitemparams_74.name = u'Speed'
    shipBuilder_vehicleitemparams_74.value = 75.5
    shipBuilder_vehicleitemparams_74 = importer.save_or_locate(shipBuilder_vehicleitemparams_74)

    shipBuilder_vehicleitemparams_75 = VehicleItemParams()
    shipBuilder_vehicleitemparams_75.name = u'Warhead'
    shipBuilder_vehicleitemparams_75.value = 71.43
    shipBuilder_vehicleitemparams_75 = importer.save_or_locate(shipBuilder_vehicleitemparams_75)

    shipBuilder_vehicleitemparams_76 = VehicleItemParams()
    shipBuilder_vehicleitemparams_76.name = u'Radius'
    shipBuilder_vehicleitemparams_76.value = 23.33
    shipBuilder_vehicleitemparams_76 = importer.save_or_locate(shipBuilder_vehicleitemparams_76)

    shipBuilder_vehicleitemparams_77 = VehicleItemParams()
    shipBuilder_vehicleitemparams_77.name = u'Concuss'
    shipBuilder_vehicleitemparams_77.value = 9.33
    shipBuilder_vehicleitemparams_77 = importer.save_or_locate(shipBuilder_vehicleitemparams_77)

    shipBuilder_vehicleitemparams_78 = VehicleItemParams()
    shipBuilder_vehicleitemparams_78.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_78.value = 40.0
    shipBuilder_vehicleitemparams_78 = importer.save_or_locate(shipBuilder_vehicleitemparams_78)

    shipBuilder_vehicleitemparams_79 = VehicleItemParams()
    shipBuilder_vehicleitemparams_79.name = u'rollMax'
    shipBuilder_vehicleitemparams_79.value = 90.0
    shipBuilder_vehicleitemparams_79 = importer.save_or_locate(shipBuilder_vehicleitemparams_79)

    shipBuilder_vehicleitemparams_80 = VehicleItemParams()
    shipBuilder_vehicleitemparams_80.name = u'maxThrust'
    shipBuilder_vehicleitemparams_80.value = 250000.0
    shipBuilder_vehicleitemparams_80 = importer.save_or_locate(shipBuilder_vehicleitemparams_80)

    shipBuilder_vehicleitemparams_81 = VehicleItemParams()
    shipBuilder_vehicleitemparams_81.name = u'rollSpeed'
    shipBuilder_vehicleitemparams_81.value = 80.0
    shipBuilder_vehicleitemparams_81 = importer.save_or_locate(shipBuilder_vehicleitemparams_81)

    shipBuilder_vehicleitemparams_82 = VehicleItemParams()
    shipBuilder_vehicleitemparams_82.name = u'rollAcceleration'
    shipBuilder_vehicleitemparams_82.value = 40.0
    shipBuilder_vehicleitemparams_82 = importer.save_or_locate(shipBuilder_vehicleitemparams_82)

    shipBuilder_vehicleitemparams_83 = VehicleItemParams()
    shipBuilder_vehicleitemparams_83.name = u'yawMin'
    shipBuilder_vehicleitemparams_83.value = -90.0
    shipBuilder_vehicleitemparams_83 = importer.save_or_locate(shipBuilder_vehicleitemparams_83)

    shipBuilder_vehicleitemparams_84 = VehicleItemParams()
    shipBuilder_vehicleitemparams_84.name = u'yawMax'
    shipBuilder_vehicleitemparams_84.value = 90.0
    shipBuilder_vehicleitemparams_84 = importer.save_or_locate(shipBuilder_vehicleitemparams_84)

    shipBuilder_vehicleitemparams_85 = VehicleItemParams()
    shipBuilder_vehicleitemparams_85.name = u'rollMin'
    shipBuilder_vehicleitemparams_85.value = 0.0
    shipBuilder_vehicleitemparams_85 = importer.save_or_locate(shipBuilder_vehicleitemparams_85)

    shipBuilder_vehicleitemparams_86 = VehicleItemParams()
    shipBuilder_vehicleitemparams_86.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_86.value = 80.0
    shipBuilder_vehicleitemparams_86 = importer.save_or_locate(shipBuilder_vehicleitemparams_86)

    shipBuilder_vehicleitemparams_87 = VehicleItemParams()
    shipBuilder_vehicleitemparams_87.name = u'acceleration'
    shipBuilder_vehicleitemparams_87.value = 20.0
    shipBuilder_vehicleitemparams_87 = importer.save_or_locate(shipBuilder_vehicleitemparams_87)

    shipBuilder_vehicleitemparams_88 = VehicleItemParams()
    shipBuilder_vehicleitemparams_88.name = u'pitchMax'
    shipBuilder_vehicleitemparams_88.value = 10.0
    shipBuilder_vehicleitemparams_88 = importer.save_or_locate(shipBuilder_vehicleitemparams_88)

    shipBuilder_vehicleitemparams_89 = VehicleItemParams()
    shipBuilder_vehicleitemparams_89.name = u'maxThrust'
    shipBuilder_vehicleitemparams_89.value = 2600000.0
    shipBuilder_vehicleitemparams_89 = importer.save_or_locate(shipBuilder_vehicleitemparams_89)

    shipBuilder_vehicleitemparams_90 = VehicleItemParams()
    shipBuilder_vehicleitemparams_90.name = u'pitchMin'
    shipBuilder_vehicleitemparams_90.value = -10.0
    shipBuilder_vehicleitemparams_90 = importer.save_or_locate(shipBuilder_vehicleitemparams_90)

    shipBuilder_vehicleitemparams_91 = VehicleItemParams()
    shipBuilder_vehicleitemparams_91.name = u'yawMin'
    shipBuilder_vehicleitemparams_91.value = -10.0
    shipBuilder_vehicleitemparams_91 = importer.save_or_locate(shipBuilder_vehicleitemparams_91)

    shipBuilder_vehicleitemparams_92 = VehicleItemParams()
    shipBuilder_vehicleitemparams_92.name = u'yawMax'
    shipBuilder_vehicleitemparams_92.value = 10.0
    shipBuilder_vehicleitemparams_92 = importer.save_or_locate(shipBuilder_vehicleitemparams_92)

    shipBuilder_vehicleitemparams_93 = VehicleItemParams()
    shipBuilder_vehicleitemparams_93.name = u'speed'
    shipBuilder_vehicleitemparams_93.value = 40.0
    shipBuilder_vehicleitemparams_93 = importer.save_or_locate(shipBuilder_vehicleitemparams_93)

    shipBuilder_vehicleitemparams_94 = VehicleItemParams()
    shipBuilder_vehicleitemparams_94.name = u'acceleration'
    shipBuilder_vehicleitemparams_94.value = 20.0
    shipBuilder_vehicleitemparams_94 = importer.save_or_locate(shipBuilder_vehicleitemparams_94)

    shipBuilder_vehicleitemparams_95 = VehicleItemParams()
    shipBuilder_vehicleitemparams_95.name = u'maxThrust'
    shipBuilder_vehicleitemparams_95.value = 2600000.0
    shipBuilder_vehicleitemparams_95 = importer.save_or_locate(shipBuilder_vehicleitemparams_95)

    shipBuilder_vehicleitemparams_96 = VehicleItemParams()
    shipBuilder_vehicleitemparams_96.name = u'speed'
    shipBuilder_vehicleitemparams_96.value = 40.0
    shipBuilder_vehicleitemparams_96 = importer.save_or_locate(shipBuilder_vehicleitemparams_96)

    shipBuilder_vehicleitemparams_97 = VehicleItemParams()
    shipBuilder_vehicleitemparams_97.name = u'Speed'
    shipBuilder_vehicleitemparams_97.value = 80.0
    shipBuilder_vehicleitemparams_97 = importer.save_or_locate(shipBuilder_vehicleitemparams_97)

    shipBuilder_vehicleitemparams_98 = VehicleItemParams()
    shipBuilder_vehicleitemparams_98.name = u'Warhead'
    shipBuilder_vehicleitemparams_98.value = 51.43
    shipBuilder_vehicleitemparams_98 = importer.save_or_locate(shipBuilder_vehicleitemparams_98)

    shipBuilder_vehicleitemparams_99 = VehicleItemParams()
    shipBuilder_vehicleitemparams_99.name = u'Radius'
    shipBuilder_vehicleitemparams_99.value = 66.67
    shipBuilder_vehicleitemparams_99 = importer.save_or_locate(shipBuilder_vehicleitemparams_99)

    shipBuilder_vehicleitemparams_100 = VehicleItemParams()
    shipBuilder_vehicleitemparams_100.name = u'Concuss'
    shipBuilder_vehicleitemparams_100.value = 66.67
    shipBuilder_vehicleitemparams_100 = importer.save_or_locate(shipBuilder_vehicleitemparams_100)

    shipBuilder_vehicleitemparams_101 = VehicleItemParams()
    shipBuilder_vehicleitemparams_101.name = u'pitchMax'
    shipBuilder_vehicleitemparams_101.value = 90.0
    shipBuilder_vehicleitemparams_101 = importer.save_or_locate(shipBuilder_vehicleitemparams_101)

    shipBuilder_vehicleitemparams_102 = VehicleItemParams()
    shipBuilder_vehicleitemparams_102.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_102.value = 40.0
    shipBuilder_vehicleitemparams_102 = importer.save_or_locate(shipBuilder_vehicleitemparams_102)

    shipBuilder_vehicleitemparams_103 = VehicleItemParams()
    shipBuilder_vehicleitemparams_103.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_103.value = 40.0
    shipBuilder_vehicleitemparams_103 = importer.save_or_locate(shipBuilder_vehicleitemparams_103)

    shipBuilder_vehicleitemparams_104 = VehicleItemParams()
    shipBuilder_vehicleitemparams_104.name = u'maxThrust'
    shipBuilder_vehicleitemparams_104.value = 250000.0
    shipBuilder_vehicleitemparams_104 = importer.save_or_locate(shipBuilder_vehicleitemparams_104)

    shipBuilder_vehicleitemparams_105 = VehicleItemParams()
    shipBuilder_vehicleitemparams_105.name = u'yawMax'
    shipBuilder_vehicleitemparams_105.value = 0.0
    shipBuilder_vehicleitemparams_105 = importer.save_or_locate(shipBuilder_vehicleitemparams_105)

    shipBuilder_vehicleitemparams_106 = VehicleItemParams()
    shipBuilder_vehicleitemparams_106.name = u'pitchMin'
    shipBuilder_vehicleitemparams_106.value = -90.0
    shipBuilder_vehicleitemparams_106 = importer.save_or_locate(shipBuilder_vehicleitemparams_106)

    shipBuilder_vehicleitemparams_107 = VehicleItemParams()
    shipBuilder_vehicleitemparams_107.name = u'yawMin'
    shipBuilder_vehicleitemparams_107.value = -90.0
    shipBuilder_vehicleitemparams_107 = importer.save_or_locate(shipBuilder_vehicleitemparams_107)

    shipBuilder_vehicleitemparams_108 = VehicleItemParams()
    shipBuilder_vehicleitemparams_108.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_108.value = 80.0
    shipBuilder_vehicleitemparams_108 = importer.save_or_locate(shipBuilder_vehicleitemparams_108)

    shipBuilder_vehicleitemparams_109 = VehicleItemParams()
    shipBuilder_vehicleitemparams_109.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_109.value = 80.0
    shipBuilder_vehicleitemparams_109 = importer.save_or_locate(shipBuilder_vehicleitemparams_109)

    shipBuilder_vehicleitemparams_110 = VehicleItemParams()
    shipBuilder_vehicleitemparams_110.name = u'RoF'
    shipBuilder_vehicleitemparams_110.value = 5.0
    shipBuilder_vehicleitemparams_110 = importer.save_or_locate(shipBuilder_vehicleitemparams_110)

    shipBuilder_vehicleitemparams_111 = VehicleItemParams()
    shipBuilder_vehicleitemparams_111.name = u'Range'
    shipBuilder_vehicleitemparams_111.value = 30.0
    shipBuilder_vehicleitemparams_111 = importer.save_or_locate(shipBuilder_vehicleitemparams_111)

    shipBuilder_vehicleitemparams_112 = VehicleItemParams()
    shipBuilder_vehicleitemparams_112.name = u'Damage'
    shipBuilder_vehicleitemparams_112.value = 20.0
    shipBuilder_vehicleitemparams_112 = importer.save_or_locate(shipBuilder_vehicleitemparams_112)

    shipBuilder_vehicleitemparams_113 = VehicleItemParams()
    shipBuilder_vehicleitemparams_113.name = u'Power'
    shipBuilder_vehicleitemparams_113.value = 49.5
    shipBuilder_vehicleitemparams_113 = importer.save_or_locate(shipBuilder_vehicleitemparams_113)

    shipBuilder_vehicleitemparams_114 = VehicleItemParams()
    shipBuilder_vehicleitemparams_114.name = u'RoF'
    shipBuilder_vehicleitemparams_114.value = 6.67
    shipBuilder_vehicleitemparams_114 = importer.save_or_locate(shipBuilder_vehicleitemparams_114)

    shipBuilder_vehicleitemparams_115 = VehicleItemParams()
    shipBuilder_vehicleitemparams_115.name = u'Range'
    shipBuilder_vehicleitemparams_115.value = 90.0
    shipBuilder_vehicleitemparams_115 = importer.save_or_locate(shipBuilder_vehicleitemparams_115)

    shipBuilder_vehicleitemparams_116 = VehicleItemParams()
    shipBuilder_vehicleitemparams_116.name = u'Damage'
    shipBuilder_vehicleitemparams_116.value = 10.0
    shipBuilder_vehicleitemparams_116 = importer.save_or_locate(shipBuilder_vehicleitemparams_116)

    shipBuilder_vehicleitemparams_117 = VehicleItemParams()
    shipBuilder_vehicleitemparams_117.name = u'Power'
    shipBuilder_vehicleitemparams_117.value = 4.0
    shipBuilder_vehicleitemparams_117 = importer.save_or_locate(shipBuilder_vehicleitemparams_117)

    shipBuilder_vehicleitemparams_118 = VehicleItemParams()
    shipBuilder_vehicleitemparams_118.name = u'RoF'
    shipBuilder_vehicleitemparams_118.value = 26.5
    shipBuilder_vehicleitemparams_118 = importer.save_or_locate(shipBuilder_vehicleitemparams_118)

    shipBuilder_vehicleitemparams_119 = VehicleItemParams()
    shipBuilder_vehicleitemparams_119.name = u'Range'
    shipBuilder_vehicleitemparams_119.value = 60.0
    shipBuilder_vehicleitemparams_119 = importer.save_or_locate(shipBuilder_vehicleitemparams_119)

    shipBuilder_vehicleitemparams_120 = VehicleItemParams()
    shipBuilder_vehicleitemparams_120.name = u'Damage'
    shipBuilder_vehicleitemparams_120.value = 2.5
    shipBuilder_vehicleitemparams_120 = importer.save_or_locate(shipBuilder_vehicleitemparams_120)

    shipBuilder_vehicleitemparams_121 = VehicleItemParams()
    shipBuilder_vehicleitemparams_121.name = u'Power'
    shipBuilder_vehicleitemparams_121.value = 1.0
    shipBuilder_vehicleitemparams_121 = importer.save_or_locate(shipBuilder_vehicleitemparams_121)

    shipBuilder_vehicleitemparams_122 = VehicleItemParams()
    shipBuilder_vehicleitemparams_122.name = u'RoF'
    shipBuilder_vehicleitemparams_122.value = 20.0
    shipBuilder_vehicleitemparams_122 = importer.save_or_locate(shipBuilder_vehicleitemparams_122)

    shipBuilder_vehicleitemparams_123 = VehicleItemParams()
    shipBuilder_vehicleitemparams_123.name = u'Range'
    shipBuilder_vehicleitemparams_123.value = 90.0
    shipBuilder_vehicleitemparams_123 = importer.save_or_locate(shipBuilder_vehicleitemparams_123)

    shipBuilder_vehicleitemparams_124 = VehicleItemParams()
    shipBuilder_vehicleitemparams_124.name = u'Damage'
    shipBuilder_vehicleitemparams_124.value = 3.5
    shipBuilder_vehicleitemparams_124 = importer.save_or_locate(shipBuilder_vehicleitemparams_124)

    shipBuilder_vehicleitemparams_125 = VehicleItemParams()
    shipBuilder_vehicleitemparams_125.name = u'Power'
    shipBuilder_vehicleitemparams_125.value = 27.3
    shipBuilder_vehicleitemparams_125 = importer.save_or_locate(shipBuilder_vehicleitemparams_125)

    shipBuilder_vehicleitemparams_126 = VehicleItemParams()
    shipBuilder_vehicleitemparams_126.name = u'RoF'
    shipBuilder_vehicleitemparams_126.value = 20.0
    shipBuilder_vehicleitemparams_126 = importer.save_or_locate(shipBuilder_vehicleitemparams_126)

    shipBuilder_vehicleitemparams_127 = VehicleItemParams()
    shipBuilder_vehicleitemparams_127.name = u'Range'
    shipBuilder_vehicleitemparams_127.value = 90.0
    shipBuilder_vehicleitemparams_127 = importer.save_or_locate(shipBuilder_vehicleitemparams_127)

    shipBuilder_vehicleitemparams_128 = VehicleItemParams()
    shipBuilder_vehicleitemparams_128.name = u'Damage'
    shipBuilder_vehicleitemparams_128.value = 4.5
    shipBuilder_vehicleitemparams_128 = importer.save_or_locate(shipBuilder_vehicleitemparams_128)

    shipBuilder_vehicleitemparams_129 = VehicleItemParams()
    shipBuilder_vehicleitemparams_129.name = u'Power'
    shipBuilder_vehicleitemparams_129.value = 35.1
    shipBuilder_vehicleitemparams_129 = importer.save_or_locate(shipBuilder_vehicleitemparams_129)

    shipBuilder_vehicleitemparams_130 = VehicleItemParams()
    shipBuilder_vehicleitemparams_130.name = u'pitchMax'
    shipBuilder_vehicleitemparams_130.value = 90.0
    shipBuilder_vehicleitemparams_130 = importer.save_or_locate(shipBuilder_vehicleitemparams_130)

    shipBuilder_vehicleitemparams_131 = VehicleItemParams()
    shipBuilder_vehicleitemparams_131.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_131.value = 40.0
    shipBuilder_vehicleitemparams_131 = importer.save_or_locate(shipBuilder_vehicleitemparams_131)

    shipBuilder_vehicleitemparams_132 = VehicleItemParams()
    shipBuilder_vehicleitemparams_132.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_132.value = 40.0
    shipBuilder_vehicleitemparams_132 = importer.save_or_locate(shipBuilder_vehicleitemparams_132)

    shipBuilder_vehicleitemparams_133 = VehicleItemParams()
    shipBuilder_vehicleitemparams_133.name = u'maxThrust'
    shipBuilder_vehicleitemparams_133.value = 350000.0
    shipBuilder_vehicleitemparams_133 = importer.save_or_locate(shipBuilder_vehicleitemparams_133)

    shipBuilder_vehicleitemparams_134 = VehicleItemParams()
    shipBuilder_vehicleitemparams_134.name = u'yawMax'
    shipBuilder_vehicleitemparams_134.value = 90.0
    shipBuilder_vehicleitemparams_134 = importer.save_or_locate(shipBuilder_vehicleitemparams_134)

    shipBuilder_vehicleitemparams_135 = VehicleItemParams()
    shipBuilder_vehicleitemparams_135.name = u'pitchMin'
    shipBuilder_vehicleitemparams_135.value = -90.0
    shipBuilder_vehicleitemparams_135 = importer.save_or_locate(shipBuilder_vehicleitemparams_135)

    shipBuilder_vehicleitemparams_136 = VehicleItemParams()
    shipBuilder_vehicleitemparams_136.name = u'yawMin'
    shipBuilder_vehicleitemparams_136.value = 0.0
    shipBuilder_vehicleitemparams_136 = importer.save_or_locate(shipBuilder_vehicleitemparams_136)

    shipBuilder_vehicleitemparams_137 = VehicleItemParams()
    shipBuilder_vehicleitemparams_137.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_137.value = 80.0
    shipBuilder_vehicleitemparams_137 = importer.save_or_locate(shipBuilder_vehicleitemparams_137)

    shipBuilder_vehicleitemparams_138 = VehicleItemParams()
    shipBuilder_vehicleitemparams_138.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_138.value = 80.0
    shipBuilder_vehicleitemparams_138 = importer.save_or_locate(shipBuilder_vehicleitemparams_138)

    shipBuilder_vehicleitemparams_139 = VehicleItemParams()
    shipBuilder_vehicleitemparams_139.name = u'RoF'
    shipBuilder_vehicleitemparams_139.value = 20.0
    shipBuilder_vehicleitemparams_139 = importer.save_or_locate(shipBuilder_vehicleitemparams_139)

    shipBuilder_vehicleitemparams_140 = VehicleItemParams()
    shipBuilder_vehicleitemparams_140.name = u'Range'
    shipBuilder_vehicleitemparams_140.value = 90.0
    shipBuilder_vehicleitemparams_140 = importer.save_or_locate(shipBuilder_vehicleitemparams_140)

    shipBuilder_vehicleitemparams_141 = VehicleItemParams()
    shipBuilder_vehicleitemparams_141.name = u'Damage'
    shipBuilder_vehicleitemparams_141.value = 5.5
    shipBuilder_vehicleitemparams_141 = importer.save_or_locate(shipBuilder_vehicleitemparams_141)

    shipBuilder_vehicleitemparams_142 = VehicleItemParams()
    shipBuilder_vehicleitemparams_142.name = u'Power'
    shipBuilder_vehicleitemparams_142.value = 46.8
    shipBuilder_vehicleitemparams_142 = importer.save_or_locate(shipBuilder_vehicleitemparams_142)

    shipBuilder_vehicleitemparams_143 = VehicleItemParams()
    shipBuilder_vehicleitemparams_143.name = u'acceleration'
    shipBuilder_vehicleitemparams_143.value = 20.0
    shipBuilder_vehicleitemparams_143 = importer.save_or_locate(shipBuilder_vehicleitemparams_143)

    shipBuilder_vehicleitemparams_144 = VehicleItemParams()
    shipBuilder_vehicleitemparams_144.name = u'pitchMax'
    shipBuilder_vehicleitemparams_144.value = 10.0
    shipBuilder_vehicleitemparams_144 = importer.save_or_locate(shipBuilder_vehicleitemparams_144)

    shipBuilder_vehicleitemparams_145 = VehicleItemParams()
    shipBuilder_vehicleitemparams_145.name = u'maxThrust'
    shipBuilder_vehicleitemparams_145.value = 2600000.0
    shipBuilder_vehicleitemparams_145 = importer.save_or_locate(shipBuilder_vehicleitemparams_145)

    shipBuilder_vehicleitemparams_146 = VehicleItemParams()
    shipBuilder_vehicleitemparams_146.name = u'pitchMin'
    shipBuilder_vehicleitemparams_146.value = -10.0
    shipBuilder_vehicleitemparams_146 = importer.save_or_locate(shipBuilder_vehicleitemparams_146)

    shipBuilder_vehicleitemparams_147 = VehicleItemParams()
    shipBuilder_vehicleitemparams_147.name = u'yawMin'
    shipBuilder_vehicleitemparams_147.value = -10.0
    shipBuilder_vehicleitemparams_147 = importer.save_or_locate(shipBuilder_vehicleitemparams_147)

    shipBuilder_vehicleitemparams_148 = VehicleItemParams()
    shipBuilder_vehicleitemparams_148.name = u'yawMax'
    shipBuilder_vehicleitemparams_148.value = 10.0
    shipBuilder_vehicleitemparams_148 = importer.save_or_locate(shipBuilder_vehicleitemparams_148)

    shipBuilder_vehicleitemparams_149 = VehicleItemParams()
    shipBuilder_vehicleitemparams_149.name = u'speed'
    shipBuilder_vehicleitemparams_149.value = 40.0
    shipBuilder_vehicleitemparams_149 = importer.save_or_locate(shipBuilder_vehicleitemparams_149)

    shipBuilder_vehicleitemparams_150 = VehicleItemParams()
    shipBuilder_vehicleitemparams_150.name = u'acceleration'
    shipBuilder_vehicleitemparams_150.value = 20.0
    shipBuilder_vehicleitemparams_150 = importer.save_or_locate(shipBuilder_vehicleitemparams_150)

    shipBuilder_vehicleitemparams_151 = VehicleItemParams()
    shipBuilder_vehicleitemparams_151.name = u'maxThrust'
    shipBuilder_vehicleitemparams_151.value = 2600000.0
    shipBuilder_vehicleitemparams_151 = importer.save_or_locate(shipBuilder_vehicleitemparams_151)

    shipBuilder_vehicleitemparams_152 = VehicleItemParams()
    shipBuilder_vehicleitemparams_152.name = u'speed'
    shipBuilder_vehicleitemparams_152.value = 40.0
    shipBuilder_vehicleitemparams_152 = importer.save_or_locate(shipBuilder_vehicleitemparams_152)

    shipBuilder_vehicleitemparams_153 = VehicleItemParams()
    shipBuilder_vehicleitemparams_153.name = u'Speed'
    shipBuilder_vehicleitemparams_153.value = 74.5
    shipBuilder_vehicleitemparams_153 = importer.save_or_locate(shipBuilder_vehicleitemparams_153)

    shipBuilder_vehicleitemparams_154 = VehicleItemParams()
    shipBuilder_vehicleitemparams_154.name = u'Warhead'
    shipBuilder_vehicleitemparams_154.value = 62.86
    shipBuilder_vehicleitemparams_154 = importer.save_or_locate(shipBuilder_vehicleitemparams_154)

    shipBuilder_vehicleitemparams_155 = VehicleItemParams()
    shipBuilder_vehicleitemparams_155.name = u'Radius'
    shipBuilder_vehicleitemparams_155.value = 80.0
    shipBuilder_vehicleitemparams_155 = importer.save_or_locate(shipBuilder_vehicleitemparams_155)

    shipBuilder_vehicleitemparams_156 = VehicleItemParams()
    shipBuilder_vehicleitemparams_156.name = u'Concuss'
    shipBuilder_vehicleitemparams_156.value = 93.33
    shipBuilder_vehicleitemparams_156 = importer.save_or_locate(shipBuilder_vehicleitemparams_156)

    shipBuilder_vehicleitemparams_157 = VehicleItemParams()
    shipBuilder_vehicleitemparams_157.name = u'acceleration'
    shipBuilder_vehicleitemparams_157.value = 20.0
    shipBuilder_vehicleitemparams_157 = importer.save_or_locate(shipBuilder_vehicleitemparams_157)

    shipBuilder_vehicleitemparams_158 = VehicleItemParams()
    shipBuilder_vehicleitemparams_158.name = u'pitchMax'
    shipBuilder_vehicleitemparams_158.value = 10.0
    shipBuilder_vehicleitemparams_158 = importer.save_or_locate(shipBuilder_vehicleitemparams_158)

    shipBuilder_vehicleitemparams_159 = VehicleItemParams()
    shipBuilder_vehicleitemparams_159.name = u'maxThrust'
    shipBuilder_vehicleitemparams_159.value = 2600000.0
    shipBuilder_vehicleitemparams_159 = importer.save_or_locate(shipBuilder_vehicleitemparams_159)

    shipBuilder_vehicleitemparams_160 = VehicleItemParams()
    shipBuilder_vehicleitemparams_160.name = u'pitchMin'
    shipBuilder_vehicleitemparams_160.value = -10.0
    shipBuilder_vehicleitemparams_160 = importer.save_or_locate(shipBuilder_vehicleitemparams_160)

    shipBuilder_vehicleitemparams_161 = VehicleItemParams()
    shipBuilder_vehicleitemparams_161.name = u'yawMin'
    shipBuilder_vehicleitemparams_161.value = -10.0
    shipBuilder_vehicleitemparams_161 = importer.save_or_locate(shipBuilder_vehicleitemparams_161)

    shipBuilder_vehicleitemparams_162 = VehicleItemParams()
    shipBuilder_vehicleitemparams_162.name = u'yawMax'
    shipBuilder_vehicleitemparams_162.value = 10.0
    shipBuilder_vehicleitemparams_162 = importer.save_or_locate(shipBuilder_vehicleitemparams_162)

    shipBuilder_vehicleitemparams_163 = VehicleItemParams()
    shipBuilder_vehicleitemparams_163.name = u'speed'
    shipBuilder_vehicleitemparams_163.value = 40.0
    shipBuilder_vehicleitemparams_163 = importer.save_or_locate(shipBuilder_vehicleitemparams_163)

    shipBuilder_vehicleitemparams_164 = VehicleItemParams()
    shipBuilder_vehicleitemparams_164.name = u'acceleration'
    shipBuilder_vehicleitemparams_164.value = 20.0
    shipBuilder_vehicleitemparams_164 = importer.save_or_locate(shipBuilder_vehicleitemparams_164)

    shipBuilder_vehicleitemparams_165 = VehicleItemParams()
    shipBuilder_vehicleitemparams_165.name = u'pitchMax'
    shipBuilder_vehicleitemparams_165.value = 10.0
    shipBuilder_vehicleitemparams_165 = importer.save_or_locate(shipBuilder_vehicleitemparams_165)

    shipBuilder_vehicleitemparams_166 = VehicleItemParams()
    shipBuilder_vehicleitemparams_166.name = u'maxThrust'
    shipBuilder_vehicleitemparams_166.value = 2600000.0
    shipBuilder_vehicleitemparams_166 = importer.save_or_locate(shipBuilder_vehicleitemparams_166)

    shipBuilder_vehicleitemparams_167 = VehicleItemParams()
    shipBuilder_vehicleitemparams_167.name = u'pitchMin'
    shipBuilder_vehicleitemparams_167.value = -10.0
    shipBuilder_vehicleitemparams_167 = importer.save_or_locate(shipBuilder_vehicleitemparams_167)

    shipBuilder_vehicleitemparams_168 = VehicleItemParams()
    shipBuilder_vehicleitemparams_168.name = u'yawMin'
    shipBuilder_vehicleitemparams_168.value = -10.0
    shipBuilder_vehicleitemparams_168 = importer.save_or_locate(shipBuilder_vehicleitemparams_168)

    shipBuilder_vehicleitemparams_169 = VehicleItemParams()
    shipBuilder_vehicleitemparams_169.name = u'yawMax'
    shipBuilder_vehicleitemparams_169.value = 10.0
    shipBuilder_vehicleitemparams_169 = importer.save_or_locate(shipBuilder_vehicleitemparams_169)

    shipBuilder_vehicleitemparams_170 = VehicleItemParams()
    shipBuilder_vehicleitemparams_170.name = u'speed'
    shipBuilder_vehicleitemparams_170.value = 40.0
    shipBuilder_vehicleitemparams_170 = importer.save_or_locate(shipBuilder_vehicleitemparams_170)

    shipBuilder_vehicleitemparams_171 = VehicleItemParams()
    shipBuilder_vehicleitemparams_171.name = u'RoF'
    shipBuilder_vehicleitemparams_171.value = 60.0
    shipBuilder_vehicleitemparams_171 = importer.save_or_locate(shipBuilder_vehicleitemparams_171)

    shipBuilder_vehicleitemparams_172 = VehicleItemParams()
    shipBuilder_vehicleitemparams_172.name = u'Range'
    shipBuilder_vehicleitemparams_172.value = 60.0
    shipBuilder_vehicleitemparams_172 = importer.save_or_locate(shipBuilder_vehicleitemparams_172)

    shipBuilder_vehicleitemparams_173 = VehicleItemParams()
    shipBuilder_vehicleitemparams_173.name = u'Damage'
    shipBuilder_vehicleitemparams_173.value = 1.25
    shipBuilder_vehicleitemparams_173 = importer.save_or_locate(shipBuilder_vehicleitemparams_173)

    shipBuilder_vehicleitemparams_174 = VehicleItemParams()
    shipBuilder_vehicleitemparams_174.name = u'Power'
    shipBuilder_vehicleitemparams_174.value = 32.4
    shipBuilder_vehicleitemparams_174 = importer.save_or_locate(shipBuilder_vehicleitemparams_174)

    shipBuilder_vehicleitemparams_175 = VehicleItemParams()
    shipBuilder_vehicleitemparams_175.name = u'displayRadius'
    shipBuilder_vehicleitemparams_175.value = -1.0
    shipBuilder_vehicleitemparams_175 = importer.save_or_locate(shipBuilder_vehicleitemparams_175)

    shipBuilder_vehicleitemparams_176 = VehicleItemParams()
    shipBuilder_vehicleitemparams_176.name = u'isSphere'
    shipBuilder_vehicleitemparams_176.value = 1.0
    shipBuilder_vehicleitemparams_176 = importer.save_or_locate(shipBuilder_vehicleitemparams_176)

    shipBuilder_vehicleitemparams_177 = VehicleItemParams()
    shipBuilder_vehicleitemparams_177.name = u'numTargetsAllowed'
    shipBuilder_vehicleitemparams_177.value = 2.0
    shipBuilder_vehicleitemparams_177 = importer.save_or_locate(shipBuilder_vehicleitemparams_177)

    shipBuilder_vehicleitemparams_178 = VehicleItemParams()
    shipBuilder_vehicleitemparams_178.name = u'acceleration'
    shipBuilder_vehicleitemparams_178.value = 40.0
    shipBuilder_vehicleitemparams_178 = importer.save_or_locate(shipBuilder_vehicleitemparams_178)

    shipBuilder_vehicleitemparams_179 = VehicleItemParams()
    shipBuilder_vehicleitemparams_179.name = u'maxThrust'
    shipBuilder_vehicleitemparams_179.value = 300000.0
    shipBuilder_vehicleitemparams_179 = importer.save_or_locate(shipBuilder_vehicleitemparams_179)

    shipBuilder_vehicleitemparams_180 = VehicleItemParams()
    shipBuilder_vehicleitemparams_180.name = u'speed'
    shipBuilder_vehicleitemparams_180.value = 80.0
    shipBuilder_vehicleitemparams_180 = importer.save_or_locate(shipBuilder_vehicleitemparams_180)

    shipBuilder_vehicleitemparams_181 = VehicleItemParams()
    shipBuilder_vehicleitemparams_181.name = u'pitchMin'
    shipBuilder_vehicleitemparams_181.value = -180.0
    shipBuilder_vehicleitemparams_181 = importer.save_or_locate(shipBuilder_vehicleitemparams_181)

    shipBuilder_vehicleitemparams_182 = VehicleItemParams()
    shipBuilder_vehicleitemparams_182.name = u'pitchMax'
    shipBuilder_vehicleitemparams_182.value = 180.0
    shipBuilder_vehicleitemparams_182 = importer.save_or_locate(shipBuilder_vehicleitemparams_182)

    shipBuilder_vehicleitemparams_183 = VehicleItemParams()
    shipBuilder_vehicleitemparams_183.name = u'acceleration'
    shipBuilder_vehicleitemparams_183.value = 20.0
    shipBuilder_vehicleitemparams_183 = importer.save_or_locate(shipBuilder_vehicleitemparams_183)

    shipBuilder_vehicleitemparams_184 = VehicleItemParams()
    shipBuilder_vehicleitemparams_184.name = u'pitchMax'
    shipBuilder_vehicleitemparams_184.value = 10.0
    shipBuilder_vehicleitemparams_184 = importer.save_or_locate(shipBuilder_vehicleitemparams_184)

    shipBuilder_vehicleitemparams_185 = VehicleItemParams()
    shipBuilder_vehicleitemparams_185.name = u'maxThrust'
    shipBuilder_vehicleitemparams_185.value = 2600000.0
    shipBuilder_vehicleitemparams_185 = importer.save_or_locate(shipBuilder_vehicleitemparams_185)

    shipBuilder_vehicleitemparams_186 = VehicleItemParams()
    shipBuilder_vehicleitemparams_186.name = u'pitchMin'
    shipBuilder_vehicleitemparams_186.value = -10.0
    shipBuilder_vehicleitemparams_186 = importer.save_or_locate(shipBuilder_vehicleitemparams_186)

    shipBuilder_vehicleitemparams_187 = VehicleItemParams()
    shipBuilder_vehicleitemparams_187.name = u'yawMin'
    shipBuilder_vehicleitemparams_187.value = -10.0
    shipBuilder_vehicleitemparams_187 = importer.save_or_locate(shipBuilder_vehicleitemparams_187)

    shipBuilder_vehicleitemparams_188 = VehicleItemParams()
    shipBuilder_vehicleitemparams_188.name = u'yawMax'
    shipBuilder_vehicleitemparams_188.value = 10.0
    shipBuilder_vehicleitemparams_188 = importer.save_or_locate(shipBuilder_vehicleitemparams_188)

    shipBuilder_vehicleitemparams_189 = VehicleItemParams()
    shipBuilder_vehicleitemparams_189.name = u'speed'
    shipBuilder_vehicleitemparams_189.value = 40.0
    shipBuilder_vehicleitemparams_189 = importer.save_or_locate(shipBuilder_vehicleitemparams_189)

    shipBuilder_vehicleitemparams_190 = VehicleItemParams()
    shipBuilder_vehicleitemparams_190.name = u'pitchMax'
    shipBuilder_vehicleitemparams_190.value = 90.0
    shipBuilder_vehicleitemparams_190 = importer.save_or_locate(shipBuilder_vehicleitemparams_190)

    shipBuilder_vehicleitemparams_191 = VehicleItemParams()
    shipBuilder_vehicleitemparams_191.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_191.value = 40.0
    shipBuilder_vehicleitemparams_191 = importer.save_or_locate(shipBuilder_vehicleitemparams_191)

    shipBuilder_vehicleitemparams_192 = VehicleItemParams()
    shipBuilder_vehicleitemparams_192.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_192.value = 40.0
    shipBuilder_vehicleitemparams_192 = importer.save_or_locate(shipBuilder_vehicleitemparams_192)

    shipBuilder_vehicleitemparams_193 = VehicleItemParams()
    shipBuilder_vehicleitemparams_193.name = u'maxThrust'
    shipBuilder_vehicleitemparams_193.value = 250000.0
    shipBuilder_vehicleitemparams_193 = importer.save_or_locate(shipBuilder_vehicleitemparams_193)

    shipBuilder_vehicleitemparams_194 = VehicleItemParams()
    shipBuilder_vehicleitemparams_194.name = u'yawMax'
    shipBuilder_vehicleitemparams_194.value = 0.0
    shipBuilder_vehicleitemparams_194 = importer.save_or_locate(shipBuilder_vehicleitemparams_194)

    shipBuilder_vehicleitemparams_195 = VehicleItemParams()
    shipBuilder_vehicleitemparams_195.name = u'pitchMin'
    shipBuilder_vehicleitemparams_195.value = -90.0
    shipBuilder_vehicleitemparams_195 = importer.save_or_locate(shipBuilder_vehicleitemparams_195)

    shipBuilder_vehicleitemparams_196 = VehicleItemParams()
    shipBuilder_vehicleitemparams_196.name = u'yawMin'
    shipBuilder_vehicleitemparams_196.value = -90.0
    shipBuilder_vehicleitemparams_196 = importer.save_or_locate(shipBuilder_vehicleitemparams_196)

    shipBuilder_vehicleitemparams_197 = VehicleItemParams()
    shipBuilder_vehicleitemparams_197.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_197.value = 80.0
    shipBuilder_vehicleitemparams_197 = importer.save_or_locate(shipBuilder_vehicleitemparams_197)

    shipBuilder_vehicleitemparams_198 = VehicleItemParams()
    shipBuilder_vehicleitemparams_198.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_198.value = 80.0
    shipBuilder_vehicleitemparams_198 = importer.save_or_locate(shipBuilder_vehicleitemparams_198)

    shipBuilder_vehicleitemparams_199 = VehicleItemParams()
    shipBuilder_vehicleitemparams_199.name = u'RoF'
    shipBuilder_vehicleitemparams_199.value = 26.7
    shipBuilder_vehicleitemparams_199 = importer.save_or_locate(shipBuilder_vehicleitemparams_199)

    shipBuilder_vehicleitemparams_200 = VehicleItemParams()
    shipBuilder_vehicleitemparams_200.name = u'Range'
    shipBuilder_vehicleitemparams_200.value = 60.0
    shipBuilder_vehicleitemparams_200 = importer.save_or_locate(shipBuilder_vehicleitemparams_200)

    shipBuilder_vehicleitemparams_201 = VehicleItemParams()
    shipBuilder_vehicleitemparams_201.name = u'Damage'
    shipBuilder_vehicleitemparams_201.value = 2.25
    shipBuilder_vehicleitemparams_201 = importer.save_or_locate(shipBuilder_vehicleitemparams_201)

    shipBuilder_vehicleitemparams_202 = VehicleItemParams()
    shipBuilder_vehicleitemparams_202.name = u'Power'
    shipBuilder_vehicleitemparams_202.value = 1.0
    shipBuilder_vehicleitemparams_202 = importer.save_or_locate(shipBuilder_vehicleitemparams_202)

    shipBuilder_vehicleitemparams_203 = VehicleItemParams()
    shipBuilder_vehicleitemparams_203.name = u'acceleration'
    shipBuilder_vehicleitemparams_203.value = 40.0
    shipBuilder_vehicleitemparams_203 = importer.save_or_locate(shipBuilder_vehicleitemparams_203)

    shipBuilder_vehicleitemparams_204 = VehicleItemParams()
    shipBuilder_vehicleitemparams_204.name = u'maxThrust'
    shipBuilder_vehicleitemparams_204.value = 300000.0
    shipBuilder_vehicleitemparams_204 = importer.save_or_locate(shipBuilder_vehicleitemparams_204)

    shipBuilder_vehicleitemparams_205 = VehicleItemParams()
    shipBuilder_vehicleitemparams_205.name = u'speed'
    shipBuilder_vehicleitemparams_205.value = 80.0
    shipBuilder_vehicleitemparams_205 = importer.save_or_locate(shipBuilder_vehicleitemparams_205)

    shipBuilder_vehicleitemparams_206 = VehicleItemParams()
    shipBuilder_vehicleitemparams_206.name = u'pitchMin'
    shipBuilder_vehicleitemparams_206.value = 0.0
    shipBuilder_vehicleitemparams_206 = importer.save_or_locate(shipBuilder_vehicleitemparams_206)

    shipBuilder_vehicleitemparams_207 = VehicleItemParams()
    shipBuilder_vehicleitemparams_207.name = u'pitchMax'
    shipBuilder_vehicleitemparams_207.value = 180.0
    shipBuilder_vehicleitemparams_207 = importer.save_or_locate(shipBuilder_vehicleitemparams_207)

    shipBuilder_vehicleitemparams_208 = VehicleItemParams()
    shipBuilder_vehicleitemparams_208.name = u'acceleration'
    shipBuilder_vehicleitemparams_208.value = 20.0
    shipBuilder_vehicleitemparams_208 = importer.save_or_locate(shipBuilder_vehicleitemparams_208)

    shipBuilder_vehicleitemparams_209 = VehicleItemParams()
    shipBuilder_vehicleitemparams_209.name = u'pitchMax'
    shipBuilder_vehicleitemparams_209.value = 10.0
    shipBuilder_vehicleitemparams_209 = importer.save_or_locate(shipBuilder_vehicleitemparams_209)

    shipBuilder_vehicleitemparams_210 = VehicleItemParams()
    shipBuilder_vehicleitemparams_210.name = u'maxThrust'
    shipBuilder_vehicleitemparams_210.value = 2600000.0
    shipBuilder_vehicleitemparams_210 = importer.save_or_locate(shipBuilder_vehicleitemparams_210)

    shipBuilder_vehicleitemparams_211 = VehicleItemParams()
    shipBuilder_vehicleitemparams_211.name = u'pitchMin'
    shipBuilder_vehicleitemparams_211.value = -10.0
    shipBuilder_vehicleitemparams_211 = importer.save_or_locate(shipBuilder_vehicleitemparams_211)

    shipBuilder_vehicleitemparams_212 = VehicleItemParams()
    shipBuilder_vehicleitemparams_212.name = u'yawMin'
    shipBuilder_vehicleitemparams_212.value = -10.0
    shipBuilder_vehicleitemparams_212 = importer.save_or_locate(shipBuilder_vehicleitemparams_212)

    shipBuilder_vehicleitemparams_213 = VehicleItemParams()
    shipBuilder_vehicleitemparams_213.name = u'yawMax'
    shipBuilder_vehicleitemparams_213.value = 10.0
    shipBuilder_vehicleitemparams_213 = importer.save_or_locate(shipBuilder_vehicleitemparams_213)

    shipBuilder_vehicleitemparams_214 = VehicleItemParams()
    shipBuilder_vehicleitemparams_214.name = u'speed'
    shipBuilder_vehicleitemparams_214.value = 40.0
    shipBuilder_vehicleitemparams_214 = importer.save_or_locate(shipBuilder_vehicleitemparams_214)

    shipBuilder_vehicleitemparams_215 = VehicleItemParams()
    shipBuilder_vehicleitemparams_215.name = u'acceleration'
    shipBuilder_vehicleitemparams_215.value = 20.0
    shipBuilder_vehicleitemparams_215 = importer.save_or_locate(shipBuilder_vehicleitemparams_215)

    shipBuilder_vehicleitemparams_216 = VehicleItemParams()
    shipBuilder_vehicleitemparams_216.name = u'maxThrust'
    shipBuilder_vehicleitemparams_216.value = 2600000.0
    shipBuilder_vehicleitemparams_216 = importer.save_or_locate(shipBuilder_vehicleitemparams_216)

    shipBuilder_vehicleitemparams_217 = VehicleItemParams()
    shipBuilder_vehicleitemparams_217.name = u'speed'
    shipBuilder_vehicleitemparams_217.value = 40.0
    shipBuilder_vehicleitemparams_217 = importer.save_or_locate(shipBuilder_vehicleitemparams_217)

    shipBuilder_vehicleitemparams_218 = VehicleItemParams()
    shipBuilder_vehicleitemparams_218.name = u'gridSize'
    shipBuilder_vehicleitemparams_218.value = 5.0
    shipBuilder_vehicleitemparams_218 = importer.save_or_locate(shipBuilder_vehicleitemparams_218)

    shipBuilder_vehicleitemparams_219 = VehicleItemParams()
    shipBuilder_vehicleitemparams_219.name = u'radius'
    shipBuilder_vehicleitemparams_219.value = 10000.0
    shipBuilder_vehicleitemparams_219 = importer.save_or_locate(shipBuilder_vehicleitemparams_219)

    shipBuilder_vehicleitemparams_220 = VehicleItemParams()
    shipBuilder_vehicleitemparams_220.name = u'identifyTime'
    shipBuilder_vehicleitemparams_220.value = 0.5
    shipBuilder_vehicleitemparams_220 = importer.save_or_locate(shipBuilder_vehicleitemparams_220)

    shipBuilder_vehicleitemparams_221 = VehicleItemParams()
    shipBuilder_vehicleitemparams_221.name = u'radarTime'
    shipBuilder_vehicleitemparams_221.value = 4.0
    shipBuilder_vehicleitemparams_221 = importer.save_or_locate(shipBuilder_vehicleitemparams_221)

    shipBuilder_vehicleitemparams_222 = VehicleItemParams()
    shipBuilder_vehicleitemparams_222.name = u'radarType'
    shipBuilder_vehicleitemparams_222.value = 0.0
    shipBuilder_vehicleitemparams_222 = importer.save_or_locate(shipBuilder_vehicleitemparams_222)

    shipBuilder_vehicleitemparams_223 = VehicleItemParams()
    shipBuilder_vehicleitemparams_223.name = u'acceleration'
    shipBuilder_vehicleitemparams_223.value = 20.0
    shipBuilder_vehicleitemparams_223 = importer.save_or_locate(shipBuilder_vehicleitemparams_223)

    shipBuilder_vehicleitemparams_224 = VehicleItemParams()
    shipBuilder_vehicleitemparams_224.name = u'pitchMax'
    shipBuilder_vehicleitemparams_224.value = 10.0
    shipBuilder_vehicleitemparams_224 = importer.save_or_locate(shipBuilder_vehicleitemparams_224)

    shipBuilder_vehicleitemparams_225 = VehicleItemParams()
    shipBuilder_vehicleitemparams_225.name = u'maxThrust'
    shipBuilder_vehicleitemparams_225.value = 2600000.0
    shipBuilder_vehicleitemparams_225 = importer.save_or_locate(shipBuilder_vehicleitemparams_225)

    shipBuilder_vehicleitemparams_226 = VehicleItemParams()
    shipBuilder_vehicleitemparams_226.name = u'pitchMin'
    shipBuilder_vehicleitemparams_226.value = -10.0
    shipBuilder_vehicleitemparams_226 = importer.save_or_locate(shipBuilder_vehicleitemparams_226)

    shipBuilder_vehicleitemparams_227 = VehicleItemParams()
    shipBuilder_vehicleitemparams_227.name = u'yawMin'
    shipBuilder_vehicleitemparams_227.value = -10.0
    shipBuilder_vehicleitemparams_227 = importer.save_or_locate(shipBuilder_vehicleitemparams_227)

    shipBuilder_vehicleitemparams_228 = VehicleItemParams()
    shipBuilder_vehicleitemparams_228.name = u'yawMax'
    shipBuilder_vehicleitemparams_228.value = 10.0
    shipBuilder_vehicleitemparams_228 = importer.save_or_locate(shipBuilder_vehicleitemparams_228)

    shipBuilder_vehicleitemparams_229 = VehicleItemParams()
    shipBuilder_vehicleitemparams_229.name = u'speed'
    shipBuilder_vehicleitemparams_229.value = 40.0
    shipBuilder_vehicleitemparams_229 = importer.save_or_locate(shipBuilder_vehicleitemparams_229)

    shipBuilder_vehicleitemparams_230 = VehicleItemParams()
    shipBuilder_vehicleitemparams_230.name = u'chargeRate'
    shipBuilder_vehicleitemparams_230.value = 100.0
    shipBuilder_vehicleitemparams_230 = importer.save_or_locate(shipBuilder_vehicleitemparams_230)

    shipBuilder_vehicleitemparams_231 = VehicleItemParams()
    shipBuilder_vehicleitemparams_231.name = u'output'
    shipBuilder_vehicleitemparams_231.value = 200.0
    shipBuilder_vehicleitemparams_231 = importer.save_or_locate(shipBuilder_vehicleitemparams_231)

    shipBuilder_vehicleitemparams_232 = VehicleItemParams()
    shipBuilder_vehicleitemparams_232.name = u'capacity'
    shipBuilder_vehicleitemparams_232.value = 700.0
    shipBuilder_vehicleitemparams_232 = importer.save_or_locate(shipBuilder_vehicleitemparams_232)

    shipBuilder_vehicleitemparams_233 = VehicleItemParams()
    shipBuilder_vehicleitemparams_233.name = u'gridSize'
    shipBuilder_vehicleitemparams_233.value = 1.0
    shipBuilder_vehicleitemparams_233 = importer.save_or_locate(shipBuilder_vehicleitemparams_233)

    shipBuilder_vehicleitemparams_234 = VehicleItemParams()
    shipBuilder_vehicleitemparams_234.name = u'radius'
    shipBuilder_vehicleitemparams_234.value = 1500.0
    shipBuilder_vehicleitemparams_234 = importer.save_or_locate(shipBuilder_vehicleitemparams_234)

    shipBuilder_vehicleitemparams_235 = VehicleItemParams()
    shipBuilder_vehicleitemparams_235.name = u'identifyTime'
    shipBuilder_vehicleitemparams_235.value = 0.5
    shipBuilder_vehicleitemparams_235 = importer.save_or_locate(shipBuilder_vehicleitemparams_235)

    shipBuilder_vehicleitemparams_236 = VehicleItemParams()
    shipBuilder_vehicleitemparams_236.name = u'radarTime'
    shipBuilder_vehicleitemparams_236.value = 0.0
    shipBuilder_vehicleitemparams_236 = importer.save_or_locate(shipBuilder_vehicleitemparams_236)

    shipBuilder_vehicleitemparams_237 = VehicleItemParams()
    shipBuilder_vehicleitemparams_237.name = u'radarType'
    shipBuilder_vehicleitemparams_237.value = 2.0
    shipBuilder_vehicleitemparams_237 = importer.save_or_locate(shipBuilder_vehicleitemparams_237)

    shipBuilder_vehicleitemparams_238 = VehicleItemParams()
    shipBuilder_vehicleitemparams_238.name = u'RoF'
    shipBuilder_vehicleitemparams_238.value = 60.0
    shipBuilder_vehicleitemparams_238 = importer.save_or_locate(shipBuilder_vehicleitemparams_238)

    shipBuilder_vehicleitemparams_239 = VehicleItemParams()
    shipBuilder_vehicleitemparams_239.name = u'Range'
    shipBuilder_vehicleitemparams_239.value = 60.0
    shipBuilder_vehicleitemparams_239 = importer.save_or_locate(shipBuilder_vehicleitemparams_239)

    shipBuilder_vehicleitemparams_240 = VehicleItemParams()
    shipBuilder_vehicleitemparams_240.name = u'Damage'
    shipBuilder_vehicleitemparams_240.value = 1.5
    shipBuilder_vehicleitemparams_240 = importer.save_or_locate(shipBuilder_vehicleitemparams_240)

    shipBuilder_vehicleitemparams_241 = VehicleItemParams()
    shipBuilder_vehicleitemparams_241.name = u'Power'
    shipBuilder_vehicleitemparams_241.value = 37.8
    shipBuilder_vehicleitemparams_241 = importer.save_or_locate(shipBuilder_vehicleitemparams_241)

    #Processing model: VehicleItemPower

    from shipBuilder.models import VehicleItemPower

    shipBuilder_vehicleitempower_1 = VehicleItemPower()
    shipBuilder_vehicleitempower_1.state = u'Active'
    shipBuilder_vehicleitempower_1.value = u'-10'
    shipBuilder_vehicleitempower_1 = importer.save_or_locate(shipBuilder_vehicleitempower_1)

    shipBuilder_vehicleitempower_2 = VehicleItemPower()
    shipBuilder_vehicleitempower_2.state = u'Idle'
    shipBuilder_vehicleitempower_2.value = u'-3'
    shipBuilder_vehicleitempower_2 = importer.save_or_locate(shipBuilder_vehicleitempower_2)

    shipBuilder_vehicleitempower_3 = VehicleItemPower()
    shipBuilder_vehicleitempower_3.state = u'Shooting'
    shipBuilder_vehicleitempower_3.value = u'-30'
    shipBuilder_vehicleitempower_3 = importer.save_or_locate(shipBuilder_vehicleitempower_3)

    shipBuilder_vehicleitempower_4 = VehicleItemPower()
    shipBuilder_vehicleitempower_4.state = u'Default'
    shipBuilder_vehicleitempower_4.value = u'100'
    shipBuilder_vehicleitempower_4 = importer.save_or_locate(shipBuilder_vehicleitempower_4)

    shipBuilder_vehicleitempower_5 = VehicleItemPower()
    shipBuilder_vehicleitempower_5.state = u'Active'
    shipBuilder_vehicleitempower_5.value = u'-10'
    shipBuilder_vehicleitempower_5 = importer.save_or_locate(shipBuilder_vehicleitempower_5)

    shipBuilder_vehicleitempower_6 = VehicleItemPower()
    shipBuilder_vehicleitempower_6.state = u'Idle'
    shipBuilder_vehicleitempower_6.value = u'-3'
    shipBuilder_vehicleitempower_6 = importer.save_or_locate(shipBuilder_vehicleitempower_6)

    shipBuilder_vehicleitempower_7 = VehicleItemPower()
    shipBuilder_vehicleitempower_7.state = u'Targeting'
    shipBuilder_vehicleitempower_7.value = u'-30'
    shipBuilder_vehicleitempower_7 = importer.save_or_locate(shipBuilder_vehicleitempower_7)

    shipBuilder_vehicleitempower_8 = VehicleItemPower()
    shipBuilder_vehicleitempower_8.state = u'Default'
    shipBuilder_vehicleitempower_8.value = u'100'
    shipBuilder_vehicleitempower_8 = importer.save_or_locate(shipBuilder_vehicleitempower_8)

    shipBuilder_vehicleitempower_9 = VehicleItemPower()
    shipBuilder_vehicleitempower_9.state = u'Active'
    shipBuilder_vehicleitempower_9.value = u'-10'
    shipBuilder_vehicleitempower_9 = importer.save_or_locate(shipBuilder_vehicleitempower_9)

    shipBuilder_vehicleitempower_10 = VehicleItemPower()
    shipBuilder_vehicleitempower_10.state = u'Idle'
    shipBuilder_vehicleitempower_10.value = u'-3'
    shipBuilder_vehicleitempower_10 = importer.save_or_locate(shipBuilder_vehicleitempower_10)

    shipBuilder_vehicleitempower_11 = VehicleItemPower()
    shipBuilder_vehicleitempower_11.state = u'Targeting'
    shipBuilder_vehicleitempower_11.value = u'-80'
    shipBuilder_vehicleitempower_11 = importer.save_or_locate(shipBuilder_vehicleitempower_11)

    shipBuilder_vehicleitempower_12 = VehicleItemPower()
    shipBuilder_vehicleitempower_12.state = u'Active'
    shipBuilder_vehicleitempower_12.value = u'-10'
    shipBuilder_vehicleitempower_12 = importer.save_or_locate(shipBuilder_vehicleitempower_12)

    shipBuilder_vehicleitempower_13 = VehicleItemPower()
    shipBuilder_vehicleitempower_13.state = u'Idle'
    shipBuilder_vehicleitempower_13.value = u'-10'
    shipBuilder_vehicleitempower_13 = importer.save_or_locate(shipBuilder_vehicleitempower_13)

    shipBuilder_vehicleitempower_14 = VehicleItemPower()
    shipBuilder_vehicleitempower_14.state = u'Shooting'
    shipBuilder_vehicleitempower_14.value = u'-80'
    shipBuilder_vehicleitempower_14 = importer.save_or_locate(shipBuilder_vehicleitempower_14)

    shipBuilder_vehicleitempower_15 = VehicleItemPower()
    shipBuilder_vehicleitempower_15.state = u'Active'
    shipBuilder_vehicleitempower_15.value = u'-10'
    shipBuilder_vehicleitempower_15 = importer.save_or_locate(shipBuilder_vehicleitempower_15)

    shipBuilder_vehicleitempower_16 = VehicleItemPower()
    shipBuilder_vehicleitempower_16.state = u'Idle'
    shipBuilder_vehicleitempower_16.value = u'-3'
    shipBuilder_vehicleitempower_16 = importer.save_or_locate(shipBuilder_vehicleitempower_16)

    shipBuilder_vehicleitempower_17 = VehicleItemPower()
    shipBuilder_vehicleitempower_17.state = u'Targeting'
    shipBuilder_vehicleitempower_17.value = u'-30'
    shipBuilder_vehicleitempower_17 = importer.save_or_locate(shipBuilder_vehicleitempower_17)

    shipBuilder_vehicleitempower_18 = VehicleItemPower()
    shipBuilder_vehicleitempower_18.state = u'Active'
    shipBuilder_vehicleitempower_18.value = u'-10'
    shipBuilder_vehicleitempower_18 = importer.save_or_locate(shipBuilder_vehicleitempower_18)

    shipBuilder_vehicleitempower_19 = VehicleItemPower()
    shipBuilder_vehicleitempower_19.state = u'Idle'
    shipBuilder_vehicleitempower_19.value = u'-3'
    shipBuilder_vehicleitempower_19 = importer.save_or_locate(shipBuilder_vehicleitempower_19)

    shipBuilder_vehicleitempower_20 = VehicleItemPower()
    shipBuilder_vehicleitempower_20.state = u'Shooting'
    shipBuilder_vehicleitempower_20.value = u'-30'
    shipBuilder_vehicleitempower_20 = importer.save_or_locate(shipBuilder_vehicleitempower_20)

    shipBuilder_vehicleitempower_21 = VehicleItemPower()
    shipBuilder_vehicleitempower_21.state = u'Default'
    shipBuilder_vehicleitempower_21.value = u'100'
    shipBuilder_vehicleitempower_21 = importer.save_or_locate(shipBuilder_vehicleitempower_21)

    shipBuilder_vehicleitempower_22 = VehicleItemPower()
    shipBuilder_vehicleitempower_22.state = u'Active'
    shipBuilder_vehicleitempower_22.value = u'-10'
    shipBuilder_vehicleitempower_22 = importer.save_or_locate(shipBuilder_vehicleitempower_22)

    shipBuilder_vehicleitempower_23 = VehicleItemPower()
    shipBuilder_vehicleitempower_23.state = u'Idle'
    shipBuilder_vehicleitempower_23.value = u'-3'
    shipBuilder_vehicleitempower_23 = importer.save_or_locate(shipBuilder_vehicleitempower_23)

    shipBuilder_vehicleitempower_24 = VehicleItemPower()
    shipBuilder_vehicleitempower_24.state = u'Shooting'
    shipBuilder_vehicleitempower_24.value = u'-30'
    shipBuilder_vehicleitempower_24 = importer.save_or_locate(shipBuilder_vehicleitempower_24)

    shipBuilder_vehicleitempower_25 = VehicleItemPower()
    shipBuilder_vehicleitempower_25.state = u'Default'
    shipBuilder_vehicleitempower_25.value = u'100'
    shipBuilder_vehicleitempower_25 = importer.save_or_locate(shipBuilder_vehicleitempower_25)

    shipBuilder_vehicleitempower_26 = VehicleItemPower()
    shipBuilder_vehicleitempower_26.state = u'Active'
    shipBuilder_vehicleitempower_26.value = u'-10'
    shipBuilder_vehicleitempower_26 = importer.save_or_locate(shipBuilder_vehicleitempower_26)

    shipBuilder_vehicleitempower_27 = VehicleItemPower()
    shipBuilder_vehicleitempower_27.state = u'Idle'
    shipBuilder_vehicleitempower_27.value = u'-3'
    shipBuilder_vehicleitempower_27 = importer.save_or_locate(shipBuilder_vehicleitempower_27)

    shipBuilder_vehicleitempower_28 = VehicleItemPower()
    shipBuilder_vehicleitempower_28.state = u'Shooting'
    shipBuilder_vehicleitempower_28.value = u'-30'
    shipBuilder_vehicleitempower_28 = importer.save_or_locate(shipBuilder_vehicleitempower_28)

    shipBuilder_vehicleitempower_29 = VehicleItemPower()
    shipBuilder_vehicleitempower_29.state = u'Active'
    shipBuilder_vehicleitempower_29.value = u'-10'
    shipBuilder_vehicleitempower_29 = importer.save_or_locate(shipBuilder_vehicleitempower_29)

    shipBuilder_vehicleitempower_30 = VehicleItemPower()
    shipBuilder_vehicleitempower_30.state = u'Idle'
    shipBuilder_vehicleitempower_30.value = u'-3'
    shipBuilder_vehicleitempower_30 = importer.save_or_locate(shipBuilder_vehicleitempower_30)

    shipBuilder_vehicleitempower_31 = VehicleItemPower()
    shipBuilder_vehicleitempower_31.state = u'Targeting'
    shipBuilder_vehicleitempower_31.value = u'-30'
    shipBuilder_vehicleitempower_31 = importer.save_or_locate(shipBuilder_vehicleitempower_31)

    shipBuilder_vehicleitempower_32 = VehicleItemPower()
    shipBuilder_vehicleitempower_32.state = u'Default'
    shipBuilder_vehicleitempower_32.value = u'100'
    shipBuilder_vehicleitempower_32 = importer.save_or_locate(shipBuilder_vehicleitempower_32)

    shipBuilder_vehicleitempower_33 = VehicleItemPower()
    shipBuilder_vehicleitempower_33.state = u'Active'
    shipBuilder_vehicleitempower_33.value = u'-10'
    shipBuilder_vehicleitempower_33 = importer.save_or_locate(shipBuilder_vehicleitempower_33)

    shipBuilder_vehicleitempower_34 = VehicleItemPower()
    shipBuilder_vehicleitempower_34.state = u'Idle'
    shipBuilder_vehicleitempower_34.value = u'-3'
    shipBuilder_vehicleitempower_34 = importer.save_or_locate(shipBuilder_vehicleitempower_34)

    shipBuilder_vehicleitempower_35 = VehicleItemPower()
    shipBuilder_vehicleitempower_35.state = u'Targeting'
    shipBuilder_vehicleitempower_35.value = u'-30'
    shipBuilder_vehicleitempower_35 = importer.save_or_locate(shipBuilder_vehicleitempower_35)

    shipBuilder_vehicleitempower_36 = VehicleItemPower()
    shipBuilder_vehicleitempower_36.state = u'Default'
    shipBuilder_vehicleitempower_36.value = u'100'
    shipBuilder_vehicleitempower_36 = importer.save_or_locate(shipBuilder_vehicleitempower_36)

    shipBuilder_vehicleitempower_37 = VehicleItemPower()
    shipBuilder_vehicleitempower_37.state = u'Active'
    shipBuilder_vehicleitempower_37.value = u'-10'
    shipBuilder_vehicleitempower_37 = importer.save_or_locate(shipBuilder_vehicleitempower_37)

    shipBuilder_vehicleitempower_38 = VehicleItemPower()
    shipBuilder_vehicleitempower_38.state = u'Idle'
    shipBuilder_vehicleitempower_38.value = u'-3'
    shipBuilder_vehicleitempower_38 = importer.save_or_locate(shipBuilder_vehicleitempower_38)

    shipBuilder_vehicleitempower_39 = VehicleItemPower()
    shipBuilder_vehicleitempower_39.state = u'Shooting'
    shipBuilder_vehicleitempower_39.value = u'-30'
    shipBuilder_vehicleitempower_39 = importer.save_or_locate(shipBuilder_vehicleitempower_39)

    shipBuilder_vehicleitempower_40 = VehicleItemPower()
    shipBuilder_vehicleitempower_40.state = u'Active'
    shipBuilder_vehicleitempower_40.value = u'-10'
    shipBuilder_vehicleitempower_40 = importer.save_or_locate(shipBuilder_vehicleitempower_40)

    shipBuilder_vehicleitempower_41 = VehicleItemPower()
    shipBuilder_vehicleitempower_41.state = u'Idle'
    shipBuilder_vehicleitempower_41.value = u'-3'
    shipBuilder_vehicleitempower_41 = importer.save_or_locate(shipBuilder_vehicleitempower_41)

    shipBuilder_vehicleitempower_42 = VehicleItemPower()
    shipBuilder_vehicleitempower_42.state = u'Targeting'
    shipBuilder_vehicleitempower_42.value = u'-30'
    shipBuilder_vehicleitempower_42 = importer.save_or_locate(shipBuilder_vehicleitempower_42)

    shipBuilder_vehicleitempower_43 = VehicleItemPower()
    shipBuilder_vehicleitempower_43.state = u'Active'
    shipBuilder_vehicleitempower_43.value = u'-10'
    shipBuilder_vehicleitempower_43 = importer.save_or_locate(shipBuilder_vehicleitempower_43)

    shipBuilder_vehicleitempower_44 = VehicleItemPower()
    shipBuilder_vehicleitempower_44.state = u'Idle'
    shipBuilder_vehicleitempower_44.value = u'-3'
    shipBuilder_vehicleitempower_44 = importer.save_or_locate(shipBuilder_vehicleitempower_44)

    shipBuilder_vehicleitempower_45 = VehicleItemPower()
    shipBuilder_vehicleitempower_45.state = u'Shooting'
    shipBuilder_vehicleitempower_45.value = u'-30'
    shipBuilder_vehicleitempower_45 = importer.save_or_locate(shipBuilder_vehicleitempower_45)

    shipBuilder_vehicleitempower_46 = VehicleItemPower()
    shipBuilder_vehicleitempower_46.state = u'Active'
    shipBuilder_vehicleitempower_46.value = u'-10'
    shipBuilder_vehicleitempower_46 = importer.save_or_locate(shipBuilder_vehicleitempower_46)

    shipBuilder_vehicleitempower_47 = VehicleItemPower()
    shipBuilder_vehicleitempower_47.state = u'Idle'
    shipBuilder_vehicleitempower_47.value = u'-3'
    shipBuilder_vehicleitempower_47 = importer.save_or_locate(shipBuilder_vehicleitempower_47)

    shipBuilder_vehicleitempower_48 = VehicleItemPower()
    shipBuilder_vehicleitempower_48.state = u'Shooting'
    shipBuilder_vehicleitempower_48.value = u'-30'
    shipBuilder_vehicleitempower_48 = importer.save_or_locate(shipBuilder_vehicleitempower_48)

    shipBuilder_vehicleitempower_49 = VehicleItemPower()
    shipBuilder_vehicleitempower_49.state = u'Active'
    shipBuilder_vehicleitempower_49.value = u'-10'
    shipBuilder_vehicleitempower_49 = importer.save_or_locate(shipBuilder_vehicleitempower_49)

    shipBuilder_vehicleitempower_50 = VehicleItemPower()
    shipBuilder_vehicleitempower_50.state = u'Idle'
    shipBuilder_vehicleitempower_50.value = u'-3'
    shipBuilder_vehicleitempower_50 = importer.save_or_locate(shipBuilder_vehicleitempower_50)

    shipBuilder_vehicleitempower_51 = VehicleItemPower()
    shipBuilder_vehicleitempower_51.state = u'Shooting'
    shipBuilder_vehicleitempower_51.value = u'-30'
    shipBuilder_vehicleitempower_51 = importer.save_or_locate(shipBuilder_vehicleitempower_51)

    shipBuilder_vehicleitempower_52 = VehicleItemPower()
    shipBuilder_vehicleitempower_52.state = u'Active'
    shipBuilder_vehicleitempower_52.value = u'-10'
    shipBuilder_vehicleitempower_52 = importer.save_or_locate(shipBuilder_vehicleitempower_52)

    shipBuilder_vehicleitempower_53 = VehicleItemPower()
    shipBuilder_vehicleitempower_53.state = u'Idle'
    shipBuilder_vehicleitempower_53.value = u'-3'
    shipBuilder_vehicleitempower_53 = importer.save_or_locate(shipBuilder_vehicleitempower_53)

    shipBuilder_vehicleitempower_54 = VehicleItemPower()
    shipBuilder_vehicleitempower_54.state = u'Shooting'
    shipBuilder_vehicleitempower_54.value = u'-30'
    shipBuilder_vehicleitempower_54 = importer.save_or_locate(shipBuilder_vehicleitempower_54)

    shipBuilder_vehicleitempower_55 = VehicleItemPower()
    shipBuilder_vehicleitempower_55.state = u'Default'
    shipBuilder_vehicleitempower_55.value = u'100'
    shipBuilder_vehicleitempower_55 = importer.save_or_locate(shipBuilder_vehicleitempower_55)

    shipBuilder_vehicleitempower_56 = VehicleItemPower()
    shipBuilder_vehicleitempower_56.state = u'Active'
    shipBuilder_vehicleitempower_56.value = u'-10'
    shipBuilder_vehicleitempower_56 = importer.save_or_locate(shipBuilder_vehicleitempower_56)

    shipBuilder_vehicleitempower_57 = VehicleItemPower()
    shipBuilder_vehicleitempower_57.state = u'Idle'
    shipBuilder_vehicleitempower_57.value = u'-3'
    shipBuilder_vehicleitempower_57 = importer.save_or_locate(shipBuilder_vehicleitempower_57)

    shipBuilder_vehicleitempower_58 = VehicleItemPower()
    shipBuilder_vehicleitempower_58.state = u'Shooting'
    shipBuilder_vehicleitempower_58.value = u'-30'
    shipBuilder_vehicleitempower_58 = importer.save_or_locate(shipBuilder_vehicleitempower_58)

    shipBuilder_vehicleitempower_59 = VehicleItemPower()
    shipBuilder_vehicleitempower_59.state = u'Active'
    shipBuilder_vehicleitempower_59.value = u'-10'
    shipBuilder_vehicleitempower_59 = importer.save_or_locate(shipBuilder_vehicleitempower_59)

    shipBuilder_vehicleitempower_60 = VehicleItemPower()
    shipBuilder_vehicleitempower_60.state = u'Idle'
    shipBuilder_vehicleitempower_60.value = u'-3'
    shipBuilder_vehicleitempower_60 = importer.save_or_locate(shipBuilder_vehicleitempower_60)

    shipBuilder_vehicleitempower_61 = VehicleItemPower()
    shipBuilder_vehicleitempower_61.state = u'Shooting'
    shipBuilder_vehicleitempower_61.value = u'-30'
    shipBuilder_vehicleitempower_61 = importer.save_or_locate(shipBuilder_vehicleitempower_61)

    shipBuilder_vehicleitempower_62 = VehicleItemPower()
    shipBuilder_vehicleitempower_62.state = u'Default'
    shipBuilder_vehicleitempower_62.value = u'100'
    shipBuilder_vehicleitempower_62 = importer.save_or_locate(shipBuilder_vehicleitempower_62)

    shipBuilder_vehicleitempower_63 = VehicleItemPower()
    shipBuilder_vehicleitempower_63.state = u'Active'
    shipBuilder_vehicleitempower_63.value = u'-10'
    shipBuilder_vehicleitempower_63 = importer.save_or_locate(shipBuilder_vehicleitempower_63)

    shipBuilder_vehicleitempower_64 = VehicleItemPower()
    shipBuilder_vehicleitempower_64.state = u'Idle'
    shipBuilder_vehicleitempower_64.value = u'-3'
    shipBuilder_vehicleitempower_64 = importer.save_or_locate(shipBuilder_vehicleitempower_64)

    shipBuilder_vehicleitempower_65 = VehicleItemPower()
    shipBuilder_vehicleitempower_65.state = u'Shooting'
    shipBuilder_vehicleitempower_65.value = u'-30'
    shipBuilder_vehicleitempower_65 = importer.save_or_locate(shipBuilder_vehicleitempower_65)

    shipBuilder_vehicleitempower_66 = VehicleItemPower()
    shipBuilder_vehicleitempower_66.state = u'Default'
    shipBuilder_vehicleitempower_66.value = u'100'
    shipBuilder_vehicleitempower_66 = importer.save_or_locate(shipBuilder_vehicleitempower_66)

    shipBuilder_vehicleitempower_67 = VehicleItemPower()
    shipBuilder_vehicleitempower_67.state = u'Default'
    shipBuilder_vehicleitempower_67.value = u'100'
    shipBuilder_vehicleitempower_67 = importer.save_or_locate(shipBuilder_vehicleitempower_67)

    shipBuilder_vehicleitempower_68 = VehicleItemPower()
    shipBuilder_vehicleitempower_68.state = u'Default'
    shipBuilder_vehicleitempower_68.value = u'100'
    shipBuilder_vehicleitempower_68 = importer.save_or_locate(shipBuilder_vehicleitempower_68)

    shipBuilder_vehicleitempower_69 = VehicleItemPower()
    shipBuilder_vehicleitempower_69.state = u'Default'
    shipBuilder_vehicleitempower_69.value = u'100'
    shipBuilder_vehicleitempower_69 = importer.save_or_locate(shipBuilder_vehicleitempower_69)

    shipBuilder_vehicleitempower_70 = VehicleItemPower()
    shipBuilder_vehicleitempower_70.state = u'Active'
    shipBuilder_vehicleitempower_70.value = u'-10'
    shipBuilder_vehicleitempower_70 = importer.save_or_locate(shipBuilder_vehicleitempower_70)

    shipBuilder_vehicleitempower_71 = VehicleItemPower()
    shipBuilder_vehicleitempower_71.state = u'Idle'
    shipBuilder_vehicleitempower_71.value = u'-3'
    shipBuilder_vehicleitempower_71 = importer.save_or_locate(shipBuilder_vehicleitempower_71)

    shipBuilder_vehicleitempower_72 = VehicleItemPower()
    shipBuilder_vehicleitempower_72.state = u'Targeting'
    shipBuilder_vehicleitempower_72.value = u'-30'
    shipBuilder_vehicleitempower_72 = importer.save_or_locate(shipBuilder_vehicleitempower_72)

    shipBuilder_vehicleitempower_73 = VehicleItemPower()
    shipBuilder_vehicleitempower_73.state = u'Active'
    shipBuilder_vehicleitempower_73.value = u'-10'
    shipBuilder_vehicleitempower_73 = importer.save_or_locate(shipBuilder_vehicleitempower_73)

    shipBuilder_vehicleitempower_74 = VehicleItemPower()
    shipBuilder_vehicleitempower_74.state = u'Idle'
    shipBuilder_vehicleitempower_74.value = u'-3'
    shipBuilder_vehicleitempower_74 = importer.save_or_locate(shipBuilder_vehicleitempower_74)

    shipBuilder_vehicleitempower_75 = VehicleItemPower()
    shipBuilder_vehicleitempower_75.state = u'Shooting'
    shipBuilder_vehicleitempower_75.value = u'-30'
    shipBuilder_vehicleitempower_75 = importer.save_or_locate(shipBuilder_vehicleitempower_75)

    shipBuilder_vehicleitempower_76 = VehicleItemPower()
    shipBuilder_vehicleitempower_76.state = u'Default'
    shipBuilder_vehicleitempower_76.value = u'100'
    shipBuilder_vehicleitempower_76 = importer.save_or_locate(shipBuilder_vehicleitempower_76)

    shipBuilder_vehicleitempower_77 = VehicleItemPower()
    shipBuilder_vehicleitempower_77.state = u'Default'
    shipBuilder_vehicleitempower_77.value = u'100'
    shipBuilder_vehicleitempower_77 = importer.save_or_locate(shipBuilder_vehicleitempower_77)

    shipBuilder_vehicleitempower_78 = VehicleItemPower()
    shipBuilder_vehicleitempower_78.state = u'Default'
    shipBuilder_vehicleitempower_78.value = u'100'
    shipBuilder_vehicleitempower_78 = importer.save_or_locate(shipBuilder_vehicleitempower_78)

    shipBuilder_vehicleitempower_79 = VehicleItemPower()
    shipBuilder_vehicleitempower_79.state = u'Active'
    shipBuilder_vehicleitempower_79.value = u'-10'
    shipBuilder_vehicleitempower_79 = importer.save_or_locate(shipBuilder_vehicleitempower_79)

    shipBuilder_vehicleitempower_80 = VehicleItemPower()
    shipBuilder_vehicleitempower_80.state = u'Idle'
    shipBuilder_vehicleitempower_80.value = u'-3'
    shipBuilder_vehicleitempower_80 = importer.save_or_locate(shipBuilder_vehicleitempower_80)

    shipBuilder_vehicleitempower_81 = VehicleItemPower()
    shipBuilder_vehicleitempower_81.state = u'Shooting'
    shipBuilder_vehicleitempower_81.value = u'-30'
    shipBuilder_vehicleitempower_81 = importer.save_or_locate(shipBuilder_vehicleitempower_81)

    shipBuilder_vehicleitempower_82 = VehicleItemPower()
    shipBuilder_vehicleitempower_82.state = u'Default'
    shipBuilder_vehicleitempower_82.value = u'100'
    shipBuilder_vehicleitempower_82 = importer.save_or_locate(shipBuilder_vehicleitempower_82)

    shipBuilder_vehicleitempower_83 = VehicleItemPower()
    shipBuilder_vehicleitempower_83.state = u'Default'
    shipBuilder_vehicleitempower_83.value = u'100'
    shipBuilder_vehicleitempower_83 = importer.save_or_locate(shipBuilder_vehicleitempower_83)

    shipBuilder_vehicleitempower_84 = VehicleItemPower()
    shipBuilder_vehicleitempower_84.state = u'Active'
    shipBuilder_vehicleitempower_84.value = u'-10'
    shipBuilder_vehicleitempower_84 = importer.save_or_locate(shipBuilder_vehicleitempower_84)

    shipBuilder_vehicleitempower_85 = VehicleItemPower()
    shipBuilder_vehicleitempower_85.state = u'Idle'
    shipBuilder_vehicleitempower_85.value = u'-3'
    shipBuilder_vehicleitempower_85 = importer.save_or_locate(shipBuilder_vehicleitempower_85)

    shipBuilder_vehicleitempower_86 = VehicleItemPower()
    shipBuilder_vehicleitempower_86.state = u'Shooting'
    shipBuilder_vehicleitempower_86.value = u'-30'
    shipBuilder_vehicleitempower_86 = importer.save_or_locate(shipBuilder_vehicleitempower_86)

    shipBuilder_vehicleitempower_87 = VehicleItemPower()
    shipBuilder_vehicleitempower_87.state = u'Active'
    shipBuilder_vehicleitempower_87.value = u'-10'
    shipBuilder_vehicleitempower_87 = importer.save_or_locate(shipBuilder_vehicleitempower_87)

    shipBuilder_vehicleitempower_88 = VehicleItemPower()
    shipBuilder_vehicleitempower_88.state = u'Idle'
    shipBuilder_vehicleitempower_88.value = u'-3'
    shipBuilder_vehicleitempower_88 = importer.save_or_locate(shipBuilder_vehicleitempower_88)

    shipBuilder_vehicleitempower_89 = VehicleItemPower()
    shipBuilder_vehicleitempower_89.state = u'Shooting'
    shipBuilder_vehicleitempower_89.value = u'-80'
    shipBuilder_vehicleitempower_89 = importer.save_or_locate(shipBuilder_vehicleitempower_89)

    shipBuilder_vehicleitempower_90 = VehicleItemPower()
    shipBuilder_vehicleitempower_90.state = u'Default'
    shipBuilder_vehicleitempower_90.value = u'100'
    shipBuilder_vehicleitempower_90 = importer.save_or_locate(shipBuilder_vehicleitempower_90)

    shipBuilder_vehicleitempower_91 = VehicleItemPower()
    shipBuilder_vehicleitempower_91.state = u'Active'
    shipBuilder_vehicleitempower_91.value = u'-10'
    shipBuilder_vehicleitempower_91 = importer.save_or_locate(shipBuilder_vehicleitempower_91)

    shipBuilder_vehicleitempower_92 = VehicleItemPower()
    shipBuilder_vehicleitempower_92.state = u'Idle'
    shipBuilder_vehicleitempower_92.value = u'-10'
    shipBuilder_vehicleitempower_92 = importer.save_or_locate(shipBuilder_vehicleitempower_92)

    shipBuilder_vehicleitempower_93 = VehicleItemPower()
    shipBuilder_vehicleitempower_93.state = u'Shooting'
    shipBuilder_vehicleitempower_93.value = u'-80'
    shipBuilder_vehicleitempower_93 = importer.save_or_locate(shipBuilder_vehicleitempower_93)

    shipBuilder_vehicleitempower_94 = VehicleItemPower()
    shipBuilder_vehicleitempower_94.state = u'Default'
    shipBuilder_vehicleitempower_94.value = u'100'
    shipBuilder_vehicleitempower_94 = importer.save_or_locate(shipBuilder_vehicleitempower_94)

    shipBuilder_vehicleitempower_95 = VehicleItemPower()
    shipBuilder_vehicleitempower_95.state = u'Active'
    shipBuilder_vehicleitempower_95.value = u'-10'
    shipBuilder_vehicleitempower_95 = importer.save_or_locate(shipBuilder_vehicleitempower_95)

    shipBuilder_vehicleitempower_96 = VehicleItemPower()
    shipBuilder_vehicleitempower_96.state = u'Idle'
    shipBuilder_vehicleitempower_96.value = u'-3'
    shipBuilder_vehicleitempower_96 = importer.save_or_locate(shipBuilder_vehicleitempower_96)

    shipBuilder_vehicleitempower_97 = VehicleItemPower()
    shipBuilder_vehicleitempower_97.state = u'Shooting'
    shipBuilder_vehicleitempower_97.value = u'-30'
    shipBuilder_vehicleitempower_97 = importer.save_or_locate(shipBuilder_vehicleitempower_97)

    #Processing model: VehicleItemHeat

    from shipBuilder.models import VehicleItemHeat

    shipBuilder_vehicleitemheat_1 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_1.state = u'Active'
    shipBuilder_vehicleitemheat_1.value = u'3'
    shipBuilder_vehicleitemheat_1 = importer.save_or_locate(shipBuilder_vehicleitemheat_1)

    shipBuilder_vehicleitemheat_2 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_2.state = u'Idle'
    shipBuilder_vehicleitemheat_2.value = u'3'
    shipBuilder_vehicleitemheat_2 = importer.save_or_locate(shipBuilder_vehicleitemheat_2)

    shipBuilder_vehicleitemheat_3 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_3.state = u'Shooting'
    shipBuilder_vehicleitemheat_3.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_3 = importer.save_or_locate(shipBuilder_vehicleitemheat_3)

    shipBuilder_vehicleitemheat_4 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_4.state = u'Active'
    shipBuilder_vehicleitemheat_4.value = u'3'
    shipBuilder_vehicleitemheat_4 = importer.save_or_locate(shipBuilder_vehicleitemheat_4)

    shipBuilder_vehicleitemheat_5 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_5.state = u'Idle'
    shipBuilder_vehicleitemheat_5.value = u'3'
    shipBuilder_vehicleitemheat_5 = importer.save_or_locate(shipBuilder_vehicleitemheat_5)

    shipBuilder_vehicleitemheat_6 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_6.state = u'Targeting'
    shipBuilder_vehicleitemheat_6.value = u'3'
    shipBuilder_vehicleitemheat_6 = importer.save_or_locate(shipBuilder_vehicleitemheat_6)

    shipBuilder_vehicleitemheat_7 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_7.state = u'Active'
    shipBuilder_vehicleitemheat_7.value = u'3'
    shipBuilder_vehicleitemheat_7 = importer.save_or_locate(shipBuilder_vehicleitemheat_7)

    shipBuilder_vehicleitemheat_8 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_8.state = u'Idle'
    shipBuilder_vehicleitemheat_8.value = u'3'
    shipBuilder_vehicleitemheat_8 = importer.save_or_locate(shipBuilder_vehicleitemheat_8)

    shipBuilder_vehicleitemheat_9 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_9.state = u'Targeting'
    shipBuilder_vehicleitemheat_9.value = u'3'
    shipBuilder_vehicleitemheat_9 = importer.save_or_locate(shipBuilder_vehicleitemheat_9)

    shipBuilder_vehicleitemheat_10 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_10.state = u'Active'
    shipBuilder_vehicleitemheat_10.value = u'3'
    shipBuilder_vehicleitemheat_10 = importer.save_or_locate(shipBuilder_vehicleitemheat_10)

    shipBuilder_vehicleitemheat_11 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_11.state = u'Idle'
    shipBuilder_vehicleitemheat_11.value = u'3'
    shipBuilder_vehicleitemheat_11 = importer.save_or_locate(shipBuilder_vehicleitemheat_11)

    shipBuilder_vehicleitemheat_12 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_12.state = u'Shooting'
    shipBuilder_vehicleitemheat_12.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_12 = importer.save_or_locate(shipBuilder_vehicleitemheat_12)

    shipBuilder_vehicleitemheat_13 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_13.state = u'Active'
    shipBuilder_vehicleitemheat_13.value = u'3'
    shipBuilder_vehicleitemheat_13 = importer.save_or_locate(shipBuilder_vehicleitemheat_13)

    shipBuilder_vehicleitemheat_14 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_14.state = u'Idle'
    shipBuilder_vehicleitemheat_14.value = u'3'
    shipBuilder_vehicleitemheat_14 = importer.save_or_locate(shipBuilder_vehicleitemheat_14)

    shipBuilder_vehicleitemheat_15 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_15.state = u'Targeting'
    shipBuilder_vehicleitemheat_15.value = u'3'
    shipBuilder_vehicleitemheat_15 = importer.save_or_locate(shipBuilder_vehicleitemheat_15)

    shipBuilder_vehicleitemheat_16 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_16.state = u'Active'
    shipBuilder_vehicleitemheat_16.value = u'3'
    shipBuilder_vehicleitemheat_16 = importer.save_or_locate(shipBuilder_vehicleitemheat_16)

    shipBuilder_vehicleitemheat_17 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_17.state = u'Idle'
    shipBuilder_vehicleitemheat_17.value = u'3'
    shipBuilder_vehicleitemheat_17 = importer.save_or_locate(shipBuilder_vehicleitemheat_17)

    shipBuilder_vehicleitemheat_18 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_18.state = u'Shooting'
    shipBuilder_vehicleitemheat_18.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_18 = importer.save_or_locate(shipBuilder_vehicleitemheat_18)

    shipBuilder_vehicleitemheat_19 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_19.state = u'Active'
    shipBuilder_vehicleitemheat_19.value = u'3'
    shipBuilder_vehicleitemheat_19 = importer.save_or_locate(shipBuilder_vehicleitemheat_19)

    shipBuilder_vehicleitemheat_20 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_20.state = u'Idle'
    shipBuilder_vehicleitemheat_20.value = u'3'
    shipBuilder_vehicleitemheat_20 = importer.save_or_locate(shipBuilder_vehicleitemheat_20)

    shipBuilder_vehicleitemheat_21 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_21.state = u'Shooting'
    shipBuilder_vehicleitemheat_21.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_21 = importer.save_or_locate(shipBuilder_vehicleitemheat_21)

    shipBuilder_vehicleitemheat_22 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_22.state = u'Active'
    shipBuilder_vehicleitemheat_22.value = u'3'
    shipBuilder_vehicleitemheat_22 = importer.save_or_locate(shipBuilder_vehicleitemheat_22)

    shipBuilder_vehicleitemheat_23 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_23.state = u'Idle'
    shipBuilder_vehicleitemheat_23.value = u'3'
    shipBuilder_vehicleitemheat_23 = importer.save_or_locate(shipBuilder_vehicleitemheat_23)

    shipBuilder_vehicleitemheat_24 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_24.state = u'Shooting'
    shipBuilder_vehicleitemheat_24.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_24 = importer.save_or_locate(shipBuilder_vehicleitemheat_24)

    shipBuilder_vehicleitemheat_25 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_25.state = u'Active'
    shipBuilder_vehicleitemheat_25.value = u'3'
    shipBuilder_vehicleitemheat_25 = importer.save_or_locate(shipBuilder_vehicleitemheat_25)

    shipBuilder_vehicleitemheat_26 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_26.state = u'Idle'
    shipBuilder_vehicleitemheat_26.value = u'3'
    shipBuilder_vehicleitemheat_26 = importer.save_or_locate(shipBuilder_vehicleitemheat_26)

    shipBuilder_vehicleitemheat_27 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_27.state = u'Targeting'
    shipBuilder_vehicleitemheat_27.value = u'3'
    shipBuilder_vehicleitemheat_27 = importer.save_or_locate(shipBuilder_vehicleitemheat_27)

    shipBuilder_vehicleitemheat_28 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_28.state = u'Active'
    shipBuilder_vehicleitemheat_28.value = u'3'
    shipBuilder_vehicleitemheat_28 = importer.save_or_locate(shipBuilder_vehicleitemheat_28)

    shipBuilder_vehicleitemheat_29 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_29.state = u'Idle'
    shipBuilder_vehicleitemheat_29.value = u'3'
    shipBuilder_vehicleitemheat_29 = importer.save_or_locate(shipBuilder_vehicleitemheat_29)

    shipBuilder_vehicleitemheat_30 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_30.state = u'Targeting'
    shipBuilder_vehicleitemheat_30.value = u'3'
    shipBuilder_vehicleitemheat_30 = importer.save_or_locate(shipBuilder_vehicleitemheat_30)

    shipBuilder_vehicleitemheat_31 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_31.state = u'Active'
    shipBuilder_vehicleitemheat_31.value = u'3'
    shipBuilder_vehicleitemheat_31 = importer.save_or_locate(shipBuilder_vehicleitemheat_31)

    shipBuilder_vehicleitemheat_32 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_32.state = u'Idle'
    shipBuilder_vehicleitemheat_32.value = u'3'
    shipBuilder_vehicleitemheat_32 = importer.save_or_locate(shipBuilder_vehicleitemheat_32)

    shipBuilder_vehicleitemheat_33 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_33.state = u'Shooting'
    shipBuilder_vehicleitemheat_33.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_33 = importer.save_or_locate(shipBuilder_vehicleitemheat_33)

    shipBuilder_vehicleitemheat_34 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_34.state = u'Active'
    shipBuilder_vehicleitemheat_34.value = u'3'
    shipBuilder_vehicleitemheat_34 = importer.save_or_locate(shipBuilder_vehicleitemheat_34)

    shipBuilder_vehicleitemheat_35 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_35.state = u'Idle'
    shipBuilder_vehicleitemheat_35.value = u'3'
    shipBuilder_vehicleitemheat_35 = importer.save_or_locate(shipBuilder_vehicleitemheat_35)

    shipBuilder_vehicleitemheat_36 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_36.state = u'Targeting'
    shipBuilder_vehicleitemheat_36.value = u'3'
    shipBuilder_vehicleitemheat_36 = importer.save_or_locate(shipBuilder_vehicleitemheat_36)

    shipBuilder_vehicleitemheat_37 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_37.state = u'Active'
    shipBuilder_vehicleitemheat_37.value = u'3'
    shipBuilder_vehicleitemheat_37 = importer.save_or_locate(shipBuilder_vehicleitemheat_37)

    shipBuilder_vehicleitemheat_38 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_38.state = u'Idle'
    shipBuilder_vehicleitemheat_38.value = u'3'
    shipBuilder_vehicleitemheat_38 = importer.save_or_locate(shipBuilder_vehicleitemheat_38)

    shipBuilder_vehicleitemheat_39 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_39.state = u'Shooting'
    shipBuilder_vehicleitemheat_39.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_39 = importer.save_or_locate(shipBuilder_vehicleitemheat_39)

    shipBuilder_vehicleitemheat_40 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_40.state = u'Active'
    shipBuilder_vehicleitemheat_40.value = u'3'
    shipBuilder_vehicleitemheat_40 = importer.save_or_locate(shipBuilder_vehicleitemheat_40)

    shipBuilder_vehicleitemheat_41 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_41.state = u'Idle'
    shipBuilder_vehicleitemheat_41.value = u'3'
    shipBuilder_vehicleitemheat_41 = importer.save_or_locate(shipBuilder_vehicleitemheat_41)

    shipBuilder_vehicleitemheat_42 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_42.state = u'Shooting'
    shipBuilder_vehicleitemheat_42.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_42 = importer.save_or_locate(shipBuilder_vehicleitemheat_42)

    shipBuilder_vehicleitemheat_43 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_43.state = u'Active'
    shipBuilder_vehicleitemheat_43.value = u'3'
    shipBuilder_vehicleitemheat_43 = importer.save_or_locate(shipBuilder_vehicleitemheat_43)

    shipBuilder_vehicleitemheat_44 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_44.state = u'Idle'
    shipBuilder_vehicleitemheat_44.value = u'3'
    shipBuilder_vehicleitemheat_44 = importer.save_or_locate(shipBuilder_vehicleitemheat_44)

    shipBuilder_vehicleitemheat_45 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_45.state = u'Shooting'
    shipBuilder_vehicleitemheat_45.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_45 = importer.save_or_locate(shipBuilder_vehicleitemheat_45)

    shipBuilder_vehicleitemheat_46 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_46.state = u'Default'
    shipBuilder_vehicleitemheat_46.value = u'-30'
    shipBuilder_vehicleitemheat_46 = importer.save_or_locate(shipBuilder_vehicleitemheat_46)

    shipBuilder_vehicleitemheat_47 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_47.state = u'Active'
    shipBuilder_vehicleitemheat_47.value = u'3'
    shipBuilder_vehicleitemheat_47 = importer.save_or_locate(shipBuilder_vehicleitemheat_47)

    shipBuilder_vehicleitemheat_48 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_48.state = u'Idle'
    shipBuilder_vehicleitemheat_48.value = u'3'
    shipBuilder_vehicleitemheat_48 = importer.save_or_locate(shipBuilder_vehicleitemheat_48)

    shipBuilder_vehicleitemheat_49 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_49.state = u'Shooting'
    shipBuilder_vehicleitemheat_49.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_49 = importer.save_or_locate(shipBuilder_vehicleitemheat_49)

    shipBuilder_vehicleitemheat_50 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_50.state = u'Active'
    shipBuilder_vehicleitemheat_50.value = u'3'
    shipBuilder_vehicleitemheat_50 = importer.save_or_locate(shipBuilder_vehicleitemheat_50)

    shipBuilder_vehicleitemheat_51 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_51.state = u'Idle'
    shipBuilder_vehicleitemheat_51.value = u'3'
    shipBuilder_vehicleitemheat_51 = importer.save_or_locate(shipBuilder_vehicleitemheat_51)

    shipBuilder_vehicleitemheat_52 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_52.state = u'Shooting'
    shipBuilder_vehicleitemheat_52.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_52 = importer.save_or_locate(shipBuilder_vehicleitemheat_52)

    shipBuilder_vehicleitemheat_53 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_53.state = u'Active'
    shipBuilder_vehicleitemheat_53.value = u'3'
    shipBuilder_vehicleitemheat_53 = importer.save_or_locate(shipBuilder_vehicleitemheat_53)

    shipBuilder_vehicleitemheat_54 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_54.state = u'Idle'
    shipBuilder_vehicleitemheat_54.value = u'3'
    shipBuilder_vehicleitemheat_54 = importer.save_or_locate(shipBuilder_vehicleitemheat_54)

    shipBuilder_vehicleitemheat_55 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_55.state = u'Shooting'
    shipBuilder_vehicleitemheat_55.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_55 = importer.save_or_locate(shipBuilder_vehicleitemheat_55)

    shipBuilder_vehicleitemheat_56 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_56.state = u'Active'
    shipBuilder_vehicleitemheat_56.value = u'3'
    shipBuilder_vehicleitemheat_56 = importer.save_or_locate(shipBuilder_vehicleitemheat_56)

    shipBuilder_vehicleitemheat_57 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_57.state = u'Idle'
    shipBuilder_vehicleitemheat_57.value = u'3'
    shipBuilder_vehicleitemheat_57 = importer.save_or_locate(shipBuilder_vehicleitemheat_57)

    shipBuilder_vehicleitemheat_58 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_58.state = u'Shooting'
    shipBuilder_vehicleitemheat_58.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_58 = importer.save_or_locate(shipBuilder_vehicleitemheat_58)

    shipBuilder_vehicleitemheat_59 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_59.state = u'Active'
    shipBuilder_vehicleitemheat_59.value = u'3'
    shipBuilder_vehicleitemheat_59 = importer.save_or_locate(shipBuilder_vehicleitemheat_59)

    shipBuilder_vehicleitemheat_60 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_60.state = u'Idle'
    shipBuilder_vehicleitemheat_60.value = u'3'
    shipBuilder_vehicleitemheat_60 = importer.save_or_locate(shipBuilder_vehicleitemheat_60)

    shipBuilder_vehicleitemheat_61 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_61.state = u'Targeting'
    shipBuilder_vehicleitemheat_61.value = u'3'
    shipBuilder_vehicleitemheat_61 = importer.save_or_locate(shipBuilder_vehicleitemheat_61)

    shipBuilder_vehicleitemheat_62 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_62.state = u'Active'
    shipBuilder_vehicleitemheat_62.value = u'3'
    shipBuilder_vehicleitemheat_62 = importer.save_or_locate(shipBuilder_vehicleitemheat_62)

    shipBuilder_vehicleitemheat_63 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_63.state = u'Idle'
    shipBuilder_vehicleitemheat_63.value = u'3'
    shipBuilder_vehicleitemheat_63 = importer.save_or_locate(shipBuilder_vehicleitemheat_63)

    shipBuilder_vehicleitemheat_64 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_64.state = u'Shooting'
    shipBuilder_vehicleitemheat_64.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_64 = importer.save_or_locate(shipBuilder_vehicleitemheat_64)

    shipBuilder_vehicleitemheat_65 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_65.state = u'Active'
    shipBuilder_vehicleitemheat_65.value = u'3'
    shipBuilder_vehicleitemheat_65 = importer.save_or_locate(shipBuilder_vehicleitemheat_65)

    shipBuilder_vehicleitemheat_66 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_66.state = u'Idle'
    shipBuilder_vehicleitemheat_66.value = u'3'
    shipBuilder_vehicleitemheat_66 = importer.save_or_locate(shipBuilder_vehicleitemheat_66)

    shipBuilder_vehicleitemheat_67 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_67.state = u'Shooting'
    shipBuilder_vehicleitemheat_67.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_67 = importer.save_or_locate(shipBuilder_vehicleitemheat_67)

    shipBuilder_vehicleitemheat_68 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_68.state = u'Active'
    shipBuilder_vehicleitemheat_68.value = u'3'
    shipBuilder_vehicleitemheat_68 = importer.save_or_locate(shipBuilder_vehicleitemheat_68)

    shipBuilder_vehicleitemheat_69 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_69.state = u'Idle'
    shipBuilder_vehicleitemheat_69.value = u'3'
    shipBuilder_vehicleitemheat_69 = importer.save_or_locate(shipBuilder_vehicleitemheat_69)

    shipBuilder_vehicleitemheat_70 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_70.state = u'Shooting'
    shipBuilder_vehicleitemheat_70.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_70 = importer.save_or_locate(shipBuilder_vehicleitemheat_70)

    shipBuilder_vehicleitemheat_71 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_71.state = u'Active'
    shipBuilder_vehicleitemheat_71.value = u'3'
    shipBuilder_vehicleitemheat_71 = importer.save_or_locate(shipBuilder_vehicleitemheat_71)

    shipBuilder_vehicleitemheat_72 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_72.state = u'Idle'
    shipBuilder_vehicleitemheat_72.value = u'3'
    shipBuilder_vehicleitemheat_72 = importer.save_or_locate(shipBuilder_vehicleitemheat_72)

    shipBuilder_vehicleitemheat_73 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_73.state = u'Shooting'
    shipBuilder_vehicleitemheat_73.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_73 = importer.save_or_locate(shipBuilder_vehicleitemheat_73)

    shipBuilder_vehicleitemheat_74 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_74.state = u'Active'
    shipBuilder_vehicleitemheat_74.value = u'3'
    shipBuilder_vehicleitemheat_74 = importer.save_or_locate(shipBuilder_vehicleitemheat_74)

    shipBuilder_vehicleitemheat_75 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_75.state = u'Idle'
    shipBuilder_vehicleitemheat_75.value = u'3'
    shipBuilder_vehicleitemheat_75 = importer.save_or_locate(shipBuilder_vehicleitemheat_75)

    shipBuilder_vehicleitemheat_76 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_76.state = u'Shooting'
    shipBuilder_vehicleitemheat_76.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_76 = importer.save_or_locate(shipBuilder_vehicleitemheat_76)

    shipBuilder_vehicleitemheat_77 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_77.state = u'Active'
    shipBuilder_vehicleitemheat_77.value = u'3'
    shipBuilder_vehicleitemheat_77 = importer.save_or_locate(shipBuilder_vehicleitemheat_77)

    shipBuilder_vehicleitemheat_78 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_78.state = u'Idle'
    shipBuilder_vehicleitemheat_78.value = u'3'
    shipBuilder_vehicleitemheat_78 = importer.save_or_locate(shipBuilder_vehicleitemheat_78)

    shipBuilder_vehicleitemheat_79 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_79.state = u'Shooting'
    shipBuilder_vehicleitemheat_79.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_79 = importer.save_or_locate(shipBuilder_vehicleitemheat_79)

    #Processing model: VehicleItemAvionics

    from shipBuilder.models import VehicleItemAvionics

    shipBuilder_vehicleitemavionics_1 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_1.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_1.value = u'20'
    shipBuilder_vehicleitemavionics_1 = importer.save_or_locate(shipBuilder_vehicleitemavionics_1)

    shipBuilder_vehicleitemavionics_2 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_2.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_2.value = u'0'
    shipBuilder_vehicleitemavionics_2 = importer.save_or_locate(shipBuilder_vehicleitemavionics_2)

    shipBuilder_vehicleitemavionics_3 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_3.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_3.value = u'20'
    shipBuilder_vehicleitemavionics_3 = importer.save_or_locate(shipBuilder_vehicleitemavionics_3)

    shipBuilder_vehicleitemavionics_4 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_4.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_4.value = u'0'
    shipBuilder_vehicleitemavionics_4 = importer.save_or_locate(shipBuilder_vehicleitemavionics_4)

    shipBuilder_vehicleitemavionics_5 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_5.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_5.value = u'20'
    shipBuilder_vehicleitemavionics_5 = importer.save_or_locate(shipBuilder_vehicleitemavionics_5)

    shipBuilder_vehicleitemavionics_6 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_6.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_6.value = u'0'
    shipBuilder_vehicleitemavionics_6 = importer.save_or_locate(shipBuilder_vehicleitemavionics_6)

    shipBuilder_vehicleitemavionics_7 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_7.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_7.value = u'20'
    shipBuilder_vehicleitemavionics_7 = importer.save_or_locate(shipBuilder_vehicleitemavionics_7)

    shipBuilder_vehicleitemavionics_8 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_8.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_8.value = u'0'
    shipBuilder_vehicleitemavionics_8 = importer.save_or_locate(shipBuilder_vehicleitemavionics_8)

    shipBuilder_vehicleitemavionics_9 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_9.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_9.value = u'20'
    shipBuilder_vehicleitemavionics_9 = importer.save_or_locate(shipBuilder_vehicleitemavionics_9)

    shipBuilder_vehicleitemavionics_10 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_10.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_10.value = u'0'
    shipBuilder_vehicleitemavionics_10 = importer.save_or_locate(shipBuilder_vehicleitemavionics_10)

    shipBuilder_vehicleitemavionics_11 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_11.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_11.value = u'20'
    shipBuilder_vehicleitemavionics_11 = importer.save_or_locate(shipBuilder_vehicleitemavionics_11)

    shipBuilder_vehicleitemavionics_12 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_12.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_12.value = u'0'
    shipBuilder_vehicleitemavionics_12 = importer.save_or_locate(shipBuilder_vehicleitemavionics_12)

    shipBuilder_vehicleitemavionics_13 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_13.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_13.value = u'20'
    shipBuilder_vehicleitemavionics_13 = importer.save_or_locate(shipBuilder_vehicleitemavionics_13)

    shipBuilder_vehicleitemavionics_14 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_14.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_14.value = u'0'
    shipBuilder_vehicleitemavionics_14 = importer.save_or_locate(shipBuilder_vehicleitemavionics_14)

    shipBuilder_vehicleitemavionics_15 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_15.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_15.value = u'20'
    shipBuilder_vehicleitemavionics_15 = importer.save_or_locate(shipBuilder_vehicleitemavionics_15)

    shipBuilder_vehicleitemavionics_16 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_16.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_16.value = u'0'
    shipBuilder_vehicleitemavionics_16 = importer.save_or_locate(shipBuilder_vehicleitemavionics_16)

    shipBuilder_vehicleitemavionics_17 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_17.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_17.value = u'20'
    shipBuilder_vehicleitemavionics_17 = importer.save_or_locate(shipBuilder_vehicleitemavionics_17)

    shipBuilder_vehicleitemavionics_18 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_18.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_18.value = u'0'
    shipBuilder_vehicleitemavionics_18 = importer.save_or_locate(shipBuilder_vehicleitemavionics_18)

    shipBuilder_vehicleitemavionics_19 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_19.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_19.value = u'20'
    shipBuilder_vehicleitemavionics_19 = importer.save_or_locate(shipBuilder_vehicleitemavionics_19)

    shipBuilder_vehicleitemavionics_20 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_20.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_20.value = u'0'
    shipBuilder_vehicleitemavionics_20 = importer.save_or_locate(shipBuilder_vehicleitemavionics_20)

    shipBuilder_vehicleitemavionics_21 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_21.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_21.value = u'20'
    shipBuilder_vehicleitemavionics_21 = importer.save_or_locate(shipBuilder_vehicleitemavionics_21)

    shipBuilder_vehicleitemavionics_22 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_22.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_22.value = u'0'
    shipBuilder_vehicleitemavionics_22 = importer.save_or_locate(shipBuilder_vehicleitemavionics_22)

    shipBuilder_vehicleitemavionics_23 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_23.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_23.value = u'20'
    shipBuilder_vehicleitemavionics_23 = importer.save_or_locate(shipBuilder_vehicleitemavionics_23)

    shipBuilder_vehicleitemavionics_24 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_24.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_24.value = u'0'
    shipBuilder_vehicleitemavionics_24 = importer.save_or_locate(shipBuilder_vehicleitemavionics_24)

    shipBuilder_vehicleitemavionics_25 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_25.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_25.value = u'20'
    shipBuilder_vehicleitemavionics_25 = importer.save_or_locate(shipBuilder_vehicleitemavionics_25)

    shipBuilder_vehicleitemavionics_26 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_26.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_26.value = u'0'
    shipBuilder_vehicleitemavionics_26 = importer.save_or_locate(shipBuilder_vehicleitemavionics_26)

    shipBuilder_vehicleitemavionics_27 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_27.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_27.value = u'20'
    shipBuilder_vehicleitemavionics_27 = importer.save_or_locate(shipBuilder_vehicleitemavionics_27)

    shipBuilder_vehicleitemavionics_28 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_28.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_28.value = u'0'
    shipBuilder_vehicleitemavionics_28 = importer.save_or_locate(shipBuilder_vehicleitemavionics_28)

    shipBuilder_vehicleitemavionics_29 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_29.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_29.value = u'20'
    shipBuilder_vehicleitemavionics_29 = importer.save_or_locate(shipBuilder_vehicleitemavionics_29)

    shipBuilder_vehicleitemavionics_30 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_30.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_30.value = u'0'
    shipBuilder_vehicleitemavionics_30 = importer.save_or_locate(shipBuilder_vehicleitemavionics_30)

    shipBuilder_vehicleitemavionics_31 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_31.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_31.value = u'20'
    shipBuilder_vehicleitemavionics_31 = importer.save_or_locate(shipBuilder_vehicleitemavionics_31)

    shipBuilder_vehicleitemavionics_32 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_32.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_32.value = u'0'
    shipBuilder_vehicleitemavionics_32 = importer.save_or_locate(shipBuilder_vehicleitemavionics_32)

    shipBuilder_vehicleitemavionics_33 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_33.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_33.value = u'20'
    shipBuilder_vehicleitemavionics_33 = importer.save_or_locate(shipBuilder_vehicleitemavionics_33)

    shipBuilder_vehicleitemavionics_34 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_34.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_34.value = u'0'
    shipBuilder_vehicleitemavionics_34 = importer.save_or_locate(shipBuilder_vehicleitemavionics_34)

    shipBuilder_vehicleitemavionics_35 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_35.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_35.value = u'20'
    shipBuilder_vehicleitemavionics_35 = importer.save_or_locate(shipBuilder_vehicleitemavionics_35)

    shipBuilder_vehicleitemavionics_36 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_36.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_36.value = u'0'
    shipBuilder_vehicleitemavionics_36 = importer.save_or_locate(shipBuilder_vehicleitemavionics_36)

    shipBuilder_vehicleitemavionics_37 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_37.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_37.value = u'20'
    shipBuilder_vehicleitemavionics_37 = importer.save_or_locate(shipBuilder_vehicleitemavionics_37)

    shipBuilder_vehicleitemavionics_38 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_38.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_38.value = u'0'
    shipBuilder_vehicleitemavionics_38 = importer.save_or_locate(shipBuilder_vehicleitemavionics_38)

    shipBuilder_vehicleitemavionics_39 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_39.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_39.value = u'20'
    shipBuilder_vehicleitemavionics_39 = importer.save_or_locate(shipBuilder_vehicleitemavionics_39)

    shipBuilder_vehicleitemavionics_40 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_40.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_40.value = u'0'
    shipBuilder_vehicleitemavionics_40 = importer.save_or_locate(shipBuilder_vehicleitemavionics_40)

    shipBuilder_vehicleitemavionics_41 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_41.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_41.value = u'20'
    shipBuilder_vehicleitemavionics_41 = importer.save_or_locate(shipBuilder_vehicleitemavionics_41)

    shipBuilder_vehicleitemavionics_42 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_42.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_42.value = u'0'
    shipBuilder_vehicleitemavionics_42 = importer.save_or_locate(shipBuilder_vehicleitemavionics_42)

    shipBuilder_vehicleitemavionics_43 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_43.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_43.value = u'20'
    shipBuilder_vehicleitemavionics_43 = importer.save_or_locate(shipBuilder_vehicleitemavionics_43)

    shipBuilder_vehicleitemavionics_44 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_44.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_44.value = u'0'
    shipBuilder_vehicleitemavionics_44 = importer.save_or_locate(shipBuilder_vehicleitemavionics_44)

    shipBuilder_vehicleitemavionics_45 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_45.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_45.value = u'20'
    shipBuilder_vehicleitemavionics_45 = importer.save_or_locate(shipBuilder_vehicleitemavionics_45)

    shipBuilder_vehicleitemavionics_46 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_46.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_46.value = u'0'
    shipBuilder_vehicleitemavionics_46 = importer.save_or_locate(shipBuilder_vehicleitemavionics_46)

    shipBuilder_vehicleitemavionics_47 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_47.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_47.value = u'20'
    shipBuilder_vehicleitemavionics_47 = importer.save_or_locate(shipBuilder_vehicleitemavionics_47)

    shipBuilder_vehicleitemavionics_48 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_48.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_48.value = u'0'
    shipBuilder_vehicleitemavionics_48 = importer.save_or_locate(shipBuilder_vehicleitemavionics_48)

    shipBuilder_vehicleitemavionics_49 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_49.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_49.value = u'20'
    shipBuilder_vehicleitemavionics_49 = importer.save_or_locate(shipBuilder_vehicleitemavionics_49)

    shipBuilder_vehicleitemavionics_50 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_50.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_50.value = u'0'
    shipBuilder_vehicleitemavionics_50 = importer.save_or_locate(shipBuilder_vehicleitemavionics_50)

    shipBuilder_vehicleitemavionics_51 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_51.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_51.value = u'20'
    shipBuilder_vehicleitemavionics_51 = importer.save_or_locate(shipBuilder_vehicleitemavionics_51)

    shipBuilder_vehicleitemavionics_52 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_52.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_52.value = u'0'
    shipBuilder_vehicleitemavionics_52 = importer.save_or_locate(shipBuilder_vehicleitemavionics_52)

    #Processing model: VehicleItem

    from shipBuilder.models import VehicleItem

    shipBuilder_vehicleitem_1 = VehicleItem()
    shipBuilder_vehicleitem_1.itemClass = 0L
    shipBuilder_vehicleitem_1.description = u'Designed exclusively for the Hornet F7C, the Stor-All Big Box model H replaces the void left by the turret system of the military-spec craft with a respectable cargo hold. Transforming the flagship fighter of the UEEN into a durable hauling ship.'
    shipBuilder_vehicleitem_1.name = u'Stor-All_Big_Box_Model_H'
    shipBuilder_vehicleitem_1.displayName = u'Stor-All Big Box Model H'
    shipBuilder_vehicleitem_1.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_1.itemSubType = shipBuilder_vehicleitemsubtype_1
    shipBuilder_vehicleitem_1.manufacturer = shipBuilder_manufacturer_24
    shipBuilder_vehicleitem_1.itemSize = 4L
    shipBuilder_vehicleitem_1.views = 1L
    shipBuilder_vehicleitem_1 = importer.save_or_locate(shipBuilder_vehicleitem_1)

    shipBuilder_vehicleitem_2 = VehicleItem()
    shipBuilder_vehicleitem_2.itemClass = 0L
    shipBuilder_vehicleitem_2.description = u'The 5 ton Stor-All Mini cargo pod allows the enterprising Aurora pilot to begin his business in the commodities transportation sector. It has a double wall and pressurized construction that can withstand the rigors of space or the occasional laser blast.'
    shipBuilder_vehicleitem_2.name = u'Stor-All_Mini'
    shipBuilder_vehicleitem_2.displayName = u'Stor-All Mini'
    shipBuilder_vehicleitem_2.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_2.itemSubType = shipBuilder_vehicleitemsubtype_1
    shipBuilder_vehicleitem_2.manufacturer = shipBuilder_manufacturer_24
    shipBuilder_vehicleitem_2.itemSize = 4L
    shipBuilder_vehicleitem_2.views = 0L
    shipBuilder_vehicleitem_2 = importer.save_or_locate(shipBuilder_vehicleitem_2)

    shipBuilder_vehicleitem_3 = VehicleItem()
    shipBuilder_vehicleitem_3.itemClass = 1L
    shipBuilder_vehicleitem_3.description = u"The Omnisky III is the base model in A&R's line of laser cannons for small ships and has a comparable rate of fire, damage output and range to other weapons in its size class. It uses mid-grade components in its design, offering a marked increase in power efficiency over some of its less expensive competitors."
    shipBuilder_vehicleitem_3.name = u'Omnisky_III_Laser'
    shipBuilder_vehicleitem_3.displayName = u'Omnisky III Laser Cannon'
    shipBuilder_vehicleitem_3.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_3.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_3.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_3.itemSize = 1L
    shipBuilder_vehicleitem_3.views = 0L
    shipBuilder_vehicleitem_3 = importer.save_or_locate(shipBuilder_vehicleitem_3)

    shipBuilder_vehicleitem_3.power.add(shipBuilder_vehicleitempower_1)
    shipBuilder_vehicleitem_3.power.add(shipBuilder_vehicleitempower_2)
    shipBuilder_vehicleitem_3.power.add(shipBuilder_vehicleitempower_3)
    shipBuilder_vehicleitem_3.heat.add(shipBuilder_vehicleitemheat_1)
    shipBuilder_vehicleitem_3.heat.add(shipBuilder_vehicleitemheat_2)
    shipBuilder_vehicleitem_3.heat.add(shipBuilder_vehicleitemheat_3)
    shipBuilder_vehicleitem_3.avionics.add(shipBuilder_vehicleitemavionics_1)
    shipBuilder_vehicleitem_3.avionics.add(shipBuilder_vehicleitemavionics_2)

    shipBuilder_vehicleitem_4 = VehicleItem()
    shipBuilder_vehicleitem_4.itemClass = 0L
    shipBuilder_vehicleitem_4.description = u''
    shipBuilder_vehicleitem_4.name = u'Aegis_TR4_Vector_Thruster'
    shipBuilder_vehicleitem_4.displayName = u'Aegis TR4 Vector Thruster'
    shipBuilder_vehicleitem_4.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_4.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_4.manufacturer = shipBuilder_manufacturer_37
    shipBuilder_vehicleitem_4.itemSize = 4L
    shipBuilder_vehicleitem_4.views = 0L
    shipBuilder_vehicleitem_4 = importer.save_or_locate(shipBuilder_vehicleitem_4)

    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_1)
    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_2)
    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_3)
    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_4)
    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_5)
    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_6)
    shipBuilder_vehicleitem_4.itemStats.add(shipBuilder_vehicleitemparams_7)

    shipBuilder_vehicleitem_5 = VehicleItem()
    shipBuilder_vehicleitem_5.itemClass = 0L
    shipBuilder_vehicleitem_5.description = u''
    shipBuilder_vehicleitem_5.name = u'MissileTurret'
    shipBuilder_vehicleitem_5.displayName = u''
    shipBuilder_vehicleitem_5.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_5.itemSubType = shipBuilder_vehicleitemsubtype_4
    shipBuilder_vehicleitem_5.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_5.itemSize = 2L
    shipBuilder_vehicleitem_5.views = 0L
    shipBuilder_vehicleitem_5 = importer.save_or_locate(shipBuilder_vehicleitem_5)

    shipBuilder_vehicleitem_6 = VehicleItem()
    shipBuilder_vehicleitem_6.itemClass = 0L
    shipBuilder_vehicleitem_6.description = u"Designed as an competitor to Lightning Power's Powerbolt, the 6HE8A manages to achieve an even smaller EM signature by utilizing a new Helium 6 sonoluminescent process. The 6HE8A's applications for covert flight make it the ideal power plant for pilots who wish to be shadows in space."
    shipBuilder_vehicleitem_6.name = u'Sakura_Sun_Light_Blossom_6HE8A'
    shipBuilder_vehicleitem_6.displayName = u'Sakura Sun Light Blossom 6HE8A'
    shipBuilder_vehicleitem_6.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_6.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_6.manufacturer = shipBuilder_manufacturer_39
    shipBuilder_vehicleitem_6.itemSize = 2L
    shipBuilder_vehicleitem_6.views = 0L
    shipBuilder_vehicleitem_6 = importer.save_or_locate(shipBuilder_vehicleitem_6)

    shipBuilder_vehicleitem_6.power.add(shipBuilder_vehicleitempower_4)

    shipBuilder_vehicleitem_7 = VehicleItem()
    shipBuilder_vehicleitem_7.itemClass = 3L
    shipBuilder_vehicleitem_7.description = u"The Behring Marksman heat seeking missile utilizes an enemy's heat signature to obtain and maintain a lock on the target. This tried-and-true method of target acquisition has a few drawbacks: it is easily confused by flares and it may be difficult to establish lock on ships with low heat signatures. These issues aside, the Marksman is the go-to missile of choice for many independent operators and pilots. Rack of four (4)."
    shipBuilder_vehicleitem_7.name = u'Behring_Marksman_HS_Platform_x4'
    shipBuilder_vehicleitem_7.displayName = u'Behring Marksman HS Quad Platform'
    shipBuilder_vehicleitem_7.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_7.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_7.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_7.itemSize = 2L
    shipBuilder_vehicleitem_7.views = 1L
    shipBuilder_vehicleitem_7 = importer.save_or_locate(shipBuilder_vehicleitem_7)

    shipBuilder_vehicleitem_7.power.add(shipBuilder_vehicleitempower_5)
    shipBuilder_vehicleitem_7.power.add(shipBuilder_vehicleitempower_6)
    shipBuilder_vehicleitem_7.power.add(shipBuilder_vehicleitempower_7)
    shipBuilder_vehicleitem_7.heat.add(shipBuilder_vehicleitemheat_4)
    shipBuilder_vehicleitem_7.heat.add(shipBuilder_vehicleitemheat_5)
    shipBuilder_vehicleitem_7.heat.add(shipBuilder_vehicleitemheat_6)
    shipBuilder_vehicleitem_7.avionics.add(shipBuilder_vehicleitemavionics_3)
    shipBuilder_vehicleitem_7.avionics.add(shipBuilder_vehicleitemavionics_4)
    shipBuilder_vehicleitem_7.itemStats.add(shipBuilder_vehicleitemparams_8)
    shipBuilder_vehicleitem_7.itemStats.add(shipBuilder_vehicleitemparams_9)
    shipBuilder_vehicleitem_7.itemStats.add(shipBuilder_vehicleitemparams_10)
    shipBuilder_vehicleitem_7.itemStats.add(shipBuilder_vehicleitemparams_11)

    shipBuilder_vehicleitem_8 = VehicleItem()
    shipBuilder_vehicleitem_8.itemClass = 0L
    shipBuilder_vehicleitem_8.description = u"The K3S-9 introduces the tried-and-true KS line of power plants to commercial-class ships, offering the same reliability and dependability for those long hauls through the black. The K3S-9's Chromodyanmic Assembler system will keep your systems online through thick and thin."
    shipBuilder_vehicleitem_8.name = u'Alliance_Startech_K3S-9'
    shipBuilder_vehicleitem_8.displayName = u'Alliance Startech K3S-9'
    shipBuilder_vehicleitem_8.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_8.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_8.manufacturer = shipBuilder_manufacturer_14
    shipBuilder_vehicleitem_8.itemSize = 3L
    shipBuilder_vehicleitem_8.views = 0L
    shipBuilder_vehicleitem_8 = importer.save_or_locate(shipBuilder_vehicleitem_8)

    shipBuilder_vehicleitem_8.power.add(shipBuilder_vehicleitempower_8)

    shipBuilder_vehicleitem_9 = VehicleItem()
    shipBuilder_vehicleitem_9.itemClass = 0L
    shipBuilder_vehicleitem_9.description = u''
    shipBuilder_vehicleitem_9.name = u'RSI_MissileBay'
    shipBuilder_vehicleitem_9.displayName = u'Missile Bay'
    shipBuilder_vehicleitem_9.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_9.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_9.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_9.itemSize = 2L
    shipBuilder_vehicleitem_9.views = 0L
    shipBuilder_vehicleitem_9 = importer.save_or_locate(shipBuilder_vehicleitem_9)

    shipBuilder_vehicleitem_9.power.add(shipBuilder_vehicleitempower_9)
    shipBuilder_vehicleitem_9.power.add(shipBuilder_vehicleitempower_10)
    shipBuilder_vehicleitem_9.power.add(shipBuilder_vehicleitempower_11)
    shipBuilder_vehicleitem_9.heat.add(shipBuilder_vehicleitemheat_7)
    shipBuilder_vehicleitem_9.heat.add(shipBuilder_vehicleitemheat_8)
    shipBuilder_vehicleitem_9.heat.add(shipBuilder_vehicleitemheat_9)
    shipBuilder_vehicleitem_9.avionics.add(shipBuilder_vehicleitemavionics_5)
    shipBuilder_vehicleitem_9.avionics.add(shipBuilder_vehicleitemavionics_6)

    shipBuilder_vehicleitem_10 = VehicleItem()
    shipBuilder_vehicleitem_10.itemClass = 0L
    shipBuilder_vehicleitem_10.description = u''
    shipBuilder_vehicleitem_10.name = u'OJ_Scalpel_Precision_Thruster_TR2'
    shipBuilder_vehicleitem_10.displayName = u'Origin Scalpel Precision Thruster'
    shipBuilder_vehicleitem_10.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_10.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_10.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_vehicleitem_10.itemSize = 1L
    shipBuilder_vehicleitem_10.views = 0L
    shipBuilder_vehicleitem_10 = importer.save_or_locate(shipBuilder_vehicleitem_10)

    shipBuilder_vehicleitem_10.itemStats.add(shipBuilder_vehicleitemparams_12)
    shipBuilder_vehicleitem_10.itemStats.add(shipBuilder_vehicleitemparams_13)
    shipBuilder_vehicleitem_10.itemStats.add(shipBuilder_vehicleitemparams_14)
    shipBuilder_vehicleitem_10.itemStats.add(shipBuilder_vehicleitemparams_15)
    shipBuilder_vehicleitem_10.itemStats.add(shipBuilder_vehicleitemparams_16)

    shipBuilder_vehicleitem_11 = VehicleItem()
    shipBuilder_vehicleitem_11.itemClass = 0L
    shipBuilder_vehicleitem_11.description = u'Featuring a three-barrel sequential fire design, the Klaus & Werner CF-007 Bulldog repeater is capable of high rates of fire while maintaining accuracy. It has low damage per projectile and, although it has relatively low power consumption over-all, several publications have commented on its somewhat lackluster efficiency. Even so, the CF-007 remains a favorite among new pilots who are outfitting their first ship.'
    shipBuilder_vehicleitem_11.name = u'K_W_CF_007_Bulldog_Laser_Repeater_Turret'
    shipBuilder_vehicleitem_11.displayName = u'007 Bulldog Laser Repeater Turret'
    shipBuilder_vehicleitem_11.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_11.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_11.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_11.itemSize = 2L
    shipBuilder_vehicleitem_11.views = 0L
    shipBuilder_vehicleitem_11 = importer.save_or_locate(shipBuilder_vehicleitem_11)

    shipBuilder_vehicleitem_11.power.add(shipBuilder_vehicleitempower_12)
    shipBuilder_vehicleitem_11.power.add(shipBuilder_vehicleitempower_13)
    shipBuilder_vehicleitem_11.power.add(shipBuilder_vehicleitempower_14)
    shipBuilder_vehicleitem_11.heat.add(shipBuilder_vehicleitemheat_10)
    shipBuilder_vehicleitem_11.heat.add(shipBuilder_vehicleitemheat_11)
    shipBuilder_vehicleitem_11.heat.add(shipBuilder_vehicleitemheat_12)
    shipBuilder_vehicleitem_11.avionics.add(shipBuilder_vehicleitemavionics_7)
    shipBuilder_vehicleitem_11.avionics.add(shipBuilder_vehicleitemavionics_8)

    shipBuilder_vehicleitem_12 = VehicleItem()
    shipBuilder_vehicleitem_12.itemClass = 3L
    shipBuilder_vehicleitem_12.description = u'Talon Stalker missiles track and lock their target by use of highly sensitive optical cameras and image processing software. Although they have an increased lock time over other missile types, they are much more difficult for targets to shake once lock is attained. Rack of two (2).'
    shipBuilder_vehicleitem_12.name = u'Talon_Stalker_Twin'
    shipBuilder_vehicleitem_12.displayName = u'Talon Stalker Twin Rack'
    shipBuilder_vehicleitem_12.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_12.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_12.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_vehicleitem_12.itemSize = 3L
    shipBuilder_vehicleitem_12.views = 0L
    shipBuilder_vehicleitem_12 = importer.save_or_locate(shipBuilder_vehicleitem_12)

    shipBuilder_vehicleitem_12.power.add(shipBuilder_vehicleitempower_15)
    shipBuilder_vehicleitem_12.power.add(shipBuilder_vehicleitempower_16)
    shipBuilder_vehicleitem_12.power.add(shipBuilder_vehicleitempower_17)
    shipBuilder_vehicleitem_12.heat.add(shipBuilder_vehicleitemheat_13)
    shipBuilder_vehicleitem_12.heat.add(shipBuilder_vehicleitemheat_14)
    shipBuilder_vehicleitem_12.heat.add(shipBuilder_vehicleitemheat_15)
    shipBuilder_vehicleitem_12.avionics.add(shipBuilder_vehicleitemavionics_9)
    shipBuilder_vehicleitem_12.avionics.add(shipBuilder_vehicleitemavionics_10)
    shipBuilder_vehicleitem_12.itemStats.add(shipBuilder_vehicleitemparams_17)
    shipBuilder_vehicleitem_12.itemStats.add(shipBuilder_vehicleitemparams_18)
    shipBuilder_vehicleitem_12.itemStats.add(shipBuilder_vehicleitemparams_19)
    shipBuilder_vehicleitem_12.itemStats.add(shipBuilder_vehicleitemparams_20)

    shipBuilder_vehicleitem_13 = VehicleItem()
    shipBuilder_vehicleitem_13.itemClass = 0L
    shipBuilder_vehicleitem_13.description = u''
    shipBuilder_vehicleitem_13.name = u'RSI_DefaultRadarMidRange'
    shipBuilder_vehicleitem_13.displayName = u'RSI Radar Mid Range'
    shipBuilder_vehicleitem_13.itemType = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitem_13.itemSubType = shipBuilder_vehicleitemsubtype_9
    shipBuilder_vehicleitem_13.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_13.itemSize = 1L
    shipBuilder_vehicleitem_13.views = 0L
    shipBuilder_vehicleitem_13 = importer.save_or_locate(shipBuilder_vehicleitem_13)

    shipBuilder_vehicleitem_13.itemStats.add(shipBuilder_vehicleitemparams_21)
    shipBuilder_vehicleitem_13.itemStats.add(shipBuilder_vehicleitemparams_22)
    shipBuilder_vehicleitem_13.itemStats.add(shipBuilder_vehicleitemparams_23)
    shipBuilder_vehicleitem_13.itemStats.add(shipBuilder_vehicleitemparams_24)
    shipBuilder_vehicleitem_13.itemStats.add(shipBuilder_vehicleitemparams_25)

    shipBuilder_vehicleitem_14 = VehicleItem()
    shipBuilder_vehicleitem_14.itemClass = 1L
    shipBuilder_vehicleitem_14.description = u"The M3A is Behring's entry level laser cannon. The cannon configuration offers modest damage per projectile and a fairly low rate of fire. As the most basic offering in Behring's weapons lineup, it features low power consumption, but poor power efficiency. It makes up ground for its shortcomings by being cheap, a feature many pilots are looking for when outfitting their ships on a budget."
    shipBuilder_vehicleitem_14.name = u'Behring_M3A_Laser'
    shipBuilder_vehicleitem_14.displayName = u'Behring M3A Laser'
    shipBuilder_vehicleitem_14.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_14.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_14.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_14.itemSize = 1L
    shipBuilder_vehicleitem_14.views = 2L
    shipBuilder_vehicleitem_14 = importer.save_or_locate(shipBuilder_vehicleitem_14)

    shipBuilder_vehicleitem_14.power.add(shipBuilder_vehicleitempower_18)
    shipBuilder_vehicleitem_14.power.add(shipBuilder_vehicleitempower_19)
    shipBuilder_vehicleitem_14.power.add(shipBuilder_vehicleitempower_20)
    shipBuilder_vehicleitem_14.heat.add(shipBuilder_vehicleitemheat_16)
    shipBuilder_vehicleitem_14.heat.add(shipBuilder_vehicleitemheat_17)
    shipBuilder_vehicleitem_14.heat.add(shipBuilder_vehicleitemheat_18)
    shipBuilder_vehicleitem_14.avionics.add(shipBuilder_vehicleitemavionics_11)
    shipBuilder_vehicleitem_14.avionics.add(shipBuilder_vehicleitemavionics_12)
    shipBuilder_vehicleitem_14.itemStats.add(shipBuilder_vehicleitemparams_26)
    shipBuilder_vehicleitem_14.itemStats.add(shipBuilder_vehicleitemparams_27)
    shipBuilder_vehicleitem_14.itemStats.add(shipBuilder_vehicleitemparams_28)
    shipBuilder_vehicleitem_14.itemStats.add(shipBuilder_vehicleitemparams_29)

    shipBuilder_vehicleitem_15 = VehicleItem()
    shipBuilder_vehicleitem_15.itemClass = 0L
    shipBuilder_vehicleitem_15.description = u''
    shipBuilder_vehicleitem_15.name = u'OJ_Omni_Precison_Thruster_TR2'
    shipBuilder_vehicleitem_15.displayName = u'Origin Omni Precision Ball Thruster'
    shipBuilder_vehicleitem_15.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_15.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_15.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_vehicleitem_15.itemSize = 1L
    shipBuilder_vehicleitem_15.views = 0L
    shipBuilder_vehicleitem_15 = importer.save_or_locate(shipBuilder_vehicleitem_15)

    shipBuilder_vehicleitem_15.itemStats.add(shipBuilder_vehicleitemparams_30)
    shipBuilder_vehicleitem_15.itemStats.add(shipBuilder_vehicleitemparams_31)
    shipBuilder_vehicleitem_15.itemStats.add(shipBuilder_vehicleitemparams_32)
    shipBuilder_vehicleitem_15.itemStats.add(shipBuilder_vehicleitemparams_33)
    shipBuilder_vehicleitem_15.itemStats.add(shipBuilder_vehicleitemparams_34)

    shipBuilder_vehicleitem_16 = VehicleItem()
    shipBuilder_vehicleitem_16.itemClass = 0L
    shipBuilder_vehicleitem_16.description = u''
    shipBuilder_vehicleitem_16.name = u'KDK_TM-4_Slider'
    shipBuilder_vehicleitem_16.displayName = u'KDK TM-4 Slider Thruster'
    shipBuilder_vehicleitem_16.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_16.itemSubType = shipBuilder_vehicleitemsubtype_10
    shipBuilder_vehicleitem_16.manufacturer = shipBuilder_manufacturer_40
    shipBuilder_vehicleitem_16.itemSize = 1L
    shipBuilder_vehicleitem_16.views = 0L
    shipBuilder_vehicleitem_16 = importer.save_or_locate(shipBuilder_vehicleitem_16)

    shipBuilder_vehicleitem_16.itemStats.add(shipBuilder_vehicleitemparams_35)
    shipBuilder_vehicleitem_16.itemStats.add(shipBuilder_vehicleitemparams_36)
    shipBuilder_vehicleitem_16.itemStats.add(shipBuilder_vehicleitemparams_37)
    shipBuilder_vehicleitem_16.itemStats.add(shipBuilder_vehicleitemparams_38)
    shipBuilder_vehicleitem_16.itemStats.add(shipBuilder_vehicleitemparams_39)

    shipBuilder_vehicleitem_17 = VehicleItem()
    shipBuilder_vehicleitem_17.itemClass = 0L
    shipBuilder_vehicleitem_17.description = u"The KS-9 Enhanced features the same dependable construction of the KS-9 but with a series of higher quality parts compliments of the Alliance Startech's Commercial Development Division in Terra."
    shipBuilder_vehicleitem_17.name = u'Alliance_Startech_KS-9_Enhanced'
    shipBuilder_vehicleitem_17.displayName = u'Alliance Startech KS-9 Enhanced'
    shipBuilder_vehicleitem_17.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_17.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_17.manufacturer = shipBuilder_manufacturer_14
    shipBuilder_vehicleitem_17.itemSize = 1L
    shipBuilder_vehicleitem_17.views = 0L
    shipBuilder_vehicleitem_17 = importer.save_or_locate(shipBuilder_vehicleitem_17)

    shipBuilder_vehicleitem_17.power.add(shipBuilder_vehicleitempower_21)

    shipBuilder_vehicleitem_18 = VehicleItem()
    shipBuilder_vehicleitem_18.itemClass = 1L
    shipBuilder_vehicleitem_18.description = u'The Omnisky VI is the mid-sized laser cannon from manufacturer A&R. It boasts increased damage and range and power consumption over its smaller brother, the Omnisky III, and utilizes many of the same components resulting in middle-of-the-road power efficiency.'
    shipBuilder_vehicleitem_18.name = u'Omnisky_VI_Laser'
    shipBuilder_vehicleitem_18.displayName = u'Omnisky VI Laser Cannon'
    shipBuilder_vehicleitem_18.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_18.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_18.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_18.itemSize = 2L
    shipBuilder_vehicleitem_18.views = 0L
    shipBuilder_vehicleitem_18 = importer.save_or_locate(shipBuilder_vehicleitem_18)

    shipBuilder_vehicleitem_18.power.add(shipBuilder_vehicleitempower_22)
    shipBuilder_vehicleitem_18.power.add(shipBuilder_vehicleitempower_23)
    shipBuilder_vehicleitem_18.power.add(shipBuilder_vehicleitempower_24)
    shipBuilder_vehicleitem_18.heat.add(shipBuilder_vehicleitemheat_19)
    shipBuilder_vehicleitem_18.heat.add(shipBuilder_vehicleitemheat_20)
    shipBuilder_vehicleitem_18.heat.add(shipBuilder_vehicleitemheat_21)
    shipBuilder_vehicleitem_18.avionics.add(shipBuilder_vehicleitemavionics_13)
    shipBuilder_vehicleitem_18.avionics.add(shipBuilder_vehicleitemavionics_14)
    shipBuilder_vehicleitem_18.itemStats.add(shipBuilder_vehicleitemparams_40)
    shipBuilder_vehicleitem_18.itemStats.add(shipBuilder_vehicleitemparams_41)
    shipBuilder_vehicleitem_18.itemStats.add(shipBuilder_vehicleitemparams_42)
    shipBuilder_vehicleitem_18.itemStats.add(shipBuilder_vehicleitemparams_43)

    shipBuilder_vehicleitem_19 = VehicleItem()
    shipBuilder_vehicleitem_19.itemClass = 0L
    shipBuilder_vehicleitem_19.description = u"Hammer Propulsion's HE 5.5 offers the same high quality, high output design that you find in the 5.3 but amplified to handle larger class vessels. the 5.5 is one of the most durable and robust thrusters on the market for commercial and shipping vehicles."
    shipBuilder_vehicleitem_19.name = u'Hammer_Propulsion_HE_5_5'
    shipBuilder_vehicleitem_19.displayName = u'Hammer Propulsion HE 5.5'
    shipBuilder_vehicleitem_19.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_19.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_19.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_19.itemSize = 5L
    shipBuilder_vehicleitem_19.views = 0L
    shipBuilder_vehicleitem_19 = importer.save_or_locate(shipBuilder_vehicleitem_19)

    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_44)
    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_45)
    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_46)
    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_47)
    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_48)
    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_49)
    shipBuilder_vehicleitem_19.itemStats.add(shipBuilder_vehicleitemparams_50)

    shipBuilder_vehicleitem_20 = VehicleItem()
    shipBuilder_vehicleitem_20.itemClass = 0L
    shipBuilder_vehicleitem_20.description = u'The Endurance-300 from Juno Starwerk utilizes a VHTR (very high temperature reactor) and is a solid choice for Aurora pilots operating in tough environments. Although based on somewhat antiquated fission technology resulting in slightly lower power output and increased signature, the extra insulation required in its construction has the added benefit of making the Endurance-300 a very damage-resilient power source.'
    shipBuilder_vehicleitem_20.name = u'Juno_Starwerk_Endurance-300'
    shipBuilder_vehicleitem_20.displayName = u'Juno Starwerk Endurance-300'
    shipBuilder_vehicleitem_20.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_20.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_20.manufacturer = shipBuilder_manufacturer_15
    shipBuilder_vehicleitem_20.itemSize = 1L
    shipBuilder_vehicleitem_20.views = 0L
    shipBuilder_vehicleitem_20 = importer.save_or_locate(shipBuilder_vehicleitem_20)

    shipBuilder_vehicleitem_20.power.add(shipBuilder_vehicleitempower_25)

    shipBuilder_vehicleitem_21 = VehicleItem()
    shipBuilder_vehicleitem_21.itemClass = 1L
    shipBuilder_vehicleitem_21.description = u'Featuring a three-barrel sequential fire design, the Klaus & Werner CF-007 Bulldog repeater is capable of high rates of fire while maintaining accuracy. It has low damage per projectile and, although it has relatively low power consumption over-all, several publications have commented on its somewhat lackluster efficiency. Even so, the CF-007 remains a favorite among new pilots who are outfitting their first ship.'
    shipBuilder_vehicleitem_21.name = u'K_and_W_CF-007_Bulldog_Repeater'
    shipBuilder_vehicleitem_21.displayName = u'CF-007 Bulldog Repeater'
    shipBuilder_vehicleitem_21.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_21.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_21.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_21.itemSize = 1L
    shipBuilder_vehicleitem_21.views = 0L
    shipBuilder_vehicleitem_21 = importer.save_or_locate(shipBuilder_vehicleitem_21)

    shipBuilder_vehicleitem_21.power.add(shipBuilder_vehicleitempower_26)
    shipBuilder_vehicleitem_21.power.add(shipBuilder_vehicleitempower_27)
    shipBuilder_vehicleitem_21.power.add(shipBuilder_vehicleitempower_28)
    shipBuilder_vehicleitem_21.heat.add(shipBuilder_vehicleitemheat_22)
    shipBuilder_vehicleitem_21.heat.add(shipBuilder_vehicleitemheat_23)
    shipBuilder_vehicleitem_21.heat.add(shipBuilder_vehicleitemheat_24)
    shipBuilder_vehicleitem_21.avionics.add(shipBuilder_vehicleitemavionics_15)
    shipBuilder_vehicleitem_21.avionics.add(shipBuilder_vehicleitemavionics_16)
    shipBuilder_vehicleitem_21.itemStats.add(shipBuilder_vehicleitemparams_51)
    shipBuilder_vehicleitem_21.itemStats.add(shipBuilder_vehicleitemparams_52)
    shipBuilder_vehicleitem_21.itemStats.add(shipBuilder_vehicleitemparams_53)
    shipBuilder_vehicleitem_21.itemStats.add(shipBuilder_vehicleitemparams_54)

    shipBuilder_vehicleitem_22 = VehicleItem()
    shipBuilder_vehicleitem_22.itemClass = 0L
    shipBuilder_vehicleitem_22.description = u"The Dragon Stellar STC Red is a great choice for pilots of small ships. Despite its lack of fuel and power efficiency it boasts a respectable thrust output that really shines on low mass ships such as the Aurora. As an added benefit, Dragon Stellear recently developed new technology that reduces the output signature, great for pilots who don't wish to call a lot of attention to themselves. Its thrust rating of 3 gives it more thrust than the Blue, at the cost of higher power consumption and signature."
    shipBuilder_vehicleitem_22.name = u'Dragon_STC_Red'
    shipBuilder_vehicleitem_22.displayName = u'Dragon STC Red Main Engine'
    shipBuilder_vehicleitem_22.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_22.itemSubType = shipBuilder_vehicleitemsubtype_11
    shipBuilder_vehicleitem_22.manufacturer = shipBuilder_manufacturer_41
    shipBuilder_vehicleitem_22.itemSize = 3L
    shipBuilder_vehicleitem_22.views = 0L
    shipBuilder_vehicleitem_22 = importer.save_or_locate(shipBuilder_vehicleitem_22)

    shipBuilder_vehicleitem_22.itemStats.add(shipBuilder_vehicleitemparams_55)
    shipBuilder_vehicleitem_22.itemStats.add(shipBuilder_vehicleitemparams_56)
    shipBuilder_vehicleitem_22.itemStats.add(shipBuilder_vehicleitemparams_57)

    shipBuilder_vehicleitem_23 = VehicleItem()
    shipBuilder_vehicleitem_23.itemClass = 3L
    shipBuilder_vehicleitem_23.description = u"In the thin market of FF missiles, the Dominator is one of the few stand-outs. With Talon's state-of-the-art target recognition system, these missiles are ideal for mixing it up with large numbers of ships. Varying sizes available."
    shipBuilder_vehicleitem_23.name = u'Talon_Dominator_Platform_x4'
    shipBuilder_vehicleitem_23.displayName = u'Talon Dominator FF Quad'
    shipBuilder_vehicleitem_23.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_23.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_23.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_vehicleitem_23.itemSize = 3L
    shipBuilder_vehicleitem_23.views = 0L
    shipBuilder_vehicleitem_23 = importer.save_or_locate(shipBuilder_vehicleitem_23)

    shipBuilder_vehicleitem_23.power.add(shipBuilder_vehicleitempower_29)
    shipBuilder_vehicleitem_23.power.add(shipBuilder_vehicleitempower_30)
    shipBuilder_vehicleitem_23.power.add(shipBuilder_vehicleitempower_31)
    shipBuilder_vehicleitem_23.heat.add(shipBuilder_vehicleitemheat_25)
    shipBuilder_vehicleitem_23.heat.add(shipBuilder_vehicleitemheat_26)
    shipBuilder_vehicleitem_23.heat.add(shipBuilder_vehicleitemheat_27)
    shipBuilder_vehicleitem_23.avionics.add(shipBuilder_vehicleitemavionics_17)
    shipBuilder_vehicleitem_23.avionics.add(shipBuilder_vehicleitemavionics_18)
    shipBuilder_vehicleitem_23.itemStats.add(shipBuilder_vehicleitemparams_58)
    shipBuilder_vehicleitem_23.itemStats.add(shipBuilder_vehicleitemparams_59)
    shipBuilder_vehicleitem_23.itemStats.add(shipBuilder_vehicleitemparams_60)
    shipBuilder_vehicleitem_23.itemStats.add(shipBuilder_vehicleitemparams_61)

    shipBuilder_vehicleitem_24 = VehicleItem()
    shipBuilder_vehicleitem_24.itemClass = 0L
    shipBuilder_vehicleitem_24.description = u''
    shipBuilder_vehicleitem_24.name = u'AATurret'
    shipBuilder_vehicleitem_24.displayName = u''
    shipBuilder_vehicleitem_24.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_24.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_24.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_24.itemSize = 2L
    shipBuilder_vehicleitem_24.views = 1L
    shipBuilder_vehicleitem_24 = importer.save_or_locate(shipBuilder_vehicleitem_24)

    shipBuilder_vehicleitem_25 = VehicleItem()
    shipBuilder_vehicleitem_25.itemClass = 0L
    shipBuilder_vehicleitem_25.description = u'The STC Silver from Dragon Stellar Transit Company is a TR4 engine noted for its high thrust ouput and low EM emissions. It has been rumored that Dragon Stellar has been using inferior components, but for some pilots the decreased power and fuel efficiency is worth the extra boost, especially at this price point.'
    shipBuilder_vehicleitem_25.name = u'Dragon_STC_Silver'
    shipBuilder_vehicleitem_25.displayName = u'Dragon STC Silver Main Engine'
    shipBuilder_vehicleitem_25.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_25.itemSubType = shipBuilder_vehicleitemsubtype_11
    shipBuilder_vehicleitem_25.manufacturer = shipBuilder_manufacturer_41
    shipBuilder_vehicleitem_25.itemSize = 4L
    shipBuilder_vehicleitem_25.views = 0L
    shipBuilder_vehicleitem_25 = importer.save_or_locate(shipBuilder_vehicleitem_25)

    shipBuilder_vehicleitem_25.itemStats.add(shipBuilder_vehicleitemparams_62)
    shipBuilder_vehicleitem_25.itemStats.add(shipBuilder_vehicleitemparams_63)
    shipBuilder_vehicleitem_25.itemStats.add(shipBuilder_vehicleitemparams_64)

    shipBuilder_vehicleitem_26 = VehicleItem()
    shipBuilder_vehicleitem_26.itemClass = 0L
    shipBuilder_vehicleitem_26.description = u''
    shipBuilder_vehicleitem_26.name = u'Anvil_Flex_Thruster_TR2_Back_Left'
    shipBuilder_vehicleitem_26.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_26.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_26.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_26.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_26.itemSize = 2L
    shipBuilder_vehicleitem_26.views = 0L
    shipBuilder_vehicleitem_26 = importer.save_or_locate(shipBuilder_vehicleitem_26)

    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_65)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_66)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_67)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_68)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_69)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_70)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_71)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_72)
    shipBuilder_vehicleitem_26.itemStats.add(shipBuilder_vehicleitemparams_73)

    shipBuilder_vehicleitem_27 = VehicleItem()
    shipBuilder_vehicleitem_27.itemClass = 0L
    shipBuilder_vehicleitem_27.description = u"Wei-Tek's HFR2 Plus reactors are specially designed and optimized for medium sized craft. The hydrogen 6+ technology offers a robust power output but with a lower heat signature and higher durability."
    shipBuilder_vehicleitem_27.name = u'Wei_Tek_HFR2_Plus'
    shipBuilder_vehicleitem_27.displayName = u'Wei Tek HFR2 Plus'
    shipBuilder_vehicleitem_27.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_27.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_27.manufacturer = shipBuilder_manufacturer_12
    shipBuilder_vehicleitem_27.itemSize = 5L
    shipBuilder_vehicleitem_27.views = 0L
    shipBuilder_vehicleitem_27 = importer.save_or_locate(shipBuilder_vehicleitem_27)

    shipBuilder_vehicleitem_27.power.add(shipBuilder_vehicleitempower_32)

    shipBuilder_vehicleitem_28 = VehicleItem()
    shipBuilder_vehicleitem_28.itemClass = 3L
    shipBuilder_vehicleitem_28.description = u'Talon Stalker missiles track and lock their target by use of highly sensitive optical cameras and image processing software. Although they have an increased lock time over other missile types, they are much more difficult for targets to shake once lock is attained. Rack of four (4).'
    shipBuilder_vehicleitem_28.name = u'Talon_Stalker_Quad'
    shipBuilder_vehicleitem_28.displayName = u'Talon Stalker Quad Rack'
    shipBuilder_vehicleitem_28.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_28.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_28.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_vehicleitem_28.itemSize = 3L
    shipBuilder_vehicleitem_28.views = 0L
    shipBuilder_vehicleitem_28 = importer.save_or_locate(shipBuilder_vehicleitem_28)

    shipBuilder_vehicleitem_28.power.add(shipBuilder_vehicleitempower_33)
    shipBuilder_vehicleitem_28.power.add(shipBuilder_vehicleitempower_34)
    shipBuilder_vehicleitem_28.power.add(shipBuilder_vehicleitempower_35)
    shipBuilder_vehicleitem_28.heat.add(shipBuilder_vehicleitemheat_28)
    shipBuilder_vehicleitem_28.heat.add(shipBuilder_vehicleitemheat_29)
    shipBuilder_vehicleitem_28.heat.add(shipBuilder_vehicleitemheat_30)
    shipBuilder_vehicleitem_28.avionics.add(shipBuilder_vehicleitemavionics_19)
    shipBuilder_vehicleitem_28.avionics.add(shipBuilder_vehicleitemavionics_20)
    shipBuilder_vehicleitem_28.itemStats.add(shipBuilder_vehicleitemparams_74)
    shipBuilder_vehicleitem_28.itemStats.add(shipBuilder_vehicleitemparams_75)
    shipBuilder_vehicleitem_28.itemStats.add(shipBuilder_vehicleitemparams_76)
    shipBuilder_vehicleitem_28.itemStats.add(shipBuilder_vehicleitemparams_77)

    shipBuilder_vehicleitem_29 = VehicleItem()
    shipBuilder_vehicleitem_29.itemClass = 0L
    shipBuilder_vehicleitem_29.description = u''
    shipBuilder_vehicleitem_29.name = u'Anvil_Flex_MK2'
    shipBuilder_vehicleitem_29.displayName = u'Anvil MK2 Flex Thruster'
    shipBuilder_vehicleitem_29.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_29.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_29.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_29.itemSize = 2L
    shipBuilder_vehicleitem_29.views = 1L
    shipBuilder_vehicleitem_29 = importer.save_or_locate(shipBuilder_vehicleitem_29)

    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_78)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_79)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_80)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_81)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_82)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_83)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_84)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_85)
    shipBuilder_vehicleitem_29.itemStats.add(shipBuilder_vehicleitemparams_86)

    shipBuilder_vehicleitem_30 = VehicleItem()
    shipBuilder_vehicleitem_30.itemClass = 0L
    shipBuilder_vehicleitem_30.description = u'The Hammer Propulsion Twin HM4.3 is notable for the fact that it utilizes 2 high-performance TR3 thrusters in a small package. An unusual application, the original design was a joint collaboration between Hammer Propulsion and the Origin Jumpworks racing team. With the additional thrust provided by a second thruster the Twin HM4.3 is ideal for applications where speed is the goal. Speed comes at a cost, however; this configuration has a thirst for fuel that rivals much larger single thruster systems, and with all of its available space being taken up by the thruster internals not much space is left for durability reinforcement. This makes the HM4.3 ideal for most racing pilots, but less suitable for combat-oriented missions.'
    shipBuilder_vehicleitem_30.name = u'350r_Hammer_Propulsion_HE_4_3'
    shipBuilder_vehicleitem_30.displayName = u'Hammer Propulsion HM 4.3'
    shipBuilder_vehicleitem_30.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_30.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_30.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_30.itemSize = 3L
    shipBuilder_vehicleitem_30.views = 0L
    shipBuilder_vehicleitem_30 = importer.save_or_locate(shipBuilder_vehicleitem_30)

    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_87)
    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_88)
    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_89)
    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_90)
    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_91)
    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_92)
    shipBuilder_vehicleitem_30.itemStats.add(shipBuilder_vehicleitemparams_93)

    shipBuilder_vehicleitem_31 = VehicleItem()
    shipBuilder_vehicleitem_31.itemClass = 0L
    shipBuilder_vehicleitem_31.description = u''
    shipBuilder_vehicleitem_31.name = u'OKB_Energia_IV'
    shipBuilder_vehicleitem_31.displayName = u'OKB Voshkod Energia IV'
    shipBuilder_vehicleitem_31.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_31.itemSubType = shipBuilder_vehicleitemsubtype_11
    shipBuilder_vehicleitem_31.manufacturer = shipBuilder_manufacturer_20
    shipBuilder_vehicleitem_31.itemSize = 2L
    shipBuilder_vehicleitem_31.views = 0L
    shipBuilder_vehicleitem_31 = importer.save_or_locate(shipBuilder_vehicleitem_31)

    shipBuilder_vehicleitem_31.itemStats.add(shipBuilder_vehicleitemparams_94)
    shipBuilder_vehicleitem_31.itemStats.add(shipBuilder_vehicleitemparams_95)
    shipBuilder_vehicleitem_31.itemStats.add(shipBuilder_vehicleitemparams_96)

    shipBuilder_vehicleitem_32 = VehicleItem()
    shipBuilder_vehicleitem_32.itemClass = 0L
    shipBuilder_vehicleitem_32.description = u'The FusionPro 3H III is optimized for medium sized spacecraft. The 3H boasts the expected high durability and performance under fire while maintaining a robust energy output. The signature can run awfully hot.'
    shipBuilder_vehicleitem_32.name = u'Ace_Astrogation_FusionPro_3H_III'
    shipBuilder_vehicleitem_32.displayName = u'Ace Astrogation FusionPro 3H III'
    shipBuilder_vehicleitem_32.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_32.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_32.manufacturer = shipBuilder_manufacturer_16
    shipBuilder_vehicleitem_32.itemSize = 4L
    shipBuilder_vehicleitem_32.views = 0L
    shipBuilder_vehicleitem_32 = importer.save_or_locate(shipBuilder_vehicleitem_32)

    shipBuilder_vehicleitem_32.power.add(shipBuilder_vehicleitempower_36)

    shipBuilder_vehicleitem_33 = VehicleItem()
    shipBuilder_vehicleitem_33.itemClass = 0L
    shipBuilder_vehicleitem_33.description = u''
    shipBuilder_vehicleitem_33.name = u'RSI_DefaultWeaponDisplay'
    shipBuilder_vehicleitem_33.displayName = u'RSI Weapon Display'
    shipBuilder_vehicleitem_33.itemType = shipBuilder_vehicleitemtype_6
    shipBuilder_vehicleitem_33.itemSubType = shipBuilder_vehicleitemsubtype_12
    shipBuilder_vehicleitem_33.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_33.itemSize = 1L
    shipBuilder_vehicleitem_33.views = 0L
    shipBuilder_vehicleitem_33 = importer.save_or_locate(shipBuilder_vehicleitem_33)

    shipBuilder_vehicleitem_34 = VehicleItem()
    shipBuilder_vehicleitem_34.itemClass = 0L
    shipBuilder_vehicleitem_34.description = u''
    shipBuilder_vehicleitem_34.name = u'ScytheRightWingCannon'
    shipBuilder_vehicleitem_34.displayName = u''
    shipBuilder_vehicleitem_34.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_34.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_34.manufacturer = shipBuilder_manufacturer_42
    shipBuilder_vehicleitem_34.itemSize = 2L
    shipBuilder_vehicleitem_34.views = 0L
    shipBuilder_vehicleitem_34 = importer.save_or_locate(shipBuilder_vehicleitem_34)

    shipBuilder_vehicleitem_35 = VehicleItem()
    shipBuilder_vehicleitem_35.itemClass = 0L
    shipBuilder_vehicleitem_35.description = u"A heavier model than the Stinger. Sure, the VOLT Hellfire pulls more juice from your power plant and the rate of fire isn't as high, but that extra draw means a little more punch."
    shipBuilder_vehicleitem_35.name = u'Hellfire'
    shipBuilder_vehicleitem_35.displayName = u'Hellfire'
    shipBuilder_vehicleitem_35.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_35.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_35.manufacturer = shipBuilder_manufacturer_43
    shipBuilder_vehicleitem_35.itemSize = 1L
    shipBuilder_vehicleitem_35.views = 1L
    shipBuilder_vehicleitem_35 = importer.save_or_locate(shipBuilder_vehicleitem_35)

    shipBuilder_vehicleitem_35.power.add(shipBuilder_vehicleitempower_37)
    shipBuilder_vehicleitem_35.power.add(shipBuilder_vehicleitempower_38)
    shipBuilder_vehicleitem_35.power.add(shipBuilder_vehicleitempower_39)
    shipBuilder_vehicleitem_35.heat.add(shipBuilder_vehicleitemheat_31)
    shipBuilder_vehicleitem_35.heat.add(shipBuilder_vehicleitemheat_32)
    shipBuilder_vehicleitem_35.heat.add(shipBuilder_vehicleitemheat_33)
    shipBuilder_vehicleitem_35.avionics.add(shipBuilder_vehicleitemavionics_21)
    shipBuilder_vehicleitem_35.avionics.add(shipBuilder_vehicleitemavionics_22)

    shipBuilder_vehicleitem_36 = VehicleItem()
    shipBuilder_vehicleitem_36.itemClass = 3L
    shipBuilder_vehicleitem_36.description = u"The Behring Marksman heat seeking missile utilizes an enemy's heat signature to obtain and maintain a lock on the target. This tried-and-true method of target acquisition has a few drawbacks: it is easily confused by flares and it may be difficult to establish lock on ships with low heat signatures. These issues aside, the Marksman is the go-to missile of choice for many independent operators and pilots. Rack of four (4)."
    shipBuilder_vehicleitem_36.name = u'Behring_Marksman_Quad'
    shipBuilder_vehicleitem_36.displayName = u'Behring Marksman HS Quad Platform'
    shipBuilder_vehicleitem_36.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_36.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_36.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_36.itemSize = 2L
    shipBuilder_vehicleitem_36.views = 0L
    shipBuilder_vehicleitem_36 = importer.save_or_locate(shipBuilder_vehicleitem_36)

    shipBuilder_vehicleitem_36.power.add(shipBuilder_vehicleitempower_40)
    shipBuilder_vehicleitem_36.power.add(shipBuilder_vehicleitempower_41)
    shipBuilder_vehicleitem_36.power.add(shipBuilder_vehicleitempower_42)
    shipBuilder_vehicleitem_36.heat.add(shipBuilder_vehicleitemheat_34)
    shipBuilder_vehicleitem_36.heat.add(shipBuilder_vehicleitemheat_35)
    shipBuilder_vehicleitem_36.heat.add(shipBuilder_vehicleitemheat_36)
    shipBuilder_vehicleitem_36.avionics.add(shipBuilder_vehicleitemavionics_23)
    shipBuilder_vehicleitem_36.avionics.add(shipBuilder_vehicleitemavionics_24)
    shipBuilder_vehicleitem_36.itemStats.add(shipBuilder_vehicleitemparams_97)
    shipBuilder_vehicleitem_36.itemStats.add(shipBuilder_vehicleitemparams_98)
    shipBuilder_vehicleitem_36.itemStats.add(shipBuilder_vehicleitemparams_99)
    shipBuilder_vehicleitem_36.itemStats.add(shipBuilder_vehicleitemparams_100)

    shipBuilder_vehicleitem_37 = VehicleItem()
    shipBuilder_vehicleitem_37.itemClass = 0L
    shipBuilder_vehicleitem_37.description = u''
    shipBuilder_vehicleitem_37.name = u'Anvil_Flex_Thruster_TR2_Front_Right'
    shipBuilder_vehicleitem_37.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_37.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_37.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_37.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_37.itemSize = 2L
    shipBuilder_vehicleitem_37.views = 0L
    shipBuilder_vehicleitem_37 = importer.save_or_locate(shipBuilder_vehicleitem_37)

    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_101)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_102)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_103)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_104)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_105)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_106)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_107)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_108)
    shipBuilder_vehicleitem_37.itemStats.add(shipBuilder_vehicleitemparams_109)

    shipBuilder_vehicleitem_38 = VehicleItem()
    shipBuilder_vehicleitem_38.itemClass = 1L
    shipBuilder_vehicleitem_38.description = u'MaxOx\u2019s NN-13 Neutron Gun offers a massive energy payload at the expense of speed and energy efficiency. One could argue the virtues of speed, rate of fire and distance over damage, but the argument becomes irrelevant if you only need to hit them once.'
    shipBuilder_vehicleitem_38.name = u'Max_Ox_NN13_Neutron'
    shipBuilder_vehicleitem_38.displayName = u'MaxOx NN-13 Neutron Cannon'
    shipBuilder_vehicleitem_38.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_38.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_38.manufacturer = shipBuilder_manufacturer_30
    shipBuilder_vehicleitem_38.itemSize = 1L
    shipBuilder_vehicleitem_38.views = 0L
    shipBuilder_vehicleitem_38 = importer.save_or_locate(shipBuilder_vehicleitem_38)

    shipBuilder_vehicleitem_38.power.add(shipBuilder_vehicleitempower_43)
    shipBuilder_vehicleitem_38.power.add(shipBuilder_vehicleitempower_44)
    shipBuilder_vehicleitem_38.power.add(shipBuilder_vehicleitempower_45)
    shipBuilder_vehicleitem_38.heat.add(shipBuilder_vehicleitemheat_37)
    shipBuilder_vehicleitem_38.heat.add(shipBuilder_vehicleitemheat_38)
    shipBuilder_vehicleitem_38.heat.add(shipBuilder_vehicleitemheat_39)
    shipBuilder_vehicleitem_38.avionics.add(shipBuilder_vehicleitemavionics_25)
    shipBuilder_vehicleitem_38.avionics.add(shipBuilder_vehicleitemavionics_26)
    shipBuilder_vehicleitem_38.itemStats.add(shipBuilder_vehicleitemparams_110)
    shipBuilder_vehicleitem_38.itemStats.add(shipBuilder_vehicleitemparams_111)
    shipBuilder_vehicleitem_38.itemStats.add(shipBuilder_vehicleitemparams_112)
    shipBuilder_vehicleitem_38.itemStats.add(shipBuilder_vehicleitemparams_113)

    shipBuilder_vehicleitem_39 = VehicleItem()
    shipBuilder_vehicleitem_39.itemClass = 1L
    shipBuilder_vehicleitem_39.description = u"The K&W Mass Driver Cannon is a 35mm hard-ammo ballistic weapon capable of firing multiple types of ammunition. This weapon's increased shield penetration capabilities comes at a cost, however; magazine space is limited, and ammunition must be replenished regularly. Because it does not use energy-based projectiles, the K&W mass driver has a reduced power cost and therefore results in a reduced EM signature."
    shipBuilder_vehicleitem_39.name = u'K_and_W_Mass_Driver_Cannon'
    shipBuilder_vehicleitem_39.displayName = u'K and W Mass Driver Cannon'
    shipBuilder_vehicleitem_39.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_39.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_39.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_39.itemSize = 2L
    shipBuilder_vehicleitem_39.views = 0L
    shipBuilder_vehicleitem_39 = importer.save_or_locate(shipBuilder_vehicleitem_39)

    shipBuilder_vehicleitem_39.power.add(shipBuilder_vehicleitempower_46)
    shipBuilder_vehicleitem_39.power.add(shipBuilder_vehicleitempower_47)
    shipBuilder_vehicleitem_39.power.add(shipBuilder_vehicleitempower_48)
    shipBuilder_vehicleitem_39.heat.add(shipBuilder_vehicleitemheat_40)
    shipBuilder_vehicleitem_39.heat.add(shipBuilder_vehicleitemheat_41)
    shipBuilder_vehicleitem_39.heat.add(shipBuilder_vehicleitemheat_42)
    shipBuilder_vehicleitem_39.avionics.add(shipBuilder_vehicleitemavionics_27)
    shipBuilder_vehicleitem_39.avionics.add(shipBuilder_vehicleitemavionics_28)
    shipBuilder_vehicleitem_39.itemStats.add(shipBuilder_vehicleitemparams_114)
    shipBuilder_vehicleitem_39.itemStats.add(shipBuilder_vehicleitemparams_115)
    shipBuilder_vehicleitem_39.itemStats.add(shipBuilder_vehicleitemparams_116)
    shipBuilder_vehicleitem_39.itemStats.add(shipBuilder_vehicleitemparams_117)

    shipBuilder_vehicleitem_40 = VehicleItem()
    shipBuilder_vehicleitem_40.itemClass = 0L
    shipBuilder_vehicleitem_40.description = u''
    shipBuilder_vehicleitem_40.name = u'RSI_DefaultVisor'
    shipBuilder_vehicleitem_40.displayName = u'RSI Visor Display'
    shipBuilder_vehicleitem_40.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_40.itemSubType = shipBuilder_vehicleitemsubtype_13
    shipBuilder_vehicleitem_40.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_40.itemSize = 1L
    shipBuilder_vehicleitem_40.views = 0L
    shipBuilder_vehicleitem_40 = importer.save_or_locate(shipBuilder_vehicleitem_40)

    shipBuilder_vehicleitem_41 = VehicleItem()
    shipBuilder_vehicleitem_41.itemClass = 0L
    shipBuilder_vehicleitem_41.description = u"Strike fast and strike hard with the VOLT Stinger. Sure, each shot isn't much on its own, but what does that matter when they've got a dozen more friends a second?"
    shipBuilder_vehicleitem_41.name = u'Stinger'
    shipBuilder_vehicleitem_41.displayName = u'Stinger'
    shipBuilder_vehicleitem_41.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_41.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_41.manufacturer = shipBuilder_manufacturer_43
    shipBuilder_vehicleitem_41.itemSize = 1L
    shipBuilder_vehicleitem_41.views = 0L
    shipBuilder_vehicleitem_41 = importer.save_or_locate(shipBuilder_vehicleitem_41)

    shipBuilder_vehicleitem_41.power.add(shipBuilder_vehicleitempower_49)
    shipBuilder_vehicleitem_41.power.add(shipBuilder_vehicleitempower_50)
    shipBuilder_vehicleitem_41.power.add(shipBuilder_vehicleitempower_51)
    shipBuilder_vehicleitem_41.heat.add(shipBuilder_vehicleitemheat_43)
    shipBuilder_vehicleitem_41.heat.add(shipBuilder_vehicleitemheat_44)
    shipBuilder_vehicleitem_41.heat.add(shipBuilder_vehicleitemheat_45)
    shipBuilder_vehicleitem_41.avionics.add(shipBuilder_vehicleitemavionics_29)
    shipBuilder_vehicleitem_41.avionics.add(shipBuilder_vehicleitemavionics_30)

    shipBuilder_vehicleitem_42 = VehicleItem()
    shipBuilder_vehicleitem_42.itemClass = 0L
    shipBuilder_vehicleitem_42.description = u''
    shipBuilder_vehicleitem_42.name = u'RSI_DefaultCooler'
    shipBuilder_vehicleitem_42.displayName = u'RSI Heat Cooler'
    shipBuilder_vehicleitem_42.itemType = shipBuilder_vehicleitemtype_8
    shipBuilder_vehicleitem_42.itemSubType = shipBuilder_vehicleitemsubtype_14
    shipBuilder_vehicleitem_42.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_42.itemSize = 1L
    shipBuilder_vehicleitem_42.views = 0L
    shipBuilder_vehicleitem_42 = importer.save_or_locate(shipBuilder_vehicleitem_42)

    shipBuilder_vehicleitem_42.heat.add(shipBuilder_vehicleitemheat_46)

    shipBuilder_vehicleitem_43 = VehicleItem()
    shipBuilder_vehicleitem_43.itemClass = 1L
    shipBuilder_vehicleitem_43.description = u"The 11-Series Broadsword is the cannon pilots come to when they want the 3 D's: distance, dependability and damage. Packing a 45mm round, the Broadsword can fire a variety of rounds for any occasion."
    shipBuilder_vehicleitem_43.name = u'Knightbridge_11_Series_Broadsword'
    shipBuilder_vehicleitem_43.displayName = u'11-Series Broadsword'
    shipBuilder_vehicleitem_43.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_43.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_43.manufacturer = shipBuilder_manufacturer_44
    shipBuilder_vehicleitem_43.itemSize = 3L
    shipBuilder_vehicleitem_43.views = 0L
    shipBuilder_vehicleitem_43 = importer.save_or_locate(shipBuilder_vehicleitem_43)

    shipBuilder_vehicleitem_43.power.add(shipBuilder_vehicleitempower_52)
    shipBuilder_vehicleitem_43.power.add(shipBuilder_vehicleitempower_53)
    shipBuilder_vehicleitem_43.power.add(shipBuilder_vehicleitempower_54)
    shipBuilder_vehicleitem_43.heat.add(shipBuilder_vehicleitemheat_47)
    shipBuilder_vehicleitem_43.heat.add(shipBuilder_vehicleitemheat_48)
    shipBuilder_vehicleitem_43.heat.add(shipBuilder_vehicleitemheat_49)
    shipBuilder_vehicleitem_43.avionics.add(shipBuilder_vehicleitemavionics_31)
    shipBuilder_vehicleitem_43.avionics.add(shipBuilder_vehicleitemavionics_32)
    shipBuilder_vehicleitem_43.itemStats.add(shipBuilder_vehicleitemparams_118)
    shipBuilder_vehicleitem_43.itemStats.add(shipBuilder_vehicleitemparams_119)
    shipBuilder_vehicleitem_43.itemStats.add(shipBuilder_vehicleitemparams_120)
    shipBuilder_vehicleitem_43.itemStats.add(shipBuilder_vehicleitemparams_121)

    shipBuilder_vehicleitem_44 = VehicleItem()
    shipBuilder_vehicleitem_44.itemClass = 0L
    shipBuilder_vehicleitem_44.description = u"Lightning Power ltd's Powerbolt makes its living by offering the perfect blend of performance and signature masking. Lightning's proprietary Superfluid Quantum Vortex technology keeps energy emissions low while providing better output than typical stealth-oriented plants."
    shipBuilder_vehicleitem_44.name = u'LPB_Powerbolt'
    shipBuilder_vehicleitem_44.displayName = u'Lightning Powerbolt Powerbolt'
    shipBuilder_vehicleitem_44.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_44.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_44.manufacturer = shipBuilder_manufacturer_45
    shipBuilder_vehicleitem_44.itemSize = 4L
    shipBuilder_vehicleitem_44.views = 0L
    shipBuilder_vehicleitem_44 = importer.save_or_locate(shipBuilder_vehicleitem_44)

    shipBuilder_vehicleitem_44.power.add(shipBuilder_vehicleitempower_55)

    shipBuilder_vehicleitem_45 = VehicleItem()
    shipBuilder_vehicleitem_45.itemClass = 0L
    shipBuilder_vehicleitem_45.description = u''
    shipBuilder_vehicleitem_45.name = u'PhalanxTurret'
    shipBuilder_vehicleitem_45.displayName = u''
    shipBuilder_vehicleitem_45.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_45.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_45.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_45.itemSize = 2L
    shipBuilder_vehicleitem_45.views = 0L
    shipBuilder_vehicleitem_45 = importer.save_or_locate(shipBuilder_vehicleitem_45)

    shipBuilder_vehicleitem_46 = VehicleItem()
    shipBuilder_vehicleitem_46.itemClass = 0L
    shipBuilder_vehicleitem_46.description = u"The M4A is Behring's second tier laser cannon. Its bigger size means more power consumption in exchange for packing a bigger punch. Fire rate and power efficiency are comparable to the M3A model."
    shipBuilder_vehicleitem_46.name = u'Behring_M4A_Laser'
    shipBuilder_vehicleitem_46.displayName = u'Behring M4A Laser'
    shipBuilder_vehicleitem_46.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_46.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_46.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_46.itemSize = 2L
    shipBuilder_vehicleitem_46.views = 0L
    shipBuilder_vehicleitem_46 = importer.save_or_locate(shipBuilder_vehicleitem_46)

    shipBuilder_vehicleitem_46.power.add(shipBuilder_vehicleitempower_56)
    shipBuilder_vehicleitem_46.power.add(shipBuilder_vehicleitempower_57)
    shipBuilder_vehicleitem_46.power.add(shipBuilder_vehicleitempower_58)
    shipBuilder_vehicleitem_46.heat.add(shipBuilder_vehicleitemheat_50)
    shipBuilder_vehicleitem_46.heat.add(shipBuilder_vehicleitemheat_51)
    shipBuilder_vehicleitem_46.heat.add(shipBuilder_vehicleitemheat_52)
    shipBuilder_vehicleitem_46.avionics.add(shipBuilder_vehicleitemavionics_33)
    shipBuilder_vehicleitem_46.avionics.add(shipBuilder_vehicleitemavionics_34)
    shipBuilder_vehicleitem_46.itemStats.add(shipBuilder_vehicleitemparams_122)
    shipBuilder_vehicleitem_46.itemStats.add(shipBuilder_vehicleitemparams_123)
    shipBuilder_vehicleitem_46.itemStats.add(shipBuilder_vehicleitemparams_124)
    shipBuilder_vehicleitem_46.itemStats.add(shipBuilder_vehicleitemparams_125)

    shipBuilder_vehicleitem_47 = VehicleItem()
    shipBuilder_vehicleitem_47.itemClass = 1L
    shipBuilder_vehicleitem_47.description = u"Behring's M5A laser cannon bridges the gap between small ship and large ship weapons. Suitable for most ship models, the M5A offers respectable offensive capability in any situation. Fire rate and power efficiency are comparable to the M-series lasers."
    shipBuilder_vehicleitem_47.name = u'Behring_M5A_Laser'
    shipBuilder_vehicleitem_47.displayName = u'Behring M5A Laser'
    shipBuilder_vehicleitem_47.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_47.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_47.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_47.itemSize = 1L
    shipBuilder_vehicleitem_47.views = 1L
    shipBuilder_vehicleitem_47 = importer.save_or_locate(shipBuilder_vehicleitem_47)

    shipBuilder_vehicleitem_47.power.add(shipBuilder_vehicleitempower_59)
    shipBuilder_vehicleitem_47.power.add(shipBuilder_vehicleitempower_60)
    shipBuilder_vehicleitem_47.power.add(shipBuilder_vehicleitempower_61)
    shipBuilder_vehicleitem_47.heat.add(shipBuilder_vehicleitemheat_53)
    shipBuilder_vehicleitem_47.heat.add(shipBuilder_vehicleitemheat_54)
    shipBuilder_vehicleitem_47.heat.add(shipBuilder_vehicleitemheat_55)
    shipBuilder_vehicleitem_47.avionics.add(shipBuilder_vehicleitemavionics_35)
    shipBuilder_vehicleitem_47.avionics.add(shipBuilder_vehicleitemavionics_36)
    shipBuilder_vehicleitem_47.itemStats.add(shipBuilder_vehicleitemparams_126)
    shipBuilder_vehicleitem_47.itemStats.add(shipBuilder_vehicleitemparams_127)
    shipBuilder_vehicleitem_47.itemStats.add(shipBuilder_vehicleitemparams_128)
    shipBuilder_vehicleitem_47.itemStats.add(shipBuilder_vehicleitemparams_129)

    shipBuilder_vehicleitem_48 = VehicleItem()
    shipBuilder_vehicleitem_48.itemClass = 0L
    shipBuilder_vehicleitem_48.description = u"By far ACOM's most popular model, the StarHeart III solves many of the problems of the StarLight models by increasing durability, decreasing signature, while maintaining the high power output."
    shipBuilder_vehicleitem_48.name = u'300i_ACOM_StarHeart_III'
    shipBuilder_vehicleitem_48.displayName = u'ACOM StarHeart III Engine'
    shipBuilder_vehicleitem_48.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_48.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_48.manufacturer = shipBuilder_manufacturer_10
    shipBuilder_vehicleitem_48.itemSize = 2L
    shipBuilder_vehicleitem_48.views = 0L
    shipBuilder_vehicleitem_48 = importer.save_or_locate(shipBuilder_vehicleitem_48)

    shipBuilder_vehicleitem_48.power.add(shipBuilder_vehicleitempower_62)

    shipBuilder_vehicleitem_49 = VehicleItem()
    shipBuilder_vehicleitem_49.itemClass = 0L
    shipBuilder_vehicleitem_49.description = u''
    shipBuilder_vehicleitem_49.name = u'Anvil_Flex_Thruster_TR2_Back_Right'
    shipBuilder_vehicleitem_49.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_49.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_49.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_49.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_49.itemSize = 2L
    shipBuilder_vehicleitem_49.views = 0L
    shipBuilder_vehicleitem_49 = importer.save_or_locate(shipBuilder_vehicleitem_49)

    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_130)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_131)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_132)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_133)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_134)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_135)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_136)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_137)
    shipBuilder_vehicleitem_49.itemStats.add(shipBuilder_vehicleitemparams_138)

    shipBuilder_vehicleitem_50 = VehicleItem()
    shipBuilder_vehicleitem_50.itemClass = 1L
    shipBuilder_vehicleitem_50.description = u'The Mk VI is a trusted and dependable high-power laser weapon system for pilots who desire additional precision and power efficiency. The Mk VI is ideal for larger ships and can even be deployed in capital ship turrets.'
    shipBuilder_vehicleitem_50.name = u'Behring_Mk_VI_Laser'
    shipBuilder_vehicleitem_50.displayName = u'Behring Mk VI Laser'
    shipBuilder_vehicleitem_50.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_50.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_50.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_50.itemSize = 4L
    shipBuilder_vehicleitem_50.views = 0L
    shipBuilder_vehicleitem_50 = importer.save_or_locate(shipBuilder_vehicleitem_50)

    shipBuilder_vehicleitem_50.power.add(shipBuilder_vehicleitempower_63)
    shipBuilder_vehicleitem_50.power.add(shipBuilder_vehicleitempower_64)
    shipBuilder_vehicleitem_50.power.add(shipBuilder_vehicleitempower_65)
    shipBuilder_vehicleitem_50.heat.add(shipBuilder_vehicleitemheat_56)
    shipBuilder_vehicleitem_50.heat.add(shipBuilder_vehicleitemheat_57)
    shipBuilder_vehicleitem_50.heat.add(shipBuilder_vehicleitemheat_58)
    shipBuilder_vehicleitem_50.avionics.add(shipBuilder_vehicleitemavionics_37)
    shipBuilder_vehicleitem_50.avionics.add(shipBuilder_vehicleitemavionics_38)
    shipBuilder_vehicleitem_50.itemStats.add(shipBuilder_vehicleitemparams_139)
    shipBuilder_vehicleitem_50.itemStats.add(shipBuilder_vehicleitemparams_140)
    shipBuilder_vehicleitem_50.itemStats.add(shipBuilder_vehicleitemparams_141)
    shipBuilder_vehicleitem_50.itemStats.add(shipBuilder_vehicleitemparams_142)

    shipBuilder_vehicleitem_51 = VehicleItem()
    shipBuilder_vehicleitem_51.itemClass = 0L
    shipBuilder_vehicleitem_51.description = u"The LR-7 ULTRA OverDrive is the patriarch of the LR series. Capable of handling any number of hauling or commercial needs, the LR-7 features a reinforced plasma-core to combat the increased heat signature. Odds are, if you need a monster of a power plant like this, your ship isn't hiding."
    shipBuilder_vehicleitem_51.name = u'A_and_R_LR-7_ULTRA_OverDrive'
    shipBuilder_vehicleitem_51.displayName = u'A&R LR-7 ULTRA OverDrive'
    shipBuilder_vehicleitem_51.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_51.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_51.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_vehicleitem_51.itemSize = 3L
    shipBuilder_vehicleitem_51.views = 0L
    shipBuilder_vehicleitem_51 = importer.save_or_locate(shipBuilder_vehicleitem_51)

    shipBuilder_vehicleitem_51.power.add(shipBuilder_vehicleitempower_66)

    shipBuilder_vehicleitem_52 = VehicleItem()
    shipBuilder_vehicleitem_52.itemClass = 0L
    shipBuilder_vehicleitem_52.description = u''
    shipBuilder_vehicleitem_52.name = u'STSTurret'
    shipBuilder_vehicleitem_52.displayName = u''
    shipBuilder_vehicleitem_52.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_52.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_52.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_52.itemSize = 2L
    shipBuilder_vehicleitem_52.views = 0L
    shipBuilder_vehicleitem_52 = importer.save_or_locate(shipBuilder_vehicleitem_52)

    shipBuilder_vehicleitem_53 = VehicleItem()
    shipBuilder_vehicleitem_53.itemClass = 0L
    shipBuilder_vehicleitem_53.description = u"The StarLight II is the baseline model of ACOM's award winning Star Series of anti-tritium power planets. While this model offers a robust output, the durability and signature of the power source suffer from the smaller size."
    shipBuilder_vehicleitem_53.name = u'ACOM_StarLight_II'
    shipBuilder_vehicleitem_53.displayName = u'ACOM StarLight II Engine'
    shipBuilder_vehicleitem_53.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_53.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_53.manufacturer = shipBuilder_manufacturer_10
    shipBuilder_vehicleitem_53.itemSize = 1L
    shipBuilder_vehicleitem_53.views = 0L
    shipBuilder_vehicleitem_53 = importer.save_or_locate(shipBuilder_vehicleitem_53)

    shipBuilder_vehicleitem_53.power.add(shipBuilder_vehicleitempower_67)

    shipBuilder_vehicleitem_54 = VehicleItem()
    shipBuilder_vehicleitem_54.itemClass = 0L
    shipBuilder_vehicleitem_54.description = u"Capable of powering a medium class vessel, the HM4.4 is all speed and no caution. It's main selling point, the heavy output, becomes its biggest detriment as the engine flash will make conventional countermeasures useless when attempting to distract missiles. But, like the ad says, if it's speed you want..."
    shipBuilder_vehicleitem_54.name = u'Hammer_Propulsion_HM_4.4'
    shipBuilder_vehicleitem_54.displayName = u'Hammer Propulsion HMX 4.4'
    shipBuilder_vehicleitem_54.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_54.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_54.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_54.itemSize = 4L
    shipBuilder_vehicleitem_54.views = 0L
    shipBuilder_vehicleitem_54 = importer.save_or_locate(shipBuilder_vehicleitem_54)

    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_143)
    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_144)
    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_145)
    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_146)
    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_147)
    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_148)
    shipBuilder_vehicleitem_54.itemStats.add(shipBuilder_vehicleitemparams_149)

    shipBuilder_vehicleitem_55 = VehicleItem()
    shipBuilder_vehicleitem_55.itemClass = 0L
    shipBuilder_vehicleitem_55.description = u"Wei-Tek's VHT2 Plus is one of their oldest models. A fission-based power plant, the VHT2 Plus maintains the fission tradition of low output and high signature, but offers a higher quality construction than most of its competitors that increases the technology's longevity."
    shipBuilder_vehicleitem_55.name = u'Wei_Tek_VHT2_Plus'
    shipBuilder_vehicleitem_55.displayName = u'Wei Tek VHT2 Plus'
    shipBuilder_vehicleitem_55.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_55.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_55.manufacturer = shipBuilder_manufacturer_12
    shipBuilder_vehicleitem_55.itemSize = 4L
    shipBuilder_vehicleitem_55.views = 0L
    shipBuilder_vehicleitem_55 = importer.save_or_locate(shipBuilder_vehicleitem_55)

    shipBuilder_vehicleitem_55.power.add(shipBuilder_vehicleitempower_68)

    shipBuilder_vehicleitem_56 = VehicleItem()
    shipBuilder_vehicleitem_56.itemClass = 0L
    shipBuilder_vehicleitem_56.description = u''
    shipBuilder_vehicleitem_56.name = u'ScytheMissileRacks'
    shipBuilder_vehicleitem_56.displayName = u''
    shipBuilder_vehicleitem_56.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_56.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_56.manufacturer = shipBuilder_manufacturer_42
    shipBuilder_vehicleitem_56.itemSize = 2L
    shipBuilder_vehicleitem_56.views = 0L
    shipBuilder_vehicleitem_56 = importer.save_or_locate(shipBuilder_vehicleitem_56)

    shipBuilder_vehicleitem_57 = VehicleItem()
    shipBuilder_vehicleitem_57.itemClass = 0L
    shipBuilder_vehicleitem_57.description = u''
    shipBuilder_vehicleitem_57.name = u'ScytheLeftWingCannon'
    shipBuilder_vehicleitem_57.displayName = u''
    shipBuilder_vehicleitem_57.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_57.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_57.manufacturer = shipBuilder_manufacturer_42
    shipBuilder_vehicleitem_57.itemSize = 2L
    shipBuilder_vehicleitem_57.views = 0L
    shipBuilder_vehicleitem_57 = importer.save_or_locate(shipBuilder_vehicleitem_57)

    shipBuilder_vehicleitem_58 = VehicleItem()
    shipBuilder_vehicleitem_58.itemClass = 0L
    shipBuilder_vehicleitem_58.description = u''
    shipBuilder_vehicleitem_58.name = u'Aegis_Dynamics_M-5c_PowerPlant'
    shipBuilder_vehicleitem_58.displayName = u'Aegis Dynamics M-5c Thorium Engine'
    shipBuilder_vehicleitem_58.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_58.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_58.manufacturer = shipBuilder_manufacturer_37
    shipBuilder_vehicleitem_58.itemSize = 4L
    shipBuilder_vehicleitem_58.views = 0L
    shipBuilder_vehicleitem_58 = importer.save_or_locate(shipBuilder_vehicleitem_58)

    shipBuilder_vehicleitem_58.power.add(shipBuilder_vehicleitempower_69)

    shipBuilder_vehicleitem_59 = VehicleItem()
    shipBuilder_vehicleitem_59.itemClass = 0L
    shipBuilder_vehicleitem_59.description = u'The STC Blue by perrenial thruster manufacturer Dragon Stellar Transit Company offers high output and low emissions, great for pilots wishing to close the distance while maintaining a low profile. The smallest thruster in the STC lineup, the Blue has a thrust rating of 2.'
    shipBuilder_vehicleitem_59.name = u'Dragon_STC_Blue'
    shipBuilder_vehicleitem_59.displayName = u'Dragon STC Blue Main Engine'
    shipBuilder_vehicleitem_59.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_59.itemSubType = shipBuilder_vehicleitemsubtype_11
    shipBuilder_vehicleitem_59.manufacturer = shipBuilder_manufacturer_41
    shipBuilder_vehicleitem_59.itemSize = 2L
    shipBuilder_vehicleitem_59.views = 0L
    shipBuilder_vehicleitem_59 = importer.save_or_locate(shipBuilder_vehicleitem_59)

    shipBuilder_vehicleitem_59.itemStats.add(shipBuilder_vehicleitemparams_150)
    shipBuilder_vehicleitem_59.itemStats.add(shipBuilder_vehicleitemparams_151)
    shipBuilder_vehicleitem_59.itemStats.add(shipBuilder_vehicleitemparams_152)

    shipBuilder_vehicleitem_60 = VehicleItem()
    shipBuilder_vehicleitem_60.itemClass = 3L
    shipBuilder_vehicleitem_60.description = u"Talon's Executioner missiles track and lock their target by use of highly sensitive optical cameras and image processing software. The Executioners deliver a combination of hull-breaching and high-explosive payload, making them effective weapons against smaller capital ships."
    shipBuilder_vehicleitem_60.name = u'Talon_Executioner_IR_Twin'
    shipBuilder_vehicleitem_60.displayName = u'Talon Executioner IR Twin'
    shipBuilder_vehicleitem_60.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_60.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_60.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_vehicleitem_60.itemSize = 5L
    shipBuilder_vehicleitem_60.views = 0L
    shipBuilder_vehicleitem_60 = importer.save_or_locate(shipBuilder_vehicleitem_60)

    shipBuilder_vehicleitem_60.power.add(shipBuilder_vehicleitempower_70)
    shipBuilder_vehicleitem_60.power.add(shipBuilder_vehicleitempower_71)
    shipBuilder_vehicleitem_60.power.add(shipBuilder_vehicleitempower_72)
    shipBuilder_vehicleitem_60.heat.add(shipBuilder_vehicleitemheat_59)
    shipBuilder_vehicleitem_60.heat.add(shipBuilder_vehicleitemheat_60)
    shipBuilder_vehicleitem_60.heat.add(shipBuilder_vehicleitemheat_61)
    shipBuilder_vehicleitem_60.avionics.add(shipBuilder_vehicleitemavionics_39)
    shipBuilder_vehicleitem_60.avionics.add(shipBuilder_vehicleitemavionics_40)
    shipBuilder_vehicleitem_60.itemStats.add(shipBuilder_vehicleitemparams_153)
    shipBuilder_vehicleitem_60.itemStats.add(shipBuilder_vehicleitemparams_154)
    shipBuilder_vehicleitem_60.itemStats.add(shipBuilder_vehicleitemparams_155)
    shipBuilder_vehicleitem_60.itemStats.add(shipBuilder_vehicleitemparams_156)

    shipBuilder_vehicleitem_61 = VehicleItem()
    shipBuilder_vehicleitem_61.itemClass = 0L
    shipBuilder_vehicleitem_61.description = u'The Hammer Propulsion HE5.3 features a high output, fuel efficient design. Its thrust output and low fuel consumption make it ideal for long hauls though it has been reported to be somewhat of a missile magnet on occasions where owners have been subject to pirate activity.'
    shipBuilder_vehicleitem_61.name = u'300i_Hammer_Propulsion_HE_5_3'
    shipBuilder_vehicleitem_61.displayName = u'Hammer Propulsion HE 5.3'
    shipBuilder_vehicleitem_61.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_61.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_61.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_61.itemSize = 3L
    shipBuilder_vehicleitem_61.views = 0L
    shipBuilder_vehicleitem_61 = importer.save_or_locate(shipBuilder_vehicleitem_61)

    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_157)
    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_158)
    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_159)
    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_160)
    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_161)
    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_162)
    shipBuilder_vehicleitem_61.itemStats.add(shipBuilder_vehicleitemparams_163)

    shipBuilder_vehicleitem_62 = VehicleItem()
    shipBuilder_vehicleitem_62.itemClass = 0L
    shipBuilder_vehicleitem_62.description = u"If speed is what you're after, the HM4.3 engine can give it to you. Built under supervision of the Racing Division at Hammer Propulsion, the 4.3 is a single-thruster system iteration of the award-winning Twin HM4.3 propulsion units made famous by the Origin 350r racers. The 4.3 has been specifically crafted down to the smallest pinion to give you the most boost possible in a single engine system."
    shipBuilder_vehicleitem_62.name = u'Hammer_Propulsion_HM_4_3'
    shipBuilder_vehicleitem_62.displayName = u'Hammer Propulsion HM 4.3'
    shipBuilder_vehicleitem_62.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_62.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_62.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_62.itemSize = 3L
    shipBuilder_vehicleitem_62.views = 0L
    shipBuilder_vehicleitem_62 = importer.save_or_locate(shipBuilder_vehicleitem_62)

    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_164)
    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_165)
    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_166)
    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_167)
    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_168)
    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_169)
    shipBuilder_vehicleitem_62.itemStats.add(shipBuilder_vehicleitemparams_170)

    shipBuilder_vehicleitem_63 = VehicleItem()
    shipBuilder_vehicleitem_63.itemClass = 1L
    shipBuilder_vehicleitem_63.description = u"Badger repeater is Klaus & Werner's dependable second-tier repeating laser. Its increased output (and corresponding power consumption) make it a solid contender in any fight. Power efficiency continues to be a problem with the K&W models, however."
    shipBuilder_vehicleitem_63.name = u'K_and_W_CF-117_Badger_Repeater'
    shipBuilder_vehicleitem_63.displayName = u'CF-117 Badger Repeater'
    shipBuilder_vehicleitem_63.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_63.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_63.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_63.itemSize = 2L
    shipBuilder_vehicleitem_63.views = 0L
    shipBuilder_vehicleitem_63 = importer.save_or_locate(shipBuilder_vehicleitem_63)

    shipBuilder_vehicleitem_63.power.add(shipBuilder_vehicleitempower_73)
    shipBuilder_vehicleitem_63.power.add(shipBuilder_vehicleitempower_74)
    shipBuilder_vehicleitem_63.power.add(shipBuilder_vehicleitempower_75)
    shipBuilder_vehicleitem_63.heat.add(shipBuilder_vehicleitemheat_62)
    shipBuilder_vehicleitem_63.heat.add(shipBuilder_vehicleitemheat_63)
    shipBuilder_vehicleitem_63.heat.add(shipBuilder_vehicleitemheat_64)
    shipBuilder_vehicleitem_63.avionics.add(shipBuilder_vehicleitemavionics_41)
    shipBuilder_vehicleitem_63.avionics.add(shipBuilder_vehicleitemavionics_42)
    shipBuilder_vehicleitem_63.itemStats.add(shipBuilder_vehicleitemparams_171)
    shipBuilder_vehicleitem_63.itemStats.add(shipBuilder_vehicleitemparams_172)
    shipBuilder_vehicleitem_63.itemStats.add(shipBuilder_vehicleitemparams_173)
    shipBuilder_vehicleitem_63.itemStats.add(shipBuilder_vehicleitemparams_174)

    shipBuilder_vehicleitem_64 = VehicleItem()
    shipBuilder_vehicleitem_64.itemClass = 0L
    shipBuilder_vehicleitem_64.description = u"The inaugural model of GNP's new Etoile series, the Etoile-00 utilizes a liquid fluoride thorium reactor technology to create a highly damage-resistant power alternative to medium class ships."
    shipBuilder_vehicleitem_64.name = u'Groupe_Nouveau_Paradigme_Etoile-00'
    shipBuilder_vehicleitem_64.displayName = u'Groupe Nouveau Paradigme Etoile-00'
    shipBuilder_vehicleitem_64.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_64.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_64.manufacturer = shipBuilder_manufacturer_17
    shipBuilder_vehicleitem_64.itemSize = 4L
    shipBuilder_vehicleitem_64.views = 0L
    shipBuilder_vehicleitem_64 = importer.save_or_locate(shipBuilder_vehicleitem_64)

    shipBuilder_vehicleitem_64.power.add(shipBuilder_vehicleitempower_76)

    shipBuilder_vehicleitem_65 = VehicleItem()
    shipBuilder_vehicleitem_65.itemClass = 0L
    shipBuilder_vehicleitem_65.description = u''
    shipBuilder_vehicleitem_65.name = u'RSI_DefaultRadarDisplay'
    shipBuilder_vehicleitem_65.displayName = u'RSI Radar Display'
    shipBuilder_vehicleitem_65.itemType = shipBuilder_vehicleitemtype_6
    shipBuilder_vehicleitem_65.itemSubType = shipBuilder_vehicleitemsubtype_15
    shipBuilder_vehicleitem_65.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_65.itemSize = 1L
    shipBuilder_vehicleitem_65.views = 0L
    shipBuilder_vehicleitem_65 = importer.save_or_locate(shipBuilder_vehicleitem_65)

    shipBuilder_vehicleitem_65.itemStats.add(shipBuilder_vehicleitemparams_175)
    shipBuilder_vehicleitem_65.itemStats.add(shipBuilder_vehicleitemparams_176)

    shipBuilder_vehicleitem_66 = VehicleItem()
    shipBuilder_vehicleitem_66.itemClass = 0L
    shipBuilder_vehicleitem_66.description = u''
    shipBuilder_vehicleitem_66.name = u'RSI_DefaultTargetSelector'
    shipBuilder_vehicleitem_66.displayName = u'RSI Target Selection Device'
    shipBuilder_vehicleitem_66.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_66.itemSubType = shipBuilder_vehicleitemsubtype_16
    shipBuilder_vehicleitem_66.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_66.itemSize = 1L
    shipBuilder_vehicleitem_66.views = 2L
    shipBuilder_vehicleitem_66 = importer.save_or_locate(shipBuilder_vehicleitem_66)

    shipBuilder_vehicleitem_66.itemStats.add(shipBuilder_vehicleitemparams_177)

    shipBuilder_vehicleitem_67 = VehicleItem()
    shipBuilder_vehicleitem_67.itemClass = 0L
    shipBuilder_vehicleitem_67.description = u"Lightning Power ltd's Powerbolt makes its living by offering the perfect blend of performance and signature masking. Lightning's proprietary Superfluid Quantum Vortex technology keeps energy emissions low while providing better output than typical stealth-oriented plants."
    shipBuilder_vehicleitem_67.name = u'LPB_Condensed_Matter_Reactor'
    shipBuilder_vehicleitem_67.displayName = u'Lightning Powerbolt Hyperfluid Quantum Vortex'
    shipBuilder_vehicleitem_67.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_67.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_67.manufacturer = shipBuilder_manufacturer_37
    shipBuilder_vehicleitem_67.itemSize = 2L
    shipBuilder_vehicleitem_67.views = 0L
    shipBuilder_vehicleitem_67 = importer.save_or_locate(shipBuilder_vehicleitem_67)

    shipBuilder_vehicleitem_67.power.add(shipBuilder_vehicleitempower_77)

    shipBuilder_vehicleitem_68 = VehicleItem()
    shipBuilder_vehicleitem_68.itemClass = 0L
    shipBuilder_vehicleitem_68.description = u''
    shipBuilder_vehicleitem_68.name = u'Anvil_Joint_Thruster_TR2'
    shipBuilder_vehicleitem_68.displayName = u'Anvil TR2 Jointed Thruster'
    shipBuilder_vehicleitem_68.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_68.itemSubType = shipBuilder_vehicleitemsubtype_10
    shipBuilder_vehicleitem_68.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_68.itemSize = 2L
    shipBuilder_vehicleitem_68.views = 0L
    shipBuilder_vehicleitem_68 = importer.save_or_locate(shipBuilder_vehicleitem_68)

    shipBuilder_vehicleitem_68.itemStats.add(shipBuilder_vehicleitemparams_178)
    shipBuilder_vehicleitem_68.itemStats.add(shipBuilder_vehicleitemparams_179)
    shipBuilder_vehicleitem_68.itemStats.add(shipBuilder_vehicleitemparams_180)
    shipBuilder_vehicleitem_68.itemStats.add(shipBuilder_vehicleitemparams_181)
    shipBuilder_vehicleitem_68.itemStats.add(shipBuilder_vehicleitemparams_182)

    shipBuilder_vehicleitem_69 = VehicleItem()
    shipBuilder_vehicleitem_69.itemClass = 0L
    shipBuilder_vehicleitem_69.description = u"ArcCorp's Arc Duo 400 was recently named one of Whitley's Ten Best Commercial Grade Thrusters. Designed to handle the payload requirements of larger class vessels, the Arc Duo 400 continues ArcCorp's design philosophy of lower signature and better efficiency."
    shipBuilder_vehicleitem_69.name = u'Arc_Duo_400'
    shipBuilder_vehicleitem_69.displayName = u'ArcLight 300'
    shipBuilder_vehicleitem_69.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_69.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_69.manufacturer = shipBuilder_manufacturer_21
    shipBuilder_vehicleitem_69.itemSize = 3L
    shipBuilder_vehicleitem_69.views = 0L
    shipBuilder_vehicleitem_69 = importer.save_or_locate(shipBuilder_vehicleitem_69)

    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_183)
    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_184)
    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_185)
    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_186)
    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_187)
    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_188)
    shipBuilder_vehicleitem_69.itemStats.add(shipBuilder_vehicleitemparams_189)

    shipBuilder_vehicleitem_70 = VehicleItem()
    shipBuilder_vehicleitem_70.itemClass = 0L
    shipBuilder_vehicleitem_70.description = u'The Alliance Startech KS-9 Chromodynamic Assembler system is a durable, low-signature power plant most commonly used in Aurora class starships. The decreased signature and increased reliability come at the cost of relatively weak power production, something that pilots will want to consider if they intend on mounting weapons systems with large power requirements.'
    shipBuilder_vehicleitem_70.name = u'Alliance_Startech_KS-9'
    shipBuilder_vehicleitem_70.displayName = u'Alliance_Startech_KS-9'
    shipBuilder_vehicleitem_70.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_70.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_70.manufacturer = shipBuilder_manufacturer_14
    shipBuilder_vehicleitem_70.itemSize = 1L
    shipBuilder_vehicleitem_70.views = 0L
    shipBuilder_vehicleitem_70 = importer.save_or_locate(shipBuilder_vehicleitem_70)

    shipBuilder_vehicleitem_70.power.add(shipBuilder_vehicleitempower_78)

    shipBuilder_vehicleitem_71 = VehicleItem()
    shipBuilder_vehicleitem_71.itemClass = 0L
    shipBuilder_vehicleitem_71.description = u'The Mantis GT-220 is a hydraulically-driven Gatling-type rotary cannon designed to deliver smaller rounds at a very high rate of fire. The Mantis is designed to shred armor on very fast targets, sacrificing power for absolute saturation of the target area.'
    shipBuilder_vehicleitem_71.name = u'Mantis_GT-220'
    shipBuilder_vehicleitem_71.displayName = u'Mantis GT-220'
    shipBuilder_vehicleitem_71.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_71.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_71.manufacturer = shipBuilder_manufacturer_31
    shipBuilder_vehicleitem_71.itemSize = 2L
    shipBuilder_vehicleitem_71.views = 0L
    shipBuilder_vehicleitem_71 = importer.save_or_locate(shipBuilder_vehicleitem_71)

    shipBuilder_vehicleitem_71.power.add(shipBuilder_vehicleitempower_79)
    shipBuilder_vehicleitem_71.power.add(shipBuilder_vehicleitempower_80)
    shipBuilder_vehicleitem_71.power.add(shipBuilder_vehicleitempower_81)
    shipBuilder_vehicleitem_71.heat.add(shipBuilder_vehicleitemheat_65)
    shipBuilder_vehicleitem_71.heat.add(shipBuilder_vehicleitemheat_66)
    shipBuilder_vehicleitem_71.heat.add(shipBuilder_vehicleitemheat_67)
    shipBuilder_vehicleitem_71.avionics.add(shipBuilder_vehicleitemavionics_43)
    shipBuilder_vehicleitem_71.avionics.add(shipBuilder_vehicleitemavionics_44)

    shipBuilder_vehicleitem_72 = VehicleItem()
    shipBuilder_vehicleitem_72.itemClass = 0L
    shipBuilder_vehicleitem_72.description = u''
    shipBuilder_vehicleitem_72.name = u'Anvil_Flex_Thruster_TR2_Front_Left'
    shipBuilder_vehicleitem_72.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_72.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_72.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_72.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_72.itemSize = 2L
    shipBuilder_vehicleitem_72.views = 0L
    shipBuilder_vehicleitem_72 = importer.save_or_locate(shipBuilder_vehicleitem_72)

    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_190)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_191)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_192)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_193)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_194)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_195)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_196)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_197)
    shipBuilder_vehicleitem_72.itemStats.add(shipBuilder_vehicleitemparams_198)

    shipBuilder_vehicleitem_73 = VehicleItem()
    shipBuilder_vehicleitem_73.itemClass = 0L
    shipBuilder_vehicleitem_73.description = u"Designed in conjunction with the engineers at RSI, the A&R LR-5 Max OverDrive features the same great engine you've come to expect from A&R, but with higher quality parts built with the care and dedication that you've come to expect from the company that's been taking humanity to the stars since 2075."
    shipBuilder_vehicleitem_73.name = u'A_and_R_LR-5_MAX_OverDrive'
    shipBuilder_vehicleitem_73.displayName = u'A&R LR-5 MAX OverDrive'
    shipBuilder_vehicleitem_73.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_73.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_73.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_vehicleitem_73.itemSize = 1L
    shipBuilder_vehicleitem_73.views = 0L
    shipBuilder_vehicleitem_73 = importer.save_or_locate(shipBuilder_vehicleitem_73)

    shipBuilder_vehicleitem_73.power.add(shipBuilder_vehicleitempower_82)

    shipBuilder_vehicleitem_74 = VehicleItem()
    shipBuilder_vehicleitem_74.itemClass = 0L
    shipBuilder_vehicleitem_74.description = u''
    shipBuilder_vehicleitem_74.name = u'RSI_DefaultPowerPlant'
    shipBuilder_vehicleitem_74.displayName = u'RSI Power Supply'
    shipBuilder_vehicleitem_74.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_74.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_74.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_74.itemSize = 1L
    shipBuilder_vehicleitem_74.views = 0L
    shipBuilder_vehicleitem_74 = importer.save_or_locate(shipBuilder_vehicleitem_74)

    shipBuilder_vehicleitem_74.power.add(shipBuilder_vehicleitempower_83)

    shipBuilder_vehicleitem_75 = VehicleItem()
    shipBuilder_vehicleitem_75.itemClass = 1L
    shipBuilder_vehicleitem_75.description = u"The entry level weapon of the Sword-series, the Longsword fires a 35mm round designed for use against a variety of armored targets. Don't let shields slow down your domination of the galaxy."
    shipBuilder_vehicleitem_75.name = u'Knightbridge_9_Series_Longsword'
    shipBuilder_vehicleitem_75.displayName = u'9-Series Longsword'
    shipBuilder_vehicleitem_75.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_75.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_75.manufacturer = shipBuilder_manufacturer_44
    shipBuilder_vehicleitem_75.itemSize = 1L
    shipBuilder_vehicleitem_75.views = 0L
    shipBuilder_vehicleitem_75 = importer.save_or_locate(shipBuilder_vehicleitem_75)

    shipBuilder_vehicleitem_75.power.add(shipBuilder_vehicleitempower_84)
    shipBuilder_vehicleitem_75.power.add(shipBuilder_vehicleitempower_85)
    shipBuilder_vehicleitem_75.power.add(shipBuilder_vehicleitempower_86)
    shipBuilder_vehicleitem_75.heat.add(shipBuilder_vehicleitemheat_68)
    shipBuilder_vehicleitem_75.heat.add(shipBuilder_vehicleitemheat_69)
    shipBuilder_vehicleitem_75.heat.add(shipBuilder_vehicleitemheat_70)
    shipBuilder_vehicleitem_75.avionics.add(shipBuilder_vehicleitemavionics_45)
    shipBuilder_vehicleitem_75.avionics.add(shipBuilder_vehicleitemavionics_46)
    shipBuilder_vehicleitem_75.itemStats.add(shipBuilder_vehicleitemparams_199)
    shipBuilder_vehicleitem_75.itemStats.add(shipBuilder_vehicleitemparams_200)
    shipBuilder_vehicleitem_75.itemStats.add(shipBuilder_vehicleitemparams_201)
    shipBuilder_vehicleitem_75.itemStats.add(shipBuilder_vehicleitemparams_202)

    shipBuilder_vehicleitem_76 = VehicleItem()
    shipBuilder_vehicleitem_76.itemClass = 0L
    shipBuilder_vehicleitem_76.description = u'Greycat\u2019s latest addition to their field-tested tractor beam line is a dependable addition to their catalog. Aside from a more efficient pull/draw ratio, the latest model does little to advance from the previous models. The Sure Grip has settings to target and extract everything from asteroid fragments to drifting crewmen, backed by Greycat\u2019s certified Soft-Touch\xae guarantee.'
    shipBuilder_vehicleitem_76.name = u'Greycat_Industrial_Sure_Grip_Tractor'
    shipBuilder_vehicleitem_76.displayName = u'Sure Grip Tractor'
    shipBuilder_vehicleitem_76.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_76.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_76.manufacturer = shipBuilder_manufacturer_29
    shipBuilder_vehicleitem_76.itemSize = 1L
    shipBuilder_vehicleitem_76.views = 0L
    shipBuilder_vehicleitem_76 = importer.save_or_locate(shipBuilder_vehicleitem_76)

    shipBuilder_vehicleitem_77 = VehicleItem()
    shipBuilder_vehicleitem_77.itemClass = 1L
    shipBuilder_vehicleitem_77.description = u"The M4A is Behring's second tier laser cannon. Its bigger size means more power consumption in exchange for packing a bigger punch. Fire rate and power efficiency are comparable to the M3A model."
    shipBuilder_vehicleitem_77.name = u'Behring_M4A_lasser_Cannon'
    shipBuilder_vehicleitem_77.displayName = u'M4A Lasser Cannon'
    shipBuilder_vehicleitem_77.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_77.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_77.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_77.itemSize = 2L
    shipBuilder_vehicleitem_77.views = 0L
    shipBuilder_vehicleitem_77 = importer.save_or_locate(shipBuilder_vehicleitem_77)

    shipBuilder_vehicleitem_77.power.add(shipBuilder_vehicleitempower_87)
    shipBuilder_vehicleitem_77.power.add(shipBuilder_vehicleitempower_88)
    shipBuilder_vehicleitem_77.power.add(shipBuilder_vehicleitempower_89)
    shipBuilder_vehicleitem_77.heat.add(shipBuilder_vehicleitemheat_71)
    shipBuilder_vehicleitem_77.heat.add(shipBuilder_vehicleitemheat_72)
    shipBuilder_vehicleitem_77.heat.add(shipBuilder_vehicleitemheat_73)
    shipBuilder_vehicleitem_77.avionics.add(shipBuilder_vehicleitemavionics_47)
    shipBuilder_vehicleitem_77.avionics.add(shipBuilder_vehicleitemavionics_48)

    shipBuilder_vehicleitem_78 = VehicleItem()
    shipBuilder_vehicleitem_78.itemClass = 0L
    shipBuilder_vehicleitem_78.description = u''
    shipBuilder_vehicleitem_78.name = u'Anvil_Joint_MK2'
    shipBuilder_vehicleitem_78.displayName = u'Anvil MK2 Jointed Thruster'
    shipBuilder_vehicleitem_78.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_78.itemSubType = shipBuilder_vehicleitemsubtype_10
    shipBuilder_vehicleitem_78.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_78.itemSize = 2L
    shipBuilder_vehicleitem_78.views = 0L
    shipBuilder_vehicleitem_78 = importer.save_or_locate(shipBuilder_vehicleitem_78)

    shipBuilder_vehicleitem_78.itemStats.add(shipBuilder_vehicleitemparams_203)
    shipBuilder_vehicleitem_78.itemStats.add(shipBuilder_vehicleitemparams_204)
    shipBuilder_vehicleitem_78.itemStats.add(shipBuilder_vehicleitemparams_205)
    shipBuilder_vehicleitem_78.itemStats.add(shipBuilder_vehicleitemparams_206)
    shipBuilder_vehicleitem_78.itemStats.add(shipBuilder_vehicleitemparams_207)

    shipBuilder_vehicleitem_79 = VehicleItem()
    shipBuilder_vehicleitem_79.itemClass = 0L
    shipBuilder_vehicleitem_79.description = u"By far ACOM's most popular model, the StarHeart III solves many of the problems of the StarLight models by increasing durability and decreasing signature while maintaining the high power output."
    shipBuilder_vehicleitem_79.name = u'ACOM_StarHeart_III'
    shipBuilder_vehicleitem_79.displayName = u'ACOM StarHeart III Power Plant'
    shipBuilder_vehicleitem_79.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_79.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_79.manufacturer = shipBuilder_manufacturer_10
    shipBuilder_vehicleitem_79.itemSize = 2L
    shipBuilder_vehicleitem_79.views = 0L
    shipBuilder_vehicleitem_79 = importer.save_or_locate(shipBuilder_vehicleitem_79)

    shipBuilder_vehicleitem_79.power.add(shipBuilder_vehicleitempower_90)

    shipBuilder_vehicleitem_80 = VehicleItem()
    shipBuilder_vehicleitem_80.itemClass = 0L
    shipBuilder_vehicleitem_80.description = u"The luxury version of the HM4.3, Hammer Propulsion's HMX4.3 engine system features customized racing parts from some of the league's top engineers to help weather corrosion and general part decay."
    shipBuilder_vehicleitem_80.name = u'Hammer_Propulsion_HMX_4.3'
    shipBuilder_vehicleitem_80.displayName = u'Hammer Propulsion HMX 4.3'
    shipBuilder_vehicleitem_80.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_80.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_80.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_80.itemSize = 3L
    shipBuilder_vehicleitem_80.views = 0L
    shipBuilder_vehicleitem_80 = importer.save_or_locate(shipBuilder_vehicleitem_80)

    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_208)
    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_209)
    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_210)
    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_211)
    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_212)
    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_213)
    shipBuilder_vehicleitem_80.itemStats.add(shipBuilder_vehicleitemparams_214)

    shipBuilder_vehicleitem_81 = VehicleItem()
    shipBuilder_vehicleitem_81.itemClass = 0L
    shipBuilder_vehicleitem_81.description = u'The X-Forge P/S2-80 is a small thruster that mainly finds use on Aurora class starships. Boasting good thrust output and fuel efficiency, the P/S2-80 is an excellent choice for those with a bit of wanderlust.'
    shipBuilder_vehicleitem_81.name = u'XForge_PS2_80'
    shipBuilder_vehicleitem_81.displayName = u'XForge P/S2-80 Main Engine'
    shipBuilder_vehicleitem_81.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_81.itemSubType = shipBuilder_vehicleitemsubtype_11
    shipBuilder_vehicleitem_81.manufacturer = shipBuilder_manufacturer_46
    shipBuilder_vehicleitem_81.itemSize = 2L
    shipBuilder_vehicleitem_81.views = 0L
    shipBuilder_vehicleitem_81 = importer.save_or_locate(shipBuilder_vehicleitem_81)

    shipBuilder_vehicleitem_81.itemStats.add(shipBuilder_vehicleitemparams_215)
    shipBuilder_vehicleitem_81.itemStats.add(shipBuilder_vehicleitemparams_216)
    shipBuilder_vehicleitem_81.itemStats.add(shipBuilder_vehicleitemparams_217)

    shipBuilder_vehicleitem_82 = VehicleItem()
    shipBuilder_vehicleitem_82.itemClass = 0L
    shipBuilder_vehicleitem_82.description = u''
    shipBuilder_vehicleitem_82.name = u'RSI_DefaultRadarLongRange'
    shipBuilder_vehicleitem_82.displayName = u'RSI Radar Long Range'
    shipBuilder_vehicleitem_82.itemType = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitem_82.itemSubType = shipBuilder_vehicleitemsubtype_17
    shipBuilder_vehicleitem_82.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_82.itemSize = 1L
    shipBuilder_vehicleitem_82.views = 0L
    shipBuilder_vehicleitem_82 = importer.save_or_locate(shipBuilder_vehicleitem_82)

    shipBuilder_vehicleitem_82.itemStats.add(shipBuilder_vehicleitemparams_218)
    shipBuilder_vehicleitem_82.itemStats.add(shipBuilder_vehicleitemparams_219)
    shipBuilder_vehicleitem_82.itemStats.add(shipBuilder_vehicleitemparams_220)
    shipBuilder_vehicleitem_82.itemStats.add(shipBuilder_vehicleitemparams_221)
    shipBuilder_vehicleitem_82.itemStats.add(shipBuilder_vehicleitemparams_222)

    shipBuilder_vehicleitem_83 = VehicleItem()
    shipBuilder_vehicleitem_83.itemClass = 0L
    shipBuilder_vehicleitem_83.description = u'The Hammer Propulsion HE5.3 features a high output, fuel efficient design. Its thrust output and low fuel consumption make it ideal for long hauls though it has been reported to be somewhat of a missile magnet on occasions where owners have been subject to pirate activity.'
    shipBuilder_vehicleitem_83.name = u'325a_Hammer_Propulsion_HE_5_3'
    shipBuilder_vehicleitem_83.displayName = u'Hammer Propulsion HE 5.3'
    shipBuilder_vehicleitem_83.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_83.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_83.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_83.itemSize = 3L
    shipBuilder_vehicleitem_83.views = 0L
    shipBuilder_vehicleitem_83 = importer.save_or_locate(shipBuilder_vehicleitem_83)

    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_223)
    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_224)
    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_225)
    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_226)
    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_227)
    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_228)
    shipBuilder_vehicleitem_83.itemStats.add(shipBuilder_vehicleitemparams_229)

    shipBuilder_vehicleitem_84 = VehicleItem()
    shipBuilder_vehicleitem_84.itemClass = 0L
    shipBuilder_vehicleitem_84.description = u'MaxOx\u2019s NN-13 Neutron Gun offers a massive energy payload at the expense of speed and energy efficiency. One could argue the virtues of speed, rate of fire and distance over damage, but the argument becomes irrelevant if you only need to hit them once.'
    shipBuilder_vehicleitem_84.name = u'K_W_CF_117_Badger_Repeater_Laser_Turret'
    shipBuilder_vehicleitem_84.displayName = u'CF-117 Badger Repeater Laser Turret'
    shipBuilder_vehicleitem_84.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_84.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_84.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_84.itemSize = 2L
    shipBuilder_vehicleitem_84.views = 0L
    shipBuilder_vehicleitem_84 = importer.save_or_locate(shipBuilder_vehicleitem_84)

    shipBuilder_vehicleitem_84.power.add(shipBuilder_vehicleitempower_91)
    shipBuilder_vehicleitem_84.power.add(shipBuilder_vehicleitempower_92)
    shipBuilder_vehicleitem_84.power.add(shipBuilder_vehicleitempower_93)
    shipBuilder_vehicleitem_84.heat.add(shipBuilder_vehicleitemheat_74)
    shipBuilder_vehicleitem_84.heat.add(shipBuilder_vehicleitemheat_75)
    shipBuilder_vehicleitem_84.heat.add(shipBuilder_vehicleitemheat_76)
    shipBuilder_vehicleitem_84.avionics.add(shipBuilder_vehicleitemavionics_49)
    shipBuilder_vehicleitem_84.avionics.add(shipBuilder_vehicleitemavionics_50)

    shipBuilder_vehicleitem_85 = VehicleItem()
    shipBuilder_vehicleitem_85.itemClass = 0L
    shipBuilder_vehicleitem_85.description = u"A&R's LR-5 OverDrive is your gateway to the world of fusion-based power plants. Designed to be a rugged, high-output alternative to other power sources, the LR-5 OverDrive does suffer from an above average generation of heat."
    shipBuilder_vehicleitem_85.name = u'A_and_R_LR-5_OverDrive'
    shipBuilder_vehicleitem_85.displayName = u'A&R LR-5 OverDrive'
    shipBuilder_vehicleitem_85.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_85.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_85.manufacturer = shipBuilder_manufacturer_5
    shipBuilder_vehicleitem_85.itemSize = 1L
    shipBuilder_vehicleitem_85.views = 0L
    shipBuilder_vehicleitem_85 = importer.save_or_locate(shipBuilder_vehicleitem_85)

    shipBuilder_vehicleitem_85.power.add(shipBuilder_vehicleitempower_94)

    shipBuilder_vehicleitem_86 = VehicleItem()
    shipBuilder_vehicleitem_86.itemClass = 0L
    shipBuilder_vehicleitem_86.description = u''
    shipBuilder_vehicleitem_86.name = u'RSI_DefaultBattery'
    shipBuilder_vehicleitem_86.displayName = u'RSI Battery'
    shipBuilder_vehicleitem_86.itemType = shipBuilder_vehicleitemtype_10
    shipBuilder_vehicleitem_86.itemSubType = shipBuilder_vehicleitemsubtype_18
    shipBuilder_vehicleitem_86.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_86.itemSize = 1L
    shipBuilder_vehicleitem_86.views = 0L
    shipBuilder_vehicleitem_86 = importer.save_or_locate(shipBuilder_vehicleitem_86)

    shipBuilder_vehicleitem_86.itemStats.add(shipBuilder_vehicleitemparams_230)
    shipBuilder_vehicleitem_86.itemStats.add(shipBuilder_vehicleitemparams_231)
    shipBuilder_vehicleitem_86.itemStats.add(shipBuilder_vehicleitemparams_232)

    shipBuilder_vehicleitem_87 = VehicleItem()
    shipBuilder_vehicleitem_87.itemClass = 0L
    shipBuilder_vehicleitem_87.description = u''
    shipBuilder_vehicleitem_87.name = u'RSI_DefaultRadarShortRange'
    shipBuilder_vehicleitem_87.displayName = u'RSI Radar Short Range'
    shipBuilder_vehicleitem_87.itemType = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitem_87.itemSubType = shipBuilder_vehicleitemsubtype_19
    shipBuilder_vehicleitem_87.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_87.itemSize = 1L
    shipBuilder_vehicleitem_87.views = 0L
    shipBuilder_vehicleitem_87 = importer.save_or_locate(shipBuilder_vehicleitem_87)

    shipBuilder_vehicleitem_87.itemStats.add(shipBuilder_vehicleitemparams_233)
    shipBuilder_vehicleitem_87.itemStats.add(shipBuilder_vehicleitemparams_234)
    shipBuilder_vehicleitem_87.itemStats.add(shipBuilder_vehicleitemparams_235)
    shipBuilder_vehicleitem_87.itemStats.add(shipBuilder_vehicleitemparams_236)
    shipBuilder_vehicleitem_87.itemStats.add(shipBuilder_vehicleitemparams_237)

    shipBuilder_vehicleitem_88 = VehicleItem()
    shipBuilder_vehicleitem_88.itemClass = 1L
    shipBuilder_vehicleitem_88.description = u"The CF-227 Panther is a grinder. The mid-range model of Klaus and Werner's repeaters, the Panther is the definition of a fire-and-forget weapon. Its impressive rate of fire and respectable power consumption make the Panther an effective combat solution for all ship sizes."
    shipBuilder_vehicleitem_88.name = u'K_and_W_CF-227_Panther_Repeater'
    shipBuilder_vehicleitem_88.displayName = u'CF-227 Panther Repeater'
    shipBuilder_vehicleitem_88.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_88.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_88.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_88.itemSize = 3L
    shipBuilder_vehicleitem_88.views = 0L
    shipBuilder_vehicleitem_88 = importer.save_or_locate(shipBuilder_vehicleitem_88)

    shipBuilder_vehicleitem_88.power.add(shipBuilder_vehicleitempower_95)
    shipBuilder_vehicleitem_88.power.add(shipBuilder_vehicleitempower_96)
    shipBuilder_vehicleitem_88.power.add(shipBuilder_vehicleitempower_97)
    shipBuilder_vehicleitem_88.heat.add(shipBuilder_vehicleitemheat_77)
    shipBuilder_vehicleitem_88.heat.add(shipBuilder_vehicleitemheat_78)
    shipBuilder_vehicleitem_88.heat.add(shipBuilder_vehicleitemheat_79)
    shipBuilder_vehicleitem_88.avionics.add(shipBuilder_vehicleitemavionics_51)
    shipBuilder_vehicleitem_88.avionics.add(shipBuilder_vehicleitemavionics_52)
    shipBuilder_vehicleitem_88.itemStats.add(shipBuilder_vehicleitemparams_238)
    shipBuilder_vehicleitem_88.itemStats.add(shipBuilder_vehicleitemparams_239)
    shipBuilder_vehicleitem_88.itemStats.add(shipBuilder_vehicleitemparams_240)
    shipBuilder_vehicleitem_88.itemStats.add(shipBuilder_vehicleitemparams_241)

    shipBuilder_vehicleitem_89 = VehicleItem()
    shipBuilder_vehicleitem_89.itemClass = 0L
    shipBuilder_vehicleitem_89.description = u'Made with the same rugged construction techniques as the smaller 5 ton model, the Stor-All model A Big Box cargo pod upgrade for the Aurora doubles the available cargo space. (Replaces default cargo option.)'
    shipBuilder_vehicleitem_89.name = u'Stor-All_Big_Box_Model_A'
    shipBuilder_vehicleitem_89.displayName = u'Stor-All Big Box Model A'
    shipBuilder_vehicleitem_89.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_89.itemSubType = shipBuilder_vehicleitemsubtype_1
    shipBuilder_vehicleitem_89.manufacturer = shipBuilder_manufacturer_24
    shipBuilder_vehicleitem_89.itemSize = 4L
    shipBuilder_vehicleitem_89.views = 2L
    shipBuilder_vehicleitem_89 = importer.save_or_locate(shipBuilder_vehicleitem_89)

    #Processing model: VehicleCategory

    from shipBuilder.models import VehicleCategory

    shipBuilder_vehiclecategory_1 = VehicleCategory()
    shipBuilder_vehiclecategory_1.name = u'Transport'
    shipBuilder_vehiclecategory_1 = importer.save_or_locate(shipBuilder_vehiclecategory_1)

    shipBuilder_vehiclecategory_2 = VehicleCategory()
    shipBuilder_vehiclecategory_2.name = u'StarFighter'
    shipBuilder_vehiclecategory_2 = importer.save_or_locate(shipBuilder_vehiclecategory_2)

    shipBuilder_vehiclecategory_3 = VehicleCategory()
    shipBuilder_vehiclecategory_3.name = u'Star Fighter'
    shipBuilder_vehiclecategory_3 = importer.save_or_locate(shipBuilder_vehiclecategory_3)

    #Processing model: Vehicle

    from shipBuilder.models import Vehicle

    shipBuilder_vehicle_1 = Vehicle()
    shipBuilder_vehicle_1.vehicleClass = 3L
    shipBuilder_vehicle_1.category = shipBuilder_vehiclecategory_1
    shipBuilder_vehicle_1.displayName = u'MISC Freelancer'
    shipBuilder_vehicle_1.name = u'MISC_Freelancer'
    shipBuilder_vehicle_1.views = 1L
    shipBuilder_vehicle_1.upgradeSlots = 0L
    shipBuilder_vehicle_1.maximum_crew = 1L
    shipBuilder_vehicle_1.empty_mass = 0L
    shipBuilder_vehicle_1.length = 0.0
    shipBuilder_vehicle_1.width = 0.0
    shipBuilder_vehicle_1.height = 0.0
    shipBuilder_vehicle_1.thumbnail = u''
    shipBuilder_vehicle_1.available = False
    shipBuilder_vehicle_1.manufacturer = None
    shipBuilder_vehicle_1 = importer.save_or_locate(shipBuilder_vehicle_1)

    shipBuilder_vehicle_2 = Vehicle()
    shipBuilder_vehicle_2.vehicleClass = 2L
    shipBuilder_vehicle_2.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_2.displayName = u'Anvil Hornet'
    shipBuilder_vehicle_2.name = u'Anvil_Hornet'
    shipBuilder_vehicle_2.views = 1L
    shipBuilder_vehicle_2.upgradeSlots = 0L
    shipBuilder_vehicle_2.maximum_crew = 1L
    shipBuilder_vehicle_2.empty_mass = 0L
    shipBuilder_vehicle_2.length = 0.0
    shipBuilder_vehicle_2.width = 0.0
    shipBuilder_vehicle_2.height = 0.0
    shipBuilder_vehicle_2.thumbnail = u''
    shipBuilder_vehicle_2.available = False
    shipBuilder_vehicle_2.manufacturer = None
    shipBuilder_vehicle_2 = importer.save_or_locate(shipBuilder_vehicle_2)

    shipBuilder_vehicle_3 = Vehicle()
    shipBuilder_vehicle_3.vehicleClass = 3L
    shipBuilder_vehicle_3.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_3.displayName = u'RSI Constellation'
    shipBuilder_vehicle_3.name = u'RSI_Constellation'
    shipBuilder_vehicle_3.views = 3L
    shipBuilder_vehicle_3.upgradeSlots = 0L
    shipBuilder_vehicle_3.maximum_crew = 1L
    shipBuilder_vehicle_3.empty_mass = 0L
    shipBuilder_vehicle_3.length = 0.0
    shipBuilder_vehicle_3.width = 0.0
    shipBuilder_vehicle_3.height = 0.0
    shipBuilder_vehicle_3.thumbnail = u''
    shipBuilder_vehicle_3.available = False
    shipBuilder_vehicle_3.manufacturer = None
    shipBuilder_vehicle_3 = importer.save_or_locate(shipBuilder_vehicle_3)

    shipBuilder_vehicle_4 = Vehicle()
    shipBuilder_vehicle_4.vehicleClass = 1L
    shipBuilder_vehicle_4.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_4.displayName = u'RSI Aurora LX'
    shipBuilder_vehicle_4.name = u'RSI_Aurora_LX'
    shipBuilder_vehicle_4.views = 1L
    shipBuilder_vehicle_4.upgradeSlots = 0L
    shipBuilder_vehicle_4.maximum_crew = 1L
    shipBuilder_vehicle_4.empty_mass = 0L
    shipBuilder_vehicle_4.length = 0.0
    shipBuilder_vehicle_4.width = 0.0
    shipBuilder_vehicle_4.height = 0.0
    shipBuilder_vehicle_4.thumbnail = u''
    shipBuilder_vehicle_4.available = False
    shipBuilder_vehicle_4.manufacturer = None
    shipBuilder_vehicle_4 = importer.save_or_locate(shipBuilder_vehicle_4)

    shipBuilder_vehicle_5 = Vehicle()
    shipBuilder_vehicle_5.vehicleClass = 1L
    shipBuilder_vehicle_5.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_5.displayName = u'RSI Aurora ES'
    shipBuilder_vehicle_5.name = u'RSI_Aurora_ES'
    shipBuilder_vehicle_5.views = 2L
    shipBuilder_vehicle_5.upgradeSlots = 0L
    shipBuilder_vehicle_5.maximum_crew = 1L
    shipBuilder_vehicle_5.empty_mass = 0L
    shipBuilder_vehicle_5.length = 0.0
    shipBuilder_vehicle_5.width = 0.0
    shipBuilder_vehicle_5.height = 0.0
    shipBuilder_vehicle_5.thumbnail = u''
    shipBuilder_vehicle_5.available = False
    shipBuilder_vehicle_5.manufacturer = None
    shipBuilder_vehicle_5 = importer.save_or_locate(shipBuilder_vehicle_5)

    shipBuilder_vehicle_6 = Vehicle()
    shipBuilder_vehicle_6.vehicleClass = 2L
    shipBuilder_vehicle_6.category = shipBuilder_vehiclecategory_3
    shipBuilder_vehicle_6.displayName = u'Anvil Hornet F7C'
    shipBuilder_vehicle_6.name = u'Anvil_Hornet_F7C'
    shipBuilder_vehicle_6.views = 1L
    shipBuilder_vehicle_6.upgradeSlots = 0L
    shipBuilder_vehicle_6.maximum_crew = 1L
    shipBuilder_vehicle_6.empty_mass = 0L
    shipBuilder_vehicle_6.length = 0.0
    shipBuilder_vehicle_6.width = 0.0
    shipBuilder_vehicle_6.height = 0.0
    shipBuilder_vehicle_6.thumbnail = u''
    shipBuilder_vehicle_6.available = False
    shipBuilder_vehicle_6.manufacturer = None
    shipBuilder_vehicle_6 = importer.save_or_locate(shipBuilder_vehicle_6)

    shipBuilder_vehicle_7 = Vehicle()
    shipBuilder_vehicle_7.vehicleClass = 2L
    shipBuilder_vehicle_7.category = shipBuilder_vehiclecategory_3
    shipBuilder_vehicle_7.displayName = u'Origin Jumpworks 350r'
    shipBuilder_vehicle_7.name = u'OJ_350r'
    shipBuilder_vehicle_7.views = 0L
    shipBuilder_vehicle_7.upgradeSlots = 0L
    shipBuilder_vehicle_7.maximum_crew = 1L
    shipBuilder_vehicle_7.empty_mass = 0L
    shipBuilder_vehicle_7.length = 0.0
    shipBuilder_vehicle_7.width = 0.0
    shipBuilder_vehicle_7.height = 0.0
    shipBuilder_vehicle_7.thumbnail = u''
    shipBuilder_vehicle_7.available = False
    shipBuilder_vehicle_7.manufacturer = None
    shipBuilder_vehicle_7 = importer.save_or_locate(shipBuilder_vehicle_7)

    shipBuilder_vehicle_8 = Vehicle()
    shipBuilder_vehicle_8.vehicleClass = 3L
    shipBuilder_vehicle_8.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_8.displayName = u'Origin JumpWorks 315p'
    shipBuilder_vehicle_8.name = u'OJ_315p'
    shipBuilder_vehicle_8.views = 0L
    shipBuilder_vehicle_8.upgradeSlots = 0L
    shipBuilder_vehicle_8.maximum_crew = 1L
    shipBuilder_vehicle_8.empty_mass = 0L
    shipBuilder_vehicle_8.length = 0.0
    shipBuilder_vehicle_8.width = 0.0
    shipBuilder_vehicle_8.height = 0.0
    shipBuilder_vehicle_8.thumbnail = u''
    shipBuilder_vehicle_8.available = False
    shipBuilder_vehicle_8.manufacturer = None
    shipBuilder_vehicle_8 = importer.save_or_locate(shipBuilder_vehicle_8)

    shipBuilder_vehicle_9 = Vehicle()
    shipBuilder_vehicle_9.vehicleClass = 1L
    shipBuilder_vehicle_9.category = shipBuilder_vehiclecategory_3
    shipBuilder_vehicle_9.displayName = u'RSI Aurora MR'
    shipBuilder_vehicle_9.name = u'RSI_Aurora_MR'
    shipBuilder_vehicle_9.views = 0L
    shipBuilder_vehicle_9.upgradeSlots = 0L
    shipBuilder_vehicle_9.maximum_crew = 1L
    shipBuilder_vehicle_9.empty_mass = 0L
    shipBuilder_vehicle_9.length = 0.0
    shipBuilder_vehicle_9.width = 0.0
    shipBuilder_vehicle_9.height = 0.0
    shipBuilder_vehicle_9.thumbnail = u''
    shipBuilder_vehicle_9.available = False
    shipBuilder_vehicle_9.manufacturer = None
    shipBuilder_vehicle_9 = importer.save_or_locate(shipBuilder_vehicle_9)

    shipBuilder_vehicle_10 = Vehicle()
    shipBuilder_vehicle_10.vehicleClass = 3L
    shipBuilder_vehicle_10.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_10.displayName = u'Origin JumpWorks 300i'
    shipBuilder_vehicle_10.name = u'OJ_300i'
    shipBuilder_vehicle_10.views = 1L
    shipBuilder_vehicle_10.upgradeSlots = 0L
    shipBuilder_vehicle_10.maximum_crew = 1L
    shipBuilder_vehicle_10.empty_mass = 0L
    shipBuilder_vehicle_10.length = 0.0
    shipBuilder_vehicle_10.width = 0.0
    shipBuilder_vehicle_10.height = 0.0
    shipBuilder_vehicle_10.thumbnail = u''
    shipBuilder_vehicle_10.available = False
    shipBuilder_vehicle_10.manufacturer = None
    shipBuilder_vehicle_10 = importer.save_or_locate(shipBuilder_vehicle_10)

    shipBuilder_vehicle_11 = Vehicle()
    shipBuilder_vehicle_11.vehicleClass = 1L
    shipBuilder_vehicle_11.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_11.displayName = u'RSI Aurora CL'
    shipBuilder_vehicle_11.name = u'RSI_Aurora_CL'
    shipBuilder_vehicle_11.views = 0L
    shipBuilder_vehicle_11.upgradeSlots = 0L
    shipBuilder_vehicle_11.maximum_crew = 1L
    shipBuilder_vehicle_11.empty_mass = 0L
    shipBuilder_vehicle_11.length = 0.0
    shipBuilder_vehicle_11.width = 0.0
    shipBuilder_vehicle_11.height = 0.0
    shipBuilder_vehicle_11.thumbnail = u''
    shipBuilder_vehicle_11.available = False
    shipBuilder_vehicle_11.manufacturer = None
    shipBuilder_vehicle_11 = importer.save_or_locate(shipBuilder_vehicle_11)

    shipBuilder_vehicle_12 = Vehicle()
    shipBuilder_vehicle_12.vehicleClass = 3L
    shipBuilder_vehicle_12.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_12.displayName = u'Origin JumpWorks 325a'
    shipBuilder_vehicle_12.name = u'OJ_325a'
    shipBuilder_vehicle_12.views = 0L
    shipBuilder_vehicle_12.upgradeSlots = 0L
    shipBuilder_vehicle_12.maximum_crew = 1L
    shipBuilder_vehicle_12.empty_mass = 0L
    shipBuilder_vehicle_12.length = 0.0
    shipBuilder_vehicle_12.width = 0.0
    shipBuilder_vehicle_12.height = 0.0
    shipBuilder_vehicle_12.thumbnail = u''
    shipBuilder_vehicle_12.available = False
    shipBuilder_vehicle_12.manufacturer = None
    shipBuilder_vehicle_12 = importer.save_or_locate(shipBuilder_vehicle_12)

    #Processing model: MigrationHistory

    from south.models import MigrationHistory


    #Processing model: LogEntry

    from django.contrib.admin.models import LogEntry


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

    #Processing model: VehicleImage

    from shipBuilder.models import VehicleImage


    #Processing model: ItemPort

    from shipBuilder.models import ItemPort

    shipBuilder_itemport_1 = ItemPort()
    shipBuilder_itemport_1.displayName = None
    shipBuilder_itemport_1.name = u''
    shipBuilder_itemport_1.flags = u''
    shipBuilder_itemport_1.maxSize = 1L
    shipBuilder_itemport_1.minSize = 0L
    shipBuilder_itemport_1.parentVehicle = None
    shipBuilder_itemport_1.portClass = 0L
    shipBuilder_itemport_1.image = None
    shipBuilder_itemport_1.tagLocationX = 0L
    shipBuilder_itemport_1.tagLocationY = 0L
    shipBuilder_itemport_1 = importer.save_or_locate(shipBuilder_itemport_1)

    shipBuilder_itemport_2 = ItemPort()
    shipBuilder_itemport_2.displayName = u'Power Plant'
    shipBuilder_itemport_2.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_2.flags = u'main rear'
    shipBuilder_itemport_2.maxSize = 5L
    shipBuilder_itemport_2.minSize = 3L
    shipBuilder_itemport_2.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_2.portClass = 0L
    shipBuilder_itemport_2.image = None
    shipBuilder_itemport_2.tagLocationX = 0L
    shipBuilder_itemport_2.tagLocationY = 0L
    shipBuilder_itemport_2 = importer.save_or_locate(shipBuilder_itemport_2)

    shipBuilder_itemport_2.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_3 = ItemPort()
    shipBuilder_itemport_3.displayName = None
    shipBuilder_itemport_3.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_3.flags = u'main rear'
    shipBuilder_itemport_3.maxSize = 5L
    shipBuilder_itemport_3.minSize = 4L
    shipBuilder_itemport_3.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_3.portClass = 0L
    shipBuilder_itemport_3.image = None
    shipBuilder_itemport_3.tagLocationX = 0L
    shipBuilder_itemport_3.tagLocationY = 0L
    shipBuilder_itemport_3 = importer.save_or_locate(shipBuilder_itemport_3)

    shipBuilder_itemport_3.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_4 = ItemPort()
    shipBuilder_itemport_4.displayName = None
    shipBuilder_itemport_4.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_4.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_4.maxSize = 2L
    shipBuilder_itemport_4.minSize = 1L
    shipBuilder_itemport_4.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_4.portClass = 0L
    shipBuilder_itemport_4.image = None
    shipBuilder_itemport_4.tagLocationX = 0L
    shipBuilder_itemport_4.tagLocationY = 0L
    shipBuilder_itemport_4 = importer.save_or_locate(shipBuilder_itemport_4)

    shipBuilder_itemport_4.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_5 = ItemPort()
    shipBuilder_itemport_5.displayName = None
    shipBuilder_itemport_5.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_5.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_5.maxSize = 2L
    shipBuilder_itemport_5.minSize = 1L
    shipBuilder_itemport_5.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_5.portClass = 0L
    shipBuilder_itemport_5.image = None
    shipBuilder_itemport_5.tagLocationX = 0L
    shipBuilder_itemport_5.tagLocationY = 0L
    shipBuilder_itemport_5 = importer.save_or_locate(shipBuilder_itemport_5)

    shipBuilder_itemport_5.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_6 = ItemPort()
    shipBuilder_itemport_6.displayName = None
    shipBuilder_itemport_6.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_6.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_6.maxSize = 2L
    shipBuilder_itemport_6.minSize = 1L
    shipBuilder_itemport_6.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_6.portClass = 0L
    shipBuilder_itemport_6.image = None
    shipBuilder_itemport_6.tagLocationX = 0L
    shipBuilder_itemport_6.tagLocationY = 0L
    shipBuilder_itemport_6 = importer.save_or_locate(shipBuilder_itemport_6)

    shipBuilder_itemport_6.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_7 = ItemPort()
    shipBuilder_itemport_7.displayName = None
    shipBuilder_itemport_7.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_7.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_7.maxSize = 2L
    shipBuilder_itemport_7.minSize = 1L
    shipBuilder_itemport_7.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_7.portClass = 0L
    shipBuilder_itemport_7.image = None
    shipBuilder_itemport_7.tagLocationX = 0L
    shipBuilder_itemport_7.tagLocationY = 0L
    shipBuilder_itemport_7 = importer.save_or_locate(shipBuilder_itemport_7)

    shipBuilder_itemport_7.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_8 = ItemPort()
    shipBuilder_itemport_8.displayName = None
    shipBuilder_itemport_8.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_8.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_8.maxSize = 2L
    shipBuilder_itemport_8.minSize = 1L
    shipBuilder_itemport_8.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_8.portClass = 0L
    shipBuilder_itemport_8.image = None
    shipBuilder_itemport_8.tagLocationX = 0L
    shipBuilder_itemport_8.tagLocationY = 0L
    shipBuilder_itemport_8 = importer.save_or_locate(shipBuilder_itemport_8)

    shipBuilder_itemport_8.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_9 = ItemPort()
    shipBuilder_itemport_9.displayName = None
    shipBuilder_itemport_9.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_9.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_9.maxSize = 2L
    shipBuilder_itemport_9.minSize = 1L
    shipBuilder_itemport_9.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_9.portClass = 0L
    shipBuilder_itemport_9.image = None
    shipBuilder_itemport_9.tagLocationX = 0L
    shipBuilder_itemport_9.tagLocationY = 0L
    shipBuilder_itemport_9 = importer.save_or_locate(shipBuilder_itemport_9)

    shipBuilder_itemport_9.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_10 = ItemPort()
    shipBuilder_itemport_10.displayName = None
    shipBuilder_itemport_10.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_10.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_10.maxSize = 2L
    shipBuilder_itemport_10.minSize = 1L
    shipBuilder_itemport_10.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_10.portClass = 0L
    shipBuilder_itemport_10.image = None
    shipBuilder_itemport_10.tagLocationX = 0L
    shipBuilder_itemport_10.tagLocationY = 0L
    shipBuilder_itemport_10 = importer.save_or_locate(shipBuilder_itemport_10)

    shipBuilder_itemport_10.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_11 = ItemPort()
    shipBuilder_itemport_11.displayName = None
    shipBuilder_itemport_11.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_11.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_11.maxSize = 2L
    shipBuilder_itemport_11.minSize = 1L
    shipBuilder_itemport_11.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_11.portClass = 0L
    shipBuilder_itemport_11.image = None
    shipBuilder_itemport_11.tagLocationX = 0L
    shipBuilder_itemport_11.tagLocationY = 0L
    shipBuilder_itemport_11 = importer.save_or_locate(shipBuilder_itemport_11)

    shipBuilder_itemport_11.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_12 = ItemPort()
    shipBuilder_itemport_12.displayName = None
    shipBuilder_itemport_12.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_12.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_12.maxSize = 2L
    shipBuilder_itemport_12.minSize = 1L
    shipBuilder_itemport_12.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_12.portClass = 0L
    shipBuilder_itemport_12.image = None
    shipBuilder_itemport_12.tagLocationX = 0L
    shipBuilder_itemport_12.tagLocationY = 0L
    shipBuilder_itemport_12 = importer.save_or_locate(shipBuilder_itemport_12)

    shipBuilder_itemport_12.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_13 = ItemPort()
    shipBuilder_itemport_13.displayName = None
    shipBuilder_itemport_13.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_13.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_13.maxSize = 2L
    shipBuilder_itemport_13.minSize = 1L
    shipBuilder_itemport_13.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_13.portClass = 0L
    shipBuilder_itemport_13.image = None
    shipBuilder_itemport_13.tagLocationX = 0L
    shipBuilder_itemport_13.tagLocationY = 0L
    shipBuilder_itemport_13 = importer.save_or_locate(shipBuilder_itemport_13)

    shipBuilder_itemport_13.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_14 = ItemPort()
    shipBuilder_itemport_14.displayName = None
    shipBuilder_itemport_14.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_14.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_14.maxSize = 2L
    shipBuilder_itemport_14.minSize = 1L
    shipBuilder_itemport_14.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_14.portClass = 0L
    shipBuilder_itemport_14.image = None
    shipBuilder_itemport_14.tagLocationX = 0L
    shipBuilder_itemport_14.tagLocationY = 0L
    shipBuilder_itemport_14 = importer.save_or_locate(shipBuilder_itemport_14)

    shipBuilder_itemport_14.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_15 = ItemPort()
    shipBuilder_itemport_15.displayName = None
    shipBuilder_itemport_15.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_15.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_15.maxSize = 2L
    shipBuilder_itemport_15.minSize = 1L
    shipBuilder_itemport_15.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_15.portClass = 0L
    shipBuilder_itemport_15.image = None
    shipBuilder_itemport_15.tagLocationX = 0L
    shipBuilder_itemport_15.tagLocationY = 0L
    shipBuilder_itemport_15 = importer.save_or_locate(shipBuilder_itemport_15)

    shipBuilder_itemport_15.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_16 = ItemPort()
    shipBuilder_itemport_16.displayName = u'Left Class 2 Mount Top'
    shipBuilder_itemport_16.name = u'Freelancer_side_cannon_L_Hardpoint'
    shipBuilder_itemport_16.flags = u'left side top'
    shipBuilder_itemport_16.maxSize = 5L
    shipBuilder_itemport_16.minSize = 3L
    shipBuilder_itemport_16.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_16.portClass = 0L
    shipBuilder_itemport_16.image = None
    shipBuilder_itemport_16.tagLocationX = 0L
    shipBuilder_itemport_16.tagLocationY = 0L
    shipBuilder_itemport_16 = importer.save_or_locate(shipBuilder_itemport_16)

    shipBuilder_itemport_16.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_16.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_17 = ItemPort()
    shipBuilder_itemport_17.displayName = u'Left Class 2 Mount Bottom'
    shipBuilder_itemport_17.name = u'Freelancer_side_cannon_L_Bottom_Hardpoint'
    shipBuilder_itemport_17.flags = u'left side bottom'
    shipBuilder_itemport_17.maxSize = 5L
    shipBuilder_itemport_17.minSize = 3L
    shipBuilder_itemport_17.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_17.portClass = 0L
    shipBuilder_itemport_17.image = None
    shipBuilder_itemport_17.tagLocationX = 0L
    shipBuilder_itemport_17.tagLocationY = 0L
    shipBuilder_itemport_17 = importer.save_or_locate(shipBuilder_itemport_17)

    shipBuilder_itemport_17.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_17.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_18 = ItemPort()
    shipBuilder_itemport_18.displayName = u'Right Class 2 Mount Top'
    shipBuilder_itemport_18.name = u'Freelancer_side_cannon_R_Hardpoint'
    shipBuilder_itemport_18.flags = u'right side top'
    shipBuilder_itemport_18.maxSize = 5L
    shipBuilder_itemport_18.minSize = 3L
    shipBuilder_itemport_18.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_18.portClass = 0L
    shipBuilder_itemport_18.image = None
    shipBuilder_itemport_18.tagLocationX = 0L
    shipBuilder_itemport_18.tagLocationY = 0L
    shipBuilder_itemport_18 = importer.save_or_locate(shipBuilder_itemport_18)

    shipBuilder_itemport_18.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_18.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_19 = ItemPort()
    shipBuilder_itemport_19.displayName = u'Right Class 2 Mount Bottom'
    shipBuilder_itemport_19.name = u'Freelancer_side_cannon_R_Bottom_Hardpoint'
    shipBuilder_itemport_19.flags = u'right side bottom'
    shipBuilder_itemport_19.maxSize = 5L
    shipBuilder_itemport_19.minSize = 3L
    shipBuilder_itemport_19.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_19.portClass = 0L
    shipBuilder_itemport_19.image = None
    shipBuilder_itemport_19.tagLocationX = 0L
    shipBuilder_itemport_19.tagLocationY = 0L
    shipBuilder_itemport_19 = importer.save_or_locate(shipBuilder_itemport_19)

    shipBuilder_itemport_19.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_19.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_20 = ItemPort()
    shipBuilder_itemport_20.displayName = u'Top Turret Slot'
    shipBuilder_itemport_20.name = u'hardpoint_class_4_cannonball'
    shipBuilder_itemport_20.flags = u'front nose'
    shipBuilder_itemport_20.maxSize = 4L
    shipBuilder_itemport_20.minSize = 1L
    shipBuilder_itemport_20.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_20.portClass = 0L
    shipBuilder_itemport_20.image = None
    shipBuilder_itemport_20.tagLocationX = 0L
    shipBuilder_itemport_20.tagLocationY = 0L
    shipBuilder_itemport_20 = importer.save_or_locate(shipBuilder_itemport_20)

    shipBuilder_itemport_20.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_20.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)

    shipBuilder_itemport_21 = ItemPort()
    shipBuilder_itemport_21.displayName = u'Left Bay Slot'
    shipBuilder_itemport_21.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_21.flags = u'left bottom'
    shipBuilder_itemport_21.maxSize = 3L
    shipBuilder_itemport_21.minSize = 1L
    shipBuilder_itemport_21.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_21.portClass = 0L
    shipBuilder_itemport_21.image = None
    shipBuilder_itemport_21.tagLocationX = 0L
    shipBuilder_itemport_21.tagLocationY = 0L
    shipBuilder_itemport_21 = importer.save_or_locate(shipBuilder_itemport_21)

    shipBuilder_itemport_21.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_21.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_22 = ItemPort()
    shipBuilder_itemport_22.displayName = u'Right Bay Slot'
    shipBuilder_itemport_22.name = u'hardpoint_class_3_right_bay_door'
    shipBuilder_itemport_22.flags = u'right bottom'
    shipBuilder_itemport_22.maxSize = 3L
    shipBuilder_itemport_22.minSize = 1L
    shipBuilder_itemport_22.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_22.portClass = 0L
    shipBuilder_itemport_22.image = None
    shipBuilder_itemport_22.tagLocationX = 0L
    shipBuilder_itemport_22.tagLocationY = 0L
    shipBuilder_itemport_22 = importer.save_or_locate(shipBuilder_itemport_22)

    shipBuilder_itemport_22.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_22.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_23 = ItemPort()
    shipBuilder_itemport_23.displayName = u'Power Plant'
    shipBuilder_itemport_23.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_23.flags = u''
    shipBuilder_itemport_23.maxSize = 4L
    shipBuilder_itemport_23.minSize = 1L
    shipBuilder_itemport_23.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_23.portClass = 0L
    shipBuilder_itemport_23.image = None
    shipBuilder_itemport_23.tagLocationX = 0L
    shipBuilder_itemport_23.tagLocationY = 0L
    shipBuilder_itemport_23 = importer.save_or_locate(shipBuilder_itemport_23)

    shipBuilder_itemport_23.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_24 = ItemPort()
    shipBuilder_itemport_24.displayName = None
    shipBuilder_itemport_24.name = u'Port_Thruster_Main_TR4'
    shipBuilder_itemport_24.flags = u'main rear'
    shipBuilder_itemport_24.maxSize = 4L
    shipBuilder_itemport_24.minSize = 4L
    shipBuilder_itemport_24.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_24.portClass = 0L
    shipBuilder_itemport_24.image = None
    shipBuilder_itemport_24.tagLocationX = 0L
    shipBuilder_itemport_24.tagLocationY = 0L
    shipBuilder_itemport_24 = importer.save_or_locate(shipBuilder_itemport_24)

    shipBuilder_itemport_24.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_25 = ItemPort()
    shipBuilder_itemport_25.displayName = None
    shipBuilder_itemport_25.name = u'Port_Thruster_Bottom_Left_Back'
    shipBuilder_itemport_25.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_25.maxSize = 2L
    shipBuilder_itemport_25.minSize = 1L
    shipBuilder_itemport_25.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_25.portClass = 0L
    shipBuilder_itemport_25.image = None
    shipBuilder_itemport_25.tagLocationX = 0L
    shipBuilder_itemport_25.tagLocationY = 0L
    shipBuilder_itemport_25 = importer.save_or_locate(shipBuilder_itemport_25)

    shipBuilder_itemport_25.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_26 = ItemPort()
    shipBuilder_itemport_26.displayName = None
    shipBuilder_itemport_26.name = u'Port_Thruster_Bottom_Right_Back'
    shipBuilder_itemport_26.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_26.maxSize = 2L
    shipBuilder_itemport_26.minSize = 1L
    shipBuilder_itemport_26.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_26.portClass = 0L
    shipBuilder_itemport_26.image = None
    shipBuilder_itemport_26.tagLocationX = 0L
    shipBuilder_itemport_26.tagLocationY = 0L
    shipBuilder_itemport_26 = importer.save_or_locate(shipBuilder_itemport_26)

    shipBuilder_itemport_26.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_27 = ItemPort()
    shipBuilder_itemport_27.displayName = None
    shipBuilder_itemport_27.name = u'Port_Thruster_Bottom_Left_Front'
    shipBuilder_itemport_27.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_27.maxSize = 2L
    shipBuilder_itemport_27.minSize = 1L
    shipBuilder_itemport_27.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_27.portClass = 0L
    shipBuilder_itemport_27.image = None
    shipBuilder_itemport_27.tagLocationX = 0L
    shipBuilder_itemport_27.tagLocationY = 0L
    shipBuilder_itemport_27 = importer.save_or_locate(shipBuilder_itemport_27)

    shipBuilder_itemport_27.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_28 = ItemPort()
    shipBuilder_itemport_28.displayName = None
    shipBuilder_itemport_28.name = u'Port_Thruster_Bottom_Right_Front'
    shipBuilder_itemport_28.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_28.maxSize = 2L
    shipBuilder_itemport_28.minSize = 1L
    shipBuilder_itemport_28.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_28.portClass = 0L
    shipBuilder_itemport_28.image = None
    shipBuilder_itemport_28.tagLocationX = 0L
    shipBuilder_itemport_28.tagLocationY = 0L
    shipBuilder_itemport_28 = importer.save_or_locate(shipBuilder_itemport_28)

    shipBuilder_itemport_28.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_29 = ItemPort()
    shipBuilder_itemport_29.displayName = None
    shipBuilder_itemport_29.name = u'Port_Thruster_Upper_Right_Front'
    shipBuilder_itemport_29.flags = u'maneuver orientation retro -X -Z upper front right'
    shipBuilder_itemport_29.maxSize = 2L
    shipBuilder_itemport_29.minSize = 1L
    shipBuilder_itemport_29.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_29.portClass = 0L
    shipBuilder_itemport_29.image = None
    shipBuilder_itemport_29.tagLocationX = 0L
    shipBuilder_itemport_29.tagLocationY = 0L
    shipBuilder_itemport_29 = importer.save_or_locate(shipBuilder_itemport_29)

    shipBuilder_itemport_29.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_30 = ItemPort()
    shipBuilder_itemport_30.displayName = None
    shipBuilder_itemport_30.name = u'Port_Thruster_Upper_Left_Front'
    shipBuilder_itemport_30.flags = u'maneuver orientation retro +X -Z upper front left'
    shipBuilder_itemport_30.maxSize = 2L
    shipBuilder_itemport_30.minSize = 1L
    shipBuilder_itemport_30.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_30.portClass = 0L
    shipBuilder_itemport_30.image = None
    shipBuilder_itemport_30.tagLocationX = 0L
    shipBuilder_itemport_30.tagLocationY = 0L
    shipBuilder_itemport_30 = importer.save_or_locate(shipBuilder_itemport_30)

    shipBuilder_itemport_30.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_31 = ItemPort()
    shipBuilder_itemport_31.displayName = None
    shipBuilder_itemport_31.name = u'Port_Thruster_Upper_Right_Back'
    shipBuilder_itemport_31.flags = u'maneuver orientation -X -Z upper rear right'
    shipBuilder_itemport_31.maxSize = 2L
    shipBuilder_itemport_31.minSize = 1L
    shipBuilder_itemport_31.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_31.portClass = 0L
    shipBuilder_itemport_31.image = None
    shipBuilder_itemport_31.tagLocationX = 0L
    shipBuilder_itemport_31.tagLocationY = 0L
    shipBuilder_itemport_31 = importer.save_or_locate(shipBuilder_itemport_31)

    shipBuilder_itemport_31.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_32 = ItemPort()
    shipBuilder_itemport_32.displayName = None
    shipBuilder_itemport_32.name = u'Port_Thruster_Upper_Left_Back'
    shipBuilder_itemport_32.flags = u'maneuver orientation +X -Z upper rear left'
    shipBuilder_itemport_32.maxSize = 2L
    shipBuilder_itemport_32.minSize = 1L
    shipBuilder_itemport_32.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_32.portClass = 0L
    shipBuilder_itemport_32.image = None
    shipBuilder_itemport_32.tagLocationX = 0L
    shipBuilder_itemport_32.tagLocationY = 0L
    shipBuilder_itemport_32 = importer.save_or_locate(shipBuilder_itemport_32)

    shipBuilder_itemport_32.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_33 = ItemPort()
    shipBuilder_itemport_33.displayName = u'Class 2 Lower Left Nacelle'
    shipBuilder_itemport_33.name = u'Hardpoint_Class_2_Laser_bottom_left'
    shipBuilder_itemport_33.flags = u'Lower Left'
    shipBuilder_itemport_33.maxSize = 2L
    shipBuilder_itemport_33.minSize = 1L
    shipBuilder_itemport_33.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_33.portClass = 0L
    shipBuilder_itemport_33.image = None
    shipBuilder_itemport_33.tagLocationX = 0L
    shipBuilder_itemport_33.tagLocationY = 0L
    shipBuilder_itemport_33 = importer.save_or_locate(shipBuilder_itemport_33)

    shipBuilder_itemport_33.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_33.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_34 = ItemPort()
    shipBuilder_itemport_34.displayName = u'Class 2 Upper Left Nacelle'
    shipBuilder_itemport_34.name = u'Hardpoint_Class_2_Laser_top_left'
    shipBuilder_itemport_34.flags = u'Upper Left'
    shipBuilder_itemport_34.maxSize = 2L
    shipBuilder_itemport_34.minSize = 1L
    shipBuilder_itemport_34.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_34.portClass = 0L
    shipBuilder_itemport_34.image = None
    shipBuilder_itemport_34.tagLocationX = 0L
    shipBuilder_itemport_34.tagLocationY = 0L
    shipBuilder_itemport_34 = importer.save_or_locate(shipBuilder_itemport_34)

    shipBuilder_itemport_34.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_34.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_35 = ItemPort()
    shipBuilder_itemport_35.displayName = u'Class 2 Lower Right Nacelle'
    shipBuilder_itemport_35.name = u'Hardpoint_Class_2_Laser_bottom_right'
    shipBuilder_itemport_35.flags = u'Lower Right'
    shipBuilder_itemport_35.maxSize = 2L
    shipBuilder_itemport_35.minSize = 1L
    shipBuilder_itemport_35.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_35.portClass = 0L
    shipBuilder_itemport_35.image = None
    shipBuilder_itemport_35.tagLocationX = 0L
    shipBuilder_itemport_35.tagLocationY = 0L
    shipBuilder_itemport_35 = importer.save_or_locate(shipBuilder_itemport_35)

    shipBuilder_itemport_35.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_35.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_36 = ItemPort()
    shipBuilder_itemport_36.displayName = u'Class 2 Upper Right Nacelle'
    shipBuilder_itemport_36.name = u'Hardpoint_Class_2_Laser_top_right'
    shipBuilder_itemport_36.flags = u'Upper Right'
    shipBuilder_itemport_36.maxSize = 2L
    shipBuilder_itemport_36.minSize = 1L
    shipBuilder_itemport_36.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_36.portClass = 0L
    shipBuilder_itemport_36.image = None
    shipBuilder_itemport_36.tagLocationX = 0L
    shipBuilder_itemport_36.tagLocationY = 0L
    shipBuilder_itemport_36 = importer.save_or_locate(shipBuilder_itemport_36)

    shipBuilder_itemport_36.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_36.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_37 = ItemPort()
    shipBuilder_itemport_37.displayName = None
    shipBuilder_itemport_37.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_37.flags = u'main rear'
    shipBuilder_itemport_37.maxSize = 3L
    shipBuilder_itemport_37.minSize = 2L
    shipBuilder_itemport_37.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_37.portClass = 0L
    shipBuilder_itemport_37.image = None
    shipBuilder_itemport_37.tagLocationX = 0L
    shipBuilder_itemport_37.tagLocationY = 0L
    shipBuilder_itemport_37 = importer.save_or_locate(shipBuilder_itemport_37)

    shipBuilder_itemport_37.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_38 = ItemPort()
    shipBuilder_itemport_38.displayName = None
    shipBuilder_itemport_38.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_38.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_38.maxSize = 1L
    shipBuilder_itemport_38.minSize = 1L
    shipBuilder_itemport_38.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_38.portClass = 0L
    shipBuilder_itemport_38.image = None
    shipBuilder_itemport_38.tagLocationX = 0L
    shipBuilder_itemport_38.tagLocationY = 0L
    shipBuilder_itemport_38 = importer.save_or_locate(shipBuilder_itemport_38)

    shipBuilder_itemport_38.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_39 = ItemPort()
    shipBuilder_itemport_39.displayName = None
    shipBuilder_itemport_39.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_39.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_39.maxSize = 1L
    shipBuilder_itemport_39.minSize = 1L
    shipBuilder_itemport_39.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_39.portClass = 0L
    shipBuilder_itemport_39.image = None
    shipBuilder_itemport_39.tagLocationX = 0L
    shipBuilder_itemport_39.tagLocationY = 0L
    shipBuilder_itemport_39 = importer.save_or_locate(shipBuilder_itemport_39)

    shipBuilder_itemport_39.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_40 = ItemPort()
    shipBuilder_itemport_40.displayName = None
    shipBuilder_itemport_40.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_40.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_40.maxSize = 1L
    shipBuilder_itemport_40.minSize = 1L
    shipBuilder_itemport_40.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_40.portClass = 0L
    shipBuilder_itemport_40.image = None
    shipBuilder_itemport_40.tagLocationX = 0L
    shipBuilder_itemport_40.tagLocationY = 0L
    shipBuilder_itemport_40 = importer.save_or_locate(shipBuilder_itemport_40)

    shipBuilder_itemport_40.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_41 = ItemPort()
    shipBuilder_itemport_41.displayName = None
    shipBuilder_itemport_41.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_41.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_41.maxSize = 1L
    shipBuilder_itemport_41.minSize = 1L
    shipBuilder_itemport_41.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_41.portClass = 0L
    shipBuilder_itemport_41.image = None
    shipBuilder_itemport_41.tagLocationX = 0L
    shipBuilder_itemport_41.tagLocationY = 0L
    shipBuilder_itemport_41 = importer.save_or_locate(shipBuilder_itemport_41)

    shipBuilder_itemport_41.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_42 = ItemPort()
    shipBuilder_itemport_42.displayName = None
    shipBuilder_itemport_42.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_42.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_42.maxSize = 1L
    shipBuilder_itemport_42.minSize = 1L
    shipBuilder_itemport_42.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_42.portClass = 0L
    shipBuilder_itemport_42.image = None
    shipBuilder_itemport_42.tagLocationX = 0L
    shipBuilder_itemport_42.tagLocationY = 0L
    shipBuilder_itemport_42 = importer.save_or_locate(shipBuilder_itemport_42)

    shipBuilder_itemport_42.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_43 = ItemPort()
    shipBuilder_itemport_43.displayName = None
    shipBuilder_itemport_43.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_43.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_43.maxSize = 1L
    shipBuilder_itemport_43.minSize = 1L
    shipBuilder_itemport_43.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_43.portClass = 0L
    shipBuilder_itemport_43.image = None
    shipBuilder_itemport_43.tagLocationX = 0L
    shipBuilder_itemport_43.tagLocationY = 0L
    shipBuilder_itemport_43 = importer.save_or_locate(shipBuilder_itemport_43)

    shipBuilder_itemport_43.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_44 = ItemPort()
    shipBuilder_itemport_44.displayName = u'Class 3 Slot'
    shipBuilder_itemport_44.name = u'hardpoint_class_3'
    shipBuilder_itemport_44.flags = u'top mid'
    shipBuilder_itemport_44.maxSize = 3L
    shipBuilder_itemport_44.minSize = 2L
    shipBuilder_itemport_44.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_44.portClass = 0L
    shipBuilder_itemport_44.image = None
    shipBuilder_itemport_44.tagLocationX = 0L
    shipBuilder_itemport_44.tagLocationY = 0L
    shipBuilder_itemport_44 = importer.save_or_locate(shipBuilder_itemport_44)

    shipBuilder_itemport_44.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_44.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_45 = ItemPort()
    shipBuilder_itemport_45.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_45.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_45.flags = u'left'
    shipBuilder_itemport_45.maxSize = 2L
    shipBuilder_itemport_45.minSize = 1L
    shipBuilder_itemport_45.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_45.portClass = 0L
    shipBuilder_itemport_45.image = None
    shipBuilder_itemport_45.tagLocationX = 0L
    shipBuilder_itemport_45.tagLocationY = 0L
    shipBuilder_itemport_45 = importer.save_or_locate(shipBuilder_itemport_45)

    shipBuilder_itemport_45.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_46 = ItemPort()
    shipBuilder_itemport_46.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_46.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_46.flags = u'right'
    shipBuilder_itemport_46.maxSize = 2L
    shipBuilder_itemport_46.minSize = 1L
    shipBuilder_itemport_46.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_46.portClass = 0L
    shipBuilder_itemport_46.image = None
    shipBuilder_itemport_46.tagLocationX = 0L
    shipBuilder_itemport_46.tagLocationY = 0L
    shipBuilder_itemport_46 = importer.save_or_locate(shipBuilder_itemport_46)

    shipBuilder_itemport_46.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_47 = ItemPort()
    shipBuilder_itemport_47.displayName = None
    shipBuilder_itemport_47.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_47.flags = u'main rear'
    shipBuilder_itemport_47.maxSize = 3L
    shipBuilder_itemport_47.minSize = 2L
    shipBuilder_itemport_47.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_47.portClass = 0L
    shipBuilder_itemport_47.image = None
    shipBuilder_itemport_47.tagLocationX = 0L
    shipBuilder_itemport_47.tagLocationY = 0L
    shipBuilder_itemport_47 = importer.save_or_locate(shipBuilder_itemport_47)

    shipBuilder_itemport_47.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_48 = ItemPort()
    shipBuilder_itemport_48.displayName = None
    shipBuilder_itemport_48.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_48.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_48.maxSize = 1L
    shipBuilder_itemport_48.minSize = 1L
    shipBuilder_itemport_48.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_48.portClass = 0L
    shipBuilder_itemport_48.image = None
    shipBuilder_itemport_48.tagLocationX = 0L
    shipBuilder_itemport_48.tagLocationY = 0L
    shipBuilder_itemport_48 = importer.save_or_locate(shipBuilder_itemport_48)

    shipBuilder_itemport_48.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_49 = ItemPort()
    shipBuilder_itemport_49.displayName = None
    shipBuilder_itemport_49.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_49.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_49.maxSize = 1L
    shipBuilder_itemport_49.minSize = 1L
    shipBuilder_itemport_49.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_49.portClass = 0L
    shipBuilder_itemport_49.image = None
    shipBuilder_itemport_49.tagLocationX = 0L
    shipBuilder_itemport_49.tagLocationY = 0L
    shipBuilder_itemport_49 = importer.save_or_locate(shipBuilder_itemport_49)

    shipBuilder_itemport_49.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_50 = ItemPort()
    shipBuilder_itemport_50.displayName = None
    shipBuilder_itemport_50.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_50.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_50.maxSize = 1L
    shipBuilder_itemport_50.minSize = 1L
    shipBuilder_itemport_50.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_50.portClass = 0L
    shipBuilder_itemport_50.image = None
    shipBuilder_itemport_50.tagLocationX = 0L
    shipBuilder_itemport_50.tagLocationY = 0L
    shipBuilder_itemport_50 = importer.save_or_locate(shipBuilder_itemport_50)

    shipBuilder_itemport_50.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_51 = ItemPort()
    shipBuilder_itemport_51.displayName = None
    shipBuilder_itemport_51.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_51.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_51.maxSize = 1L
    shipBuilder_itemport_51.minSize = 1L
    shipBuilder_itemport_51.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_51.portClass = 0L
    shipBuilder_itemport_51.image = None
    shipBuilder_itemport_51.tagLocationX = 0L
    shipBuilder_itemport_51.tagLocationY = 0L
    shipBuilder_itemport_51 = importer.save_or_locate(shipBuilder_itemport_51)

    shipBuilder_itemport_51.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_52 = ItemPort()
    shipBuilder_itemport_52.displayName = None
    shipBuilder_itemport_52.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_52.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_52.maxSize = 1L
    shipBuilder_itemport_52.minSize = 1L
    shipBuilder_itemport_52.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_52.portClass = 0L
    shipBuilder_itemport_52.image = None
    shipBuilder_itemport_52.tagLocationX = 0L
    shipBuilder_itemport_52.tagLocationY = 0L
    shipBuilder_itemport_52 = importer.save_or_locate(shipBuilder_itemport_52)

    shipBuilder_itemport_52.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_53 = ItemPort()
    shipBuilder_itemport_53.displayName = None
    shipBuilder_itemport_53.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_53.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_53.maxSize = 1L
    shipBuilder_itemport_53.minSize = 1L
    shipBuilder_itemport_53.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_53.portClass = 0L
    shipBuilder_itemport_53.image = None
    shipBuilder_itemport_53.tagLocationX = 0L
    shipBuilder_itemport_53.tagLocationY = 0L
    shipBuilder_itemport_53 = importer.save_or_locate(shipBuilder_itemport_53)

    shipBuilder_itemport_53.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_54 = ItemPort()
    shipBuilder_itemport_54.displayName = u'Class 3 Slot'
    shipBuilder_itemport_54.name = u'hardpoint_class_3'
    shipBuilder_itemport_54.flags = u'top mid'
    shipBuilder_itemport_54.maxSize = 3L
    shipBuilder_itemport_54.minSize = 1L
    shipBuilder_itemport_54.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_54.portClass = 0L
    shipBuilder_itemport_54.image = None
    shipBuilder_itemport_54.tagLocationX = 0L
    shipBuilder_itemport_54.tagLocationY = 0L
    shipBuilder_itemport_54 = importer.save_or_locate(shipBuilder_itemport_54)

    shipBuilder_itemport_54.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_54.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_55 = ItemPort()
    shipBuilder_itemport_55.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_55.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_55.flags = u'left'
    shipBuilder_itemport_55.maxSize = 2L
    shipBuilder_itemport_55.minSize = 1L
    shipBuilder_itemport_55.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_55.portClass = 0L
    shipBuilder_itemport_55.image = None
    shipBuilder_itemport_55.tagLocationX = 0L
    shipBuilder_itemport_55.tagLocationY = 0L
    shipBuilder_itemport_55 = importer.save_or_locate(shipBuilder_itemport_55)

    shipBuilder_itemport_55.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_56 = ItemPort()
    shipBuilder_itemport_56.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_56.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_56.flags = u'right'
    shipBuilder_itemport_56.maxSize = 2L
    shipBuilder_itemport_56.minSize = 1L
    shipBuilder_itemport_56.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_56.portClass = 0L
    shipBuilder_itemport_56.image = None
    shipBuilder_itemport_56.tagLocationX = 0L
    shipBuilder_itemport_56.tagLocationY = 0L
    shipBuilder_itemport_56 = importer.save_or_locate(shipBuilder_itemport_56)

    shipBuilder_itemport_56.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_57 = ItemPort()
    shipBuilder_itemport_57.displayName = u'Right Nose Slot'
    shipBuilder_itemport_57.name = u'hardpoint_class_1_nose_right'
    shipBuilder_itemport_57.flags = u'nose right'
    shipBuilder_itemport_57.maxSize = 2L
    shipBuilder_itemport_57.minSize = 1L
    shipBuilder_itemport_57.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_57.portClass = 0L
    shipBuilder_itemport_57.image = None
    shipBuilder_itemport_57.tagLocationX = 0L
    shipBuilder_itemport_57.tagLocationY = 0L
    shipBuilder_itemport_57 = importer.save_or_locate(shipBuilder_itemport_57)

    shipBuilder_itemport_57.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_57.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_58 = ItemPort()
    shipBuilder_itemport_58.displayName = u'Left Nose Slot'
    shipBuilder_itemport_58.name = u'hardpoint_class_1_nose_left'
    shipBuilder_itemport_58.flags = u'nose left'
    shipBuilder_itemport_58.maxSize = 2L
    shipBuilder_itemport_58.minSize = 1L
    shipBuilder_itemport_58.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_58.portClass = 0L
    shipBuilder_itemport_58.image = None
    shipBuilder_itemport_58.tagLocationX = 0L
    shipBuilder_itemport_58.tagLocationY = 0L
    shipBuilder_itemport_58 = importer.save_or_locate(shipBuilder_itemport_58)

    shipBuilder_itemport_58.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_58.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_59 = ItemPort()
    shipBuilder_itemport_59.displayName = u'Power Plant'
    shipBuilder_itemport_59.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_59.flags = u''
    shipBuilder_itemport_59.maxSize = 3L
    shipBuilder_itemport_59.minSize = 2L
    shipBuilder_itemport_59.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_59.portClass = 0L
    shipBuilder_itemport_59.image = None
    shipBuilder_itemport_59.tagLocationX = 0L
    shipBuilder_itemport_59.tagLocationY = 0L
    shipBuilder_itemport_59 = importer.save_or_locate(shipBuilder_itemport_59)

    shipBuilder_itemport_59.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_60 = ItemPort()
    shipBuilder_itemport_60.displayName = None
    shipBuilder_itemport_60.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_60.flags = u'main rear'
    shipBuilder_itemport_60.maxSize = 4L
    shipBuilder_itemport_60.minSize = 3L
    shipBuilder_itemport_60.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_60.portClass = 0L
    shipBuilder_itemport_60.image = None
    shipBuilder_itemport_60.tagLocationX = 0L
    shipBuilder_itemport_60.tagLocationY = 0L
    shipBuilder_itemport_60 = importer.save_or_locate(shipBuilder_itemport_60)

    shipBuilder_itemport_60.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_61 = ItemPort()
    shipBuilder_itemport_61.displayName = None
    shipBuilder_itemport_61.name = u'hardpoint_thruster_bottom_back_left'
    shipBuilder_itemport_61.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_61.maxSize = 2L
    shipBuilder_itemport_61.minSize = 1L
    shipBuilder_itemport_61.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_61.portClass = 0L
    shipBuilder_itemport_61.image = None
    shipBuilder_itemport_61.tagLocationX = 0L
    shipBuilder_itemport_61.tagLocationY = 0L
    shipBuilder_itemport_61 = importer.save_or_locate(shipBuilder_itemport_61)

    shipBuilder_itemport_61.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_62 = ItemPort()
    shipBuilder_itemport_62.displayName = None
    shipBuilder_itemport_62.name = u'hardpoint_thruster_bottom_back_right'
    shipBuilder_itemport_62.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_62.maxSize = 2L
    shipBuilder_itemport_62.minSize = 1L
    shipBuilder_itemport_62.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_62.portClass = 0L
    shipBuilder_itemport_62.image = None
    shipBuilder_itemport_62.tagLocationX = 0L
    shipBuilder_itemport_62.tagLocationY = 0L
    shipBuilder_itemport_62 = importer.save_or_locate(shipBuilder_itemport_62)

    shipBuilder_itemport_62.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_63 = ItemPort()
    shipBuilder_itemport_63.displayName = None
    shipBuilder_itemport_63.name = u'hardpoint_thruster_bottom_front_left'
    shipBuilder_itemport_63.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_63.maxSize = 2L
    shipBuilder_itemport_63.minSize = 1L
    shipBuilder_itemport_63.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_63.portClass = 0L
    shipBuilder_itemport_63.image = None
    shipBuilder_itemport_63.tagLocationX = 0L
    shipBuilder_itemport_63.tagLocationY = 0L
    shipBuilder_itemport_63 = importer.save_or_locate(shipBuilder_itemport_63)

    shipBuilder_itemport_63.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_64 = ItemPort()
    shipBuilder_itemport_64.displayName = None
    shipBuilder_itemport_64.name = u'hardpoint_thruster_bottom_front_right'
    shipBuilder_itemport_64.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_64.maxSize = 2L
    shipBuilder_itemport_64.minSize = 1L
    shipBuilder_itemport_64.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_64.portClass = 0L
    shipBuilder_itemport_64.image = None
    shipBuilder_itemport_64.tagLocationX = 0L
    shipBuilder_itemport_64.tagLocationY = 0L
    shipBuilder_itemport_64 = importer.save_or_locate(shipBuilder_itemport_64)

    shipBuilder_itemport_64.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_65 = ItemPort()
    shipBuilder_itemport_65.displayName = None
    shipBuilder_itemport_65.name = u'hardpoint_thruster_top_front_right'
    shipBuilder_itemport_65.flags = u'maneuver orientation retro -X -Z top front right'
    shipBuilder_itemport_65.maxSize = 2L
    shipBuilder_itemport_65.minSize = 1L
    shipBuilder_itemport_65.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_65.portClass = 0L
    shipBuilder_itemport_65.image = None
    shipBuilder_itemport_65.tagLocationX = 0L
    shipBuilder_itemport_65.tagLocationY = 0L
    shipBuilder_itemport_65 = importer.save_or_locate(shipBuilder_itemport_65)

    shipBuilder_itemport_65.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_66 = ItemPort()
    shipBuilder_itemport_66.displayName = None
    shipBuilder_itemport_66.name = u'hardpoint_thruster_top_front_left'
    shipBuilder_itemport_66.flags = u'maneuver orientation retro +X -Z top front left'
    shipBuilder_itemport_66.maxSize = 2L
    shipBuilder_itemport_66.minSize = 1L
    shipBuilder_itemport_66.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_66.portClass = 0L
    shipBuilder_itemport_66.image = None
    shipBuilder_itemport_66.tagLocationX = 0L
    shipBuilder_itemport_66.tagLocationY = 0L
    shipBuilder_itemport_66 = importer.save_or_locate(shipBuilder_itemport_66)

    shipBuilder_itemport_66.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_67 = ItemPort()
    shipBuilder_itemport_67.displayName = None
    shipBuilder_itemport_67.name = u'hardpoint_thruster_top_back_right'
    shipBuilder_itemport_67.flags = u'maneuver orientation -X -Z top rear right'
    shipBuilder_itemport_67.maxSize = 2L
    shipBuilder_itemport_67.minSize = 1L
    shipBuilder_itemport_67.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_67.portClass = 0L
    shipBuilder_itemport_67.image = None
    shipBuilder_itemport_67.tagLocationX = 0L
    shipBuilder_itemport_67.tagLocationY = 0L
    shipBuilder_itemport_67 = importer.save_or_locate(shipBuilder_itemport_67)

    shipBuilder_itemport_67.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_68 = ItemPort()
    shipBuilder_itemport_68.displayName = None
    shipBuilder_itemport_68.name = u'hardpoint_thruster_top_back_left'
    shipBuilder_itemport_68.flags = u'maneuver orientation +X -Z top rear left'
    shipBuilder_itemport_68.maxSize = 2L
    shipBuilder_itemport_68.minSize = 1L
    shipBuilder_itemport_68.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_68.portClass = 0L
    shipBuilder_itemport_68.image = None
    shipBuilder_itemport_68.tagLocationX = 0L
    shipBuilder_itemport_68.tagLocationY = 0L
    shipBuilder_itemport_68 = importer.save_or_locate(shipBuilder_itemport_68)

    shipBuilder_itemport_68.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_69 = ItemPort()
    shipBuilder_itemport_69.displayName = u'Power Plant'
    shipBuilder_itemport_69.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_69.flags = u'main rear'
    shipBuilder_itemport_69.maxSize = 4L
    shipBuilder_itemport_69.minSize = 2L
    shipBuilder_itemport_69.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_69.portClass = 0L
    shipBuilder_itemport_69.image = None
    shipBuilder_itemport_69.tagLocationX = 0L
    shipBuilder_itemport_69.tagLocationY = 0L
    shipBuilder_itemport_69 = importer.save_or_locate(shipBuilder_itemport_69)

    shipBuilder_itemport_69.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_70 = ItemPort()
    shipBuilder_itemport_70.displayName = None
    shipBuilder_itemport_70.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_70.flags = u'main rear'
    shipBuilder_itemport_70.maxSize = 4L
    shipBuilder_itemport_70.minSize = 3L
    shipBuilder_itemport_70.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_70.portClass = 0L
    shipBuilder_itemport_70.image = None
    shipBuilder_itemport_70.tagLocationX = 0L
    shipBuilder_itemport_70.tagLocationY = 0L
    shipBuilder_itemport_70 = importer.save_or_locate(shipBuilder_itemport_70)

    shipBuilder_itemport_70.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_71 = ItemPort()
    shipBuilder_itemport_71.displayName = None
    shipBuilder_itemport_71.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_71.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_71.maxSize = 1L
    shipBuilder_itemport_71.minSize = 1L
    shipBuilder_itemport_71.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_71.portClass = 0L
    shipBuilder_itemport_71.image = None
    shipBuilder_itemport_71.tagLocationX = 0L
    shipBuilder_itemport_71.tagLocationY = 0L
    shipBuilder_itemport_71 = importer.save_or_locate(shipBuilder_itemport_71)

    shipBuilder_itemport_71.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_72 = ItemPort()
    shipBuilder_itemport_72.displayName = None
    shipBuilder_itemport_72.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_72.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_72.maxSize = 1L
    shipBuilder_itemport_72.minSize = 1L
    shipBuilder_itemport_72.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_72.portClass = 0L
    shipBuilder_itemport_72.image = None
    shipBuilder_itemport_72.tagLocationX = 0L
    shipBuilder_itemport_72.tagLocationY = 0L
    shipBuilder_itemport_72 = importer.save_or_locate(shipBuilder_itemport_72)

    shipBuilder_itemport_72.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_73 = ItemPort()
    shipBuilder_itemport_73.displayName = None
    shipBuilder_itemport_73.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_73.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_73.maxSize = 1L
    shipBuilder_itemport_73.minSize = 1L
    shipBuilder_itemport_73.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_73.portClass = 0L
    shipBuilder_itemport_73.image = None
    shipBuilder_itemport_73.tagLocationX = 0L
    shipBuilder_itemport_73.tagLocationY = 0L
    shipBuilder_itemport_73 = importer.save_or_locate(shipBuilder_itemport_73)

    shipBuilder_itemport_73.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_74 = ItemPort()
    shipBuilder_itemport_74.displayName = None
    shipBuilder_itemport_74.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_74.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_74.maxSize = 1L
    shipBuilder_itemport_74.minSize = 1L
    shipBuilder_itemport_74.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_74.portClass = 0L
    shipBuilder_itemport_74.image = None
    shipBuilder_itemport_74.tagLocationX = 0L
    shipBuilder_itemport_74.tagLocationY = 0L
    shipBuilder_itemport_74 = importer.save_or_locate(shipBuilder_itemport_74)

    shipBuilder_itemport_74.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_75 = ItemPort()
    shipBuilder_itemport_75.displayName = None
    shipBuilder_itemport_75.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_75.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_75.maxSize = 1L
    shipBuilder_itemport_75.minSize = 1L
    shipBuilder_itemport_75.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_75.portClass = 0L
    shipBuilder_itemport_75.image = None
    shipBuilder_itemport_75.tagLocationX = 0L
    shipBuilder_itemport_75.tagLocationY = 0L
    shipBuilder_itemport_75 = importer.save_or_locate(shipBuilder_itemport_75)

    shipBuilder_itemport_75.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_76 = ItemPort()
    shipBuilder_itemport_76.displayName = None
    shipBuilder_itemport_76.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_76.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_76.maxSize = 1L
    shipBuilder_itemport_76.minSize = 1L
    shipBuilder_itemport_76.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_76.portClass = 0L
    shipBuilder_itemport_76.image = None
    shipBuilder_itemport_76.tagLocationX = 0L
    shipBuilder_itemport_76.tagLocationY = 0L
    shipBuilder_itemport_76 = importer.save_or_locate(shipBuilder_itemport_76)

    shipBuilder_itemport_76.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_77 = ItemPort()
    shipBuilder_itemport_77.displayName = None
    shipBuilder_itemport_77.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_77.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_77.maxSize = 1L
    shipBuilder_itemport_77.minSize = 1L
    shipBuilder_itemport_77.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_77.portClass = 0L
    shipBuilder_itemport_77.image = None
    shipBuilder_itemport_77.tagLocationX = 0L
    shipBuilder_itemport_77.tagLocationY = 0L
    shipBuilder_itemport_77 = importer.save_or_locate(shipBuilder_itemport_77)

    shipBuilder_itemport_77.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_78 = ItemPort()
    shipBuilder_itemport_78.displayName = None
    shipBuilder_itemport_78.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_78.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_78.maxSize = 1L
    shipBuilder_itemport_78.minSize = 1L
    shipBuilder_itemport_78.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_78.portClass = 0L
    shipBuilder_itemport_78.image = None
    shipBuilder_itemport_78.tagLocationX = 0L
    shipBuilder_itemport_78.tagLocationY = 0L
    shipBuilder_itemport_78 = importer.save_or_locate(shipBuilder_itemport_78)

    shipBuilder_itemport_78.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_79 = ItemPort()
    shipBuilder_itemport_79.displayName = None
    shipBuilder_itemport_79.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_79.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_79.maxSize = 1L
    shipBuilder_itemport_79.minSize = 1L
    shipBuilder_itemport_79.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_79.portClass = 0L
    shipBuilder_itemport_79.image = None
    shipBuilder_itemport_79.tagLocationX = 0L
    shipBuilder_itemport_79.tagLocationY = 0L
    shipBuilder_itemport_79 = importer.save_or_locate(shipBuilder_itemport_79)

    shipBuilder_itemport_79.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_80 = ItemPort()
    shipBuilder_itemport_80.displayName = None
    shipBuilder_itemport_80.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_80.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_80.maxSize = 1L
    shipBuilder_itemport_80.minSize = 1L
    shipBuilder_itemport_80.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_80.portClass = 0L
    shipBuilder_itemport_80.image = None
    shipBuilder_itemport_80.tagLocationX = 0L
    shipBuilder_itemport_80.tagLocationY = 0L
    shipBuilder_itemport_80 = importer.save_or_locate(shipBuilder_itemport_80)

    shipBuilder_itemport_80.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_81 = ItemPort()
    shipBuilder_itemport_81.displayName = None
    shipBuilder_itemport_81.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_81.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_81.maxSize = 1L
    shipBuilder_itemport_81.minSize = 1L
    shipBuilder_itemport_81.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_81.portClass = 0L
    shipBuilder_itemport_81.image = None
    shipBuilder_itemport_81.tagLocationX = 0L
    shipBuilder_itemport_81.tagLocationY = 0L
    shipBuilder_itemport_81 = importer.save_or_locate(shipBuilder_itemport_81)

    shipBuilder_itemport_81.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_82 = ItemPort()
    shipBuilder_itemport_82.displayName = None
    shipBuilder_itemport_82.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_82.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_82.maxSize = 1L
    shipBuilder_itemport_82.minSize = 1L
    shipBuilder_itemport_82.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_82.portClass = 0L
    shipBuilder_itemport_82.image = None
    shipBuilder_itemport_82.tagLocationX = 0L
    shipBuilder_itemport_82.tagLocationY = 0L
    shipBuilder_itemport_82 = importer.save_or_locate(shipBuilder_itemport_82)

    shipBuilder_itemport_82.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_83 = ItemPort()
    shipBuilder_itemport_83.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_83.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_83.flags = u'nose'
    shipBuilder_itemport_83.maxSize = 2L
    shipBuilder_itemport_83.minSize = 1L
    shipBuilder_itemport_83.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_83.portClass = 0L
    shipBuilder_itemport_83.image = None
    shipBuilder_itemport_83.tagLocationX = 0L
    shipBuilder_itemport_83.tagLocationY = 0L
    shipBuilder_itemport_83 = importer.save_or_locate(shipBuilder_itemport_83)

    shipBuilder_itemport_83.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_84 = ItemPort()
    shipBuilder_itemport_84.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_84.name = u'hardpoint_class3_top_left_wing_350R'
    shipBuilder_itemport_84.flags = u'upper left wing'
    shipBuilder_itemport_84.maxSize = 3L
    shipBuilder_itemport_84.minSize = 1L
    shipBuilder_itemport_84.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_84.portClass = 0L
    shipBuilder_itemport_84.image = None
    shipBuilder_itemport_84.tagLocationX = 0L
    shipBuilder_itemport_84.tagLocationY = 0L
    shipBuilder_itemport_84 = importer.save_or_locate(shipBuilder_itemport_84)

    shipBuilder_itemport_84.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_84.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_85 = ItemPort()
    shipBuilder_itemport_85.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_85.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_85.flags = u'left wing'
    shipBuilder_itemport_85.maxSize = 3L
    shipBuilder_itemport_85.minSize = 1L
    shipBuilder_itemport_85.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_85.portClass = 0L
    shipBuilder_itemport_85.image = None
    shipBuilder_itemport_85.tagLocationX = 0L
    shipBuilder_itemport_85.tagLocationY = 0L
    shipBuilder_itemport_85 = importer.save_or_locate(shipBuilder_itemport_85)

    shipBuilder_itemport_85.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_86 = ItemPort()
    shipBuilder_itemport_86.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_86.name = u'hardpoint_class3_top_right_wing_350R'
    shipBuilder_itemport_86.flags = u'upper right wing'
    shipBuilder_itemport_86.maxSize = 3L
    shipBuilder_itemport_86.minSize = 1L
    shipBuilder_itemport_86.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_86.portClass = 0L
    shipBuilder_itemport_86.image = None
    shipBuilder_itemport_86.tagLocationX = 0L
    shipBuilder_itemport_86.tagLocationY = 0L
    shipBuilder_itemport_86 = importer.save_or_locate(shipBuilder_itemport_86)

    shipBuilder_itemport_86.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_86.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_87 = ItemPort()
    shipBuilder_itemport_87.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_87.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_87.flags = u'right wing'
    shipBuilder_itemport_87.maxSize = 3L
    shipBuilder_itemport_87.minSize = 1L
    shipBuilder_itemport_87.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_87.portClass = 0L
    shipBuilder_itemport_87.image = None
    shipBuilder_itemport_87.tagLocationX = 0L
    shipBuilder_itemport_87.tagLocationY = 0L
    shipBuilder_itemport_87 = importer.save_or_locate(shipBuilder_itemport_87)

    shipBuilder_itemport_87.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_88 = ItemPort()
    shipBuilder_itemport_88.displayName = u'Power Plant'
    shipBuilder_itemport_88.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_88.flags = u'main rear'
    shipBuilder_itemport_88.maxSize = 3L
    shipBuilder_itemport_88.minSize = 2L
    shipBuilder_itemport_88.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_88.portClass = 0L
    shipBuilder_itemport_88.image = None
    shipBuilder_itemport_88.tagLocationX = 0L
    shipBuilder_itemport_88.tagLocationY = 0L
    shipBuilder_itemport_88 = importer.save_or_locate(shipBuilder_itemport_88)

    shipBuilder_itemport_88.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_89 = ItemPort()
    shipBuilder_itemport_89.displayName = None
    shipBuilder_itemport_89.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_89.flags = u'main rear'
    shipBuilder_itemport_89.maxSize = 4L
    shipBuilder_itemport_89.minSize = 3L
    shipBuilder_itemport_89.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_89.portClass = 0L
    shipBuilder_itemport_89.image = None
    shipBuilder_itemport_89.tagLocationX = 0L
    shipBuilder_itemport_89.tagLocationY = 0L
    shipBuilder_itemport_89 = importer.save_or_locate(shipBuilder_itemport_89)

    shipBuilder_itemport_89.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_90 = ItemPort()
    shipBuilder_itemport_90.displayName = None
    shipBuilder_itemport_90.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_90.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_90.maxSize = 1L
    shipBuilder_itemport_90.minSize = 1L
    shipBuilder_itemport_90.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_90.portClass = 0L
    shipBuilder_itemport_90.image = None
    shipBuilder_itemport_90.tagLocationX = 0L
    shipBuilder_itemport_90.tagLocationY = 0L
    shipBuilder_itemport_90 = importer.save_or_locate(shipBuilder_itemport_90)

    shipBuilder_itemport_90.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_91 = ItemPort()
    shipBuilder_itemport_91.displayName = None
    shipBuilder_itemport_91.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_91.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_91.maxSize = 1L
    shipBuilder_itemport_91.minSize = 1L
    shipBuilder_itemport_91.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_91.portClass = 0L
    shipBuilder_itemport_91.image = None
    shipBuilder_itemport_91.tagLocationX = 0L
    shipBuilder_itemport_91.tagLocationY = 0L
    shipBuilder_itemport_91 = importer.save_or_locate(shipBuilder_itemport_91)

    shipBuilder_itemport_91.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_92 = ItemPort()
    shipBuilder_itemport_92.displayName = None
    shipBuilder_itemport_92.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_92.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_92.maxSize = 1L
    shipBuilder_itemport_92.minSize = 1L
    shipBuilder_itemport_92.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_92.portClass = 0L
    shipBuilder_itemport_92.image = None
    shipBuilder_itemport_92.tagLocationX = 0L
    shipBuilder_itemport_92.tagLocationY = 0L
    shipBuilder_itemport_92 = importer.save_or_locate(shipBuilder_itemport_92)

    shipBuilder_itemport_92.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_93 = ItemPort()
    shipBuilder_itemport_93.displayName = None
    shipBuilder_itemport_93.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_93.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_93.maxSize = 1L
    shipBuilder_itemport_93.minSize = 1L
    shipBuilder_itemport_93.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_93.portClass = 0L
    shipBuilder_itemport_93.image = None
    shipBuilder_itemport_93.tagLocationX = 0L
    shipBuilder_itemport_93.tagLocationY = 0L
    shipBuilder_itemport_93 = importer.save_or_locate(shipBuilder_itemport_93)

    shipBuilder_itemport_93.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_94 = ItemPort()
    shipBuilder_itemport_94.displayName = None
    shipBuilder_itemport_94.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_94.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_94.maxSize = 1L
    shipBuilder_itemport_94.minSize = 1L
    shipBuilder_itemport_94.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_94.portClass = 0L
    shipBuilder_itemport_94.image = None
    shipBuilder_itemport_94.tagLocationX = 0L
    shipBuilder_itemport_94.tagLocationY = 0L
    shipBuilder_itemport_94 = importer.save_or_locate(shipBuilder_itemport_94)

    shipBuilder_itemport_94.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_95 = ItemPort()
    shipBuilder_itemport_95.displayName = None
    shipBuilder_itemport_95.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_95.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_95.maxSize = 1L
    shipBuilder_itemport_95.minSize = 1L
    shipBuilder_itemport_95.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_95.portClass = 0L
    shipBuilder_itemport_95.image = None
    shipBuilder_itemport_95.tagLocationX = 0L
    shipBuilder_itemport_95.tagLocationY = 0L
    shipBuilder_itemport_95 = importer.save_or_locate(shipBuilder_itemport_95)

    shipBuilder_itemport_95.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_96 = ItemPort()
    shipBuilder_itemport_96.displayName = None
    shipBuilder_itemport_96.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_96.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_96.maxSize = 1L
    shipBuilder_itemport_96.minSize = 1L
    shipBuilder_itemport_96.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_96.portClass = 0L
    shipBuilder_itemport_96.image = None
    shipBuilder_itemport_96.tagLocationX = 0L
    shipBuilder_itemport_96.tagLocationY = 0L
    shipBuilder_itemport_96 = importer.save_or_locate(shipBuilder_itemport_96)

    shipBuilder_itemport_96.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_97 = ItemPort()
    shipBuilder_itemport_97.displayName = None
    shipBuilder_itemport_97.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_97.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_97.maxSize = 1L
    shipBuilder_itemport_97.minSize = 1L
    shipBuilder_itemport_97.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_97.portClass = 0L
    shipBuilder_itemport_97.image = None
    shipBuilder_itemport_97.tagLocationX = 0L
    shipBuilder_itemport_97.tagLocationY = 0L
    shipBuilder_itemport_97 = importer.save_or_locate(shipBuilder_itemport_97)

    shipBuilder_itemport_97.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_98 = ItemPort()
    shipBuilder_itemport_98.displayName = None
    shipBuilder_itemport_98.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_98.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_98.maxSize = 1L
    shipBuilder_itemport_98.minSize = 1L
    shipBuilder_itemport_98.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_98.portClass = 0L
    shipBuilder_itemport_98.image = None
    shipBuilder_itemport_98.tagLocationX = 0L
    shipBuilder_itemport_98.tagLocationY = 0L
    shipBuilder_itemport_98 = importer.save_or_locate(shipBuilder_itemport_98)

    shipBuilder_itemport_98.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_99 = ItemPort()
    shipBuilder_itemport_99.displayName = None
    shipBuilder_itemport_99.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_99.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_99.maxSize = 1L
    shipBuilder_itemport_99.minSize = 1L
    shipBuilder_itemport_99.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_99.portClass = 0L
    shipBuilder_itemport_99.image = None
    shipBuilder_itemport_99.tagLocationX = 0L
    shipBuilder_itemport_99.tagLocationY = 0L
    shipBuilder_itemport_99 = importer.save_or_locate(shipBuilder_itemport_99)

    shipBuilder_itemport_99.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_100 = ItemPort()
    shipBuilder_itemport_100.displayName = None
    shipBuilder_itemport_100.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_100.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_100.maxSize = 1L
    shipBuilder_itemport_100.minSize = 1L
    shipBuilder_itemport_100.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_100.portClass = 0L
    shipBuilder_itemport_100.image = None
    shipBuilder_itemport_100.tagLocationX = 0L
    shipBuilder_itemport_100.tagLocationY = 0L
    shipBuilder_itemport_100 = importer.save_or_locate(shipBuilder_itemport_100)

    shipBuilder_itemport_100.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_101 = ItemPort()
    shipBuilder_itemport_101.displayName = None
    shipBuilder_itemport_101.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_101.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_101.maxSize = 1L
    shipBuilder_itemport_101.minSize = 1L
    shipBuilder_itemport_101.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_101.portClass = 0L
    shipBuilder_itemport_101.image = None
    shipBuilder_itemport_101.tagLocationX = 0L
    shipBuilder_itemport_101.tagLocationY = 0L
    shipBuilder_itemport_101 = importer.save_or_locate(shipBuilder_itemport_101)

    shipBuilder_itemport_101.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_102 = ItemPort()
    shipBuilder_itemport_102.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_102.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_102.flags = u'nose'
    shipBuilder_itemport_102.maxSize = 2L
    shipBuilder_itemport_102.minSize = 1L
    shipBuilder_itemport_102.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_102.portClass = 0L
    shipBuilder_itemport_102.image = None
    shipBuilder_itemport_102.tagLocationX = 0L
    shipBuilder_itemport_102.tagLocationY = 0L
    shipBuilder_itemport_102 = importer.save_or_locate(shipBuilder_itemport_102)

    shipBuilder_itemport_102.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_103 = ItemPort()
    shipBuilder_itemport_103.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_103.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_103.flags = u'upper left wing'
    shipBuilder_itemport_103.maxSize = 3L
    shipBuilder_itemport_103.minSize = 1L
    shipBuilder_itemport_103.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_103.portClass = 0L
    shipBuilder_itemport_103.image = None
    shipBuilder_itemport_103.tagLocationX = 0L
    shipBuilder_itemport_103.tagLocationY = 0L
    shipBuilder_itemport_103 = importer.save_or_locate(shipBuilder_itemport_103)

    shipBuilder_itemport_103.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_103.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_104 = ItemPort()
    shipBuilder_itemport_104.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_104.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_104.flags = u'left wing'
    shipBuilder_itemport_104.maxSize = 3L
    shipBuilder_itemport_104.minSize = 1L
    shipBuilder_itemport_104.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_104.portClass = 0L
    shipBuilder_itemport_104.image = None
    shipBuilder_itemport_104.tagLocationX = 0L
    shipBuilder_itemport_104.tagLocationY = 0L
    shipBuilder_itemport_104 = importer.save_or_locate(shipBuilder_itemport_104)

    shipBuilder_itemport_104.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_105 = ItemPort()
    shipBuilder_itemport_105.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_105.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_105.flags = u'upper right wing'
    shipBuilder_itemport_105.maxSize = 3L
    shipBuilder_itemport_105.minSize = 1L
    shipBuilder_itemport_105.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_105.portClass = 0L
    shipBuilder_itemport_105.image = None
    shipBuilder_itemport_105.tagLocationX = 0L
    shipBuilder_itemport_105.tagLocationY = 0L
    shipBuilder_itemport_105 = importer.save_or_locate(shipBuilder_itemport_105)

    shipBuilder_itemport_105.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_105.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_106 = ItemPort()
    shipBuilder_itemport_106.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_106.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_106.flags = u'right wing'
    shipBuilder_itemport_106.maxSize = 3L
    shipBuilder_itemport_106.minSize = 1L
    shipBuilder_itemport_106.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_106.portClass = 0L
    shipBuilder_itemport_106.image = None
    shipBuilder_itemport_106.tagLocationX = 0L
    shipBuilder_itemport_106.tagLocationY = 0L
    shipBuilder_itemport_106 = importer.save_or_locate(shipBuilder_itemport_106)

    shipBuilder_itemport_106.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_107 = ItemPort()
    shipBuilder_itemport_107.displayName = None
    shipBuilder_itemport_107.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_107.flags = u'main rear'
    shipBuilder_itemport_107.maxSize = 3L
    shipBuilder_itemport_107.minSize = 2L
    shipBuilder_itemport_107.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_107.portClass = 0L
    shipBuilder_itemport_107.image = None
    shipBuilder_itemport_107.tagLocationX = 0L
    shipBuilder_itemport_107.tagLocationY = 0L
    shipBuilder_itemport_107 = importer.save_or_locate(shipBuilder_itemport_107)

    shipBuilder_itemport_107.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_108 = ItemPort()
    shipBuilder_itemport_108.displayName = None
    shipBuilder_itemport_108.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_108.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_108.maxSize = 1L
    shipBuilder_itemport_108.minSize = 1L
    shipBuilder_itemport_108.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_108.portClass = 0L
    shipBuilder_itemport_108.image = None
    shipBuilder_itemport_108.tagLocationX = 0L
    shipBuilder_itemport_108.tagLocationY = 0L
    shipBuilder_itemport_108 = importer.save_or_locate(shipBuilder_itemport_108)

    shipBuilder_itemport_108.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_109 = ItemPort()
    shipBuilder_itemport_109.displayName = None
    shipBuilder_itemport_109.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_109.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_109.maxSize = 1L
    shipBuilder_itemport_109.minSize = 1L
    shipBuilder_itemport_109.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_109.portClass = 0L
    shipBuilder_itemport_109.image = None
    shipBuilder_itemport_109.tagLocationX = 0L
    shipBuilder_itemport_109.tagLocationY = 0L
    shipBuilder_itemport_109 = importer.save_or_locate(shipBuilder_itemport_109)

    shipBuilder_itemport_109.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_110 = ItemPort()
    shipBuilder_itemport_110.displayName = None
    shipBuilder_itemport_110.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_110.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_110.maxSize = 1L
    shipBuilder_itemport_110.minSize = 1L
    shipBuilder_itemport_110.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_110.portClass = 0L
    shipBuilder_itemport_110.image = None
    shipBuilder_itemport_110.tagLocationX = 0L
    shipBuilder_itemport_110.tagLocationY = 0L
    shipBuilder_itemport_110 = importer.save_or_locate(shipBuilder_itemport_110)

    shipBuilder_itemport_110.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_111 = ItemPort()
    shipBuilder_itemport_111.displayName = None
    shipBuilder_itemport_111.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_111.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_111.maxSize = 1L
    shipBuilder_itemport_111.minSize = 1L
    shipBuilder_itemport_111.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_111.portClass = 0L
    shipBuilder_itemport_111.image = None
    shipBuilder_itemport_111.tagLocationX = 0L
    shipBuilder_itemport_111.tagLocationY = 0L
    shipBuilder_itemport_111 = importer.save_or_locate(shipBuilder_itemport_111)

    shipBuilder_itemport_111.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_112 = ItemPort()
    shipBuilder_itemport_112.displayName = None
    shipBuilder_itemport_112.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_112.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_112.maxSize = 1L
    shipBuilder_itemport_112.minSize = 1L
    shipBuilder_itemport_112.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_112.portClass = 0L
    shipBuilder_itemport_112.image = None
    shipBuilder_itemport_112.tagLocationX = 0L
    shipBuilder_itemport_112.tagLocationY = 0L
    shipBuilder_itemport_112 = importer.save_or_locate(shipBuilder_itemport_112)

    shipBuilder_itemport_112.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_113 = ItemPort()
    shipBuilder_itemport_113.displayName = None
    shipBuilder_itemport_113.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_113.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_113.maxSize = 2L
    shipBuilder_itemport_113.minSize = 1L
    shipBuilder_itemport_113.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_113.portClass = 0L
    shipBuilder_itemport_113.image = None
    shipBuilder_itemport_113.tagLocationX = 0L
    shipBuilder_itemport_113.tagLocationY = 0L
    shipBuilder_itemport_113 = importer.save_or_locate(shipBuilder_itemport_113)

    shipBuilder_itemport_113.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_114 = ItemPort()
    shipBuilder_itemport_114.displayName = u'Class 3 Slot'
    shipBuilder_itemport_114.name = u'hardpoint_class_3'
    shipBuilder_itemport_114.flags = u'top mid'
    shipBuilder_itemport_114.maxSize = 3L
    shipBuilder_itemport_114.minSize = 1L
    shipBuilder_itemport_114.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_114.portClass = 0L
    shipBuilder_itemport_114.image = None
    shipBuilder_itemport_114.tagLocationX = 0L
    shipBuilder_itemport_114.tagLocationY = 0L
    shipBuilder_itemport_114 = importer.save_or_locate(shipBuilder_itemport_114)

    shipBuilder_itemport_114.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_114.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_115 = ItemPort()
    shipBuilder_itemport_115.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_115.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_115.flags = u'left'
    shipBuilder_itemport_115.maxSize = 2L
    shipBuilder_itemport_115.minSize = 1L
    shipBuilder_itemport_115.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_115.portClass = 0L
    shipBuilder_itemport_115.image = None
    shipBuilder_itemport_115.tagLocationX = 0L
    shipBuilder_itemport_115.tagLocationY = 0L
    shipBuilder_itemport_115 = importer.save_or_locate(shipBuilder_itemport_115)

    shipBuilder_itemport_115.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_116 = ItemPort()
    shipBuilder_itemport_116.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_116.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_116.flags = u'right'
    shipBuilder_itemport_116.maxSize = 2L
    shipBuilder_itemport_116.minSize = 1L
    shipBuilder_itemport_116.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_116.portClass = 0L
    shipBuilder_itemport_116.image = None
    shipBuilder_itemport_116.tagLocationX = 0L
    shipBuilder_itemport_116.tagLocationY = 0L
    shipBuilder_itemport_116 = importer.save_or_locate(shipBuilder_itemport_116)

    shipBuilder_itemport_116.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_117 = ItemPort()
    shipBuilder_itemport_117.displayName = u'Power Plant'
    shipBuilder_itemport_117.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_117.flags = u'main rear'
    shipBuilder_itemport_117.maxSize = 3L
    shipBuilder_itemport_117.minSize = 2L
    shipBuilder_itemport_117.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_117.portClass = 0L
    shipBuilder_itemport_117.image = None
    shipBuilder_itemport_117.tagLocationX = 0L
    shipBuilder_itemport_117.tagLocationY = 0L
    shipBuilder_itemport_117 = importer.save_or_locate(shipBuilder_itemport_117)

    shipBuilder_itemport_117.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_118 = ItemPort()
    shipBuilder_itemport_118.displayName = None
    shipBuilder_itemport_118.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_118.flags = u'main rear'
    shipBuilder_itemport_118.maxSize = 4L
    shipBuilder_itemport_118.minSize = 3L
    shipBuilder_itemport_118.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_118.portClass = 0L
    shipBuilder_itemport_118.image = None
    shipBuilder_itemport_118.tagLocationX = 0L
    shipBuilder_itemport_118.tagLocationY = 0L
    shipBuilder_itemport_118 = importer.save_or_locate(shipBuilder_itemport_118)

    shipBuilder_itemport_118.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_119 = ItemPort()
    shipBuilder_itemport_119.displayName = None
    shipBuilder_itemport_119.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_119.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_119.maxSize = 1L
    shipBuilder_itemport_119.minSize = 1L
    shipBuilder_itemport_119.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_119.portClass = 0L
    shipBuilder_itemport_119.image = None
    shipBuilder_itemport_119.tagLocationX = 0L
    shipBuilder_itemport_119.tagLocationY = 0L
    shipBuilder_itemport_119 = importer.save_or_locate(shipBuilder_itemport_119)

    shipBuilder_itemport_119.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_120 = ItemPort()
    shipBuilder_itemport_120.displayName = None
    shipBuilder_itemport_120.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_120.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_120.maxSize = 1L
    shipBuilder_itemport_120.minSize = 1L
    shipBuilder_itemport_120.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_120.portClass = 0L
    shipBuilder_itemport_120.image = None
    shipBuilder_itemport_120.tagLocationX = 0L
    shipBuilder_itemport_120.tagLocationY = 0L
    shipBuilder_itemport_120 = importer.save_or_locate(shipBuilder_itemport_120)

    shipBuilder_itemport_120.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_121 = ItemPort()
    shipBuilder_itemport_121.displayName = None
    shipBuilder_itemport_121.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_121.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_121.maxSize = 1L
    shipBuilder_itemport_121.minSize = 1L
    shipBuilder_itemport_121.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_121.portClass = 0L
    shipBuilder_itemport_121.image = None
    shipBuilder_itemport_121.tagLocationX = 0L
    shipBuilder_itemport_121.tagLocationY = 0L
    shipBuilder_itemport_121 = importer.save_or_locate(shipBuilder_itemport_121)

    shipBuilder_itemport_121.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_122 = ItemPort()
    shipBuilder_itemport_122.displayName = None
    shipBuilder_itemport_122.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_122.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_122.maxSize = 1L
    shipBuilder_itemport_122.minSize = 1L
    shipBuilder_itemport_122.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_122.portClass = 0L
    shipBuilder_itemport_122.image = None
    shipBuilder_itemport_122.tagLocationX = 0L
    shipBuilder_itemport_122.tagLocationY = 0L
    shipBuilder_itemport_122 = importer.save_or_locate(shipBuilder_itemport_122)

    shipBuilder_itemport_122.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_123 = ItemPort()
    shipBuilder_itemport_123.displayName = None
    shipBuilder_itemport_123.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_123.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_123.maxSize = 1L
    shipBuilder_itemport_123.minSize = 1L
    shipBuilder_itemport_123.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_123.portClass = 0L
    shipBuilder_itemport_123.image = None
    shipBuilder_itemport_123.tagLocationX = 0L
    shipBuilder_itemport_123.tagLocationY = 0L
    shipBuilder_itemport_123 = importer.save_or_locate(shipBuilder_itemport_123)

    shipBuilder_itemport_123.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_124 = ItemPort()
    shipBuilder_itemport_124.displayName = None
    shipBuilder_itemport_124.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_124.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_124.maxSize = 1L
    shipBuilder_itemport_124.minSize = 1L
    shipBuilder_itemport_124.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_124.portClass = 0L
    shipBuilder_itemport_124.image = None
    shipBuilder_itemport_124.tagLocationX = 0L
    shipBuilder_itemport_124.tagLocationY = 0L
    shipBuilder_itemport_124 = importer.save_or_locate(shipBuilder_itemport_124)

    shipBuilder_itemport_124.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_125 = ItemPort()
    shipBuilder_itemport_125.displayName = None
    shipBuilder_itemport_125.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_125.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_125.maxSize = 1L
    shipBuilder_itemport_125.minSize = 1L
    shipBuilder_itemport_125.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_125.portClass = 0L
    shipBuilder_itemport_125.image = None
    shipBuilder_itemport_125.tagLocationX = 0L
    shipBuilder_itemport_125.tagLocationY = 0L
    shipBuilder_itemport_125 = importer.save_or_locate(shipBuilder_itemport_125)

    shipBuilder_itemport_125.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_126 = ItemPort()
    shipBuilder_itemport_126.displayName = None
    shipBuilder_itemport_126.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_126.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_126.maxSize = 1L
    shipBuilder_itemport_126.minSize = 1L
    shipBuilder_itemport_126.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_126.portClass = 0L
    shipBuilder_itemport_126.image = None
    shipBuilder_itemport_126.tagLocationX = 0L
    shipBuilder_itemport_126.tagLocationY = 0L
    shipBuilder_itemport_126 = importer.save_or_locate(shipBuilder_itemport_126)

    shipBuilder_itemport_126.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_127 = ItemPort()
    shipBuilder_itemport_127.displayName = None
    shipBuilder_itemport_127.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_127.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_127.maxSize = 1L
    shipBuilder_itemport_127.minSize = 1L
    shipBuilder_itemport_127.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_127.portClass = 0L
    shipBuilder_itemport_127.image = None
    shipBuilder_itemport_127.tagLocationX = 0L
    shipBuilder_itemport_127.tagLocationY = 0L
    shipBuilder_itemport_127 = importer.save_or_locate(shipBuilder_itemport_127)

    shipBuilder_itemport_127.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_128 = ItemPort()
    shipBuilder_itemport_128.displayName = None
    shipBuilder_itemport_128.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_128.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_128.maxSize = 1L
    shipBuilder_itemport_128.minSize = 1L
    shipBuilder_itemport_128.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_128.portClass = 0L
    shipBuilder_itemport_128.image = None
    shipBuilder_itemport_128.tagLocationX = 0L
    shipBuilder_itemport_128.tagLocationY = 0L
    shipBuilder_itemport_128 = importer.save_or_locate(shipBuilder_itemport_128)

    shipBuilder_itemport_128.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_129 = ItemPort()
    shipBuilder_itemport_129.displayName = None
    shipBuilder_itemport_129.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_129.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_129.maxSize = 1L
    shipBuilder_itemport_129.minSize = 1L
    shipBuilder_itemport_129.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_129.portClass = 0L
    shipBuilder_itemport_129.image = None
    shipBuilder_itemport_129.tagLocationX = 0L
    shipBuilder_itemport_129.tagLocationY = 0L
    shipBuilder_itemport_129 = importer.save_or_locate(shipBuilder_itemport_129)

    shipBuilder_itemport_129.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_130 = ItemPort()
    shipBuilder_itemport_130.displayName = None
    shipBuilder_itemport_130.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_130.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_130.maxSize = 1L
    shipBuilder_itemport_130.minSize = 1L
    shipBuilder_itemport_130.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_130.portClass = 0L
    shipBuilder_itemport_130.image = None
    shipBuilder_itemport_130.tagLocationX = 0L
    shipBuilder_itemport_130.tagLocationY = 0L
    shipBuilder_itemport_130 = importer.save_or_locate(shipBuilder_itemport_130)

    shipBuilder_itemport_130.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_131 = ItemPort()
    shipBuilder_itemport_131.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_131.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_131.flags = u'nose'
    shipBuilder_itemport_131.maxSize = 2L
    shipBuilder_itemport_131.minSize = 1L
    shipBuilder_itemport_131.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_131.portClass = 0L
    shipBuilder_itemport_131.image = None
    shipBuilder_itemport_131.tagLocationX = 0L
    shipBuilder_itemport_131.tagLocationY = 0L
    shipBuilder_itemport_131 = importer.save_or_locate(shipBuilder_itemport_131)

    shipBuilder_itemport_131.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_132 = ItemPort()
    shipBuilder_itemport_132.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_132.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_132.flags = u'upper left wing'
    shipBuilder_itemport_132.maxSize = 3L
    shipBuilder_itemport_132.minSize = 1L
    shipBuilder_itemport_132.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_132.portClass = 0L
    shipBuilder_itemport_132.image = None
    shipBuilder_itemport_132.tagLocationX = 0L
    shipBuilder_itemport_132.tagLocationY = 0L
    shipBuilder_itemport_132 = importer.save_or_locate(shipBuilder_itemport_132)

    shipBuilder_itemport_132.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_132.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_133 = ItemPort()
    shipBuilder_itemport_133.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_133.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_133.flags = u'left wing'
    shipBuilder_itemport_133.maxSize = 3L
    shipBuilder_itemport_133.minSize = 1L
    shipBuilder_itemport_133.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_133.portClass = 0L
    shipBuilder_itemport_133.image = None
    shipBuilder_itemport_133.tagLocationX = 0L
    shipBuilder_itemport_133.tagLocationY = 0L
    shipBuilder_itemport_133 = importer.save_or_locate(shipBuilder_itemport_133)

    shipBuilder_itemport_133.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_134 = ItemPort()
    shipBuilder_itemport_134.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_134.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_134.flags = u'upper right wing'
    shipBuilder_itemport_134.maxSize = 3L
    shipBuilder_itemport_134.minSize = 1L
    shipBuilder_itemport_134.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_134.portClass = 0L
    shipBuilder_itemport_134.image = None
    shipBuilder_itemport_134.tagLocationX = 0L
    shipBuilder_itemport_134.tagLocationY = 0L
    shipBuilder_itemport_134 = importer.save_or_locate(shipBuilder_itemport_134)

    shipBuilder_itemport_134.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_134.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_135 = ItemPort()
    shipBuilder_itemport_135.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_135.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_135.flags = u'right wing'
    shipBuilder_itemport_135.maxSize = 3L
    shipBuilder_itemport_135.minSize = 1L
    shipBuilder_itemport_135.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_135.portClass = 0L
    shipBuilder_itemport_135.image = None
    shipBuilder_itemport_135.tagLocationX = 0L
    shipBuilder_itemport_135.tagLocationY = 0L
    shipBuilder_itemport_135 = importer.save_or_locate(shipBuilder_itemport_135)

    shipBuilder_itemport_135.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_136 = ItemPort()
    shipBuilder_itemport_136.displayName = None
    shipBuilder_itemport_136.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_136.flags = u'main rear'
    shipBuilder_itemport_136.maxSize = 3L
    shipBuilder_itemport_136.minSize = 2L
    shipBuilder_itemport_136.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_136.portClass = 0L
    shipBuilder_itemport_136.image = None
    shipBuilder_itemport_136.tagLocationX = 0L
    shipBuilder_itemport_136.tagLocationY = 0L
    shipBuilder_itemport_136 = importer.save_or_locate(shipBuilder_itemport_136)

    shipBuilder_itemport_136.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_137 = ItemPort()
    shipBuilder_itemport_137.displayName = None
    shipBuilder_itemport_137.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_137.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_137.maxSize = 1L
    shipBuilder_itemport_137.minSize = 1L
    shipBuilder_itemport_137.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_137.portClass = 0L
    shipBuilder_itemport_137.image = None
    shipBuilder_itemport_137.tagLocationX = 0L
    shipBuilder_itemport_137.tagLocationY = 0L
    shipBuilder_itemport_137 = importer.save_or_locate(shipBuilder_itemport_137)

    shipBuilder_itemport_137.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_138 = ItemPort()
    shipBuilder_itemport_138.displayName = None
    shipBuilder_itemport_138.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_138.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_138.maxSize = 1L
    shipBuilder_itemport_138.minSize = 1L
    shipBuilder_itemport_138.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_138.portClass = 0L
    shipBuilder_itemport_138.image = None
    shipBuilder_itemport_138.tagLocationX = 0L
    shipBuilder_itemport_138.tagLocationY = 0L
    shipBuilder_itemport_138 = importer.save_or_locate(shipBuilder_itemport_138)

    shipBuilder_itemport_138.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_139 = ItemPort()
    shipBuilder_itemport_139.displayName = None
    shipBuilder_itemport_139.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_139.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_139.maxSize = 1L
    shipBuilder_itemport_139.minSize = 1L
    shipBuilder_itemport_139.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_139.portClass = 0L
    shipBuilder_itemport_139.image = None
    shipBuilder_itemport_139.tagLocationX = 0L
    shipBuilder_itemport_139.tagLocationY = 0L
    shipBuilder_itemport_139 = importer.save_or_locate(shipBuilder_itemport_139)

    shipBuilder_itemport_139.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_140 = ItemPort()
    shipBuilder_itemport_140.displayName = None
    shipBuilder_itemport_140.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_140.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_140.maxSize = 1L
    shipBuilder_itemport_140.minSize = 1L
    shipBuilder_itemport_140.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_140.portClass = 0L
    shipBuilder_itemport_140.image = None
    shipBuilder_itemport_140.tagLocationX = 0L
    shipBuilder_itemport_140.tagLocationY = 0L
    shipBuilder_itemport_140 = importer.save_or_locate(shipBuilder_itemport_140)

    shipBuilder_itemport_140.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_141 = ItemPort()
    shipBuilder_itemport_141.displayName = None
    shipBuilder_itemport_141.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_141.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_141.maxSize = 1L
    shipBuilder_itemport_141.minSize = 1L
    shipBuilder_itemport_141.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_141.portClass = 0L
    shipBuilder_itemport_141.image = None
    shipBuilder_itemport_141.tagLocationX = 0L
    shipBuilder_itemport_141.tagLocationY = 0L
    shipBuilder_itemport_141 = importer.save_or_locate(shipBuilder_itemport_141)

    shipBuilder_itemport_141.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_142 = ItemPort()
    shipBuilder_itemport_142.displayName = None
    shipBuilder_itemport_142.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_142.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_142.maxSize = 1L
    shipBuilder_itemport_142.minSize = 1L
    shipBuilder_itemport_142.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_142.portClass = 0L
    shipBuilder_itemport_142.image = None
    shipBuilder_itemport_142.tagLocationX = 0L
    shipBuilder_itemport_142.tagLocationY = 0L
    shipBuilder_itemport_142 = importer.save_or_locate(shipBuilder_itemport_142)

    shipBuilder_itemport_142.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_143 = ItemPort()
    shipBuilder_itemport_143.displayName = u'Class 3 Slot'
    shipBuilder_itemport_143.name = u'hardpoint_class_3'
    shipBuilder_itemport_143.flags = u'top mid'
    shipBuilder_itemport_143.maxSize = 3L
    shipBuilder_itemport_143.minSize = 1L
    shipBuilder_itemport_143.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_143.portClass = 0L
    shipBuilder_itemport_143.image = None
    shipBuilder_itemport_143.tagLocationX = 0L
    shipBuilder_itemport_143.tagLocationY = 0L
    shipBuilder_itemport_143 = importer.save_or_locate(shipBuilder_itemport_143)

    shipBuilder_itemport_143.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_143.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_144 = ItemPort()
    shipBuilder_itemport_144.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_144.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_144.flags = u'left'
    shipBuilder_itemport_144.maxSize = 2L
    shipBuilder_itemport_144.minSize = 1L
    shipBuilder_itemport_144.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_144.portClass = 0L
    shipBuilder_itemport_144.image = None
    shipBuilder_itemport_144.tagLocationX = 0L
    shipBuilder_itemport_144.tagLocationY = 0L
    shipBuilder_itemport_144 = importer.save_or_locate(shipBuilder_itemport_144)

    shipBuilder_itemport_144.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_145 = ItemPort()
    shipBuilder_itemport_145.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_145.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_145.flags = u'right'
    shipBuilder_itemport_145.maxSize = 2L
    shipBuilder_itemport_145.minSize = 1L
    shipBuilder_itemport_145.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_145.portClass = 0L
    shipBuilder_itemport_145.image = None
    shipBuilder_itemport_145.tagLocationX = 0L
    shipBuilder_itemport_145.tagLocationY = 0L
    shipBuilder_itemport_145 = importer.save_or_locate(shipBuilder_itemport_145)

    shipBuilder_itemport_145.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_146 = ItemPort()
    shipBuilder_itemport_146.displayName = u'Power Plant'
    shipBuilder_itemport_146.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_146.flags = u'main rear'
    shipBuilder_itemport_146.maxSize = 3L
    shipBuilder_itemport_146.minSize = 2L
    shipBuilder_itemport_146.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_146.portClass = 0L
    shipBuilder_itemport_146.image = None
    shipBuilder_itemport_146.tagLocationX = 0L
    shipBuilder_itemport_146.tagLocationY = 0L
    shipBuilder_itemport_146 = importer.save_or_locate(shipBuilder_itemport_146)

    shipBuilder_itemport_146.supportedTypes.add(shipBuilder_vehicleitemtype_4)

    shipBuilder_itemport_147 = ItemPort()
    shipBuilder_itemport_147.displayName = None
    shipBuilder_itemport_147.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_147.flags = u'main rear'
    shipBuilder_itemport_147.maxSize = 4L
    shipBuilder_itemport_147.minSize = 3L
    shipBuilder_itemport_147.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_147.portClass = 0L
    shipBuilder_itemport_147.image = None
    shipBuilder_itemport_147.tagLocationX = 0L
    shipBuilder_itemport_147.tagLocationY = 0L
    shipBuilder_itemport_147 = importer.save_or_locate(shipBuilder_itemport_147)

    shipBuilder_itemport_147.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_148 = ItemPort()
    shipBuilder_itemport_148.displayName = None
    shipBuilder_itemport_148.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_148.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_148.maxSize = 1L
    shipBuilder_itemport_148.minSize = 1L
    shipBuilder_itemport_148.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_148.portClass = 0L
    shipBuilder_itemport_148.image = None
    shipBuilder_itemport_148.tagLocationX = 0L
    shipBuilder_itemport_148.tagLocationY = 0L
    shipBuilder_itemport_148 = importer.save_or_locate(shipBuilder_itemport_148)

    shipBuilder_itemport_148.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_149 = ItemPort()
    shipBuilder_itemport_149.displayName = None
    shipBuilder_itemport_149.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_149.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_149.maxSize = 1L
    shipBuilder_itemport_149.minSize = 1L
    shipBuilder_itemport_149.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_149.portClass = 0L
    shipBuilder_itemport_149.image = None
    shipBuilder_itemport_149.tagLocationX = 0L
    shipBuilder_itemport_149.tagLocationY = 0L
    shipBuilder_itemport_149 = importer.save_or_locate(shipBuilder_itemport_149)

    shipBuilder_itemport_149.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_150 = ItemPort()
    shipBuilder_itemport_150.displayName = None
    shipBuilder_itemport_150.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_150.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_150.maxSize = 1L
    shipBuilder_itemport_150.minSize = 1L
    shipBuilder_itemport_150.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_150.portClass = 0L
    shipBuilder_itemport_150.image = None
    shipBuilder_itemport_150.tagLocationX = 0L
    shipBuilder_itemport_150.tagLocationY = 0L
    shipBuilder_itemport_150 = importer.save_or_locate(shipBuilder_itemport_150)

    shipBuilder_itemport_150.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_151 = ItemPort()
    shipBuilder_itemport_151.displayName = None
    shipBuilder_itemport_151.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_151.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_151.maxSize = 1L
    shipBuilder_itemport_151.minSize = 1L
    shipBuilder_itemport_151.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_151.portClass = 0L
    shipBuilder_itemport_151.image = None
    shipBuilder_itemport_151.tagLocationX = 0L
    shipBuilder_itemport_151.tagLocationY = 0L
    shipBuilder_itemport_151 = importer.save_or_locate(shipBuilder_itemport_151)

    shipBuilder_itemport_151.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_152 = ItemPort()
    shipBuilder_itemport_152.displayName = None
    shipBuilder_itemport_152.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_152.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_152.maxSize = 1L
    shipBuilder_itemport_152.minSize = 1L
    shipBuilder_itemport_152.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_152.portClass = 0L
    shipBuilder_itemport_152.image = None
    shipBuilder_itemport_152.tagLocationX = 0L
    shipBuilder_itemport_152.tagLocationY = 0L
    shipBuilder_itemport_152 = importer.save_or_locate(shipBuilder_itemport_152)

    shipBuilder_itemport_152.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_153 = ItemPort()
    shipBuilder_itemport_153.displayName = None
    shipBuilder_itemport_153.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_153.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_153.maxSize = 1L
    shipBuilder_itemport_153.minSize = 1L
    shipBuilder_itemport_153.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_153.portClass = 0L
    shipBuilder_itemport_153.image = None
    shipBuilder_itemport_153.tagLocationX = 0L
    shipBuilder_itemport_153.tagLocationY = 0L
    shipBuilder_itemport_153 = importer.save_or_locate(shipBuilder_itemport_153)

    shipBuilder_itemport_153.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_154 = ItemPort()
    shipBuilder_itemport_154.displayName = None
    shipBuilder_itemport_154.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_154.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_154.maxSize = 1L
    shipBuilder_itemport_154.minSize = 1L
    shipBuilder_itemport_154.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_154.portClass = 0L
    shipBuilder_itemport_154.image = None
    shipBuilder_itemport_154.tagLocationX = 0L
    shipBuilder_itemport_154.tagLocationY = 0L
    shipBuilder_itemport_154 = importer.save_or_locate(shipBuilder_itemport_154)

    shipBuilder_itemport_154.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_155 = ItemPort()
    shipBuilder_itemport_155.displayName = None
    shipBuilder_itemport_155.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_155.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_155.maxSize = 1L
    shipBuilder_itemport_155.minSize = 1L
    shipBuilder_itemport_155.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_155.portClass = 0L
    shipBuilder_itemport_155.image = None
    shipBuilder_itemport_155.tagLocationX = 0L
    shipBuilder_itemport_155.tagLocationY = 0L
    shipBuilder_itemport_155 = importer.save_or_locate(shipBuilder_itemport_155)

    shipBuilder_itemport_155.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_156 = ItemPort()
    shipBuilder_itemport_156.displayName = None
    shipBuilder_itemport_156.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_156.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_156.maxSize = 1L
    shipBuilder_itemport_156.minSize = 1L
    shipBuilder_itemport_156.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_156.portClass = 0L
    shipBuilder_itemport_156.image = None
    shipBuilder_itemport_156.tagLocationX = 0L
    shipBuilder_itemport_156.tagLocationY = 0L
    shipBuilder_itemport_156 = importer.save_or_locate(shipBuilder_itemport_156)

    shipBuilder_itemport_156.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_157 = ItemPort()
    shipBuilder_itemport_157.displayName = None
    shipBuilder_itemport_157.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_157.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_157.maxSize = 1L
    shipBuilder_itemport_157.minSize = 1L
    shipBuilder_itemport_157.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_157.portClass = 0L
    shipBuilder_itemport_157.image = None
    shipBuilder_itemport_157.tagLocationX = 0L
    shipBuilder_itemport_157.tagLocationY = 0L
    shipBuilder_itemport_157 = importer.save_or_locate(shipBuilder_itemport_157)

    shipBuilder_itemport_157.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_158 = ItemPort()
    shipBuilder_itemport_158.displayName = None
    shipBuilder_itemport_158.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_158.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_158.maxSize = 1L
    shipBuilder_itemport_158.minSize = 1L
    shipBuilder_itemport_158.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_158.portClass = 0L
    shipBuilder_itemport_158.image = None
    shipBuilder_itemport_158.tagLocationX = 0L
    shipBuilder_itemport_158.tagLocationY = 0L
    shipBuilder_itemport_158 = importer.save_or_locate(shipBuilder_itemport_158)

    shipBuilder_itemport_158.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_159 = ItemPort()
    shipBuilder_itemport_159.displayName = None
    shipBuilder_itemport_159.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_159.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_159.maxSize = 1L
    shipBuilder_itemport_159.minSize = 1L
    shipBuilder_itemport_159.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_159.portClass = 0L
    shipBuilder_itemport_159.image = None
    shipBuilder_itemport_159.tagLocationX = 0L
    shipBuilder_itemport_159.tagLocationY = 0L
    shipBuilder_itemport_159 = importer.save_or_locate(shipBuilder_itemport_159)

    shipBuilder_itemport_159.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    shipBuilder_itemport_160 = ItemPort()
    shipBuilder_itemport_160.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_160.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_160.flags = u'nose'
    shipBuilder_itemport_160.maxSize = 2L
    shipBuilder_itemport_160.minSize = 1L
    shipBuilder_itemport_160.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_160.portClass = 0L
    shipBuilder_itemport_160.image = None
    shipBuilder_itemport_160.tagLocationX = 0L
    shipBuilder_itemport_160.tagLocationY = 0L
    shipBuilder_itemport_160 = importer.save_or_locate(shipBuilder_itemport_160)

    shipBuilder_itemport_160.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_161 = ItemPort()
    shipBuilder_itemport_161.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_161.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_161.flags = u'upper left wing'
    shipBuilder_itemport_161.maxSize = 3L
    shipBuilder_itemport_161.minSize = 1L
    shipBuilder_itemport_161.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_161.portClass = 0L
    shipBuilder_itemport_161.image = None
    shipBuilder_itemport_161.tagLocationX = 0L
    shipBuilder_itemport_161.tagLocationY = 0L
    shipBuilder_itemport_161 = importer.save_or_locate(shipBuilder_itemport_161)

    shipBuilder_itemport_161.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_161.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_162 = ItemPort()
    shipBuilder_itemport_162.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_162.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_162.flags = u'left wing'
    shipBuilder_itemport_162.maxSize = 3L
    shipBuilder_itemport_162.minSize = 1L
    shipBuilder_itemport_162.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_162.portClass = 0L
    shipBuilder_itemport_162.image = None
    shipBuilder_itemport_162.tagLocationX = 0L
    shipBuilder_itemport_162.tagLocationY = 0L
    shipBuilder_itemport_162 = importer.save_or_locate(shipBuilder_itemport_162)

    shipBuilder_itemport_162.supportedTypes.add(shipBuilder_vehicleitemtype_2)

    shipBuilder_itemport_163 = ItemPort()
    shipBuilder_itemport_163.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_163.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_163.flags = u'upper right wing'
    shipBuilder_itemport_163.maxSize = 3L
    shipBuilder_itemport_163.minSize = 1L
    shipBuilder_itemport_163.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_163.portClass = 0L
    shipBuilder_itemport_163.image = None
    shipBuilder_itemport_163.tagLocationX = 0L
    shipBuilder_itemport_163.tagLocationY = 0L
    shipBuilder_itemport_163 = importer.save_or_locate(shipBuilder_itemport_163)

    shipBuilder_itemport_163.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_163.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_164 = ItemPort()
    shipBuilder_itemport_164.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_164.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_164.flags = u'right wing'
    shipBuilder_itemport_164.maxSize = 3L
    shipBuilder_itemport_164.minSize = 1L
    shipBuilder_itemport_164.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_164.portClass = 0L
    shipBuilder_itemport_164.image = None
    shipBuilder_itemport_164.tagLocationX = 0L
    shipBuilder_itemport_164.tagLocationY = 0L
    shipBuilder_itemport_164 = importer.save_or_locate(shipBuilder_itemport_164)

    shipBuilder_itemport_164.supportedTypes.add(shipBuilder_vehicleitemtype_2)

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

    #Processing model: Build

    from shipBuilder.models import Build


    #Processing model: BuildHardpoint

    from shipBuilder.models import BuildHardpoint


    #Processing model: BuildEngineMod

    from shipBuilder.models import BuildEngineMod


    #Processing model: BuildHullMod

    from shipBuilder.models import BuildHullMod


