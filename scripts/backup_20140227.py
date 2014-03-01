#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# which this script has hooks to.
#
# On that file, don't forget to add the necessary Django imports
# and take a look at how locate_object() and save_or_locate()
# are implemented here and expected to behave.
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


IMPORT_HELPER_AVAILABLE = False
try:
    import import_helper
    IMPORT_HELPER_AVAILABLE = True
except ImportError:
    pass

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

def run():
    #initial imports

    def locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
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


        if IMPORT_HELPER_AVAILABLE and hasattr(import_helper, "locate_object"):
            return import_helper.locate_object(original_class, original_pk_name, the_class, pk_name, pk_value, obj_content)

        search_data = { pk_name: pk_value }
        the_obj =the_class.objects.get(**search_data)
        return the_obj

    def save_or_locate(the_obj):
        if IMPORT_HELPER_AVAILABLE and hasattr(import_helper, "save_or_locate"):
            the_obj = import_helper.save_or_locate(the_obj)
        else:
            the_obj.save()
        return the_obj



    #Processing model: Group

    from django.contrib.auth.models import Group


    #Processing model: User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = u'pbkdf2_sha256$10000$9vVBhI0AgB5H$n8lJa5MNMaD2TTc9gmbNU5d1eT/bPaNWHmHHirhooK8='
    auth_user_1.last_login = datetime.datetime(2014, 1, 4, 22, 20, 20, 33162)
    auth_user_1.is_superuser = True
    auth_user_1.username = u'agathorn'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u''
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = datetime.datetime(2013, 12, 24, 2, 40, 51, 486199)
    auth_user_1 = save_or_locate(auth_user_1)

    #Processing model: Session

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'zb5u7uatk6ajote406xjk1w1fxwljrlj'
    django_session_1.session_data = u'YzQ2MDdhYzk2ZTE4NjJlZmE2MTU3YmVjYTc3ZWI5NmRjZWU0NWRiNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_1.expire_date = datetime.datetime(2014, 1, 7, 2, 45, 53, 100648)
    django_session_1 = save_or_locate(django_session_1)

    django_session_2 = Session()
    django_session_2.session_key = u'uy25tyafygtiuq0p0rdya4kqbspt7t4s'
    django_session_2.session_data = u'YzQ2MDdhYzk2ZTE4NjJlZmE2MTU3YmVjYTc3ZWI5NmRjZWU0NWRiNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQRLAXUu'
    django_session_2.expire_date = datetime.datetime(2014, 1, 18, 22, 20, 20, 35067)
    django_session_2 = save_or_locate(django_session_2)

    #Processing model: Manufacturer

    from shipBuilder.models import Manufacturer

    shipBuilder_manufacturer_1 = Manufacturer()
    shipBuilder_manufacturer_1.name = u'Acom'
    shipBuilder_manufacturer_1.description = u''
    shipBuilder_manufacturer_1 = save_or_locate(shipBuilder_manufacturer_1)

    shipBuilder_manufacturer_2 = Manufacturer()
    shipBuilder_manufacturer_2.name = u'Hammer Propulsion'
    shipBuilder_manufacturer_2.description = u''
    shipBuilder_manufacturer_2 = save_or_locate(shipBuilder_manufacturer_2)

    shipBuilder_manufacturer_3 = Manufacturer()
    shipBuilder_manufacturer_3.name = u'A&R'
    shipBuilder_manufacturer_3.description = u''
    shipBuilder_manufacturer_3 = save_or_locate(shipBuilder_manufacturer_3)

    shipBuilder_manufacturer_4 = Manufacturer()
    shipBuilder_manufacturer_4.name = u'RSI'
    shipBuilder_manufacturer_4.description = u''
    shipBuilder_manufacturer_4 = save_or_locate(shipBuilder_manufacturer_4)

    shipBuilder_manufacturer_5 = Manufacturer()
    shipBuilder_manufacturer_5.name = u'Ace Astrogation'
    shipBuilder_manufacturer_5.description = u''
    shipBuilder_manufacturer_5 = save_or_locate(shipBuilder_manufacturer_5)

    shipBuilder_manufacturer_6 = Manufacturer()
    shipBuilder_manufacturer_6.name = u'Ageis Dynamics'
    shipBuilder_manufacturer_6.description = u''
    shipBuilder_manufacturer_6 = save_or_locate(shipBuilder_manufacturer_6)

    shipBuilder_manufacturer_7 = Manufacturer()
    shipBuilder_manufacturer_7.name = u'Alliance Startech'
    shipBuilder_manufacturer_7.description = u''
    shipBuilder_manufacturer_7 = save_or_locate(shipBuilder_manufacturer_7)

    shipBuilder_manufacturer_8 = Manufacturer()
    shipBuilder_manufacturer_8.name = u'Anvil Aerospace'
    shipBuilder_manufacturer_8.description = u''
    shipBuilder_manufacturer_8 = save_or_locate(shipBuilder_manufacturer_8)

    shipBuilder_manufacturer_9 = Manufacturer()
    shipBuilder_manufacturer_9.name = u'ArcCorp'
    shipBuilder_manufacturer_9.description = u''
    shipBuilder_manufacturer_9 = save_or_locate(shipBuilder_manufacturer_9)

    shipBuilder_manufacturer_10 = Manufacturer()
    shipBuilder_manufacturer_10.name = u'Behring'
    shipBuilder_manufacturer_10.description = u''
    shipBuilder_manufacturer_10 = save_or_locate(shipBuilder_manufacturer_10)

    shipBuilder_manufacturer_11 = Manufacturer()
    shipBuilder_manufacturer_11.name = u'A & R'
    shipBuilder_manufacturer_11.description = u''
    shipBuilder_manufacturer_11 = save_or_locate(shipBuilder_manufacturer_11)

    shipBuilder_manufacturer_12 = Manufacturer()
    shipBuilder_manufacturer_12.name = u'Dragon STC'
    shipBuilder_manufacturer_12.description = u''
    shipBuilder_manufacturer_12 = save_or_locate(shipBuilder_manufacturer_12)

    shipBuilder_manufacturer_13 = Manufacturer()
    shipBuilder_manufacturer_13.name = u'Greycat Industrial'
    shipBuilder_manufacturer_13.description = u''
    shipBuilder_manufacturer_13 = save_or_locate(shipBuilder_manufacturer_13)

    shipBuilder_manufacturer_14 = Manufacturer()
    shipBuilder_manufacturer_14.name = u'Groupe Nouveau Paradigme'
    shipBuilder_manufacturer_14.description = u''
    shipBuilder_manufacturer_14 = save_or_locate(shipBuilder_manufacturer_14)

    shipBuilder_manufacturer_15 = Manufacturer()
    shipBuilder_manufacturer_15.name = u'VOLT'
    shipBuilder_manufacturer_15.description = u''
    shipBuilder_manufacturer_15 = save_or_locate(shipBuilder_manufacturer_15)

    shipBuilder_manufacturer_16 = Manufacturer()
    shipBuilder_manufacturer_16.name = u'Juno Starwerk'
    shipBuilder_manufacturer_16.description = u''
    shipBuilder_manufacturer_16 = save_or_locate(shipBuilder_manufacturer_16)

    shipBuilder_manufacturer_17 = Manufacturer()
    shipBuilder_manufacturer_17.name = u'Klaus & Werner'
    shipBuilder_manufacturer_17.description = u''
    shipBuilder_manufacturer_17 = save_or_locate(shipBuilder_manufacturer_17)

    shipBuilder_manufacturer_18 = Manufacturer()
    shipBuilder_manufacturer_18.name = u'KDK'
    shipBuilder_manufacturer_18.description = u''
    shipBuilder_manufacturer_18 = save_or_locate(shipBuilder_manufacturer_18)

    shipBuilder_manufacturer_19 = Manufacturer()
    shipBuilder_manufacturer_19.name = u'KnightBridge'
    shipBuilder_manufacturer_19.description = u''
    shipBuilder_manufacturer_19 = save_or_locate(shipBuilder_manufacturer_19)

    shipBuilder_manufacturer_20 = Manufacturer()
    shipBuilder_manufacturer_20.name = u'Lightning Power ltd.'
    shipBuilder_manufacturer_20.description = u''
    shipBuilder_manufacturer_20 = save_or_locate(shipBuilder_manufacturer_20)

    shipBuilder_manufacturer_21 = Manufacturer()
    shipBuilder_manufacturer_21.name = u'Max Ox'
    shipBuilder_manufacturer_21.description = u''
    shipBuilder_manufacturer_21 = save_or_locate(shipBuilder_manufacturer_21)

    shipBuilder_manufacturer_22 = Manufacturer()
    shipBuilder_manufacturer_22.name = u'Origin Jumpworks'
    shipBuilder_manufacturer_22.description = u''
    shipBuilder_manufacturer_22 = save_or_locate(shipBuilder_manufacturer_22)

    shipBuilder_manufacturer_23 = Manufacturer()
    shipBuilder_manufacturer_23.name = u'OKB Voshkod'
    shipBuilder_manufacturer_23.description = u''
    shipBuilder_manufacturer_23 = save_or_locate(shipBuilder_manufacturer_23)

    shipBuilder_manufacturer_24 = Manufacturer()
    shipBuilder_manufacturer_24.name = u'Sakura Sun'
    shipBuilder_manufacturer_24.description = u''
    shipBuilder_manufacturer_24 = save_or_locate(shipBuilder_manufacturer_24)

    shipBuilder_manufacturer_25 = Manufacturer()
    shipBuilder_manufacturer_25.name = u'V&uul Tech'
    shipBuilder_manufacturer_25.description = u''
    shipBuilder_manufacturer_25 = save_or_locate(shipBuilder_manufacturer_25)

    shipBuilder_manufacturer_26 = Manufacturer()
    shipBuilder_manufacturer_26.name = u'Stor-All'
    shipBuilder_manufacturer_26.description = u''
    shipBuilder_manufacturer_26 = save_or_locate(shipBuilder_manufacturer_26)

    shipBuilder_manufacturer_27 = Manufacturer()
    shipBuilder_manufacturer_27.name = u'Talon'
    shipBuilder_manufacturer_27.description = u''
    shipBuilder_manufacturer_27 = save_or_locate(shipBuilder_manufacturer_27)

    shipBuilder_manufacturer_28 = Manufacturer()
    shipBuilder_manufacturer_28.name = u'Wei-Tek'
    shipBuilder_manufacturer_28.description = u''
    shipBuilder_manufacturer_28 = save_or_locate(shipBuilder_manufacturer_28)

    shipBuilder_manufacturer_29 = Manufacturer()
    shipBuilder_manufacturer_29.name = u'XForge'
    shipBuilder_manufacturer_29.description = u''
    shipBuilder_manufacturer_29 = save_or_locate(shipBuilder_manufacturer_29)

    shipBuilder_manufacturer_30 = Manufacturer()
    shipBuilder_manufacturer_30.name = u'Anvil'
    shipBuilder_manufacturer_30.description = u''
    shipBuilder_manufacturer_30 = save_or_locate(shipBuilder_manufacturer_30)

    #Processing model: ItemCategory

    from shipBuilder.models import ItemCategory


    #Processing model: ItemType

    from shipBuilder.models import ItemType


    #Processing model: WeaponData

    from shipBuilder.models import WeaponData


    #Processing model: PowerplantData

    from shipBuilder.models import PowerplantData


    #Processing model: ThrusterData

    from shipBuilder.models import ThrusterData


    #Processing model: ShieldData

    from shipBuilder.models import ShieldData


    #Processing model: EngineIntakeData

    from shipBuilder.models import EngineIntakeData


    #Processing model: Ship

    from shipBuilder.models import Ship


    #Processing model: Image

    from shipBuilder.models import Image


    #Processing model: LocalizedDescriptionManufacturer

    from shipBuilder.models import LocalizedDescriptionManufacturer


    #Processing model: VehicleItemType

    from shipBuilder.models import VehicleItemType

    shipBuilder_vehicleitemtype_1 = VehicleItemType()
    shipBuilder_vehicleitemtype_1.name = u'powerplant:power'
    shipBuilder_vehicleitemtype_1.typeName = u'powerplant'
    shipBuilder_vehicleitemtype_1.subTypeName = u'power'
    shipBuilder_vehicleitemtype_1 = save_or_locate(shipBuilder_vehicleitemtype_1)

    shipBuilder_vehicleitemtype_2 = VehicleItemType()
    shipBuilder_vehicleitemtype_2.name = u'thruster:vectorthruster'
    shipBuilder_vehicleitemtype_2.typeName = u'thruster'
    shipBuilder_vehicleitemtype_2.subTypeName = u'vectorthruster'
    shipBuilder_vehicleitemtype_2 = save_or_locate(shipBuilder_vehicleitemtype_2)

    shipBuilder_vehicleitemtype_3 = VehicleItemType()
    shipBuilder_vehicleitemtype_3.name = u'weapon:gunturret'
    shipBuilder_vehicleitemtype_3.typeName = u'weapon'
    shipBuilder_vehicleitemtype_3.subTypeName = u'gunturret'
    shipBuilder_vehicleitemtype_3 = save_or_locate(shipBuilder_vehicleitemtype_3)

    shipBuilder_vehicleitemtype_4 = VehicleItemType()
    shipBuilder_vehicleitemtype_4.name = u'thruster:flexthruster'
    shipBuilder_vehicleitemtype_4.typeName = u'thruster'
    shipBuilder_vehicleitemtype_4.subTypeName = u'flexthruster'
    shipBuilder_vehicleitemtype_4 = save_or_locate(shipBuilder_vehicleitemtype_4)

    shipBuilder_vehicleitemtype_5 = VehicleItemType()
    shipBuilder_vehicleitemtype_5.name = u'weapon:missileturret'
    shipBuilder_vehicleitemtype_5.typeName = u'weapon'
    shipBuilder_vehicleitemtype_5.subTypeName = u'MissileTurret'
    shipBuilder_vehicleitemtype_5 = save_or_locate(shipBuilder_vehicleitemtype_5)

    shipBuilder_vehicleitemtype_6 = VehicleItemType()
    shipBuilder_vehicleitemtype_6.name = u'radar'
    shipBuilder_vehicleitemtype_6.typeName = u'radar'
    shipBuilder_vehicleitemtype_6.subTypeName = u''
    shipBuilder_vehicleitemtype_6 = save_or_locate(shipBuilder_vehicleitemtype_6)

    shipBuilder_vehicleitemtype_7 = VehicleItemType()
    shipBuilder_vehicleitemtype_7.name = u'weapon:missilerack'
    shipBuilder_vehicleitemtype_7.typeName = u'weapon'
    shipBuilder_vehicleitemtype_7.subTypeName = u'MissileRack'
    shipBuilder_vehicleitemtype_7 = save_or_locate(shipBuilder_vehicleitemtype_7)

    shipBuilder_vehicleitemtype_8 = VehicleItemType()
    shipBuilder_vehicleitemtype_8.name = u'display'
    shipBuilder_vehicleitemtype_8.typeName = u'display'
    shipBuilder_vehicleitemtype_8.subTypeName = u''
    shipBuilder_vehicleitemtype_8 = save_or_locate(shipBuilder_vehicleitemtype_8)

    shipBuilder_vehicleitemtype_9 = VehicleItemType()
    shipBuilder_vehicleitemtype_9.name = u'weapon:gun'
    shipBuilder_vehicleitemtype_9.typeName = u'weapon'
    shipBuilder_vehicleitemtype_9.subTypeName = u'Gun'
    shipBuilder_vehicleitemtype_9 = save_or_locate(shipBuilder_vehicleitemtype_9)

    shipBuilder_vehicleitemtype_10 = VehicleItemType()
    shipBuilder_vehicleitemtype_10.name = u'powerplant'
    shipBuilder_vehicleitemtype_10.typeName = u'powerplant'
    shipBuilder_vehicleitemtype_10.subTypeName = u''
    shipBuilder_vehicleitemtype_10 = save_or_locate(shipBuilder_vehicleitemtype_10)

    shipBuilder_vehicleitemtype_11 = VehicleItemType()
    shipBuilder_vehicleitemtype_11.name = u'thruster'
    shipBuilder_vehicleitemtype_11.typeName = u'thruster'
    shipBuilder_vehicleitemtype_11.subTypeName = u''
    shipBuilder_vehicleitemtype_11 = save_or_locate(shipBuilder_vehicleitemtype_11)

    shipBuilder_vehicleitemtype_12 = VehicleItemType()
    shipBuilder_vehicleitemtype_12.name = u'container'
    shipBuilder_vehicleitemtype_12.typeName = u'container'
    shipBuilder_vehicleitemtype_12.subTypeName = u''
    shipBuilder_vehicleitemtype_12 = save_or_locate(shipBuilder_vehicleitemtype_12)

    shipBuilder_vehicleitemtype_13 = VehicleItemType()
    shipBuilder_vehicleitemtype_13.name = u'thruster:jointthruster'
    shipBuilder_vehicleitemtype_13.typeName = u'thruster'
    shipBuilder_vehicleitemtype_13.subTypeName = u'jointthruster'
    shipBuilder_vehicleitemtype_13 = save_or_locate(shipBuilder_vehicleitemtype_13)

    shipBuilder_vehicleitemtype_14 = VehicleItemType()
    shipBuilder_vehicleitemtype_14.name = u'thruster:fixedthruster'
    shipBuilder_vehicleitemtype_14.typeName = u'thruster'
    shipBuilder_vehicleitemtype_14.subTypeName = u'fixedthruster'
    shipBuilder_vehicleitemtype_14 = save_or_locate(shipBuilder_vehicleitemtype_14)

    shipBuilder_vehicleitemtype_15 = VehicleItemType()
    shipBuilder_vehicleitemtype_15.name = u'weapon'
    shipBuilder_vehicleitemtype_15.typeName = u'weapon'
    shipBuilder_vehicleitemtype_15.subTypeName = u''
    shipBuilder_vehicleitemtype_15 = save_or_locate(shipBuilder_vehicleitemtype_15)

    shipBuilder_vehicleitemtype_16 = VehicleItemType()
    shipBuilder_vehicleitemtype_16.name = u'battery:power'
    shipBuilder_vehicleitemtype_16.typeName = u'battery'
    shipBuilder_vehicleitemtype_16.subTypeName = u'power'
    shipBuilder_vehicleitemtype_16 = save_or_locate(shipBuilder_vehicleitemtype_16)

    shipBuilder_vehicleitemtype_17 = VehicleItemType()
    shipBuilder_vehicleitemtype_17.name = u'cooler:heat'
    shipBuilder_vehicleitemtype_17.typeName = u'cooler'
    shipBuilder_vehicleitemtype_17.subTypeName = u'heat'
    shipBuilder_vehicleitemtype_17 = save_or_locate(shipBuilder_vehicleitemtype_17)

    shipBuilder_vehicleitemtype_18 = VehicleItemType()
    shipBuilder_vehicleitemtype_18.name = u'display:radar'
    shipBuilder_vehicleitemtype_18.typeName = u'display'
    shipBuilder_vehicleitemtype_18.subTypeName = u'radar'
    shipBuilder_vehicleitemtype_18 = save_or_locate(shipBuilder_vehicleitemtype_18)

    shipBuilder_vehicleitemtype_19 = VehicleItemType()
    shipBuilder_vehicleitemtype_19.name = u'radar:longrangeradar'
    shipBuilder_vehicleitemtype_19.typeName = u'radar'
    shipBuilder_vehicleitemtype_19.subTypeName = u'longrangeradar'
    shipBuilder_vehicleitemtype_19 = save_or_locate(shipBuilder_vehicleitemtype_19)

    shipBuilder_vehicleitemtype_20 = VehicleItemType()
    shipBuilder_vehicleitemtype_20.name = u'radar:midrangeradar'
    shipBuilder_vehicleitemtype_20.typeName = u'radar'
    shipBuilder_vehicleitemtype_20.subTypeName = u'midrangeradar'
    shipBuilder_vehicleitemtype_20 = save_or_locate(shipBuilder_vehicleitemtype_20)

    shipBuilder_vehicleitemtype_21 = VehicleItemType()
    shipBuilder_vehicleitemtype_21.name = u'radar:shortrangeradar'
    shipBuilder_vehicleitemtype_21.typeName = u'radar'
    shipBuilder_vehicleitemtype_21.subTypeName = u'shortrangeradar'
    shipBuilder_vehicleitemtype_21 = save_or_locate(shipBuilder_vehicleitemtype_21)

    shipBuilder_vehicleitemtype_22 = VehicleItemType()
    shipBuilder_vehicleitemtype_22.name = u'avionics:targetingcomputer'
    shipBuilder_vehicleitemtype_22.typeName = u'avionics'
    shipBuilder_vehicleitemtype_22.subTypeName = u'targetingcomputer'
    shipBuilder_vehicleitemtype_22 = save_or_locate(shipBuilder_vehicleitemtype_22)

    shipBuilder_vehicleitemtype_23 = VehicleItemType()
    shipBuilder_vehicleitemtype_23.name = u'visor:tagging'
    shipBuilder_vehicleitemtype_23.typeName = u'visor'
    shipBuilder_vehicleitemtype_23.subTypeName = u'tagging'
    shipBuilder_vehicleitemtype_23 = save_or_locate(shipBuilder_vehicleitemtype_23)

    shipBuilder_vehicleitemtype_24 = VehicleItemType()
    shipBuilder_vehicleitemtype_24.name = u'display:weapon'
    shipBuilder_vehicleitemtype_24.typeName = u'display'
    shipBuilder_vehicleitemtype_24.subTypeName = u'weapon'
    shipBuilder_vehicleitemtype_24 = save_or_locate(shipBuilder_vehicleitemtype_24)

    shipBuilder_vehicleitemtype_25 = VehicleItemType()
    shipBuilder_vehicleitemtype_25.name = u'container:cargo'
    shipBuilder_vehicleitemtype_25.typeName = u'container'
    shipBuilder_vehicleitemtype_25.subTypeName = u'cargo'
    shipBuilder_vehicleitemtype_25 = save_or_locate(shipBuilder_vehicleitemtype_25)

    shipBuilder_vehicleitemtype_26 = VehicleItemType()
    shipBuilder_vehicleitemtype_26.name = u'mainthruster'
    shipBuilder_vehicleitemtype_26.typeName = u'mainthruster'
    shipBuilder_vehicleitemtype_26.subTypeName = u''
    shipBuilder_vehicleitemtype_26 = save_or_locate(shipBuilder_vehicleitemtype_26)

    shipBuilder_vehicleitemtype_27 = VehicleItemType()
    shipBuilder_vehicleitemtype_27.name = u'light'
    shipBuilder_vehicleitemtype_27.typeName = u'light'
    shipBuilder_vehicleitemtype_27.subTypeName = u''
    shipBuilder_vehicleitemtype_27 = save_or_locate(shipBuilder_vehicleitemtype_27)

    shipBuilder_vehicleitemtype_28 = VehicleItemType()
    shipBuilder_vehicleitemtype_28.name = u'seat:pilot'
    shipBuilder_vehicleitemtype_28.typeName = u'seat'
    shipBuilder_vehicleitemtype_28.subTypeName = u'Pilot'
    shipBuilder_vehicleitemtype_28 = save_or_locate(shipBuilder_vehicleitemtype_28)

    #Processing model: VehicleItemAvionics

    from shipBuilder.models import VehicleItemAvionics

    shipBuilder_vehicleitemavionics_1 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_1.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_1.value = u'20'
    shipBuilder_vehicleitemavionics_1 = save_or_locate(shipBuilder_vehicleitemavionics_1)

    shipBuilder_vehicleitemavionics_2 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_2.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_2.value = u'0'
    shipBuilder_vehicleitemavionics_2 = save_or_locate(shipBuilder_vehicleitemavionics_2)

    shipBuilder_vehicleitemavionics_3 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_3.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_3.value = u'20'
    shipBuilder_vehicleitemavionics_3 = save_or_locate(shipBuilder_vehicleitemavionics_3)

    shipBuilder_vehicleitemavionics_4 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_4.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_4.value = u'0'
    shipBuilder_vehicleitemavionics_4 = save_or_locate(shipBuilder_vehicleitemavionics_4)

    shipBuilder_vehicleitemavionics_5 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_5.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_5.value = u'20'
    shipBuilder_vehicleitemavionics_5 = save_or_locate(shipBuilder_vehicleitemavionics_5)

    shipBuilder_vehicleitemavionics_6 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_6.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_6.value = u'0'
    shipBuilder_vehicleitemavionics_6 = save_or_locate(shipBuilder_vehicleitemavionics_6)

    shipBuilder_vehicleitemavionics_7 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_7.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_7.value = u'20'
    shipBuilder_vehicleitemavionics_7 = save_or_locate(shipBuilder_vehicleitemavionics_7)

    shipBuilder_vehicleitemavionics_8 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_8.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_8.value = u'0'
    shipBuilder_vehicleitemavionics_8 = save_or_locate(shipBuilder_vehicleitemavionics_8)

    shipBuilder_vehicleitemavionics_9 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_9.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_9.value = u'20'
    shipBuilder_vehicleitemavionics_9 = save_or_locate(shipBuilder_vehicleitemavionics_9)

    shipBuilder_vehicleitemavionics_10 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_10.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_10.value = u'0'
    shipBuilder_vehicleitemavionics_10 = save_or_locate(shipBuilder_vehicleitemavionics_10)

    shipBuilder_vehicleitemavionics_11 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_11.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_11.value = u'20'
    shipBuilder_vehicleitemavionics_11 = save_or_locate(shipBuilder_vehicleitemavionics_11)

    shipBuilder_vehicleitemavionics_12 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_12.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_12.value = u'0'
    shipBuilder_vehicleitemavionics_12 = save_or_locate(shipBuilder_vehicleitemavionics_12)

    shipBuilder_vehicleitemavionics_13 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_13.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_13.value = u'20'
    shipBuilder_vehicleitemavionics_13 = save_or_locate(shipBuilder_vehicleitemavionics_13)

    shipBuilder_vehicleitemavionics_14 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_14.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_14.value = u'0'
    shipBuilder_vehicleitemavionics_14 = save_or_locate(shipBuilder_vehicleitemavionics_14)

    shipBuilder_vehicleitemavionics_15 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_15.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_15.value = u'20'
    shipBuilder_vehicleitemavionics_15 = save_or_locate(shipBuilder_vehicleitemavionics_15)

    shipBuilder_vehicleitemavionics_16 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_16.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_16.value = u'0'
    shipBuilder_vehicleitemavionics_16 = save_or_locate(shipBuilder_vehicleitemavionics_16)

    shipBuilder_vehicleitemavionics_17 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_17.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_17.value = u'20'
    shipBuilder_vehicleitemavionics_17 = save_or_locate(shipBuilder_vehicleitemavionics_17)

    shipBuilder_vehicleitemavionics_18 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_18.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_18.value = u'0'
    shipBuilder_vehicleitemavionics_18 = save_or_locate(shipBuilder_vehicleitemavionics_18)

    shipBuilder_vehicleitemavionics_19 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_19.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_19.value = u'20'
    shipBuilder_vehicleitemavionics_19 = save_or_locate(shipBuilder_vehicleitemavionics_19)

    shipBuilder_vehicleitemavionics_20 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_20.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_20.value = u'0'
    shipBuilder_vehicleitemavionics_20 = save_or_locate(shipBuilder_vehicleitemavionics_20)

    shipBuilder_vehicleitemavionics_21 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_21.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_21.value = u'20'
    shipBuilder_vehicleitemavionics_21 = save_or_locate(shipBuilder_vehicleitemavionics_21)

    shipBuilder_vehicleitemavionics_22 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_22.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_22.value = u'0'
    shipBuilder_vehicleitemavionics_22 = save_or_locate(shipBuilder_vehicleitemavionics_22)

    shipBuilder_vehicleitemavionics_23 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_23.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_23.value = u'20'
    shipBuilder_vehicleitemavionics_23 = save_or_locate(shipBuilder_vehicleitemavionics_23)

    shipBuilder_vehicleitemavionics_24 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_24.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_24.value = u'0'
    shipBuilder_vehicleitemavionics_24 = save_or_locate(shipBuilder_vehicleitemavionics_24)

    shipBuilder_vehicleitemavionics_25 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_25.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_25.value = u'20'
    shipBuilder_vehicleitemavionics_25 = save_or_locate(shipBuilder_vehicleitemavionics_25)

    shipBuilder_vehicleitemavionics_26 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_26.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_26.value = u'0'
    shipBuilder_vehicleitemavionics_26 = save_or_locate(shipBuilder_vehicleitemavionics_26)

    shipBuilder_vehicleitemavionics_27 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_27.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_27.value = u'20'
    shipBuilder_vehicleitemavionics_27 = save_or_locate(shipBuilder_vehicleitemavionics_27)

    shipBuilder_vehicleitemavionics_28 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_28.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_28.value = u'0'
    shipBuilder_vehicleitemavionics_28 = save_or_locate(shipBuilder_vehicleitemavionics_28)

    shipBuilder_vehicleitemavionics_29 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_29.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_29.value = u'20'
    shipBuilder_vehicleitemavionics_29 = save_or_locate(shipBuilder_vehicleitemavionics_29)

    shipBuilder_vehicleitemavionics_30 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_30.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_30.value = u'0'
    shipBuilder_vehicleitemavionics_30 = save_or_locate(shipBuilder_vehicleitemavionics_30)

    shipBuilder_vehicleitemavionics_31 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_31.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_31.value = u'20'
    shipBuilder_vehicleitemavionics_31 = save_or_locate(shipBuilder_vehicleitemavionics_31)

    shipBuilder_vehicleitemavionics_32 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_32.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_32.value = u'0'
    shipBuilder_vehicleitemavionics_32 = save_or_locate(shipBuilder_vehicleitemavionics_32)

    shipBuilder_vehicleitemavionics_33 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_33.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_33.value = u'20'
    shipBuilder_vehicleitemavionics_33 = save_or_locate(shipBuilder_vehicleitemavionics_33)

    shipBuilder_vehicleitemavionics_34 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_34.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_34.value = u'0'
    shipBuilder_vehicleitemavionics_34 = save_or_locate(shipBuilder_vehicleitemavionics_34)

    shipBuilder_vehicleitemavionics_35 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_35.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_35.value = u'20'
    shipBuilder_vehicleitemavionics_35 = save_or_locate(shipBuilder_vehicleitemavionics_35)

    shipBuilder_vehicleitemavionics_36 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_36.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_36.value = u'0'
    shipBuilder_vehicleitemavionics_36 = save_or_locate(shipBuilder_vehicleitemavionics_36)

    shipBuilder_vehicleitemavionics_37 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_37.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_37.value = u'20'
    shipBuilder_vehicleitemavionics_37 = save_or_locate(shipBuilder_vehicleitemavionics_37)

    shipBuilder_vehicleitemavionics_38 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_38.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_38.value = u'0'
    shipBuilder_vehicleitemavionics_38 = save_or_locate(shipBuilder_vehicleitemavionics_38)

    shipBuilder_vehicleitemavionics_39 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_39.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_39.value = u'20'
    shipBuilder_vehicleitemavionics_39 = save_or_locate(shipBuilder_vehicleitemavionics_39)

    shipBuilder_vehicleitemavionics_40 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_40.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_40.value = u'0'
    shipBuilder_vehicleitemavionics_40 = save_or_locate(shipBuilder_vehicleitemavionics_40)

    shipBuilder_vehicleitemavionics_41 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_41.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_41.value = u'20'
    shipBuilder_vehicleitemavionics_41 = save_or_locate(shipBuilder_vehicleitemavionics_41)

    shipBuilder_vehicleitemavionics_42 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_42.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_42.value = u'0'
    shipBuilder_vehicleitemavionics_42 = save_or_locate(shipBuilder_vehicleitemavionics_42)

    shipBuilder_vehicleitemavionics_43 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_43.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_43.value = u'20'
    shipBuilder_vehicleitemavionics_43 = save_or_locate(shipBuilder_vehicleitemavionics_43)

    shipBuilder_vehicleitemavionics_44 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_44.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_44.value = u'0'
    shipBuilder_vehicleitemavionics_44 = save_or_locate(shipBuilder_vehicleitemavionics_44)

    shipBuilder_vehicleitemavionics_45 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_45.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_45.value = u'20'
    shipBuilder_vehicleitemavionics_45 = save_or_locate(shipBuilder_vehicleitemavionics_45)

    shipBuilder_vehicleitemavionics_46 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_46.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_46.value = u'0'
    shipBuilder_vehicleitemavionics_46 = save_or_locate(shipBuilder_vehicleitemavionics_46)

    shipBuilder_vehicleitemavionics_47 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_47.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_47.value = u'20'
    shipBuilder_vehicleitemavionics_47 = save_or_locate(shipBuilder_vehicleitemavionics_47)

    shipBuilder_vehicleitemavionics_48 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_48.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_48.value = u'0'
    shipBuilder_vehicleitemavionics_48 = save_or_locate(shipBuilder_vehicleitemavionics_48)

    shipBuilder_vehicleitemavionics_49 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_49.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_49.value = u'20'
    shipBuilder_vehicleitemavionics_49 = save_or_locate(shipBuilder_vehicleitemavionics_49)

    shipBuilder_vehicleitemavionics_50 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_50.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_50.value = u'0'
    shipBuilder_vehicleitemavionics_50 = save_or_locate(shipBuilder_vehicleitemavionics_50)

    shipBuilder_vehicleitemavionics_51 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_51.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_51.value = u'20'
    shipBuilder_vehicleitemavionics_51 = save_or_locate(shipBuilder_vehicleitemavionics_51)

    shipBuilder_vehicleitemavionics_52 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_52.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_52.value = u'0'
    shipBuilder_vehicleitemavionics_52 = save_or_locate(shipBuilder_vehicleitemavionics_52)

    shipBuilder_vehicleitemavionics_53 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_53.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_53.value = u'20'
    shipBuilder_vehicleitemavionics_53 = save_or_locate(shipBuilder_vehicleitemavionics_53)

    shipBuilder_vehicleitemavionics_54 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_54.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_54.value = u'0'
    shipBuilder_vehicleitemavionics_54 = save_or_locate(shipBuilder_vehicleitemavionics_54)

    shipBuilder_vehicleitemavionics_55 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_55.state = u'AutoControl'
    shipBuilder_vehicleitemavionics_55.value = u'20'
    shipBuilder_vehicleitemavionics_55 = save_or_locate(shipBuilder_vehicleitemavionics_55)

    shipBuilder_vehicleitemavionics_56 = VehicleItemAvionics()
    shipBuilder_vehicleitemavionics_56.state = u'ManualControl'
    shipBuilder_vehicleitemavionics_56.value = u'0'
    shipBuilder_vehicleitemavionics_56 = save_or_locate(shipBuilder_vehicleitemavionics_56)

    #Processing model: VehicleItem

    from shipBuilder.models import VehicleItem

    shipBuilder_vehicleitem_1 = VehicleItem()
    shipBuilder_vehicleitem_1.itemClass = 0
    shipBuilder_vehicleitem_1.description = u"By far ACOM's most popular model, the StarHeart III solves many of the problems of the StarLight models by increasing durability, decreasing signature, while maintaining the high power output."
    shipBuilder_vehicleitem_1.name = u'300i_ACOM_StarHeart_III'
    shipBuilder_vehicleitem_1.displayName = u'ACOM StarHeart III Engine'
    shipBuilder_vehicleitem_1.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_1.manufacturer = None
    shipBuilder_vehicleitem_1.itemSize = 2
    shipBuilder_vehicleitem_1.views = 0
    shipBuilder_vehicleitem_1.disabled = True
    shipBuilder_vehicleitem_1 = save_or_locate(shipBuilder_vehicleitem_1)

    shipBuilder_vehicleitem_2 = VehicleItem()
    shipBuilder_vehicleitem_2.itemClass = 0
    shipBuilder_vehicleitem_2.description = u'The Hammer Propulsion HE5.3 features a high output, fuel efficient design. Its thrust output and low fuel consumption make it ideal for long hauls though it has been reported to be somewhat of a missile magnet on occasions where owners have been subject to pirate activity.'
    shipBuilder_vehicleitem_2.name = u'300i_Hammer_Propulsion_HE_5_3'
    shipBuilder_vehicleitem_2.displayName = u'Hammer Propulsion HE 5.3'
    shipBuilder_vehicleitem_2.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_2.manufacturer = None
    shipBuilder_vehicleitem_2.itemSize = 4
    shipBuilder_vehicleitem_2.views = 0
    shipBuilder_vehicleitem_2.disabled = True
    shipBuilder_vehicleitem_2 = save_or_locate(shipBuilder_vehicleitem_2)

    shipBuilder_vehicleitem_3 = VehicleItem()
    shipBuilder_vehicleitem_3.itemClass = 0
    shipBuilder_vehicleitem_3.description = u'The Hammer Propulsion HE5.3 features a high output, fuel efficient design. Its thrust output and low fuel consumption make it ideal for long hauls though it has been reported to be somewhat of a missile magnet on occasions where owners have been subject to pirate activity.'
    shipBuilder_vehicleitem_3.name = u'325a_Hammer_Propulsion_HE_5_3'
    shipBuilder_vehicleitem_3.displayName = u'Hammer Propulsion HE 5.3'
    shipBuilder_vehicleitem_3.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_3.manufacturer = None
    shipBuilder_vehicleitem_3.itemSize = 4
    shipBuilder_vehicleitem_3.views = 0
    shipBuilder_vehicleitem_3.disabled = True
    shipBuilder_vehicleitem_3 = save_or_locate(shipBuilder_vehicleitem_3)

    shipBuilder_vehicleitem_4 = VehicleItem()
    shipBuilder_vehicleitem_4.itemClass = 0
    shipBuilder_vehicleitem_4.description = u'The Hammer Propulsion Twin HM4.3 is notable for the fact that it utilizes 2 high-performance TR3 thrusters in a small package. An unusual application, the original design was a joint collaboration between Hammer Propulsion and the Origin Jumpworks racing team. With the additional thrust provided by a second thruster the Twin HM4.3 is ideal for applications where speed is the goal. Speed comes at a cost, however; this configuration has a thirst for fuel that rivals much larger single thruster systems, and with all of its available space being taken up by the thruster internals not much space is left for durability reinforcement. This makes the HM4.3 ideal for most racing pilots, but less suitable for combat-oriented missions.'
    shipBuilder_vehicleitem_4.name = u'350r_Hammer_Propulsion_HE_4_3'
    shipBuilder_vehicleitem_4.displayName = u'Hammer Propulsion HM 4.3'
    shipBuilder_vehicleitem_4.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_4.manufacturer = None
    shipBuilder_vehicleitem_4.itemSize = 4
    shipBuilder_vehicleitem_4.views = 0
    shipBuilder_vehicleitem_4.disabled = True
    shipBuilder_vehicleitem_4 = save_or_locate(shipBuilder_vehicleitem_4)

    shipBuilder_vehicleitem_5 = VehicleItem()
    shipBuilder_vehicleitem_5.itemClass = 0
    shipBuilder_vehicleitem_5.description = u"Designed in conjunction with the engineers at RSI, the A&R LR-5 Max OverDrive features the same great engine you've come to expect from A&R, but with higher quality parts built with the care and dedication that you've come to expect from the company that's been taking humanity to the stars since 2075."
    shipBuilder_vehicleitem_5.name = u'A&R_LR-5_MAX_OverDrive'
    shipBuilder_vehicleitem_5.displayName = u'A&R LR-5 MAX OverDrive'
    shipBuilder_vehicleitem_5.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_5.manufacturer = None
    shipBuilder_vehicleitem_5.itemSize = 4
    shipBuilder_vehicleitem_5.views = 0
    shipBuilder_vehicleitem_5.disabled = True
    shipBuilder_vehicleitem_5 = save_or_locate(shipBuilder_vehicleitem_5)

    shipBuilder_vehicleitem_6 = VehicleItem()
    shipBuilder_vehicleitem_6.itemClass = 0
    shipBuilder_vehicleitem_6.description = u"A&R's LR-5 OverDrive is your gateway to the world of fusion-based power plants. Designed to be a rugged, high-output alternative to other power sources, the LR-5 OverDrive does suffer from an above average generation of heat."
    shipBuilder_vehicleitem_6.name = u'A&R_LR-5_OverDrive'
    shipBuilder_vehicleitem_6.displayName = u'A&R LR-5 OverDrive'
    shipBuilder_vehicleitem_6.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_6.manufacturer = None
    shipBuilder_vehicleitem_6.itemSize = 4
    shipBuilder_vehicleitem_6.views = 0
    shipBuilder_vehicleitem_6.disabled = True
    shipBuilder_vehicleitem_6 = save_or_locate(shipBuilder_vehicleitem_6)

    shipBuilder_vehicleitem_7 = VehicleItem()
    shipBuilder_vehicleitem_7.itemClass = 0
    shipBuilder_vehicleitem_7.description = u"The LR-7 ULTRA OverDrive is the patriarch of the LR series. Capable of handling any number of hauling or commercial needs, the LR-7 features a reinforced plasma-core to combat the increased heat signature. Odds are, if you need a monster of a power plant like this, your ship isn't hiding."
    shipBuilder_vehicleitem_7.name = u'A&R_LR-7_ULTRA_OverDrive'
    shipBuilder_vehicleitem_7.displayName = u'A&R LR-7 ULTRA OverDrive'
    shipBuilder_vehicleitem_7.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_7.manufacturer = None
    shipBuilder_vehicleitem_7.itemSize = 4
    shipBuilder_vehicleitem_7.views = 0
    shipBuilder_vehicleitem_7.disabled = True
    shipBuilder_vehicleitem_7 = save_or_locate(shipBuilder_vehicleitem_7)

    shipBuilder_vehicleitem_8 = VehicleItem()
    shipBuilder_vehicleitem_8.itemClass = 0
    shipBuilder_vehicleitem_8.description = None
    shipBuilder_vehicleitem_8.name = u'AATurret'
    shipBuilder_vehicleitem_8.displayName = u'Aaturret'
    shipBuilder_vehicleitem_8.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_8.manufacturer = None
    shipBuilder_vehicleitem_8.itemSize = 2
    shipBuilder_vehicleitem_8.views = 0
    shipBuilder_vehicleitem_8.disabled = True
    shipBuilder_vehicleitem_8 = save_or_locate(shipBuilder_vehicleitem_8)

    shipBuilder_vehicleitem_9 = VehicleItem()
    shipBuilder_vehicleitem_9.itemClass = 0
    shipBuilder_vehicleitem_9.description = u'The FusionPro 3H III is optimized for medium sized spacecraft. The 3H boasts the expected high durability and performance under fire while maintaining a robust energy output. The signature can run awfully hot.'
    shipBuilder_vehicleitem_9.name = u'Ace_Astrogation_FusionPro_3H_III'
    shipBuilder_vehicleitem_9.displayName = u'Ace Astrogation FusionPro 3H III'
    shipBuilder_vehicleitem_9.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_9.manufacturer = None
    shipBuilder_vehicleitem_9.itemSize = 4
    shipBuilder_vehicleitem_9.views = 0
    shipBuilder_vehicleitem_9.disabled = True
    shipBuilder_vehicleitem_9 = save_or_locate(shipBuilder_vehicleitem_9)

    shipBuilder_vehicleitem_10 = VehicleItem()
    shipBuilder_vehicleitem_10.itemClass = 0
    shipBuilder_vehicleitem_10.description = u"By far ACOM's most popular model, the StarHeart III solves many of the problems of the StarLight models by increasing durability and decreasing signature while maintaining the high power output."
    shipBuilder_vehicleitem_10.name = u'ACOM_StarHeart_III'
    shipBuilder_vehicleitem_10.displayName = u'ACOM StarHeart III Power Plant'
    shipBuilder_vehicleitem_10.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_10.manufacturer = None
    shipBuilder_vehicleitem_10.itemSize = 2
    shipBuilder_vehicleitem_10.views = 0
    shipBuilder_vehicleitem_10.disabled = True
    shipBuilder_vehicleitem_10 = save_or_locate(shipBuilder_vehicleitem_10)

    shipBuilder_vehicleitem_11 = VehicleItem()
    shipBuilder_vehicleitem_11.itemClass = 0
    shipBuilder_vehicleitem_11.description = u"The StarLight II is the baseline model of ACOM's award winning Star Series of anti-tritium power planets. While this model offers a robust output, the durability and signature of the power source suffer from the smaller size."
    shipBuilder_vehicleitem_11.name = u'ACOM_StarLight_II'
    shipBuilder_vehicleitem_11.displayName = u'ACOM StarLight II Engine'
    shipBuilder_vehicleitem_11.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_11.manufacturer = None
    shipBuilder_vehicleitem_11.itemSize = 4
    shipBuilder_vehicleitem_11.views = 0
    shipBuilder_vehicleitem_11.disabled = True
    shipBuilder_vehicleitem_11 = save_or_locate(shipBuilder_vehicleitem_11)

    shipBuilder_vehicleitem_12 = VehicleItem()
    shipBuilder_vehicleitem_12.itemClass = 0
    shipBuilder_vehicleitem_12.description = None
    shipBuilder_vehicleitem_12.name = u'Aegis_Dynamics_M-5c_PowerPlant'
    shipBuilder_vehicleitem_12.displayName = u'Aegis Dynamics M-5c Thorium Engine'
    shipBuilder_vehicleitem_12.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_12.manufacturer = None
    shipBuilder_vehicleitem_12.itemSize = 4
    shipBuilder_vehicleitem_12.views = 0
    shipBuilder_vehicleitem_12.disabled = True
    shipBuilder_vehicleitem_12 = save_or_locate(shipBuilder_vehicleitem_12)

    shipBuilder_vehicleitem_13 = VehicleItem()
    shipBuilder_vehicleitem_13.itemClass = 0
    shipBuilder_vehicleitem_13.description = None
    shipBuilder_vehicleitem_13.name = u'Aegis_TR4_Vector_Thruster'
    shipBuilder_vehicleitem_13.displayName = u'Aegis TR4 Vector Thruster'
    shipBuilder_vehicleitem_13.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_13.manufacturer = None
    shipBuilder_vehicleitem_13.itemSize = 4
    shipBuilder_vehicleitem_13.views = 0
    shipBuilder_vehicleitem_13.disabled = True
    shipBuilder_vehicleitem_13 = save_or_locate(shipBuilder_vehicleitem_13)

    shipBuilder_vehicleitem_14 = VehicleItem()
    shipBuilder_vehicleitem_14.itemClass = 0
    shipBuilder_vehicleitem_14.description = u"The K3S-9 introduces the tried-and-true KS line of power plants to commercial-class ships, offering the same reliability and dependability for those long hauls through the black. The K3S-9's Chromodyanmic Assembler system will keep your systems online through thick and thin."
    shipBuilder_vehicleitem_14.name = u'Alliance_Startech_K3S-9'
    shipBuilder_vehicleitem_14.displayName = u'Alliance Startech K3S-9'
    shipBuilder_vehicleitem_14.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_14.manufacturer = None
    shipBuilder_vehicleitem_14.itemSize = 4
    shipBuilder_vehicleitem_14.views = 0
    shipBuilder_vehicleitem_14.disabled = True
    shipBuilder_vehicleitem_14 = save_or_locate(shipBuilder_vehicleitem_14)

    shipBuilder_vehicleitem_15 = VehicleItem()
    shipBuilder_vehicleitem_15.itemClass = 0
    shipBuilder_vehicleitem_15.description = u'The Alliance Startech KS-9 Chromodynamic Assembler system is a durable, low-signature power plant most commonly used in Aurora class starships. The decreased signature and increased reliability come at the cost of relatively weak power production, something that pilots will want to consider if they intend on mounting weapons systems with large power requirements.'
    shipBuilder_vehicleitem_15.name = u'Alliance_Startech_KS-9'
    shipBuilder_vehicleitem_15.displayName = u'Alliance_Startech_KS-9'
    shipBuilder_vehicleitem_15.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_15.manufacturer = None
    shipBuilder_vehicleitem_15.itemSize = 1
    shipBuilder_vehicleitem_15.views = 0
    shipBuilder_vehicleitem_15.disabled = True
    shipBuilder_vehicleitem_15 = save_or_locate(shipBuilder_vehicleitem_15)

    shipBuilder_vehicleitem_16 = VehicleItem()
    shipBuilder_vehicleitem_16.itemClass = 0
    shipBuilder_vehicleitem_16.description = u"The KS-9 Enhanced features the same dependable construction of the KS-9 but with a series of higher quality parts compliments of the Alliance Startech's Commercial Development Division in Terra."
    shipBuilder_vehicleitem_16.name = u'Alliance_Startech_KS-9_Enhanced'
    shipBuilder_vehicleitem_16.displayName = u'Alliance Startech KS-9 Enhanced'
    shipBuilder_vehicleitem_16.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_16.manufacturer = None
    shipBuilder_vehicleitem_16.itemSize = 4
    shipBuilder_vehicleitem_16.views = 0
    shipBuilder_vehicleitem_16.disabled = True
    shipBuilder_vehicleitem_16 = save_or_locate(shipBuilder_vehicleitem_16)

    shipBuilder_vehicleitem_17 = VehicleItem()
    shipBuilder_vehicleitem_17.itemClass = 0
    shipBuilder_vehicleitem_17.description = None
    shipBuilder_vehicleitem_17.name = u'Anvil_Flex_MK2'
    shipBuilder_vehicleitem_17.displayName = u'Anvil MK2 Flex Thruster'
    shipBuilder_vehicleitem_17.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_17.manufacturer = None
    shipBuilder_vehicleitem_17.itemSize = 2
    shipBuilder_vehicleitem_17.views = 0
    shipBuilder_vehicleitem_17.disabled = True
    shipBuilder_vehicleitem_17 = save_or_locate(shipBuilder_vehicleitem_17)

    shipBuilder_vehicleitem_18 = VehicleItem()
    shipBuilder_vehicleitem_18.itemClass = 0
    shipBuilder_vehicleitem_18.description = None
    shipBuilder_vehicleitem_18.name = u'Anvil_Flex_Thruster_TR2_Back_Left'
    shipBuilder_vehicleitem_18.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_18.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_18.manufacturer = None
    shipBuilder_vehicleitem_18.itemSize = 2
    shipBuilder_vehicleitem_18.views = 0
    shipBuilder_vehicleitem_18.disabled = True
    shipBuilder_vehicleitem_18 = save_or_locate(shipBuilder_vehicleitem_18)

    shipBuilder_vehicleitem_19 = VehicleItem()
    shipBuilder_vehicleitem_19.itemClass = 0
    shipBuilder_vehicleitem_19.description = None
    shipBuilder_vehicleitem_19.name = u'Anvil_Flex_Thruster_TR2_Back_Right'
    shipBuilder_vehicleitem_19.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_19.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_19.manufacturer = None
    shipBuilder_vehicleitem_19.itemSize = 2
    shipBuilder_vehicleitem_19.views = 0
    shipBuilder_vehicleitem_19.disabled = True
    shipBuilder_vehicleitem_19 = save_or_locate(shipBuilder_vehicleitem_19)

    shipBuilder_vehicleitem_20 = VehicleItem()
    shipBuilder_vehicleitem_20.itemClass = 0
    shipBuilder_vehicleitem_20.description = None
    shipBuilder_vehicleitem_20.name = u'Anvil_Flex_Thruster_TR2_Front_Left'
    shipBuilder_vehicleitem_20.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_20.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_20.manufacturer = None
    shipBuilder_vehicleitem_20.itemSize = 2
    shipBuilder_vehicleitem_20.views = 0
    shipBuilder_vehicleitem_20.disabled = True
    shipBuilder_vehicleitem_20 = save_or_locate(shipBuilder_vehicleitem_20)

    shipBuilder_vehicleitem_21 = VehicleItem()
    shipBuilder_vehicleitem_21.itemClass = 0
    shipBuilder_vehicleitem_21.description = None
    shipBuilder_vehicleitem_21.name = u'Anvil_Flex_Thruster_TR2_Front_Right'
    shipBuilder_vehicleitem_21.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_21.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_21.manufacturer = None
    shipBuilder_vehicleitem_21.itemSize = 2
    shipBuilder_vehicleitem_21.views = 0
    shipBuilder_vehicleitem_21.disabled = True
    shipBuilder_vehicleitem_21 = save_or_locate(shipBuilder_vehicleitem_21)

    shipBuilder_vehicleitem_22 = VehicleItem()
    shipBuilder_vehicleitem_22.itemClass = 0
    shipBuilder_vehicleitem_22.description = None
    shipBuilder_vehicleitem_22.name = u'Anvil_Joint_MK2'
    shipBuilder_vehicleitem_22.displayName = u'Anvil MK2 Jointed Thruster'
    shipBuilder_vehicleitem_22.itemType = shipBuilder_vehicleitemtype_13
    shipBuilder_vehicleitem_22.manufacturer = None
    shipBuilder_vehicleitem_22.itemSize = 2
    shipBuilder_vehicleitem_22.views = 0
    shipBuilder_vehicleitem_22.disabled = True
    shipBuilder_vehicleitem_22 = save_or_locate(shipBuilder_vehicleitem_22)

    shipBuilder_vehicleitem_23 = VehicleItem()
    shipBuilder_vehicleitem_23.itemClass = 0
    shipBuilder_vehicleitem_23.description = None
    shipBuilder_vehicleitem_23.name = u'Anvil_Joint_Thruster_TR2'
    shipBuilder_vehicleitem_23.displayName = u'Anvil TR2 Jointed Thruster'
    shipBuilder_vehicleitem_23.itemType = shipBuilder_vehicleitemtype_13
    shipBuilder_vehicleitem_23.manufacturer = None
    shipBuilder_vehicleitem_23.itemSize = 2
    shipBuilder_vehicleitem_23.views = 0
    shipBuilder_vehicleitem_23.disabled = True
    shipBuilder_vehicleitem_23 = save_or_locate(shipBuilder_vehicleitem_23)

    shipBuilder_vehicleitem_24 = VehicleItem()
    shipBuilder_vehicleitem_24.itemClass = 0
    shipBuilder_vehicleitem_24.description = u"ArcCorp's Arc Duo 400 was recently named one of Whitley's Ten Best Commercial Grade Thrusters. Designed to handle the payload requirements of larger class vessels, the Arc Duo 400 continues ArcCorp's design philosophy of lower signature and better efficiency."
    shipBuilder_vehicleitem_24.name = u'Arc_Duo_400'
    shipBuilder_vehicleitem_24.displayName = u'ArcLight 300'
    shipBuilder_vehicleitem_24.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_24.manufacturer = None
    shipBuilder_vehicleitem_24.itemSize = 3
    shipBuilder_vehicleitem_24.views = 0
    shipBuilder_vehicleitem_24.disabled = True
    shipBuilder_vehicleitem_24 = save_or_locate(shipBuilder_vehicleitem_24)

    shipBuilder_vehicleitem_25 = VehicleItem()
    shipBuilder_vehicleitem_25.itemClass = 1
    shipBuilder_vehicleitem_25.description = u"The M3A is Behring's entry level laser cannon. The cannon configuration offers modest damage per projectile and a fairly low rate of fire. As the most basic offering in Behring's weapons lineup, it features low power consumption, but poor power efficiency. It makes up ground for its shortcomings by being cheap, a feature many pilots are looking for when outfitting their ships on a budget."
    shipBuilder_vehicleitem_25.name = u'Behring_M3A_Laser'
    shipBuilder_vehicleitem_25.displayName = u'Behring M3A Laser'
    shipBuilder_vehicleitem_25.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_25.manufacturer = None
    shipBuilder_vehicleitem_25.itemSize = 1
    shipBuilder_vehicleitem_25.views = 0
    shipBuilder_vehicleitem_25.disabled = True
    shipBuilder_vehicleitem_25 = save_or_locate(shipBuilder_vehicleitem_25)

    shipBuilder_vehicleitem_26 = VehicleItem()
    shipBuilder_vehicleitem_26.itemClass = 0
    shipBuilder_vehicleitem_26.description = u"The M4A is Behring's second tier laser cannon. Its bigger size means more power consumption in exchange for packing a bigger punch. Fire rate and power efficiency are comparable to the M3A model."
    shipBuilder_vehicleitem_26.name = u'Behring_M4A_Laser'
    shipBuilder_vehicleitem_26.displayName = u'Behring M4A Laser'
    shipBuilder_vehicleitem_26.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_26.manufacturer = None
    shipBuilder_vehicleitem_26.itemSize = 2
    shipBuilder_vehicleitem_26.views = 1
    shipBuilder_vehicleitem_26.disabled = True
    shipBuilder_vehicleitem_26 = save_or_locate(shipBuilder_vehicleitem_26)

    shipBuilder_vehicleitem_27 = VehicleItem()
    shipBuilder_vehicleitem_27.itemClass = 1
    shipBuilder_vehicleitem_27.description = u"The M4A is Behring's second tier laser cannon. Its bigger size means more power consumption in exchange for packing a bigger punch. Fire rate and power efficiency are comparable to the M3A model."
    shipBuilder_vehicleitem_27.name = u'Behring_M4A_lasser_Cannon'
    shipBuilder_vehicleitem_27.displayName = u'M4A Lasser Cannon'
    shipBuilder_vehicleitem_27.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_27.manufacturer = None
    shipBuilder_vehicleitem_27.itemSize = 2
    shipBuilder_vehicleitem_27.views = 0
    shipBuilder_vehicleitem_27.disabled = True
    shipBuilder_vehicleitem_27 = save_or_locate(shipBuilder_vehicleitem_27)

    shipBuilder_vehicleitem_28 = VehicleItem()
    shipBuilder_vehicleitem_28.itemClass = 1
    shipBuilder_vehicleitem_28.description = u"Behring's M5A laser cannon bridges the gap between small ship and large ship weapons. Suitable for most ship models, the M5A offers respectable offensive capability in any situation. Fire rate and power efficiency are comparable to the M-series lasers."
    shipBuilder_vehicleitem_28.name = u'Behring_M5A_Laser'
    shipBuilder_vehicleitem_28.displayName = u'Behring M5A Laser'
    shipBuilder_vehicleitem_28.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_28.manufacturer = None
    shipBuilder_vehicleitem_28.itemSize = 1
    shipBuilder_vehicleitem_28.views = 0
    shipBuilder_vehicleitem_28.disabled = True
    shipBuilder_vehicleitem_28 = save_or_locate(shipBuilder_vehicleitem_28)

    shipBuilder_vehicleitem_29 = VehicleItem()
    shipBuilder_vehicleitem_29.itemClass = 3
    shipBuilder_vehicleitem_29.description = u"The Behring Marksman heat seeking missile utilizes an enemy's heat signature to obtain and maintain a lock on the target. This tried-and-true method of target acquisition has a few drawbacks: it is easily confused by flares and it may be difficult to establish lock on ships with low heat signatures. These issues aside, the Marksman is the go-to missile of choice for many independent operators and pilots. Rack of four (4)."
    shipBuilder_vehicleitem_29.name = u'Behring_Marksman_HS_Platform_x4'
    shipBuilder_vehicleitem_29.displayName = u'Behring Marksman HS Quad Platform'
    shipBuilder_vehicleitem_29.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_29.manufacturer = None
    shipBuilder_vehicleitem_29.itemSize = 2
    shipBuilder_vehicleitem_29.views = 0
    shipBuilder_vehicleitem_29.disabled = True
    shipBuilder_vehicleitem_29 = save_or_locate(shipBuilder_vehicleitem_29)

    shipBuilder_vehicleitem_30 = VehicleItem()
    shipBuilder_vehicleitem_30.itemClass = 3
    shipBuilder_vehicleitem_30.description = u"The Behring Marksman heat seeking missile utilizes an enemy's heat signature to obtain and maintain a lock on the target. This tried-and-true method of target acquisition has a few drawbacks: it is easily confused by flares and it may be difficult to establish lock on ships with low heat signatures. These issues aside, the Marksman is the go-to missile of choice for many independent operators and pilots. Rack of four (4)."
    shipBuilder_vehicleitem_30.name = u'Behring_Marksman_Quad'
    shipBuilder_vehicleitem_30.displayName = u'Behring Marksman HS Quad Platform'
    shipBuilder_vehicleitem_30.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_30.manufacturer = None
    shipBuilder_vehicleitem_30.itemSize = 2
    shipBuilder_vehicleitem_30.views = 0
    shipBuilder_vehicleitem_30.disabled = True
    shipBuilder_vehicleitem_30 = save_or_locate(shipBuilder_vehicleitem_30)

    shipBuilder_vehicleitem_31 = VehicleItem()
    shipBuilder_vehicleitem_31.itemClass = 1
    shipBuilder_vehicleitem_31.description = u'The Mk VI is a trusted and dependable high-power laser weapon system for pilots who desire additional precision and power efficiency. The Mk VI is ideal for larger ships and can even be deployed in capital ship turrets.'
    shipBuilder_vehicleitem_31.name = u'Behring_Mk_VI_Laser'
    shipBuilder_vehicleitem_31.displayName = u'Behring Mk VI Laser'
    shipBuilder_vehicleitem_31.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_31.manufacturer = None
    shipBuilder_vehicleitem_31.itemSize = 3
    shipBuilder_vehicleitem_31.views = 0
    shipBuilder_vehicleitem_31.disabled = True
    shipBuilder_vehicleitem_31 = save_or_locate(shipBuilder_vehicleitem_31)

    shipBuilder_vehicleitem_32 = VehicleItem()
    shipBuilder_vehicleitem_32.itemClass = 0
    shipBuilder_vehicleitem_32.description = u'The STC Blue by perrenial thruster manufacturer Dragon Stellar Transit Company offers high output and low emissions, great for pilots wishing to close the distance while maintaining a low profile. The smallest thruster in the STC lineup, the Blue has a thrust rating of 2.'
    shipBuilder_vehicleitem_32.name = u'Dragon_STC_Blue'
    shipBuilder_vehicleitem_32.displayName = u'Dragon STC Blue Main Engine'
    shipBuilder_vehicleitem_32.itemType = shipBuilder_vehicleitemtype_14
    shipBuilder_vehicleitem_32.manufacturer = None
    shipBuilder_vehicleitem_32.itemSize = 2
    shipBuilder_vehicleitem_32.views = 0
    shipBuilder_vehicleitem_32.disabled = True
    shipBuilder_vehicleitem_32 = save_or_locate(shipBuilder_vehicleitem_32)

    shipBuilder_vehicleitem_33 = VehicleItem()
    shipBuilder_vehicleitem_33.itemClass = 0
    shipBuilder_vehicleitem_33.description = u"The Dragon Stellar STC Red is a great choice for pilots of small ships. Despite its lack of fuel and power efficiency it boasts a respectable thrust output that really shines on low mass ships such as the Aurora. As an added benefit, Dragon Stellear recently developed new technology that reduces the output signature, great for pilots who don't wish to call a lot of attention to themselves. Its thrust rating of 3 gives it more thrust than the Blue, at the cost of higher power consumption and signature."
    shipBuilder_vehicleitem_33.name = u'Dragon_STC_Red'
    shipBuilder_vehicleitem_33.displayName = u'Dragon STC Red Main Engine'
    shipBuilder_vehicleitem_33.itemType = shipBuilder_vehicleitemtype_14
    shipBuilder_vehicleitem_33.manufacturer = None
    shipBuilder_vehicleitem_33.itemSize = 3
    shipBuilder_vehicleitem_33.views = 0
    shipBuilder_vehicleitem_33.disabled = True
    shipBuilder_vehicleitem_33 = save_or_locate(shipBuilder_vehicleitem_33)

    shipBuilder_vehicleitem_34 = VehicleItem()
    shipBuilder_vehicleitem_34.itemClass = 0
    shipBuilder_vehicleitem_34.description = u'The STC Silver from Dragon Stellar Transit Company is a TR4 engine noted for its high thrust ouput and low EM emissions. It has been rumored that Dragon Stellar has been using inferior components, but for some pilots the decreased power and fuel efficiency is worth the extra boost, especially at this price point.'
    shipBuilder_vehicleitem_34.name = u'Dragon_STC_Silver'
    shipBuilder_vehicleitem_34.displayName = u'Dragon STC Silver Main Engine'
    shipBuilder_vehicleitem_34.itemType = shipBuilder_vehicleitemtype_14
    shipBuilder_vehicleitem_34.manufacturer = None
    shipBuilder_vehicleitem_34.itemSize = 4
    shipBuilder_vehicleitem_34.views = 0
    shipBuilder_vehicleitem_34.disabled = True
    shipBuilder_vehicleitem_34 = save_or_locate(shipBuilder_vehicleitem_34)

    shipBuilder_vehicleitem_35 = VehicleItem()
    shipBuilder_vehicleitem_35.itemClass = 0
    shipBuilder_vehicleitem_35.description = u'Greycat\u2019s latest addition to their field-tested tractor beam line is a dependable addition to their catalog. Aside from a more efficient pull/draw ratio, the latest model does little to advance from the previous models. The Sure Grip has settings to target and extract everything from asteroid fragments to drifting crewmen, backed by Greycat\u2019s certified Soft-Touch\xae guarantee.'
    shipBuilder_vehicleitem_35.name = u'Greycat_Industrial_Sure_Grip_Tractor'
    shipBuilder_vehicleitem_35.displayName = u'Sure Grip Tractor'
    shipBuilder_vehicleitem_35.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_35.manufacturer = None
    shipBuilder_vehicleitem_35.itemSize = 1
    shipBuilder_vehicleitem_35.views = 0
    shipBuilder_vehicleitem_35.disabled = True
    shipBuilder_vehicleitem_35 = save_or_locate(shipBuilder_vehicleitem_35)

    shipBuilder_vehicleitem_36 = VehicleItem()
    shipBuilder_vehicleitem_36.itemClass = 0
    shipBuilder_vehicleitem_36.description = u"The inaugural model of GNP's new Etoile series, the Etoile-00 utilizes a liquid fluoride thorium reactor technology to create a highly damage-resistant power alternative to medium class ships."
    shipBuilder_vehicleitem_36.name = u'Groupe_Nouveau_Paradigme_Etoile-00'
    shipBuilder_vehicleitem_36.displayName = u'Groupe Nouveau Paradigme Etoile-00'
    shipBuilder_vehicleitem_36.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_36.manufacturer = None
    shipBuilder_vehicleitem_36.itemSize = 4
    shipBuilder_vehicleitem_36.views = 0
    shipBuilder_vehicleitem_36.disabled = True
    shipBuilder_vehicleitem_36 = save_or_locate(shipBuilder_vehicleitem_36)

    shipBuilder_vehicleitem_37 = VehicleItem()
    shipBuilder_vehicleitem_37.itemClass = 0
    shipBuilder_vehicleitem_37.description = u"Hammer Propulsion's HE 5.5 offers the same high quality, high output design that you find in the 5.3 but amplified to handle larger class vessels. the 5.5 is one of the most durable and robust thrusters on the market for commercial and shipping vehicles."
    shipBuilder_vehicleitem_37.name = u'Hammer_Propulsion_HE_5_5'
    shipBuilder_vehicleitem_37.displayName = u'Hammer Propulsion HE 5.5'
    shipBuilder_vehicleitem_37.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_37.manufacturer = None
    shipBuilder_vehicleitem_37.itemSize = 4
    shipBuilder_vehicleitem_37.views = 0
    shipBuilder_vehicleitem_37.disabled = True
    shipBuilder_vehicleitem_37 = save_or_locate(shipBuilder_vehicleitem_37)

    shipBuilder_vehicleitem_38 = VehicleItem()
    shipBuilder_vehicleitem_38.itemClass = 0
    shipBuilder_vehicleitem_38.description = u"The luxury version of the HM4.3, Hammer Propulsion's HMX4.3 engine system features customized racing parts from some of the league's top engineers to help weather corrosion and general part decay."
    shipBuilder_vehicleitem_38.name = u'Hammer_Propulsion_HM_4.4'
    shipBuilder_vehicleitem_38.displayName = u'Hammer Propulsion HMX 4.3'
    shipBuilder_vehicleitem_38.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_38.manufacturer = None
    shipBuilder_vehicleitem_38.itemSize = 4
    shipBuilder_vehicleitem_38.views = 0
    shipBuilder_vehicleitem_38.disabled = True
    shipBuilder_vehicleitem_38 = save_or_locate(shipBuilder_vehicleitem_38)

    shipBuilder_vehicleitem_39 = VehicleItem()
    shipBuilder_vehicleitem_39.itemClass = 0
    shipBuilder_vehicleitem_39.description = u"If speed is what you're after, the HM4.3 engine can give it to you. Built under supervision of the Racing Division at Hammer Propulsion, the 4.3 is a single-thruster system iteration of the award-winning Twin HM4.3 propulsion units made famous by the Origin 350r racers. The 4.3 has been specifically crafted down to the smallest pinion to give you the most boost possible in a single engine system."
    shipBuilder_vehicleitem_39.name = u'Hammer_Propulsion_HM_4_3'
    shipBuilder_vehicleitem_39.displayName = u'Hammer Propulsion HM 4.3'
    shipBuilder_vehicleitem_39.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_39.manufacturer = None
    shipBuilder_vehicleitem_39.itemSize = 4
    shipBuilder_vehicleitem_39.views = 0
    shipBuilder_vehicleitem_39.disabled = True
    shipBuilder_vehicleitem_39 = save_or_locate(shipBuilder_vehicleitem_39)

    shipBuilder_vehicleitem_40 = VehicleItem()
    shipBuilder_vehicleitem_40.itemClass = 0
    shipBuilder_vehicleitem_40.description = u"A heavier model than the Stinger. Sure, the VOLT Hellfire pulls more juice from your power plant and the rate of fire isn't as high, but that extra draw means a little more punch."
    shipBuilder_vehicleitem_40.name = u'Hellfire'
    shipBuilder_vehicleitem_40.displayName = u'Hellfire'
    shipBuilder_vehicleitem_40.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_40.manufacturer = None
    shipBuilder_vehicleitem_40.itemSize = 1
    shipBuilder_vehicleitem_40.views = 0
    shipBuilder_vehicleitem_40.disabled = True
    shipBuilder_vehicleitem_40 = save_or_locate(shipBuilder_vehicleitem_40)

    shipBuilder_vehicleitem_41 = VehicleItem()
    shipBuilder_vehicleitem_41.itemClass = 0
    shipBuilder_vehicleitem_41.description = u'The Endurance-300 from Juno Starwerk utilizes a VHTR (very high temperature reactor) and is a solid choice for Aurora pilots operating in tough environments. Although based on somewhat antiquated fission technology resulting in slightly lower power output and increased signature, the extra insulation required in its construction has the added benefit of making the Endurance-300 a very damage-resilient power source.'
    shipBuilder_vehicleitem_41.name = u'Juno_Starwerk_Endurance-300'
    shipBuilder_vehicleitem_41.displayName = u'Juno Starwerk Endurance-300'
    shipBuilder_vehicleitem_41.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_41.manufacturer = None
    shipBuilder_vehicleitem_41.itemSize = 1
    shipBuilder_vehicleitem_41.views = 0
    shipBuilder_vehicleitem_41.disabled = True
    shipBuilder_vehicleitem_41 = save_or_locate(shipBuilder_vehicleitem_41)

    shipBuilder_vehicleitem_42 = VehicleItem()
    shipBuilder_vehicleitem_42.itemClass = 1
    shipBuilder_vehicleitem_42.description = u'Featuring a three-barrel sequential fire design, the Klaus & Werner CF-007 Bulldog repeater is capable of high rates of fire while maintaining accuracy. It has low damage per projectile and, although it has relatively low power consumption over-all, several publications have commented on its somewhat lackluster efficiency. Even so, the CF-007 remains a favorite among new pilots who are outfitting their first ship.'
    shipBuilder_vehicleitem_42.name = u'K_and_W_CF-007_Bulldog_Repeater'
    shipBuilder_vehicleitem_42.displayName = u'CF-007 Bulldog Repeater'
    shipBuilder_vehicleitem_42.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_42.manufacturer = None
    shipBuilder_vehicleitem_42.itemSize = 1
    shipBuilder_vehicleitem_42.views = 0
    shipBuilder_vehicleitem_42.disabled = True
    shipBuilder_vehicleitem_42 = save_or_locate(shipBuilder_vehicleitem_42)

    shipBuilder_vehicleitem_43 = VehicleItem()
    shipBuilder_vehicleitem_43.itemClass = 1
    shipBuilder_vehicleitem_43.description = u"Badger repeater is Klaus & Werner's dependable second-tier repeating laser. Its increased output (and corresponding power consumption) make it a solid contender in any fight. Power efficiency continues to be a problem with the K&W models, however."
    shipBuilder_vehicleitem_43.name = u'K_and_W_CF-117_Badger_Repeater'
    shipBuilder_vehicleitem_43.displayName = u'CF-117 Badger Repeater'
    shipBuilder_vehicleitem_43.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_43.manufacturer = None
    shipBuilder_vehicleitem_43.itemSize = 2
    shipBuilder_vehicleitem_43.views = 0
    shipBuilder_vehicleitem_43.disabled = True
    shipBuilder_vehicleitem_43 = save_or_locate(shipBuilder_vehicleitem_43)

    shipBuilder_vehicleitem_44 = VehicleItem()
    shipBuilder_vehicleitem_44.itemClass = 1
    shipBuilder_vehicleitem_44.description = u"The CF-227 Panther is a grinder. The mid-range model of Klaus and Werner's repeaters, the Panther is the definition of a fire-and-forget weapon. Its impressive rate of fire and respectable power consumption make the Panther an effective combat solution for all ship sizes."
    shipBuilder_vehicleitem_44.name = u'K_and_W_CF-227_Panther_Repeater'
    shipBuilder_vehicleitem_44.displayName = u'CF-227 Panther Repeater'
    shipBuilder_vehicleitem_44.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_44.manufacturer = None
    shipBuilder_vehicleitem_44.itemSize = 3
    shipBuilder_vehicleitem_44.views = 0
    shipBuilder_vehicleitem_44.disabled = True
    shipBuilder_vehicleitem_44 = save_or_locate(shipBuilder_vehicleitem_44)

    shipBuilder_vehicleitem_45 = VehicleItem()
    shipBuilder_vehicleitem_45.itemClass = 1
    shipBuilder_vehicleitem_45.description = u"The K&W Mass Driver Cannon is a 35mm hard-ammo ballistic weapon capable of firing multiple types of ammunition. This weapon's increased shield penetration capabilities comes at a cost, however; magazine space is limited, and ammunition must be replenished regularly. Because it does not use energy-based projectiles, the K&W mass driver has a reduced power cost and therefore results in a reduced EM signature."
    shipBuilder_vehicleitem_45.name = u'K_and_W_Mass_Driver_Cannon'
    shipBuilder_vehicleitem_45.displayName = u'K and W Mass Driver Cannon'
    shipBuilder_vehicleitem_45.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_45.manufacturer = None
    shipBuilder_vehicleitem_45.itemSize = 2
    shipBuilder_vehicleitem_45.views = 0
    shipBuilder_vehicleitem_45.disabled = True
    shipBuilder_vehicleitem_45 = save_or_locate(shipBuilder_vehicleitem_45)

    shipBuilder_vehicleitem_46 = VehicleItem()
    shipBuilder_vehicleitem_46.itemClass = 0
    shipBuilder_vehicleitem_46.description = u'Featuring a three-barrel sequential fire design, the Klaus & Werner CF-007 Bulldog repeater is capable of high rates of fire while maintaining accuracy. It has low damage per projectile and, although it has relatively low power consumption over-all, several publications have commented on its somewhat lackluster efficiency. Even so, the CF-007 remains a favorite among new pilots who are outfitting their first ship.'
    shipBuilder_vehicleitem_46.name = u'K_W_CF_007_Bulldog_Laser_Repeater_Turret'
    shipBuilder_vehicleitem_46.displayName = u'007 Bulldog Laser Repeater Turret'
    shipBuilder_vehicleitem_46.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_46.manufacturer = None
    shipBuilder_vehicleitem_46.itemSize = 2
    shipBuilder_vehicleitem_46.views = 0
    shipBuilder_vehicleitem_46.disabled = True
    shipBuilder_vehicleitem_46 = save_or_locate(shipBuilder_vehicleitem_46)

    shipBuilder_vehicleitem_47 = VehicleItem()
    shipBuilder_vehicleitem_47.itemClass = 0
    shipBuilder_vehicleitem_47.description = u'MaxOx\u2019s NN-13 Neutron Gun offers a massive energy payload at the expense of speed and energy efficiency. One could argue the virtues of speed, rate of fire and distance over damage, but the argument becomes irrelevant if you only need to hit them once.'
    shipBuilder_vehicleitem_47.name = u'K_W_CF_117_Badger_Repeater_Laser_Turret'
    shipBuilder_vehicleitem_47.displayName = u'CF-117 Badger Repeater Laser Turret'
    shipBuilder_vehicleitem_47.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_47.manufacturer = None
    shipBuilder_vehicleitem_47.itemSize = 4
    shipBuilder_vehicleitem_47.views = 0
    shipBuilder_vehicleitem_47.disabled = True
    shipBuilder_vehicleitem_47 = save_or_locate(shipBuilder_vehicleitem_47)

    shipBuilder_vehicleitem_48 = VehicleItem()
    shipBuilder_vehicleitem_48.itemClass = 0
    shipBuilder_vehicleitem_48.description = None
    shipBuilder_vehicleitem_48.name = u'KDK_TM-4_Slider'
    shipBuilder_vehicleitem_48.displayName = u'KDK TM-4 Slider Thruster'
    shipBuilder_vehicleitem_48.itemType = shipBuilder_vehicleitemtype_13
    shipBuilder_vehicleitem_48.manufacturer = None
    shipBuilder_vehicleitem_48.itemSize = 1
    shipBuilder_vehicleitem_48.views = 0
    shipBuilder_vehicleitem_48.disabled = True
    shipBuilder_vehicleitem_48 = save_or_locate(shipBuilder_vehicleitem_48)

    shipBuilder_vehicleitem_49 = VehicleItem()
    shipBuilder_vehicleitem_49.itemClass = 1
    shipBuilder_vehicleitem_49.description = u"The 11-Series Broadsword is the cannon pilots come to when they want the 3 D's: distance, dependability and damage. Packing a 45mm round, the Broadsword can fire a variety of rounds for any occasion."
    shipBuilder_vehicleitem_49.name = u'Knightbridge_11_Series_Broadsword'
    shipBuilder_vehicleitem_49.displayName = u'11-Series Broadsword'
    shipBuilder_vehicleitem_49.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_49.manufacturer = None
    shipBuilder_vehicleitem_49.itemSize = 3
    shipBuilder_vehicleitem_49.views = 0
    shipBuilder_vehicleitem_49.disabled = True
    shipBuilder_vehicleitem_49 = save_or_locate(shipBuilder_vehicleitem_49)

    shipBuilder_vehicleitem_50 = VehicleItem()
    shipBuilder_vehicleitem_50.itemClass = 1
    shipBuilder_vehicleitem_50.description = u"The entry level weapon of the Sword-series, the Longsword fires a 35mm round designed for use against a variety of armored targets. Don't let shields slow down your domination of the galaxy."
    shipBuilder_vehicleitem_50.name = u'Knightbridge_9_Series_Longsword'
    shipBuilder_vehicleitem_50.displayName = u'9-Series Longsword'
    shipBuilder_vehicleitem_50.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_50.manufacturer = None
    shipBuilder_vehicleitem_50.itemSize = 1
    shipBuilder_vehicleitem_50.views = 0
    shipBuilder_vehicleitem_50.disabled = True
    shipBuilder_vehicleitem_50 = save_or_locate(shipBuilder_vehicleitem_50)

    shipBuilder_vehicleitem_51 = VehicleItem()
    shipBuilder_vehicleitem_51.itemClass = 0
    shipBuilder_vehicleitem_51.description = None
    shipBuilder_vehicleitem_51.name = u'LPB_Condensed_Matter_Reactor'
    shipBuilder_vehicleitem_51.displayName = u'Lightning Powerbolt Hyperfluid Quantum Vortex'
    shipBuilder_vehicleitem_51.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_51.manufacturer = None
    shipBuilder_vehicleitem_51.itemSize = 3
    shipBuilder_vehicleitem_51.views = 0
    shipBuilder_vehicleitem_51.disabled = True
    shipBuilder_vehicleitem_51 = save_or_locate(shipBuilder_vehicleitem_51)

    shipBuilder_vehicleitem_52 = VehicleItem()
    shipBuilder_vehicleitem_52.itemClass = 0
    shipBuilder_vehicleitem_52.description = u"Lightning Power ltd's Powerbolt makes its living by offering the perfect blend of performance and signature masking. Lightning's proprietary Superfluid Quantum Vortex technology keeps energy emissions low while providing better output than typical stealth-oriented plants."
    shipBuilder_vehicleitem_52.name = u'LPB_Powerbolt'
    shipBuilder_vehicleitem_52.displayName = u'Lightning Powerbolt Powerbolt'
    shipBuilder_vehicleitem_52.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_52.manufacturer = None
    shipBuilder_vehicleitem_52.itemSize = 4
    shipBuilder_vehicleitem_52.views = 0
    shipBuilder_vehicleitem_52.disabled = True
    shipBuilder_vehicleitem_52 = save_or_locate(shipBuilder_vehicleitem_52)

    shipBuilder_vehicleitem_53 = VehicleItem()
    shipBuilder_vehicleitem_53.itemClass = 0
    shipBuilder_vehicleitem_53.description = u'The Mantis GT-220 is a hydraulically-driven Gatling-type rotary cannon designed to deliver smaller rounds at a very high rate of fire. The Mantis is designed to shred armor on very fast targets, sacrificing power for absolute saturation of the target area.'
    shipBuilder_vehicleitem_53.name = u'Mantis_GT-220'
    shipBuilder_vehicleitem_53.displayName = u'Mantis GT-220'
    shipBuilder_vehicleitem_53.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_53.manufacturer = None
    shipBuilder_vehicleitem_53.itemSize = 2
    shipBuilder_vehicleitem_53.views = 0
    shipBuilder_vehicleitem_53.disabled = True
    shipBuilder_vehicleitem_53 = save_or_locate(shipBuilder_vehicleitem_53)

    shipBuilder_vehicleitem_54 = VehicleItem()
    shipBuilder_vehicleitem_54.itemClass = 1
    shipBuilder_vehicleitem_54.description = None
    shipBuilder_vehicleitem_54.name = u'Max_Ox_NN13_Neutron'
    shipBuilder_vehicleitem_54.displayName = u'MaxOx NN-13 Neutron Cannon'
    shipBuilder_vehicleitem_54.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_54.manufacturer = None
    shipBuilder_vehicleitem_54.itemSize = 1
    shipBuilder_vehicleitem_54.views = 0
    shipBuilder_vehicleitem_54.disabled = True
    shipBuilder_vehicleitem_54 = save_or_locate(shipBuilder_vehicleitem_54)

    shipBuilder_vehicleitem_55 = VehicleItem()
    shipBuilder_vehicleitem_55.itemClass = 0
    shipBuilder_vehicleitem_55.description = None
    shipBuilder_vehicleitem_55.name = u'MissileTurret'
    shipBuilder_vehicleitem_55.displayName = u'Missileturret'
    shipBuilder_vehicleitem_55.itemType = shipBuilder_vehicleitemtype_5
    shipBuilder_vehicleitem_55.manufacturer = None
    shipBuilder_vehicleitem_55.itemSize = 2
    shipBuilder_vehicleitem_55.views = 0
    shipBuilder_vehicleitem_55.disabled = True
    shipBuilder_vehicleitem_55 = save_or_locate(shipBuilder_vehicleitem_55)

    shipBuilder_vehicleitem_56 = VehicleItem()
    shipBuilder_vehicleitem_56.itemClass = 0
    shipBuilder_vehicleitem_56.description = None
    shipBuilder_vehicleitem_56.name = u'OJ_Omni_Precison_Thruster_TR2'
    shipBuilder_vehicleitem_56.displayName = u'Origin Omni Precision Ball Thruster'
    shipBuilder_vehicleitem_56.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_56.manufacturer = None
    shipBuilder_vehicleitem_56.itemSize = 1
    shipBuilder_vehicleitem_56.views = 0
    shipBuilder_vehicleitem_56.disabled = True
    shipBuilder_vehicleitem_56 = save_or_locate(shipBuilder_vehicleitem_56)

    shipBuilder_vehicleitem_57 = VehicleItem()
    shipBuilder_vehicleitem_57.itemClass = 0
    shipBuilder_vehicleitem_57.description = None
    shipBuilder_vehicleitem_57.name = u'OJ_Scalpel_Precision_Thruster_TR2'
    shipBuilder_vehicleitem_57.displayName = u'Origin Scalpel Precision Thruster'
    shipBuilder_vehicleitem_57.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_57.manufacturer = None
    shipBuilder_vehicleitem_57.itemSize = 1
    shipBuilder_vehicleitem_57.views = 0
    shipBuilder_vehicleitem_57.disabled = True
    shipBuilder_vehicleitem_57 = save_or_locate(shipBuilder_vehicleitem_57)

    shipBuilder_vehicleitem_58 = VehicleItem()
    shipBuilder_vehicleitem_58.itemClass = 0
    shipBuilder_vehicleitem_58.description = u''
    shipBuilder_vehicleitem_58.name = u'OKB_Energia_IV'
    shipBuilder_vehicleitem_58.displayName = u'OKB Voshkod Energia IV'
    shipBuilder_vehicleitem_58.itemType = shipBuilder_vehicleitemtype_14
    shipBuilder_vehicleitem_58.manufacturer = None
    shipBuilder_vehicleitem_58.itemSize = 2
    shipBuilder_vehicleitem_58.views = 0
    shipBuilder_vehicleitem_58.disabled = True
    shipBuilder_vehicleitem_58 = save_or_locate(shipBuilder_vehicleitem_58)

    shipBuilder_vehicleitem_59 = VehicleItem()
    shipBuilder_vehicleitem_59.itemClass = 1
    shipBuilder_vehicleitem_59.description = u"The Omnisky III is the base model in A&R's line of laser cannons for small ships and has a comparable rate of fire, damage output and range to other weapons in its size class. It uses mid-grade components in its design, offering a marked increase in power efficiency over some of its less expensive competitors."
    shipBuilder_vehicleitem_59.name = u'Omnisky_III_Laser'
    shipBuilder_vehicleitem_59.displayName = u'Omnisky III Laser Cannon'
    shipBuilder_vehicleitem_59.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_59.manufacturer = None
    shipBuilder_vehicleitem_59.itemSize = 1
    shipBuilder_vehicleitem_59.views = 0
    shipBuilder_vehicleitem_59.disabled = True
    shipBuilder_vehicleitem_59 = save_or_locate(shipBuilder_vehicleitem_59)

    shipBuilder_vehicleitem_60 = VehicleItem()
    shipBuilder_vehicleitem_60.itemClass = 1
    shipBuilder_vehicleitem_60.description = u'The Omnisky VI is the mid-sized laser cannon from manufacturer A&R. It boasts increased damage and range and power consumption over its smaller brother, the Omnisky III, and utilizes many of the same components resulting in middle-of-the-road power efficiency.'
    shipBuilder_vehicleitem_60.name = u'Omnisky_VI_Laser'
    shipBuilder_vehicleitem_60.displayName = u'Omnisky VI Laser Cannon'
    shipBuilder_vehicleitem_60.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_60.manufacturer = None
    shipBuilder_vehicleitem_60.itemSize = 2
    shipBuilder_vehicleitem_60.views = 0
    shipBuilder_vehicleitem_60.disabled = True
    shipBuilder_vehicleitem_60 = save_or_locate(shipBuilder_vehicleitem_60)

    shipBuilder_vehicleitem_61 = VehicleItem()
    shipBuilder_vehicleitem_61.itemClass = 0
    shipBuilder_vehicleitem_61.description = None
    shipBuilder_vehicleitem_61.name = u'PhalanxTurret'
    shipBuilder_vehicleitem_61.displayName = u'Phalanxturret'
    shipBuilder_vehicleitem_61.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_61.manufacturer = None
    shipBuilder_vehicleitem_61.itemSize = 2
    shipBuilder_vehicleitem_61.views = 0
    shipBuilder_vehicleitem_61.disabled = True
    shipBuilder_vehicleitem_61 = save_or_locate(shipBuilder_vehicleitem_61)

    shipBuilder_vehicleitem_62 = VehicleItem()
    shipBuilder_vehicleitem_62.itemClass = 0
    shipBuilder_vehicleitem_62.description = None
    shipBuilder_vehicleitem_62.name = u'RSI_DefaultBattery'
    shipBuilder_vehicleitem_62.displayName = u'RSI Battery'
    shipBuilder_vehicleitem_62.itemType = shipBuilder_vehicleitemtype_16
    shipBuilder_vehicleitem_62.manufacturer = None
    shipBuilder_vehicleitem_62.itemSize = 1
    shipBuilder_vehicleitem_62.views = 0
    shipBuilder_vehicleitem_62.disabled = True
    shipBuilder_vehicleitem_62 = save_or_locate(shipBuilder_vehicleitem_62)

    shipBuilder_vehicleitem_63 = VehicleItem()
    shipBuilder_vehicleitem_63.itemClass = 0
    shipBuilder_vehicleitem_63.description = None
    shipBuilder_vehicleitem_63.name = u'RSI_DefaultCooler'
    shipBuilder_vehicleitem_63.displayName = u'RSI Heat Cooler'
    shipBuilder_vehicleitem_63.itemType = shipBuilder_vehicleitemtype_17
    shipBuilder_vehicleitem_63.manufacturer = None
    shipBuilder_vehicleitem_63.itemSize = 1
    shipBuilder_vehicleitem_63.views = 0
    shipBuilder_vehicleitem_63.disabled = True
    shipBuilder_vehicleitem_63 = save_or_locate(shipBuilder_vehicleitem_63)

    shipBuilder_vehicleitem_64 = VehicleItem()
    shipBuilder_vehicleitem_64.itemClass = 0
    shipBuilder_vehicleitem_64.description = None
    shipBuilder_vehicleitem_64.name = u'RSI_DefaultPowerPlant'
    shipBuilder_vehicleitem_64.displayName = u'RSI Power Supply'
    shipBuilder_vehicleitem_64.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_64.manufacturer = None
    shipBuilder_vehicleitem_64.itemSize = 1
    shipBuilder_vehicleitem_64.views = 0
    shipBuilder_vehicleitem_64.disabled = True
    shipBuilder_vehicleitem_64 = save_or_locate(shipBuilder_vehicleitem_64)

    shipBuilder_vehicleitem_65 = VehicleItem()
    shipBuilder_vehicleitem_65.itemClass = 0
    shipBuilder_vehicleitem_65.description = None
    shipBuilder_vehicleitem_65.name = u'RSI_DefaultRadarDisplay'
    shipBuilder_vehicleitem_65.displayName = u'RSI Radar Display'
    shipBuilder_vehicleitem_65.itemType = shipBuilder_vehicleitemtype_18
    shipBuilder_vehicleitem_65.manufacturer = None
    shipBuilder_vehicleitem_65.itemSize = 1
    shipBuilder_vehicleitem_65.views = 0
    shipBuilder_vehicleitem_65.disabled = True
    shipBuilder_vehicleitem_65 = save_or_locate(shipBuilder_vehicleitem_65)

    shipBuilder_vehicleitem_66 = VehicleItem()
    shipBuilder_vehicleitem_66.itemClass = 0
    shipBuilder_vehicleitem_66.description = None
    shipBuilder_vehicleitem_66.name = u'RSI_DefaultRadarLongRange'
    shipBuilder_vehicleitem_66.displayName = u'RSI Radar Long Range'
    shipBuilder_vehicleitem_66.itemType = shipBuilder_vehicleitemtype_19
    shipBuilder_vehicleitem_66.manufacturer = None
    shipBuilder_vehicleitem_66.itemSize = 1
    shipBuilder_vehicleitem_66.views = 0
    shipBuilder_vehicleitem_66.disabled = True
    shipBuilder_vehicleitem_66 = save_or_locate(shipBuilder_vehicleitem_66)

    shipBuilder_vehicleitem_67 = VehicleItem()
    shipBuilder_vehicleitem_67.itemClass = 0
    shipBuilder_vehicleitem_67.description = None
    shipBuilder_vehicleitem_67.name = u'RSI_DefaultRadarMidRange'
    shipBuilder_vehicleitem_67.displayName = u'RSI Radar Mid Range'
    shipBuilder_vehicleitem_67.itemType = shipBuilder_vehicleitemtype_20
    shipBuilder_vehicleitem_67.manufacturer = None
    shipBuilder_vehicleitem_67.itemSize = 1
    shipBuilder_vehicleitem_67.views = 0
    shipBuilder_vehicleitem_67.disabled = True
    shipBuilder_vehicleitem_67 = save_or_locate(shipBuilder_vehicleitem_67)

    shipBuilder_vehicleitem_68 = VehicleItem()
    shipBuilder_vehicleitem_68.itemClass = 0
    shipBuilder_vehicleitem_68.description = None
    shipBuilder_vehicleitem_68.name = u'RSI_DefaultRadarShortRange'
    shipBuilder_vehicleitem_68.displayName = u'RSI Radar Short Range'
    shipBuilder_vehicleitem_68.itemType = shipBuilder_vehicleitemtype_21
    shipBuilder_vehicleitem_68.manufacturer = None
    shipBuilder_vehicleitem_68.itemSize = 1
    shipBuilder_vehicleitem_68.views = 0
    shipBuilder_vehicleitem_68.disabled = True
    shipBuilder_vehicleitem_68 = save_or_locate(shipBuilder_vehicleitem_68)

    shipBuilder_vehicleitem_69 = VehicleItem()
    shipBuilder_vehicleitem_69.itemClass = 0
    shipBuilder_vehicleitem_69.description = None
    shipBuilder_vehicleitem_69.name = u'RSI_DefaultTargetSelector'
    shipBuilder_vehicleitem_69.displayName = u'RSI Target Selection Device'
    shipBuilder_vehicleitem_69.itemType = shipBuilder_vehicleitemtype_22
    shipBuilder_vehicleitem_69.manufacturer = None
    shipBuilder_vehicleitem_69.itemSize = 1
    shipBuilder_vehicleitem_69.views = 0
    shipBuilder_vehicleitem_69.disabled = True
    shipBuilder_vehicleitem_69 = save_or_locate(shipBuilder_vehicleitem_69)

    shipBuilder_vehicleitem_70 = VehicleItem()
    shipBuilder_vehicleitem_70.itemClass = 0
    shipBuilder_vehicleitem_70.description = None
    shipBuilder_vehicleitem_70.name = u'RSI_DefaultVisor'
    shipBuilder_vehicleitem_70.displayName = u'RSI Visor Display'
    shipBuilder_vehicleitem_70.itemType = shipBuilder_vehicleitemtype_23
    shipBuilder_vehicleitem_70.manufacturer = None
    shipBuilder_vehicleitem_70.itemSize = 1
    shipBuilder_vehicleitem_70.views = 0
    shipBuilder_vehicleitem_70.disabled = True
    shipBuilder_vehicleitem_70 = save_or_locate(shipBuilder_vehicleitem_70)

    shipBuilder_vehicleitem_71 = VehicleItem()
    shipBuilder_vehicleitem_71.itemClass = 0
    shipBuilder_vehicleitem_71.description = None
    shipBuilder_vehicleitem_71.name = u'RSI_DefaultWeaponDisplay'
    shipBuilder_vehicleitem_71.displayName = u'RSI Weapon Display'
    shipBuilder_vehicleitem_71.itemType = shipBuilder_vehicleitemtype_24
    shipBuilder_vehicleitem_71.manufacturer = None
    shipBuilder_vehicleitem_71.itemSize = 1
    shipBuilder_vehicleitem_71.views = 0
    shipBuilder_vehicleitem_71.disabled = True
    shipBuilder_vehicleitem_71 = save_or_locate(shipBuilder_vehicleitem_71)

    shipBuilder_vehicleitem_72 = VehicleItem()
    shipBuilder_vehicleitem_72.itemClass = 0
    shipBuilder_vehicleitem_72.description = None
    shipBuilder_vehicleitem_72.name = u'RSI_MissileBay'
    shipBuilder_vehicleitem_72.displayName = u'Missile Bay'
    shipBuilder_vehicleitem_72.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_72.manufacturer = None
    shipBuilder_vehicleitem_72.itemSize = 2
    shipBuilder_vehicleitem_72.views = 0
    shipBuilder_vehicleitem_72.disabled = True
    shipBuilder_vehicleitem_72 = save_or_locate(shipBuilder_vehicleitem_72)

    shipBuilder_vehicleitem_73 = VehicleItem()
    shipBuilder_vehicleitem_73.itemClass = 0
    shipBuilder_vehicleitem_73.description = u"Designed as an competitor to Lightning Power's Powerbolt, the 6HE8A manages to achieve an even smaller EM signature by utilizing a new Helium 6 sonoluminescent process. The 6HE8A's applications for covert flight make it the ideal power plant for pilots who wish to be shadows in space."
    shipBuilder_vehicleitem_73.name = u'Sakura_Sun_Light_Blossom_6HE8A'
    shipBuilder_vehicleitem_73.displayName = u'Sakura Sun Light Blossom 6HE8A'
    shipBuilder_vehicleitem_73.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_73.manufacturer = None
    shipBuilder_vehicleitem_73.itemSize = 4
    shipBuilder_vehicleitem_73.views = 0
    shipBuilder_vehicleitem_73.disabled = True
    shipBuilder_vehicleitem_73 = save_or_locate(shipBuilder_vehicleitem_73)

    shipBuilder_vehicleitem_74 = VehicleItem()
    shipBuilder_vehicleitem_74.itemClass = 0
    shipBuilder_vehicleitem_74.description = None
    shipBuilder_vehicleitem_74.name = u'ScytheLeftWingCannon'
    shipBuilder_vehicleitem_74.displayName = u'Scytheleftwingcannon'
    shipBuilder_vehicleitem_74.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_74.manufacturer = None
    shipBuilder_vehicleitem_74.itemSize = 2
    shipBuilder_vehicleitem_74.views = 0
    shipBuilder_vehicleitem_74.disabled = True
    shipBuilder_vehicleitem_74 = save_or_locate(shipBuilder_vehicleitem_74)

    shipBuilder_vehicleitem_75 = VehicleItem()
    shipBuilder_vehicleitem_75.itemClass = 0
    shipBuilder_vehicleitem_75.description = None
    shipBuilder_vehicleitem_75.name = u'ScytheMissileRacks'
    shipBuilder_vehicleitem_75.displayName = u'Scythemissileracks'
    shipBuilder_vehicleitem_75.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_75.manufacturer = None
    shipBuilder_vehicleitem_75.itemSize = 2
    shipBuilder_vehicleitem_75.views = 0
    shipBuilder_vehicleitem_75.disabled = True
    shipBuilder_vehicleitem_75 = save_or_locate(shipBuilder_vehicleitem_75)

    shipBuilder_vehicleitem_76 = VehicleItem()
    shipBuilder_vehicleitem_76.itemClass = 0
    shipBuilder_vehicleitem_76.description = None
    shipBuilder_vehicleitem_76.name = u'ScytheRightWingCannon'
    shipBuilder_vehicleitem_76.displayName = u'Scytherightwingcannon'
    shipBuilder_vehicleitem_76.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_76.manufacturer = None
    shipBuilder_vehicleitem_76.itemSize = 2
    shipBuilder_vehicleitem_76.views = 0
    shipBuilder_vehicleitem_76.disabled = True
    shipBuilder_vehicleitem_76 = save_or_locate(shipBuilder_vehicleitem_76)

    shipBuilder_vehicleitem_77 = VehicleItem()
    shipBuilder_vehicleitem_77.itemClass = 0
    shipBuilder_vehicleitem_77.description = u"Strike fast and strike hard with the VOLT Stinger. Sure, each shot isn't much on its own, but what does that matter when they've got a dozen more friends a second?"
    shipBuilder_vehicleitem_77.name = u'Stinger'
    shipBuilder_vehicleitem_77.displayName = u'Stinger'
    shipBuilder_vehicleitem_77.itemType = shipBuilder_vehicleitemtype_9
    shipBuilder_vehicleitem_77.manufacturer = None
    shipBuilder_vehicleitem_77.itemSize = 1
    shipBuilder_vehicleitem_77.views = 0
    shipBuilder_vehicleitem_77.disabled = True
    shipBuilder_vehicleitem_77 = save_or_locate(shipBuilder_vehicleitem_77)

    shipBuilder_vehicleitem_78 = VehicleItem()
    shipBuilder_vehicleitem_78.itemClass = 0
    shipBuilder_vehicleitem_78.description = u'Made with the same rugged construction techniques as the smaller 5 ton model, the Stor-All model A Big Box cargo pod upgrade for the Aurora doubles the available cargo space. (Replaces default cargo option.)'
    shipBuilder_vehicleitem_78.name = u'Stor-All_Big_Box_Model_A'
    shipBuilder_vehicleitem_78.displayName = u'Stor-All Big Box Model A'
    shipBuilder_vehicleitem_78.itemType = shipBuilder_vehicleitemtype_25
    shipBuilder_vehicleitem_78.manufacturer = None
    shipBuilder_vehicleitem_78.itemSize = 4
    shipBuilder_vehicleitem_78.views = 0
    shipBuilder_vehicleitem_78.disabled = True
    shipBuilder_vehicleitem_78 = save_or_locate(shipBuilder_vehicleitem_78)

    shipBuilder_vehicleitem_79 = VehicleItem()
    shipBuilder_vehicleitem_79.itemClass = 0
    shipBuilder_vehicleitem_79.description = u'Designed exclusively for the Hornet F7C, the Stor-All Big Box model H replaces the void left by the turret system of the military-spec craft with a respectable cargo hold. Transforming the flagship fighter of the UEEN into a durable hauling ship.'
    shipBuilder_vehicleitem_79.name = u'Stor-All_Big_Box_Model_H'
    shipBuilder_vehicleitem_79.displayName = u'Stor-All Big Box Model H'
    shipBuilder_vehicleitem_79.itemType = shipBuilder_vehicleitemtype_25
    shipBuilder_vehicleitem_79.manufacturer = None
    shipBuilder_vehicleitem_79.itemSize = 4
    shipBuilder_vehicleitem_79.views = 0
    shipBuilder_vehicleitem_79.disabled = True
    shipBuilder_vehicleitem_79 = save_or_locate(shipBuilder_vehicleitem_79)

    shipBuilder_vehicleitem_80 = VehicleItem()
    shipBuilder_vehicleitem_80.itemClass = 0
    shipBuilder_vehicleitem_80.description = u'The 5 ton Stor-All Mini cargo pod allows the enterprising Aurora pilot to begin his business in the commodities transportation sector. It has a double wall and pressurized construction that can withstand the rigors of space or the occasional laser blast.'
    shipBuilder_vehicleitem_80.name = u'Stor-All_Mini'
    shipBuilder_vehicleitem_80.displayName = u'Stor-All Mini'
    shipBuilder_vehicleitem_80.itemType = shipBuilder_vehicleitemtype_25
    shipBuilder_vehicleitem_80.manufacturer = None
    shipBuilder_vehicleitem_80.itemSize = 4
    shipBuilder_vehicleitem_80.views = 0
    shipBuilder_vehicleitem_80.disabled = True
    shipBuilder_vehicleitem_80 = save_or_locate(shipBuilder_vehicleitem_80)

    shipBuilder_vehicleitem_81 = VehicleItem()
    shipBuilder_vehicleitem_81.itemClass = 0
    shipBuilder_vehicleitem_81.description = None
    shipBuilder_vehicleitem_81.name = u'STSTurret'
    shipBuilder_vehicleitem_81.displayName = u'Ststurret'
    shipBuilder_vehicleitem_81.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_81.manufacturer = None
    shipBuilder_vehicleitem_81.itemSize = 2
    shipBuilder_vehicleitem_81.views = 0
    shipBuilder_vehicleitem_81.disabled = True
    shipBuilder_vehicleitem_81 = save_or_locate(shipBuilder_vehicleitem_81)

    shipBuilder_vehicleitem_82 = VehicleItem()
    shipBuilder_vehicleitem_82.itemClass = 3
    shipBuilder_vehicleitem_82.description = u"In the thin market of FF missiles, the Dominator is one of the few stand-outs. With Talon's state-of-the-art target recognition system, these missiles are ideal for mixing it up with large numbers of ships. Varying sizes available."
    shipBuilder_vehicleitem_82.name = u'Talon_Dominator_Platform_x4'
    shipBuilder_vehicleitem_82.displayName = u'Talon Dominator FF Quad'
    shipBuilder_vehicleitem_82.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_82.manufacturer = None
    shipBuilder_vehicleitem_82.itemSize = 3
    shipBuilder_vehicleitem_82.views = 0
    shipBuilder_vehicleitem_82.disabled = True
    shipBuilder_vehicleitem_82 = save_or_locate(shipBuilder_vehicleitem_82)

    shipBuilder_vehicleitem_83 = VehicleItem()
    shipBuilder_vehicleitem_83.itemClass = 3
    shipBuilder_vehicleitem_83.description = u"Talon's Executioner missiles track and lock their target by use of highly sensitive optical cameras and image processing software. The Executioners deliver a combination of hull-breaching and high-explosive payload, making them effective weapons against smaller capital ships."
    shipBuilder_vehicleitem_83.name = u'Talon_Executioner_IR_Twin'
    shipBuilder_vehicleitem_83.displayName = u'Talon Executioner IR Twin'
    shipBuilder_vehicleitem_83.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_83.manufacturer = None
    shipBuilder_vehicleitem_83.itemSize = 2
    shipBuilder_vehicleitem_83.views = 0
    shipBuilder_vehicleitem_83.disabled = True
    shipBuilder_vehicleitem_83 = save_or_locate(shipBuilder_vehicleitem_83)

    shipBuilder_vehicleitem_84 = VehicleItem()
    shipBuilder_vehicleitem_84.itemClass = 3
    shipBuilder_vehicleitem_84.description = u'Talon Stalker missiles track and lock their target by use of highly sensitive optical cameras and image processing software. Although they have an increased lock time over other missile types, they are much more difficult for targets to shake once lock is attained. Rack of four (4).'
    shipBuilder_vehicleitem_84.name = u'Talon_Stalker_Quad'
    shipBuilder_vehicleitem_84.displayName = u'Talon Stalker Quad Rack'
    shipBuilder_vehicleitem_84.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_84.manufacturer = None
    shipBuilder_vehicleitem_84.itemSize = 3
    shipBuilder_vehicleitem_84.views = 0
    shipBuilder_vehicleitem_84.disabled = True
    shipBuilder_vehicleitem_84 = save_or_locate(shipBuilder_vehicleitem_84)

    shipBuilder_vehicleitem_85 = VehicleItem()
    shipBuilder_vehicleitem_85.itemClass = 3
    shipBuilder_vehicleitem_85.description = u'Talon Stalker missiles track and lock their target by use of highly sensitive optical cameras and image processing software. Although they have an increased lock time over other missile types, they are much more difficult for targets to shake once lock is attained. Rack of two (2).'
    shipBuilder_vehicleitem_85.name = u'Talon_Stalker_Twin'
    shipBuilder_vehicleitem_85.displayName = u'Talon Stalker Twin Rack'
    shipBuilder_vehicleitem_85.itemType = shipBuilder_vehicleitemtype_7
    shipBuilder_vehicleitem_85.manufacturer = None
    shipBuilder_vehicleitem_85.itemSize = 3
    shipBuilder_vehicleitem_85.views = 0
    shipBuilder_vehicleitem_85.disabled = True
    shipBuilder_vehicleitem_85 = save_or_locate(shipBuilder_vehicleitem_85)

    shipBuilder_vehicleitem_86 = VehicleItem()
    shipBuilder_vehicleitem_86.itemClass = 0
    shipBuilder_vehicleitem_86.description = u"Wei-Tek's HFR2 Plus reactors are specially designed and optimized for medium sized craft. The hydrogen 6+ technology offers a robust power output but with a lower heat signature and higher durability."
    shipBuilder_vehicleitem_86.name = u'Wei_Tek_HFR2_Plus'
    shipBuilder_vehicleitem_86.displayName = u'Wei Tek HFR2 Plus'
    shipBuilder_vehicleitem_86.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_86.manufacturer = None
    shipBuilder_vehicleitem_86.itemSize = 4
    shipBuilder_vehicleitem_86.views = 0
    shipBuilder_vehicleitem_86.disabled = True
    shipBuilder_vehicleitem_86 = save_or_locate(shipBuilder_vehicleitem_86)

    shipBuilder_vehicleitem_87 = VehicleItem()
    shipBuilder_vehicleitem_87.itemClass = 0
    shipBuilder_vehicleitem_87.description = u"Wei-Tek's VHT2 Plus is one of their oldest models. A fission-based power plant, the VHT2 Plus maintains the fission tradition of low output and high signature, but offers a higher quality construction than most of its competitors that increases the technology's longevity."
    shipBuilder_vehicleitem_87.name = u'Wei_Tek_VHT2_Plus'
    shipBuilder_vehicleitem_87.displayName = u'Wei Tek VHT2 Plus'
    shipBuilder_vehicleitem_87.itemType = shipBuilder_vehicleitemtype_1
    shipBuilder_vehicleitem_87.manufacturer = None
    shipBuilder_vehicleitem_87.itemSize = 4
    shipBuilder_vehicleitem_87.views = 0
    shipBuilder_vehicleitem_87.disabled = True
    shipBuilder_vehicleitem_87 = save_or_locate(shipBuilder_vehicleitem_87)

    shipBuilder_vehicleitem_88 = VehicleItem()
    shipBuilder_vehicleitem_88.itemClass = 0
    shipBuilder_vehicleitem_88.description = u'The X-Forge P/S2-80 is a small thruster that mainly finds use on Aurora class starships. Boasting good thrust output and fuel efficiency, the P/S2-80 is an excellent choice for those with a bit of wanderlust.'
    shipBuilder_vehicleitem_88.name = u'XForge_PS2_80'
    shipBuilder_vehicleitem_88.displayName = u'XForge P/S2-80 Main Engine'
    shipBuilder_vehicleitem_88.itemType = shipBuilder_vehicleitemtype_14
    shipBuilder_vehicleitem_88.manufacturer = None
    shipBuilder_vehicleitem_88.itemSize = 2
    shipBuilder_vehicleitem_88.views = 0
    shipBuilder_vehicleitem_88.disabled = True
    shipBuilder_vehicleitem_88 = save_or_locate(shipBuilder_vehicleitem_88)

    shipBuilder_vehicleitem_89 = VehicleItem()
    shipBuilder_vehicleitem_89.itemClass = 0
    shipBuilder_vehicleitem_89.description = u'MaxOx\u2019s NN-13 Neutron Gun offers a massive energy payload at the expense of speed and energy efficiency. One could argue the virtues of speed, rate of fire and distance over damage, but the argument becomes irrelevant if you only need to hit them once.'
    shipBuilder_vehicleitem_89.name = u'Hornet_BallTurret'
    shipBuilder_vehicleitem_89.displayName = u'CF-117 Badger Repeater Laser Turret'
    shipBuilder_vehicleitem_89.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_89.manufacturer = None
    shipBuilder_vehicleitem_89.itemSize = 2
    shipBuilder_vehicleitem_89.views = 0
    shipBuilder_vehicleitem_89.disabled = False
    shipBuilder_vehicleitem_89 = save_or_locate(shipBuilder_vehicleitem_89)

    shipBuilder_vehicleitem_90 = VehicleItem()
    shipBuilder_vehicleitem_90.itemClass = 0
    shipBuilder_vehicleitem_90.description = u'Featuring a three-barrel sequential fire design, the Klaus & Werner CF-007 Bulldog repeater is capable of high rates of fire while maintaining accuracy. It has low damage per projectile and, although it has relatively low power consumption over-all, several publications have commented on its somewhat lackluster efficiency. Even so, the CF-007 remains a favorite among new pilots who are outfitting their first ship.'
    shipBuilder_vehicleitem_90.name = u'Hornet_CanardTurret'
    shipBuilder_vehicleitem_90.displayName = u'007 Bulldog Laser Repeater Turret'
    shipBuilder_vehicleitem_90.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_90.manufacturer = None
    shipBuilder_vehicleitem_90.itemSize = 2
    shipBuilder_vehicleitem_90.views = 0
    shipBuilder_vehicleitem_90.disabled = False
    shipBuilder_vehicleitem_90 = save_or_locate(shipBuilder_vehicleitem_90)

    #Processing model: ItemPort

    from shipBuilder.models import ItemPort

    shipBuilder_itemport_1 = ItemPort()
    shipBuilder_itemport_1.displayName = u'Top Turret Slot'
    shipBuilder_itemport_1.name = u'hardpoint_class_4_cannonball'
    shipBuilder_itemport_1.flags = u'front nose'
    shipBuilder_itemport_1.maxSize = 4
    shipBuilder_itemport_1.minSize = 1
    shipBuilder_itemport_1.parentItem = None
    shipBuilder_itemport_1.portClass = 0
    shipBuilder_itemport_1.disabled = False
    shipBuilder_itemport_1 = save_or_locate(shipBuilder_itemport_1)

    shipBuilder_itemport_1.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_1.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_1.supportedTypes.add(shipBuilder_vehicleitemtype_6)

    shipBuilder_itemport_2 = ItemPort()
    shipBuilder_itemport_2.displayName = u'Left Bay Slot'
    shipBuilder_itemport_2.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_2.flags = u'left bottom'
    shipBuilder_itemport_2.maxSize = 3
    shipBuilder_itemport_2.minSize = 1
    shipBuilder_itemport_2.parentItem = None
    shipBuilder_itemport_2.portClass = 0
    shipBuilder_itemport_2.disabled = False
    shipBuilder_itemport_2 = save_or_locate(shipBuilder_itemport_2)

    shipBuilder_itemport_2.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_3 = ItemPort()
    shipBuilder_itemport_3.displayName = u'Right Bay Slot'
    shipBuilder_itemport_3.name = u'hardpoint_class_3_right_bay_door'
    shipBuilder_itemport_3.flags = u'right bottom'
    shipBuilder_itemport_3.maxSize = 3
    shipBuilder_itemport_3.minSize = 1
    shipBuilder_itemport_3.parentItem = None
    shipBuilder_itemport_3.portClass = 0
    shipBuilder_itemport_3.disabled = False
    shipBuilder_itemport_3 = save_or_locate(shipBuilder_itemport_3)

    shipBuilder_itemport_3.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_4 = ItemPort()
    shipBuilder_itemport_4.displayName = u'Left Display'
    shipBuilder_itemport_4.name = u'left_movil_lower_rotor'
    shipBuilder_itemport_4.flags = u'left lower'
    shipBuilder_itemport_4.maxSize = 1
    shipBuilder_itemport_4.minSize = 1
    shipBuilder_itemport_4.parentItem = None
    shipBuilder_itemport_4.portClass = 0
    shipBuilder_itemport_4.disabled = False
    shipBuilder_itemport_4 = save_or_locate(shipBuilder_itemport_4)

    shipBuilder_itemport_4.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_5 = ItemPort()
    shipBuilder_itemport_5.displayName = u'Right Display'
    shipBuilder_itemport_5.name = u'right_movil_lower_rotor'
    shipBuilder_itemport_5.flags = u'right lower'
    shipBuilder_itemport_5.maxSize = 1
    shipBuilder_itemport_5.minSize = 1
    shipBuilder_itemport_5.parentItem = None
    shipBuilder_itemport_5.portClass = 0
    shipBuilder_itemport_5.disabled = False
    shipBuilder_itemport_5 = save_or_locate(shipBuilder_itemport_5)

    shipBuilder_itemport_5.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_6 = ItemPort()
    shipBuilder_itemport_6.displayName = u'Top Left Display'
    shipBuilder_itemport_6.name = u'top_left_movil_lower_rotor'
    shipBuilder_itemport_6.flags = u'left upper'
    shipBuilder_itemport_6.maxSize = 1
    shipBuilder_itemport_6.minSize = 1
    shipBuilder_itemport_6.parentItem = None
    shipBuilder_itemport_6.portClass = 0
    shipBuilder_itemport_6.disabled = False
    shipBuilder_itemport_6 = save_or_locate(shipBuilder_itemport_6)

    shipBuilder_itemport_6.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_7 = ItemPort()
    shipBuilder_itemport_7.displayName = u'Top Right Display'
    shipBuilder_itemport_7.name = u'top_right_movil_lower_rotor'
    shipBuilder_itemport_7.flags = u'right upper'
    shipBuilder_itemport_7.maxSize = 1
    shipBuilder_itemport_7.minSize = 1
    shipBuilder_itemport_7.parentItem = None
    shipBuilder_itemport_7.portClass = 0
    shipBuilder_itemport_7.disabled = False
    shipBuilder_itemport_7 = save_or_locate(shipBuilder_itemport_7)

    shipBuilder_itemport_7.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_8 = ItemPort()
    shipBuilder_itemport_8.displayName = u'Front Slot'
    shipBuilder_itemport_8.name = u'hardpoint_class_4_nose'
    shipBuilder_itemport_8.flags = u'front nose'
    shipBuilder_itemport_8.maxSize = 4
    shipBuilder_itemport_8.minSize = 1
    shipBuilder_itemport_8.parentItem = None
    shipBuilder_itemport_8.portClass = 0
    shipBuilder_itemport_8.disabled = False
    shipBuilder_itemport_8 = save_or_locate(shipBuilder_itemport_8)

    shipBuilder_itemport_8.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_8.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_8.supportedTypes.add(shipBuilder_vehicleitemtype_6)

    shipBuilder_itemport_9 = ItemPort()
    shipBuilder_itemport_9.displayName = u'Left Wing Slot'
    shipBuilder_itemport_9.name = u'hardpoint_class_2_left_wing'
    shipBuilder_itemport_9.flags = u'left wing bottom'
    shipBuilder_itemport_9.maxSize = 4
    shipBuilder_itemport_9.minSize = 1
    shipBuilder_itemport_9.parentItem = None
    shipBuilder_itemport_9.portClass = 0
    shipBuilder_itemport_9.disabled = False
    shipBuilder_itemport_9 = save_or_locate(shipBuilder_itemport_9)

    shipBuilder_itemport_9.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_10 = ItemPort()
    shipBuilder_itemport_10.displayName = u'Right Wing Slot'
    shipBuilder_itemport_10.name = u'hardpoint_class_2_right_wing'
    shipBuilder_itemport_10.flags = u'right wing bottom'
    shipBuilder_itemport_10.maxSize = 4
    shipBuilder_itemport_10.minSize = 1
    shipBuilder_itemport_10.parentItem = None
    shipBuilder_itemport_10.portClass = 0
    shipBuilder_itemport_10.disabled = False
    shipBuilder_itemport_10 = save_or_locate(shipBuilder_itemport_10)

    shipBuilder_itemport_10.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_11 = ItemPort()
    shipBuilder_itemport_11.displayName = u'Power Plant'
    shipBuilder_itemport_11.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_11.flags = u''
    shipBuilder_itemport_11.maxSize = 4
    shipBuilder_itemport_11.minSize = 1
    shipBuilder_itemport_11.parentItem = None
    shipBuilder_itemport_11.portClass = 0
    shipBuilder_itemport_11.disabled = False
    shipBuilder_itemport_11 = save_or_locate(shipBuilder_itemport_11)

    shipBuilder_itemport_11.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_12 = ItemPort()
    shipBuilder_itemport_12.displayName = u'Port Thruster Main Tr4'
    shipBuilder_itemport_12.name = u'Port_Thruster_Main_TR4'
    shipBuilder_itemport_12.flags = u'main rear'
    shipBuilder_itemport_12.maxSize = 4
    shipBuilder_itemport_12.minSize = 4
    shipBuilder_itemport_12.parentItem = None
    shipBuilder_itemport_12.portClass = 0
    shipBuilder_itemport_12.disabled = False
    shipBuilder_itemport_12 = save_or_locate(shipBuilder_itemport_12)

    shipBuilder_itemport_12.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_13 = ItemPort()
    shipBuilder_itemport_13.displayName = u'Port Thruster Bottom Left Back'
    shipBuilder_itemport_13.name = u'Port_Thruster_Bottom_Left_Back'
    shipBuilder_itemport_13.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_13.maxSize = 2
    shipBuilder_itemport_13.minSize = 1
    shipBuilder_itemport_13.parentItem = None
    shipBuilder_itemport_13.portClass = 0
    shipBuilder_itemport_13.disabled = False
    shipBuilder_itemport_13 = save_or_locate(shipBuilder_itemport_13)

    shipBuilder_itemport_13.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_14 = ItemPort()
    shipBuilder_itemport_14.displayName = u'Port Thruster Bottom Right Back'
    shipBuilder_itemport_14.name = u'Port_Thruster_Bottom_Right_Back'
    shipBuilder_itemport_14.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_14.maxSize = 2
    shipBuilder_itemport_14.minSize = 1
    shipBuilder_itemport_14.parentItem = None
    shipBuilder_itemport_14.portClass = 0
    shipBuilder_itemport_14.disabled = False
    shipBuilder_itemport_14 = save_or_locate(shipBuilder_itemport_14)

    shipBuilder_itemport_14.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_15 = ItemPort()
    shipBuilder_itemport_15.displayName = u'Port Thruster Bottom Left Front'
    shipBuilder_itemport_15.name = u'Port_Thruster_Bottom_Left_Front'
    shipBuilder_itemport_15.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_15.maxSize = 2
    shipBuilder_itemport_15.minSize = 1
    shipBuilder_itemport_15.parentItem = None
    shipBuilder_itemport_15.portClass = 0
    shipBuilder_itemport_15.disabled = False
    shipBuilder_itemport_15 = save_or_locate(shipBuilder_itemport_15)

    shipBuilder_itemport_15.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_16 = ItemPort()
    shipBuilder_itemport_16.displayName = u'Port Thruster Bottom Right Front'
    shipBuilder_itemport_16.name = u'Port_Thruster_Bottom_Right_Front'
    shipBuilder_itemport_16.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_16.maxSize = 2
    shipBuilder_itemport_16.minSize = 1
    shipBuilder_itemport_16.parentItem = None
    shipBuilder_itemport_16.portClass = 0
    shipBuilder_itemport_16.disabled = False
    shipBuilder_itemport_16 = save_or_locate(shipBuilder_itemport_16)

    shipBuilder_itemport_16.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_17 = ItemPort()
    shipBuilder_itemport_17.displayName = u'Port Thruster Upper Right Front'
    shipBuilder_itemport_17.name = u'Port_Thruster_Upper_Right_Front'
    shipBuilder_itemport_17.flags = u'maneuver orientation retro -X -Z upper front right'
    shipBuilder_itemport_17.maxSize = 2
    shipBuilder_itemport_17.minSize = 1
    shipBuilder_itemport_17.parentItem = None
    shipBuilder_itemport_17.portClass = 0
    shipBuilder_itemport_17.disabled = False
    shipBuilder_itemport_17 = save_or_locate(shipBuilder_itemport_17)

    shipBuilder_itemport_17.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_18 = ItemPort()
    shipBuilder_itemport_18.displayName = u'Port Thruster Upper Left Front'
    shipBuilder_itemport_18.name = u'Port_Thruster_Upper_Left_Front'
    shipBuilder_itemport_18.flags = u'maneuver orientation retro +X -Z upper front left'
    shipBuilder_itemport_18.maxSize = 2
    shipBuilder_itemport_18.minSize = 1
    shipBuilder_itemport_18.parentItem = None
    shipBuilder_itemport_18.portClass = 0
    shipBuilder_itemport_18.disabled = False
    shipBuilder_itemport_18 = save_or_locate(shipBuilder_itemport_18)

    shipBuilder_itemport_18.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_19 = ItemPort()
    shipBuilder_itemport_19.displayName = u'Port Thruster Upper Right Back'
    shipBuilder_itemport_19.name = u'Port_Thruster_Upper_Right_Back'
    shipBuilder_itemport_19.flags = u'maneuver orientation -X -Z upper rear right'
    shipBuilder_itemport_19.maxSize = 2
    shipBuilder_itemport_19.minSize = 1
    shipBuilder_itemport_19.parentItem = None
    shipBuilder_itemport_19.portClass = 0
    shipBuilder_itemport_19.disabled = False
    shipBuilder_itemport_19 = save_or_locate(shipBuilder_itemport_19)

    shipBuilder_itemport_19.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_20 = ItemPort()
    shipBuilder_itemport_20.displayName = u'Port Thruster Upper Left Back'
    shipBuilder_itemport_20.name = u'Port_Thruster_Upper_Left_Back'
    shipBuilder_itemport_20.flags = u'maneuver orientation +X -Z upper rear left'
    shipBuilder_itemport_20.maxSize = 2
    shipBuilder_itemport_20.minSize = 1
    shipBuilder_itemport_20.parentItem = None
    shipBuilder_itemport_20.portClass = 0
    shipBuilder_itemport_20.disabled = False
    shipBuilder_itemport_20 = save_or_locate(shipBuilder_itemport_20)

    shipBuilder_itemport_20.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_21 = ItemPort()
    shipBuilder_itemport_21.displayName = u'Top Turret Slot'
    shipBuilder_itemport_21.name = u'hardpoint_class_4_center'
    shipBuilder_itemport_21.flags = u'center'
    shipBuilder_itemport_21.maxSize = 4
    shipBuilder_itemport_21.minSize = 2
    shipBuilder_itemport_21.parentItem = None
    shipBuilder_itemport_21.portClass = 0
    shipBuilder_itemport_21.disabled = False
    shipBuilder_itemport_21 = save_or_locate(shipBuilder_itemport_21)

    shipBuilder_itemport_21.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_21.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_21.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_21.supportedTypes.add(shipBuilder_vehicleitemtype_12)

    shipBuilder_itemport_22 = ItemPort()
    shipBuilder_itemport_22.displayName = u'Left Bay Slot'
    shipBuilder_itemport_22.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_22.flags = u'left bottom'
    shipBuilder_itemport_22.maxSize = 3
    shipBuilder_itemport_22.minSize = 1
    shipBuilder_itemport_22.parentItem = None
    shipBuilder_itemport_22.portClass = 0
    shipBuilder_itemport_22.disabled = False
    shipBuilder_itemport_22 = save_or_locate(shipBuilder_itemport_22)

    shipBuilder_itemport_22.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_23 = ItemPort()
    shipBuilder_itemport_23.displayName = u'Right Bay Slot'
    shipBuilder_itemport_23.name = u'hardpoint_class_3_right_bay_door'
    shipBuilder_itemport_23.flags = u'right bottom'
    shipBuilder_itemport_23.maxSize = 3
    shipBuilder_itemport_23.minSize = 1
    shipBuilder_itemport_23.parentItem = None
    shipBuilder_itemport_23.portClass = 0
    shipBuilder_itemport_23.disabled = False
    shipBuilder_itemport_23 = save_or_locate(shipBuilder_itemport_23)

    shipBuilder_itemport_23.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_24 = ItemPort()
    shipBuilder_itemport_24.displayName = u'Front Slot'
    shipBuilder_itemport_24.name = u'hardpoint_class_4_nose'
    shipBuilder_itemport_24.flags = u'front nose'
    shipBuilder_itemport_24.maxSize = 3
    shipBuilder_itemport_24.minSize = 1
    shipBuilder_itemport_24.parentItem = None
    shipBuilder_itemport_24.portClass = 0
    shipBuilder_itemport_24.disabled = False
    shipBuilder_itemport_24 = save_or_locate(shipBuilder_itemport_24)

    shipBuilder_itemport_24.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_24.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_24.supportedTypes.add(shipBuilder_vehicleitemtype_6)

    shipBuilder_itemport_25 = ItemPort()
    shipBuilder_itemport_25.displayName = u'Left Display'
    shipBuilder_itemport_25.name = u'left_movil_lower_rotor'
    shipBuilder_itemport_25.flags = u'left lower'
    shipBuilder_itemport_25.maxSize = 1
    shipBuilder_itemport_25.minSize = 1
    shipBuilder_itemport_25.parentItem = None
    shipBuilder_itemport_25.portClass = 0
    shipBuilder_itemport_25.disabled = False
    shipBuilder_itemport_25 = save_or_locate(shipBuilder_itemport_25)

    shipBuilder_itemport_25.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_26 = ItemPort()
    shipBuilder_itemport_26.displayName = u'Right Display'
    shipBuilder_itemport_26.name = u'right_movil_lower_rotor'
    shipBuilder_itemport_26.flags = u'right lower'
    shipBuilder_itemport_26.maxSize = 1
    shipBuilder_itemport_26.minSize = 1
    shipBuilder_itemport_26.parentItem = None
    shipBuilder_itemport_26.portClass = 0
    shipBuilder_itemport_26.disabled = False
    shipBuilder_itemport_26 = save_or_locate(shipBuilder_itemport_26)

    shipBuilder_itemport_26.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_27 = ItemPort()
    shipBuilder_itemport_27.displayName = u'Top Left Display'
    shipBuilder_itemport_27.name = u'top_left_movil_lower_rotor'
    shipBuilder_itemport_27.flags = u'left upper'
    shipBuilder_itemport_27.maxSize = 1
    shipBuilder_itemport_27.minSize = 1
    shipBuilder_itemport_27.parentItem = None
    shipBuilder_itemport_27.portClass = 0
    shipBuilder_itemport_27.disabled = False
    shipBuilder_itemport_27 = save_or_locate(shipBuilder_itemport_27)

    shipBuilder_itemport_27.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_28 = ItemPort()
    shipBuilder_itemport_28.displayName = u'Top Right Display'
    shipBuilder_itemport_28.name = u'top_right_movil_lower_rotor'
    shipBuilder_itemport_28.flags = u'right upper'
    shipBuilder_itemport_28.maxSize = 1
    shipBuilder_itemport_28.minSize = 1
    shipBuilder_itemport_28.parentItem = None
    shipBuilder_itemport_28.portClass = 0
    shipBuilder_itemport_28.disabled = False
    shipBuilder_itemport_28 = save_or_locate(shipBuilder_itemport_28)

    shipBuilder_itemport_28.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_29 = ItemPort()
    shipBuilder_itemport_29.displayName = u'Right Nose Slot'
    shipBuilder_itemport_29.name = u'hardpoint_class_1_nose_right'
    shipBuilder_itemport_29.flags = u'nose right'
    shipBuilder_itemport_29.maxSize = 2
    shipBuilder_itemport_29.minSize = 1
    shipBuilder_itemport_29.parentItem = None
    shipBuilder_itemport_29.portClass = 0
    shipBuilder_itemport_29.disabled = False
    shipBuilder_itemport_29 = save_or_locate(shipBuilder_itemport_29)

    shipBuilder_itemport_29.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_30 = ItemPort()
    shipBuilder_itemport_30.displayName = u'Left Nose Slot'
    shipBuilder_itemport_30.name = u'hardpoint_class_1_nose_left'
    shipBuilder_itemport_30.flags = u'nose left'
    shipBuilder_itemport_30.maxSize = 2
    shipBuilder_itemport_30.minSize = 1
    shipBuilder_itemport_30.parentItem = None
    shipBuilder_itemport_30.portClass = 0
    shipBuilder_itemport_30.disabled = False
    shipBuilder_itemport_30 = save_or_locate(shipBuilder_itemport_30)

    shipBuilder_itemport_30.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_31 = ItemPort()
    shipBuilder_itemport_31.displayName = u'Left Wing Slot'
    shipBuilder_itemport_31.name = u'hardpoint_class_2_left_wing'
    shipBuilder_itemport_31.flags = u'left wing bottom'
    shipBuilder_itemport_31.maxSize = 3
    shipBuilder_itemport_31.minSize = 1
    shipBuilder_itemport_31.parentItem = None
    shipBuilder_itemport_31.portClass = 0
    shipBuilder_itemport_31.disabled = False
    shipBuilder_itemport_31 = save_or_locate(shipBuilder_itemport_31)

    shipBuilder_itemport_31.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_32 = ItemPort()
    shipBuilder_itemport_32.displayName = u'Right Wing Slot'
    shipBuilder_itemport_32.name = u'hardpoint_class_2_right_wing'
    shipBuilder_itemport_32.flags = u'right wing bottom'
    shipBuilder_itemport_32.maxSize = 3
    shipBuilder_itemport_32.minSize = 1
    shipBuilder_itemport_32.parentItem = None
    shipBuilder_itemport_32.portClass = 0
    shipBuilder_itemport_32.disabled = False
    shipBuilder_itemport_32 = save_or_locate(shipBuilder_itemport_32)

    shipBuilder_itemport_32.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_33 = ItemPort()
    shipBuilder_itemport_33.displayName = u'Power Plant'
    shipBuilder_itemport_33.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_33.flags = u''
    shipBuilder_itemport_33.maxSize = 3
    shipBuilder_itemport_33.minSize = 2
    shipBuilder_itemport_33.parentItem = None
    shipBuilder_itemport_33.portClass = 0
    shipBuilder_itemport_33.disabled = False
    shipBuilder_itemport_33 = save_or_locate(shipBuilder_itemport_33)

    shipBuilder_itemport_33.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_34 = ItemPort()
    shipBuilder_itemport_34.displayName = u'Engine Attach'
    shipBuilder_itemport_34.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_34.flags = u'main rear'
    shipBuilder_itemport_34.maxSize = 4
    shipBuilder_itemport_34.minSize = 3
    shipBuilder_itemport_34.parentItem = None
    shipBuilder_itemport_34.portClass = 0
    shipBuilder_itemport_34.disabled = False
    shipBuilder_itemport_34 = save_or_locate(shipBuilder_itemport_34)

    shipBuilder_itemport_34.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_35 = ItemPort()
    shipBuilder_itemport_35.displayName = u'Thruster Bottom Back Left'
    shipBuilder_itemport_35.name = u'hardpoint_thruster_bottom_back_left'
    shipBuilder_itemport_35.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_35.maxSize = 2
    shipBuilder_itemport_35.minSize = 1
    shipBuilder_itemport_35.parentItem = None
    shipBuilder_itemport_35.portClass = 0
    shipBuilder_itemport_35.disabled = False
    shipBuilder_itemport_35 = save_or_locate(shipBuilder_itemport_35)

    shipBuilder_itemport_35.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_36 = ItemPort()
    shipBuilder_itemport_36.displayName = u'Thruster Bottom Back Right'
    shipBuilder_itemport_36.name = u'hardpoint_thruster_bottom_back_right'
    shipBuilder_itemport_36.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_36.maxSize = 2
    shipBuilder_itemport_36.minSize = 1
    shipBuilder_itemport_36.parentItem = None
    shipBuilder_itemport_36.portClass = 0
    shipBuilder_itemport_36.disabled = False
    shipBuilder_itemport_36 = save_or_locate(shipBuilder_itemport_36)

    shipBuilder_itemport_36.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_37 = ItemPort()
    shipBuilder_itemport_37.displayName = u'Thruster Bottom Front Left'
    shipBuilder_itemport_37.name = u'hardpoint_thruster_bottom_front_left'
    shipBuilder_itemport_37.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_37.maxSize = 2
    shipBuilder_itemport_37.minSize = 1
    shipBuilder_itemport_37.parentItem = None
    shipBuilder_itemport_37.portClass = 0
    shipBuilder_itemport_37.disabled = False
    shipBuilder_itemport_37 = save_or_locate(shipBuilder_itemport_37)

    shipBuilder_itemport_37.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_38 = ItemPort()
    shipBuilder_itemport_38.displayName = u'Thruster Bottom Front Right'
    shipBuilder_itemport_38.name = u'hardpoint_thruster_bottom_front_right'
    shipBuilder_itemport_38.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_38.maxSize = 2
    shipBuilder_itemport_38.minSize = 1
    shipBuilder_itemport_38.parentItem = None
    shipBuilder_itemport_38.portClass = 0
    shipBuilder_itemport_38.disabled = False
    shipBuilder_itemport_38 = save_or_locate(shipBuilder_itemport_38)

    shipBuilder_itemport_38.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_39 = ItemPort()
    shipBuilder_itemport_39.displayName = u'Thruster Top Front Right'
    shipBuilder_itemport_39.name = u'hardpoint_thruster_top_front_right'
    shipBuilder_itemport_39.flags = u'maneuver orientation retro -X -Z top front right'
    shipBuilder_itemport_39.maxSize = 2
    shipBuilder_itemport_39.minSize = 1
    shipBuilder_itemport_39.parentItem = None
    shipBuilder_itemport_39.portClass = 0
    shipBuilder_itemport_39.disabled = False
    shipBuilder_itemport_39 = save_or_locate(shipBuilder_itemport_39)

    shipBuilder_itemport_39.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_40 = ItemPort()
    shipBuilder_itemport_40.displayName = u'Thruster Top Front Left'
    shipBuilder_itemport_40.name = u'hardpoint_thruster_top_front_left'
    shipBuilder_itemport_40.flags = u'maneuver orientation retro +X -Z top front left'
    shipBuilder_itemport_40.maxSize = 2
    shipBuilder_itemport_40.minSize = 1
    shipBuilder_itemport_40.parentItem = None
    shipBuilder_itemport_40.portClass = 0
    shipBuilder_itemport_40.disabled = False
    shipBuilder_itemport_40 = save_or_locate(shipBuilder_itemport_40)

    shipBuilder_itemport_40.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_41 = ItemPort()
    shipBuilder_itemport_41.displayName = u'Thruster Top Back Right'
    shipBuilder_itemport_41.name = u'hardpoint_thruster_top_back_right'
    shipBuilder_itemport_41.flags = u'maneuver orientation -X -Z top rear right'
    shipBuilder_itemport_41.maxSize = 2
    shipBuilder_itemport_41.minSize = 1
    shipBuilder_itemport_41.parentItem = None
    shipBuilder_itemport_41.portClass = 0
    shipBuilder_itemport_41.disabled = False
    shipBuilder_itemport_41 = save_or_locate(shipBuilder_itemport_41)

    shipBuilder_itemport_41.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_42 = ItemPort()
    shipBuilder_itemport_42.displayName = u'Thruster Top Back Left'
    shipBuilder_itemport_42.name = u'hardpoint_thruster_top_back_left'
    shipBuilder_itemport_42.flags = u'maneuver orientation +X -Z top rear left'
    shipBuilder_itemport_42.maxSize = 2
    shipBuilder_itemport_42.minSize = 1
    shipBuilder_itemport_42.parentItem = None
    shipBuilder_itemport_42.portClass = 0
    shipBuilder_itemport_42.disabled = False
    shipBuilder_itemport_42 = save_or_locate(shipBuilder_itemport_42)

    shipBuilder_itemport_42.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_43 = ItemPort()
    shipBuilder_itemport_43.displayName = u'Power Plant'
    shipBuilder_itemport_43.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_43.flags = u'main rear'
    shipBuilder_itemport_43.maxSize = 5
    shipBuilder_itemport_43.minSize = 3
    shipBuilder_itemport_43.parentItem = None
    shipBuilder_itemport_43.portClass = 0
    shipBuilder_itemport_43.disabled = False
    shipBuilder_itemport_43 = save_or_locate(shipBuilder_itemport_43)

    shipBuilder_itemport_43.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_44 = ItemPort()
    shipBuilder_itemport_44.displayName = u'Engine Attach'
    shipBuilder_itemport_44.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_44.flags = u'main rear'
    shipBuilder_itemport_44.maxSize = 5
    shipBuilder_itemport_44.minSize = 4
    shipBuilder_itemport_44.parentItem = None
    shipBuilder_itemport_44.portClass = 0
    shipBuilder_itemport_44.disabled = False
    shipBuilder_itemport_44 = save_or_locate(shipBuilder_itemport_44)

    shipBuilder_itemport_44.supportedTypes.add(shipBuilder_vehicleitemtype_26)

    shipBuilder_itemport_45 = ItemPort()
    shipBuilder_itemport_45.displayName = u'Thruster Rear Right Bottom'
    shipBuilder_itemport_45.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_45.flags = u'maneuver orientation lower rear right'
    shipBuilder_itemport_45.maxSize = 2
    shipBuilder_itemport_45.minSize = 1
    shipBuilder_itemport_45.parentItem = None
    shipBuilder_itemport_45.portClass = 0
    shipBuilder_itemport_45.disabled = False
    shipBuilder_itemport_45 = save_or_locate(shipBuilder_itemport_45)

    shipBuilder_itemport_45.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_46 = ItemPort()
    shipBuilder_itemport_46.displayName = u'Thruster Rear Right Mid'
    shipBuilder_itemport_46.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_46.flags = u'maneuver orientation mid rear right'
    shipBuilder_itemport_46.maxSize = 2
    shipBuilder_itemport_46.minSize = 1
    shipBuilder_itemport_46.parentItem = None
    shipBuilder_itemport_46.portClass = 0
    shipBuilder_itemport_46.disabled = False
    shipBuilder_itemport_46 = save_or_locate(shipBuilder_itemport_46)

    shipBuilder_itemport_46.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_47 = ItemPort()
    shipBuilder_itemport_47.displayName = u'Thruster Rear Right Upper'
    shipBuilder_itemport_47.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_47.flags = u'maneuver orientation +Z upper rear right'
    shipBuilder_itemport_47.maxSize = 2
    shipBuilder_itemport_47.minSize = 1
    shipBuilder_itemport_47.parentItem = None
    shipBuilder_itemport_47.portClass = 0
    shipBuilder_itemport_47.disabled = False
    shipBuilder_itemport_47 = save_or_locate(shipBuilder_itemport_47)

    shipBuilder_itemport_47.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_48 = ItemPort()
    shipBuilder_itemport_48.displayName = u'Thruster Rear Left Bottom'
    shipBuilder_itemport_48.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_48.flags = u'maneuver orientation lower rear left'
    shipBuilder_itemport_48.maxSize = 2
    shipBuilder_itemport_48.minSize = 1
    shipBuilder_itemport_48.parentItem = None
    shipBuilder_itemport_48.portClass = 0
    shipBuilder_itemport_48.disabled = False
    shipBuilder_itemport_48 = save_or_locate(shipBuilder_itemport_48)

    shipBuilder_itemport_48.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_49 = ItemPort()
    shipBuilder_itemport_49.displayName = u'Thruster Rear Left Mid'
    shipBuilder_itemport_49.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_49.flags = u'maneuver orientation mid rear left'
    shipBuilder_itemport_49.maxSize = 2
    shipBuilder_itemport_49.minSize = 1
    shipBuilder_itemport_49.parentItem = None
    shipBuilder_itemport_49.portClass = 0
    shipBuilder_itemport_49.disabled = False
    shipBuilder_itemport_49 = save_or_locate(shipBuilder_itemport_49)

    shipBuilder_itemport_49.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_50 = ItemPort()
    shipBuilder_itemport_50.displayName = u'Thruster Rear Left Upper'
    shipBuilder_itemport_50.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_50.flags = u'maneuver orientation upper rear left'
    shipBuilder_itemport_50.maxSize = 2
    shipBuilder_itemport_50.minSize = 1
    shipBuilder_itemport_50.parentItem = None
    shipBuilder_itemport_50.portClass = 0
    shipBuilder_itemport_50.disabled = False
    shipBuilder_itemport_50 = save_or_locate(shipBuilder_itemport_50)

    shipBuilder_itemport_50.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_51 = ItemPort()
    shipBuilder_itemport_51.displayName = u'Thruster Front Right Bottom'
    shipBuilder_itemport_51.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_51.flags = u'maneuver orientation retro lower front right'
    shipBuilder_itemport_51.maxSize = 2
    shipBuilder_itemport_51.minSize = 1
    shipBuilder_itemport_51.parentItem = None
    shipBuilder_itemport_51.portClass = 0
    shipBuilder_itemport_51.disabled = False
    shipBuilder_itemport_51 = save_or_locate(shipBuilder_itemport_51)

    shipBuilder_itemport_51.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_52 = ItemPort()
    shipBuilder_itemport_52.displayName = u'Thruster Front Right Upper'
    shipBuilder_itemport_52.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_52.flags = u'maneuver orientation retro upper front right'
    shipBuilder_itemport_52.maxSize = 2
    shipBuilder_itemport_52.minSize = 1
    shipBuilder_itemport_52.parentItem = None
    shipBuilder_itemport_52.portClass = 0
    shipBuilder_itemport_52.disabled = False
    shipBuilder_itemport_52 = save_or_locate(shipBuilder_itemport_52)

    shipBuilder_itemport_52.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_53 = ItemPort()
    shipBuilder_itemport_53.displayName = u'Thruster Front Right Mid'
    shipBuilder_itemport_53.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_53.flags = u'maneuver orientation retro mid front right'
    shipBuilder_itemport_53.maxSize = 2
    shipBuilder_itemport_53.minSize = 1
    shipBuilder_itemport_53.parentItem = None
    shipBuilder_itemport_53.portClass = 0
    shipBuilder_itemport_53.disabled = False
    shipBuilder_itemport_53 = save_or_locate(shipBuilder_itemport_53)

    shipBuilder_itemport_53.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_54 = ItemPort()
    shipBuilder_itemport_54.displayName = u'Thruster Front Left Bottom'
    shipBuilder_itemport_54.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_54.flags = u'maneuver orientation retro lower front left'
    shipBuilder_itemport_54.maxSize = 2
    shipBuilder_itemport_54.minSize = 1
    shipBuilder_itemport_54.parentItem = None
    shipBuilder_itemport_54.portClass = 0
    shipBuilder_itemport_54.disabled = False
    shipBuilder_itemport_54 = save_or_locate(shipBuilder_itemport_54)

    shipBuilder_itemport_54.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_55 = ItemPort()
    shipBuilder_itemport_55.displayName = u'Thruster Front Left Upper'
    shipBuilder_itemport_55.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_55.flags = u'maneuver orientation retro upper front left'
    shipBuilder_itemport_55.maxSize = 2
    shipBuilder_itemport_55.minSize = 1
    shipBuilder_itemport_55.parentItem = None
    shipBuilder_itemport_55.portClass = 0
    shipBuilder_itemport_55.disabled = False
    shipBuilder_itemport_55 = save_or_locate(shipBuilder_itemport_55)

    shipBuilder_itemport_55.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_56 = ItemPort()
    shipBuilder_itemport_56.displayName = u'Thruster Front Left Mid'
    shipBuilder_itemport_56.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_56.flags = u'maneuver orientation retro mid front left'
    shipBuilder_itemport_56.maxSize = 2
    shipBuilder_itemport_56.minSize = 1
    shipBuilder_itemport_56.parentItem = None
    shipBuilder_itemport_56.portClass = 0
    shipBuilder_itemport_56.disabled = False
    shipBuilder_itemport_56 = save_or_locate(shipBuilder_itemport_56)

    shipBuilder_itemport_56.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_57 = ItemPort()
    shipBuilder_itemport_57.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_57.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_57.flags = u'nose'
    shipBuilder_itemport_57.maxSize = 2
    shipBuilder_itemport_57.minSize = 1
    shipBuilder_itemport_57.parentItem = None
    shipBuilder_itemport_57.portClass = 0
    shipBuilder_itemport_57.disabled = False
    shipBuilder_itemport_57 = save_or_locate(shipBuilder_itemport_57)

    shipBuilder_itemport_57.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_58 = ItemPort()
    shipBuilder_itemport_58.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_58.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_58.flags = u'upper left wing'
    shipBuilder_itemport_58.maxSize = 5
    shipBuilder_itemport_58.minSize = 3
    shipBuilder_itemport_58.parentItem = None
    shipBuilder_itemport_58.portClass = 0
    shipBuilder_itemport_58.disabled = False
    shipBuilder_itemport_58 = save_or_locate(shipBuilder_itemport_58)

    shipBuilder_itemport_58.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_59 = ItemPort()
    shipBuilder_itemport_59.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_59.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_59.flags = u'upper right wing'
    shipBuilder_itemport_59.maxSize = 3
    shipBuilder_itemport_59.minSize = 1
    shipBuilder_itemport_59.parentItem = None
    shipBuilder_itemport_59.portClass = 0
    shipBuilder_itemport_59.disabled = False
    shipBuilder_itemport_59 = save_or_locate(shipBuilder_itemport_59)

    shipBuilder_itemport_59.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_60 = ItemPort()
    shipBuilder_itemport_60.displayName = u'Left Class 2 Mount Top'
    shipBuilder_itemport_60.name = u'Freelancer_side_cannon_L_Hardpoint'
    shipBuilder_itemport_60.flags = u'left side top'
    shipBuilder_itemport_60.maxSize = 5
    shipBuilder_itemport_60.minSize = 3
    shipBuilder_itemport_60.parentItem = None
    shipBuilder_itemport_60.portClass = 0
    shipBuilder_itemport_60.disabled = False
    shipBuilder_itemport_60 = save_or_locate(shipBuilder_itemport_60)

    shipBuilder_itemport_60.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_61 = ItemPort()
    shipBuilder_itemport_61.displayName = u'Left Class 2 Mount Bottom'
    shipBuilder_itemport_61.name = u'Freelancer_side_cannon_L_Bottom_Hardpoint'
    shipBuilder_itemport_61.flags = u'left side bottom'
    shipBuilder_itemport_61.maxSize = 5
    shipBuilder_itemport_61.minSize = 3
    shipBuilder_itemport_61.parentItem = None
    shipBuilder_itemport_61.portClass = 0
    shipBuilder_itemport_61.disabled = False
    shipBuilder_itemport_61 = save_or_locate(shipBuilder_itemport_61)

    shipBuilder_itemport_61.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_62 = ItemPort()
    shipBuilder_itemport_62.displayName = u'Right Class 2 Mount Top'
    shipBuilder_itemport_62.name = u'Freelancer_side_cannon_R_Hardpoint'
    shipBuilder_itemport_62.flags = u'right side top'
    shipBuilder_itemport_62.maxSize = 5
    shipBuilder_itemport_62.minSize = 3
    shipBuilder_itemport_62.parentItem = None
    shipBuilder_itemport_62.portClass = 0
    shipBuilder_itemport_62.disabled = False
    shipBuilder_itemport_62 = save_or_locate(shipBuilder_itemport_62)

    shipBuilder_itemport_62.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_63 = ItemPort()
    shipBuilder_itemport_63.displayName = u'Right Class 2 Mount Bottom'
    shipBuilder_itemport_63.name = u'Freelancer_side_cannon_R_Bottom_Hardpoint'
    shipBuilder_itemport_63.flags = u'right side bottom'
    shipBuilder_itemport_63.maxSize = 5
    shipBuilder_itemport_63.minSize = 3
    shipBuilder_itemport_63.parentItem = None
    shipBuilder_itemport_63.portClass = 0
    shipBuilder_itemport_63.disabled = False
    shipBuilder_itemport_63 = save_or_locate(shipBuilder_itemport_63)

    shipBuilder_itemport_63.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_64 = ItemPort()
    shipBuilder_itemport_64.displayName = u'Power Plant'
    shipBuilder_itemport_64.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_64.flags = u'main rear'
    shipBuilder_itemport_64.maxSize = 3
    shipBuilder_itemport_64.minSize = 2
    shipBuilder_itemport_64.parentItem = None
    shipBuilder_itemport_64.portClass = 0
    shipBuilder_itemport_64.disabled = False
    shipBuilder_itemport_64 = save_or_locate(shipBuilder_itemport_64)

    shipBuilder_itemport_64.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_65 = ItemPort()
    shipBuilder_itemport_65.displayName = u'Engine Attach'
    shipBuilder_itemport_65.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_65.flags = u'main rear'
    shipBuilder_itemport_65.maxSize = 4
    shipBuilder_itemport_65.minSize = 3
    shipBuilder_itemport_65.parentItem = None
    shipBuilder_itemport_65.portClass = 0
    shipBuilder_itemport_65.disabled = False
    shipBuilder_itemport_65 = save_or_locate(shipBuilder_itemport_65)

    shipBuilder_itemport_65.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_66 = ItemPort()
    shipBuilder_itemport_66.displayName = u'Thruster Rear Right Bottom'
    shipBuilder_itemport_66.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_66.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_66.maxSize = 1
    shipBuilder_itemport_66.minSize = 1
    shipBuilder_itemport_66.parentItem = None
    shipBuilder_itemport_66.portClass = 0
    shipBuilder_itemport_66.disabled = False
    shipBuilder_itemport_66 = save_or_locate(shipBuilder_itemport_66)

    shipBuilder_itemport_66.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_67 = ItemPort()
    shipBuilder_itemport_67.displayName = u'Thruster Rear Right Mid'
    shipBuilder_itemport_67.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_67.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_67.maxSize = 1
    shipBuilder_itemport_67.minSize = 1
    shipBuilder_itemport_67.parentItem = None
    shipBuilder_itemport_67.portClass = 0
    shipBuilder_itemport_67.disabled = False
    shipBuilder_itemport_67 = save_or_locate(shipBuilder_itemport_67)

    shipBuilder_itemport_67.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_68 = ItemPort()
    shipBuilder_itemport_68.displayName = u'Thruster Rear Right Upper'
    shipBuilder_itemport_68.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_68.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_68.maxSize = 1
    shipBuilder_itemport_68.minSize = 1
    shipBuilder_itemport_68.parentItem = None
    shipBuilder_itemport_68.portClass = 0
    shipBuilder_itemport_68.disabled = False
    shipBuilder_itemport_68 = save_or_locate(shipBuilder_itemport_68)

    shipBuilder_itemport_68.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_69 = ItemPort()
    shipBuilder_itemport_69.displayName = u'Thruster Rear Left Bottom'
    shipBuilder_itemport_69.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_69.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_69.maxSize = 1
    shipBuilder_itemport_69.minSize = 1
    shipBuilder_itemport_69.parentItem = None
    shipBuilder_itemport_69.portClass = 0
    shipBuilder_itemport_69.disabled = False
    shipBuilder_itemport_69 = save_or_locate(shipBuilder_itemport_69)

    shipBuilder_itemport_69.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_70 = ItemPort()
    shipBuilder_itemport_70.displayName = u'Thruster Rear Left Mid'
    shipBuilder_itemport_70.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_70.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_70.maxSize = 1
    shipBuilder_itemport_70.minSize = 1
    shipBuilder_itemport_70.parentItem = None
    shipBuilder_itemport_70.portClass = 0
    shipBuilder_itemport_70.disabled = False
    shipBuilder_itemport_70 = save_or_locate(shipBuilder_itemport_70)

    shipBuilder_itemport_70.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_71 = ItemPort()
    shipBuilder_itemport_71.displayName = u'Thruster Rear Left Upper'
    shipBuilder_itemport_71.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_71.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_71.maxSize = 1
    shipBuilder_itemport_71.minSize = 1
    shipBuilder_itemport_71.parentItem = None
    shipBuilder_itemport_71.portClass = 0
    shipBuilder_itemport_71.disabled = False
    shipBuilder_itemport_71 = save_or_locate(shipBuilder_itemport_71)

    shipBuilder_itemport_71.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_72 = ItemPort()
    shipBuilder_itemport_72.displayName = u'Thruster Front Right Bottom'
    shipBuilder_itemport_72.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_72.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_72.maxSize = 1
    shipBuilder_itemport_72.minSize = 1
    shipBuilder_itemport_72.parentItem = None
    shipBuilder_itemport_72.portClass = 0
    shipBuilder_itemport_72.disabled = False
    shipBuilder_itemport_72 = save_or_locate(shipBuilder_itemport_72)

    shipBuilder_itemport_72.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_73 = ItemPort()
    shipBuilder_itemport_73.displayName = u'Thruster Front Right Upper'
    shipBuilder_itemport_73.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_73.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_73.maxSize = 1
    shipBuilder_itemport_73.minSize = 1
    shipBuilder_itemport_73.parentItem = None
    shipBuilder_itemport_73.portClass = 0
    shipBuilder_itemport_73.disabled = False
    shipBuilder_itemport_73 = save_or_locate(shipBuilder_itemport_73)

    shipBuilder_itemport_73.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_74 = ItemPort()
    shipBuilder_itemport_74.displayName = u'Thruster Front Right Mid'
    shipBuilder_itemport_74.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_74.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_74.maxSize = 1
    shipBuilder_itemport_74.minSize = 1
    shipBuilder_itemport_74.parentItem = None
    shipBuilder_itemport_74.portClass = 0
    shipBuilder_itemport_74.disabled = False
    shipBuilder_itemport_74 = save_or_locate(shipBuilder_itemport_74)

    shipBuilder_itemport_74.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_75 = ItemPort()
    shipBuilder_itemport_75.displayName = u'Thruster Front Left Bottom'
    shipBuilder_itemport_75.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_75.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_75.maxSize = 1
    shipBuilder_itemport_75.minSize = 1
    shipBuilder_itemport_75.parentItem = None
    shipBuilder_itemport_75.portClass = 0
    shipBuilder_itemport_75.disabled = False
    shipBuilder_itemport_75 = save_or_locate(shipBuilder_itemport_75)

    shipBuilder_itemport_75.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_76 = ItemPort()
    shipBuilder_itemport_76.displayName = u'Thruster Front Left Upper'
    shipBuilder_itemport_76.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_76.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_76.maxSize = 1
    shipBuilder_itemport_76.minSize = 1
    shipBuilder_itemport_76.parentItem = None
    shipBuilder_itemport_76.portClass = 0
    shipBuilder_itemport_76.disabled = False
    shipBuilder_itemport_76 = save_or_locate(shipBuilder_itemport_76)

    shipBuilder_itemport_76.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_77 = ItemPort()
    shipBuilder_itemport_77.displayName = u'Thruster Front Left Mid'
    shipBuilder_itemport_77.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_77.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_77.maxSize = 1
    shipBuilder_itemport_77.minSize = 1
    shipBuilder_itemport_77.parentItem = None
    shipBuilder_itemport_77.portClass = 0
    shipBuilder_itemport_77.disabled = False
    shipBuilder_itemport_77 = save_or_locate(shipBuilder_itemport_77)

    shipBuilder_itemport_77.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_78 = ItemPort()
    shipBuilder_itemport_78.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_78.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_78.flags = u'nose'
    shipBuilder_itemport_78.maxSize = 2
    shipBuilder_itemport_78.minSize = 1
    shipBuilder_itemport_78.parentItem = None
    shipBuilder_itemport_78.portClass = 0
    shipBuilder_itemport_78.disabled = False
    shipBuilder_itemport_78 = save_or_locate(shipBuilder_itemport_78)

    shipBuilder_itemport_78.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_79 = ItemPort()
    shipBuilder_itemport_79.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_79.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_79.flags = u'upper left wing'
    shipBuilder_itemport_79.maxSize = 3
    shipBuilder_itemport_79.minSize = 1
    shipBuilder_itemport_79.parentItem = None
    shipBuilder_itemport_79.portClass = 0
    shipBuilder_itemport_79.disabled = False
    shipBuilder_itemport_79 = save_or_locate(shipBuilder_itemport_79)

    shipBuilder_itemport_79.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_80 = ItemPort()
    shipBuilder_itemport_80.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_80.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_80.flags = u'left wing'
    shipBuilder_itemport_80.maxSize = 3
    shipBuilder_itemport_80.minSize = 1
    shipBuilder_itemport_80.parentItem = None
    shipBuilder_itemport_80.portClass = 0
    shipBuilder_itemport_80.disabled = False
    shipBuilder_itemport_80 = save_or_locate(shipBuilder_itemport_80)

    shipBuilder_itemport_80.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_81 = ItemPort()
    shipBuilder_itemport_81.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_81.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_81.flags = u'upper right wing'
    shipBuilder_itemport_81.maxSize = 3
    shipBuilder_itemport_81.minSize = 1
    shipBuilder_itemport_81.parentItem = None
    shipBuilder_itemport_81.portClass = 0
    shipBuilder_itemport_81.disabled = False
    shipBuilder_itemport_81 = save_or_locate(shipBuilder_itemport_81)

    shipBuilder_itemport_81.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_82 = ItemPort()
    shipBuilder_itemport_82.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_82.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_82.flags = u'right wing'
    shipBuilder_itemport_82.maxSize = 3
    shipBuilder_itemport_82.minSize = 1
    shipBuilder_itemport_82.parentItem = None
    shipBuilder_itemport_82.portClass = 0
    shipBuilder_itemport_82.disabled = False
    shipBuilder_itemport_82 = save_or_locate(shipBuilder_itemport_82)

    shipBuilder_itemport_82.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_83 = ItemPort()
    shipBuilder_itemport_83.displayName = u'Power Plant'
    shipBuilder_itemport_83.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_83.flags = u'main rear'
    shipBuilder_itemport_83.maxSize = 3
    shipBuilder_itemport_83.minSize = 2
    shipBuilder_itemport_83.parentItem = None
    shipBuilder_itemport_83.portClass = 0
    shipBuilder_itemport_83.disabled = False
    shipBuilder_itemport_83 = save_or_locate(shipBuilder_itemport_83)

    shipBuilder_itemport_83.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_84 = ItemPort()
    shipBuilder_itemport_84.displayName = u'Engine Attach'
    shipBuilder_itemport_84.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_84.flags = u'main rear'
    shipBuilder_itemport_84.maxSize = 4
    shipBuilder_itemport_84.minSize = 3
    shipBuilder_itemport_84.parentItem = None
    shipBuilder_itemport_84.portClass = 0
    shipBuilder_itemport_84.disabled = False
    shipBuilder_itemport_84 = save_or_locate(shipBuilder_itemport_84)

    shipBuilder_itemport_84.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_85 = ItemPort()
    shipBuilder_itemport_85.displayName = u'Thruster Rear Right Bottom'
    shipBuilder_itemport_85.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_85.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_85.maxSize = 1
    shipBuilder_itemport_85.minSize = 1
    shipBuilder_itemport_85.parentItem = None
    shipBuilder_itemport_85.portClass = 0
    shipBuilder_itemport_85.disabled = False
    shipBuilder_itemport_85 = save_or_locate(shipBuilder_itemport_85)

    shipBuilder_itemport_85.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_86 = ItemPort()
    shipBuilder_itemport_86.displayName = u'Thruster Rear Right Mid'
    shipBuilder_itemport_86.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_86.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_86.maxSize = 1
    shipBuilder_itemport_86.minSize = 1
    shipBuilder_itemport_86.parentItem = None
    shipBuilder_itemport_86.portClass = 0
    shipBuilder_itemport_86.disabled = False
    shipBuilder_itemport_86 = save_or_locate(shipBuilder_itemport_86)

    shipBuilder_itemport_86.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_87 = ItemPort()
    shipBuilder_itemport_87.displayName = u'Thruster Rear Right Upper'
    shipBuilder_itemport_87.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_87.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_87.maxSize = 1
    shipBuilder_itemport_87.minSize = 1
    shipBuilder_itemport_87.parentItem = None
    shipBuilder_itemport_87.portClass = 0
    shipBuilder_itemport_87.disabled = False
    shipBuilder_itemport_87 = save_or_locate(shipBuilder_itemport_87)

    shipBuilder_itemport_87.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_88 = ItemPort()
    shipBuilder_itemport_88.displayName = u'Thruster Rear Left Bottom'
    shipBuilder_itemport_88.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_88.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_88.maxSize = 1
    shipBuilder_itemport_88.minSize = 1
    shipBuilder_itemport_88.parentItem = None
    shipBuilder_itemport_88.portClass = 0
    shipBuilder_itemport_88.disabled = False
    shipBuilder_itemport_88 = save_or_locate(shipBuilder_itemport_88)

    shipBuilder_itemport_88.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_89 = ItemPort()
    shipBuilder_itemport_89.displayName = u'Thruster Rear Left Mid'
    shipBuilder_itemport_89.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_89.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_89.maxSize = 1
    shipBuilder_itemport_89.minSize = 1
    shipBuilder_itemport_89.parentItem = None
    shipBuilder_itemport_89.portClass = 0
    shipBuilder_itemport_89.disabled = False
    shipBuilder_itemport_89 = save_or_locate(shipBuilder_itemport_89)

    shipBuilder_itemport_89.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_90 = ItemPort()
    shipBuilder_itemport_90.displayName = u'Thruster Rear Left Upper'
    shipBuilder_itemport_90.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_90.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_90.maxSize = 1
    shipBuilder_itemport_90.minSize = 1
    shipBuilder_itemport_90.parentItem = None
    shipBuilder_itemport_90.portClass = 0
    shipBuilder_itemport_90.disabled = False
    shipBuilder_itemport_90 = save_or_locate(shipBuilder_itemport_90)

    shipBuilder_itemport_90.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_91 = ItemPort()
    shipBuilder_itemport_91.displayName = u'Thruster Front Right Bottom'
    shipBuilder_itemport_91.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_91.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_91.maxSize = 1
    shipBuilder_itemport_91.minSize = 1
    shipBuilder_itemport_91.parentItem = None
    shipBuilder_itemport_91.portClass = 0
    shipBuilder_itemport_91.disabled = False
    shipBuilder_itemport_91 = save_or_locate(shipBuilder_itemport_91)

    shipBuilder_itemport_91.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_92 = ItemPort()
    shipBuilder_itemport_92.displayName = u'Thruster Front Right Upper'
    shipBuilder_itemport_92.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_92.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_92.maxSize = 1
    shipBuilder_itemport_92.minSize = 1
    shipBuilder_itemport_92.parentItem = None
    shipBuilder_itemport_92.portClass = 0
    shipBuilder_itemport_92.disabled = False
    shipBuilder_itemport_92 = save_or_locate(shipBuilder_itemport_92)

    shipBuilder_itemport_92.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_93 = ItemPort()
    shipBuilder_itemport_93.displayName = u'Thruster Front Right Mid'
    shipBuilder_itemport_93.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_93.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_93.maxSize = 1
    shipBuilder_itemport_93.minSize = 1
    shipBuilder_itemport_93.parentItem = None
    shipBuilder_itemport_93.portClass = 0
    shipBuilder_itemport_93.disabled = False
    shipBuilder_itemport_93 = save_or_locate(shipBuilder_itemport_93)

    shipBuilder_itemport_93.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_94 = ItemPort()
    shipBuilder_itemport_94.displayName = u'Thruster Front Left Bottom'
    shipBuilder_itemport_94.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_94.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_94.maxSize = 1
    shipBuilder_itemport_94.minSize = 1
    shipBuilder_itemport_94.parentItem = None
    shipBuilder_itemport_94.portClass = 0
    shipBuilder_itemport_94.disabled = False
    shipBuilder_itemport_94 = save_or_locate(shipBuilder_itemport_94)

    shipBuilder_itemport_94.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_95 = ItemPort()
    shipBuilder_itemport_95.displayName = u'Thruster Front Left Upper'
    shipBuilder_itemport_95.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_95.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_95.maxSize = 1
    shipBuilder_itemport_95.minSize = 1
    shipBuilder_itemport_95.parentItem = None
    shipBuilder_itemport_95.portClass = 0
    shipBuilder_itemport_95.disabled = False
    shipBuilder_itemport_95 = save_or_locate(shipBuilder_itemport_95)

    shipBuilder_itemport_95.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_96 = ItemPort()
    shipBuilder_itemport_96.displayName = u'Thruster Front Left Mid'
    shipBuilder_itemport_96.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_96.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_96.maxSize = 1
    shipBuilder_itemport_96.minSize = 1
    shipBuilder_itemport_96.parentItem = None
    shipBuilder_itemport_96.portClass = 0
    shipBuilder_itemport_96.disabled = False
    shipBuilder_itemport_96 = save_or_locate(shipBuilder_itemport_96)

    shipBuilder_itemport_96.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_97 = ItemPort()
    shipBuilder_itemport_97.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_97.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_97.flags = u'nose'
    shipBuilder_itemport_97.maxSize = 2
    shipBuilder_itemport_97.minSize = 1
    shipBuilder_itemport_97.parentItem = None
    shipBuilder_itemport_97.portClass = 0
    shipBuilder_itemport_97.disabled = False
    shipBuilder_itemport_97 = save_or_locate(shipBuilder_itemport_97)

    shipBuilder_itemport_97.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_98 = ItemPort()
    shipBuilder_itemport_98.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_98.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_98.flags = u'upper left wing'
    shipBuilder_itemport_98.maxSize = 3
    shipBuilder_itemport_98.minSize = 1
    shipBuilder_itemport_98.parentItem = None
    shipBuilder_itemport_98.portClass = 0
    shipBuilder_itemport_98.disabled = False
    shipBuilder_itemport_98 = save_or_locate(shipBuilder_itemport_98)

    shipBuilder_itemport_98.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_99 = ItemPort()
    shipBuilder_itemport_99.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_99.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_99.flags = u'left wing'
    shipBuilder_itemport_99.maxSize = 3
    shipBuilder_itemport_99.minSize = 1
    shipBuilder_itemport_99.parentItem = None
    shipBuilder_itemport_99.portClass = 0
    shipBuilder_itemport_99.disabled = False
    shipBuilder_itemport_99 = save_or_locate(shipBuilder_itemport_99)

    shipBuilder_itemport_99.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_100 = ItemPort()
    shipBuilder_itemport_100.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_100.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_100.flags = u'upper right wing'
    shipBuilder_itemport_100.maxSize = 3
    shipBuilder_itemport_100.minSize = 1
    shipBuilder_itemport_100.parentItem = None
    shipBuilder_itemport_100.portClass = 0
    shipBuilder_itemport_100.disabled = False
    shipBuilder_itemport_100 = save_or_locate(shipBuilder_itemport_100)

    shipBuilder_itemport_100.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_101 = ItemPort()
    shipBuilder_itemport_101.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_101.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_101.flags = u'right wing'
    shipBuilder_itemport_101.maxSize = 3
    shipBuilder_itemport_101.minSize = 1
    shipBuilder_itemport_101.parentItem = None
    shipBuilder_itemport_101.portClass = 0
    shipBuilder_itemport_101.disabled = False
    shipBuilder_itemport_101 = save_or_locate(shipBuilder_itemport_101)

    shipBuilder_itemport_101.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_102 = ItemPort()
    shipBuilder_itemport_102.displayName = u'Power Plant'
    shipBuilder_itemport_102.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_102.flags = u'main rear'
    shipBuilder_itemport_102.maxSize = 3
    shipBuilder_itemport_102.minSize = 2
    shipBuilder_itemport_102.parentItem = None
    shipBuilder_itemport_102.portClass = 0
    shipBuilder_itemport_102.disabled = False
    shipBuilder_itemport_102 = save_or_locate(shipBuilder_itemport_102)

    shipBuilder_itemport_102.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_103 = ItemPort()
    shipBuilder_itemport_103.displayName = u'Engine Attach'
    shipBuilder_itemport_103.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_103.flags = u'main rear'
    shipBuilder_itemport_103.maxSize = 4
    shipBuilder_itemport_103.minSize = 3
    shipBuilder_itemport_103.parentItem = None
    shipBuilder_itemport_103.portClass = 0
    shipBuilder_itemport_103.disabled = False
    shipBuilder_itemport_103 = save_or_locate(shipBuilder_itemport_103)

    shipBuilder_itemport_103.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_104 = ItemPort()
    shipBuilder_itemport_104.displayName = u'Thruster Rear Right Bottom'
    shipBuilder_itemport_104.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_104.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_104.maxSize = 1
    shipBuilder_itemport_104.minSize = 1
    shipBuilder_itemport_104.parentItem = None
    shipBuilder_itemport_104.portClass = 0
    shipBuilder_itemport_104.disabled = False
    shipBuilder_itemport_104 = save_or_locate(shipBuilder_itemport_104)

    shipBuilder_itemport_104.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_105 = ItemPort()
    shipBuilder_itemport_105.displayName = u'Thruster Rear Right Mid'
    shipBuilder_itemport_105.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_105.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_105.maxSize = 1
    shipBuilder_itemport_105.minSize = 1
    shipBuilder_itemport_105.parentItem = None
    shipBuilder_itemport_105.portClass = 0
    shipBuilder_itemport_105.disabled = False
    shipBuilder_itemport_105 = save_or_locate(shipBuilder_itemport_105)

    shipBuilder_itemport_105.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_106 = ItemPort()
    shipBuilder_itemport_106.displayName = u'Thruster Rear Right Upper'
    shipBuilder_itemport_106.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_106.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_106.maxSize = 1
    shipBuilder_itemport_106.minSize = 1
    shipBuilder_itemport_106.parentItem = None
    shipBuilder_itemport_106.portClass = 0
    shipBuilder_itemport_106.disabled = False
    shipBuilder_itemport_106 = save_or_locate(shipBuilder_itemport_106)

    shipBuilder_itemport_106.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_107 = ItemPort()
    shipBuilder_itemport_107.displayName = u'Thruster Rear Left Bottom'
    shipBuilder_itemport_107.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_107.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_107.maxSize = 1
    shipBuilder_itemport_107.minSize = 1
    shipBuilder_itemport_107.parentItem = None
    shipBuilder_itemport_107.portClass = 0
    shipBuilder_itemport_107.disabled = False
    shipBuilder_itemport_107 = save_or_locate(shipBuilder_itemport_107)

    shipBuilder_itemport_107.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_108 = ItemPort()
    shipBuilder_itemport_108.displayName = u'Thruster Rear Left Mid'
    shipBuilder_itemport_108.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_108.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_108.maxSize = 1
    shipBuilder_itemport_108.minSize = 1
    shipBuilder_itemport_108.parentItem = None
    shipBuilder_itemport_108.portClass = 0
    shipBuilder_itemport_108.disabled = False
    shipBuilder_itemport_108 = save_or_locate(shipBuilder_itemport_108)

    shipBuilder_itemport_108.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_109 = ItemPort()
    shipBuilder_itemport_109.displayName = u'Thruster Rear Left Upper'
    shipBuilder_itemport_109.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_109.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_109.maxSize = 1
    shipBuilder_itemport_109.minSize = 1
    shipBuilder_itemport_109.parentItem = None
    shipBuilder_itemport_109.portClass = 0
    shipBuilder_itemport_109.disabled = False
    shipBuilder_itemport_109 = save_or_locate(shipBuilder_itemport_109)

    shipBuilder_itemport_109.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_110 = ItemPort()
    shipBuilder_itemport_110.displayName = u'Thruster Front Right Bottom'
    shipBuilder_itemport_110.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_110.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_110.maxSize = 1
    shipBuilder_itemport_110.minSize = 1
    shipBuilder_itemport_110.parentItem = None
    shipBuilder_itemport_110.portClass = 0
    shipBuilder_itemport_110.disabled = False
    shipBuilder_itemport_110 = save_or_locate(shipBuilder_itemport_110)

    shipBuilder_itemport_110.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_111 = ItemPort()
    shipBuilder_itemport_111.displayName = u'Thruster Front Right Upper'
    shipBuilder_itemport_111.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_111.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_111.maxSize = 1
    shipBuilder_itemport_111.minSize = 1
    shipBuilder_itemport_111.parentItem = None
    shipBuilder_itemport_111.portClass = 0
    shipBuilder_itemport_111.disabled = False
    shipBuilder_itemport_111 = save_or_locate(shipBuilder_itemport_111)

    shipBuilder_itemport_111.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_112 = ItemPort()
    shipBuilder_itemport_112.displayName = u'Thruster Front Right Mid'
    shipBuilder_itemport_112.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_112.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_112.maxSize = 1
    shipBuilder_itemport_112.minSize = 1
    shipBuilder_itemport_112.parentItem = None
    shipBuilder_itemport_112.portClass = 0
    shipBuilder_itemport_112.disabled = False
    shipBuilder_itemport_112 = save_or_locate(shipBuilder_itemport_112)

    shipBuilder_itemport_112.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_113 = ItemPort()
    shipBuilder_itemport_113.displayName = u'Thruster Front Left Bottom'
    shipBuilder_itemport_113.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_113.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_113.maxSize = 1
    shipBuilder_itemport_113.minSize = 1
    shipBuilder_itemport_113.parentItem = None
    shipBuilder_itemport_113.portClass = 0
    shipBuilder_itemport_113.disabled = False
    shipBuilder_itemport_113 = save_or_locate(shipBuilder_itemport_113)

    shipBuilder_itemport_113.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_114 = ItemPort()
    shipBuilder_itemport_114.displayName = u'Thruster Front Left Upper'
    shipBuilder_itemport_114.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_114.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_114.maxSize = 1
    shipBuilder_itemport_114.minSize = 1
    shipBuilder_itemport_114.parentItem = None
    shipBuilder_itemport_114.portClass = 0
    shipBuilder_itemport_114.disabled = False
    shipBuilder_itemport_114 = save_or_locate(shipBuilder_itemport_114)

    shipBuilder_itemport_114.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_115 = ItemPort()
    shipBuilder_itemport_115.displayName = u'Thruster Front Left Mid'
    shipBuilder_itemport_115.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_115.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_115.maxSize = 1
    shipBuilder_itemport_115.minSize = 1
    shipBuilder_itemport_115.parentItem = None
    shipBuilder_itemport_115.portClass = 0
    shipBuilder_itemport_115.disabled = False
    shipBuilder_itemport_115 = save_or_locate(shipBuilder_itemport_115)

    shipBuilder_itemport_115.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_116 = ItemPort()
    shipBuilder_itemport_116.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_116.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_116.flags = u'nose'
    shipBuilder_itemport_116.maxSize = 2
    shipBuilder_itemport_116.minSize = 1
    shipBuilder_itemport_116.parentItem = None
    shipBuilder_itemport_116.portClass = 0
    shipBuilder_itemport_116.disabled = False
    shipBuilder_itemport_116 = save_or_locate(shipBuilder_itemport_116)

    shipBuilder_itemport_116.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_117 = ItemPort()
    shipBuilder_itemport_117.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_117.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_117.flags = u'upper left wing'
    shipBuilder_itemport_117.maxSize = 3
    shipBuilder_itemport_117.minSize = 1
    shipBuilder_itemport_117.parentItem = None
    shipBuilder_itemport_117.portClass = 0
    shipBuilder_itemport_117.disabled = False
    shipBuilder_itemport_117 = save_or_locate(shipBuilder_itemport_117)

    shipBuilder_itemport_117.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_118 = ItemPort()
    shipBuilder_itemport_118.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_118.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_118.flags = u'left wing'
    shipBuilder_itemport_118.maxSize = 3
    shipBuilder_itemport_118.minSize = 1
    shipBuilder_itemport_118.parentItem = None
    shipBuilder_itemport_118.portClass = 0
    shipBuilder_itemport_118.disabled = False
    shipBuilder_itemport_118 = save_or_locate(shipBuilder_itemport_118)

    shipBuilder_itemport_118.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_119 = ItemPort()
    shipBuilder_itemport_119.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_119.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_119.flags = u'upper right wing'
    shipBuilder_itemport_119.maxSize = 3
    shipBuilder_itemport_119.minSize = 1
    shipBuilder_itemport_119.parentItem = None
    shipBuilder_itemport_119.portClass = 0
    shipBuilder_itemport_119.disabled = False
    shipBuilder_itemport_119 = save_or_locate(shipBuilder_itemport_119)

    shipBuilder_itemport_119.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_120 = ItemPort()
    shipBuilder_itemport_120.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_120.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_120.flags = u'right wing'
    shipBuilder_itemport_120.maxSize = 3
    shipBuilder_itemport_120.minSize = 1
    shipBuilder_itemport_120.parentItem = None
    shipBuilder_itemport_120.portClass = 0
    shipBuilder_itemport_120.disabled = False
    shipBuilder_itemport_120 = save_or_locate(shipBuilder_itemport_120)

    shipBuilder_itemport_120.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_121 = ItemPort()
    shipBuilder_itemport_121.displayName = u'Power Plant'
    shipBuilder_itemport_121.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_121.flags = u'main rear'
    shipBuilder_itemport_121.maxSize = 4
    shipBuilder_itemport_121.minSize = 3
    shipBuilder_itemport_121.parentItem = None
    shipBuilder_itemport_121.portClass = 0
    shipBuilder_itemport_121.disabled = False
    shipBuilder_itemport_121 = save_or_locate(shipBuilder_itemport_121)

    shipBuilder_itemport_121.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_122 = ItemPort()
    shipBuilder_itemport_122.displayName = u'Engine Attach'
    shipBuilder_itemport_122.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_122.flags = u'main rear'
    shipBuilder_itemport_122.maxSize = 4
    shipBuilder_itemport_122.minSize = 3
    shipBuilder_itemport_122.parentItem = None
    shipBuilder_itemport_122.portClass = 0
    shipBuilder_itemport_122.disabled = False
    shipBuilder_itemport_122 = save_or_locate(shipBuilder_itemport_122)

    shipBuilder_itemport_122.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_123 = ItemPort()
    shipBuilder_itemport_123.displayName = u'Thruster Rear Right Bottom'
    shipBuilder_itemport_123.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_123.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_123.maxSize = 1
    shipBuilder_itemport_123.minSize = 1
    shipBuilder_itemport_123.parentItem = None
    shipBuilder_itemport_123.portClass = 0
    shipBuilder_itemport_123.disabled = False
    shipBuilder_itemport_123 = save_or_locate(shipBuilder_itemport_123)

    shipBuilder_itemport_123.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_124 = ItemPort()
    shipBuilder_itemport_124.displayName = u'Thruster Rear Right Mid'
    shipBuilder_itemport_124.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_124.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_124.maxSize = 1
    shipBuilder_itemport_124.minSize = 1
    shipBuilder_itemport_124.parentItem = None
    shipBuilder_itemport_124.portClass = 0
    shipBuilder_itemport_124.disabled = False
    shipBuilder_itemport_124 = save_or_locate(shipBuilder_itemport_124)

    shipBuilder_itemport_124.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_125 = ItemPort()
    shipBuilder_itemport_125.displayName = u'Thruster Rear Right Upper'
    shipBuilder_itemport_125.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_125.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_125.maxSize = 1
    shipBuilder_itemport_125.minSize = 1
    shipBuilder_itemport_125.parentItem = None
    shipBuilder_itemport_125.portClass = 0
    shipBuilder_itemport_125.disabled = False
    shipBuilder_itemport_125 = save_or_locate(shipBuilder_itemport_125)

    shipBuilder_itemport_125.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_126 = ItemPort()
    shipBuilder_itemport_126.displayName = u'Thruster Rear Left Bottom'
    shipBuilder_itemport_126.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_126.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_126.maxSize = 1
    shipBuilder_itemport_126.minSize = 1
    shipBuilder_itemport_126.parentItem = None
    shipBuilder_itemport_126.portClass = 0
    shipBuilder_itemport_126.disabled = False
    shipBuilder_itemport_126 = save_or_locate(shipBuilder_itemport_126)

    shipBuilder_itemport_126.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_127 = ItemPort()
    shipBuilder_itemport_127.displayName = u'Thruster Rear Left Mid'
    shipBuilder_itemport_127.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_127.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_127.maxSize = 1
    shipBuilder_itemport_127.minSize = 1
    shipBuilder_itemport_127.parentItem = None
    shipBuilder_itemport_127.portClass = 0
    shipBuilder_itemport_127.disabled = False
    shipBuilder_itemport_127 = save_or_locate(shipBuilder_itemport_127)

    shipBuilder_itemport_127.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_128 = ItemPort()
    shipBuilder_itemport_128.displayName = u'Thruster Rear Left Upper'
    shipBuilder_itemport_128.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_128.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_128.maxSize = 1
    shipBuilder_itemport_128.minSize = 1
    shipBuilder_itemport_128.parentItem = None
    shipBuilder_itemport_128.portClass = 0
    shipBuilder_itemport_128.disabled = False
    shipBuilder_itemport_128 = save_or_locate(shipBuilder_itemport_128)

    shipBuilder_itemport_128.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_129 = ItemPort()
    shipBuilder_itemport_129.displayName = u'Thruster Front Right Bottom'
    shipBuilder_itemport_129.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_129.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_129.maxSize = 1
    shipBuilder_itemport_129.minSize = 1
    shipBuilder_itemport_129.parentItem = None
    shipBuilder_itemport_129.portClass = 0
    shipBuilder_itemport_129.disabled = False
    shipBuilder_itemport_129 = save_or_locate(shipBuilder_itemport_129)

    shipBuilder_itemport_129.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_130 = ItemPort()
    shipBuilder_itemport_130.displayName = u'Thruster Front Right Upper'
    shipBuilder_itemport_130.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_130.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_130.maxSize = 1
    shipBuilder_itemport_130.minSize = 1
    shipBuilder_itemport_130.parentItem = None
    shipBuilder_itemport_130.portClass = 0
    shipBuilder_itemport_130.disabled = False
    shipBuilder_itemport_130 = save_or_locate(shipBuilder_itemport_130)

    shipBuilder_itemport_130.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_131 = ItemPort()
    shipBuilder_itemport_131.displayName = u'Thruster Front Right Mid'
    shipBuilder_itemport_131.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_131.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_131.maxSize = 1
    shipBuilder_itemport_131.minSize = 1
    shipBuilder_itemport_131.parentItem = None
    shipBuilder_itemport_131.portClass = 0
    shipBuilder_itemport_131.disabled = False
    shipBuilder_itemport_131 = save_or_locate(shipBuilder_itemport_131)

    shipBuilder_itemport_131.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_132 = ItemPort()
    shipBuilder_itemport_132.displayName = u'Thruster Front Left Bottom'
    shipBuilder_itemport_132.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_132.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_132.maxSize = 1
    shipBuilder_itemport_132.minSize = 1
    shipBuilder_itemport_132.parentItem = None
    shipBuilder_itemport_132.portClass = 0
    shipBuilder_itemport_132.disabled = False
    shipBuilder_itemport_132 = save_or_locate(shipBuilder_itemport_132)

    shipBuilder_itemport_132.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_133 = ItemPort()
    shipBuilder_itemport_133.displayName = u'Thruster Front Left Upper'
    shipBuilder_itemport_133.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_133.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_133.maxSize = 1
    shipBuilder_itemport_133.minSize = 1
    shipBuilder_itemport_133.parentItem = None
    shipBuilder_itemport_133.portClass = 0
    shipBuilder_itemport_133.disabled = False
    shipBuilder_itemport_133 = save_or_locate(shipBuilder_itemport_133)

    shipBuilder_itemport_133.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_134 = ItemPort()
    shipBuilder_itemport_134.displayName = u'Thruster Front Left Mid'
    shipBuilder_itemport_134.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_134.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_134.maxSize = 1
    shipBuilder_itemport_134.minSize = 1
    shipBuilder_itemport_134.parentItem = None
    shipBuilder_itemport_134.portClass = 0
    shipBuilder_itemport_134.disabled = False
    shipBuilder_itemport_134 = save_or_locate(shipBuilder_itemport_134)

    shipBuilder_itemport_134.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_135 = ItemPort()
    shipBuilder_itemport_135.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_135.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_135.flags = u'nose'
    shipBuilder_itemport_135.maxSize = 2
    shipBuilder_itemport_135.minSize = 1
    shipBuilder_itemport_135.parentItem = None
    shipBuilder_itemport_135.portClass = 0
    shipBuilder_itemport_135.disabled = False
    shipBuilder_itemport_135 = save_or_locate(shipBuilder_itemport_135)

    shipBuilder_itemport_135.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_136 = ItemPort()
    shipBuilder_itemport_136.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_136.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_136.flags = u'upper left wing'
    shipBuilder_itemport_136.maxSize = 3
    shipBuilder_itemport_136.minSize = 1
    shipBuilder_itemport_136.parentItem = None
    shipBuilder_itemport_136.portClass = 0
    shipBuilder_itemport_136.disabled = False
    shipBuilder_itemport_136 = save_or_locate(shipBuilder_itemport_136)

    shipBuilder_itemport_136.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_137 = ItemPort()
    shipBuilder_itemport_137.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_137.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_137.flags = u'left wing'
    shipBuilder_itemport_137.maxSize = 3
    shipBuilder_itemport_137.minSize = 1
    shipBuilder_itemport_137.parentItem = None
    shipBuilder_itemport_137.portClass = 0
    shipBuilder_itemport_137.disabled = False
    shipBuilder_itemport_137 = save_or_locate(shipBuilder_itemport_137)

    shipBuilder_itemport_137.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_138 = ItemPort()
    shipBuilder_itemport_138.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_138.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_138.flags = u'upper right wing'
    shipBuilder_itemport_138.maxSize = 3
    shipBuilder_itemport_138.minSize = 1
    shipBuilder_itemport_138.parentItem = None
    shipBuilder_itemport_138.portClass = 0
    shipBuilder_itemport_138.disabled = False
    shipBuilder_itemport_138 = save_or_locate(shipBuilder_itemport_138)

    shipBuilder_itemport_138.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_139 = ItemPort()
    shipBuilder_itemport_139.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_139.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_139.flags = u'right wing'
    shipBuilder_itemport_139.maxSize = 3
    shipBuilder_itemport_139.minSize = 1
    shipBuilder_itemport_139.parentItem = None
    shipBuilder_itemport_139.portClass = 0
    shipBuilder_itemport_139.disabled = False
    shipBuilder_itemport_139 = save_or_locate(shipBuilder_itemport_139)

    shipBuilder_itemport_139.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_140 = ItemPort()
    shipBuilder_itemport_140.displayName = u'Power Plant'
    shipBuilder_itemport_140.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_140.flags = u'main rear'
    shipBuilder_itemport_140.maxSize = 2
    shipBuilder_itemport_140.minSize = 1
    shipBuilder_itemport_140.parentItem = None
    shipBuilder_itemport_140.portClass = 0
    shipBuilder_itemport_140.disabled = False
    shipBuilder_itemport_140 = save_or_locate(shipBuilder_itemport_140)

    shipBuilder_itemport_140.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_141 = ItemPort()
    shipBuilder_itemport_141.displayName = u'Engine Attach'
    shipBuilder_itemport_141.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_141.flags = u'main rear'
    shipBuilder_itemport_141.maxSize = 3
    shipBuilder_itemport_141.minSize = 2
    shipBuilder_itemport_141.parentItem = None
    shipBuilder_itemport_141.portClass = 0
    shipBuilder_itemport_141.disabled = False
    shipBuilder_itemport_141 = save_or_locate(shipBuilder_itemport_141)

    shipBuilder_itemport_141.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_142 = ItemPort()
    shipBuilder_itemport_142.displayName = u'Thruster Rear Mid Right'
    shipBuilder_itemport_142.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_142.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_142.maxSize = 1
    shipBuilder_itemport_142.minSize = 1
    shipBuilder_itemport_142.parentItem = None
    shipBuilder_itemport_142.portClass = 0
    shipBuilder_itemport_142.disabled = False
    shipBuilder_itemport_142 = save_or_locate(shipBuilder_itemport_142)

    shipBuilder_itemport_142.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_143 = ItemPort()
    shipBuilder_itemport_143.displayName = u'Thruster Rear Mid Left'
    shipBuilder_itemport_143.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_143.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_143.maxSize = 1
    shipBuilder_itemport_143.minSize = 1
    shipBuilder_itemport_143.parentItem = None
    shipBuilder_itemport_143.portClass = 0
    shipBuilder_itemport_143.disabled = False
    shipBuilder_itemport_143 = save_or_locate(shipBuilder_itemport_143)

    shipBuilder_itemport_143.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_144 = ItemPort()
    shipBuilder_itemport_144.displayName = u'Thruster Front Mid Right'
    shipBuilder_itemport_144.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_144.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_144.maxSize = 1
    shipBuilder_itemport_144.minSize = 1
    shipBuilder_itemport_144.parentItem = None
    shipBuilder_itemport_144.portClass = 0
    shipBuilder_itemport_144.disabled = False
    shipBuilder_itemport_144 = save_or_locate(shipBuilder_itemport_144)

    shipBuilder_itemport_144.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_145 = ItemPort()
    shipBuilder_itemport_145.displayName = u'Thruster Front Mid Left'
    shipBuilder_itemport_145.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_145.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_145.maxSize = 1
    shipBuilder_itemport_145.minSize = 1
    shipBuilder_itemport_145.parentItem = None
    shipBuilder_itemport_145.portClass = 0
    shipBuilder_itemport_145.disabled = False
    shipBuilder_itemport_145 = save_or_locate(shipBuilder_itemport_145)

    shipBuilder_itemport_145.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_146 = ItemPort()
    shipBuilder_itemport_146.displayName = u'Thruster Front Top'
    shipBuilder_itemport_146.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_146.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_146.maxSize = 1
    shipBuilder_itemport_146.minSize = 1
    shipBuilder_itemport_146.parentItem = None
    shipBuilder_itemport_146.portClass = 0
    shipBuilder_itemport_146.disabled = False
    shipBuilder_itemport_146 = save_or_locate(shipBuilder_itemport_146)

    shipBuilder_itemport_146.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_147 = ItemPort()
    shipBuilder_itemport_147.displayName = u'Thruster Front Bottom'
    shipBuilder_itemport_147.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_147.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_147.maxSize = 1
    shipBuilder_itemport_147.minSize = 1
    shipBuilder_itemport_147.parentItem = None
    shipBuilder_itemport_147.portClass = 0
    shipBuilder_itemport_147.disabled = False
    shipBuilder_itemport_147 = save_or_locate(shipBuilder_itemport_147)

    shipBuilder_itemport_147.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_148 = ItemPort()
    shipBuilder_itemport_148.displayName = u'Class 3 Slot'
    shipBuilder_itemport_148.name = u'hardpoint_class_3'
    shipBuilder_itemport_148.flags = u'top mid'
    shipBuilder_itemport_148.maxSize = 3
    shipBuilder_itemport_148.minSize = 1
    shipBuilder_itemport_148.parentItem = None
    shipBuilder_itemport_148.portClass = 0
    shipBuilder_itemport_148.disabled = False
    shipBuilder_itemport_148 = save_or_locate(shipBuilder_itemport_148)

    shipBuilder_itemport_148.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_149 = ItemPort()
    shipBuilder_itemport_149.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_149.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_149.flags = u'left'
    shipBuilder_itemport_149.maxSize = 2
    shipBuilder_itemport_149.minSize = 1
    shipBuilder_itemport_149.parentItem = None
    shipBuilder_itemport_149.portClass = 0
    shipBuilder_itemport_149.disabled = False
    shipBuilder_itemport_149 = save_or_locate(shipBuilder_itemport_149)

    shipBuilder_itemport_149.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_150 = ItemPort()
    shipBuilder_itemport_150.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_150.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_150.flags = u'right'
    shipBuilder_itemport_150.maxSize = 2
    shipBuilder_itemport_150.minSize = 1
    shipBuilder_itemport_150.parentItem = None
    shipBuilder_itemport_150.portClass = 0
    shipBuilder_itemport_150.disabled = False
    shipBuilder_itemport_150 = save_or_locate(shipBuilder_itemport_150)

    shipBuilder_itemport_150.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_151 = ItemPort()
    shipBuilder_itemport_151.displayName = u'Power Plant'
    shipBuilder_itemport_151.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_151.flags = u'main rear'
    shipBuilder_itemport_151.maxSize = 2
    shipBuilder_itemport_151.minSize = 1
    shipBuilder_itemport_151.parentItem = None
    shipBuilder_itemport_151.portClass = 0
    shipBuilder_itemport_151.disabled = False
    shipBuilder_itemport_151 = save_or_locate(shipBuilder_itemport_151)

    shipBuilder_itemport_151.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_152 = ItemPort()
    shipBuilder_itemport_152.displayName = u'Engine Attach'
    shipBuilder_itemport_152.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_152.flags = u'main rear'
    shipBuilder_itemport_152.maxSize = 3
    shipBuilder_itemport_152.minSize = 2
    shipBuilder_itemport_152.parentItem = None
    shipBuilder_itemport_152.portClass = 0
    shipBuilder_itemport_152.disabled = False
    shipBuilder_itemport_152 = save_or_locate(shipBuilder_itemport_152)

    shipBuilder_itemport_152.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_153 = ItemPort()
    shipBuilder_itemport_153.displayName = u'Thruster Rear Mid Right'
    shipBuilder_itemport_153.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_153.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_153.maxSize = 1
    shipBuilder_itemport_153.minSize = 1
    shipBuilder_itemport_153.parentItem = None
    shipBuilder_itemport_153.portClass = 0
    shipBuilder_itemport_153.disabled = False
    shipBuilder_itemport_153 = save_or_locate(shipBuilder_itemport_153)

    shipBuilder_itemport_153.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_154 = ItemPort()
    shipBuilder_itemport_154.displayName = u'Thruster Rear Mid Left'
    shipBuilder_itemport_154.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_154.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_154.maxSize = 1
    shipBuilder_itemport_154.minSize = 1
    shipBuilder_itemport_154.parentItem = None
    shipBuilder_itemport_154.portClass = 0
    shipBuilder_itemport_154.disabled = False
    shipBuilder_itemport_154 = save_or_locate(shipBuilder_itemport_154)

    shipBuilder_itemport_154.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_155 = ItemPort()
    shipBuilder_itemport_155.displayName = u'Thruster Front Mid Right'
    shipBuilder_itemport_155.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_155.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_155.maxSize = 1
    shipBuilder_itemport_155.minSize = 1
    shipBuilder_itemport_155.parentItem = None
    shipBuilder_itemport_155.portClass = 0
    shipBuilder_itemport_155.disabled = False
    shipBuilder_itemport_155 = save_or_locate(shipBuilder_itemport_155)

    shipBuilder_itemport_155.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_156 = ItemPort()
    shipBuilder_itemport_156.displayName = u'Thruster Front Mid Left'
    shipBuilder_itemport_156.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_156.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_156.maxSize = 1
    shipBuilder_itemport_156.minSize = 1
    shipBuilder_itemport_156.parentItem = None
    shipBuilder_itemport_156.portClass = 0
    shipBuilder_itemport_156.disabled = False
    shipBuilder_itemport_156 = save_or_locate(shipBuilder_itemport_156)

    shipBuilder_itemport_156.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_157 = ItemPort()
    shipBuilder_itemport_157.displayName = u'Thruster Front Top'
    shipBuilder_itemport_157.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_157.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_157.maxSize = 1
    shipBuilder_itemport_157.minSize = 1
    shipBuilder_itemport_157.parentItem = None
    shipBuilder_itemport_157.portClass = 0
    shipBuilder_itemport_157.disabled = False
    shipBuilder_itemport_157 = save_or_locate(shipBuilder_itemport_157)

    shipBuilder_itemport_157.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_158 = ItemPort()
    shipBuilder_itemport_158.displayName = u'Thruster Front Bottom'
    shipBuilder_itemport_158.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_158.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_158.maxSize = 1
    shipBuilder_itemport_158.minSize = 1
    shipBuilder_itemport_158.parentItem = None
    shipBuilder_itemport_158.portClass = 0
    shipBuilder_itemport_158.disabled = False
    shipBuilder_itemport_158 = save_or_locate(shipBuilder_itemport_158)

    shipBuilder_itemport_158.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_159 = ItemPort()
    shipBuilder_itemport_159.displayName = u'Class 3 Slot'
    shipBuilder_itemport_159.name = u'hardpoint_class_3'
    shipBuilder_itemport_159.flags = u'top mid'
    shipBuilder_itemport_159.maxSize = 3
    shipBuilder_itemport_159.minSize = 1
    shipBuilder_itemport_159.parentItem = None
    shipBuilder_itemport_159.portClass = 0
    shipBuilder_itemport_159.disabled = False
    shipBuilder_itemport_159 = save_or_locate(shipBuilder_itemport_159)

    shipBuilder_itemport_159.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_160 = ItemPort()
    shipBuilder_itemport_160.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_160.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_160.flags = u'left'
    shipBuilder_itemport_160.maxSize = 2
    shipBuilder_itemport_160.minSize = 1
    shipBuilder_itemport_160.parentItem = None
    shipBuilder_itemport_160.portClass = 0
    shipBuilder_itemport_160.disabled = False
    shipBuilder_itemport_160 = save_or_locate(shipBuilder_itemport_160)

    shipBuilder_itemport_160.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_161 = ItemPort()
    shipBuilder_itemport_161.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_161.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_161.flags = u'right'
    shipBuilder_itemport_161.maxSize = 2
    shipBuilder_itemport_161.minSize = 1
    shipBuilder_itemport_161.parentItem = None
    shipBuilder_itemport_161.portClass = 0
    shipBuilder_itemport_161.disabled = False
    shipBuilder_itemport_161 = save_or_locate(shipBuilder_itemport_161)

    shipBuilder_itemport_161.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_162 = ItemPort()
    shipBuilder_itemport_162.displayName = u'Power Plant'
    shipBuilder_itemport_162.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_162.flags = u'main rear'
    shipBuilder_itemport_162.maxSize = 2
    shipBuilder_itemport_162.minSize = 1
    shipBuilder_itemport_162.parentItem = None
    shipBuilder_itemport_162.portClass = 0
    shipBuilder_itemport_162.disabled = False
    shipBuilder_itemport_162 = save_or_locate(shipBuilder_itemport_162)

    shipBuilder_itemport_162.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_163 = ItemPort()
    shipBuilder_itemport_163.displayName = u'Engine Attach'
    shipBuilder_itemport_163.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_163.flags = u'main rear'
    shipBuilder_itemport_163.maxSize = 3
    shipBuilder_itemport_163.minSize = 2
    shipBuilder_itemport_163.parentItem = None
    shipBuilder_itemport_163.portClass = 0
    shipBuilder_itemport_163.disabled = False
    shipBuilder_itemport_163 = save_or_locate(shipBuilder_itemport_163)

    shipBuilder_itemport_163.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_164 = ItemPort()
    shipBuilder_itemport_164.displayName = u'Thruster Rear Mid Right'
    shipBuilder_itemport_164.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_164.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_164.maxSize = 1
    shipBuilder_itemport_164.minSize = 1
    shipBuilder_itemport_164.parentItem = None
    shipBuilder_itemport_164.portClass = 0
    shipBuilder_itemport_164.disabled = False
    shipBuilder_itemport_164 = save_or_locate(shipBuilder_itemport_164)

    shipBuilder_itemport_164.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_165 = ItemPort()
    shipBuilder_itemport_165.displayName = u'Thruster Rear Mid Left'
    shipBuilder_itemport_165.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_165.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_165.maxSize = 1
    shipBuilder_itemport_165.minSize = 1
    shipBuilder_itemport_165.parentItem = None
    shipBuilder_itemport_165.portClass = 0
    shipBuilder_itemport_165.disabled = False
    shipBuilder_itemport_165 = save_or_locate(shipBuilder_itemport_165)

    shipBuilder_itemport_165.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_166 = ItemPort()
    shipBuilder_itemport_166.displayName = u'Thruster Front Mid Right'
    shipBuilder_itemport_166.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_166.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_166.maxSize = 1
    shipBuilder_itemport_166.minSize = 1
    shipBuilder_itemport_166.parentItem = None
    shipBuilder_itemport_166.portClass = 0
    shipBuilder_itemport_166.disabled = False
    shipBuilder_itemport_166 = save_or_locate(shipBuilder_itemport_166)

    shipBuilder_itemport_166.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_167 = ItemPort()
    shipBuilder_itemport_167.displayName = u'Thruster Front Mid Left'
    shipBuilder_itemport_167.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_167.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_167.maxSize = 1
    shipBuilder_itemport_167.minSize = 1
    shipBuilder_itemport_167.parentItem = None
    shipBuilder_itemport_167.portClass = 0
    shipBuilder_itemport_167.disabled = False
    shipBuilder_itemport_167 = save_or_locate(shipBuilder_itemport_167)

    shipBuilder_itemport_167.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_168 = ItemPort()
    shipBuilder_itemport_168.displayName = u'Thruster Front Top'
    shipBuilder_itemport_168.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_168.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_168.maxSize = 1
    shipBuilder_itemport_168.minSize = 1
    shipBuilder_itemport_168.parentItem = None
    shipBuilder_itemport_168.portClass = 0
    shipBuilder_itemport_168.disabled = False
    shipBuilder_itemport_168 = save_or_locate(shipBuilder_itemport_168)

    shipBuilder_itemport_168.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_169 = ItemPort()
    shipBuilder_itemport_169.displayName = u'Thruster Front Bottom'
    shipBuilder_itemport_169.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_169.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_169.maxSize = 1
    shipBuilder_itemport_169.minSize = 1
    shipBuilder_itemport_169.parentItem = None
    shipBuilder_itemport_169.portClass = 0
    shipBuilder_itemport_169.disabled = False
    shipBuilder_itemport_169 = save_or_locate(shipBuilder_itemport_169)

    shipBuilder_itemport_169.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_170 = ItemPort()
    shipBuilder_itemport_170.displayName = u'Class 3 Slot'
    shipBuilder_itemport_170.name = u'hardpoint_class_3'
    shipBuilder_itemport_170.flags = u'top mid'
    shipBuilder_itemport_170.maxSize = 3
    shipBuilder_itemport_170.minSize = 2
    shipBuilder_itemport_170.parentItem = None
    shipBuilder_itemport_170.portClass = 0
    shipBuilder_itemport_170.disabled = False
    shipBuilder_itemport_170 = save_or_locate(shipBuilder_itemport_170)

    shipBuilder_itemport_170.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_171 = ItemPort()
    shipBuilder_itemport_171.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_171.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_171.flags = u'left'
    shipBuilder_itemport_171.maxSize = 2
    shipBuilder_itemport_171.minSize = 1
    shipBuilder_itemport_171.parentItem = None
    shipBuilder_itemport_171.portClass = 0
    shipBuilder_itemport_171.disabled = False
    shipBuilder_itemport_171 = save_or_locate(shipBuilder_itemport_171)

    shipBuilder_itemport_171.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_172 = ItemPort()
    shipBuilder_itemport_172.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_172.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_172.flags = u'right'
    shipBuilder_itemport_172.maxSize = 2
    shipBuilder_itemport_172.minSize = 1
    shipBuilder_itemport_172.parentItem = None
    shipBuilder_itemport_172.portClass = 0
    shipBuilder_itemport_172.disabled = False
    shipBuilder_itemport_172 = save_or_locate(shipBuilder_itemport_172)

    shipBuilder_itemport_172.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_173 = ItemPort()
    shipBuilder_itemport_173.displayName = u'Engine Attach'
    shipBuilder_itemport_173.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_173.flags = u'main rear'
    shipBuilder_itemport_173.maxSize = 3
    shipBuilder_itemport_173.minSize = 2
    shipBuilder_itemport_173.parentItem = None
    shipBuilder_itemport_173.portClass = 0
    shipBuilder_itemport_173.disabled = False
    shipBuilder_itemport_173 = save_or_locate(shipBuilder_itemport_173)

    shipBuilder_itemport_173.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_174 = ItemPort()
    shipBuilder_itemport_174.displayName = u'Thruster Rear Mid Right'
    shipBuilder_itemport_174.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_174.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_174.maxSize = 1
    shipBuilder_itemport_174.minSize = 1
    shipBuilder_itemport_174.parentItem = None
    shipBuilder_itemport_174.portClass = 0
    shipBuilder_itemport_174.disabled = False
    shipBuilder_itemport_174 = save_or_locate(shipBuilder_itemport_174)

    shipBuilder_itemport_174.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_175 = ItemPort()
    shipBuilder_itemport_175.displayName = u'Thruster Rear Mid Left'
    shipBuilder_itemport_175.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_175.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_175.maxSize = 1
    shipBuilder_itemport_175.minSize = 1
    shipBuilder_itemport_175.parentItem = None
    shipBuilder_itemport_175.portClass = 0
    shipBuilder_itemport_175.disabled = False
    shipBuilder_itemport_175 = save_or_locate(shipBuilder_itemport_175)

    shipBuilder_itemport_175.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_176 = ItemPort()
    shipBuilder_itemport_176.displayName = u'Thruster Front Mid Right'
    shipBuilder_itemport_176.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_176.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_176.maxSize = 1
    shipBuilder_itemport_176.minSize = 1
    shipBuilder_itemport_176.parentItem = None
    shipBuilder_itemport_176.portClass = 0
    shipBuilder_itemport_176.disabled = False
    shipBuilder_itemport_176 = save_or_locate(shipBuilder_itemport_176)

    shipBuilder_itemport_176.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_177 = ItemPort()
    shipBuilder_itemport_177.displayName = u'Thruster Front Mid Left'
    shipBuilder_itemport_177.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_177.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_177.maxSize = 1
    shipBuilder_itemport_177.minSize = 1
    shipBuilder_itemport_177.parentItem = None
    shipBuilder_itemport_177.portClass = 0
    shipBuilder_itemport_177.disabled = False
    shipBuilder_itemport_177 = save_or_locate(shipBuilder_itemport_177)

    shipBuilder_itemport_177.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_178 = ItemPort()
    shipBuilder_itemport_178.displayName = u'Thruster Front Top'
    shipBuilder_itemport_178.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_178.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_178.maxSize = 1
    shipBuilder_itemport_178.minSize = 1
    shipBuilder_itemport_178.parentItem = None
    shipBuilder_itemport_178.portClass = 0
    shipBuilder_itemport_178.disabled = False
    shipBuilder_itemport_178 = save_or_locate(shipBuilder_itemport_178)

    shipBuilder_itemport_178.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_179 = ItemPort()
    shipBuilder_itemport_179.displayName = u'Thruster Front Bottom'
    shipBuilder_itemport_179.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_179.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_179.maxSize = 2
    shipBuilder_itemport_179.minSize = 1
    shipBuilder_itemport_179.parentItem = None
    shipBuilder_itemport_179.portClass = 0
    shipBuilder_itemport_179.disabled = False
    shipBuilder_itemport_179 = save_or_locate(shipBuilder_itemport_179)

    shipBuilder_itemport_179.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_180 = ItemPort()
    shipBuilder_itemport_180.displayName = u'Class 3 Slot'
    shipBuilder_itemport_180.name = u'hardpoint_class_3'
    shipBuilder_itemport_180.flags = u'top mid'
    shipBuilder_itemport_180.maxSize = 3
    shipBuilder_itemport_180.minSize = 1
    shipBuilder_itemport_180.parentItem = None
    shipBuilder_itemport_180.portClass = 0
    shipBuilder_itemport_180.disabled = False
    shipBuilder_itemport_180 = save_or_locate(shipBuilder_itemport_180)

    shipBuilder_itemport_180.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_181 = ItemPort()
    shipBuilder_itemport_181.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_181.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_181.flags = u'left'
    shipBuilder_itemport_181.maxSize = 2
    shipBuilder_itemport_181.minSize = 1
    shipBuilder_itemport_181.parentItem = None
    shipBuilder_itemport_181.portClass = 0
    shipBuilder_itemport_181.disabled = False
    shipBuilder_itemport_181 = save_or_locate(shipBuilder_itemport_181)

    shipBuilder_itemport_181.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_182 = ItemPort()
    shipBuilder_itemport_182.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_182.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_182.flags = u'right'
    shipBuilder_itemport_182.maxSize = 2
    shipBuilder_itemport_182.minSize = 1
    shipBuilder_itemport_182.parentItem = None
    shipBuilder_itemport_182.portClass = 0
    shipBuilder_itemport_182.disabled = False
    shipBuilder_itemport_182 = save_or_locate(shipBuilder_itemport_182)

    shipBuilder_itemport_182.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_183 = ItemPort()
    shipBuilder_itemport_183.displayName = u'Class 2 Lower Left Nacelle'
    shipBuilder_itemport_183.name = u'Hardpoint_Class_2_Laser_bottom_left'
    shipBuilder_itemport_183.flags = u'Lower Left'
    shipBuilder_itemport_183.maxSize = 2
    shipBuilder_itemport_183.minSize = 1
    shipBuilder_itemport_183.parentItem = None
    shipBuilder_itemport_183.portClass = 0
    shipBuilder_itemport_183.disabled = False
    shipBuilder_itemport_183 = save_or_locate(shipBuilder_itemport_183)

    shipBuilder_itemport_183.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_184 = ItemPort()
    shipBuilder_itemport_184.displayName = u'Class 2 Upper Left Nacelle'
    shipBuilder_itemport_184.name = u'Hardpoint_Class_2_Laser_top_left'
    shipBuilder_itemport_184.flags = u'Upper Left'
    shipBuilder_itemport_184.maxSize = 2
    shipBuilder_itemport_184.minSize = 1
    shipBuilder_itemport_184.parentItem = None
    shipBuilder_itemport_184.portClass = 0
    shipBuilder_itemport_184.disabled = False
    shipBuilder_itemport_184 = save_or_locate(shipBuilder_itemport_184)

    shipBuilder_itemport_184.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_185 = ItemPort()
    shipBuilder_itemport_185.displayName = u'Class 2 Lower Right Nacelle'
    shipBuilder_itemport_185.name = u'Hardpoint_Class_2_Laser_bottom_right'
    shipBuilder_itemport_185.flags = u'Lower Right'
    shipBuilder_itemport_185.maxSize = 2
    shipBuilder_itemport_185.minSize = 1
    shipBuilder_itemport_185.parentItem = None
    shipBuilder_itemport_185.portClass = 0
    shipBuilder_itemport_185.disabled = False
    shipBuilder_itemport_185 = save_or_locate(shipBuilder_itemport_185)

    shipBuilder_itemport_185.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_186 = ItemPort()
    shipBuilder_itemport_186.displayName = u'Class 2 Upper Right Nacelle'
    shipBuilder_itemport_186.name = u'Hardpoint_Class_2_Laser_top_right'
    shipBuilder_itemport_186.flags = u'Upper Right'
    shipBuilder_itemport_186.maxSize = 2
    shipBuilder_itemport_186.minSize = 1
    shipBuilder_itemport_186.parentItem = None
    shipBuilder_itemport_186.portClass = 0
    shipBuilder_itemport_186.disabled = False
    shipBuilder_itemport_186 = save_or_locate(shipBuilder_itemport_186)

    shipBuilder_itemport_186.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_187 = ItemPort()
    shipBuilder_itemport_187.displayName = u'Top Turret Slot'
    shipBuilder_itemport_187.name = u'hardpoint_class_4_center'
    shipBuilder_itemport_187.flags = u'center'
    shipBuilder_itemport_187.maxSize = 4
    shipBuilder_itemport_187.minSize = 2
    shipBuilder_itemport_187.parentItem = None
    shipBuilder_itemport_187.portClass = 0
    shipBuilder_itemport_187.disabled = False
    shipBuilder_itemport_187 = save_or_locate(shipBuilder_itemport_187)

    shipBuilder_itemport_187.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_187.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_187.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_187.supportedTypes.add(shipBuilder_vehicleitemtype_12)

    shipBuilder_itemport_188 = ItemPort()
    shipBuilder_itemport_188.displayName = u'Left Bay Slot'
    shipBuilder_itemport_188.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_188.flags = u'left bottom'
    shipBuilder_itemport_188.maxSize = 3
    shipBuilder_itemport_188.minSize = 1
    shipBuilder_itemport_188.parentItem = None
    shipBuilder_itemport_188.portClass = 0
    shipBuilder_itemport_188.disabled = False
    shipBuilder_itemport_188 = save_or_locate(shipBuilder_itemport_188)

    shipBuilder_itemport_188.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_189 = ItemPort()
    shipBuilder_itemport_189.displayName = u'Right Bay Slot'
    shipBuilder_itemport_189.name = u'hardpoint_class_3_right_bay_door'
    shipBuilder_itemport_189.flags = u'right bottom'
    shipBuilder_itemport_189.maxSize = 3
    shipBuilder_itemport_189.minSize = 1
    shipBuilder_itemport_189.parentItem = None
    shipBuilder_itemport_189.portClass = 0
    shipBuilder_itemport_189.disabled = False
    shipBuilder_itemport_189 = save_or_locate(shipBuilder_itemport_189)

    shipBuilder_itemport_189.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_190 = ItemPort()
    shipBuilder_itemport_190.displayName = u'Front Slot'
    shipBuilder_itemport_190.name = u'hardpoint_class_4_nose'
    shipBuilder_itemport_190.flags = u'front nose'
    shipBuilder_itemport_190.maxSize = 3
    shipBuilder_itemport_190.minSize = 1
    shipBuilder_itemport_190.parentItem = None
    shipBuilder_itemport_190.portClass = 0
    shipBuilder_itemport_190.disabled = False
    shipBuilder_itemport_190 = save_or_locate(shipBuilder_itemport_190)

    shipBuilder_itemport_190.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_190.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_190.supportedTypes.add(shipBuilder_vehicleitemtype_6)

    shipBuilder_itemport_191 = ItemPort()
    shipBuilder_itemport_191.displayName = u'Left Display'
    shipBuilder_itemport_191.name = u'left_movil_lower_rotor'
    shipBuilder_itemport_191.flags = u'left lower'
    shipBuilder_itemport_191.maxSize = 1
    shipBuilder_itemport_191.minSize = 1
    shipBuilder_itemport_191.parentItem = None
    shipBuilder_itemport_191.portClass = 0
    shipBuilder_itemport_191.disabled = False
    shipBuilder_itemport_191 = save_or_locate(shipBuilder_itemport_191)

    shipBuilder_itemport_191.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_192 = ItemPort()
    shipBuilder_itemport_192.displayName = u'Right Display'
    shipBuilder_itemport_192.name = u'right_movil_lower_rotor'
    shipBuilder_itemport_192.flags = u'right lower'
    shipBuilder_itemport_192.maxSize = 1
    shipBuilder_itemport_192.minSize = 1
    shipBuilder_itemport_192.parentItem = None
    shipBuilder_itemport_192.portClass = 0
    shipBuilder_itemport_192.disabled = False
    shipBuilder_itemport_192 = save_or_locate(shipBuilder_itemport_192)

    shipBuilder_itemport_192.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_193 = ItemPort()
    shipBuilder_itemport_193.displayName = u'Top Left Display'
    shipBuilder_itemport_193.name = u'top_left_movil_lower_rotor'
    shipBuilder_itemport_193.flags = u'left upper'
    shipBuilder_itemport_193.maxSize = 1
    shipBuilder_itemport_193.minSize = 1
    shipBuilder_itemport_193.parentItem = None
    shipBuilder_itemport_193.portClass = 0
    shipBuilder_itemport_193.disabled = False
    shipBuilder_itemport_193 = save_or_locate(shipBuilder_itemport_193)

    shipBuilder_itemport_193.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_194 = ItemPort()
    shipBuilder_itemport_194.displayName = u'Top Right Display'
    shipBuilder_itemport_194.name = u'top_right_movil_lower_rotor'
    shipBuilder_itemport_194.flags = u'right upper'
    shipBuilder_itemport_194.maxSize = 1
    shipBuilder_itemport_194.minSize = 1
    shipBuilder_itemport_194.parentItem = None
    shipBuilder_itemport_194.portClass = 0
    shipBuilder_itemport_194.disabled = False
    shipBuilder_itemport_194 = save_or_locate(shipBuilder_itemport_194)

    shipBuilder_itemport_194.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_195 = ItemPort()
    shipBuilder_itemport_195.displayName = u'Right Nose Slot'
    shipBuilder_itemport_195.name = u'hardpoint_class_1_nose_right'
    shipBuilder_itemport_195.flags = u'nose right'
    shipBuilder_itemport_195.maxSize = 2
    shipBuilder_itemport_195.minSize = 1
    shipBuilder_itemport_195.parentItem = None
    shipBuilder_itemport_195.portClass = 0
    shipBuilder_itemport_195.disabled = False
    shipBuilder_itemport_195 = save_or_locate(shipBuilder_itemport_195)

    shipBuilder_itemport_195.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_196 = ItemPort()
    shipBuilder_itemport_196.displayName = u'Left Nose Slot'
    shipBuilder_itemport_196.name = u'hardpoint_class_1_nose_left'
    shipBuilder_itemport_196.flags = u'nose left'
    shipBuilder_itemport_196.maxSize = 2
    shipBuilder_itemport_196.minSize = 1
    shipBuilder_itemport_196.parentItem = None
    shipBuilder_itemport_196.portClass = 0
    shipBuilder_itemport_196.disabled = False
    shipBuilder_itemport_196 = save_or_locate(shipBuilder_itemport_196)

    shipBuilder_itemport_196.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_197 = ItemPort()
    shipBuilder_itemport_197.displayName = u'Left Wing Slot'
    shipBuilder_itemport_197.name = u'hardpoint_class_2_left_wing'
    shipBuilder_itemport_197.flags = u'left wing bottom'
    shipBuilder_itemport_197.maxSize = 3
    shipBuilder_itemport_197.minSize = 1
    shipBuilder_itemport_197.parentItem = None
    shipBuilder_itemport_197.portClass = 0
    shipBuilder_itemport_197.disabled = False
    shipBuilder_itemport_197 = save_or_locate(shipBuilder_itemport_197)

    shipBuilder_itemport_197.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_197.supportedTypes.add(shipBuilder_vehicleitemtype_5)

    shipBuilder_itemport_198 = ItemPort()
    shipBuilder_itemport_198.displayName = u'Right Wing Slot'
    shipBuilder_itemport_198.name = u'hardpoint_class_2_right_wing'
    shipBuilder_itemport_198.flags = u'right wing bottom'
    shipBuilder_itemport_198.maxSize = 3
    shipBuilder_itemport_198.minSize = 1
    shipBuilder_itemport_198.parentItem = None
    shipBuilder_itemport_198.portClass = 0
    shipBuilder_itemport_198.disabled = False
    shipBuilder_itemport_198 = save_or_locate(shipBuilder_itemport_198)

    shipBuilder_itemport_198.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_198.supportedTypes.add(shipBuilder_vehicleitemtype_5)

    shipBuilder_itemport_199 = ItemPort()
    shipBuilder_itemport_199.displayName = u'Power Plant'
    shipBuilder_itemport_199.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_199.flags = u''
    shipBuilder_itemport_199.maxSize = 3
    shipBuilder_itemport_199.minSize = 2
    shipBuilder_itemport_199.parentItem = None
    shipBuilder_itemport_199.portClass = 0
    shipBuilder_itemport_199.disabled = False
    shipBuilder_itemport_199 = save_or_locate(shipBuilder_itemport_199)

    shipBuilder_itemport_199.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_200 = ItemPort()
    shipBuilder_itemport_200.displayName = u'Engine Attach'
    shipBuilder_itemport_200.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_200.flags = u'main rear'
    shipBuilder_itemport_200.maxSize = 4
    shipBuilder_itemport_200.minSize = 3
    shipBuilder_itemport_200.parentItem = None
    shipBuilder_itemport_200.portClass = 0
    shipBuilder_itemport_200.disabled = False
    shipBuilder_itemport_200 = save_or_locate(shipBuilder_itemport_200)

    shipBuilder_itemport_200.supportedTypes.add(shipBuilder_vehicleitemtype_26)

    shipBuilder_itemport_201 = ItemPort()
    shipBuilder_itemport_201.displayName = u'Thruster Bottom Back Left'
    shipBuilder_itemport_201.name = u'hardpoint_thruster_bottom_back_left'
    shipBuilder_itemport_201.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_201.maxSize = 2
    shipBuilder_itemport_201.minSize = 1
    shipBuilder_itemport_201.parentItem = None
    shipBuilder_itemport_201.portClass = 0
    shipBuilder_itemport_201.disabled = False
    shipBuilder_itemport_201 = save_or_locate(shipBuilder_itemport_201)

    shipBuilder_itemport_201.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_202 = ItemPort()
    shipBuilder_itemport_202.displayName = u'Thruster Bottom Back Right'
    shipBuilder_itemport_202.name = u'hardpoint_thruster_bottom_back_right'
    shipBuilder_itemport_202.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_202.maxSize = 2
    shipBuilder_itemport_202.minSize = 1
    shipBuilder_itemport_202.parentItem = None
    shipBuilder_itemport_202.portClass = 0
    shipBuilder_itemport_202.disabled = False
    shipBuilder_itemport_202 = save_or_locate(shipBuilder_itemport_202)

    shipBuilder_itemport_202.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_203 = ItemPort()
    shipBuilder_itemport_203.displayName = u'Thruster Bottom Front Left'
    shipBuilder_itemport_203.name = u'hardpoint_thruster_bottom_front_left'
    shipBuilder_itemport_203.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_203.maxSize = 2
    shipBuilder_itemport_203.minSize = 1
    shipBuilder_itemport_203.parentItem = None
    shipBuilder_itemport_203.portClass = 0
    shipBuilder_itemport_203.disabled = False
    shipBuilder_itemport_203 = save_or_locate(shipBuilder_itemport_203)

    shipBuilder_itemport_203.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_204 = ItemPort()
    shipBuilder_itemport_204.displayName = u'Thruster Bottom Front Right'
    shipBuilder_itemport_204.name = u'hardpoint_thruster_bottom_front_right'
    shipBuilder_itemport_204.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_204.maxSize = 2
    shipBuilder_itemport_204.minSize = 1
    shipBuilder_itemport_204.parentItem = None
    shipBuilder_itemport_204.portClass = 0
    shipBuilder_itemport_204.disabled = False
    shipBuilder_itemport_204 = save_or_locate(shipBuilder_itemport_204)

    shipBuilder_itemport_204.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_205 = ItemPort()
    shipBuilder_itemport_205.displayName = u'Thruster Top Front Right'
    shipBuilder_itemport_205.name = u'hardpoint_thruster_top_front_right'
    shipBuilder_itemport_205.flags = u'maneuver orientation retro -X -Z upper front right'
    shipBuilder_itemport_205.maxSize = 2
    shipBuilder_itemport_205.minSize = 1
    shipBuilder_itemport_205.parentItem = None
    shipBuilder_itemport_205.portClass = 0
    shipBuilder_itemport_205.disabled = False
    shipBuilder_itemport_205 = save_or_locate(shipBuilder_itemport_205)

    shipBuilder_itemport_205.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_206 = ItemPort()
    shipBuilder_itemport_206.displayName = u'Thruster Top Front Left'
    shipBuilder_itemport_206.name = u'hardpoint_thruster_top_front_left'
    shipBuilder_itemport_206.flags = u'maneuver orientation retro +X -Z upper front left'
    shipBuilder_itemport_206.maxSize = 2
    shipBuilder_itemport_206.minSize = 1
    shipBuilder_itemport_206.parentItem = None
    shipBuilder_itemport_206.portClass = 0
    shipBuilder_itemport_206.disabled = False
    shipBuilder_itemport_206 = save_or_locate(shipBuilder_itemport_206)

    shipBuilder_itemport_206.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_207 = ItemPort()
    shipBuilder_itemport_207.displayName = u'Thruster Top Back Right'
    shipBuilder_itemport_207.name = u'hardpoint_thruster_top_back_right'
    shipBuilder_itemport_207.flags = u'maneuver orientation -X -Z upper rear right'
    shipBuilder_itemport_207.maxSize = 2
    shipBuilder_itemport_207.minSize = 1
    shipBuilder_itemport_207.parentItem = None
    shipBuilder_itemport_207.portClass = 0
    shipBuilder_itemport_207.disabled = False
    shipBuilder_itemport_207 = save_or_locate(shipBuilder_itemport_207)

    shipBuilder_itemport_207.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_208 = ItemPort()
    shipBuilder_itemport_208.displayName = u'Thruster Top Back Left'
    shipBuilder_itemport_208.name = u'hardpoint_thruster_top_back_left'
    shipBuilder_itemport_208.flags = u'maneuver orientation +X -Z upper rear left'
    shipBuilder_itemport_208.maxSize = 2
    shipBuilder_itemport_208.minSize = 1
    shipBuilder_itemport_208.parentItem = None
    shipBuilder_itemport_208.portClass = 0
    shipBuilder_itemport_208.disabled = False
    shipBuilder_itemport_208 = save_or_locate(shipBuilder_itemport_208)

    shipBuilder_itemport_208.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_209 = ItemPort()
    shipBuilder_itemport_209.displayName = u'Body Lights'
    shipBuilder_itemport_209.name = u'hardpoint_light_body'
    shipBuilder_itemport_209.flags = u'body'
    shipBuilder_itemport_209.maxSize = 1
    shipBuilder_itemport_209.minSize = 1
    shipBuilder_itemport_209.parentItem = None
    shipBuilder_itemport_209.portClass = 0
    shipBuilder_itemport_209.disabled = False
    shipBuilder_itemport_209 = save_or_locate(shipBuilder_itemport_209)

    shipBuilder_itemport_209.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_210 = ItemPort()
    shipBuilder_itemport_210.displayName = u'Top Turret Slot'
    shipBuilder_itemport_210.name = u'hardpoint_class_4_center'
    shipBuilder_itemport_210.flags = u'center'
    shipBuilder_itemport_210.maxSize = 4
    shipBuilder_itemport_210.minSize = 2
    shipBuilder_itemport_210.parentItem = None
    shipBuilder_itemport_210.portClass = 0
    shipBuilder_itemport_210.disabled = False
    shipBuilder_itemport_210 = save_or_locate(shipBuilder_itemport_210)

    shipBuilder_itemport_210.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_210.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_210.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_210.supportedTypes.add(shipBuilder_vehicleitemtype_12)

    shipBuilder_itemport_211 = ItemPort()
    shipBuilder_itemport_211.displayName = u'Lower Rear Left Thruster'
    shipBuilder_itemport_211.name = u'hardpoint_thruster_bottom_back_left'
    shipBuilder_itemport_211.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_211.maxSize = 2
    shipBuilder_itemport_211.minSize = 1
    shipBuilder_itemport_211.parentItem = None
    shipBuilder_itemport_211.portClass = 0
    shipBuilder_itemport_211.disabled = False
    shipBuilder_itemport_211 = save_or_locate(shipBuilder_itemport_211)

    shipBuilder_itemport_211.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_212 = ItemPort()
    shipBuilder_itemport_212.displayName = u'Lower Rear Right Thruster'
    shipBuilder_itemport_212.name = u'hardpoint_thruster_bottom_back_right'
    shipBuilder_itemport_212.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_212.maxSize = 2
    shipBuilder_itemport_212.minSize = 1
    shipBuilder_itemport_212.parentItem = None
    shipBuilder_itemport_212.portClass = 0
    shipBuilder_itemport_212.disabled = False
    shipBuilder_itemport_212 = save_or_locate(shipBuilder_itemport_212)

    shipBuilder_itemport_212.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_213 = ItemPort()
    shipBuilder_itemport_213.displayName = u'Lower Front Left Thruster'
    shipBuilder_itemport_213.name = u'hardpoint_thruster_bottom_front_left'
    shipBuilder_itemport_213.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_213.maxSize = 2
    shipBuilder_itemport_213.minSize = 1
    shipBuilder_itemport_213.parentItem = None
    shipBuilder_itemport_213.portClass = 0
    shipBuilder_itemport_213.disabled = False
    shipBuilder_itemport_213 = save_or_locate(shipBuilder_itemport_213)

    shipBuilder_itemport_213.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_214 = ItemPort()
    shipBuilder_itemport_214.displayName = u'Lower Front Right Thruster'
    shipBuilder_itemport_214.name = u'hardpoint_thruster_bottom_front_right'
    shipBuilder_itemport_214.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_214.maxSize = 2
    shipBuilder_itemport_214.minSize = 1
    shipBuilder_itemport_214.parentItem = None
    shipBuilder_itemport_214.portClass = 0
    shipBuilder_itemport_214.disabled = False
    shipBuilder_itemport_214 = save_or_locate(shipBuilder_itemport_214)

    shipBuilder_itemport_214.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_215 = ItemPort()
    shipBuilder_itemport_215.displayName = u'Upper Front Right Thruster'
    shipBuilder_itemport_215.name = u'hardpoint_thruster_top_front_right'
    shipBuilder_itemport_215.flags = u'maneuver orientation retro -X -Z upper front right'
    shipBuilder_itemport_215.maxSize = 2
    shipBuilder_itemport_215.minSize = 1
    shipBuilder_itemport_215.parentItem = None
    shipBuilder_itemport_215.portClass = 0
    shipBuilder_itemport_215.disabled = False
    shipBuilder_itemport_215 = save_or_locate(shipBuilder_itemport_215)

    shipBuilder_itemport_215.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_216 = ItemPort()
    shipBuilder_itemport_216.displayName = u'Upper Front Left Thruster'
    shipBuilder_itemport_216.name = u'hardpoint_thruster_top_front_left'
    shipBuilder_itemport_216.flags = u'maneuver orientation retro +X -Z upper front left'
    shipBuilder_itemport_216.maxSize = 2
    shipBuilder_itemport_216.minSize = 1
    shipBuilder_itemport_216.parentItem = None
    shipBuilder_itemport_216.portClass = 0
    shipBuilder_itemport_216.disabled = False
    shipBuilder_itemport_216 = save_or_locate(shipBuilder_itemport_216)

    shipBuilder_itemport_216.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_217 = ItemPort()
    shipBuilder_itemport_217.displayName = u'Upper Read Right Thruster'
    shipBuilder_itemport_217.name = u'hardpoint_thruster_top_back_right'
    shipBuilder_itemport_217.flags = u'maneuver orientation -X -Z upper rear right'
    shipBuilder_itemport_217.maxSize = 2
    shipBuilder_itemport_217.minSize = 1
    shipBuilder_itemport_217.parentItem = None
    shipBuilder_itemport_217.portClass = 0
    shipBuilder_itemport_217.disabled = False
    shipBuilder_itemport_217 = save_or_locate(shipBuilder_itemport_217)

    shipBuilder_itemport_217.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_218 = ItemPort()
    shipBuilder_itemport_218.displayName = u'Upper Read Left Thruster'
    shipBuilder_itemport_218.name = u'hardpoint_thruster_top_back_left'
    shipBuilder_itemport_218.flags = u'maneuver orientation +X -Z upper rear left'
    shipBuilder_itemport_218.maxSize = 2
    shipBuilder_itemport_218.minSize = 1
    shipBuilder_itemport_218.parentItem = None
    shipBuilder_itemport_218.portClass = 0
    shipBuilder_itemport_218.disabled = False
    shipBuilder_itemport_218 = save_or_locate(shipBuilder_itemport_218)

    shipBuilder_itemport_218.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_219 = ItemPort()
    shipBuilder_itemport_219.displayName = u'Nose Lights'
    shipBuilder_itemport_219.name = u'hardpoint_light_nose'
    shipBuilder_itemport_219.flags = u'nose'
    shipBuilder_itemport_219.maxSize = 1
    shipBuilder_itemport_219.minSize = 1
    shipBuilder_itemport_219.parentItem = None
    shipBuilder_itemport_219.portClass = 0
    shipBuilder_itemport_219.disabled = False
    shipBuilder_itemport_219 = save_or_locate(shipBuilder_itemport_219)

    shipBuilder_itemport_219.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_220 = ItemPort()
    shipBuilder_itemport_220.displayName = u'Nose Top Beacon Lights'
    shipBuilder_itemport_220.name = u'hardpoint_light_nose_dorsalbeacon'
    shipBuilder_itemport_220.flags = u'top'
    shipBuilder_itemport_220.maxSize = 1
    shipBuilder_itemport_220.minSize = 1
    shipBuilder_itemport_220.parentItem = None
    shipBuilder_itemport_220.portClass = 0
    shipBuilder_itemport_220.disabled = False
    shipBuilder_itemport_220 = save_or_locate(shipBuilder_itemport_220)

    shipBuilder_itemport_220.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_221 = ItemPort()
    shipBuilder_itemport_221.displayName = u'Nose Bottom Beacon Lights'
    shipBuilder_itemport_221.name = u'hardpoint_light_nose_ventralbeacon'
    shipBuilder_itemport_221.flags = u'bottom'
    shipBuilder_itemport_221.maxSize = 1
    shipBuilder_itemport_221.minSize = 1
    shipBuilder_itemport_221.parentItem = None
    shipBuilder_itemport_221.portClass = 0
    shipBuilder_itemport_221.disabled = False
    shipBuilder_itemport_221 = save_or_locate(shipBuilder_itemport_221)

    shipBuilder_itemport_221.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_222 = ItemPort()
    shipBuilder_itemport_222.displayName = u'Front Slot'
    shipBuilder_itemport_222.name = u'hardpoint_class_4_nose'
    shipBuilder_itemport_222.flags = u'front nose'
    shipBuilder_itemport_222.maxSize = 3
    shipBuilder_itemport_222.minSize = 1
    shipBuilder_itemport_222.parentItem = None
    shipBuilder_itemport_222.portClass = 0
    shipBuilder_itemport_222.disabled = False
    shipBuilder_itemport_222 = save_or_locate(shipBuilder_itemport_222)

    shipBuilder_itemport_222.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_222.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_222.supportedTypes.add(shipBuilder_vehicleitemtype_6)

    shipBuilder_itemport_223 = ItemPort()
    shipBuilder_itemport_223.displayName = u'Right Nose Slot'
    shipBuilder_itemport_223.name = u'hardpoint_class_1_nose_right'
    shipBuilder_itemport_223.flags = u'nose right'
    shipBuilder_itemport_223.maxSize = 2
    shipBuilder_itemport_223.minSize = 1
    shipBuilder_itemport_223.parentItem = None
    shipBuilder_itemport_223.portClass = 0
    shipBuilder_itemport_223.disabled = False
    shipBuilder_itemport_223 = save_or_locate(shipBuilder_itemport_223)

    shipBuilder_itemport_223.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_224 = ItemPort()
    shipBuilder_itemport_224.displayName = u'Left Nose Slot'
    shipBuilder_itemport_224.name = u'hardpoint_class_1_nose_left'
    shipBuilder_itemport_224.flags = u'nose left'
    shipBuilder_itemport_224.maxSize = 2
    shipBuilder_itemport_224.minSize = 1
    shipBuilder_itemport_224.parentItem = None
    shipBuilder_itemport_224.portClass = 0
    shipBuilder_itemport_224.disabled = False
    shipBuilder_itemport_224 = save_or_locate(shipBuilder_itemport_224)

    shipBuilder_itemport_224.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_225 = ItemPort()
    shipBuilder_itemport_225.displayName = u'Left Display'
    shipBuilder_itemport_225.name = u'left_movil_lower_rotor'
    shipBuilder_itemport_225.flags = u'left lower'
    shipBuilder_itemport_225.maxSize = 1
    shipBuilder_itemport_225.minSize = 1
    shipBuilder_itemport_225.parentItem = None
    shipBuilder_itemport_225.portClass = 0
    shipBuilder_itemport_225.disabled = False
    shipBuilder_itemport_225 = save_or_locate(shipBuilder_itemport_225)

    shipBuilder_itemport_225.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_226 = ItemPort()
    shipBuilder_itemport_226.displayName = u'Right Display'
    shipBuilder_itemport_226.name = u'right_movil_lower_rotor'
    shipBuilder_itemport_226.flags = u'right lower'
    shipBuilder_itemport_226.maxSize = 1
    shipBuilder_itemport_226.minSize = 1
    shipBuilder_itemport_226.parentItem = None
    shipBuilder_itemport_226.portClass = 0
    shipBuilder_itemport_226.disabled = False
    shipBuilder_itemport_226 = save_or_locate(shipBuilder_itemport_226)

    shipBuilder_itemport_226.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_227 = ItemPort()
    shipBuilder_itemport_227.displayName = u'Top Left Display'
    shipBuilder_itemport_227.name = u'top_left_movil_lower_rotor'
    shipBuilder_itemport_227.flags = u'left upper'
    shipBuilder_itemport_227.maxSize = 1
    shipBuilder_itemport_227.minSize = 1
    shipBuilder_itemport_227.parentItem = None
    shipBuilder_itemport_227.portClass = 0
    shipBuilder_itemport_227.disabled = False
    shipBuilder_itemport_227 = save_or_locate(shipBuilder_itemport_227)

    shipBuilder_itemport_227.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_228 = ItemPort()
    shipBuilder_itemport_228.displayName = u'Top Right Display'
    shipBuilder_itemport_228.name = u'top_right_movil_lower_rotor'
    shipBuilder_itemport_228.flags = u'right upper'
    shipBuilder_itemport_228.maxSize = 1
    shipBuilder_itemport_228.minSize = 1
    shipBuilder_itemport_228.parentItem = None
    shipBuilder_itemport_228.portClass = 0
    shipBuilder_itemport_228.disabled = False
    shipBuilder_itemport_228 = save_or_locate(shipBuilder_itemport_228)

    shipBuilder_itemport_228.supportedTypes.add(shipBuilder_vehicleitemtype_8)

    shipBuilder_itemport_229 = ItemPort()
    shipBuilder_itemport_229.displayName = u'Light Cockpit'
    shipBuilder_itemport_229.name = u'hardpoint_light_cockpit'
    shipBuilder_itemport_229.flags = u'cockpit'
    shipBuilder_itemport_229.maxSize = 1
    shipBuilder_itemport_229.minSize = 1
    shipBuilder_itemport_229.parentItem = None
    shipBuilder_itemport_229.portClass = 0
    shipBuilder_itemport_229.disabled = False
    shipBuilder_itemport_229 = save_or_locate(shipBuilder_itemport_229)

    shipBuilder_itemport_229.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_230 = ItemPort()
    shipBuilder_itemport_230.displayName = u'Left Bay Slot'
    shipBuilder_itemport_230.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_230.flags = u'left bottom'
    shipBuilder_itemport_230.maxSize = 3
    shipBuilder_itemport_230.minSize = 1
    shipBuilder_itemport_230.parentItem = None
    shipBuilder_itemport_230.portClass = 0
    shipBuilder_itemport_230.disabled = False
    shipBuilder_itemport_230 = save_or_locate(shipBuilder_itemport_230)

    shipBuilder_itemport_230.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_231 = ItemPort()
    shipBuilder_itemport_231.displayName = u'Right Bay Slot'
    shipBuilder_itemport_231.name = u'hardpoint_class_3_right_bay_door'
    shipBuilder_itemport_231.flags = u'right bottom'
    shipBuilder_itemport_231.maxSize = 3
    shipBuilder_itemport_231.minSize = 1
    shipBuilder_itemport_231.parentItem = None
    shipBuilder_itemport_231.portClass = 0
    shipBuilder_itemport_231.disabled = False
    shipBuilder_itemport_231 = save_or_locate(shipBuilder_itemport_231)

    shipBuilder_itemport_231.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_232 = ItemPort()
    shipBuilder_itemport_232.displayName = u'Left Wing Lights'
    shipBuilder_itemport_232.name = u'hardpoint_light_leftwing'
    shipBuilder_itemport_232.flags = u'leftwing'
    shipBuilder_itemport_232.maxSize = 1
    shipBuilder_itemport_232.minSize = 1
    shipBuilder_itemport_232.parentItem = None
    shipBuilder_itemport_232.portClass = 0
    shipBuilder_itemport_232.disabled = False
    shipBuilder_itemport_232 = save_or_locate(shipBuilder_itemport_232)

    shipBuilder_itemport_232.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_233 = ItemPort()
    shipBuilder_itemport_233.displayName = u'Left Wing Slot'
    shipBuilder_itemport_233.name = u'hardpoint_class_2_left_wing'
    shipBuilder_itemport_233.flags = u'left wing bottom'
    shipBuilder_itemport_233.maxSize = 3
    shipBuilder_itemport_233.minSize = 1
    shipBuilder_itemport_233.parentItem = None
    shipBuilder_itemport_233.portClass = 0
    shipBuilder_itemport_233.disabled = False
    shipBuilder_itemport_233 = save_or_locate(shipBuilder_itemport_233)

    shipBuilder_itemport_233.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_233.supportedTypes.add(shipBuilder_vehicleitemtype_5)

    shipBuilder_itemport_234 = ItemPort()
    shipBuilder_itemport_234.displayName = u'Left Wing Landing Lights'
    shipBuilder_itemport_234.name = u'hardpoint_light_leftwing_landing'
    shipBuilder_itemport_234.flags = u'left'
    shipBuilder_itemport_234.maxSize = 1
    shipBuilder_itemport_234.minSize = 1
    shipBuilder_itemport_234.parentItem = None
    shipBuilder_itemport_234.portClass = 0
    shipBuilder_itemport_234.disabled = False
    shipBuilder_itemport_234 = save_or_locate(shipBuilder_itemport_234)

    shipBuilder_itemport_234.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_235 = ItemPort()
    shipBuilder_itemport_235.displayName = u'Left Wing Strobe Lights'
    shipBuilder_itemport_235.name = u'hardpoint_light_leftwing_strobe'
    shipBuilder_itemport_235.flags = u'left'
    shipBuilder_itemport_235.maxSize = 1
    shipBuilder_itemport_235.minSize = 1
    shipBuilder_itemport_235.parentItem = None
    shipBuilder_itemport_235.portClass = 0
    shipBuilder_itemport_235.disabled = False
    shipBuilder_itemport_235 = save_or_locate(shipBuilder_itemport_235)

    shipBuilder_itemport_235.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_236 = ItemPort()
    shipBuilder_itemport_236.displayName = u'Left Wing Navigation Lights'
    shipBuilder_itemport_236.name = u'hardpoint_light_leftwing_navlight'
    shipBuilder_itemport_236.flags = u'left'
    shipBuilder_itemport_236.maxSize = 1
    shipBuilder_itemport_236.minSize = 1
    shipBuilder_itemport_236.parentItem = None
    shipBuilder_itemport_236.portClass = 0
    shipBuilder_itemport_236.disabled = False
    shipBuilder_itemport_236 = save_or_locate(shipBuilder_itemport_236)

    shipBuilder_itemport_236.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_237 = ItemPort()
    shipBuilder_itemport_237.displayName = u'Right Wing Lights'
    shipBuilder_itemport_237.name = u'hardpoint_light_rightwing'
    shipBuilder_itemport_237.flags = u'rightwing'
    shipBuilder_itemport_237.maxSize = 1
    shipBuilder_itemport_237.minSize = 1
    shipBuilder_itemport_237.parentItem = None
    shipBuilder_itemport_237.portClass = 0
    shipBuilder_itemport_237.disabled = False
    shipBuilder_itemport_237 = save_or_locate(shipBuilder_itemport_237)

    shipBuilder_itemport_237.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_238 = ItemPort()
    shipBuilder_itemport_238.displayName = u'Right Wing Slot'
    shipBuilder_itemport_238.name = u'hardpoint_class_2_right_wing'
    shipBuilder_itemport_238.flags = u'right wing bottom'
    shipBuilder_itemport_238.maxSize = 3
    shipBuilder_itemport_238.minSize = 1
    shipBuilder_itemport_238.parentItem = None
    shipBuilder_itemport_238.portClass = 0
    shipBuilder_itemport_238.disabled = False
    shipBuilder_itemport_238 = save_or_locate(shipBuilder_itemport_238)

    shipBuilder_itemport_238.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_238.supportedTypes.add(shipBuilder_vehicleitemtype_5)

    shipBuilder_itemport_239 = ItemPort()
    shipBuilder_itemport_239.displayName = u'Right Wing Landing Lights'
    shipBuilder_itemport_239.name = u'hardpoint_light_rightwing_landing'
    shipBuilder_itemport_239.flags = u'right'
    shipBuilder_itemport_239.maxSize = 1
    shipBuilder_itemport_239.minSize = 1
    shipBuilder_itemport_239.parentItem = None
    shipBuilder_itemport_239.portClass = 0
    shipBuilder_itemport_239.disabled = False
    shipBuilder_itemport_239 = save_or_locate(shipBuilder_itemport_239)

    shipBuilder_itemport_239.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_240 = ItemPort()
    shipBuilder_itemport_240.displayName = u'Right Wing Strobe Lights'
    shipBuilder_itemport_240.name = u'hardpoint_light_rightwing_strobe'
    shipBuilder_itemport_240.flags = u'right'
    shipBuilder_itemport_240.maxSize = 1
    shipBuilder_itemport_240.minSize = 1
    shipBuilder_itemport_240.parentItem = None
    shipBuilder_itemport_240.portClass = 0
    shipBuilder_itemport_240.disabled = False
    shipBuilder_itemport_240 = save_or_locate(shipBuilder_itemport_240)

    shipBuilder_itemport_240.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_241 = ItemPort()
    shipBuilder_itemport_241.displayName = u'Right Wing Navigation Lights'
    shipBuilder_itemport_241.name = u'hardpoint_light_rightwing_navlight'
    shipBuilder_itemport_241.flags = u'right'
    shipBuilder_itemport_241.maxSize = 1
    shipBuilder_itemport_241.minSize = 1
    shipBuilder_itemport_241.parentItem = None
    shipBuilder_itemport_241.portClass = 0
    shipBuilder_itemport_241.disabled = False
    shipBuilder_itemport_241 = save_or_locate(shipBuilder_itemport_241)

    shipBuilder_itemport_241.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_242 = ItemPort()
    shipBuilder_itemport_242.displayName = u'Power Plant'
    shipBuilder_itemport_242.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_242.flags = u''
    shipBuilder_itemport_242.maxSize = 3
    shipBuilder_itemport_242.minSize = 2
    shipBuilder_itemport_242.parentItem = None
    shipBuilder_itemport_242.portClass = 0
    shipBuilder_itemport_242.disabled = False
    shipBuilder_itemport_242 = save_or_locate(shipBuilder_itemport_242)

    shipBuilder_itemport_242.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_243 = ItemPort()
    shipBuilder_itemport_243.displayName = u'Main Thruster'
    shipBuilder_itemport_243.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_243.flags = u'main rear'
    shipBuilder_itemport_243.maxSize = 4
    shipBuilder_itemport_243.minSize = 3
    shipBuilder_itemport_243.parentItem = None
    shipBuilder_itemport_243.portClass = 0
    shipBuilder_itemport_243.disabled = False
    shipBuilder_itemport_243 = save_or_locate(shipBuilder_itemport_243)

    shipBuilder_itemport_243.supportedTypes.add(shipBuilder_vehicleitemtype_26)

    shipBuilder_itemport_244 = ItemPort()
    shipBuilder_itemport_244.displayName = u'Tail Lights'
    shipBuilder_itemport_244.name = u'hardpoint_light_tail'
    shipBuilder_itemport_244.flags = u'tail'
    shipBuilder_itemport_244.maxSize = 1
    shipBuilder_itemport_244.minSize = 1
    shipBuilder_itemport_244.parentItem = None
    shipBuilder_itemport_244.portClass = 0
    shipBuilder_itemport_244.disabled = False
    shipBuilder_itemport_244 = save_or_locate(shipBuilder_itemport_244)

    shipBuilder_itemport_244.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_245 = ItemPort()
    shipBuilder_itemport_245.displayName = u'Turretmount'
    shipBuilder_itemport_245.name = u'TurretMount'
    shipBuilder_itemport_245.flags = u'turret_base'
    shipBuilder_itemport_245.maxSize = 1
    shipBuilder_itemport_245.minSize = 1
    shipBuilder_itemport_245.parentVehicle = None
    shipBuilder_itemport_245.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_itemport_245.portClass = 0
    shipBuilder_itemport_245.disabled = False
    shipBuilder_itemport_245 = save_or_locate(shipBuilder_itemport_245)

    shipBuilder_itemport_245.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_246 = ItemPort()
    shipBuilder_itemport_246.displayName = u'Ballturret'
    shipBuilder_itemport_246.name = u'Ballturret'
    shipBuilder_itemport_246.flags = u'turret'
    shipBuilder_itemport_246.maxSize = 1
    shipBuilder_itemport_246.minSize = 1
    shipBuilder_itemport_246.parentVehicle = None
    shipBuilder_itemport_246.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_itemport_246.portClass = 0
    shipBuilder_itemport_246.disabled = False
    shipBuilder_itemport_246 = save_or_locate(shipBuilder_itemport_246)

    shipBuilder_itemport_246.supportedTypes.add(shipBuilder_vehicleitemtype_27)

    shipBuilder_itemport_247 = ItemPort()
    shipBuilder_itemport_247.displayName = u'Left Slot'
    shipBuilder_itemport_247.name = u'hardpoint_class_1_left'
    shipBuilder_itemport_247.flags = u'turret right'
    shipBuilder_itemport_247.maxSize = 4
    shipBuilder_itemport_247.minSize = 1
    shipBuilder_itemport_247.parentVehicle = None
    shipBuilder_itemport_247.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_itemport_247.portClass = 0
    shipBuilder_itemport_247.disabled = False
    shipBuilder_itemport_247 = save_or_locate(shipBuilder_itemport_247)

    shipBuilder_itemport_247.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_248 = ItemPort()
    shipBuilder_itemport_248.displayName = u'Right Slot'
    shipBuilder_itemport_248.name = u'hardpoint_class_1_right'
    shipBuilder_itemport_248.flags = u'turret left'
    shipBuilder_itemport_248.maxSize = 4
    shipBuilder_itemport_248.minSize = 1
    shipBuilder_itemport_248.parentVehicle = None
    shipBuilder_itemport_248.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_itemport_248.portClass = 0
    shipBuilder_itemport_248.disabled = False
    shipBuilder_itemport_248 = save_or_locate(shipBuilder_itemport_248)

    shipBuilder_itemport_248.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_249 = ItemPort()
    shipBuilder_itemport_249.displayName = u'Left Slot'
    shipBuilder_itemport_249.name = u'hardpoint_class_1_left'
    shipBuilder_itemport_249.flags = u'right turret'
    shipBuilder_itemport_249.maxSize = 4
    shipBuilder_itemport_249.minSize = 1
    shipBuilder_itemport_249.parentVehicle = None
    shipBuilder_itemport_249.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_itemport_249.portClass = 0
    shipBuilder_itemport_249.disabled = False
    shipBuilder_itemport_249 = save_or_locate(shipBuilder_itemport_249)

    shipBuilder_itemport_249.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_250 = ItemPort()
    shipBuilder_itemport_250.displayName = u'Right Slot'
    shipBuilder_itemport_250.name = u'hardpoint_class_1_right'
    shipBuilder_itemport_250.flags = u'left turret'
    shipBuilder_itemport_250.maxSize = 4
    shipBuilder_itemport_250.minSize = 1
    shipBuilder_itemport_250.parentVehicle = None
    shipBuilder_itemport_250.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_itemport_250.portClass = 0
    shipBuilder_itemport_250.disabled = False
    shipBuilder_itemport_250 = save_or_locate(shipBuilder_itemport_250)

    shipBuilder_itemport_250.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_251 = ItemPort()
    shipBuilder_itemport_251.displayName = u'Power Plant'
    shipBuilder_itemport_251.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_251.flags = u'main rear'
    shipBuilder_itemport_251.maxSize = 3
    shipBuilder_itemport_251.minSize = 2
    shipBuilder_itemport_251.parentItem = None
    shipBuilder_itemport_251.portClass = 0
    shipBuilder_itemport_251.disabled = False
    shipBuilder_itemport_251 = save_or_locate(shipBuilder_itemport_251)

    shipBuilder_itemport_251.supportedTypes.add(shipBuilder_vehicleitemtype_10)

    shipBuilder_itemport_252 = ItemPort()
    shipBuilder_itemport_252.displayName = u'Engine Attach'
    shipBuilder_itemport_252.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_252.flags = u'main rear'
    shipBuilder_itemport_252.maxSize = 4
    shipBuilder_itemport_252.minSize = 3
    shipBuilder_itemport_252.parentItem = None
    shipBuilder_itemport_252.portClass = 0
    shipBuilder_itemport_252.disabled = False
    shipBuilder_itemport_252 = save_or_locate(shipBuilder_itemport_252)

    shipBuilder_itemport_252.supportedTypes.add(shipBuilder_vehicleitemtype_26)

    shipBuilder_itemport_253 = ItemPort()
    shipBuilder_itemport_253.displayName = u'Thruster Rear Right Bottom'
    shipBuilder_itemport_253.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_253.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_253.maxSize = 1
    shipBuilder_itemport_253.minSize = 1
    shipBuilder_itemport_253.parentItem = None
    shipBuilder_itemport_253.portClass = 0
    shipBuilder_itemport_253.disabled = False
    shipBuilder_itemport_253 = save_or_locate(shipBuilder_itemport_253)

    shipBuilder_itemport_253.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_254 = ItemPort()
    shipBuilder_itemport_254.displayName = u'Thruster Rear Right Mid'
    shipBuilder_itemport_254.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_254.flags = u'maneuver orientation mid rear right'
    shipBuilder_itemport_254.maxSize = 1
    shipBuilder_itemport_254.minSize = 1
    shipBuilder_itemport_254.parentItem = None
    shipBuilder_itemport_254.portClass = 0
    shipBuilder_itemport_254.disabled = False
    shipBuilder_itemport_254 = save_or_locate(shipBuilder_itemport_254)

    shipBuilder_itemport_254.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_255 = ItemPort()
    shipBuilder_itemport_255.displayName = u'Thruster Rear Right Upper'
    shipBuilder_itemport_255.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_255.flags = u'maneuver orientation -Z upper rear right'
    shipBuilder_itemport_255.maxSize = 1
    shipBuilder_itemport_255.minSize = 1
    shipBuilder_itemport_255.parentItem = None
    shipBuilder_itemport_255.portClass = 0
    shipBuilder_itemport_255.disabled = False
    shipBuilder_itemport_255 = save_or_locate(shipBuilder_itemport_255)

    shipBuilder_itemport_255.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_256 = ItemPort()
    shipBuilder_itemport_256.displayName = u'Thruster Rear Left Bottom'
    shipBuilder_itemport_256.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_256.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_256.maxSize = 1
    shipBuilder_itemport_256.minSize = 1
    shipBuilder_itemport_256.parentItem = None
    shipBuilder_itemport_256.portClass = 0
    shipBuilder_itemport_256.disabled = False
    shipBuilder_itemport_256 = save_or_locate(shipBuilder_itemport_256)

    shipBuilder_itemport_256.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_257 = ItemPort()
    shipBuilder_itemport_257.displayName = u'Thruster Rear Left Mid'
    shipBuilder_itemport_257.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_257.flags = u'maneuver orientation mid rear left'
    shipBuilder_itemport_257.maxSize = 1
    shipBuilder_itemport_257.minSize = 1
    shipBuilder_itemport_257.parentItem = None
    shipBuilder_itemport_257.portClass = 0
    shipBuilder_itemport_257.disabled = False
    shipBuilder_itemport_257 = save_or_locate(shipBuilder_itemport_257)

    shipBuilder_itemport_257.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_258 = ItemPort()
    shipBuilder_itemport_258.displayName = u'Thruster Rear Left Upper'
    shipBuilder_itemport_258.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_258.flags = u'maneuver orientation -Z upper rear left'
    shipBuilder_itemport_258.maxSize = 1
    shipBuilder_itemport_258.minSize = 1
    shipBuilder_itemport_258.parentItem = None
    shipBuilder_itemport_258.portClass = 0
    shipBuilder_itemport_258.disabled = False
    shipBuilder_itemport_258 = save_or_locate(shipBuilder_itemport_258)

    shipBuilder_itemport_258.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_259 = ItemPort()
    shipBuilder_itemport_259.displayName = u'Thruster Front Right Bottom'
    shipBuilder_itemport_259.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_259.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_259.maxSize = 1
    shipBuilder_itemport_259.minSize = 1
    shipBuilder_itemport_259.parentItem = None
    shipBuilder_itemport_259.portClass = 0
    shipBuilder_itemport_259.disabled = False
    shipBuilder_itemport_259 = save_or_locate(shipBuilder_itemport_259)

    shipBuilder_itemport_259.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_260 = ItemPort()
    shipBuilder_itemport_260.displayName = u'Thruster Front Right Upper'
    shipBuilder_itemport_260.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_260.flags = u'maneuver orientation -Z retro upper front right'
    shipBuilder_itemport_260.maxSize = 1
    shipBuilder_itemport_260.minSize = 1
    shipBuilder_itemport_260.parentItem = None
    shipBuilder_itemport_260.portClass = 0
    shipBuilder_itemport_260.disabled = False
    shipBuilder_itemport_260 = save_or_locate(shipBuilder_itemport_260)

    shipBuilder_itemport_260.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_261 = ItemPort()
    shipBuilder_itemport_261.displayName = u'Thruster Front Right Mid'
    shipBuilder_itemport_261.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_261.flags = u'maneuver orientation retro mid front right'
    shipBuilder_itemport_261.maxSize = 1
    shipBuilder_itemport_261.minSize = 1
    shipBuilder_itemport_261.parentItem = None
    shipBuilder_itemport_261.portClass = 0
    shipBuilder_itemport_261.disabled = False
    shipBuilder_itemport_261 = save_or_locate(shipBuilder_itemport_261)

    shipBuilder_itemport_261.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_262 = ItemPort()
    shipBuilder_itemport_262.displayName = u'Thruster Front Left Bottom'
    shipBuilder_itemport_262.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_262.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_262.maxSize = 1
    shipBuilder_itemport_262.minSize = 1
    shipBuilder_itemport_262.parentItem = None
    shipBuilder_itemport_262.portClass = 0
    shipBuilder_itemport_262.disabled = False
    shipBuilder_itemport_262 = save_or_locate(shipBuilder_itemport_262)

    shipBuilder_itemport_262.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_263 = ItemPort()
    shipBuilder_itemport_263.displayName = u'Thruster Front Left Upper'
    shipBuilder_itemport_263.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_263.flags = u'maneuver orientation -Z retro upper front left'
    shipBuilder_itemport_263.maxSize = 1
    shipBuilder_itemport_263.minSize = 1
    shipBuilder_itemport_263.parentItem = None
    shipBuilder_itemport_263.portClass = 0
    shipBuilder_itemport_263.disabled = False
    shipBuilder_itemport_263 = save_or_locate(shipBuilder_itemport_263)

    shipBuilder_itemport_263.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_264 = ItemPort()
    shipBuilder_itemport_264.displayName = u'Thruster Front Left Mid'
    shipBuilder_itemport_264.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_264.flags = u'maneuver orientation retro mid front left'
    shipBuilder_itemport_264.maxSize = 1
    shipBuilder_itemport_264.minSize = 1
    shipBuilder_itemport_264.parentItem = None
    shipBuilder_itemport_264.portClass = 0
    shipBuilder_itemport_264.disabled = False
    shipBuilder_itemport_264 = save_or_locate(shipBuilder_itemport_264)

    shipBuilder_itemport_264.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_265 = ItemPort()
    shipBuilder_itemport_265.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_265.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_265.flags = u'nose'
    shipBuilder_itemport_265.maxSize = 2
    shipBuilder_itemport_265.minSize = 1
    shipBuilder_itemport_265.parentItem = None
    shipBuilder_itemport_265.portClass = 0
    shipBuilder_itemport_265.disabled = False
    shipBuilder_itemport_265 = save_or_locate(shipBuilder_itemport_265)

    shipBuilder_itemport_265.supportedTypes.add(shipBuilder_vehicleitemtype_15)

    shipBuilder_itemport_266 = ItemPort()
    shipBuilder_itemport_266.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_266.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_266.flags = u'upper left wing'
    shipBuilder_itemport_266.maxSize = 3
    shipBuilder_itemport_266.minSize = 1
    shipBuilder_itemport_266.parentItem = None
    shipBuilder_itemport_266.portClass = 0
    shipBuilder_itemport_266.disabled = False
    shipBuilder_itemport_266 = save_or_locate(shipBuilder_itemport_266)

    shipBuilder_itemport_266.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_267 = ItemPort()
    shipBuilder_itemport_267.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_267.name = u'left_wing_gun_hardpoint_mount'
    shipBuilder_itemport_267.flags = u'left wing'
    shipBuilder_itemport_267.maxSize = 3
    shipBuilder_itemport_267.minSize = 1
    shipBuilder_itemport_267.parentItem = None
    shipBuilder_itemport_267.portClass = 0
    shipBuilder_itemport_267.disabled = False
    shipBuilder_itemport_267 = save_or_locate(shipBuilder_itemport_267)

    shipBuilder_itemport_267.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_268 = ItemPort()
    shipBuilder_itemport_268.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_268.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_268.flags = u'upper right wing'
    shipBuilder_itemport_268.maxSize = 3
    shipBuilder_itemport_268.minSize = 1
    shipBuilder_itemport_268.parentItem = None
    shipBuilder_itemport_268.portClass = 0
    shipBuilder_itemport_268.disabled = False
    shipBuilder_itemport_268 = save_or_locate(shipBuilder_itemport_268)

    shipBuilder_itemport_268.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_269 = ItemPort()
    shipBuilder_itemport_269.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_269.name = u'right_wing_gun_hardpoint_mount'
    shipBuilder_itemport_269.flags = u'right wing'
    shipBuilder_itemport_269.maxSize = 3
    shipBuilder_itemport_269.minSize = 1
    shipBuilder_itemport_269.parentItem = None
    shipBuilder_itemport_269.portClass = 0
    shipBuilder_itemport_269.disabled = False
    shipBuilder_itemport_269 = save_or_locate(shipBuilder_itemport_269)

    shipBuilder_itemport_269.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_270 = ItemPort()
    shipBuilder_itemport_270.displayName = u'Engine Attach'
    shipBuilder_itemport_270.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_270.flags = u'main rear'
    shipBuilder_itemport_270.maxSize = 3
    shipBuilder_itemport_270.minSize = 2
    shipBuilder_itemport_270.parentItem = None
    shipBuilder_itemport_270.portClass = 0
    shipBuilder_itemport_270.disabled = False
    shipBuilder_itemport_270 = save_or_locate(shipBuilder_itemport_270)

    shipBuilder_itemport_270.supportedTypes.add(shipBuilder_vehicleitemtype_26)

    shipBuilder_itemport_271 = ItemPort()
    shipBuilder_itemport_271.displayName = u'Thruster Rear Mid Right'
    shipBuilder_itemport_271.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_271.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_271.maxSize = 1
    shipBuilder_itemport_271.minSize = 1
    shipBuilder_itemport_271.parentItem = None
    shipBuilder_itemport_271.portClass = 0
    shipBuilder_itemport_271.disabled = False
    shipBuilder_itemport_271 = save_or_locate(shipBuilder_itemport_271)

    shipBuilder_itemport_271.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_272 = ItemPort()
    shipBuilder_itemport_272.displayName = u'Thruster Rear Mid Left'
    shipBuilder_itemport_272.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_272.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_272.maxSize = 1
    shipBuilder_itemport_272.minSize = 1
    shipBuilder_itemport_272.parentItem = None
    shipBuilder_itemport_272.portClass = 0
    shipBuilder_itemport_272.disabled = False
    shipBuilder_itemport_272 = save_or_locate(shipBuilder_itemport_272)

    shipBuilder_itemport_272.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_273 = ItemPort()
    shipBuilder_itemport_273.displayName = u'Thruster Front Mid Right'
    shipBuilder_itemport_273.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_273.flags = u'maneuver orientation +Z -Z retro front mid right'
    shipBuilder_itemport_273.maxSize = 1
    shipBuilder_itemport_273.minSize = 1
    shipBuilder_itemport_273.parentItem = None
    shipBuilder_itemport_273.portClass = 0
    shipBuilder_itemport_273.disabled = False
    shipBuilder_itemport_273 = save_or_locate(shipBuilder_itemport_273)

    shipBuilder_itemport_273.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_274 = ItemPort()
    shipBuilder_itemport_274.displayName = u'Thruster Front Mid Left'
    shipBuilder_itemport_274.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_274.flags = u'maneuver orientation +Z -Z retro front mid left'
    shipBuilder_itemport_274.maxSize = 1
    shipBuilder_itemport_274.minSize = 1
    shipBuilder_itemport_274.parentItem = None
    shipBuilder_itemport_274.portClass = 0
    shipBuilder_itemport_274.disabled = False
    shipBuilder_itemport_274 = save_or_locate(shipBuilder_itemport_274)

    shipBuilder_itemport_274.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_275 = ItemPort()
    shipBuilder_itemport_275.displayName = u'Thruster Front Top'
    shipBuilder_itemport_275.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_275.flags = u'maneuver orientation retro +Z -Y front top'
    shipBuilder_itemport_275.maxSize = 1
    shipBuilder_itemport_275.minSize = 1
    shipBuilder_itemport_275.parentItem = None
    shipBuilder_itemport_275.portClass = 0
    shipBuilder_itemport_275.disabled = False
    shipBuilder_itemport_275 = save_or_locate(shipBuilder_itemport_275)

    shipBuilder_itemport_275.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_276 = ItemPort()
    shipBuilder_itemport_276.displayName = u'Thruster Front Bottom'
    shipBuilder_itemport_276.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_276.flags = u'maneuver orientation retro -Z -Y front bottom'
    shipBuilder_itemport_276.maxSize = 1
    shipBuilder_itemport_276.minSize = 1
    shipBuilder_itemport_276.parentItem = None
    shipBuilder_itemport_276.portClass = 0
    shipBuilder_itemport_276.disabled = False
    shipBuilder_itemport_276 = save_or_locate(shipBuilder_itemport_276)

    shipBuilder_itemport_276.supportedTypes.add(shipBuilder_vehicleitemtype_11)

    shipBuilder_itemport_277 = ItemPort()
    shipBuilder_itemport_277.displayName = u'Class 3 Slot'
    shipBuilder_itemport_277.name = u'hardpoint_class_3'
    shipBuilder_itemport_277.flags = u'top mid'
    shipBuilder_itemport_277.maxSize = 3
    shipBuilder_itemport_277.minSize = 1
    shipBuilder_itemport_277.parentItem = None
    shipBuilder_itemport_277.portClass = 0
    shipBuilder_itemport_277.disabled = False
    shipBuilder_itemport_277 = save_or_locate(shipBuilder_itemport_277)

    shipBuilder_itemport_277.supportedTypes.add(shipBuilder_vehicleitemtype_7)

    shipBuilder_itemport_278 = ItemPort()
    shipBuilder_itemport_278.displayName = u'Left Whisker Class 1 Slot'
    shipBuilder_itemport_278.name = u'hardpoint_class_1_left_whisker'
    shipBuilder_itemport_278.flags = u'left'
    shipBuilder_itemport_278.maxSize = 2
    shipBuilder_itemport_278.minSize = 1
    shipBuilder_itemport_278.parentItem = None
    shipBuilder_itemport_278.portClass = 0
    shipBuilder_itemport_278.disabled = False
    shipBuilder_itemport_278 = save_or_locate(shipBuilder_itemport_278)

    shipBuilder_itemport_278.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_279 = ItemPort()
    shipBuilder_itemport_279.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_279.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_279.flags = u'right'
    shipBuilder_itemport_279.maxSize = 2
    shipBuilder_itemport_279.minSize = 1
    shipBuilder_itemport_279.parentItem = None
    shipBuilder_itemport_279.portClass = 0
    shipBuilder_itemport_279.disabled = False
    shipBuilder_itemport_279 = save_or_locate(shipBuilder_itemport_279)

    shipBuilder_itemport_279.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_280 = ItemPort()
    shipBuilder_itemport_280.displayName = u'Left Wing Class 1 Slot'
    shipBuilder_itemport_280.name = u'hardpoint_wing_top_left'
    shipBuilder_itemport_280.flags = u'left'
    shipBuilder_itemport_280.maxSize = 3
    shipBuilder_itemport_280.minSize = 1
    shipBuilder_itemport_280.parentItem = None
    shipBuilder_itemport_280.portClass = 0
    shipBuilder_itemport_280.disabled = False
    shipBuilder_itemport_280 = save_or_locate(shipBuilder_itemport_280)

    shipBuilder_itemport_280.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_281 = ItemPort()
    shipBuilder_itemport_281.displayName = u'Right Wing Class 1 Slot'
    shipBuilder_itemport_281.name = u'hardpoint_wing_top_right'
    shipBuilder_itemport_281.flags = u'right'
    shipBuilder_itemport_281.maxSize = 3
    shipBuilder_itemport_281.minSize = 1
    shipBuilder_itemport_281.parentItem = None
    shipBuilder_itemport_281.portClass = 0
    shipBuilder_itemport_281.disabled = False
    shipBuilder_itemport_281 = save_or_locate(shipBuilder_itemport_281)

    shipBuilder_itemport_281.supportedTypes.add(shipBuilder_vehicleitemtype_9)

    shipBuilder_itemport_282 = ItemPort()
    shipBuilder_itemport_282.displayName = u'Pilot Seat'
    shipBuilder_itemport_282.name = u'hardpoint_pilot_chair'
    shipBuilder_itemport_282.flags = u'pilot'
    shipBuilder_itemport_282.maxSize = 1
    shipBuilder_itemport_282.minSize = 1
    shipBuilder_itemport_282.parentItem = None
    shipBuilder_itemport_282.portClass = 0
    shipBuilder_itemport_282.disabled = False
    shipBuilder_itemport_282 = save_or_locate(shipBuilder_itemport_282)

    shipBuilder_itemport_282.supportedTypes.add(shipBuilder_vehicleitemtype_28)

    shipBuilder_itemport_283 = ItemPort()
    shipBuilder_itemport_283.displayName = u'Top Turret'
    shipBuilder_itemport_283.name = u'const_ext_mesh_top_turret_cabin_interior'
    shipBuilder_itemport_283.flags = u'front nose'
    shipBuilder_itemport_283.maxSize = 3
    shipBuilder_itemport_283.minSize = 1
    shipBuilder_itemport_283.parentItem = None
    shipBuilder_itemport_283.portClass = 0
    shipBuilder_itemport_283.disabled = False
    shipBuilder_itemport_283 = save_or_locate(shipBuilder_itemport_283)

    shipBuilder_itemport_283.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_283.supportedTypes.add(shipBuilder_vehicleitemtype_5)

    shipBuilder_itemport_284 = ItemPort()
    shipBuilder_itemport_284.displayName = u'Bottom Turret'
    shipBuilder_itemport_284.name = u'const_ext_base_turret_down_elevator_06'
    shipBuilder_itemport_284.flags = u'front nose'
    shipBuilder_itemport_284.maxSize = 3
    shipBuilder_itemport_284.minSize = 1
    shipBuilder_itemport_284.parentItem = None
    shipBuilder_itemport_284.portClass = 0
    shipBuilder_itemport_284.disabled = False
    shipBuilder_itemport_284 = save_or_locate(shipBuilder_itemport_284)

    shipBuilder_itemport_284.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_284.supportedTypes.add(shipBuilder_vehicleitemtype_5)

    shipBuilder_itemport_285 = ItemPort()
    shipBuilder_itemport_285.displayName = u'Normal Turret Slot'
    shipBuilder_itemport_285.name = u'weapon_mount'
    shipBuilder_itemport_285.flags = u'center'
    shipBuilder_itemport_285.maxSize = 5
    shipBuilder_itemport_285.minSize = 1
    shipBuilder_itemport_285.parentItem = None
    shipBuilder_itemport_285.portClass = 0
    shipBuilder_itemport_285.disabled = False
    shipBuilder_itemport_285 = save_or_locate(shipBuilder_itemport_285)

    shipBuilder_itemport_285.supportedTypes.add(shipBuilder_vehicleitemtype_3)

    #Processing model: VehicleCategory

    from shipBuilder.models import VehicleCategory


    #Processing model: Vehicle

    from shipBuilder.models import Vehicle

    shipBuilder_vehicle_1 = Vehicle()
    shipBuilder_vehicle_1.vehicleClass = 2
    shipBuilder_vehicle_1.category = u'StarFighter'
    shipBuilder_vehicle_1.displayName = u'Anvil Hornet'
    shipBuilder_vehicle_1.name = u'Anvil_Hornet'
    shipBuilder_vehicle_1.views = 7
    shipBuilder_vehicle_1.upgradeSlots = 0
    shipBuilder_vehicle_1.maximum_crew = 1
    shipBuilder_vehicle_1.empty_mass = 0
    shipBuilder_vehicle_1.length = 0.0
    shipBuilder_vehicle_1.width = 0.0
    shipBuilder_vehicle_1.height = 0.0
    shipBuilder_vehicle_1.thumbnail = u''
    shipBuilder_vehicle_1.available = False
    shipBuilder_vehicle_1.manufacturer = None
    shipBuilder_vehicle_1.defaultVariant = None
    shipBuilder_vehicle_1 = save_or_locate(shipBuilder_vehicle_1)

    shipBuilder_vehicle_2 = Vehicle()
    shipBuilder_vehicle_2.vehicleClass = 2
    shipBuilder_vehicle_2.category = u'Star Fighter'
    shipBuilder_vehicle_2.displayName = u'Anvil Hornet F7C'
    shipBuilder_vehicle_2.name = u'Anvil_Hornet_F7C'
    shipBuilder_vehicle_2.views = 0
    shipBuilder_vehicle_2.upgradeSlots = 0
    shipBuilder_vehicle_2.maximum_crew = 1
    shipBuilder_vehicle_2.empty_mass = 0
    shipBuilder_vehicle_2.length = 0.0
    shipBuilder_vehicle_2.width = 0.0
    shipBuilder_vehicle_2.height = 0.0
    shipBuilder_vehicle_2.thumbnail = u''
    shipBuilder_vehicle_2.available = False
    shipBuilder_vehicle_2.manufacturer = None
    shipBuilder_vehicle_2.defaultVariant = None
    shipBuilder_vehicle_2 = save_or_locate(shipBuilder_vehicle_2)

    shipBuilder_vehicle_3 = Vehicle()
    shipBuilder_vehicle_3.vehicleClass = 3
    shipBuilder_vehicle_3.category = u'Transport'
    shipBuilder_vehicle_3.displayName = u'MISC Freelancer'
    shipBuilder_vehicle_3.name = u'MISC_Freelancer'
    shipBuilder_vehicle_3.views = 0
    shipBuilder_vehicle_3.upgradeSlots = 0
    shipBuilder_vehicle_3.maximum_crew = 1
    shipBuilder_vehicle_3.empty_mass = 0
    shipBuilder_vehicle_3.length = 0.0
    shipBuilder_vehicle_3.width = 0.0
    shipBuilder_vehicle_3.height = 0.0
    shipBuilder_vehicle_3.thumbnail = u''
    shipBuilder_vehicle_3.available = False
    shipBuilder_vehicle_3.manufacturer = None
    shipBuilder_vehicle_3.defaultVariant = None
    shipBuilder_vehicle_3 = save_or_locate(shipBuilder_vehicle_3)

    shipBuilder_vehicle_4 = Vehicle()
    shipBuilder_vehicle_4.vehicleClass = 3
    shipBuilder_vehicle_4.category = u'StarFighter'
    shipBuilder_vehicle_4.displayName = u'Origin JumpWorks 300i'
    shipBuilder_vehicle_4.name = u'OJ_300i'
    shipBuilder_vehicle_4.views = 0
    shipBuilder_vehicle_4.upgradeSlots = 0
    shipBuilder_vehicle_4.maximum_crew = 1
    shipBuilder_vehicle_4.empty_mass = 0
    shipBuilder_vehicle_4.length = 0.0
    shipBuilder_vehicle_4.width = 0.0
    shipBuilder_vehicle_4.height = 0.0
    shipBuilder_vehicle_4.thumbnail = u''
    shipBuilder_vehicle_4.available = False
    shipBuilder_vehicle_4.manufacturer = None
    shipBuilder_vehicle_4.defaultVariant = None
    shipBuilder_vehicle_4 = save_or_locate(shipBuilder_vehicle_4)

    shipBuilder_vehicle_5 = Vehicle()
    shipBuilder_vehicle_5.vehicleClass = 1
    shipBuilder_vehicle_5.category = u'StarFighter'
    shipBuilder_vehicle_5.displayName = u''
    shipBuilder_vehicle_5.name = u'OJ_315p'
    shipBuilder_vehicle_5.views = 0
    shipBuilder_vehicle_5.upgradeSlots = 0
    shipBuilder_vehicle_5.maximum_crew = 1
    shipBuilder_vehicle_5.empty_mass = 0
    shipBuilder_vehicle_5.length = 0.0
    shipBuilder_vehicle_5.width = 0.0
    shipBuilder_vehicle_5.height = 0.0
    shipBuilder_vehicle_5.thumbnail = u''
    shipBuilder_vehicle_5.available = False
    shipBuilder_vehicle_5.manufacturer = None
    shipBuilder_vehicle_5.defaultVariant = None
    shipBuilder_vehicle_5 = save_or_locate(shipBuilder_vehicle_5)

    shipBuilder_vehicle_6 = Vehicle()
    shipBuilder_vehicle_6.vehicleClass = 1
    shipBuilder_vehicle_6.category = u'StarFighter'
    shipBuilder_vehicle_6.displayName = u''
    shipBuilder_vehicle_6.name = u'OJ_325a'
    shipBuilder_vehicle_6.views = 0
    shipBuilder_vehicle_6.upgradeSlots = 0
    shipBuilder_vehicle_6.maximum_crew = 1
    shipBuilder_vehicle_6.empty_mass = 0
    shipBuilder_vehicle_6.length = 0.0
    shipBuilder_vehicle_6.width = 0.0
    shipBuilder_vehicle_6.height = 0.0
    shipBuilder_vehicle_6.thumbnail = u''
    shipBuilder_vehicle_6.available = False
    shipBuilder_vehicle_6.manufacturer = None
    shipBuilder_vehicle_6.defaultVariant = None
    shipBuilder_vehicle_6 = save_or_locate(shipBuilder_vehicle_6)

    shipBuilder_vehicle_7 = Vehicle()
    shipBuilder_vehicle_7.vehicleClass = 2
    shipBuilder_vehicle_7.category = u'Star Fighter'
    shipBuilder_vehicle_7.displayName = u'OJ 350 R'
    shipBuilder_vehicle_7.name = u'OJ_350r'
    shipBuilder_vehicle_7.views = 0
    shipBuilder_vehicle_7.upgradeSlots = 0
    shipBuilder_vehicle_7.maximum_crew = 1
    shipBuilder_vehicle_7.empty_mass = 0
    shipBuilder_vehicle_7.length = 0.0
    shipBuilder_vehicle_7.width = 0.0
    shipBuilder_vehicle_7.height = 0.0
    shipBuilder_vehicle_7.thumbnail = u''
    shipBuilder_vehicle_7.available = False
    shipBuilder_vehicle_7.manufacturer = None
    shipBuilder_vehicle_7.defaultVariant = None
    shipBuilder_vehicle_7 = save_or_locate(shipBuilder_vehicle_7)

    shipBuilder_vehicle_8 = Vehicle()
    shipBuilder_vehicle_8.vehicleClass = 1
    shipBuilder_vehicle_8.category = u'StarFighter'
    shipBuilder_vehicle_8.displayName = u'RSI Aurora CL'
    shipBuilder_vehicle_8.name = u'RSI_Aurora_CL'
    shipBuilder_vehicle_8.views = 0
    shipBuilder_vehicle_8.upgradeSlots = 0
    shipBuilder_vehicle_8.maximum_crew = 1
    shipBuilder_vehicle_8.empty_mass = 0
    shipBuilder_vehicle_8.length = 0.0
    shipBuilder_vehicle_8.width = 0.0
    shipBuilder_vehicle_8.height = 0.0
    shipBuilder_vehicle_8.thumbnail = u''
    shipBuilder_vehicle_8.available = False
    shipBuilder_vehicle_8.manufacturer = None
    shipBuilder_vehicle_8.defaultVariant = None
    shipBuilder_vehicle_8 = save_or_locate(shipBuilder_vehicle_8)

    shipBuilder_vehicle_9 = Vehicle()
    shipBuilder_vehicle_9.vehicleClass = 1
    shipBuilder_vehicle_9.category = u'StarFighter'
    shipBuilder_vehicle_9.displayName = u''
    shipBuilder_vehicle_9.name = u'RSI_Aurora_ES'
    shipBuilder_vehicle_9.views = 0
    shipBuilder_vehicle_9.upgradeSlots = 0
    shipBuilder_vehicle_9.maximum_crew = 1
    shipBuilder_vehicle_9.empty_mass = 0
    shipBuilder_vehicle_9.length = 0.0
    shipBuilder_vehicle_9.width = 0.0
    shipBuilder_vehicle_9.height = 0.0
    shipBuilder_vehicle_9.thumbnail = u''
    shipBuilder_vehicle_9.available = False
    shipBuilder_vehicle_9.manufacturer = None
    shipBuilder_vehicle_9.defaultVariant = None
    shipBuilder_vehicle_9 = save_or_locate(shipBuilder_vehicle_9)

    shipBuilder_vehicle_10 = Vehicle()
    shipBuilder_vehicle_10.vehicleClass = 1
    shipBuilder_vehicle_10.category = u'StarFighter'
    shipBuilder_vehicle_10.displayName = u''
    shipBuilder_vehicle_10.name = u'RSI_Aurora_LX'
    shipBuilder_vehicle_10.views = 0
    shipBuilder_vehicle_10.upgradeSlots = 0
    shipBuilder_vehicle_10.maximum_crew = 1
    shipBuilder_vehicle_10.empty_mass = 0
    shipBuilder_vehicle_10.length = 0.0
    shipBuilder_vehicle_10.width = 0.0
    shipBuilder_vehicle_10.height = 0.0
    shipBuilder_vehicle_10.thumbnail = u''
    shipBuilder_vehicle_10.available = False
    shipBuilder_vehicle_10.manufacturer = None
    shipBuilder_vehicle_10.defaultVariant = None
    shipBuilder_vehicle_10 = save_or_locate(shipBuilder_vehicle_10)

    shipBuilder_vehicle_11 = Vehicle()
    shipBuilder_vehicle_11.vehicleClass = 1
    shipBuilder_vehicle_11.category = u'Star Fighter'
    shipBuilder_vehicle_11.displayName = u'RSI Aurora MR'
    shipBuilder_vehicle_11.name = u'RSI_Aurora_MR'
    shipBuilder_vehicle_11.views = 0
    shipBuilder_vehicle_11.upgradeSlots = 0
    shipBuilder_vehicle_11.maximum_crew = 1
    shipBuilder_vehicle_11.empty_mass = 0
    shipBuilder_vehicle_11.length = 0.0
    shipBuilder_vehicle_11.width = 0.0
    shipBuilder_vehicle_11.height = 0.0
    shipBuilder_vehicle_11.thumbnail = u''
    shipBuilder_vehicle_11.available = False
    shipBuilder_vehicle_11.manufacturer = None
    shipBuilder_vehicle_11.defaultVariant = None
    shipBuilder_vehicle_11 = save_or_locate(shipBuilder_vehicle_11)

    shipBuilder_vehicle_12 = Vehicle()
    shipBuilder_vehicle_12.vehicleClass = 3
    shipBuilder_vehicle_12.category = u'StarFighter'
    shipBuilder_vehicle_12.displayName = u'RSI Constellation'
    shipBuilder_vehicle_12.name = u'RSI_Constellation'
    shipBuilder_vehicle_12.views = 16
    shipBuilder_vehicle_12.upgradeSlots = 0
    shipBuilder_vehicle_12.maximum_crew = 1
    shipBuilder_vehicle_12.empty_mass = 0
    shipBuilder_vehicle_12.length = 0.0
    shipBuilder_vehicle_12.width = 0.0
    shipBuilder_vehicle_12.height = 0.0
    shipBuilder_vehicle_12.thumbnail = u''
    shipBuilder_vehicle_12.available = False
    shipBuilder_vehicle_12.manufacturer = None
    shipBuilder_vehicle_12.defaultVariant = None
    shipBuilder_vehicle_12 = save_or_locate(shipBuilder_vehicle_12)

    shipBuilder_vehicle_13 = Vehicle()
    shipBuilder_vehicle_13.vehicleClass = 2
    shipBuilder_vehicle_13.category = u'Star Fighter'
    shipBuilder_vehicle_13.displayName = u'Anvil Hornet'
    shipBuilder_vehicle_13.name = u'ANVL_Hornet'
    shipBuilder_vehicle_13.views = 0
    shipBuilder_vehicle_13.upgradeSlots = 0
    shipBuilder_vehicle_13.maximum_crew = 1
    shipBuilder_vehicle_13.empty_mass = 0
    shipBuilder_vehicle_13.length = 0.0
    shipBuilder_vehicle_13.width = 0.0
    shipBuilder_vehicle_13.height = 0.0
    shipBuilder_vehicle_13.thumbnail = u''
    shipBuilder_vehicle_13.available = False
    shipBuilder_vehicle_13.manufacturer = None
    shipBuilder_vehicle_13.defaultVariant = None
    shipBuilder_vehicle_13 = save_or_locate(shipBuilder_vehicle_13)

    shipBuilder_vehicle_14 = Vehicle()
    shipBuilder_vehicle_14.vehicleClass = 2
    shipBuilder_vehicle_14.category = u'Star Fighter'
    shipBuilder_vehicle_14.displayName = u'Anvil Hornet'
    shipBuilder_vehicle_14.name = u'ANVL_Hornet_Dogfight'
    shipBuilder_vehicle_14.views = 0
    shipBuilder_vehicle_14.upgradeSlots = 0
    shipBuilder_vehicle_14.maximum_crew = 1
    shipBuilder_vehicle_14.empty_mass = 0
    shipBuilder_vehicle_14.length = 0.0
    shipBuilder_vehicle_14.width = 0.0
    shipBuilder_vehicle_14.height = 0.0
    shipBuilder_vehicle_14.thumbnail = u''
    shipBuilder_vehicle_14.available = False
    shipBuilder_vehicle_14.manufacturer = None
    shipBuilder_vehicle_14.defaultVariant = None
    shipBuilder_vehicle_14 = save_or_locate(shipBuilder_vehicle_14)

    shipBuilder_vehicle_15 = Vehicle()
    shipBuilder_vehicle_15.vehicleClass = 3
    shipBuilder_vehicle_15.category = u'StarFighter'
    shipBuilder_vehicle_15.displayName = u'Origin JumpWorks 300i'
    shipBuilder_vehicle_15.name = u'ORIG_300i'
    shipBuilder_vehicle_15.views = 0
    shipBuilder_vehicle_15.upgradeSlots = 0
    shipBuilder_vehicle_15.maximum_crew = 1
    shipBuilder_vehicle_15.empty_mass = 0
    shipBuilder_vehicle_15.length = 0.0
    shipBuilder_vehicle_15.width = 0.0
    shipBuilder_vehicle_15.height = 0.0
    shipBuilder_vehicle_15.thumbnail = u''
    shipBuilder_vehicle_15.available = False
    shipBuilder_vehicle_15.manufacturer = None
    shipBuilder_vehicle_15.defaultVariant = None
    shipBuilder_vehicle_15 = save_or_locate(shipBuilder_vehicle_15)

    shipBuilder_vehicle_16 = Vehicle()
    shipBuilder_vehicle_16.vehicleClass = 1
    shipBuilder_vehicle_16.category = u'StarFighter'
    shipBuilder_vehicle_16.displayName = u'RSI Aurora'
    shipBuilder_vehicle_16.name = u'RSI_Aurora'
    shipBuilder_vehicle_16.views = 0
    shipBuilder_vehicle_16.upgradeSlots = 0
    shipBuilder_vehicle_16.maximum_crew = 1
    shipBuilder_vehicle_16.empty_mass = 0
    shipBuilder_vehicle_16.length = 0.0
    shipBuilder_vehicle_16.width = 0.0
    shipBuilder_vehicle_16.height = 0.0
    shipBuilder_vehicle_16.thumbnail = u''
    shipBuilder_vehicle_16.available = False
    shipBuilder_vehicle_16.manufacturer = None
    shipBuilder_vehicle_16.defaultVariant = None
    shipBuilder_vehicle_16 = save_or_locate(shipBuilder_vehicle_16)

    shipBuilder_vehicle_17 = Vehicle()
    shipBuilder_vehicle_17.vehicleClass = 2
    shipBuilder_vehicle_17.category = u'Weapon Mount'
    shipBuilder_vehicle_17.displayName = u'RSI IR1337 Weapon Mount'
    shipBuilder_vehicle_17.name = u'RSI_IR1337_Weapon_Mount'
    shipBuilder_vehicle_17.views = 0
    shipBuilder_vehicle_17.upgradeSlots = 0
    shipBuilder_vehicle_17.maximum_crew = 1
    shipBuilder_vehicle_17.empty_mass = 0
    shipBuilder_vehicle_17.length = 0.0
    shipBuilder_vehicle_17.width = 0.0
    shipBuilder_vehicle_17.height = 0.0
    shipBuilder_vehicle_17.thumbnail = u''
    shipBuilder_vehicle_17.available = False
    shipBuilder_vehicle_17.manufacturer = None
    shipBuilder_vehicle_17.defaultVariant = None
    shipBuilder_vehicle_17 = save_or_locate(shipBuilder_vehicle_17)

    #Processing model: HardpointTag

    from shipBuilder.models import HardpointTag

    shipBuilder_hardpointtag_1 = HardpointTag()
    shipBuilder_hardpointtag_1.hardpoint = shipBuilder_itemport_183
    shipBuilder_hardpointtag_1.locationX = 50.0
    shipBuilder_hardpointtag_1.locationY = 50.0
    shipBuilder_hardpointtag_1.disabled = False
    shipBuilder_hardpointtag_1 = save_or_locate(shipBuilder_hardpointtag_1)

    #Processing model: VariantItem

    from shipBuilder.models import VariantItem


    #Processing model: Variant

    from shipBuilder.models import Variant


    #Processing model: GameUpdate

    from shipBuilder.models import GameUpdate

    shipBuilder_gameupdate_1 = GameUpdate()
    shipBuilder_gameupdate_1.name = u'Hangar Module - Build 0'
    shipBuilder_gameupdate_1.build = u'0'
    shipBuilder_gameupdate_1.module = u'Hangar'
    shipBuilder_gameupdate_1.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 224377)
    shipBuilder_gameupdate_1 = save_or_locate(shipBuilder_gameupdate_1)

    shipBuilder_gameupdate_2 = GameUpdate()
    shipBuilder_gameupdate_2.name = u'Hangar Module - Build 10'
    shipBuilder_gameupdate_2.build = u'10'
    shipBuilder_gameupdate_2.module = u'Hangar'
    shipBuilder_gameupdate_2.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 3, 668017)
    shipBuilder_gameupdate_2 = save_or_locate(shipBuilder_gameupdate_2)

    #Processing model: GameUpdateChange

    from shipBuilder.models import GameUpdateChange

    shipBuilder_gameupdatechange_1 = GameUpdateChange()
    shipBuilder_gameupdatechange_1.description = u"ADDED: New VehicleItem 'ACOM StarHeart III Engine'"
    shipBuilder_gameupdatechange_1.entityName = u'300i_ACOM_StarHeart_III'
    shipBuilder_gameupdatechange_1.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_1.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 229194)
    shipBuilder_gameupdatechange_1 = save_or_locate(shipBuilder_gameupdatechange_1)

    shipBuilder_gameupdatechange_2 = GameUpdateChange()
    shipBuilder_gameupdatechange_2.description = u"ADDED: New VehicleItem 'Hammer Propulsion HE 5.3'"
    shipBuilder_gameupdatechange_2.entityName = u'300i_Hammer_Propulsion_HE_5_3'
    shipBuilder_gameupdatechange_2.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_2.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 242484)
    shipBuilder_gameupdatechange_2 = save_or_locate(shipBuilder_gameupdatechange_2)

    shipBuilder_gameupdatechange_3 = GameUpdateChange()
    shipBuilder_gameupdatechange_3.description = u"ADDED: New VehicleItem 'Hammer Propulsion HE 5.3'"
    shipBuilder_gameupdatechange_3.entityName = u'325a_Hammer_Propulsion_HE_5_3'
    shipBuilder_gameupdatechange_3.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_3.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 266891)
    shipBuilder_gameupdatechange_3 = save_or_locate(shipBuilder_gameupdatechange_3)

    shipBuilder_gameupdatechange_4 = GameUpdateChange()
    shipBuilder_gameupdatechange_4.description = u"ADDED: New VehicleItem 'Hammer Propulsion HM 4.3'"
    shipBuilder_gameupdatechange_4.entityName = u'350r_Hammer_Propulsion_HE_4_3'
    shipBuilder_gameupdatechange_4.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_4.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 293350)
    shipBuilder_gameupdatechange_4 = save_or_locate(shipBuilder_gameupdatechange_4)

    shipBuilder_gameupdatechange_5 = GameUpdateChange()
    shipBuilder_gameupdatechange_5.description = u"ADDED: New VehicleItem 'A&R LR-5 MAX OverDrive'"
    shipBuilder_gameupdatechange_5.entityName = u'A&R_LR-5_MAX_OverDrive'
    shipBuilder_gameupdatechange_5.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_5.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 317035)
    shipBuilder_gameupdatechange_5 = save_or_locate(shipBuilder_gameupdatechange_5)

    shipBuilder_gameupdatechange_6 = GameUpdateChange()
    shipBuilder_gameupdatechange_6.description = u"ADDED: New VehicleItem 'A&R LR-5 OverDrive'"
    shipBuilder_gameupdatechange_6.entityName = u'A&R_LR-5_OverDrive'
    shipBuilder_gameupdatechange_6.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_6.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 328159)
    shipBuilder_gameupdatechange_6 = save_or_locate(shipBuilder_gameupdatechange_6)

    shipBuilder_gameupdatechange_7 = GameUpdateChange()
    shipBuilder_gameupdatechange_7.description = u"ADDED: New VehicleItem 'A&R LR-7 ULTRA OverDrive'"
    shipBuilder_gameupdatechange_7.entityName = u'A&R_LR-7_ULTRA_OverDrive'
    shipBuilder_gameupdatechange_7.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_7.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 337681)
    shipBuilder_gameupdatechange_7 = save_or_locate(shipBuilder_gameupdatechange_7)

    shipBuilder_gameupdatechange_8 = GameUpdateChange()
    shipBuilder_gameupdatechange_8.description = u"ADDED: New VehicleItem 'Aaturret'"
    shipBuilder_gameupdatechange_8.entityName = u'AATurret'
    shipBuilder_gameupdatechange_8.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_8.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 347368)
    shipBuilder_gameupdatechange_8 = save_or_locate(shipBuilder_gameupdatechange_8)

    shipBuilder_gameupdatechange_9 = GameUpdateChange()
    shipBuilder_gameupdatechange_9.description = u"ADDED: New VehicleItem 'Ace Astrogation FusionPro 3H III'"
    shipBuilder_gameupdatechange_9.entityName = u'Ace_Astrogation_FusionPro_3H_III'
    shipBuilder_gameupdatechange_9.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_9.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 356130)
    shipBuilder_gameupdatechange_9 = save_or_locate(shipBuilder_gameupdatechange_9)

    shipBuilder_gameupdatechange_10 = GameUpdateChange()
    shipBuilder_gameupdatechange_10.description = u"ADDED: New VehicleItem 'ACOM StarHeart III Power Plant'"
    shipBuilder_gameupdatechange_10.entityName = u'ACOM_StarHeart_III'
    shipBuilder_gameupdatechange_10.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_10.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 367748)
    shipBuilder_gameupdatechange_10 = save_or_locate(shipBuilder_gameupdatechange_10)

    shipBuilder_gameupdatechange_11 = GameUpdateChange()
    shipBuilder_gameupdatechange_11.description = u"ADDED: New VehicleItem 'ACOM StarLight II Engine'"
    shipBuilder_gameupdatechange_11.entityName = u'ACOM_StarLight_II'
    shipBuilder_gameupdatechange_11.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_11.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 377265)
    shipBuilder_gameupdatechange_11 = save_or_locate(shipBuilder_gameupdatechange_11)

    shipBuilder_gameupdatechange_12 = GameUpdateChange()
    shipBuilder_gameupdatechange_12.description = u"ADDED: New VehicleItem 'Aegis Dynamics M-5c Thorium Engine'"
    shipBuilder_gameupdatechange_12.entityName = u'Aegis_Dynamics_M-5c_PowerPlant'
    shipBuilder_gameupdatechange_12.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_12.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 412669)
    shipBuilder_gameupdatechange_12 = save_or_locate(shipBuilder_gameupdatechange_12)

    shipBuilder_gameupdatechange_13 = GameUpdateChange()
    shipBuilder_gameupdatechange_13.description = u"ADDED: New VehicleItem 'Aegis TR4 Vector Thruster'"
    shipBuilder_gameupdatechange_13.entityName = u'Aegis_TR4_Vector_Thruster'
    shipBuilder_gameupdatechange_13.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_13.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 425976)
    shipBuilder_gameupdatechange_13 = save_or_locate(shipBuilder_gameupdatechange_13)

    shipBuilder_gameupdatechange_14 = GameUpdateChange()
    shipBuilder_gameupdatechange_14.description = u"ADDED: New VehicleItem 'Alliance Startech K3S-9'"
    shipBuilder_gameupdatechange_14.entityName = u'Alliance_Startech_K3S-9'
    shipBuilder_gameupdatechange_14.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_14.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 452601)
    shipBuilder_gameupdatechange_14 = save_or_locate(shipBuilder_gameupdatechange_14)

    shipBuilder_gameupdatechange_15 = GameUpdateChange()
    shipBuilder_gameupdatechange_15.description = u"ADDED: New VehicleItem 'Alliance_Startech_KS-9'"
    shipBuilder_gameupdatechange_15.entityName = u'Alliance_Startech_KS-9'
    shipBuilder_gameupdatechange_15.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_15.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 463648)
    shipBuilder_gameupdatechange_15 = save_or_locate(shipBuilder_gameupdatechange_15)

    shipBuilder_gameupdatechange_16 = GameUpdateChange()
    shipBuilder_gameupdatechange_16.description = u"ADDED: New VehicleItem 'Alliance Startech KS-9 Enhanced'"
    shipBuilder_gameupdatechange_16.entityName = u'Alliance_Startech_KS-9_Enhanced'
    shipBuilder_gameupdatechange_16.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_16.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 473298)
    shipBuilder_gameupdatechange_16 = save_or_locate(shipBuilder_gameupdatechange_16)

    shipBuilder_gameupdatechange_17 = GameUpdateChange()
    shipBuilder_gameupdatechange_17.description = u"ADDED: New VehicleItem 'Anvil MK2 Flex Thruster'"
    shipBuilder_gameupdatechange_17.entityName = u'Anvil_Flex_MK2'
    shipBuilder_gameupdatechange_17.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_17.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 483894)
    shipBuilder_gameupdatechange_17 = save_or_locate(shipBuilder_gameupdatechange_17)

    shipBuilder_gameupdatechange_18 = GameUpdateChange()
    shipBuilder_gameupdatechange_18.description = u"ADDED: New VehicleItem 'Anvil TR2 Flex Thruster'"
    shipBuilder_gameupdatechange_18.entityName = u'Anvil_Flex_Thruster_TR2_Back_Left'
    shipBuilder_gameupdatechange_18.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_18.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 511672)
    shipBuilder_gameupdatechange_18 = save_or_locate(shipBuilder_gameupdatechange_18)

    shipBuilder_gameupdatechange_19 = GameUpdateChange()
    shipBuilder_gameupdatechange_19.description = u"ADDED: New VehicleItem 'Anvil TR2 Flex Thruster'"
    shipBuilder_gameupdatechange_19.entityName = u'Anvil_Flex_Thruster_TR2_Back_Right'
    shipBuilder_gameupdatechange_19.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_19.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 537296)
    shipBuilder_gameupdatechange_19 = save_or_locate(shipBuilder_gameupdatechange_19)

    shipBuilder_gameupdatechange_20 = GameUpdateChange()
    shipBuilder_gameupdatechange_20.description = u"ADDED: New VehicleItem 'Anvil TR2 Flex Thruster'"
    shipBuilder_gameupdatechange_20.entityName = u'Anvil_Flex_Thruster_TR2_Front_Left'
    shipBuilder_gameupdatechange_20.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_20.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 563685)
    shipBuilder_gameupdatechange_20 = save_or_locate(shipBuilder_gameupdatechange_20)

    shipBuilder_gameupdatechange_21 = GameUpdateChange()
    shipBuilder_gameupdatechange_21.description = u"ADDED: New VehicleItem 'Anvil TR2 Flex Thruster'"
    shipBuilder_gameupdatechange_21.entityName = u'Anvil_Flex_Thruster_TR2_Front_Right'
    shipBuilder_gameupdatechange_21.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_21.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 591338)
    shipBuilder_gameupdatechange_21 = save_or_locate(shipBuilder_gameupdatechange_21)

    shipBuilder_gameupdatechange_22 = GameUpdateChange()
    shipBuilder_gameupdatechange_22.description = u"ADDED: New Vehicle 'Anvil Hornet'"
    shipBuilder_gameupdatechange_22.entityName = u'Anvil_Hornet'
    shipBuilder_gameupdatechange_22.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_22.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 662385)
    shipBuilder_gameupdatechange_22 = save_or_locate(shipBuilder_gameupdatechange_22)

    shipBuilder_gameupdatechange_23 = GameUpdateChange()
    shipBuilder_gameupdatechange_23.description = u"ADDED: New Vehicle 'Anvil Hornet F7C'"
    shipBuilder_gameupdatechange_23.entityName = u'Anvil_Hornet_F7C'
    shipBuilder_gameupdatechange_23.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_23.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 34, 851555)
    shipBuilder_gameupdatechange_23 = save_or_locate(shipBuilder_gameupdatechange_23)

    shipBuilder_gameupdatechange_24 = GameUpdateChange()
    shipBuilder_gameupdatechange_24.description = u"ADDED: New VehicleItem 'Anvil MK2 Jointed Thruster'"
    shipBuilder_gameupdatechange_24.entityName = u'Anvil_Joint_MK2'
    shipBuilder_gameupdatechange_24.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_24.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 8145)
    shipBuilder_gameupdatechange_24 = save_or_locate(shipBuilder_gameupdatechange_24)

    shipBuilder_gameupdatechange_25 = GameUpdateChange()
    shipBuilder_gameupdatechange_25.description = u"ADDED: New VehicleItem 'Anvil TR2 Jointed Thruster'"
    shipBuilder_gameupdatechange_25.entityName = u'Anvil_Joint_Thruster_TR2'
    shipBuilder_gameupdatechange_25.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_25.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 56970)
    shipBuilder_gameupdatechange_25 = save_or_locate(shipBuilder_gameupdatechange_25)

    shipBuilder_gameupdatechange_26 = GameUpdateChange()
    shipBuilder_gameupdatechange_26.description = u"ADDED: New VehicleItem 'ArcLight 300'"
    shipBuilder_gameupdatechange_26.entityName = u'Arc_Duo_400'
    shipBuilder_gameupdatechange_26.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_26.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 75338)
    shipBuilder_gameupdatechange_26 = save_or_locate(shipBuilder_gameupdatechange_26)

    shipBuilder_gameupdatechange_27 = GameUpdateChange()
    shipBuilder_gameupdatechange_27.description = u"ADDED: New VehicleItem 'Behring M3A Laser'"
    shipBuilder_gameupdatechange_27.entityName = u'Behring_M3A_Laser'
    shipBuilder_gameupdatechange_27.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_27.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 99538)
    shipBuilder_gameupdatechange_27 = save_or_locate(shipBuilder_gameupdatechange_27)

    shipBuilder_gameupdatechange_28 = GameUpdateChange()
    shipBuilder_gameupdatechange_28.description = u"ADDED: New VehicleItem 'Behring M4A Laser'"
    shipBuilder_gameupdatechange_28.entityName = u'Behring_M4A_Laser'
    shipBuilder_gameupdatechange_28.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_28.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 126709)
    shipBuilder_gameupdatechange_28 = save_or_locate(shipBuilder_gameupdatechange_28)

    shipBuilder_gameupdatechange_29 = GameUpdateChange()
    shipBuilder_gameupdatechange_29.description = u"ADDED: New VehicleItem 'M4A Lasser Cannon'"
    shipBuilder_gameupdatechange_29.entityName = u'Behring_M4A_lasser_Cannon'
    shipBuilder_gameupdatechange_29.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_29.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 181699)
    shipBuilder_gameupdatechange_29 = save_or_locate(shipBuilder_gameupdatechange_29)

    shipBuilder_gameupdatechange_30 = GameUpdateChange()
    shipBuilder_gameupdatechange_30.description = u"ADDED: New VehicleItem 'Behring M5A Laser'"
    shipBuilder_gameupdatechange_30.entityName = u'Behring_M5A_Laser'
    shipBuilder_gameupdatechange_30.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_30.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 198655)
    shipBuilder_gameupdatechange_30 = save_or_locate(shipBuilder_gameupdatechange_30)

    shipBuilder_gameupdatechange_31 = GameUpdateChange()
    shipBuilder_gameupdatechange_31.description = u"ADDED: New VehicleItem 'Behring Marksman HS Quad Platform'"
    shipBuilder_gameupdatechange_31.entityName = u'Behring_Marksman_HS_Platform_x4'
    shipBuilder_gameupdatechange_31.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_31.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 224325)
    shipBuilder_gameupdatechange_31 = save_or_locate(shipBuilder_gameupdatechange_31)

    shipBuilder_gameupdatechange_32 = GameUpdateChange()
    shipBuilder_gameupdatechange_32.description = u"ADDED: New VehicleItem 'Behring Marksman HS Quad Platform'"
    shipBuilder_gameupdatechange_32.entityName = u'Behring_Marksman_Quad'
    shipBuilder_gameupdatechange_32.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_32.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 251916)
    shipBuilder_gameupdatechange_32 = save_or_locate(shipBuilder_gameupdatechange_32)

    shipBuilder_gameupdatechange_33 = GameUpdateChange()
    shipBuilder_gameupdatechange_33.description = u"ADDED: New VehicleItem 'Behring Mk VI Laser'"
    shipBuilder_gameupdatechange_33.entityName = u'Behring_Mk_VI_Laser'
    shipBuilder_gameupdatechange_33.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_33.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 277654)
    shipBuilder_gameupdatechange_33 = save_or_locate(shipBuilder_gameupdatechange_33)

    shipBuilder_gameupdatechange_34 = GameUpdateChange()
    shipBuilder_gameupdatechange_34.description = u"ADDED: New VehicleItem 'Dragon STC Blue Main Engine'"
    shipBuilder_gameupdatechange_34.entityName = u'Dragon_STC_Blue'
    shipBuilder_gameupdatechange_34.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_34.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 303687)
    shipBuilder_gameupdatechange_34 = save_or_locate(shipBuilder_gameupdatechange_34)

    shipBuilder_gameupdatechange_35 = GameUpdateChange()
    shipBuilder_gameupdatechange_35.description = u"ADDED: New VehicleItem 'Dragon STC Red Main Engine'"
    shipBuilder_gameupdatechange_35.entityName = u'Dragon_STC_Red'
    shipBuilder_gameupdatechange_35.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_35.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 319887)
    shipBuilder_gameupdatechange_35 = save_or_locate(shipBuilder_gameupdatechange_35)

    shipBuilder_gameupdatechange_36 = GameUpdateChange()
    shipBuilder_gameupdatechange_36.description = u"ADDED: New VehicleItem 'Dragon STC Silver Main Engine'"
    shipBuilder_gameupdatechange_36.entityName = u'Dragon_STC_Silver'
    shipBuilder_gameupdatechange_36.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_36.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 334193)
    shipBuilder_gameupdatechange_36 = save_or_locate(shipBuilder_gameupdatechange_36)

    shipBuilder_gameupdatechange_37 = GameUpdateChange()
    shipBuilder_gameupdatechange_37.description = u"ADDED: New VehicleItem 'Sure Grip Tractor'"
    shipBuilder_gameupdatechange_37.entityName = u'Greycat_Industrial_Sure_Grip_Tractor'
    shipBuilder_gameupdatechange_37.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_37.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 347425)
    shipBuilder_gameupdatechange_37 = save_or_locate(shipBuilder_gameupdatechange_37)

    shipBuilder_gameupdatechange_38 = GameUpdateChange()
    shipBuilder_gameupdatechange_38.description = u"ADDED: New VehicleItem 'Groupe Nouveau Paradigme Etoile-00'"
    shipBuilder_gameupdatechange_38.entityName = u'Groupe_Nouveau_Paradigme_Etoile-00'
    shipBuilder_gameupdatechange_38.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_38.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 355054)
    shipBuilder_gameupdatechange_38 = save_or_locate(shipBuilder_gameupdatechange_38)

    shipBuilder_gameupdatechange_39 = GameUpdateChange()
    shipBuilder_gameupdatechange_39.description = u"ADDED: New VehicleItem 'Hammer Propulsion HE 5.5'"
    shipBuilder_gameupdatechange_39.entityName = u'Hammer_Propulsion_HE_5_5'
    shipBuilder_gameupdatechange_39.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_39.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 366703)
    shipBuilder_gameupdatechange_39 = save_or_locate(shipBuilder_gameupdatechange_39)

    shipBuilder_gameupdatechange_40 = GameUpdateChange()
    shipBuilder_gameupdatechange_40.description = u"ADDED: New VehicleItem 'Hammer Propulsion HMX 4.3'"
    shipBuilder_gameupdatechange_40.entityName = u'Hammer_Propulsion_HM_4.4'
    shipBuilder_gameupdatechange_40.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_40.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 388580)
    shipBuilder_gameupdatechange_40 = save_or_locate(shipBuilder_gameupdatechange_40)

    shipBuilder_gameupdatechange_41 = GameUpdateChange()
    shipBuilder_gameupdatechange_41.description = u"ADDED: New VehicleItem 'Hammer Propulsion HM 4.3'"
    shipBuilder_gameupdatechange_41.entityName = u'Hammer_Propulsion_HM_4_3'
    shipBuilder_gameupdatechange_41.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_41.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 411680)
    shipBuilder_gameupdatechange_41 = save_or_locate(shipBuilder_gameupdatechange_41)

    shipBuilder_gameupdatechange_42 = GameUpdateChange()
    shipBuilder_gameupdatechange_42.description = u"ADDED: New VehicleItem 'Hellfire'"
    shipBuilder_gameupdatechange_42.entityName = u'Hellfire'
    shipBuilder_gameupdatechange_42.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_42.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 433279)
    shipBuilder_gameupdatechange_42 = save_or_locate(shipBuilder_gameupdatechange_42)

    shipBuilder_gameupdatechange_43 = GameUpdateChange()
    shipBuilder_gameupdatechange_43.description = u"ADDED: New VehicleItem 'Juno Starwerk Endurance-300'"
    shipBuilder_gameupdatechange_43.entityName = u'Juno_Starwerk_Endurance-300'
    shipBuilder_gameupdatechange_43.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_43.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 450249)
    shipBuilder_gameupdatechange_43 = save_or_locate(shipBuilder_gameupdatechange_43)

    shipBuilder_gameupdatechange_44 = GameUpdateChange()
    shipBuilder_gameupdatechange_44.description = u"ADDED: New VehicleItem 'CF-007 Bulldog Repeater'"
    shipBuilder_gameupdatechange_44.entityName = u'K_and_W_CF-007_Bulldog_Repeater'
    shipBuilder_gameupdatechange_44.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_44.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 461347)
    shipBuilder_gameupdatechange_44 = save_or_locate(shipBuilder_gameupdatechange_44)

    shipBuilder_gameupdatechange_45 = GameUpdateChange()
    shipBuilder_gameupdatechange_45.description = u"ADDED: New VehicleItem 'CF-117 Badger Repeater'"
    shipBuilder_gameupdatechange_45.entityName = u'K_and_W_CF-117_Badger_Repeater'
    shipBuilder_gameupdatechange_45.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_45.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 491659)
    shipBuilder_gameupdatechange_45 = save_or_locate(shipBuilder_gameupdatechange_45)

    shipBuilder_gameupdatechange_46 = GameUpdateChange()
    shipBuilder_gameupdatechange_46.description = u"ADDED: New VehicleItem 'CF-227 Panther Repeater'"
    shipBuilder_gameupdatechange_46.entityName = u'K_and_W_CF-227_Panther_Repeater'
    shipBuilder_gameupdatechange_46.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_46.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 517664)
    shipBuilder_gameupdatechange_46 = save_or_locate(shipBuilder_gameupdatechange_46)

    shipBuilder_gameupdatechange_47 = GameUpdateChange()
    shipBuilder_gameupdatechange_47.description = u"ADDED: New VehicleItem 'K and W Mass Driver Cannon'"
    shipBuilder_gameupdatechange_47.entityName = u'K_and_W_Mass_Driver_Cannon'
    shipBuilder_gameupdatechange_47.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_47.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 546607)
    shipBuilder_gameupdatechange_47 = save_or_locate(shipBuilder_gameupdatechange_47)

    shipBuilder_gameupdatechange_48 = GameUpdateChange()
    shipBuilder_gameupdatechange_48.description = u"ADDED: New VehicleItem '007 Bulldog Laser Repeater Turret'"
    shipBuilder_gameupdatechange_48.entityName = u'K_W_CF_007_Bulldog_Laser_Repeater_Turret'
    shipBuilder_gameupdatechange_48.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_48.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 571594)
    shipBuilder_gameupdatechange_48 = save_or_locate(shipBuilder_gameupdatechange_48)

    shipBuilder_gameupdatechange_49 = GameUpdateChange()
    shipBuilder_gameupdatechange_49.description = u"ADDED: New VehicleItem 'CF-117 Badger Repeater Laser Turret'"
    shipBuilder_gameupdatechange_49.entityName = u'K_W_CF_117_Badger_Repeater_Laser_Turret'
    shipBuilder_gameupdatechange_49.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_49.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 593399)
    shipBuilder_gameupdatechange_49 = save_or_locate(shipBuilder_gameupdatechange_49)

    shipBuilder_gameupdatechange_50 = GameUpdateChange()
    shipBuilder_gameupdatechange_50.description = u"ADDED: New VehicleItem 'KDK TM-4 Slider Thruster'"
    shipBuilder_gameupdatechange_50.entityName = u'KDK_TM-4_Slider'
    shipBuilder_gameupdatechange_50.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_50.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 626405)
    shipBuilder_gameupdatechange_50 = save_or_locate(shipBuilder_gameupdatechange_50)

    shipBuilder_gameupdatechange_51 = GameUpdateChange()
    shipBuilder_gameupdatechange_51.description = u"ADDED: New VehicleItem '11-Series Broadsword'"
    shipBuilder_gameupdatechange_51.entityName = u'Knightbridge_11_Series_Broadsword'
    shipBuilder_gameupdatechange_51.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_51.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 653511)
    shipBuilder_gameupdatechange_51 = save_or_locate(shipBuilder_gameupdatechange_51)

    shipBuilder_gameupdatechange_52 = GameUpdateChange()
    shipBuilder_gameupdatechange_52.description = u"ADDED: New VehicleItem '9-Series Longsword'"
    shipBuilder_gameupdatechange_52.entityName = u'Knightbridge_9_Series_Longsword'
    shipBuilder_gameupdatechange_52.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_52.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 680986)
    shipBuilder_gameupdatechange_52 = save_or_locate(shipBuilder_gameupdatechange_52)

    shipBuilder_gameupdatechange_53 = GameUpdateChange()
    shipBuilder_gameupdatechange_53.description = u"ADDED: New VehicleItem 'Lightning Powerbolt Hyperfluid Quantum Vortex'"
    shipBuilder_gameupdatechange_53.entityName = u'LPB_Condensed_Matter_Reactor'
    shipBuilder_gameupdatechange_53.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_53.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 706463)
    shipBuilder_gameupdatechange_53 = save_or_locate(shipBuilder_gameupdatechange_53)

    shipBuilder_gameupdatechange_54 = GameUpdateChange()
    shipBuilder_gameupdatechange_54.description = u"ADDED: New VehicleItem 'Lightning Powerbolt Powerbolt'"
    shipBuilder_gameupdatechange_54.entityName = u'LPB_Powerbolt'
    shipBuilder_gameupdatechange_54.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_54.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 717144)
    shipBuilder_gameupdatechange_54 = save_or_locate(shipBuilder_gameupdatechange_54)

    shipBuilder_gameupdatechange_55 = GameUpdateChange()
    shipBuilder_gameupdatechange_55.description = u"ADDED: New VehicleItem 'Mantis GT-220'"
    shipBuilder_gameupdatechange_55.entityName = u'Mantis_GT-220'
    shipBuilder_gameupdatechange_55.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_55.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 728564)
    shipBuilder_gameupdatechange_55 = save_or_locate(shipBuilder_gameupdatechange_55)

    shipBuilder_gameupdatechange_56 = GameUpdateChange()
    shipBuilder_gameupdatechange_56.description = u"ADDED: New VehicleItem 'MaxOx NN-13 Neutron Cannon'"
    shipBuilder_gameupdatechange_56.entityName = u'Max_Ox_NN13_Neutron'
    shipBuilder_gameupdatechange_56.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_56.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 745769)
    shipBuilder_gameupdatechange_56 = save_or_locate(shipBuilder_gameupdatechange_56)

    shipBuilder_gameupdatechange_57 = GameUpdateChange()
    shipBuilder_gameupdatechange_57.description = u"ADDED: New Vehicle 'MISC Freelancer'"
    shipBuilder_gameupdatechange_57.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_57.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_57.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 808696)
    shipBuilder_gameupdatechange_57 = save_or_locate(shipBuilder_gameupdatechange_57)

    shipBuilder_gameupdatechange_58 = GameUpdateChange()
    shipBuilder_gameupdatechange_58.description = u"ADDED: New VehicleItem 'Missileturret'"
    shipBuilder_gameupdatechange_58.entityName = u'MissileTurret'
    shipBuilder_gameupdatechange_58.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_58.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 952727)
    shipBuilder_gameupdatechange_58 = save_or_locate(shipBuilder_gameupdatechange_58)

    shipBuilder_gameupdatechange_59 = GameUpdateChange()
    shipBuilder_gameupdatechange_59.description = u"ADDED: New Vehicle 'Origin JumpWorks 300i'"
    shipBuilder_gameupdatechange_59.entityName = u'OJ_300i'
    shipBuilder_gameupdatechange_59.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_59.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 35, 987766)
    shipBuilder_gameupdatechange_59 = save_or_locate(shipBuilder_gameupdatechange_59)

    shipBuilder_gameupdatechange_60 = GameUpdateChange()
    shipBuilder_gameupdatechange_60.description = u"ADDED: New Vehicle ''"
    shipBuilder_gameupdatechange_60.entityName = u'OJ_315p'
    shipBuilder_gameupdatechange_60.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_60.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 156215)
    shipBuilder_gameupdatechange_60 = save_or_locate(shipBuilder_gameupdatechange_60)

    shipBuilder_gameupdatechange_61 = GameUpdateChange()
    shipBuilder_gameupdatechange_61.description = u"ADDED: New Vehicle ''"
    shipBuilder_gameupdatechange_61.entityName = u'OJ_325a'
    shipBuilder_gameupdatechange_61.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_61.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 339444)
    shipBuilder_gameupdatechange_61 = save_or_locate(shipBuilder_gameupdatechange_61)

    shipBuilder_gameupdatechange_62 = GameUpdateChange()
    shipBuilder_gameupdatechange_62.description = u"ADDED: New Vehicle 'OJ 350 R'"
    shipBuilder_gameupdatechange_62.entityName = u'OJ_350r'
    shipBuilder_gameupdatechange_62.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_62.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 498317)
    shipBuilder_gameupdatechange_62 = save_or_locate(shipBuilder_gameupdatechange_62)

    shipBuilder_gameupdatechange_63 = GameUpdateChange()
    shipBuilder_gameupdatechange_63.description = u"ADDED: New VehicleItem 'Origin Omni Precision Ball Thruster'"
    shipBuilder_gameupdatechange_63.entityName = u'OJ_Omni_Precison_Thruster_TR2'
    shipBuilder_gameupdatechange_63.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_63.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 628133)
    shipBuilder_gameupdatechange_63 = save_or_locate(shipBuilder_gameupdatechange_63)

    shipBuilder_gameupdatechange_64 = GameUpdateChange()
    shipBuilder_gameupdatechange_64.description = u"ADDED: New VehicleItem 'Origin Scalpel Precision Thruster'"
    shipBuilder_gameupdatechange_64.entityName = u'OJ_Scalpel_Precision_Thruster_TR2'
    shipBuilder_gameupdatechange_64.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_64.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 646891)
    shipBuilder_gameupdatechange_64 = save_or_locate(shipBuilder_gameupdatechange_64)

    shipBuilder_gameupdatechange_65 = GameUpdateChange()
    shipBuilder_gameupdatechange_65.description = u"ADDED: New VehicleItem 'OKB Voshkod Energia IV'"
    shipBuilder_gameupdatechange_65.entityName = u'OKB_Energia_IV'
    shipBuilder_gameupdatechange_65.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_65.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 664263)
    shipBuilder_gameupdatechange_65 = save_or_locate(shipBuilder_gameupdatechange_65)

    shipBuilder_gameupdatechange_66 = GameUpdateChange()
    shipBuilder_gameupdatechange_66.description = u"ADDED: New VehicleItem 'Omnisky III Laser Cannon'"
    shipBuilder_gameupdatechange_66.entityName = u'Omnisky_III_Laser'
    shipBuilder_gameupdatechange_66.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_66.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 678749)
    shipBuilder_gameupdatechange_66 = save_or_locate(shipBuilder_gameupdatechange_66)

    shipBuilder_gameupdatechange_67 = GameUpdateChange()
    shipBuilder_gameupdatechange_67.description = u"ADDED: New VehicleItem 'Omnisky VI Laser Cannon'"
    shipBuilder_gameupdatechange_67.entityName = u'Omnisky_VI_Laser'
    shipBuilder_gameupdatechange_67.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_67.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 699271)
    shipBuilder_gameupdatechange_67 = save_or_locate(shipBuilder_gameupdatechange_67)

    shipBuilder_gameupdatechange_68 = GameUpdateChange()
    shipBuilder_gameupdatechange_68.description = u"ADDED: New VehicleItem 'Phalanxturret'"
    shipBuilder_gameupdatechange_68.entityName = u'PhalanxTurret'
    shipBuilder_gameupdatechange_68.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_68.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 727657)
    shipBuilder_gameupdatechange_68 = save_or_locate(shipBuilder_gameupdatechange_68)

    shipBuilder_gameupdatechange_69 = GameUpdateChange()
    shipBuilder_gameupdatechange_69.description = u"ADDED: New Vehicle 'RSI Aurora CL'"
    shipBuilder_gameupdatechange_69.entityName = u'RSI_Aurora_CL'
    shipBuilder_gameupdatechange_69.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_69.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 756235)
    shipBuilder_gameupdatechange_69 = save_or_locate(shipBuilder_gameupdatechange_69)

    shipBuilder_gameupdatechange_70 = GameUpdateChange()
    shipBuilder_gameupdatechange_70.description = u"ADDED: New Vehicle ''"
    shipBuilder_gameupdatechange_70.entityName = u'RSI_Aurora_ES'
    shipBuilder_gameupdatechange_70.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_70.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 857780)
    shipBuilder_gameupdatechange_70 = save_or_locate(shipBuilder_gameupdatechange_70)

    shipBuilder_gameupdatechange_71 = GameUpdateChange()
    shipBuilder_gameupdatechange_71.description = u"ADDED: New Vehicle ''"
    shipBuilder_gameupdatechange_71.entityName = u'RSI_Aurora_LX'
    shipBuilder_gameupdatechange_71.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_71.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 36, 989351)
    shipBuilder_gameupdatechange_71 = save_or_locate(shipBuilder_gameupdatechange_71)

    shipBuilder_gameupdatechange_72 = GameUpdateChange()
    shipBuilder_gameupdatechange_72.description = u"ADDED: New Vehicle 'RSI Aurora MR'"
    shipBuilder_gameupdatechange_72.entityName = u'RSI_Aurora_MR'
    shipBuilder_gameupdatechange_72.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_72.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 85497)
    shipBuilder_gameupdatechange_72 = save_or_locate(shipBuilder_gameupdatechange_72)

    shipBuilder_gameupdatechange_73 = GameUpdateChange()
    shipBuilder_gameupdatechange_73.description = u"ADDED: New Vehicle ''"
    shipBuilder_gameupdatechange_73.entityName = u'RSI_Constellation'
    shipBuilder_gameupdatechange_73.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_73.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 160243)
    shipBuilder_gameupdatechange_73 = save_or_locate(shipBuilder_gameupdatechange_73)

    shipBuilder_gameupdatechange_74 = GameUpdateChange()
    shipBuilder_gameupdatechange_74.description = u"ADDED: New VehicleItem 'RSI Battery'"
    shipBuilder_gameupdatechange_74.entityName = u'RSI_DefaultBattery'
    shipBuilder_gameupdatechange_74.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_74.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 193513)
    shipBuilder_gameupdatechange_74 = save_or_locate(shipBuilder_gameupdatechange_74)

    shipBuilder_gameupdatechange_75 = GameUpdateChange()
    shipBuilder_gameupdatechange_75.description = u"ADDED: New VehicleItem 'RSI Heat Cooler'"
    shipBuilder_gameupdatechange_75.entityName = u'RSI_DefaultCooler'
    shipBuilder_gameupdatechange_75.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_75.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 212115)
    shipBuilder_gameupdatechange_75 = save_or_locate(shipBuilder_gameupdatechange_75)

    shipBuilder_gameupdatechange_76 = GameUpdateChange()
    shipBuilder_gameupdatechange_76.description = u"ADDED: New VehicleItem 'RSI Power Supply'"
    shipBuilder_gameupdatechange_76.entityName = u'RSI_DefaultPowerPlant'
    shipBuilder_gameupdatechange_76.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_76.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 222974)
    shipBuilder_gameupdatechange_76 = save_or_locate(shipBuilder_gameupdatechange_76)

    shipBuilder_gameupdatechange_77 = GameUpdateChange()
    shipBuilder_gameupdatechange_77.description = u"ADDED: New VehicleItem 'RSI Radar Display'"
    shipBuilder_gameupdatechange_77.entityName = u'RSI_DefaultRadarDisplay'
    shipBuilder_gameupdatechange_77.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_77.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 235180)
    shipBuilder_gameupdatechange_77 = save_or_locate(shipBuilder_gameupdatechange_77)

    shipBuilder_gameupdatechange_78 = GameUpdateChange()
    shipBuilder_gameupdatechange_78.description = u"ADDED: New VehicleItem 'RSI Radar Long Range'"
    shipBuilder_gameupdatechange_78.entityName = u'RSI_DefaultRadarLongRange'
    shipBuilder_gameupdatechange_78.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_78.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 247553)
    shipBuilder_gameupdatechange_78 = save_or_locate(shipBuilder_gameupdatechange_78)

    shipBuilder_gameupdatechange_79 = GameUpdateChange()
    shipBuilder_gameupdatechange_79.description = u"ADDED: New VehicleItem 'RSI Radar Mid Range'"
    shipBuilder_gameupdatechange_79.entityName = u'RSI_DefaultRadarMidRange'
    shipBuilder_gameupdatechange_79.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_79.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 265913)
    shipBuilder_gameupdatechange_79 = save_or_locate(shipBuilder_gameupdatechange_79)

    shipBuilder_gameupdatechange_80 = GameUpdateChange()
    shipBuilder_gameupdatechange_80.description = u"ADDED: New VehicleItem 'RSI Radar Short Range'"
    shipBuilder_gameupdatechange_80.entityName = u'RSI_DefaultRadarShortRange'
    shipBuilder_gameupdatechange_80.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_80.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 284583)
    shipBuilder_gameupdatechange_80 = save_or_locate(shipBuilder_gameupdatechange_80)

    shipBuilder_gameupdatechange_81 = GameUpdateChange()
    shipBuilder_gameupdatechange_81.description = u"ADDED: New VehicleItem 'RSI Target Selection Device'"
    shipBuilder_gameupdatechange_81.entityName = u'RSI_DefaultTargetSelector'
    shipBuilder_gameupdatechange_81.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_81.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 309676)
    shipBuilder_gameupdatechange_81 = save_or_locate(shipBuilder_gameupdatechange_81)

    shipBuilder_gameupdatechange_82 = GameUpdateChange()
    shipBuilder_gameupdatechange_82.description = u"ADDED: New VehicleItem 'RSI Visor Display'"
    shipBuilder_gameupdatechange_82.entityName = u'RSI_DefaultVisor'
    shipBuilder_gameupdatechange_82.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_82.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 319694)
    shipBuilder_gameupdatechange_82 = save_or_locate(shipBuilder_gameupdatechange_82)

    shipBuilder_gameupdatechange_83 = GameUpdateChange()
    shipBuilder_gameupdatechange_83.description = u"ADDED: New VehicleItem 'RSI Weapon Display'"
    shipBuilder_gameupdatechange_83.entityName = u'RSI_DefaultWeaponDisplay'
    shipBuilder_gameupdatechange_83.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_83.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 331554)
    shipBuilder_gameupdatechange_83 = save_or_locate(shipBuilder_gameupdatechange_83)

    shipBuilder_gameupdatechange_84 = GameUpdateChange()
    shipBuilder_gameupdatechange_84.description = u"ADDED: New VehicleItem 'Missile Bay'"
    shipBuilder_gameupdatechange_84.entityName = u'RSI_MissileBay'
    shipBuilder_gameupdatechange_84.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_84.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 339555)
    shipBuilder_gameupdatechange_84 = save_or_locate(shipBuilder_gameupdatechange_84)

    shipBuilder_gameupdatechange_85 = GameUpdateChange()
    shipBuilder_gameupdatechange_85.description = u"ADDED: New VehicleItem 'Sakura Sun Light Blossom 6HE8A'"
    shipBuilder_gameupdatechange_85.entityName = u'Sakura_Sun_Light_Blossom_6HE8A'
    shipBuilder_gameupdatechange_85.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_85.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 356301)
    shipBuilder_gameupdatechange_85 = save_or_locate(shipBuilder_gameupdatechange_85)

    shipBuilder_gameupdatechange_86 = GameUpdateChange()
    shipBuilder_gameupdatechange_86.description = u"ADDED: New VehicleItem 'Scytheleftwingcannon'"
    shipBuilder_gameupdatechange_86.entityName = u'ScytheLeftWingCannon'
    shipBuilder_gameupdatechange_86.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_86.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 367598)
    shipBuilder_gameupdatechange_86 = save_or_locate(shipBuilder_gameupdatechange_86)

    shipBuilder_gameupdatechange_87 = GameUpdateChange()
    shipBuilder_gameupdatechange_87.description = u"ADDED: New VehicleItem 'Scythemissileracks'"
    shipBuilder_gameupdatechange_87.entityName = u'ScytheMissileRacks'
    shipBuilder_gameupdatechange_87.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_87.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 376306)
    shipBuilder_gameupdatechange_87 = save_or_locate(shipBuilder_gameupdatechange_87)

    shipBuilder_gameupdatechange_88 = GameUpdateChange()
    shipBuilder_gameupdatechange_88.description = u"ADDED: New VehicleItem 'Scytherightwingcannon'"
    shipBuilder_gameupdatechange_88.entityName = u'ScytheRightWingCannon'
    shipBuilder_gameupdatechange_88.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_88.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 382870)
    shipBuilder_gameupdatechange_88 = save_or_locate(shipBuilder_gameupdatechange_88)

    shipBuilder_gameupdatechange_89 = GameUpdateChange()
    shipBuilder_gameupdatechange_89.description = u"ADDED: New VehicleItem 'Stinger'"
    shipBuilder_gameupdatechange_89.entityName = u'Stinger'
    shipBuilder_gameupdatechange_89.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_89.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 389733)
    shipBuilder_gameupdatechange_89 = save_or_locate(shipBuilder_gameupdatechange_89)

    shipBuilder_gameupdatechange_90 = GameUpdateChange()
    shipBuilder_gameupdatechange_90.description = u"ADDED: New VehicleItem 'Stor-All Big Box Model A'"
    shipBuilder_gameupdatechange_90.entityName = u'Stor-All_Big_Box_Model_A'
    shipBuilder_gameupdatechange_90.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_90.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 411388)
    shipBuilder_gameupdatechange_90 = save_or_locate(shipBuilder_gameupdatechange_90)

    shipBuilder_gameupdatechange_91 = GameUpdateChange()
    shipBuilder_gameupdatechange_91.description = u"ADDED: New VehicleItem 'Stor-All Big Box Model H'"
    shipBuilder_gameupdatechange_91.entityName = u'Stor-All_Big_Box_Model_H'
    shipBuilder_gameupdatechange_91.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_91.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 420840)
    shipBuilder_gameupdatechange_91 = save_or_locate(shipBuilder_gameupdatechange_91)

    shipBuilder_gameupdatechange_92 = GameUpdateChange()
    shipBuilder_gameupdatechange_92.description = u"ADDED: New VehicleItem 'Stor-All Mini'"
    shipBuilder_gameupdatechange_92.entityName = u'Stor-All_Mini'
    shipBuilder_gameupdatechange_92.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_92.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 428083)
    shipBuilder_gameupdatechange_92 = save_or_locate(shipBuilder_gameupdatechange_92)

    shipBuilder_gameupdatechange_93 = GameUpdateChange()
    shipBuilder_gameupdatechange_93.description = u"ADDED: New VehicleItem 'Ststurret'"
    shipBuilder_gameupdatechange_93.entityName = u'STSTurret'
    shipBuilder_gameupdatechange_93.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_93.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 434553)
    shipBuilder_gameupdatechange_93 = save_or_locate(shipBuilder_gameupdatechange_93)

    shipBuilder_gameupdatechange_94 = GameUpdateChange()
    shipBuilder_gameupdatechange_94.description = u"ADDED: New VehicleItem 'Talon Dominator FF Quad'"
    shipBuilder_gameupdatechange_94.entityName = u'Talon_Dominator_Platform_x4'
    shipBuilder_gameupdatechange_94.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_94.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 441708)
    shipBuilder_gameupdatechange_94 = save_or_locate(shipBuilder_gameupdatechange_94)

    shipBuilder_gameupdatechange_95 = GameUpdateChange()
    shipBuilder_gameupdatechange_95.description = u"ADDED: New VehicleItem 'Talon Executioner IR Twin'"
    shipBuilder_gameupdatechange_95.entityName = u'Talon_Executioner_IR_Twin'
    shipBuilder_gameupdatechange_95.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_95.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 470176)
    shipBuilder_gameupdatechange_95 = save_or_locate(shipBuilder_gameupdatechange_95)

    shipBuilder_gameupdatechange_96 = GameUpdateChange()
    shipBuilder_gameupdatechange_96.description = u"ADDED: New VehicleItem 'Talon Stalker Quad Rack'"
    shipBuilder_gameupdatechange_96.entityName = u'Talon_Stalker_Quad'
    shipBuilder_gameupdatechange_96.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_96.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 529108)
    shipBuilder_gameupdatechange_96 = save_or_locate(shipBuilder_gameupdatechange_96)

    shipBuilder_gameupdatechange_97 = GameUpdateChange()
    shipBuilder_gameupdatechange_97.description = u"ADDED: New VehicleItem 'Talon Stalker Twin Rack'"
    shipBuilder_gameupdatechange_97.entityName = u'Talon_Stalker_Twin'
    shipBuilder_gameupdatechange_97.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_97.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 555772)
    shipBuilder_gameupdatechange_97 = save_or_locate(shipBuilder_gameupdatechange_97)

    shipBuilder_gameupdatechange_98 = GameUpdateChange()
    shipBuilder_gameupdatechange_98.description = u"ADDED: New VehicleItem 'Wei Tek HFR2 Plus'"
    shipBuilder_gameupdatechange_98.entityName = u'Wei_Tek_HFR2_Plus'
    shipBuilder_gameupdatechange_98.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_98.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 584192)
    shipBuilder_gameupdatechange_98 = save_or_locate(shipBuilder_gameupdatechange_98)

    shipBuilder_gameupdatechange_99 = GameUpdateChange()
    shipBuilder_gameupdatechange_99.description = u"ADDED: New VehicleItem 'Wei Tek VHT2 Plus'"
    shipBuilder_gameupdatechange_99.entityName = u'Wei_Tek_VHT2_Plus'
    shipBuilder_gameupdatechange_99.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_99.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 595324)
    shipBuilder_gameupdatechange_99 = save_or_locate(shipBuilder_gameupdatechange_99)

    shipBuilder_gameupdatechange_100 = GameUpdateChange()
    shipBuilder_gameupdatechange_100.description = u"ADDED: New VehicleItem 'XForge P/S2-80 Main Engine'"
    shipBuilder_gameupdatechange_100.entityName = u'XForge_PS2_80'
    shipBuilder_gameupdatechange_100.update = shipBuilder_gameupdate_1
    shipBuilder_gameupdatechange_100.creation_date = datetime.datetime(2013, 12, 24, 2, 43, 37, 605096)
    shipBuilder_gameupdatechange_100 = save_or_locate(shipBuilder_gameupdatechange_100)

    shipBuilder_gameupdatechange_101 = GameUpdateChange()
    shipBuilder_gameupdatechange_101.description = u"ADDED: New Vehicle 'Anvil Hornet'"
    shipBuilder_gameupdatechange_101.entityName = u'ANVL_Hornet'
    shipBuilder_gameupdatechange_101.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_101.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 3, 726614)
    shipBuilder_gameupdatechange_101 = save_or_locate(shipBuilder_gameupdatechange_101)

    shipBuilder_gameupdatechange_102 = GameUpdateChange()
    shipBuilder_gameupdatechange_102.description = u"ADDED: New Vehicle 'Anvil Hornet'"
    shipBuilder_gameupdatechange_102.entityName = u'ANVL_Hornet_Dogfight'
    shipBuilder_gameupdatechange_102.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_102.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 3, 947195)
    shipBuilder_gameupdatechange_102 = save_or_locate(shipBuilder_gameupdatechange_102)

    shipBuilder_gameupdatechange_103 = GameUpdateChange()
    shipBuilder_gameupdatechange_103.description = u"ADDED: New VehicleItem 'CF-117 Badger Repeater Laser Turret'"
    shipBuilder_gameupdatechange_103.entityName = u'Hornet_BallTurret'
    shipBuilder_gameupdatechange_103.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_103.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 215821)
    shipBuilder_gameupdatechange_103 = save_or_locate(shipBuilder_gameupdatechange_103)

    shipBuilder_gameupdatechange_104 = GameUpdateChange()
    shipBuilder_gameupdatechange_104.description = u"ADDED: New VehicleItem '007 Bulldog Laser Repeater Turret'"
    shipBuilder_gameupdatechange_104.entityName = u'Hornet_CanardTurret'
    shipBuilder_gameupdatechange_104.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_104.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 264190)
    shipBuilder_gameupdatechange_104 = save_or_locate(shipBuilder_gameupdatechange_104)

    shipBuilder_gameupdatechange_105 = GameUpdateChange()
    shipBuilder_gameupdatechange_105.description = u"CHANGED: ItemPort Engine Attach: supportedTypes changed from 'thruster' to 'mainthruster'"
    shipBuilder_gameupdatechange_105.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_105.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_105.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 323002)
    shipBuilder_gameupdatechange_105 = save_or_locate(shipBuilder_gameupdatechange_105)

    shipBuilder_gameupdatechange_106 = GameUpdateChange()
    shipBuilder_gameupdatechange_106.description = u"CHANGED: ItemPort Thruster Rear Right Bottom: flags changed from 'maneuver orientation +Z lower rear left' to 'maneuver orientation lower rear right'"
    shipBuilder_gameupdatechange_106.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_106.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_106.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 325221)
    shipBuilder_gameupdatechange_106 = save_or_locate(shipBuilder_gameupdatechange_106)

    shipBuilder_gameupdatechange_107 = GameUpdateChange()
    shipBuilder_gameupdatechange_107.description = u"CHANGED: ItemPort Thruster Rear Right Mid: flags changed from 'maneuver orientation +Z mid rear left' to 'maneuver orientation mid rear right'"
    shipBuilder_gameupdatechange_107.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_107.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_107.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 327048)
    shipBuilder_gameupdatechange_107 = save_or_locate(shipBuilder_gameupdatechange_107)

    shipBuilder_gameupdatechange_108 = GameUpdateChange()
    shipBuilder_gameupdatechange_108.description = u"CHANGED: ItemPort Thruster Rear Right Upper: flags changed from 'maneuver orientation +Z upper rear left' to 'maneuver orientation +Z upper rear right'"
    shipBuilder_gameupdatechange_108.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_108.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_108.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 328708)
    shipBuilder_gameupdatechange_108 = save_or_locate(shipBuilder_gameupdatechange_108)

    shipBuilder_gameupdatechange_109 = GameUpdateChange()
    shipBuilder_gameupdatechange_109.description = u"CHANGED: ItemPort Thruster Rear Left Bottom: flags changed from 'maneuver orientation +Z lower rear left' to 'maneuver orientation lower rear left'"
    shipBuilder_gameupdatechange_109.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_109.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_109.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 330347)
    shipBuilder_gameupdatechange_109 = save_or_locate(shipBuilder_gameupdatechange_109)

    shipBuilder_gameupdatechange_110 = GameUpdateChange()
    shipBuilder_gameupdatechange_110.description = u"CHANGED: ItemPort Thruster Rear Left Mid: flags changed from 'maneuver orientation +Z mid rear left' to 'maneuver orientation mid rear left'"
    shipBuilder_gameupdatechange_110.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_110.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_110.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 332122)
    shipBuilder_gameupdatechange_110 = save_or_locate(shipBuilder_gameupdatechange_110)

    shipBuilder_gameupdatechange_111 = GameUpdateChange()
    shipBuilder_gameupdatechange_111.description = u"CHANGED: ItemPort Thruster Rear Left Upper: flags changed from 'maneuver orientation +Z upper rear left' to 'maneuver orientation upper rear left'"
    shipBuilder_gameupdatechange_111.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_111.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_111.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 333890)
    shipBuilder_gameupdatechange_111 = save_or_locate(shipBuilder_gameupdatechange_111)

    shipBuilder_gameupdatechange_112 = GameUpdateChange()
    shipBuilder_gameupdatechange_112.description = u"CHANGED: ItemPort Thruster Front Right Bottom: flags changed from 'maneuver orientation +Z lower rear left' to 'maneuver orientation retro lower front right'"
    shipBuilder_gameupdatechange_112.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_112.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_112.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 335548)
    shipBuilder_gameupdatechange_112 = save_or_locate(shipBuilder_gameupdatechange_112)

    shipBuilder_gameupdatechange_113 = GameUpdateChange()
    shipBuilder_gameupdatechange_113.description = u"CHANGED: ItemPort Thruster Front Right Upper: flags changed from 'maneuver orientation +Z upper rear left' to 'maneuver orientation retro upper front right'"
    shipBuilder_gameupdatechange_113.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_113.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_113.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 337322)
    shipBuilder_gameupdatechange_113 = save_or_locate(shipBuilder_gameupdatechange_113)

    shipBuilder_gameupdatechange_114 = GameUpdateChange()
    shipBuilder_gameupdatechange_114.description = u"CHANGED: ItemPort Thruster Front Right Mid: flags changed from 'maneuver orientation +Z mid rear left' to 'maneuver orientation retro mid front right'"
    shipBuilder_gameupdatechange_114.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_114.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_114.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 339056)
    shipBuilder_gameupdatechange_114 = save_or_locate(shipBuilder_gameupdatechange_114)

    shipBuilder_gameupdatechange_115 = GameUpdateChange()
    shipBuilder_gameupdatechange_115.description = u"CHANGED: ItemPort Thruster Front Left Bottom: flags changed from 'maneuver orientation +Z lower rear left' to 'maneuver orientation retro lower front left'"
    shipBuilder_gameupdatechange_115.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_115.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_115.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 340777)
    shipBuilder_gameupdatechange_115 = save_or_locate(shipBuilder_gameupdatechange_115)

    shipBuilder_gameupdatechange_116 = GameUpdateChange()
    shipBuilder_gameupdatechange_116.description = u"CHANGED: ItemPort Thruster Front Left Upper: flags changed from 'maneuver orientation +Z upper rear left' to 'maneuver orientation retro upper front left'"
    shipBuilder_gameupdatechange_116.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_116.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_116.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 342503)
    shipBuilder_gameupdatechange_116 = save_or_locate(shipBuilder_gameupdatechange_116)

    shipBuilder_gameupdatechange_117 = GameUpdateChange()
    shipBuilder_gameupdatechange_117.description = u"CHANGED: ItemPort Thruster Front Left Mid: flags changed from 'maneuver orientation +Z mid rear left' to 'maneuver orientation retro mid front left'"
    shipBuilder_gameupdatechange_117.entityName = u'MISC_Freelancer'
    shipBuilder_gameupdatechange_117.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_117.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 344290)
    shipBuilder_gameupdatechange_117 = save_or_locate(shipBuilder_gameupdatechange_117)

    shipBuilder_gameupdatechange_118 = GameUpdateChange()
    shipBuilder_gameupdatechange_118.description = u"ADDED: New Vehicle 'Origin JumpWorks 300i'"
    shipBuilder_gameupdatechange_118.entityName = u'ORIG_300i'
    shipBuilder_gameupdatechange_118.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_118.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 530216)
    shipBuilder_gameupdatechange_118 = save_or_locate(shipBuilder_gameupdatechange_118)

    shipBuilder_gameupdatechange_119 = GameUpdateChange()
    shipBuilder_gameupdatechange_119.description = u"ADDED: New Vehicle 'RSI Aurora'"
    shipBuilder_gameupdatechange_119.entityName = u'RSI_Aurora'
    shipBuilder_gameupdatechange_119.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_119.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 684379)
    shipBuilder_gameupdatechange_119 = save_or_locate(shipBuilder_gameupdatechange_119)

    shipBuilder_gameupdatechange_120 = GameUpdateChange()
    shipBuilder_gameupdatechange_120.description = u"CHANGED: displayname changed from '' to 'RSI Constellation'"
    shipBuilder_gameupdatechange_120.entityName = u'RSI_Constellation'
    shipBuilder_gameupdatechange_120.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_120.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 779382)
    shipBuilder_gameupdatechange_120 = save_or_locate(shipBuilder_gameupdatechange_120)

    shipBuilder_gameupdatechange_121 = GameUpdateChange()
    shipBuilder_gameupdatechange_121.description = u"CHANGED: class changed from '1' to '3'"
    shipBuilder_gameupdatechange_121.entityName = u'RSI_Constellation'
    shipBuilder_gameupdatechange_121.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_121.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 783201)
    shipBuilder_gameupdatechange_121 = save_or_locate(shipBuilder_gameupdatechange_121)

    shipBuilder_gameupdatechange_122 = GameUpdateChange()
    shipBuilder_gameupdatechange_122.description = u"ADDED: New ItemPort 'Top Turret'"
    shipBuilder_gameupdatechange_122.entityName = u'RSI_Constellation'
    shipBuilder_gameupdatechange_122.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_122.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 787060)
    shipBuilder_gameupdatechange_122 = save_or_locate(shipBuilder_gameupdatechange_122)

    shipBuilder_gameupdatechange_123 = GameUpdateChange()
    shipBuilder_gameupdatechange_123.description = u"ADDED: New ItemPort 'Bottom Turret'"
    shipBuilder_gameupdatechange_123.entityName = u'RSI_Constellation'
    shipBuilder_gameupdatechange_123.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_123.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 788189)
    shipBuilder_gameupdatechange_123 = save_or_locate(shipBuilder_gameupdatechange_123)

    shipBuilder_gameupdatechange_124 = GameUpdateChange()
    shipBuilder_gameupdatechange_124.description = u"ADDED: New Vehicle 'RSI IR1337 Weapon Mount'"
    shipBuilder_gameupdatechange_124.entityName = u'RSI_IR1337_Weapon_Mount'
    shipBuilder_gameupdatechange_124.update = shipBuilder_gameupdate_2
    shipBuilder_gameupdatechange_124.creation_date = datetime.datetime(2013, 12, 25, 4, 32, 4, 848409)
    shipBuilder_gameupdatechange_124 = save_or_locate(shipBuilder_gameupdatechange_124)

    #Processing model: Hangar

    from shipBuilder.models import Hangar


    #Processing model: MigrationHistory

    from south.models import MigrationHistory


    #Processing model: LogEntry

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2013, 12, 24, 2, 56, 20, 669035)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="shipBuilder", model="hardpointtag")
    django_admin_log_1.object_id = u'1'
    django_admin_log_1.object_repr = u'HardpointTag object'
    django_admin_log_1.action_flag = 1
    django_admin_log_1.change_message = u''
    django_admin_log_1 = save_or_locate(django_admin_log_1)

    #Processing model: Item

    from shipBuilder.models import Item


    #Processing model: CargoModData

    from shipBuilder.models import CargoModData


    #Processing model: Hardpoint

    from shipBuilder.models import Hardpoint


    #Processing model: BuildHardpoint

    from shipBuilder.models import BuildHardpoint


    #Processing model: BuildEngineMod

    from shipBuilder.models import BuildEngineMod


    #Processing model: BuildHullMod

    from shipBuilder.models import BuildHullMod


    #Processing model: Build

    from shipBuilder.models import Build


    #Processing model: LocalizedDescriptionVehicle

    from shipBuilder.models import LocalizedDescriptionVehicle


    #Processing model: LocalizedDescriptionVehicleItem

    from shipBuilder.models import LocalizedDescriptionVehicleItem


    #Processing model: VehicleItemParams

    from shipBuilder.models import VehicleItemParams

    shipBuilder_vehicleitemparams_1 = VehicleItemParams()
    shipBuilder_vehicleitemparams_1.name = u'acceleration'
    shipBuilder_vehicleitemparams_1.value = 20.0
    shipBuilder_vehicleitemparams_1.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_1 = save_or_locate(shipBuilder_vehicleitemparams_1)

    shipBuilder_vehicleitemparams_2 = VehicleItemParams()
    shipBuilder_vehicleitemparams_2.name = u'pitchMax'
    shipBuilder_vehicleitemparams_2.value = 10.0
    shipBuilder_vehicleitemparams_2.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_2 = save_or_locate(shipBuilder_vehicleitemparams_2)

    shipBuilder_vehicleitemparams_3 = VehicleItemParams()
    shipBuilder_vehicleitemparams_3.name = u'maxThrust'
    shipBuilder_vehicleitemparams_3.value = 2600000.0
    shipBuilder_vehicleitemparams_3.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_3 = save_or_locate(shipBuilder_vehicleitemparams_3)

    shipBuilder_vehicleitemparams_4 = VehicleItemParams()
    shipBuilder_vehicleitemparams_4.name = u'pitchMin'
    shipBuilder_vehicleitemparams_4.value = -10.0
    shipBuilder_vehicleitemparams_4.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_4 = save_or_locate(shipBuilder_vehicleitemparams_4)

    shipBuilder_vehicleitemparams_5 = VehicleItemParams()
    shipBuilder_vehicleitemparams_5.name = u'yawMin'
    shipBuilder_vehicleitemparams_5.value = -10.0
    shipBuilder_vehicleitemparams_5.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_5 = save_or_locate(shipBuilder_vehicleitemparams_5)

    shipBuilder_vehicleitemparams_6 = VehicleItemParams()
    shipBuilder_vehicleitemparams_6.name = u'yawMax'
    shipBuilder_vehicleitemparams_6.value = 10.0
    shipBuilder_vehicleitemparams_6.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_6 = save_or_locate(shipBuilder_vehicleitemparams_6)

    shipBuilder_vehicleitemparams_7 = VehicleItemParams()
    shipBuilder_vehicleitemparams_7.name = u'speed'
    shipBuilder_vehicleitemparams_7.value = 40.0
    shipBuilder_vehicleitemparams_7.parentItem = shipBuilder_vehicleitem_2
    shipBuilder_vehicleitemparams_7 = save_or_locate(shipBuilder_vehicleitemparams_7)

    shipBuilder_vehicleitemparams_8 = VehicleItemParams()
    shipBuilder_vehicleitemparams_8.name = u'acceleration'
    shipBuilder_vehicleitemparams_8.value = 20.0
    shipBuilder_vehicleitemparams_8.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_8 = save_or_locate(shipBuilder_vehicleitemparams_8)

    shipBuilder_vehicleitemparams_9 = VehicleItemParams()
    shipBuilder_vehicleitemparams_9.name = u'pitchMax'
    shipBuilder_vehicleitemparams_9.value = 10.0
    shipBuilder_vehicleitemparams_9.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_9 = save_or_locate(shipBuilder_vehicleitemparams_9)

    shipBuilder_vehicleitemparams_10 = VehicleItemParams()
    shipBuilder_vehicleitemparams_10.name = u'maxThrust'
    shipBuilder_vehicleitemparams_10.value = 2600000.0
    shipBuilder_vehicleitemparams_10.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_10 = save_or_locate(shipBuilder_vehicleitemparams_10)

    shipBuilder_vehicleitemparams_11 = VehicleItemParams()
    shipBuilder_vehicleitemparams_11.name = u'pitchMin'
    shipBuilder_vehicleitemparams_11.value = -10.0
    shipBuilder_vehicleitemparams_11.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_11 = save_or_locate(shipBuilder_vehicleitemparams_11)

    shipBuilder_vehicleitemparams_12 = VehicleItemParams()
    shipBuilder_vehicleitemparams_12.name = u'yawMin'
    shipBuilder_vehicleitemparams_12.value = -10.0
    shipBuilder_vehicleitemparams_12.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_12 = save_or_locate(shipBuilder_vehicleitemparams_12)

    shipBuilder_vehicleitemparams_13 = VehicleItemParams()
    shipBuilder_vehicleitemparams_13.name = u'yawMax'
    shipBuilder_vehicleitemparams_13.value = 10.0
    shipBuilder_vehicleitemparams_13.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_13 = save_or_locate(shipBuilder_vehicleitemparams_13)

    shipBuilder_vehicleitemparams_14 = VehicleItemParams()
    shipBuilder_vehicleitemparams_14.name = u'speed'
    shipBuilder_vehicleitemparams_14.value = 40.0
    shipBuilder_vehicleitemparams_14.parentItem = shipBuilder_vehicleitem_3
    shipBuilder_vehicleitemparams_14 = save_or_locate(shipBuilder_vehicleitemparams_14)

    shipBuilder_vehicleitemparams_15 = VehicleItemParams()
    shipBuilder_vehicleitemparams_15.name = u'acceleration'
    shipBuilder_vehicleitemparams_15.value = 20.0
    shipBuilder_vehicleitemparams_15.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_15 = save_or_locate(shipBuilder_vehicleitemparams_15)

    shipBuilder_vehicleitemparams_16 = VehicleItemParams()
    shipBuilder_vehicleitemparams_16.name = u'pitchMax'
    shipBuilder_vehicleitemparams_16.value = 10.0
    shipBuilder_vehicleitemparams_16.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_16 = save_or_locate(shipBuilder_vehicleitemparams_16)

    shipBuilder_vehicleitemparams_17 = VehicleItemParams()
    shipBuilder_vehicleitemparams_17.name = u'maxThrust'
    shipBuilder_vehicleitemparams_17.value = 2600000.0
    shipBuilder_vehicleitemparams_17.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_17 = save_or_locate(shipBuilder_vehicleitemparams_17)

    shipBuilder_vehicleitemparams_18 = VehicleItemParams()
    shipBuilder_vehicleitemparams_18.name = u'pitchMin'
    shipBuilder_vehicleitemparams_18.value = -10.0
    shipBuilder_vehicleitemparams_18.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_18 = save_or_locate(shipBuilder_vehicleitemparams_18)

    shipBuilder_vehicleitemparams_19 = VehicleItemParams()
    shipBuilder_vehicleitemparams_19.name = u'yawMin'
    shipBuilder_vehicleitemparams_19.value = -10.0
    shipBuilder_vehicleitemparams_19.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_19 = save_or_locate(shipBuilder_vehicleitemparams_19)

    shipBuilder_vehicleitemparams_20 = VehicleItemParams()
    shipBuilder_vehicleitemparams_20.name = u'yawMax'
    shipBuilder_vehicleitemparams_20.value = 10.0
    shipBuilder_vehicleitemparams_20.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_20 = save_or_locate(shipBuilder_vehicleitemparams_20)

    shipBuilder_vehicleitemparams_21 = VehicleItemParams()
    shipBuilder_vehicleitemparams_21.name = u'speed'
    shipBuilder_vehicleitemparams_21.value = 40.0
    shipBuilder_vehicleitemparams_21.parentItem = shipBuilder_vehicleitem_4
    shipBuilder_vehicleitemparams_21 = save_or_locate(shipBuilder_vehicleitemparams_21)

    shipBuilder_vehicleitemparams_22 = VehicleItemParams()
    shipBuilder_vehicleitemparams_22.name = u'acceleration'
    shipBuilder_vehicleitemparams_22.value = 20.0
    shipBuilder_vehicleitemparams_22.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_22 = save_or_locate(shipBuilder_vehicleitemparams_22)

    shipBuilder_vehicleitemparams_23 = VehicleItemParams()
    shipBuilder_vehicleitemparams_23.name = u'pitchMax'
    shipBuilder_vehicleitemparams_23.value = 10.0
    shipBuilder_vehicleitemparams_23.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_23 = save_or_locate(shipBuilder_vehicleitemparams_23)

    shipBuilder_vehicleitemparams_24 = VehicleItemParams()
    shipBuilder_vehicleitemparams_24.name = u'maxThrust'
    shipBuilder_vehicleitemparams_24.value = 2600000.0
    shipBuilder_vehicleitemparams_24.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_24 = save_or_locate(shipBuilder_vehicleitemparams_24)

    shipBuilder_vehicleitemparams_25 = VehicleItemParams()
    shipBuilder_vehicleitemparams_25.name = u'pitchMin'
    shipBuilder_vehicleitemparams_25.value = -10.0
    shipBuilder_vehicleitemparams_25.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_25 = save_or_locate(shipBuilder_vehicleitemparams_25)

    shipBuilder_vehicleitemparams_26 = VehicleItemParams()
    shipBuilder_vehicleitemparams_26.name = u'yawMin'
    shipBuilder_vehicleitemparams_26.value = -10.0
    shipBuilder_vehicleitemparams_26.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_26 = save_or_locate(shipBuilder_vehicleitemparams_26)

    shipBuilder_vehicleitemparams_27 = VehicleItemParams()
    shipBuilder_vehicleitemparams_27.name = u'yawMax'
    shipBuilder_vehicleitemparams_27.value = 10.0
    shipBuilder_vehicleitemparams_27.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_27 = save_or_locate(shipBuilder_vehicleitemparams_27)

    shipBuilder_vehicleitemparams_28 = VehicleItemParams()
    shipBuilder_vehicleitemparams_28.name = u'speed'
    shipBuilder_vehicleitemparams_28.value = 40.0
    shipBuilder_vehicleitemparams_28.parentItem = shipBuilder_vehicleitem_13
    shipBuilder_vehicleitemparams_28 = save_or_locate(shipBuilder_vehicleitemparams_28)

    shipBuilder_vehicleitemparams_29 = VehicleItemParams()
    shipBuilder_vehicleitemparams_29.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_29.value = 40.0
    shipBuilder_vehicleitemparams_29.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_29 = save_or_locate(shipBuilder_vehicleitemparams_29)

    shipBuilder_vehicleitemparams_30 = VehicleItemParams()
    shipBuilder_vehicleitemparams_30.name = u'rollMax'
    shipBuilder_vehicleitemparams_30.value = 90.0
    shipBuilder_vehicleitemparams_30.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_30 = save_or_locate(shipBuilder_vehicleitemparams_30)

    shipBuilder_vehicleitemparams_31 = VehicleItemParams()
    shipBuilder_vehicleitemparams_31.name = u'maxThrust'
    shipBuilder_vehicleitemparams_31.value = 250000.0
    shipBuilder_vehicleitemparams_31.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_31 = save_or_locate(shipBuilder_vehicleitemparams_31)

    shipBuilder_vehicleitemparams_32 = VehicleItemParams()
    shipBuilder_vehicleitemparams_32.name = u'rollSpeed'
    shipBuilder_vehicleitemparams_32.value = 80.0
    shipBuilder_vehicleitemparams_32.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_32 = save_or_locate(shipBuilder_vehicleitemparams_32)

    shipBuilder_vehicleitemparams_33 = VehicleItemParams()
    shipBuilder_vehicleitemparams_33.name = u'rollAcceleration'
    shipBuilder_vehicleitemparams_33.value = 40.0
    shipBuilder_vehicleitemparams_33.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_33 = save_or_locate(shipBuilder_vehicleitemparams_33)

    shipBuilder_vehicleitemparams_34 = VehicleItemParams()
    shipBuilder_vehicleitemparams_34.name = u'yawMin'
    shipBuilder_vehicleitemparams_34.value = -90.0
    shipBuilder_vehicleitemparams_34.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_34 = save_or_locate(shipBuilder_vehicleitemparams_34)

    shipBuilder_vehicleitemparams_35 = VehicleItemParams()
    shipBuilder_vehicleitemparams_35.name = u'yawMax'
    shipBuilder_vehicleitemparams_35.value = 90.0
    shipBuilder_vehicleitemparams_35.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_35 = save_or_locate(shipBuilder_vehicleitemparams_35)

    shipBuilder_vehicleitemparams_36 = VehicleItemParams()
    shipBuilder_vehicleitemparams_36.name = u'rollMin'
    shipBuilder_vehicleitemparams_36.value = 0.0
    shipBuilder_vehicleitemparams_36.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_36 = save_or_locate(shipBuilder_vehicleitemparams_36)

    shipBuilder_vehicleitemparams_37 = VehicleItemParams()
    shipBuilder_vehicleitemparams_37.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_37.value = 80.0
    shipBuilder_vehicleitemparams_37.parentItem = shipBuilder_vehicleitem_17
    shipBuilder_vehicleitemparams_37 = save_or_locate(shipBuilder_vehicleitemparams_37)

    shipBuilder_vehicleitemparams_38 = VehicleItemParams()
    shipBuilder_vehicleitemparams_38.name = u'pitchMax'
    shipBuilder_vehicleitemparams_38.value = 90.0
    shipBuilder_vehicleitemparams_38.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_38 = save_or_locate(shipBuilder_vehicleitemparams_38)

    shipBuilder_vehicleitemparams_39 = VehicleItemParams()
    shipBuilder_vehicleitemparams_39.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_39.value = 40.0
    shipBuilder_vehicleitemparams_39.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_39 = save_or_locate(shipBuilder_vehicleitemparams_39)

    shipBuilder_vehicleitemparams_40 = VehicleItemParams()
    shipBuilder_vehicleitemparams_40.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_40.value = 40.0
    shipBuilder_vehicleitemparams_40.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_40 = save_or_locate(shipBuilder_vehicleitemparams_40)

    shipBuilder_vehicleitemparams_41 = VehicleItemParams()
    shipBuilder_vehicleitemparams_41.name = u'maxThrust'
    shipBuilder_vehicleitemparams_41.value = 350000.0
    shipBuilder_vehicleitemparams_41.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_41 = save_or_locate(shipBuilder_vehicleitemparams_41)

    shipBuilder_vehicleitemparams_42 = VehicleItemParams()
    shipBuilder_vehicleitemparams_42.name = u'yawMax'
    shipBuilder_vehicleitemparams_42.value = 0.0
    shipBuilder_vehicleitemparams_42.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_42 = save_or_locate(shipBuilder_vehicleitemparams_42)

    shipBuilder_vehicleitemparams_43 = VehicleItemParams()
    shipBuilder_vehicleitemparams_43.name = u'pitchMin'
    shipBuilder_vehicleitemparams_43.value = -90.0
    shipBuilder_vehicleitemparams_43.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_43 = save_or_locate(shipBuilder_vehicleitemparams_43)

    shipBuilder_vehicleitemparams_44 = VehicleItemParams()
    shipBuilder_vehicleitemparams_44.name = u'yawMin'
    shipBuilder_vehicleitemparams_44.value = -90.0
    shipBuilder_vehicleitemparams_44.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_44 = save_or_locate(shipBuilder_vehicleitemparams_44)

    shipBuilder_vehicleitemparams_45 = VehicleItemParams()
    shipBuilder_vehicleitemparams_45.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_45.value = 80.0
    shipBuilder_vehicleitemparams_45.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_45 = save_or_locate(shipBuilder_vehicleitemparams_45)

    shipBuilder_vehicleitemparams_46 = VehicleItemParams()
    shipBuilder_vehicleitemparams_46.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_46.value = 80.0
    shipBuilder_vehicleitemparams_46.parentItem = shipBuilder_vehicleitem_18
    shipBuilder_vehicleitemparams_46 = save_or_locate(shipBuilder_vehicleitemparams_46)

    shipBuilder_vehicleitemparams_47 = VehicleItemParams()
    shipBuilder_vehicleitemparams_47.name = u'pitchMax'
    shipBuilder_vehicleitemparams_47.value = 90.0
    shipBuilder_vehicleitemparams_47.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_47 = save_or_locate(shipBuilder_vehicleitemparams_47)

    shipBuilder_vehicleitemparams_48 = VehicleItemParams()
    shipBuilder_vehicleitemparams_48.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_48.value = 40.0
    shipBuilder_vehicleitemparams_48.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_48 = save_or_locate(shipBuilder_vehicleitemparams_48)

    shipBuilder_vehicleitemparams_49 = VehicleItemParams()
    shipBuilder_vehicleitemparams_49.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_49.value = 40.0
    shipBuilder_vehicleitemparams_49.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_49 = save_or_locate(shipBuilder_vehicleitemparams_49)

    shipBuilder_vehicleitemparams_50 = VehicleItemParams()
    shipBuilder_vehicleitemparams_50.name = u'maxThrust'
    shipBuilder_vehicleitemparams_50.value = 350000.0
    shipBuilder_vehicleitemparams_50.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_50 = save_or_locate(shipBuilder_vehicleitemparams_50)

    shipBuilder_vehicleitemparams_51 = VehicleItemParams()
    shipBuilder_vehicleitemparams_51.name = u'yawMax'
    shipBuilder_vehicleitemparams_51.value = 90.0
    shipBuilder_vehicleitemparams_51.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_51 = save_or_locate(shipBuilder_vehicleitemparams_51)

    shipBuilder_vehicleitemparams_52 = VehicleItemParams()
    shipBuilder_vehicleitemparams_52.name = u'pitchMin'
    shipBuilder_vehicleitemparams_52.value = -90.0
    shipBuilder_vehicleitemparams_52.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_52 = save_or_locate(shipBuilder_vehicleitemparams_52)

    shipBuilder_vehicleitemparams_53 = VehicleItemParams()
    shipBuilder_vehicleitemparams_53.name = u'yawMin'
    shipBuilder_vehicleitemparams_53.value = 0.0
    shipBuilder_vehicleitemparams_53.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_53 = save_or_locate(shipBuilder_vehicleitemparams_53)

    shipBuilder_vehicleitemparams_54 = VehicleItemParams()
    shipBuilder_vehicleitemparams_54.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_54.value = 80.0
    shipBuilder_vehicleitemparams_54.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_54 = save_or_locate(shipBuilder_vehicleitemparams_54)

    shipBuilder_vehicleitemparams_55 = VehicleItemParams()
    shipBuilder_vehicleitemparams_55.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_55.value = 80.0
    shipBuilder_vehicleitemparams_55.parentItem = shipBuilder_vehicleitem_19
    shipBuilder_vehicleitemparams_55 = save_or_locate(shipBuilder_vehicleitemparams_55)

    shipBuilder_vehicleitemparams_56 = VehicleItemParams()
    shipBuilder_vehicleitemparams_56.name = u'pitchMax'
    shipBuilder_vehicleitemparams_56.value = 90.0
    shipBuilder_vehicleitemparams_56.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_56 = save_or_locate(shipBuilder_vehicleitemparams_56)

    shipBuilder_vehicleitemparams_57 = VehicleItemParams()
    shipBuilder_vehicleitemparams_57.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_57.value = 40.0
    shipBuilder_vehicleitemparams_57.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_57 = save_or_locate(shipBuilder_vehicleitemparams_57)

    shipBuilder_vehicleitemparams_58 = VehicleItemParams()
    shipBuilder_vehicleitemparams_58.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_58.value = 40.0
    shipBuilder_vehicleitemparams_58.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_58 = save_or_locate(shipBuilder_vehicleitemparams_58)

    shipBuilder_vehicleitemparams_59 = VehicleItemParams()
    shipBuilder_vehicleitemparams_59.name = u'maxThrust'
    shipBuilder_vehicleitemparams_59.value = 250000.0
    shipBuilder_vehicleitemparams_59.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_59 = save_or_locate(shipBuilder_vehicleitemparams_59)

    shipBuilder_vehicleitemparams_60 = VehicleItemParams()
    shipBuilder_vehicleitemparams_60.name = u'yawMax'
    shipBuilder_vehicleitemparams_60.value = 0.0
    shipBuilder_vehicleitemparams_60.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_60 = save_or_locate(shipBuilder_vehicleitemparams_60)

    shipBuilder_vehicleitemparams_61 = VehicleItemParams()
    shipBuilder_vehicleitemparams_61.name = u'pitchMin'
    shipBuilder_vehicleitemparams_61.value = -90.0
    shipBuilder_vehicleitemparams_61.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_61 = save_or_locate(shipBuilder_vehicleitemparams_61)

    shipBuilder_vehicleitemparams_62 = VehicleItemParams()
    shipBuilder_vehicleitemparams_62.name = u'yawMin'
    shipBuilder_vehicleitemparams_62.value = -90.0
    shipBuilder_vehicleitemparams_62.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_62 = save_or_locate(shipBuilder_vehicleitemparams_62)

    shipBuilder_vehicleitemparams_63 = VehicleItemParams()
    shipBuilder_vehicleitemparams_63.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_63.value = 80.0
    shipBuilder_vehicleitemparams_63.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_63 = save_or_locate(shipBuilder_vehicleitemparams_63)

    shipBuilder_vehicleitemparams_64 = VehicleItemParams()
    shipBuilder_vehicleitemparams_64.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_64.value = 80.0
    shipBuilder_vehicleitemparams_64.parentItem = shipBuilder_vehicleitem_20
    shipBuilder_vehicleitemparams_64 = save_or_locate(shipBuilder_vehicleitemparams_64)

    shipBuilder_vehicleitemparams_65 = VehicleItemParams()
    shipBuilder_vehicleitemparams_65.name = u'pitchMax'
    shipBuilder_vehicleitemparams_65.value = 90.0
    shipBuilder_vehicleitemparams_65.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_65 = save_or_locate(shipBuilder_vehicleitemparams_65)

    shipBuilder_vehicleitemparams_66 = VehicleItemParams()
    shipBuilder_vehicleitemparams_66.name = u'yawAcceleration'
    shipBuilder_vehicleitemparams_66.value = 40.0
    shipBuilder_vehicleitemparams_66.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_66 = save_or_locate(shipBuilder_vehicleitemparams_66)

    shipBuilder_vehicleitemparams_67 = VehicleItemParams()
    shipBuilder_vehicleitemparams_67.name = u'pitchAcceleration'
    shipBuilder_vehicleitemparams_67.value = 40.0
    shipBuilder_vehicleitemparams_67.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_67 = save_or_locate(shipBuilder_vehicleitemparams_67)

    shipBuilder_vehicleitemparams_68 = VehicleItemParams()
    shipBuilder_vehicleitemparams_68.name = u'maxThrust'
    shipBuilder_vehicleitemparams_68.value = 250000.0
    shipBuilder_vehicleitemparams_68.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_68 = save_or_locate(shipBuilder_vehicleitemparams_68)

    shipBuilder_vehicleitemparams_69 = VehicleItemParams()
    shipBuilder_vehicleitemparams_69.name = u'yawMax'
    shipBuilder_vehicleitemparams_69.value = 0.0
    shipBuilder_vehicleitemparams_69.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_69 = save_or_locate(shipBuilder_vehicleitemparams_69)

    shipBuilder_vehicleitemparams_70 = VehicleItemParams()
    shipBuilder_vehicleitemparams_70.name = u'pitchMin'
    shipBuilder_vehicleitemparams_70.value = -90.0
    shipBuilder_vehicleitemparams_70.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_70 = save_or_locate(shipBuilder_vehicleitemparams_70)

    shipBuilder_vehicleitemparams_71 = VehicleItemParams()
    shipBuilder_vehicleitemparams_71.name = u'yawMin'
    shipBuilder_vehicleitemparams_71.value = -90.0
    shipBuilder_vehicleitemparams_71.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_71 = save_or_locate(shipBuilder_vehicleitemparams_71)

    shipBuilder_vehicleitemparams_72 = VehicleItemParams()
    shipBuilder_vehicleitemparams_72.name = u'pitchSpeed'
    shipBuilder_vehicleitemparams_72.value = 80.0
    shipBuilder_vehicleitemparams_72.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_72 = save_or_locate(shipBuilder_vehicleitemparams_72)

    shipBuilder_vehicleitemparams_73 = VehicleItemParams()
    shipBuilder_vehicleitemparams_73.name = u'yawSpeed'
    shipBuilder_vehicleitemparams_73.value = 80.0
    shipBuilder_vehicleitemparams_73.parentItem = shipBuilder_vehicleitem_21
    shipBuilder_vehicleitemparams_73 = save_or_locate(shipBuilder_vehicleitemparams_73)

    shipBuilder_vehicleitemparams_74 = VehicleItemParams()
    shipBuilder_vehicleitemparams_74.name = u'acceleration'
    shipBuilder_vehicleitemparams_74.value = 40.0
    shipBuilder_vehicleitemparams_74.parentItem = shipBuilder_vehicleitem_22
    shipBuilder_vehicleitemparams_74 = save_or_locate(shipBuilder_vehicleitemparams_74)

    shipBuilder_vehicleitemparams_75 = VehicleItemParams()
    shipBuilder_vehicleitemparams_75.name = u'maxThrust'
    shipBuilder_vehicleitemparams_75.value = 300000.0
    shipBuilder_vehicleitemparams_75.parentItem = shipBuilder_vehicleitem_22
    shipBuilder_vehicleitemparams_75 = save_or_locate(shipBuilder_vehicleitemparams_75)

    shipBuilder_vehicleitemparams_76 = VehicleItemParams()
    shipBuilder_vehicleitemparams_76.name = u'speed'
    shipBuilder_vehicleitemparams_76.value = 80.0
    shipBuilder_vehicleitemparams_76.parentItem = shipBuilder_vehicleitem_22
    shipBuilder_vehicleitemparams_76 = save_or_locate(shipBuilder_vehicleitemparams_76)

    shipBuilder_vehicleitemparams_77 = VehicleItemParams()
    shipBuilder_vehicleitemparams_77.name = u'pitchMin'
    shipBuilder_vehicleitemparams_77.value = 0.0
    shipBuilder_vehicleitemparams_77.parentItem = shipBuilder_vehicleitem_22
    shipBuilder_vehicleitemparams_77 = save_or_locate(shipBuilder_vehicleitemparams_77)

    shipBuilder_vehicleitemparams_78 = VehicleItemParams()
    shipBuilder_vehicleitemparams_78.name = u'pitchMax'
    shipBuilder_vehicleitemparams_78.value = 180.0
    shipBuilder_vehicleitemparams_78.parentItem = shipBuilder_vehicleitem_22
    shipBuilder_vehicleitemparams_78 = save_or_locate(shipBuilder_vehicleitemparams_78)

    shipBuilder_vehicleitemparams_79 = VehicleItemParams()
    shipBuilder_vehicleitemparams_79.name = u'acceleration'
    shipBuilder_vehicleitemparams_79.value = 40.0
    shipBuilder_vehicleitemparams_79.parentItem = shipBuilder_vehicleitem_23
    shipBuilder_vehicleitemparams_79 = save_or_locate(shipBuilder_vehicleitemparams_79)

    shipBuilder_vehicleitemparams_80 = VehicleItemParams()
    shipBuilder_vehicleitemparams_80.name = u'maxThrust'
    shipBuilder_vehicleitemparams_80.value = 300000.0
    shipBuilder_vehicleitemparams_80.parentItem = shipBuilder_vehicleitem_23
    shipBuilder_vehicleitemparams_80 = save_or_locate(shipBuilder_vehicleitemparams_80)

    shipBuilder_vehicleitemparams_81 = VehicleItemParams()
    shipBuilder_vehicleitemparams_81.name = u'speed'
    shipBuilder_vehicleitemparams_81.value = 80.0
    shipBuilder_vehicleitemparams_81.parentItem = shipBuilder_vehicleitem_23
    shipBuilder_vehicleitemparams_81 = save_or_locate(shipBuilder_vehicleitemparams_81)

    shipBuilder_vehicleitemparams_82 = VehicleItemParams()
    shipBuilder_vehicleitemparams_82.name = u'pitchMin'
    shipBuilder_vehicleitemparams_82.value = -180.0
    shipBuilder_vehicleitemparams_82.parentItem = shipBuilder_vehicleitem_23
    shipBuilder_vehicleitemparams_82 = save_or_locate(shipBuilder_vehicleitemparams_82)

    shipBuilder_vehicleitemparams_83 = VehicleItemParams()
    shipBuilder_vehicleitemparams_83.name = u'pitchMax'
    shipBuilder_vehicleitemparams_83.value = 180.0
    shipBuilder_vehicleitemparams_83.parentItem = shipBuilder_vehicleitem_23
    shipBuilder_vehicleitemparams_83 = save_or_locate(shipBuilder_vehicleitemparams_83)

    shipBuilder_vehicleitemparams_84 = VehicleItemParams()
    shipBuilder_vehicleitemparams_84.name = u'acceleration'
    shipBuilder_vehicleitemparams_84.value = 20.0
    shipBuilder_vehicleitemparams_84.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_84 = save_or_locate(shipBuilder_vehicleitemparams_84)

    shipBuilder_vehicleitemparams_85 = VehicleItemParams()
    shipBuilder_vehicleitemparams_85.name = u'pitchMax'
    shipBuilder_vehicleitemparams_85.value = 10.0
    shipBuilder_vehicleitemparams_85.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_85 = save_or_locate(shipBuilder_vehicleitemparams_85)

    shipBuilder_vehicleitemparams_86 = VehicleItemParams()
    shipBuilder_vehicleitemparams_86.name = u'maxThrust'
    shipBuilder_vehicleitemparams_86.value = 2600000.0
    shipBuilder_vehicleitemparams_86.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_86 = save_or_locate(shipBuilder_vehicleitemparams_86)

    shipBuilder_vehicleitemparams_87 = VehicleItemParams()
    shipBuilder_vehicleitemparams_87.name = u'pitchMin'
    shipBuilder_vehicleitemparams_87.value = -10.0
    shipBuilder_vehicleitemparams_87.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_87 = save_or_locate(shipBuilder_vehicleitemparams_87)

    shipBuilder_vehicleitemparams_88 = VehicleItemParams()
    shipBuilder_vehicleitemparams_88.name = u'yawMin'
    shipBuilder_vehicleitemparams_88.value = -10.0
    shipBuilder_vehicleitemparams_88.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_88 = save_or_locate(shipBuilder_vehicleitemparams_88)

    shipBuilder_vehicleitemparams_89 = VehicleItemParams()
    shipBuilder_vehicleitemparams_89.name = u'yawMax'
    shipBuilder_vehicleitemparams_89.value = 10.0
    shipBuilder_vehicleitemparams_89.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_89 = save_or_locate(shipBuilder_vehicleitemparams_89)

    shipBuilder_vehicleitemparams_90 = VehicleItemParams()
    shipBuilder_vehicleitemparams_90.name = u'speed'
    shipBuilder_vehicleitemparams_90.value = 40.0
    shipBuilder_vehicleitemparams_90.parentItem = shipBuilder_vehicleitem_24
    shipBuilder_vehicleitemparams_90 = save_or_locate(shipBuilder_vehicleitemparams_90)

    shipBuilder_vehicleitemparams_91 = VehicleItemParams()
    shipBuilder_vehicleitemparams_91.name = u'RoF'
    shipBuilder_vehicleitemparams_91.value = 3.0
    shipBuilder_vehicleitemparams_91.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemparams_91 = save_or_locate(shipBuilder_vehicleitemparams_91)

    shipBuilder_vehicleitemparams_92 = VehicleItemParams()
    shipBuilder_vehicleitemparams_92.name = u'Range'
    shipBuilder_vehicleitemparams_92.value = 90.0
    shipBuilder_vehicleitemparams_92.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemparams_92 = save_or_locate(shipBuilder_vehicleitemparams_92)

    shipBuilder_vehicleitemparams_93 = VehicleItemParams()
    shipBuilder_vehicleitemparams_93.name = u'Damage'
    shipBuilder_vehicleitemparams_93.value = 2.5
    shipBuilder_vehicleitemparams_93.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemparams_93 = save_or_locate(shipBuilder_vehicleitemparams_93)

    shipBuilder_vehicleitemparams_94 = VehicleItemParams()
    shipBuilder_vehicleitemparams_94.name = u'Power'
    shipBuilder_vehicleitemparams_94.value = 19.5
    shipBuilder_vehicleitemparams_94.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemparams_94 = save_or_locate(shipBuilder_vehicleitemparams_94)

    shipBuilder_vehicleitemparams_95 = VehicleItemParams()
    shipBuilder_vehicleitemparams_95.name = u'RoF'
    shipBuilder_vehicleitemparams_95.value = 20.0
    shipBuilder_vehicleitemparams_95.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemparams_95 = save_or_locate(shipBuilder_vehicleitemparams_95)

    shipBuilder_vehicleitemparams_96 = VehicleItemParams()
    shipBuilder_vehicleitemparams_96.name = u'Range'
    shipBuilder_vehicleitemparams_96.value = 90.0
    shipBuilder_vehicleitemparams_96.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemparams_96 = save_or_locate(shipBuilder_vehicleitemparams_96)

    shipBuilder_vehicleitemparams_97 = VehicleItemParams()
    shipBuilder_vehicleitemparams_97.name = u'Damage'
    shipBuilder_vehicleitemparams_97.value = 3.5
    shipBuilder_vehicleitemparams_97.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemparams_97 = save_or_locate(shipBuilder_vehicleitemparams_97)

    shipBuilder_vehicleitemparams_98 = VehicleItemParams()
    shipBuilder_vehicleitemparams_98.name = u'Power'
    shipBuilder_vehicleitemparams_98.value = 27.3
    shipBuilder_vehicleitemparams_98.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemparams_98 = save_or_locate(shipBuilder_vehicleitemparams_98)

    shipBuilder_vehicleitemparams_99 = VehicleItemParams()
    shipBuilder_vehicleitemparams_99.name = u'RoF'
    shipBuilder_vehicleitemparams_99.value = 20.0
    shipBuilder_vehicleitemparams_99.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemparams_99 = save_or_locate(shipBuilder_vehicleitemparams_99)

    shipBuilder_vehicleitemparams_100 = VehicleItemParams()
    shipBuilder_vehicleitemparams_100.name = u'Range'
    shipBuilder_vehicleitemparams_100.value = 90.0
    shipBuilder_vehicleitemparams_100.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemparams_100 = save_or_locate(shipBuilder_vehicleitemparams_100)

    shipBuilder_vehicleitemparams_101 = VehicleItemParams()
    shipBuilder_vehicleitemparams_101.name = u'Damage'
    shipBuilder_vehicleitemparams_101.value = 4.5
    shipBuilder_vehicleitemparams_101.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemparams_101 = save_or_locate(shipBuilder_vehicleitemparams_101)

    shipBuilder_vehicleitemparams_102 = VehicleItemParams()
    shipBuilder_vehicleitemparams_102.name = u'Power'
    shipBuilder_vehicleitemparams_102.value = 35.1
    shipBuilder_vehicleitemparams_102.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemparams_102 = save_or_locate(shipBuilder_vehicleitemparams_102)

    shipBuilder_vehicleitemparams_103 = VehicleItemParams()
    shipBuilder_vehicleitemparams_103.name = u'Speed'
    shipBuilder_vehicleitemparams_103.value = 80.0
    shipBuilder_vehicleitemparams_103.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemparams_103 = save_or_locate(shipBuilder_vehicleitemparams_103)

    shipBuilder_vehicleitemparams_104 = VehicleItemParams()
    shipBuilder_vehicleitemparams_104.name = u'Warhead'
    shipBuilder_vehicleitemparams_104.value = 51.43
    shipBuilder_vehicleitemparams_104.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemparams_104 = save_or_locate(shipBuilder_vehicleitemparams_104)

    shipBuilder_vehicleitemparams_105 = VehicleItemParams()
    shipBuilder_vehicleitemparams_105.name = u'Radius'
    shipBuilder_vehicleitemparams_105.value = 66.67
    shipBuilder_vehicleitemparams_105.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemparams_105 = save_or_locate(shipBuilder_vehicleitemparams_105)

    shipBuilder_vehicleitemparams_106 = VehicleItemParams()
    shipBuilder_vehicleitemparams_106.name = u'Concuss'
    shipBuilder_vehicleitemparams_106.value = 66.67
    shipBuilder_vehicleitemparams_106.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemparams_106 = save_or_locate(shipBuilder_vehicleitemparams_106)

    shipBuilder_vehicleitemparams_107 = VehicleItemParams()
    shipBuilder_vehicleitemparams_107.name = u'Speed'
    shipBuilder_vehicleitemparams_107.value = 80.0
    shipBuilder_vehicleitemparams_107.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemparams_107 = save_or_locate(shipBuilder_vehicleitemparams_107)

    shipBuilder_vehicleitemparams_108 = VehicleItemParams()
    shipBuilder_vehicleitemparams_108.name = u'Warhead'
    shipBuilder_vehicleitemparams_108.value = 51.43
    shipBuilder_vehicleitemparams_108.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemparams_108 = save_or_locate(shipBuilder_vehicleitemparams_108)

    shipBuilder_vehicleitemparams_109 = VehicleItemParams()
    shipBuilder_vehicleitemparams_109.name = u'Radius'
    shipBuilder_vehicleitemparams_109.value = 66.67
    shipBuilder_vehicleitemparams_109.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemparams_109 = save_or_locate(shipBuilder_vehicleitemparams_109)

    shipBuilder_vehicleitemparams_110 = VehicleItemParams()
    shipBuilder_vehicleitemparams_110.name = u'Concuss'
    shipBuilder_vehicleitemparams_110.value = 66.67
    shipBuilder_vehicleitemparams_110.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemparams_110 = save_or_locate(shipBuilder_vehicleitemparams_110)

    shipBuilder_vehicleitemparams_111 = VehicleItemParams()
    shipBuilder_vehicleitemparams_111.name = u'RoF'
    shipBuilder_vehicleitemparams_111.value = 20.0
    shipBuilder_vehicleitemparams_111.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemparams_111 = save_or_locate(shipBuilder_vehicleitemparams_111)

    shipBuilder_vehicleitemparams_112 = VehicleItemParams()
    shipBuilder_vehicleitemparams_112.name = u'Range'
    shipBuilder_vehicleitemparams_112.value = 90.0
    shipBuilder_vehicleitemparams_112.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemparams_112 = save_or_locate(shipBuilder_vehicleitemparams_112)

    shipBuilder_vehicleitemparams_113 = VehicleItemParams()
    shipBuilder_vehicleitemparams_113.name = u'Damage'
    shipBuilder_vehicleitemparams_113.value = 5.5
    shipBuilder_vehicleitemparams_113.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemparams_113 = save_or_locate(shipBuilder_vehicleitemparams_113)

    shipBuilder_vehicleitemparams_114 = VehicleItemParams()
    shipBuilder_vehicleitemparams_114.name = u'Power'
    shipBuilder_vehicleitemparams_114.value = 46.8
    shipBuilder_vehicleitemparams_114.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemparams_114 = save_or_locate(shipBuilder_vehicleitemparams_114)

    shipBuilder_vehicleitemparams_115 = VehicleItemParams()
    shipBuilder_vehicleitemparams_115.name = u'acceleration'
    shipBuilder_vehicleitemparams_115.value = 20.0
    shipBuilder_vehicleitemparams_115.parentItem = shipBuilder_vehicleitem_32
    shipBuilder_vehicleitemparams_115 = save_or_locate(shipBuilder_vehicleitemparams_115)

    shipBuilder_vehicleitemparams_116 = VehicleItemParams()
    shipBuilder_vehicleitemparams_116.name = u'maxThrust'
    shipBuilder_vehicleitemparams_116.value = 2600000.0
    shipBuilder_vehicleitemparams_116.parentItem = shipBuilder_vehicleitem_32
    shipBuilder_vehicleitemparams_116 = save_or_locate(shipBuilder_vehicleitemparams_116)

    shipBuilder_vehicleitemparams_117 = VehicleItemParams()
    shipBuilder_vehicleitemparams_117.name = u'speed'
    shipBuilder_vehicleitemparams_117.value = 40.0
    shipBuilder_vehicleitemparams_117.parentItem = shipBuilder_vehicleitem_32
    shipBuilder_vehicleitemparams_117 = save_or_locate(shipBuilder_vehicleitemparams_117)

    shipBuilder_vehicleitemparams_118 = VehicleItemParams()
    shipBuilder_vehicleitemparams_118.name = u'acceleration'
    shipBuilder_vehicleitemparams_118.value = 20.0
    shipBuilder_vehicleitemparams_118.parentItem = shipBuilder_vehicleitem_33
    shipBuilder_vehicleitemparams_118 = save_or_locate(shipBuilder_vehicleitemparams_118)

    shipBuilder_vehicleitemparams_119 = VehicleItemParams()
    shipBuilder_vehicleitemparams_119.name = u'maxThrust'
    shipBuilder_vehicleitemparams_119.value = 2600000.0
    shipBuilder_vehicleitemparams_119.parentItem = shipBuilder_vehicleitem_33
    shipBuilder_vehicleitemparams_119 = save_or_locate(shipBuilder_vehicleitemparams_119)

    shipBuilder_vehicleitemparams_120 = VehicleItemParams()
    shipBuilder_vehicleitemparams_120.name = u'speed'
    shipBuilder_vehicleitemparams_120.value = 40.0
    shipBuilder_vehicleitemparams_120.parentItem = shipBuilder_vehicleitem_33
    shipBuilder_vehicleitemparams_120 = save_or_locate(shipBuilder_vehicleitemparams_120)

    shipBuilder_vehicleitemparams_121 = VehicleItemParams()
    shipBuilder_vehicleitemparams_121.name = u'acceleration'
    shipBuilder_vehicleitemparams_121.value = 20.0
    shipBuilder_vehicleitemparams_121.parentItem = shipBuilder_vehicleitem_34
    shipBuilder_vehicleitemparams_121 = save_or_locate(shipBuilder_vehicleitemparams_121)

    shipBuilder_vehicleitemparams_122 = VehicleItemParams()
    shipBuilder_vehicleitemparams_122.name = u'maxThrust'
    shipBuilder_vehicleitemparams_122.value = 2600000.0
    shipBuilder_vehicleitemparams_122.parentItem = shipBuilder_vehicleitem_34
    shipBuilder_vehicleitemparams_122 = save_or_locate(shipBuilder_vehicleitemparams_122)

    shipBuilder_vehicleitemparams_123 = VehicleItemParams()
    shipBuilder_vehicleitemparams_123.name = u'speed'
    shipBuilder_vehicleitemparams_123.value = 40.0
    shipBuilder_vehicleitemparams_123.parentItem = shipBuilder_vehicleitem_34
    shipBuilder_vehicleitemparams_123 = save_or_locate(shipBuilder_vehicleitemparams_123)

    shipBuilder_vehicleitemparams_124 = VehicleItemParams()
    shipBuilder_vehicleitemparams_124.name = u'acceleration'
    shipBuilder_vehicleitemparams_124.value = 20.0
    shipBuilder_vehicleitemparams_124.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_124 = save_or_locate(shipBuilder_vehicleitemparams_124)

    shipBuilder_vehicleitemparams_125 = VehicleItemParams()
    shipBuilder_vehicleitemparams_125.name = u'pitchMax'
    shipBuilder_vehicleitemparams_125.value = 10.0
    shipBuilder_vehicleitemparams_125.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_125 = save_or_locate(shipBuilder_vehicleitemparams_125)

    shipBuilder_vehicleitemparams_126 = VehicleItemParams()
    shipBuilder_vehicleitemparams_126.name = u'maxThrust'
    shipBuilder_vehicleitemparams_126.value = 2600000.0
    shipBuilder_vehicleitemparams_126.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_126 = save_or_locate(shipBuilder_vehicleitemparams_126)

    shipBuilder_vehicleitemparams_127 = VehicleItemParams()
    shipBuilder_vehicleitemparams_127.name = u'pitchMin'
    shipBuilder_vehicleitemparams_127.value = -10.0
    shipBuilder_vehicleitemparams_127.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_127 = save_or_locate(shipBuilder_vehicleitemparams_127)

    shipBuilder_vehicleitemparams_128 = VehicleItemParams()
    shipBuilder_vehicleitemparams_128.name = u'yawMin'
    shipBuilder_vehicleitemparams_128.value = -10.0
    shipBuilder_vehicleitemparams_128.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_128 = save_or_locate(shipBuilder_vehicleitemparams_128)

    shipBuilder_vehicleitemparams_129 = VehicleItemParams()
    shipBuilder_vehicleitemparams_129.name = u'yawMax'
    shipBuilder_vehicleitemparams_129.value = 10.0
    shipBuilder_vehicleitemparams_129.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_129 = save_or_locate(shipBuilder_vehicleitemparams_129)

    shipBuilder_vehicleitemparams_130 = VehicleItemParams()
    shipBuilder_vehicleitemparams_130.name = u'speed'
    shipBuilder_vehicleitemparams_130.value = 40.0
    shipBuilder_vehicleitemparams_130.parentItem = shipBuilder_vehicleitem_37
    shipBuilder_vehicleitemparams_130 = save_or_locate(shipBuilder_vehicleitemparams_130)

    shipBuilder_vehicleitemparams_131 = VehicleItemParams()
    shipBuilder_vehicleitemparams_131.name = u'acceleration'
    shipBuilder_vehicleitemparams_131.value = 20.0
    shipBuilder_vehicleitemparams_131.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_131 = save_or_locate(shipBuilder_vehicleitemparams_131)

    shipBuilder_vehicleitemparams_132 = VehicleItemParams()
    shipBuilder_vehicleitemparams_132.name = u'pitchMax'
    shipBuilder_vehicleitemparams_132.value = 10.0
    shipBuilder_vehicleitemparams_132.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_132 = save_or_locate(shipBuilder_vehicleitemparams_132)

    shipBuilder_vehicleitemparams_133 = VehicleItemParams()
    shipBuilder_vehicleitemparams_133.name = u'maxThrust'
    shipBuilder_vehicleitemparams_133.value = 2600000.0
    shipBuilder_vehicleitemparams_133.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_133 = save_or_locate(shipBuilder_vehicleitemparams_133)

    shipBuilder_vehicleitemparams_134 = VehicleItemParams()
    shipBuilder_vehicleitemparams_134.name = u'pitchMin'
    shipBuilder_vehicleitemparams_134.value = -10.0
    shipBuilder_vehicleitemparams_134.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_134 = save_or_locate(shipBuilder_vehicleitemparams_134)

    shipBuilder_vehicleitemparams_135 = VehicleItemParams()
    shipBuilder_vehicleitemparams_135.name = u'yawMin'
    shipBuilder_vehicleitemparams_135.value = -10.0
    shipBuilder_vehicleitemparams_135.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_135 = save_or_locate(shipBuilder_vehicleitemparams_135)

    shipBuilder_vehicleitemparams_136 = VehicleItemParams()
    shipBuilder_vehicleitemparams_136.name = u'yawMax'
    shipBuilder_vehicleitemparams_136.value = 10.0
    shipBuilder_vehicleitemparams_136.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_136 = save_or_locate(shipBuilder_vehicleitemparams_136)

    shipBuilder_vehicleitemparams_137 = VehicleItemParams()
    shipBuilder_vehicleitemparams_137.name = u'speed'
    shipBuilder_vehicleitemparams_137.value = 40.0
    shipBuilder_vehicleitemparams_137.parentItem = shipBuilder_vehicleitem_38
    shipBuilder_vehicleitemparams_137 = save_or_locate(shipBuilder_vehicleitemparams_137)

    shipBuilder_vehicleitemparams_138 = VehicleItemParams()
    shipBuilder_vehicleitemparams_138.name = u'acceleration'
    shipBuilder_vehicleitemparams_138.value = 20.0
    shipBuilder_vehicleitemparams_138.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_138 = save_or_locate(shipBuilder_vehicleitemparams_138)

    shipBuilder_vehicleitemparams_139 = VehicleItemParams()
    shipBuilder_vehicleitemparams_139.name = u'pitchMax'
    shipBuilder_vehicleitemparams_139.value = 10.0
    shipBuilder_vehicleitemparams_139.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_139 = save_or_locate(shipBuilder_vehicleitemparams_139)

    shipBuilder_vehicleitemparams_140 = VehicleItemParams()
    shipBuilder_vehicleitemparams_140.name = u'maxThrust'
    shipBuilder_vehicleitemparams_140.value = 2600000.0
    shipBuilder_vehicleitemparams_140.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_140 = save_or_locate(shipBuilder_vehicleitemparams_140)

    shipBuilder_vehicleitemparams_141 = VehicleItemParams()
    shipBuilder_vehicleitemparams_141.name = u'pitchMin'
    shipBuilder_vehicleitemparams_141.value = -10.0
    shipBuilder_vehicleitemparams_141.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_141 = save_or_locate(shipBuilder_vehicleitemparams_141)

    shipBuilder_vehicleitemparams_142 = VehicleItemParams()
    shipBuilder_vehicleitemparams_142.name = u'yawMin'
    shipBuilder_vehicleitemparams_142.value = -10.0
    shipBuilder_vehicleitemparams_142.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_142 = save_or_locate(shipBuilder_vehicleitemparams_142)

    shipBuilder_vehicleitemparams_143 = VehicleItemParams()
    shipBuilder_vehicleitemparams_143.name = u'yawMax'
    shipBuilder_vehicleitemparams_143.value = 10.0
    shipBuilder_vehicleitemparams_143.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_143 = save_or_locate(shipBuilder_vehicleitemparams_143)

    shipBuilder_vehicleitemparams_144 = VehicleItemParams()
    shipBuilder_vehicleitemparams_144.name = u'speed'
    shipBuilder_vehicleitemparams_144.value = 40.0
    shipBuilder_vehicleitemparams_144.parentItem = shipBuilder_vehicleitem_39
    shipBuilder_vehicleitemparams_144 = save_or_locate(shipBuilder_vehicleitemparams_144)

    shipBuilder_vehicleitemparams_145 = VehicleItemParams()
    shipBuilder_vehicleitemparams_145.name = u'RoF'
    shipBuilder_vehicleitemparams_145.value = 60.0
    shipBuilder_vehicleitemparams_145.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemparams_145 = save_or_locate(shipBuilder_vehicleitemparams_145)

    shipBuilder_vehicleitemparams_146 = VehicleItemParams()
    shipBuilder_vehicleitemparams_146.name = u'Range'
    shipBuilder_vehicleitemparams_146.value = 60.0
    shipBuilder_vehicleitemparams_146.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemparams_146 = save_or_locate(shipBuilder_vehicleitemparams_146)

    shipBuilder_vehicleitemparams_147 = VehicleItemParams()
    shipBuilder_vehicleitemparams_147.name = u'Damage'
    shipBuilder_vehicleitemparams_147.value = 1.0
    shipBuilder_vehicleitemparams_147.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemparams_147 = save_or_locate(shipBuilder_vehicleitemparams_147)

    shipBuilder_vehicleitemparams_148 = VehicleItemParams()
    shipBuilder_vehicleitemparams_148.name = u'Power'
    shipBuilder_vehicleitemparams_148.value = 27.0
    shipBuilder_vehicleitemparams_148.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemparams_148 = save_or_locate(shipBuilder_vehicleitemparams_148)

    shipBuilder_vehicleitemparams_149 = VehicleItemParams()
    shipBuilder_vehicleitemparams_149.name = u'RoF'
    shipBuilder_vehicleitemparams_149.value = 60.0
    shipBuilder_vehicleitemparams_149.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemparams_149 = save_or_locate(shipBuilder_vehicleitemparams_149)

    shipBuilder_vehicleitemparams_150 = VehicleItemParams()
    shipBuilder_vehicleitemparams_150.name = u'Range'
    shipBuilder_vehicleitemparams_150.value = 60.0
    shipBuilder_vehicleitemparams_150.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemparams_150 = save_or_locate(shipBuilder_vehicleitemparams_150)

    shipBuilder_vehicleitemparams_151 = VehicleItemParams()
    shipBuilder_vehicleitemparams_151.name = u'Damage'
    shipBuilder_vehicleitemparams_151.value = 1.25
    shipBuilder_vehicleitemparams_151.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemparams_151 = save_or_locate(shipBuilder_vehicleitemparams_151)

    shipBuilder_vehicleitemparams_152 = VehicleItemParams()
    shipBuilder_vehicleitemparams_152.name = u'Power'
    shipBuilder_vehicleitemparams_152.value = 32.4
    shipBuilder_vehicleitemparams_152.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemparams_152 = save_or_locate(shipBuilder_vehicleitemparams_152)

    shipBuilder_vehicleitemparams_153 = VehicleItemParams()
    shipBuilder_vehicleitemparams_153.name = u'RoF'
    shipBuilder_vehicleitemparams_153.value = 60.0
    shipBuilder_vehicleitemparams_153.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemparams_153 = save_or_locate(shipBuilder_vehicleitemparams_153)

    shipBuilder_vehicleitemparams_154 = VehicleItemParams()
    shipBuilder_vehicleitemparams_154.name = u'Range'
    shipBuilder_vehicleitemparams_154.value = 60.0
    shipBuilder_vehicleitemparams_154.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemparams_154 = save_or_locate(shipBuilder_vehicleitemparams_154)

    shipBuilder_vehicleitemparams_155 = VehicleItemParams()
    shipBuilder_vehicleitemparams_155.name = u'Damage'
    shipBuilder_vehicleitemparams_155.value = 1.5
    shipBuilder_vehicleitemparams_155.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemparams_155 = save_or_locate(shipBuilder_vehicleitemparams_155)

    shipBuilder_vehicleitemparams_156 = VehicleItemParams()
    shipBuilder_vehicleitemparams_156.name = u'Power'
    shipBuilder_vehicleitemparams_156.value = 37.8
    shipBuilder_vehicleitemparams_156.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemparams_156 = save_or_locate(shipBuilder_vehicleitemparams_156)

    shipBuilder_vehicleitemparams_157 = VehicleItemParams()
    shipBuilder_vehicleitemparams_157.name = u'RoF'
    shipBuilder_vehicleitemparams_157.value = 6.67
    shipBuilder_vehicleitemparams_157.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemparams_157 = save_or_locate(shipBuilder_vehicleitemparams_157)

    shipBuilder_vehicleitemparams_158 = VehicleItemParams()
    shipBuilder_vehicleitemparams_158.name = u'Range'
    shipBuilder_vehicleitemparams_158.value = 90.0
    shipBuilder_vehicleitemparams_158.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemparams_158 = save_or_locate(shipBuilder_vehicleitemparams_158)

    shipBuilder_vehicleitemparams_159 = VehicleItemParams()
    shipBuilder_vehicleitemparams_159.name = u'Damage'
    shipBuilder_vehicleitemparams_159.value = 10.0
    shipBuilder_vehicleitemparams_159.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemparams_159 = save_or_locate(shipBuilder_vehicleitemparams_159)

    shipBuilder_vehicleitemparams_160 = VehicleItemParams()
    shipBuilder_vehicleitemparams_160.name = u'Power'
    shipBuilder_vehicleitemparams_160.value = 4.0
    shipBuilder_vehicleitemparams_160.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemparams_160 = save_or_locate(shipBuilder_vehicleitemparams_160)

    shipBuilder_vehicleitemparams_161 = VehicleItemParams()
    shipBuilder_vehicleitemparams_161.name = u'acceleration'
    shipBuilder_vehicleitemparams_161.value = 40.0
    shipBuilder_vehicleitemparams_161.parentItem = shipBuilder_vehicleitem_48
    shipBuilder_vehicleitemparams_161 = save_or_locate(shipBuilder_vehicleitemparams_161)

    shipBuilder_vehicleitemparams_162 = VehicleItemParams()
    shipBuilder_vehicleitemparams_162.name = u'maxThrust'
    shipBuilder_vehicleitemparams_162.value = 300000.0
    shipBuilder_vehicleitemparams_162.parentItem = shipBuilder_vehicleitem_48
    shipBuilder_vehicleitemparams_162 = save_or_locate(shipBuilder_vehicleitemparams_162)

    shipBuilder_vehicleitemparams_163 = VehicleItemParams()
    shipBuilder_vehicleitemparams_163.name = u'speed'
    shipBuilder_vehicleitemparams_163.value = 80.0
    shipBuilder_vehicleitemparams_163.parentItem = shipBuilder_vehicleitem_48
    shipBuilder_vehicleitemparams_163 = save_or_locate(shipBuilder_vehicleitemparams_163)

    shipBuilder_vehicleitemparams_164 = VehicleItemParams()
    shipBuilder_vehicleitemparams_164.name = u'pitchMin'
    shipBuilder_vehicleitemparams_164.value = -45.0
    shipBuilder_vehicleitemparams_164.parentItem = shipBuilder_vehicleitem_48
    shipBuilder_vehicleitemparams_164 = save_or_locate(shipBuilder_vehicleitemparams_164)

    shipBuilder_vehicleitemparams_165 = VehicleItemParams()
    shipBuilder_vehicleitemparams_165.name = u'pitchMax'
    shipBuilder_vehicleitemparams_165.value = 45.0
    shipBuilder_vehicleitemparams_165.parentItem = shipBuilder_vehicleitem_48
    shipBuilder_vehicleitemparams_165 = save_or_locate(shipBuilder_vehicleitemparams_165)

    shipBuilder_vehicleitemparams_166 = VehicleItemParams()
    shipBuilder_vehicleitemparams_166.name = u'RoF'
    shipBuilder_vehicleitemparams_166.value = 26.5
    shipBuilder_vehicleitemparams_166.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemparams_166 = save_or_locate(shipBuilder_vehicleitemparams_166)

    shipBuilder_vehicleitemparams_167 = VehicleItemParams()
    shipBuilder_vehicleitemparams_167.name = u'Range'
    shipBuilder_vehicleitemparams_167.value = 60.0
    shipBuilder_vehicleitemparams_167.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemparams_167 = save_or_locate(shipBuilder_vehicleitemparams_167)

    shipBuilder_vehicleitemparams_168 = VehicleItemParams()
    shipBuilder_vehicleitemparams_168.name = u'Damage'
    shipBuilder_vehicleitemparams_168.value = 2.5
    shipBuilder_vehicleitemparams_168.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemparams_168 = save_or_locate(shipBuilder_vehicleitemparams_168)

    shipBuilder_vehicleitemparams_169 = VehicleItemParams()
    shipBuilder_vehicleitemparams_169.name = u'Power'
    shipBuilder_vehicleitemparams_169.value = 1.0
    shipBuilder_vehicleitemparams_169.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemparams_169 = save_or_locate(shipBuilder_vehicleitemparams_169)

    shipBuilder_vehicleitemparams_170 = VehicleItemParams()
    shipBuilder_vehicleitemparams_170.name = u'RoF'
    shipBuilder_vehicleitemparams_170.value = 26.7
    shipBuilder_vehicleitemparams_170.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemparams_170 = save_or_locate(shipBuilder_vehicleitemparams_170)

    shipBuilder_vehicleitemparams_171 = VehicleItemParams()
    shipBuilder_vehicleitemparams_171.name = u'Range'
    shipBuilder_vehicleitemparams_171.value = 60.0
    shipBuilder_vehicleitemparams_171.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemparams_171 = save_or_locate(shipBuilder_vehicleitemparams_171)

    shipBuilder_vehicleitemparams_172 = VehicleItemParams()
    shipBuilder_vehicleitemparams_172.name = u'Damage'
    shipBuilder_vehicleitemparams_172.value = 2.25
    shipBuilder_vehicleitemparams_172.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemparams_172 = save_or_locate(shipBuilder_vehicleitemparams_172)

    shipBuilder_vehicleitemparams_173 = VehicleItemParams()
    shipBuilder_vehicleitemparams_173.name = u'Power'
    shipBuilder_vehicleitemparams_173.value = 1.0
    shipBuilder_vehicleitemparams_173.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemparams_173 = save_or_locate(shipBuilder_vehicleitemparams_173)

    shipBuilder_vehicleitemparams_174 = VehicleItemParams()
    shipBuilder_vehicleitemparams_174.name = u'RoF'
    shipBuilder_vehicleitemparams_174.value = 5.0
    shipBuilder_vehicleitemparams_174.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemparams_174 = save_or_locate(shipBuilder_vehicleitemparams_174)

    shipBuilder_vehicleitemparams_175 = VehicleItemParams()
    shipBuilder_vehicleitemparams_175.name = u'Range'
    shipBuilder_vehicleitemparams_175.value = 30.0
    shipBuilder_vehicleitemparams_175.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemparams_175 = save_or_locate(shipBuilder_vehicleitemparams_175)

    shipBuilder_vehicleitemparams_176 = VehicleItemParams()
    shipBuilder_vehicleitemparams_176.name = u'Damage'
    shipBuilder_vehicleitemparams_176.value = 20.0
    shipBuilder_vehicleitemparams_176.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemparams_176 = save_or_locate(shipBuilder_vehicleitemparams_176)

    shipBuilder_vehicleitemparams_177 = VehicleItemParams()
    shipBuilder_vehicleitemparams_177.name = u'Power'
    shipBuilder_vehicleitemparams_177.value = 49.5
    shipBuilder_vehicleitemparams_177.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemparams_177 = save_or_locate(shipBuilder_vehicleitemparams_177)

    shipBuilder_vehicleitemparams_178 = VehicleItemParams()
    shipBuilder_vehicleitemparams_178.name = u'acceleration'
    shipBuilder_vehicleitemparams_178.value = 40.0
    shipBuilder_vehicleitemparams_178.parentItem = shipBuilder_vehicleitem_56
    shipBuilder_vehicleitemparams_178 = save_or_locate(shipBuilder_vehicleitemparams_178)

    shipBuilder_vehicleitemparams_179 = VehicleItemParams()
    shipBuilder_vehicleitemparams_179.name = u'maxThrust'
    shipBuilder_vehicleitemparams_179.value = 300000.0
    shipBuilder_vehicleitemparams_179.parentItem = shipBuilder_vehicleitem_56
    shipBuilder_vehicleitemparams_179 = save_or_locate(shipBuilder_vehicleitemparams_179)

    shipBuilder_vehicleitemparams_180 = VehicleItemParams()
    shipBuilder_vehicleitemparams_180.name = u'speed'
    shipBuilder_vehicleitemparams_180.value = 80.0
    shipBuilder_vehicleitemparams_180.parentItem = shipBuilder_vehicleitem_56
    shipBuilder_vehicleitemparams_180 = save_or_locate(shipBuilder_vehicleitemparams_180)

    shipBuilder_vehicleitemparams_181 = VehicleItemParams()
    shipBuilder_vehicleitemparams_181.name = u'pitchMin'
    shipBuilder_vehicleitemparams_181.value = -40.0
    shipBuilder_vehicleitemparams_181.parentItem = shipBuilder_vehicleitem_56
    shipBuilder_vehicleitemparams_181 = save_or_locate(shipBuilder_vehicleitemparams_181)

    shipBuilder_vehicleitemparams_182 = VehicleItemParams()
    shipBuilder_vehicleitemparams_182.name = u'pitchMax'
    shipBuilder_vehicleitemparams_182.value = 40.0
    shipBuilder_vehicleitemparams_182.parentItem = shipBuilder_vehicleitem_56
    shipBuilder_vehicleitemparams_182 = save_or_locate(shipBuilder_vehicleitemparams_182)

    shipBuilder_vehicleitemparams_183 = VehicleItemParams()
    shipBuilder_vehicleitemparams_183.name = u'acceleration'
    shipBuilder_vehicleitemparams_183.value = 40.0
    shipBuilder_vehicleitemparams_183.parentItem = shipBuilder_vehicleitem_57
    shipBuilder_vehicleitemparams_183 = save_or_locate(shipBuilder_vehicleitemparams_183)

    shipBuilder_vehicleitemparams_184 = VehicleItemParams()
    shipBuilder_vehicleitemparams_184.name = u'maxThrust'
    shipBuilder_vehicleitemparams_184.value = 300000.0
    shipBuilder_vehicleitemparams_184.parentItem = shipBuilder_vehicleitem_57
    shipBuilder_vehicleitemparams_184 = save_or_locate(shipBuilder_vehicleitemparams_184)

    shipBuilder_vehicleitemparams_185 = VehicleItemParams()
    shipBuilder_vehicleitemparams_185.name = u'speed'
    shipBuilder_vehicleitemparams_185.value = 80.0
    shipBuilder_vehicleitemparams_185.parentItem = shipBuilder_vehicleitem_57
    shipBuilder_vehicleitemparams_185 = save_or_locate(shipBuilder_vehicleitemparams_185)

    shipBuilder_vehicleitemparams_186 = VehicleItemParams()
    shipBuilder_vehicleitemparams_186.name = u'pitchMin'
    shipBuilder_vehicleitemparams_186.value = -45.0
    shipBuilder_vehicleitemparams_186.parentItem = shipBuilder_vehicleitem_57
    shipBuilder_vehicleitemparams_186 = save_or_locate(shipBuilder_vehicleitemparams_186)

    shipBuilder_vehicleitemparams_187 = VehicleItemParams()
    shipBuilder_vehicleitemparams_187.name = u'pitchMax'
    shipBuilder_vehicleitemparams_187.value = 45.0
    shipBuilder_vehicleitemparams_187.parentItem = shipBuilder_vehicleitem_57
    shipBuilder_vehicleitemparams_187 = save_or_locate(shipBuilder_vehicleitemparams_187)

    shipBuilder_vehicleitemparams_188 = VehicleItemParams()
    shipBuilder_vehicleitemparams_188.name = u'acceleration'
    shipBuilder_vehicleitemparams_188.value = 20.0
    shipBuilder_vehicleitemparams_188.parentItem = shipBuilder_vehicleitem_58
    shipBuilder_vehicleitemparams_188 = save_or_locate(shipBuilder_vehicleitemparams_188)

    shipBuilder_vehicleitemparams_189 = VehicleItemParams()
    shipBuilder_vehicleitemparams_189.name = u'maxThrust'
    shipBuilder_vehicleitemparams_189.value = 2600000.0
    shipBuilder_vehicleitemparams_189.parentItem = shipBuilder_vehicleitem_58
    shipBuilder_vehicleitemparams_189 = save_or_locate(shipBuilder_vehicleitemparams_189)

    shipBuilder_vehicleitemparams_190 = VehicleItemParams()
    shipBuilder_vehicleitemparams_190.name = u'speed'
    shipBuilder_vehicleitemparams_190.value = 40.0
    shipBuilder_vehicleitemparams_190.parentItem = shipBuilder_vehicleitem_58
    shipBuilder_vehicleitemparams_190 = save_or_locate(shipBuilder_vehicleitemparams_190)

    shipBuilder_vehicleitemparams_191 = VehicleItemParams()
    shipBuilder_vehicleitemparams_191.name = u'RoF'
    shipBuilder_vehicleitemparams_191.value = 20.0
    shipBuilder_vehicleitemparams_191.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemparams_191 = save_or_locate(shipBuilder_vehicleitemparams_191)

    shipBuilder_vehicleitemparams_192 = VehicleItemParams()
    shipBuilder_vehicleitemparams_192.name = u'Range'
    shipBuilder_vehicleitemparams_192.value = 90.0
    shipBuilder_vehicleitemparams_192.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemparams_192 = save_or_locate(shipBuilder_vehicleitemparams_192)

    shipBuilder_vehicleitemparams_193 = VehicleItemParams()
    shipBuilder_vehicleitemparams_193.name = u'Damage'
    shipBuilder_vehicleitemparams_193.value = 3.5
    shipBuilder_vehicleitemparams_193.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemparams_193 = save_or_locate(shipBuilder_vehicleitemparams_193)

    shipBuilder_vehicleitemparams_194 = VehicleItemParams()
    shipBuilder_vehicleitemparams_194.name = u'Power'
    shipBuilder_vehicleitemparams_194.value = 23.1
    shipBuilder_vehicleitemparams_194.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemparams_194 = save_or_locate(shipBuilder_vehicleitemparams_194)

    shipBuilder_vehicleitemparams_195 = VehicleItemParams()
    shipBuilder_vehicleitemparams_195.name = u'chargeRate'
    shipBuilder_vehicleitemparams_195.value = 100.0
    shipBuilder_vehicleitemparams_195.parentItem = shipBuilder_vehicleitem_62
    shipBuilder_vehicleitemparams_195 = save_or_locate(shipBuilder_vehicleitemparams_195)

    shipBuilder_vehicleitemparams_196 = VehicleItemParams()
    shipBuilder_vehicleitemparams_196.name = u'output'
    shipBuilder_vehicleitemparams_196.value = 200.0
    shipBuilder_vehicleitemparams_196.parentItem = shipBuilder_vehicleitem_62
    shipBuilder_vehicleitemparams_196 = save_or_locate(shipBuilder_vehicleitemparams_196)

    shipBuilder_vehicleitemparams_197 = VehicleItemParams()
    shipBuilder_vehicleitemparams_197.name = u'capacity'
    shipBuilder_vehicleitemparams_197.value = 700.0
    shipBuilder_vehicleitemparams_197.parentItem = shipBuilder_vehicleitem_62
    shipBuilder_vehicleitemparams_197 = save_or_locate(shipBuilder_vehicleitemparams_197)

    shipBuilder_vehicleitemparams_198 = VehicleItemParams()
    shipBuilder_vehicleitemparams_198.name = u'displayRadius'
    shipBuilder_vehicleitemparams_198.value = -1.0
    shipBuilder_vehicleitemparams_198.parentItem = shipBuilder_vehicleitem_65
    shipBuilder_vehicleitemparams_198 = save_or_locate(shipBuilder_vehicleitemparams_198)

    shipBuilder_vehicleitemparams_199 = VehicleItemParams()
    shipBuilder_vehicleitemparams_199.name = u'isSphere'
    shipBuilder_vehicleitemparams_199.value = 1.0
    shipBuilder_vehicleitemparams_199.parentItem = shipBuilder_vehicleitem_65
    shipBuilder_vehicleitemparams_199 = save_or_locate(shipBuilder_vehicleitemparams_199)

    shipBuilder_vehicleitemparams_200 = VehicleItemParams()
    shipBuilder_vehicleitemparams_200.name = u'gridSize'
    shipBuilder_vehicleitemparams_200.value = 5.0
    shipBuilder_vehicleitemparams_200.parentItem = shipBuilder_vehicleitem_66
    shipBuilder_vehicleitemparams_200 = save_or_locate(shipBuilder_vehicleitemparams_200)

    shipBuilder_vehicleitemparams_201 = VehicleItemParams()
    shipBuilder_vehicleitemparams_201.name = u'radius'
    shipBuilder_vehicleitemparams_201.value = 10000.0
    shipBuilder_vehicleitemparams_201.parentItem = shipBuilder_vehicleitem_66
    shipBuilder_vehicleitemparams_201 = save_or_locate(shipBuilder_vehicleitemparams_201)

    shipBuilder_vehicleitemparams_202 = VehicleItemParams()
    shipBuilder_vehicleitemparams_202.name = u'identifyTime'
    shipBuilder_vehicleitemparams_202.value = 0.5
    shipBuilder_vehicleitemparams_202.parentItem = shipBuilder_vehicleitem_66
    shipBuilder_vehicleitemparams_202 = save_or_locate(shipBuilder_vehicleitemparams_202)

    shipBuilder_vehicleitemparams_203 = VehicleItemParams()
    shipBuilder_vehicleitemparams_203.name = u'radarTime'
    shipBuilder_vehicleitemparams_203.value = 4.0
    shipBuilder_vehicleitemparams_203.parentItem = shipBuilder_vehicleitem_66
    shipBuilder_vehicleitemparams_203 = save_or_locate(shipBuilder_vehicleitemparams_203)

    shipBuilder_vehicleitemparams_204 = VehicleItemParams()
    shipBuilder_vehicleitemparams_204.name = u'radarType'
    shipBuilder_vehicleitemparams_204.value = 0.0
    shipBuilder_vehicleitemparams_204.parentItem = shipBuilder_vehicleitem_66
    shipBuilder_vehicleitemparams_204 = save_or_locate(shipBuilder_vehicleitemparams_204)

    shipBuilder_vehicleitemparams_205 = VehicleItemParams()
    shipBuilder_vehicleitemparams_205.name = u'gridSize'
    shipBuilder_vehicleitemparams_205.value = 5.0
    shipBuilder_vehicleitemparams_205.parentItem = shipBuilder_vehicleitem_67
    shipBuilder_vehicleitemparams_205 = save_or_locate(shipBuilder_vehicleitemparams_205)

    shipBuilder_vehicleitemparams_206 = VehicleItemParams()
    shipBuilder_vehicleitemparams_206.name = u'radius'
    shipBuilder_vehicleitemparams_206.value = 3000.0
    shipBuilder_vehicleitemparams_206.parentItem = shipBuilder_vehicleitem_67
    shipBuilder_vehicleitemparams_206 = save_or_locate(shipBuilder_vehicleitemparams_206)

    shipBuilder_vehicleitemparams_207 = VehicleItemParams()
    shipBuilder_vehicleitemparams_207.name = u'identifyTime'
    shipBuilder_vehicleitemparams_207.value = 0.5
    shipBuilder_vehicleitemparams_207.parentItem = shipBuilder_vehicleitem_67
    shipBuilder_vehicleitemparams_207 = save_or_locate(shipBuilder_vehicleitemparams_207)

    shipBuilder_vehicleitemparams_208 = VehicleItemParams()
    shipBuilder_vehicleitemparams_208.name = u'radarTime'
    shipBuilder_vehicleitemparams_208.value = 1.0
    shipBuilder_vehicleitemparams_208.parentItem = shipBuilder_vehicleitem_67
    shipBuilder_vehicleitemparams_208 = save_or_locate(shipBuilder_vehicleitemparams_208)

    shipBuilder_vehicleitemparams_209 = VehicleItemParams()
    shipBuilder_vehicleitemparams_209.name = u'radarType'
    shipBuilder_vehicleitemparams_209.value = 1.0
    shipBuilder_vehicleitemparams_209.parentItem = shipBuilder_vehicleitem_67
    shipBuilder_vehicleitemparams_209 = save_or_locate(shipBuilder_vehicleitemparams_209)

    shipBuilder_vehicleitemparams_210 = VehicleItemParams()
    shipBuilder_vehicleitemparams_210.name = u'gridSize'
    shipBuilder_vehicleitemparams_210.value = 1.0
    shipBuilder_vehicleitemparams_210.parentItem = shipBuilder_vehicleitem_68
    shipBuilder_vehicleitemparams_210 = save_or_locate(shipBuilder_vehicleitemparams_210)

    shipBuilder_vehicleitemparams_211 = VehicleItemParams()
    shipBuilder_vehicleitemparams_211.name = u'radius'
    shipBuilder_vehicleitemparams_211.value = 1500.0
    shipBuilder_vehicleitemparams_211.parentItem = shipBuilder_vehicleitem_68
    shipBuilder_vehicleitemparams_211 = save_or_locate(shipBuilder_vehicleitemparams_211)

    shipBuilder_vehicleitemparams_212 = VehicleItemParams()
    shipBuilder_vehicleitemparams_212.name = u'identifyTime'
    shipBuilder_vehicleitemparams_212.value = 0.5
    shipBuilder_vehicleitemparams_212.parentItem = shipBuilder_vehicleitem_68
    shipBuilder_vehicleitemparams_212 = save_or_locate(shipBuilder_vehicleitemparams_212)

    shipBuilder_vehicleitemparams_213 = VehicleItemParams()
    shipBuilder_vehicleitemparams_213.name = u'radarTime'
    shipBuilder_vehicleitemparams_213.value = 0.0
    shipBuilder_vehicleitemparams_213.parentItem = shipBuilder_vehicleitem_68
    shipBuilder_vehicleitemparams_213 = save_or_locate(shipBuilder_vehicleitemparams_213)

    shipBuilder_vehicleitemparams_214 = VehicleItemParams()
    shipBuilder_vehicleitemparams_214.name = u'radarType'
    shipBuilder_vehicleitemparams_214.value = 2.0
    shipBuilder_vehicleitemparams_214.parentItem = shipBuilder_vehicleitem_68
    shipBuilder_vehicleitemparams_214 = save_or_locate(shipBuilder_vehicleitemparams_214)

    shipBuilder_vehicleitemparams_215 = VehicleItemParams()
    shipBuilder_vehicleitemparams_215.name = u'numTargetsAllowed'
    shipBuilder_vehicleitemparams_215.value = 2.0
    shipBuilder_vehicleitemparams_215.parentItem = shipBuilder_vehicleitem_69
    shipBuilder_vehicleitemparams_215 = save_or_locate(shipBuilder_vehicleitemparams_215)

    shipBuilder_vehicleitemparams_216 = VehicleItemParams()
    shipBuilder_vehicleitemparams_216.name = u'Speed'
    shipBuilder_vehicleitemparams_216.value = 74.0
    shipBuilder_vehicleitemparams_216.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemparams_216 = save_or_locate(shipBuilder_vehicleitemparams_216)

    shipBuilder_vehicleitemparams_217 = VehicleItemParams()
    shipBuilder_vehicleitemparams_217.name = u'Warhead'
    shipBuilder_vehicleitemparams_217.value = 64.28
    shipBuilder_vehicleitemparams_217.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemparams_217 = save_or_locate(shipBuilder_vehicleitemparams_217)

    shipBuilder_vehicleitemparams_218 = VehicleItemParams()
    shipBuilder_vehicleitemparams_218.name = u'Radius'
    shipBuilder_vehicleitemparams_218.value = 20.0
    shipBuilder_vehicleitemparams_218.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemparams_218 = save_or_locate(shipBuilder_vehicleitemparams_218)

    shipBuilder_vehicleitemparams_219 = VehicleItemParams()
    shipBuilder_vehicleitemparams_219.name = u'Concuss'
    shipBuilder_vehicleitemparams_219.value = 8.0
    shipBuilder_vehicleitemparams_219.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemparams_219 = save_or_locate(shipBuilder_vehicleitemparams_219)

    shipBuilder_vehicleitemparams_220 = VehicleItemParams()
    shipBuilder_vehicleitemparams_220.name = u'Speed'
    shipBuilder_vehicleitemparams_220.value = 74.5
    shipBuilder_vehicleitemparams_220.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemparams_220 = save_or_locate(shipBuilder_vehicleitemparams_220)

    shipBuilder_vehicleitemparams_221 = VehicleItemParams()
    shipBuilder_vehicleitemparams_221.name = u'Warhead'
    shipBuilder_vehicleitemparams_221.value = 62.86
    shipBuilder_vehicleitemparams_221.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemparams_221 = save_or_locate(shipBuilder_vehicleitemparams_221)

    shipBuilder_vehicleitemparams_222 = VehicleItemParams()
    shipBuilder_vehicleitemparams_222.name = u'Radius'
    shipBuilder_vehicleitemparams_222.value = 80.0
    shipBuilder_vehicleitemparams_222.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemparams_222 = save_or_locate(shipBuilder_vehicleitemparams_222)

    shipBuilder_vehicleitemparams_223 = VehicleItemParams()
    shipBuilder_vehicleitemparams_223.name = u'Concuss'
    shipBuilder_vehicleitemparams_223.value = 93.33
    shipBuilder_vehicleitemparams_223.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemparams_223 = save_or_locate(shipBuilder_vehicleitemparams_223)

    shipBuilder_vehicleitemparams_224 = VehicleItemParams()
    shipBuilder_vehicleitemparams_224.name = u'Speed'
    shipBuilder_vehicleitemparams_224.value = 75.5
    shipBuilder_vehicleitemparams_224.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemparams_224 = save_or_locate(shipBuilder_vehicleitemparams_224)

    shipBuilder_vehicleitemparams_225 = VehicleItemParams()
    shipBuilder_vehicleitemparams_225.name = u'Warhead'
    shipBuilder_vehicleitemparams_225.value = 71.43
    shipBuilder_vehicleitemparams_225.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemparams_225 = save_or_locate(shipBuilder_vehicleitemparams_225)

    shipBuilder_vehicleitemparams_226 = VehicleItemParams()
    shipBuilder_vehicleitemparams_226.name = u'Radius'
    shipBuilder_vehicleitemparams_226.value = 23.33
    shipBuilder_vehicleitemparams_226.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemparams_226 = save_or_locate(shipBuilder_vehicleitemparams_226)

    shipBuilder_vehicleitemparams_227 = VehicleItemParams()
    shipBuilder_vehicleitemparams_227.name = u'Concuss'
    shipBuilder_vehicleitemparams_227.value = 9.33
    shipBuilder_vehicleitemparams_227.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemparams_227 = save_or_locate(shipBuilder_vehicleitemparams_227)

    shipBuilder_vehicleitemparams_228 = VehicleItemParams()
    shipBuilder_vehicleitemparams_228.name = u'Speed'
    shipBuilder_vehicleitemparams_228.value = 75.5
    shipBuilder_vehicleitemparams_228.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemparams_228 = save_or_locate(shipBuilder_vehicleitemparams_228)

    shipBuilder_vehicleitemparams_229 = VehicleItemParams()
    shipBuilder_vehicleitemparams_229.name = u'Warhead'
    shipBuilder_vehicleitemparams_229.value = 71.43
    shipBuilder_vehicleitemparams_229.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemparams_229 = save_or_locate(shipBuilder_vehicleitemparams_229)

    shipBuilder_vehicleitemparams_230 = VehicleItemParams()
    shipBuilder_vehicleitemparams_230.name = u'Radius'
    shipBuilder_vehicleitemparams_230.value = 23.33
    shipBuilder_vehicleitemparams_230.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemparams_230 = save_or_locate(shipBuilder_vehicleitemparams_230)

    shipBuilder_vehicleitemparams_231 = VehicleItemParams()
    shipBuilder_vehicleitemparams_231.name = u'Concuss'
    shipBuilder_vehicleitemparams_231.value = 9.33
    shipBuilder_vehicleitemparams_231.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemparams_231 = save_or_locate(shipBuilder_vehicleitemparams_231)

    shipBuilder_vehicleitemparams_232 = VehicleItemParams()
    shipBuilder_vehicleitemparams_232.name = u'acceleration'
    shipBuilder_vehicleitemparams_232.value = 20.0
    shipBuilder_vehicleitemparams_232.parentItem = shipBuilder_vehicleitem_88
    shipBuilder_vehicleitemparams_232 = save_or_locate(shipBuilder_vehicleitemparams_232)

    shipBuilder_vehicleitemparams_233 = VehicleItemParams()
    shipBuilder_vehicleitemparams_233.name = u'maxThrust'
    shipBuilder_vehicleitemparams_233.value = 2600000.0
    shipBuilder_vehicleitemparams_233.parentItem = shipBuilder_vehicleitem_88
    shipBuilder_vehicleitemparams_233 = save_or_locate(shipBuilder_vehicleitemparams_233)

    shipBuilder_vehicleitemparams_234 = VehicleItemParams()
    shipBuilder_vehicleitemparams_234.name = u'speed'
    shipBuilder_vehicleitemparams_234.value = 40.0
    shipBuilder_vehicleitemparams_234.parentItem = shipBuilder_vehicleitem_88
    shipBuilder_vehicleitemparams_234 = save_or_locate(shipBuilder_vehicleitemparams_234)

    #Processing model: PipeState

    from shipBuilder.models import PipeState


    #Processing model: VehicleItemPipe

    from shipBuilder.models import VehicleItemPipe


    #Processing model: VehicleItemPower

    from shipBuilder.models import VehicleItemPower

    shipBuilder_vehicleitempower_1 = VehicleItemPower()
    shipBuilder_vehicleitempower_1.state = u'Default'
    shipBuilder_vehicleitempower_1.value = u'100'
    shipBuilder_vehicleitempower_1.parentItem = shipBuilder_vehicleitem_1
    shipBuilder_vehicleitempower_1 = save_or_locate(shipBuilder_vehicleitempower_1)

    shipBuilder_vehicleitempower_2 = VehicleItemPower()
    shipBuilder_vehicleitempower_2.state = u'Default'
    shipBuilder_vehicleitempower_2.value = u'100'
    shipBuilder_vehicleitempower_2.parentItem = shipBuilder_vehicleitem_5
    shipBuilder_vehicleitempower_2 = save_or_locate(shipBuilder_vehicleitempower_2)

    shipBuilder_vehicleitempower_3 = VehicleItemPower()
    shipBuilder_vehicleitempower_3.state = u'Default'
    shipBuilder_vehicleitempower_3.value = u'100'
    shipBuilder_vehicleitempower_3.parentItem = shipBuilder_vehicleitem_6
    shipBuilder_vehicleitempower_3 = save_or_locate(shipBuilder_vehicleitempower_3)

    shipBuilder_vehicleitempower_4 = VehicleItemPower()
    shipBuilder_vehicleitempower_4.state = u'Default'
    shipBuilder_vehicleitempower_4.value = u'100'
    shipBuilder_vehicleitempower_4.parentItem = shipBuilder_vehicleitem_7
    shipBuilder_vehicleitempower_4 = save_or_locate(shipBuilder_vehicleitempower_4)

    shipBuilder_vehicleitempower_5 = VehicleItemPower()
    shipBuilder_vehicleitempower_5.state = u'Default'
    shipBuilder_vehicleitempower_5.value = u'100'
    shipBuilder_vehicleitempower_5.parentItem = shipBuilder_vehicleitem_9
    shipBuilder_vehicleitempower_5 = save_or_locate(shipBuilder_vehicleitempower_5)

    shipBuilder_vehicleitempower_6 = VehicleItemPower()
    shipBuilder_vehicleitempower_6.state = u'Default'
    shipBuilder_vehicleitempower_6.value = u'100'
    shipBuilder_vehicleitempower_6.parentItem = shipBuilder_vehicleitem_10
    shipBuilder_vehicleitempower_6 = save_or_locate(shipBuilder_vehicleitempower_6)

    shipBuilder_vehicleitempower_7 = VehicleItemPower()
    shipBuilder_vehicleitempower_7.state = u'Default'
    shipBuilder_vehicleitempower_7.value = u'100'
    shipBuilder_vehicleitempower_7.parentItem = shipBuilder_vehicleitem_11
    shipBuilder_vehicleitempower_7 = save_or_locate(shipBuilder_vehicleitempower_7)

    shipBuilder_vehicleitempower_8 = VehicleItemPower()
    shipBuilder_vehicleitempower_8.state = u'Default'
    shipBuilder_vehicleitempower_8.value = u'100'
    shipBuilder_vehicleitempower_8.parentItem = shipBuilder_vehicleitem_12
    shipBuilder_vehicleitempower_8 = save_or_locate(shipBuilder_vehicleitempower_8)

    shipBuilder_vehicleitempower_9 = VehicleItemPower()
    shipBuilder_vehicleitempower_9.state = u'Default'
    shipBuilder_vehicleitempower_9.value = u'100'
    shipBuilder_vehicleitempower_9.parentItem = shipBuilder_vehicleitem_14
    shipBuilder_vehicleitempower_9 = save_or_locate(shipBuilder_vehicleitempower_9)

    shipBuilder_vehicleitempower_10 = VehicleItemPower()
    shipBuilder_vehicleitempower_10.state = u'Default'
    shipBuilder_vehicleitempower_10.value = u'100'
    shipBuilder_vehicleitempower_10.parentItem = shipBuilder_vehicleitem_15
    shipBuilder_vehicleitempower_10 = save_or_locate(shipBuilder_vehicleitempower_10)

    shipBuilder_vehicleitempower_11 = VehicleItemPower()
    shipBuilder_vehicleitempower_11.state = u'Default'
    shipBuilder_vehicleitempower_11.value = u'100'
    shipBuilder_vehicleitempower_11.parentItem = shipBuilder_vehicleitem_16
    shipBuilder_vehicleitempower_11 = save_or_locate(shipBuilder_vehicleitempower_11)

    shipBuilder_vehicleitempower_12 = VehicleItemPower()
    shipBuilder_vehicleitempower_12.state = u'Active'
    shipBuilder_vehicleitempower_12.value = u'-10'
    shipBuilder_vehicleitempower_12.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitempower_12 = save_or_locate(shipBuilder_vehicleitempower_12)

    shipBuilder_vehicleitempower_13 = VehicleItemPower()
    shipBuilder_vehicleitempower_13.state = u'Idle'
    shipBuilder_vehicleitempower_13.value = u'-3'
    shipBuilder_vehicleitempower_13.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitempower_13 = save_or_locate(shipBuilder_vehicleitempower_13)

    shipBuilder_vehicleitempower_14 = VehicleItemPower()
    shipBuilder_vehicleitempower_14.state = u'Shooting'
    shipBuilder_vehicleitempower_14.value = u'-30'
    shipBuilder_vehicleitempower_14.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitempower_14 = save_or_locate(shipBuilder_vehicleitempower_14)

    shipBuilder_vehicleitempower_15 = VehicleItemPower()
    shipBuilder_vehicleitempower_15.state = u'Active'
    shipBuilder_vehicleitempower_15.value = u'-10'
    shipBuilder_vehicleitempower_15.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitempower_15 = save_or_locate(shipBuilder_vehicleitempower_15)

    shipBuilder_vehicleitempower_16 = VehicleItemPower()
    shipBuilder_vehicleitempower_16.state = u'Idle'
    shipBuilder_vehicleitempower_16.value = u'-3'
    shipBuilder_vehicleitempower_16.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitempower_16 = save_or_locate(shipBuilder_vehicleitempower_16)

    shipBuilder_vehicleitempower_17 = VehicleItemPower()
    shipBuilder_vehicleitempower_17.state = u'Shooting'
    shipBuilder_vehicleitempower_17.value = u'-30'
    shipBuilder_vehicleitempower_17.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitempower_17 = save_or_locate(shipBuilder_vehicleitempower_17)

    shipBuilder_vehicleitempower_18 = VehicleItemPower()
    shipBuilder_vehicleitempower_18.state = u'Active'
    shipBuilder_vehicleitempower_18.value = u'-10'
    shipBuilder_vehicleitempower_18.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitempower_18 = save_or_locate(shipBuilder_vehicleitempower_18)

    shipBuilder_vehicleitempower_19 = VehicleItemPower()
    shipBuilder_vehicleitempower_19.state = u'Idle'
    shipBuilder_vehicleitempower_19.value = u'-3'
    shipBuilder_vehicleitempower_19.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitempower_19 = save_or_locate(shipBuilder_vehicleitempower_19)

    shipBuilder_vehicleitempower_20 = VehicleItemPower()
    shipBuilder_vehicleitempower_20.state = u'Shooting'
    shipBuilder_vehicleitempower_20.value = u'-80'
    shipBuilder_vehicleitempower_20.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitempower_20 = save_or_locate(shipBuilder_vehicleitempower_20)

    shipBuilder_vehicleitempower_21 = VehicleItemPower()
    shipBuilder_vehicleitempower_21.state = u'Active'
    shipBuilder_vehicleitempower_21.value = u'-10'
    shipBuilder_vehicleitempower_21.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitempower_21 = save_or_locate(shipBuilder_vehicleitempower_21)

    shipBuilder_vehicleitempower_22 = VehicleItemPower()
    shipBuilder_vehicleitempower_22.state = u'Idle'
    shipBuilder_vehicleitempower_22.value = u'-3'
    shipBuilder_vehicleitempower_22.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitempower_22 = save_or_locate(shipBuilder_vehicleitempower_22)

    shipBuilder_vehicleitempower_23 = VehicleItemPower()
    shipBuilder_vehicleitempower_23.state = u'Shooting'
    shipBuilder_vehicleitempower_23.value = u'-30'
    shipBuilder_vehicleitempower_23.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitempower_23 = save_or_locate(shipBuilder_vehicleitempower_23)

    shipBuilder_vehicleitempower_24 = VehicleItemPower()
    shipBuilder_vehicleitempower_24.state = u'Active'
    shipBuilder_vehicleitempower_24.value = u'-10'
    shipBuilder_vehicleitempower_24.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitempower_24 = save_or_locate(shipBuilder_vehicleitempower_24)

    shipBuilder_vehicleitempower_25 = VehicleItemPower()
    shipBuilder_vehicleitempower_25.state = u'Idle'
    shipBuilder_vehicleitempower_25.value = u'-3'
    shipBuilder_vehicleitempower_25.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitempower_25 = save_or_locate(shipBuilder_vehicleitempower_25)

    shipBuilder_vehicleitempower_26 = VehicleItemPower()
    shipBuilder_vehicleitempower_26.state = u'Targeting'
    shipBuilder_vehicleitempower_26.value = u'-30'
    shipBuilder_vehicleitempower_26.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitempower_26 = save_or_locate(shipBuilder_vehicleitempower_26)

    shipBuilder_vehicleitempower_27 = VehicleItemPower()
    shipBuilder_vehicleitempower_27.state = u'Active'
    shipBuilder_vehicleitempower_27.value = u'-10'
    shipBuilder_vehicleitempower_27.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitempower_27 = save_or_locate(shipBuilder_vehicleitempower_27)

    shipBuilder_vehicleitempower_28 = VehicleItemPower()
    shipBuilder_vehicleitempower_28.state = u'Idle'
    shipBuilder_vehicleitempower_28.value = u'-3'
    shipBuilder_vehicleitempower_28.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitempower_28 = save_or_locate(shipBuilder_vehicleitempower_28)

    shipBuilder_vehicleitempower_29 = VehicleItemPower()
    shipBuilder_vehicleitempower_29.state = u'Targeting'
    shipBuilder_vehicleitempower_29.value = u'-30'
    shipBuilder_vehicleitempower_29.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitempower_29 = save_or_locate(shipBuilder_vehicleitempower_29)

    shipBuilder_vehicleitempower_30 = VehicleItemPower()
    shipBuilder_vehicleitempower_30.state = u'Active'
    shipBuilder_vehicleitempower_30.value = u'-10'
    shipBuilder_vehicleitempower_30.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitempower_30 = save_or_locate(shipBuilder_vehicleitempower_30)

    shipBuilder_vehicleitempower_31 = VehicleItemPower()
    shipBuilder_vehicleitempower_31.state = u'Idle'
    shipBuilder_vehicleitempower_31.value = u'-3'
    shipBuilder_vehicleitempower_31.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitempower_31 = save_or_locate(shipBuilder_vehicleitempower_31)

    shipBuilder_vehicleitempower_32 = VehicleItemPower()
    shipBuilder_vehicleitempower_32.state = u'Shooting'
    shipBuilder_vehicleitempower_32.value = u'-30'
    shipBuilder_vehicleitempower_32.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitempower_32 = save_or_locate(shipBuilder_vehicleitempower_32)

    shipBuilder_vehicleitempower_33 = VehicleItemPower()
    shipBuilder_vehicleitempower_33.state = u'Default'
    shipBuilder_vehicleitempower_33.value = u'100'
    shipBuilder_vehicleitempower_33.parentItem = shipBuilder_vehicleitem_36
    shipBuilder_vehicleitempower_33 = save_or_locate(shipBuilder_vehicleitempower_33)

    shipBuilder_vehicleitempower_34 = VehicleItemPower()
    shipBuilder_vehicleitempower_34.state = u'Active'
    shipBuilder_vehicleitempower_34.value = u'-10'
    shipBuilder_vehicleitempower_34.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitempower_34 = save_or_locate(shipBuilder_vehicleitempower_34)

    shipBuilder_vehicleitempower_35 = VehicleItemPower()
    shipBuilder_vehicleitempower_35.state = u'Idle'
    shipBuilder_vehicleitempower_35.value = u'-3'
    shipBuilder_vehicleitempower_35.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitempower_35 = save_or_locate(shipBuilder_vehicleitempower_35)

    shipBuilder_vehicleitempower_36 = VehicleItemPower()
    shipBuilder_vehicleitempower_36.state = u'Shooting'
    shipBuilder_vehicleitempower_36.value = u'-30'
    shipBuilder_vehicleitempower_36.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitempower_36 = save_or_locate(shipBuilder_vehicleitempower_36)

    shipBuilder_vehicleitempower_37 = VehicleItemPower()
    shipBuilder_vehicleitempower_37.state = u'Default'
    shipBuilder_vehicleitempower_37.value = u'100'
    shipBuilder_vehicleitempower_37.parentItem = shipBuilder_vehicleitem_41
    shipBuilder_vehicleitempower_37 = save_or_locate(shipBuilder_vehicleitempower_37)

    shipBuilder_vehicleitempower_38 = VehicleItemPower()
    shipBuilder_vehicleitempower_38.state = u'Active'
    shipBuilder_vehicleitempower_38.value = u'-10'
    shipBuilder_vehicleitempower_38.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitempower_38 = save_or_locate(shipBuilder_vehicleitempower_38)

    shipBuilder_vehicleitempower_39 = VehicleItemPower()
    shipBuilder_vehicleitempower_39.state = u'Idle'
    shipBuilder_vehicleitempower_39.value = u'-3'
    shipBuilder_vehicleitempower_39.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitempower_39 = save_or_locate(shipBuilder_vehicleitempower_39)

    shipBuilder_vehicleitempower_40 = VehicleItemPower()
    shipBuilder_vehicleitempower_40.state = u'Shooting'
    shipBuilder_vehicleitempower_40.value = u'-30'
    shipBuilder_vehicleitempower_40.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitempower_40 = save_or_locate(shipBuilder_vehicleitempower_40)

    shipBuilder_vehicleitempower_41 = VehicleItemPower()
    shipBuilder_vehicleitempower_41.state = u'Active'
    shipBuilder_vehicleitempower_41.value = u'-10'
    shipBuilder_vehicleitempower_41.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitempower_41 = save_or_locate(shipBuilder_vehicleitempower_41)

    shipBuilder_vehicleitempower_42 = VehicleItemPower()
    shipBuilder_vehicleitempower_42.state = u'Idle'
    shipBuilder_vehicleitempower_42.value = u'-3'
    shipBuilder_vehicleitempower_42.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitempower_42 = save_or_locate(shipBuilder_vehicleitempower_42)

    shipBuilder_vehicleitempower_43 = VehicleItemPower()
    shipBuilder_vehicleitempower_43.state = u'Shooting'
    shipBuilder_vehicleitempower_43.value = u'-30'
    shipBuilder_vehicleitempower_43.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitempower_43 = save_or_locate(shipBuilder_vehicleitempower_43)

    shipBuilder_vehicleitempower_44 = VehicleItemPower()
    shipBuilder_vehicleitempower_44.state = u'Active'
    shipBuilder_vehicleitempower_44.value = u'-10'
    shipBuilder_vehicleitempower_44.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitempower_44 = save_or_locate(shipBuilder_vehicleitempower_44)

    shipBuilder_vehicleitempower_45 = VehicleItemPower()
    shipBuilder_vehicleitempower_45.state = u'Idle'
    shipBuilder_vehicleitempower_45.value = u'-3'
    shipBuilder_vehicleitempower_45.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitempower_45 = save_or_locate(shipBuilder_vehicleitempower_45)

    shipBuilder_vehicleitempower_46 = VehicleItemPower()
    shipBuilder_vehicleitempower_46.state = u'Shooting'
    shipBuilder_vehicleitempower_46.value = u'-30'
    shipBuilder_vehicleitempower_46.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitempower_46 = save_or_locate(shipBuilder_vehicleitempower_46)

    shipBuilder_vehicleitempower_47 = VehicleItemPower()
    shipBuilder_vehicleitempower_47.state = u'Active'
    shipBuilder_vehicleitempower_47.value = u'-10'
    shipBuilder_vehicleitempower_47.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitempower_47 = save_or_locate(shipBuilder_vehicleitempower_47)

    shipBuilder_vehicleitempower_48 = VehicleItemPower()
    shipBuilder_vehicleitempower_48.state = u'Idle'
    shipBuilder_vehicleitempower_48.value = u'-3'
    shipBuilder_vehicleitempower_48.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitempower_48 = save_or_locate(shipBuilder_vehicleitempower_48)

    shipBuilder_vehicleitempower_49 = VehicleItemPower()
    shipBuilder_vehicleitempower_49.state = u'Shooting'
    shipBuilder_vehicleitempower_49.value = u'-30'
    shipBuilder_vehicleitempower_49.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitempower_49 = save_or_locate(shipBuilder_vehicleitempower_49)

    shipBuilder_vehicleitempower_50 = VehicleItemPower()
    shipBuilder_vehicleitempower_50.state = u'Active'
    shipBuilder_vehicleitempower_50.value = u'-10'
    shipBuilder_vehicleitempower_50.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitempower_50 = save_or_locate(shipBuilder_vehicleitempower_50)

    shipBuilder_vehicleitempower_51 = VehicleItemPower()
    shipBuilder_vehicleitempower_51.state = u'Idle'
    shipBuilder_vehicleitempower_51.value = u'-10'
    shipBuilder_vehicleitempower_51.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitempower_51 = save_or_locate(shipBuilder_vehicleitempower_51)

    shipBuilder_vehicleitempower_52 = VehicleItemPower()
    shipBuilder_vehicleitempower_52.state = u'Shooting'
    shipBuilder_vehicleitempower_52.value = u'-80'
    shipBuilder_vehicleitempower_52.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitempower_52 = save_or_locate(shipBuilder_vehicleitempower_52)

    shipBuilder_vehicleitempower_53 = VehicleItemPower()
    shipBuilder_vehicleitempower_53.state = u'Active'
    shipBuilder_vehicleitempower_53.value = u'-10'
    shipBuilder_vehicleitempower_53.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitempower_53 = save_or_locate(shipBuilder_vehicleitempower_53)

    shipBuilder_vehicleitempower_54 = VehicleItemPower()
    shipBuilder_vehicleitempower_54.state = u'Idle'
    shipBuilder_vehicleitempower_54.value = u'-10'
    shipBuilder_vehicleitempower_54.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitempower_54 = save_or_locate(shipBuilder_vehicleitempower_54)

    shipBuilder_vehicleitempower_55 = VehicleItemPower()
    shipBuilder_vehicleitempower_55.state = u'Shooting'
    shipBuilder_vehicleitempower_55.value = u'-80'
    shipBuilder_vehicleitempower_55.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitempower_55 = save_or_locate(shipBuilder_vehicleitempower_55)

    shipBuilder_vehicleitempower_56 = VehicleItemPower()
    shipBuilder_vehicleitempower_56.state = u'Active'
    shipBuilder_vehicleitempower_56.value = u'-10'
    shipBuilder_vehicleitempower_56.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitempower_56 = save_or_locate(shipBuilder_vehicleitempower_56)

    shipBuilder_vehicleitempower_57 = VehicleItemPower()
    shipBuilder_vehicleitempower_57.state = u'Idle'
    shipBuilder_vehicleitempower_57.value = u'-3'
    shipBuilder_vehicleitempower_57.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitempower_57 = save_or_locate(shipBuilder_vehicleitempower_57)

    shipBuilder_vehicleitempower_58 = VehicleItemPower()
    shipBuilder_vehicleitempower_58.state = u'Shooting'
    shipBuilder_vehicleitempower_58.value = u'-30'
    shipBuilder_vehicleitempower_58.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitempower_58 = save_or_locate(shipBuilder_vehicleitempower_58)

    shipBuilder_vehicleitempower_59 = VehicleItemPower()
    shipBuilder_vehicleitempower_59.state = u'Active'
    shipBuilder_vehicleitempower_59.value = u'-10'
    shipBuilder_vehicleitempower_59.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitempower_59 = save_or_locate(shipBuilder_vehicleitempower_59)

    shipBuilder_vehicleitempower_60 = VehicleItemPower()
    shipBuilder_vehicleitempower_60.state = u'Idle'
    shipBuilder_vehicleitempower_60.value = u'-3'
    shipBuilder_vehicleitempower_60.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitempower_60 = save_or_locate(shipBuilder_vehicleitempower_60)

    shipBuilder_vehicleitempower_61 = VehicleItemPower()
    shipBuilder_vehicleitempower_61.state = u'Shooting'
    shipBuilder_vehicleitempower_61.value = u'-30'
    shipBuilder_vehicleitempower_61.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitempower_61 = save_or_locate(shipBuilder_vehicleitempower_61)

    shipBuilder_vehicleitempower_62 = VehicleItemPower()
    shipBuilder_vehicleitempower_62.state = u'Default'
    shipBuilder_vehicleitempower_62.value = u'100'
    shipBuilder_vehicleitempower_62.parentItem = shipBuilder_vehicleitem_51
    shipBuilder_vehicleitempower_62 = save_or_locate(shipBuilder_vehicleitempower_62)

    shipBuilder_vehicleitempower_63 = VehicleItemPower()
    shipBuilder_vehicleitempower_63.state = u'Default'
    shipBuilder_vehicleitempower_63.value = u'100'
    shipBuilder_vehicleitempower_63.parentItem = shipBuilder_vehicleitem_52
    shipBuilder_vehicleitempower_63 = save_or_locate(shipBuilder_vehicleitempower_63)

    shipBuilder_vehicleitempower_64 = VehicleItemPower()
    shipBuilder_vehicleitempower_64.state = u'Active'
    shipBuilder_vehicleitempower_64.value = u'-10'
    shipBuilder_vehicleitempower_64.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitempower_64 = save_or_locate(shipBuilder_vehicleitempower_64)

    shipBuilder_vehicleitempower_65 = VehicleItemPower()
    shipBuilder_vehicleitempower_65.state = u'Idle'
    shipBuilder_vehicleitempower_65.value = u'-3'
    shipBuilder_vehicleitempower_65.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitempower_65 = save_or_locate(shipBuilder_vehicleitempower_65)

    shipBuilder_vehicleitempower_66 = VehicleItemPower()
    shipBuilder_vehicleitempower_66.state = u'Shooting'
    shipBuilder_vehicleitempower_66.value = u'-30'
    shipBuilder_vehicleitempower_66.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitempower_66 = save_or_locate(shipBuilder_vehicleitempower_66)

    shipBuilder_vehicleitempower_67 = VehicleItemPower()
    shipBuilder_vehicleitempower_67.state = u'Active'
    shipBuilder_vehicleitempower_67.value = u'-10'
    shipBuilder_vehicleitempower_67.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitempower_67 = save_or_locate(shipBuilder_vehicleitempower_67)

    shipBuilder_vehicleitempower_68 = VehicleItemPower()
    shipBuilder_vehicleitempower_68.state = u'Idle'
    shipBuilder_vehicleitempower_68.value = u'-3'
    shipBuilder_vehicleitempower_68.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitempower_68 = save_or_locate(shipBuilder_vehicleitempower_68)

    shipBuilder_vehicleitempower_69 = VehicleItemPower()
    shipBuilder_vehicleitempower_69.state = u'Shooting'
    shipBuilder_vehicleitempower_69.value = u'-30'
    shipBuilder_vehicleitempower_69.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitempower_69 = save_or_locate(shipBuilder_vehicleitempower_69)

    shipBuilder_vehicleitempower_70 = VehicleItemPower()
    shipBuilder_vehicleitempower_70.state = u'Active'
    shipBuilder_vehicleitempower_70.value = u'-10'
    shipBuilder_vehicleitempower_70.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitempower_70 = save_or_locate(shipBuilder_vehicleitempower_70)

    shipBuilder_vehicleitempower_71 = VehicleItemPower()
    shipBuilder_vehicleitempower_71.state = u'Idle'
    shipBuilder_vehicleitempower_71.value = u'-3'
    shipBuilder_vehicleitempower_71.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitempower_71 = save_or_locate(shipBuilder_vehicleitempower_71)

    shipBuilder_vehicleitempower_72 = VehicleItemPower()
    shipBuilder_vehicleitempower_72.state = u'Shooting'
    shipBuilder_vehicleitempower_72.value = u'-30'
    shipBuilder_vehicleitempower_72.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitempower_72 = save_or_locate(shipBuilder_vehicleitempower_72)

    shipBuilder_vehicleitempower_73 = VehicleItemPower()
    shipBuilder_vehicleitempower_73.state = u'Active'
    shipBuilder_vehicleitempower_73.value = u'-10'
    shipBuilder_vehicleitempower_73.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitempower_73 = save_or_locate(shipBuilder_vehicleitempower_73)

    shipBuilder_vehicleitempower_74 = VehicleItemPower()
    shipBuilder_vehicleitempower_74.state = u'Idle'
    shipBuilder_vehicleitempower_74.value = u'-3'
    shipBuilder_vehicleitempower_74.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitempower_74 = save_or_locate(shipBuilder_vehicleitempower_74)

    shipBuilder_vehicleitempower_75 = VehicleItemPower()
    shipBuilder_vehicleitempower_75.state = u'Shooting'
    shipBuilder_vehicleitempower_75.value = u'-30'
    shipBuilder_vehicleitempower_75.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitempower_75 = save_or_locate(shipBuilder_vehicleitempower_75)

    shipBuilder_vehicleitempower_76 = VehicleItemPower()
    shipBuilder_vehicleitempower_76.state = u'Default'
    shipBuilder_vehicleitempower_76.value = u'100'
    shipBuilder_vehicleitempower_76.parentItem = shipBuilder_vehicleitem_64
    shipBuilder_vehicleitempower_76 = save_or_locate(shipBuilder_vehicleitempower_76)

    shipBuilder_vehicleitempower_77 = VehicleItemPower()
    shipBuilder_vehicleitempower_77.state = u'Active'
    shipBuilder_vehicleitempower_77.value = u'-10'
    shipBuilder_vehicleitempower_77.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitempower_77 = save_or_locate(shipBuilder_vehicleitempower_77)

    shipBuilder_vehicleitempower_78 = VehicleItemPower()
    shipBuilder_vehicleitempower_78.state = u'Idle'
    shipBuilder_vehicleitempower_78.value = u'-3'
    shipBuilder_vehicleitempower_78.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitempower_78 = save_or_locate(shipBuilder_vehicleitempower_78)

    shipBuilder_vehicleitempower_79 = VehicleItemPower()
    shipBuilder_vehicleitempower_79.state = u'Targeting'
    shipBuilder_vehicleitempower_79.value = u'-80'
    shipBuilder_vehicleitempower_79.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitempower_79 = save_or_locate(shipBuilder_vehicleitempower_79)

    shipBuilder_vehicleitempower_80 = VehicleItemPower()
    shipBuilder_vehicleitempower_80.state = u'Default'
    shipBuilder_vehicleitempower_80.value = u'100'
    shipBuilder_vehicleitempower_80.parentItem = shipBuilder_vehicleitem_73
    shipBuilder_vehicleitempower_80 = save_or_locate(shipBuilder_vehicleitempower_80)

    shipBuilder_vehicleitempower_81 = VehicleItemPower()
    shipBuilder_vehicleitempower_81.state = u'Active'
    shipBuilder_vehicleitempower_81.value = u'-10'
    shipBuilder_vehicleitempower_81.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitempower_81 = save_or_locate(shipBuilder_vehicleitempower_81)

    shipBuilder_vehicleitempower_82 = VehicleItemPower()
    shipBuilder_vehicleitempower_82.state = u'Idle'
    shipBuilder_vehicleitempower_82.value = u'-3'
    shipBuilder_vehicleitempower_82.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitempower_82 = save_or_locate(shipBuilder_vehicleitempower_82)

    shipBuilder_vehicleitempower_83 = VehicleItemPower()
    shipBuilder_vehicleitempower_83.state = u'Shooting'
    shipBuilder_vehicleitempower_83.value = u'-30'
    shipBuilder_vehicleitempower_83.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitempower_83 = save_or_locate(shipBuilder_vehicleitempower_83)

    shipBuilder_vehicleitempower_84 = VehicleItemPower()
    shipBuilder_vehicleitempower_84.state = u'Active'
    shipBuilder_vehicleitempower_84.value = u'-10'
    shipBuilder_vehicleitempower_84.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitempower_84 = save_or_locate(shipBuilder_vehicleitempower_84)

    shipBuilder_vehicleitempower_85 = VehicleItemPower()
    shipBuilder_vehicleitempower_85.state = u'Idle'
    shipBuilder_vehicleitempower_85.value = u'-3'
    shipBuilder_vehicleitempower_85.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitempower_85 = save_or_locate(shipBuilder_vehicleitempower_85)

    shipBuilder_vehicleitempower_86 = VehicleItemPower()
    shipBuilder_vehicleitempower_86.state = u'Targeting'
    shipBuilder_vehicleitempower_86.value = u'-30'
    shipBuilder_vehicleitempower_86.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitempower_86 = save_or_locate(shipBuilder_vehicleitempower_86)

    shipBuilder_vehicleitempower_87 = VehicleItemPower()
    shipBuilder_vehicleitempower_87.state = u'Active'
    shipBuilder_vehicleitempower_87.value = u'-10'
    shipBuilder_vehicleitempower_87.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitempower_87 = save_or_locate(shipBuilder_vehicleitempower_87)

    shipBuilder_vehicleitempower_88 = VehicleItemPower()
    shipBuilder_vehicleitempower_88.state = u'Idle'
    shipBuilder_vehicleitempower_88.value = u'-3'
    shipBuilder_vehicleitempower_88.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitempower_88 = save_or_locate(shipBuilder_vehicleitempower_88)

    shipBuilder_vehicleitempower_89 = VehicleItemPower()
    shipBuilder_vehicleitempower_89.state = u'Targeting'
    shipBuilder_vehicleitempower_89.value = u'-30'
    shipBuilder_vehicleitempower_89.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitempower_89 = save_or_locate(shipBuilder_vehicleitempower_89)

    shipBuilder_vehicleitempower_90 = VehicleItemPower()
    shipBuilder_vehicleitempower_90.state = u'Active'
    shipBuilder_vehicleitempower_90.value = u'-10'
    shipBuilder_vehicleitempower_90.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitempower_90 = save_or_locate(shipBuilder_vehicleitempower_90)

    shipBuilder_vehicleitempower_91 = VehicleItemPower()
    shipBuilder_vehicleitempower_91.state = u'Idle'
    shipBuilder_vehicleitempower_91.value = u'-3'
    shipBuilder_vehicleitempower_91.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitempower_91 = save_or_locate(shipBuilder_vehicleitempower_91)

    shipBuilder_vehicleitempower_92 = VehicleItemPower()
    shipBuilder_vehicleitempower_92.state = u'Targeting'
    shipBuilder_vehicleitempower_92.value = u'-30'
    shipBuilder_vehicleitempower_92.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitempower_92 = save_or_locate(shipBuilder_vehicleitempower_92)

    shipBuilder_vehicleitempower_93 = VehicleItemPower()
    shipBuilder_vehicleitempower_93.state = u'Active'
    shipBuilder_vehicleitempower_93.value = u'-10'
    shipBuilder_vehicleitempower_93.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitempower_93 = save_or_locate(shipBuilder_vehicleitempower_93)

    shipBuilder_vehicleitempower_94 = VehicleItemPower()
    shipBuilder_vehicleitempower_94.state = u'Idle'
    shipBuilder_vehicleitempower_94.value = u'-3'
    shipBuilder_vehicleitempower_94.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitempower_94 = save_or_locate(shipBuilder_vehicleitempower_94)

    shipBuilder_vehicleitempower_95 = VehicleItemPower()
    shipBuilder_vehicleitempower_95.state = u'Targeting'
    shipBuilder_vehicleitempower_95.value = u'-30'
    shipBuilder_vehicleitempower_95.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitempower_95 = save_or_locate(shipBuilder_vehicleitempower_95)

    shipBuilder_vehicleitempower_96 = VehicleItemPower()
    shipBuilder_vehicleitempower_96.state = u'Default'
    shipBuilder_vehicleitempower_96.value = u'100'
    shipBuilder_vehicleitempower_96.parentItem = shipBuilder_vehicleitem_86
    shipBuilder_vehicleitempower_96 = save_or_locate(shipBuilder_vehicleitempower_96)

    shipBuilder_vehicleitempower_97 = VehicleItemPower()
    shipBuilder_vehicleitempower_97.state = u'Default'
    shipBuilder_vehicleitempower_97.value = u'100'
    shipBuilder_vehicleitempower_97.parentItem = shipBuilder_vehicleitem_87
    shipBuilder_vehicleitempower_97 = save_or_locate(shipBuilder_vehicleitempower_97)

    shipBuilder_vehicleitempower_98 = VehicleItemPower()
    shipBuilder_vehicleitempower_98.state = u'Active'
    shipBuilder_vehicleitempower_98.value = u'-10'
    shipBuilder_vehicleitempower_98.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitempower_98 = save_or_locate(shipBuilder_vehicleitempower_98)

    shipBuilder_vehicleitempower_99 = VehicleItemPower()
    shipBuilder_vehicleitempower_99.state = u'Idle'
    shipBuilder_vehicleitempower_99.value = u'-10'
    shipBuilder_vehicleitempower_99.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitempower_99 = save_or_locate(shipBuilder_vehicleitempower_99)

    shipBuilder_vehicleitempower_100 = VehicleItemPower()
    shipBuilder_vehicleitempower_100.state = u'Shooting'
    shipBuilder_vehicleitempower_100.value = u'-80'
    shipBuilder_vehicleitempower_100.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitempower_100 = save_or_locate(shipBuilder_vehicleitempower_100)

    shipBuilder_vehicleitempower_101 = VehicleItemPower()
    shipBuilder_vehicleitempower_101.state = u'Active'
    shipBuilder_vehicleitempower_101.value = u'-10'
    shipBuilder_vehicleitempower_101.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitempower_101 = save_or_locate(shipBuilder_vehicleitempower_101)

    shipBuilder_vehicleitempower_102 = VehicleItemPower()
    shipBuilder_vehicleitempower_102.state = u'Idle'
    shipBuilder_vehicleitempower_102.value = u'-10'
    shipBuilder_vehicleitempower_102.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitempower_102 = save_or_locate(shipBuilder_vehicleitempower_102)

    shipBuilder_vehicleitempower_103 = VehicleItemPower()
    shipBuilder_vehicleitempower_103.state = u'Shooting'
    shipBuilder_vehicleitempower_103.value = u'-80'
    shipBuilder_vehicleitempower_103.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitempower_103 = save_or_locate(shipBuilder_vehicleitempower_103)

    #Processing model: VehicleItemHeat

    from shipBuilder.models import VehicleItemHeat

    shipBuilder_vehicleitemheat_1 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_1.state = u'Active'
    shipBuilder_vehicleitemheat_1.value = u'3'
    shipBuilder_vehicleitemheat_1.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemheat_1 = save_or_locate(shipBuilder_vehicleitemheat_1)

    shipBuilder_vehicleitemheat_2 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_2.state = u'Idle'
    shipBuilder_vehicleitemheat_2.value = u'3'
    shipBuilder_vehicleitemheat_2.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemheat_2 = save_or_locate(shipBuilder_vehicleitemheat_2)

    shipBuilder_vehicleitemheat_3 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_3.state = u'Shooting'
    shipBuilder_vehicleitemheat_3.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_3.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemheat_3 = save_or_locate(shipBuilder_vehicleitemheat_3)

    shipBuilder_vehicleitemheat_4 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_4.state = u'Active'
    shipBuilder_vehicleitemheat_4.value = u'3'
    shipBuilder_vehicleitemheat_4.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemheat_4 = save_or_locate(shipBuilder_vehicleitemheat_4)

    shipBuilder_vehicleitemheat_5 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_5.state = u'Idle'
    shipBuilder_vehicleitemheat_5.value = u'3'
    shipBuilder_vehicleitemheat_5.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemheat_5 = save_or_locate(shipBuilder_vehicleitemheat_5)

    shipBuilder_vehicleitemheat_6 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_6.state = u'Shooting'
    shipBuilder_vehicleitemheat_6.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_6.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemheat_6 = save_or_locate(shipBuilder_vehicleitemheat_6)

    shipBuilder_vehicleitemheat_7 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_7.state = u'Active'
    shipBuilder_vehicleitemheat_7.value = u'3'
    shipBuilder_vehicleitemheat_7.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitemheat_7 = save_or_locate(shipBuilder_vehicleitemheat_7)

    shipBuilder_vehicleitemheat_8 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_8.state = u'Idle'
    shipBuilder_vehicleitemheat_8.value = u'3'
    shipBuilder_vehicleitemheat_8.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitemheat_8 = save_or_locate(shipBuilder_vehicleitemheat_8)

    shipBuilder_vehicleitemheat_9 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_9.state = u'Shooting'
    shipBuilder_vehicleitemheat_9.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_9.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitemheat_9 = save_or_locate(shipBuilder_vehicleitemheat_9)

    shipBuilder_vehicleitemheat_10 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_10.state = u'Active'
    shipBuilder_vehicleitemheat_10.value = u'3'
    shipBuilder_vehicleitemheat_10.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemheat_10 = save_or_locate(shipBuilder_vehicleitemheat_10)

    shipBuilder_vehicleitemheat_11 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_11.state = u'Idle'
    shipBuilder_vehicleitemheat_11.value = u'3'
    shipBuilder_vehicleitemheat_11.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemheat_11 = save_or_locate(shipBuilder_vehicleitemheat_11)

    shipBuilder_vehicleitemheat_12 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_12.state = u'Shooting'
    shipBuilder_vehicleitemheat_12.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_12.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemheat_12 = save_or_locate(shipBuilder_vehicleitemheat_12)

    shipBuilder_vehicleitemheat_13 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_13.state = u'Active'
    shipBuilder_vehicleitemheat_13.value = u'3'
    shipBuilder_vehicleitemheat_13.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemheat_13 = save_or_locate(shipBuilder_vehicleitemheat_13)

    shipBuilder_vehicleitemheat_14 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_14.state = u'Idle'
    shipBuilder_vehicleitemheat_14.value = u'3'
    shipBuilder_vehicleitemheat_14.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemheat_14 = save_or_locate(shipBuilder_vehicleitemheat_14)

    shipBuilder_vehicleitemheat_15 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_15.state = u'Targeting'
    shipBuilder_vehicleitemheat_15.value = u'3'
    shipBuilder_vehicleitemheat_15.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemheat_15 = save_or_locate(shipBuilder_vehicleitemheat_15)

    shipBuilder_vehicleitemheat_16 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_16.state = u'Active'
    shipBuilder_vehicleitemheat_16.value = u'3'
    shipBuilder_vehicleitemheat_16.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemheat_16 = save_or_locate(shipBuilder_vehicleitemheat_16)

    shipBuilder_vehicleitemheat_17 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_17.state = u'Idle'
    shipBuilder_vehicleitemheat_17.value = u'3'
    shipBuilder_vehicleitemheat_17.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemheat_17 = save_or_locate(shipBuilder_vehicleitemheat_17)

    shipBuilder_vehicleitemheat_18 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_18.state = u'Targeting'
    shipBuilder_vehicleitemheat_18.value = u'3'
    shipBuilder_vehicleitemheat_18.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemheat_18 = save_or_locate(shipBuilder_vehicleitemheat_18)

    shipBuilder_vehicleitemheat_19 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_19.state = u'Active'
    shipBuilder_vehicleitemheat_19.value = u'3'
    shipBuilder_vehicleitemheat_19.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemheat_19 = save_or_locate(shipBuilder_vehicleitemheat_19)

    shipBuilder_vehicleitemheat_20 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_20.state = u'Idle'
    shipBuilder_vehicleitemheat_20.value = u'3'
    shipBuilder_vehicleitemheat_20.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemheat_20 = save_or_locate(shipBuilder_vehicleitemheat_20)

    shipBuilder_vehicleitemheat_21 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_21.state = u'Shooting'
    shipBuilder_vehicleitemheat_21.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_21.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemheat_21 = save_or_locate(shipBuilder_vehicleitemheat_21)

    shipBuilder_vehicleitemheat_22 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_22.state = u'Active'
    shipBuilder_vehicleitemheat_22.value = u'3'
    shipBuilder_vehicleitemheat_22.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitemheat_22 = save_or_locate(shipBuilder_vehicleitemheat_22)

    shipBuilder_vehicleitemheat_23 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_23.state = u'Idle'
    shipBuilder_vehicleitemheat_23.value = u'3'
    shipBuilder_vehicleitemheat_23.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitemheat_23 = save_or_locate(shipBuilder_vehicleitemheat_23)

    shipBuilder_vehicleitemheat_24 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_24.state = u'Shooting'
    shipBuilder_vehicleitemheat_24.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_24.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitemheat_24 = save_or_locate(shipBuilder_vehicleitemheat_24)

    shipBuilder_vehicleitemheat_25 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_25.state = u'Active'
    shipBuilder_vehicleitemheat_25.value = u'3'
    shipBuilder_vehicleitemheat_25.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemheat_25 = save_or_locate(shipBuilder_vehicleitemheat_25)

    shipBuilder_vehicleitemheat_26 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_26.state = u'Idle'
    shipBuilder_vehicleitemheat_26.value = u'3'
    shipBuilder_vehicleitemheat_26.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemheat_26 = save_or_locate(shipBuilder_vehicleitemheat_26)

    shipBuilder_vehicleitemheat_27 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_27.state = u'Shooting'
    shipBuilder_vehicleitemheat_27.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_27.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemheat_27 = save_or_locate(shipBuilder_vehicleitemheat_27)

    shipBuilder_vehicleitemheat_28 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_28.state = u'Active'
    shipBuilder_vehicleitemheat_28.value = u'3'
    shipBuilder_vehicleitemheat_28.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemheat_28 = save_or_locate(shipBuilder_vehicleitemheat_28)

    shipBuilder_vehicleitemheat_29 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_29.state = u'Idle'
    shipBuilder_vehicleitemheat_29.value = u'3'
    shipBuilder_vehicleitemheat_29.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemheat_29 = save_or_locate(shipBuilder_vehicleitemheat_29)

    shipBuilder_vehicleitemheat_30 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_30.state = u'Shooting'
    shipBuilder_vehicleitemheat_30.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_30.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemheat_30 = save_or_locate(shipBuilder_vehicleitemheat_30)

    shipBuilder_vehicleitemheat_31 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_31.state = u'Active'
    shipBuilder_vehicleitemheat_31.value = u'3'
    shipBuilder_vehicleitemheat_31.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemheat_31 = save_or_locate(shipBuilder_vehicleitemheat_31)

    shipBuilder_vehicleitemheat_32 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_32.state = u'Idle'
    shipBuilder_vehicleitemheat_32.value = u'3'
    shipBuilder_vehicleitemheat_32.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemheat_32 = save_or_locate(shipBuilder_vehicleitemheat_32)

    shipBuilder_vehicleitemheat_33 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_33.state = u'Shooting'
    shipBuilder_vehicleitemheat_33.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_33.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemheat_33 = save_or_locate(shipBuilder_vehicleitemheat_33)

    shipBuilder_vehicleitemheat_34 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_34.state = u'Active'
    shipBuilder_vehicleitemheat_34.value = u'3'
    shipBuilder_vehicleitemheat_34.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemheat_34 = save_or_locate(shipBuilder_vehicleitemheat_34)

    shipBuilder_vehicleitemheat_35 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_35.state = u'Idle'
    shipBuilder_vehicleitemheat_35.value = u'3'
    shipBuilder_vehicleitemheat_35.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemheat_35 = save_or_locate(shipBuilder_vehicleitemheat_35)

    shipBuilder_vehicleitemheat_36 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_36.state = u'Shooting'
    shipBuilder_vehicleitemheat_36.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_36.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemheat_36 = save_or_locate(shipBuilder_vehicleitemheat_36)

    shipBuilder_vehicleitemheat_37 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_37.state = u'Active'
    shipBuilder_vehicleitemheat_37.value = u'3'
    shipBuilder_vehicleitemheat_37.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitemheat_37 = save_or_locate(shipBuilder_vehicleitemheat_37)

    shipBuilder_vehicleitemheat_38 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_38.state = u'Idle'
    shipBuilder_vehicleitemheat_38.value = u'3'
    shipBuilder_vehicleitemheat_38.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitemheat_38 = save_or_locate(shipBuilder_vehicleitemheat_38)

    shipBuilder_vehicleitemheat_39 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_39.state = u'Shooting'
    shipBuilder_vehicleitemheat_39.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_39.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitemheat_39 = save_or_locate(shipBuilder_vehicleitemheat_39)

    shipBuilder_vehicleitemheat_40 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_40.state = u'Active'
    shipBuilder_vehicleitemheat_40.value = u'3'
    shipBuilder_vehicleitemheat_40.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitemheat_40 = save_or_locate(shipBuilder_vehicleitemheat_40)

    shipBuilder_vehicleitemheat_41 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_41.state = u'Idle'
    shipBuilder_vehicleitemheat_41.value = u'3'
    shipBuilder_vehicleitemheat_41.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitemheat_41 = save_or_locate(shipBuilder_vehicleitemheat_41)

    shipBuilder_vehicleitemheat_42 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_42.state = u'Shooting'
    shipBuilder_vehicleitemheat_42.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_42.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitemheat_42 = save_or_locate(shipBuilder_vehicleitemheat_42)

    shipBuilder_vehicleitemheat_43 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_43.state = u'Active'
    shipBuilder_vehicleitemheat_43.value = u'3'
    shipBuilder_vehicleitemheat_43.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemheat_43 = save_or_locate(shipBuilder_vehicleitemheat_43)

    shipBuilder_vehicleitemheat_44 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_44.state = u'Idle'
    shipBuilder_vehicleitemheat_44.value = u'3'
    shipBuilder_vehicleitemheat_44.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemheat_44 = save_or_locate(shipBuilder_vehicleitemheat_44)

    shipBuilder_vehicleitemheat_45 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_45.state = u'Shooting'
    shipBuilder_vehicleitemheat_45.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_45.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemheat_45 = save_or_locate(shipBuilder_vehicleitemheat_45)

    shipBuilder_vehicleitemheat_46 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_46.state = u'Active'
    shipBuilder_vehicleitemheat_46.value = u'3'
    shipBuilder_vehicleitemheat_46.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemheat_46 = save_or_locate(shipBuilder_vehicleitemheat_46)

    shipBuilder_vehicleitemheat_47 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_47.state = u'Idle'
    shipBuilder_vehicleitemheat_47.value = u'3'
    shipBuilder_vehicleitemheat_47.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemheat_47 = save_or_locate(shipBuilder_vehicleitemheat_47)

    shipBuilder_vehicleitemheat_48 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_48.state = u'Shooting'
    shipBuilder_vehicleitemheat_48.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_48.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemheat_48 = save_or_locate(shipBuilder_vehicleitemheat_48)

    shipBuilder_vehicleitemheat_49 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_49.state = u'Active'
    shipBuilder_vehicleitemheat_49.value = u'3'
    shipBuilder_vehicleitemheat_49.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitemheat_49 = save_or_locate(shipBuilder_vehicleitemheat_49)

    shipBuilder_vehicleitemheat_50 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_50.state = u'Idle'
    shipBuilder_vehicleitemheat_50.value = u'3'
    shipBuilder_vehicleitemheat_50.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitemheat_50 = save_or_locate(shipBuilder_vehicleitemheat_50)

    shipBuilder_vehicleitemheat_51 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_51.state = u'Shooting'
    shipBuilder_vehicleitemheat_51.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_51.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitemheat_51 = save_or_locate(shipBuilder_vehicleitemheat_51)

    shipBuilder_vehicleitemheat_52 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_52.state = u'Active'
    shipBuilder_vehicleitemheat_52.value = u'3'
    shipBuilder_vehicleitemheat_52.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemheat_52 = save_or_locate(shipBuilder_vehicleitemheat_52)

    shipBuilder_vehicleitemheat_53 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_53.state = u'Idle'
    shipBuilder_vehicleitemheat_53.value = u'3'
    shipBuilder_vehicleitemheat_53.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemheat_53 = save_or_locate(shipBuilder_vehicleitemheat_53)

    shipBuilder_vehicleitemheat_54 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_54.state = u'Shooting'
    shipBuilder_vehicleitemheat_54.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_54.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemheat_54 = save_or_locate(shipBuilder_vehicleitemheat_54)

    shipBuilder_vehicleitemheat_55 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_55.state = u'Active'
    shipBuilder_vehicleitemheat_55.value = u'3'
    shipBuilder_vehicleitemheat_55.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitemheat_55 = save_or_locate(shipBuilder_vehicleitemheat_55)

    shipBuilder_vehicleitemheat_56 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_56.state = u'Idle'
    shipBuilder_vehicleitemheat_56.value = u'3'
    shipBuilder_vehicleitemheat_56.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitemheat_56 = save_or_locate(shipBuilder_vehicleitemheat_56)

    shipBuilder_vehicleitemheat_57 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_57.state = u'Shooting'
    shipBuilder_vehicleitemheat_57.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_57.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitemheat_57 = save_or_locate(shipBuilder_vehicleitemheat_57)

    shipBuilder_vehicleitemheat_58 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_58.state = u'Active'
    shipBuilder_vehicleitemheat_58.value = u'3'
    shipBuilder_vehicleitemheat_58.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemheat_58 = save_or_locate(shipBuilder_vehicleitemheat_58)

    shipBuilder_vehicleitemheat_59 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_59.state = u'Idle'
    shipBuilder_vehicleitemheat_59.value = u'3'
    shipBuilder_vehicleitemheat_59.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemheat_59 = save_or_locate(shipBuilder_vehicleitemheat_59)

    shipBuilder_vehicleitemheat_60 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_60.state = u'Shooting'
    shipBuilder_vehicleitemheat_60.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_60.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemheat_60 = save_or_locate(shipBuilder_vehicleitemheat_60)

    shipBuilder_vehicleitemheat_61 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_61.state = u'Default'
    shipBuilder_vehicleitemheat_61.value = u'-30'
    shipBuilder_vehicleitemheat_61.parentItem = shipBuilder_vehicleitem_63
    shipBuilder_vehicleitemheat_61 = save_or_locate(shipBuilder_vehicleitemheat_61)

    shipBuilder_vehicleitemheat_62 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_62.state = u'Active'
    shipBuilder_vehicleitemheat_62.value = u'3'
    shipBuilder_vehicleitemheat_62.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitemheat_62 = save_or_locate(shipBuilder_vehicleitemheat_62)

    shipBuilder_vehicleitemheat_63 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_63.state = u'Idle'
    shipBuilder_vehicleitemheat_63.value = u'3'
    shipBuilder_vehicleitemheat_63.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitemheat_63 = save_or_locate(shipBuilder_vehicleitemheat_63)

    shipBuilder_vehicleitemheat_64 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_64.state = u'Targeting'
    shipBuilder_vehicleitemheat_64.value = u'3'
    shipBuilder_vehicleitemheat_64.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitemheat_64 = save_or_locate(shipBuilder_vehicleitemheat_64)

    shipBuilder_vehicleitemheat_65 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_65.state = u'Active'
    shipBuilder_vehicleitemheat_65.value = u'3'
    shipBuilder_vehicleitemheat_65.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitemheat_65 = save_or_locate(shipBuilder_vehicleitemheat_65)

    shipBuilder_vehicleitemheat_66 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_66.state = u'Idle'
    shipBuilder_vehicleitemheat_66.value = u'3'
    shipBuilder_vehicleitemheat_66.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitemheat_66 = save_or_locate(shipBuilder_vehicleitemheat_66)

    shipBuilder_vehicleitemheat_67 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_67.state = u'Shooting'
    shipBuilder_vehicleitemheat_67.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_67.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitemheat_67 = save_or_locate(shipBuilder_vehicleitemheat_67)

    shipBuilder_vehicleitemheat_68 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_68.state = u'Active'
    shipBuilder_vehicleitemheat_68.value = u'3'
    shipBuilder_vehicleitemheat_68.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemheat_68 = save_or_locate(shipBuilder_vehicleitemheat_68)

    shipBuilder_vehicleitemheat_69 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_69.state = u'Idle'
    shipBuilder_vehicleitemheat_69.value = u'3'
    shipBuilder_vehicleitemheat_69.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemheat_69 = save_or_locate(shipBuilder_vehicleitemheat_69)

    shipBuilder_vehicleitemheat_70 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_70.state = u'Targeting'
    shipBuilder_vehicleitemheat_70.value = u'3'
    shipBuilder_vehicleitemheat_70.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemheat_70 = save_or_locate(shipBuilder_vehicleitemheat_70)

    shipBuilder_vehicleitemheat_71 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_71.state = u'Active'
    shipBuilder_vehicleitemheat_71.value = u'3'
    shipBuilder_vehicleitemheat_71.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemheat_71 = save_or_locate(shipBuilder_vehicleitemheat_71)

    shipBuilder_vehicleitemheat_72 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_72.state = u'Idle'
    shipBuilder_vehicleitemheat_72.value = u'3'
    shipBuilder_vehicleitemheat_72.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemheat_72 = save_or_locate(shipBuilder_vehicleitemheat_72)

    shipBuilder_vehicleitemheat_73 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_73.state = u'Targeting'
    shipBuilder_vehicleitemheat_73.value = u'3'
    shipBuilder_vehicleitemheat_73.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemheat_73 = save_or_locate(shipBuilder_vehicleitemheat_73)

    shipBuilder_vehicleitemheat_74 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_74.state = u'Active'
    shipBuilder_vehicleitemheat_74.value = u'3'
    shipBuilder_vehicleitemheat_74.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemheat_74 = save_or_locate(shipBuilder_vehicleitemheat_74)

    shipBuilder_vehicleitemheat_75 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_75.state = u'Idle'
    shipBuilder_vehicleitemheat_75.value = u'3'
    shipBuilder_vehicleitemheat_75.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemheat_75 = save_or_locate(shipBuilder_vehicleitemheat_75)

    shipBuilder_vehicleitemheat_76 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_76.state = u'Targeting'
    shipBuilder_vehicleitemheat_76.value = u'3'
    shipBuilder_vehicleitemheat_76.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemheat_76 = save_or_locate(shipBuilder_vehicleitemheat_76)

    shipBuilder_vehicleitemheat_77 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_77.state = u'Active'
    shipBuilder_vehicleitemheat_77.value = u'3'
    shipBuilder_vehicleitemheat_77.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemheat_77 = save_or_locate(shipBuilder_vehicleitemheat_77)

    shipBuilder_vehicleitemheat_78 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_78.state = u'Idle'
    shipBuilder_vehicleitemheat_78.value = u'3'
    shipBuilder_vehicleitemheat_78.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemheat_78 = save_or_locate(shipBuilder_vehicleitemheat_78)

    shipBuilder_vehicleitemheat_79 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_79.state = u'Targeting'
    shipBuilder_vehicleitemheat_79.value = u'3'
    shipBuilder_vehicleitemheat_79.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemheat_79 = save_or_locate(shipBuilder_vehicleitemheat_79)

    shipBuilder_vehicleitemheat_80 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_80.state = u'Active'
    shipBuilder_vehicleitemheat_80.value = u'3'
    shipBuilder_vehicleitemheat_80.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitemheat_80 = save_or_locate(shipBuilder_vehicleitemheat_80)

    shipBuilder_vehicleitemheat_81 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_81.state = u'Idle'
    shipBuilder_vehicleitemheat_81.value = u'3'
    shipBuilder_vehicleitemheat_81.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitemheat_81 = save_or_locate(shipBuilder_vehicleitemheat_81)

    shipBuilder_vehicleitemheat_82 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_82.state = u'Shooting'
    shipBuilder_vehicleitemheat_82.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_82.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitemheat_82 = save_or_locate(shipBuilder_vehicleitemheat_82)

    shipBuilder_vehicleitemheat_83 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_83.state = u'Active'
    shipBuilder_vehicleitemheat_83.value = u'3'
    shipBuilder_vehicleitemheat_83.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitemheat_83 = save_or_locate(shipBuilder_vehicleitemheat_83)

    shipBuilder_vehicleitemheat_84 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_84.state = u'Idle'
    shipBuilder_vehicleitemheat_84.value = u'3'
    shipBuilder_vehicleitemheat_84.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitemheat_84 = save_or_locate(shipBuilder_vehicleitemheat_84)

    shipBuilder_vehicleitemheat_85 = VehicleItemHeat()
    shipBuilder_vehicleitemheat_85.state = u'Shooting'
    shipBuilder_vehicleitemheat_85.value = u'0:3,3:10,5:10,7:10,10:20'
    shipBuilder_vehicleitemheat_85.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitemheat_85 = save_or_locate(shipBuilder_vehicleitemheat_85)

    #Re-processing model: VehicleItemAvionics

    shipBuilder_vehicleitemavionics_1.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemavionics_1 = save_or_locate(shipBuilder_vehicleitemavionics_1)

    shipBuilder_vehicleitemavionics_2.parentItem = shipBuilder_vehicleitem_25
    shipBuilder_vehicleitemavionics_2 = save_or_locate(shipBuilder_vehicleitemavionics_2)

    shipBuilder_vehicleitemavionics_3.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemavionics_3 = save_or_locate(shipBuilder_vehicleitemavionics_3)

    shipBuilder_vehicleitemavionics_4.parentItem = shipBuilder_vehicleitem_26
    shipBuilder_vehicleitemavionics_4 = save_or_locate(shipBuilder_vehicleitemavionics_4)

    shipBuilder_vehicleitemavionics_5.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitemavionics_5 = save_or_locate(shipBuilder_vehicleitemavionics_5)

    shipBuilder_vehicleitemavionics_6.parentItem = shipBuilder_vehicleitem_27
    shipBuilder_vehicleitemavionics_6 = save_or_locate(shipBuilder_vehicleitemavionics_6)

    shipBuilder_vehicleitemavionics_7.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemavionics_7 = save_or_locate(shipBuilder_vehicleitemavionics_7)

    shipBuilder_vehicleitemavionics_8.parentItem = shipBuilder_vehicleitem_28
    shipBuilder_vehicleitemavionics_8 = save_or_locate(shipBuilder_vehicleitemavionics_8)

    shipBuilder_vehicleitemavionics_9.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemavionics_9 = save_or_locate(shipBuilder_vehicleitemavionics_9)

    shipBuilder_vehicleitemavionics_10.parentItem = shipBuilder_vehicleitem_29
    shipBuilder_vehicleitemavionics_10 = save_or_locate(shipBuilder_vehicleitemavionics_10)

    shipBuilder_vehicleitemavionics_11.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemavionics_11 = save_or_locate(shipBuilder_vehicleitemavionics_11)

    shipBuilder_vehicleitemavionics_12.parentItem = shipBuilder_vehicleitem_30
    shipBuilder_vehicleitemavionics_12 = save_or_locate(shipBuilder_vehicleitemavionics_12)

    shipBuilder_vehicleitemavionics_13.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemavionics_13 = save_or_locate(shipBuilder_vehicleitemavionics_13)

    shipBuilder_vehicleitemavionics_14.parentItem = shipBuilder_vehicleitem_31
    shipBuilder_vehicleitemavionics_14 = save_or_locate(shipBuilder_vehicleitemavionics_14)

    shipBuilder_vehicleitemavionics_15.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitemavionics_15 = save_or_locate(shipBuilder_vehicleitemavionics_15)

    shipBuilder_vehicleitemavionics_16.parentItem = shipBuilder_vehicleitem_40
    shipBuilder_vehicleitemavionics_16 = save_or_locate(shipBuilder_vehicleitemavionics_16)

    shipBuilder_vehicleitemavionics_17.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemavionics_17 = save_or_locate(shipBuilder_vehicleitemavionics_17)

    shipBuilder_vehicleitemavionics_18.parentItem = shipBuilder_vehicleitem_42
    shipBuilder_vehicleitemavionics_18 = save_or_locate(shipBuilder_vehicleitemavionics_18)

    shipBuilder_vehicleitemavionics_19.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemavionics_19 = save_or_locate(shipBuilder_vehicleitemavionics_19)

    shipBuilder_vehicleitemavionics_20.parentItem = shipBuilder_vehicleitem_43
    shipBuilder_vehicleitemavionics_20 = save_or_locate(shipBuilder_vehicleitemavionics_20)

    shipBuilder_vehicleitemavionics_21.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemavionics_21 = save_or_locate(shipBuilder_vehicleitemavionics_21)

    shipBuilder_vehicleitemavionics_22.parentItem = shipBuilder_vehicleitem_44
    shipBuilder_vehicleitemavionics_22 = save_or_locate(shipBuilder_vehicleitemavionics_22)

    shipBuilder_vehicleitemavionics_23.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemavionics_23 = save_or_locate(shipBuilder_vehicleitemavionics_23)

    shipBuilder_vehicleitemavionics_24.parentItem = shipBuilder_vehicleitem_45
    shipBuilder_vehicleitemavionics_24 = save_or_locate(shipBuilder_vehicleitemavionics_24)

    shipBuilder_vehicleitemavionics_25.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitemavionics_25 = save_or_locate(shipBuilder_vehicleitemavionics_25)

    shipBuilder_vehicleitemavionics_26.parentItem = shipBuilder_vehicleitem_46
    shipBuilder_vehicleitemavionics_26 = save_or_locate(shipBuilder_vehicleitemavionics_26)

    shipBuilder_vehicleitemavionics_27.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitemavionics_27 = save_or_locate(shipBuilder_vehicleitemavionics_27)

    shipBuilder_vehicleitemavionics_28.parentItem = shipBuilder_vehicleitem_47
    shipBuilder_vehicleitemavionics_28 = save_or_locate(shipBuilder_vehicleitemavionics_28)

    shipBuilder_vehicleitemavionics_29.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemavionics_29 = save_or_locate(shipBuilder_vehicleitemavionics_29)

    shipBuilder_vehicleitemavionics_30.parentItem = shipBuilder_vehicleitem_49
    shipBuilder_vehicleitemavionics_30 = save_or_locate(shipBuilder_vehicleitemavionics_30)

    shipBuilder_vehicleitemavionics_31.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemavionics_31 = save_or_locate(shipBuilder_vehicleitemavionics_31)

    shipBuilder_vehicleitemavionics_32.parentItem = shipBuilder_vehicleitem_50
    shipBuilder_vehicleitemavionics_32 = save_or_locate(shipBuilder_vehicleitemavionics_32)

    shipBuilder_vehicleitemavionics_33.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitemavionics_33 = save_or_locate(shipBuilder_vehicleitemavionics_33)

    shipBuilder_vehicleitemavionics_34.parentItem = shipBuilder_vehicleitem_53
    shipBuilder_vehicleitemavionics_34 = save_or_locate(shipBuilder_vehicleitemavionics_34)

    shipBuilder_vehicleitemavionics_35.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemavionics_35 = save_or_locate(shipBuilder_vehicleitemavionics_35)

    shipBuilder_vehicleitemavionics_36.parentItem = shipBuilder_vehicleitem_54
    shipBuilder_vehicleitemavionics_36 = save_or_locate(shipBuilder_vehicleitemavionics_36)

    shipBuilder_vehicleitemavionics_37.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitemavionics_37 = save_or_locate(shipBuilder_vehicleitemavionics_37)

    shipBuilder_vehicleitemavionics_38.parentItem = shipBuilder_vehicleitem_59
    shipBuilder_vehicleitemavionics_38 = save_or_locate(shipBuilder_vehicleitemavionics_38)

    shipBuilder_vehicleitemavionics_39.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemavionics_39 = save_or_locate(shipBuilder_vehicleitemavionics_39)

    shipBuilder_vehicleitemavionics_40.parentItem = shipBuilder_vehicleitem_60
    shipBuilder_vehicleitemavionics_40 = save_or_locate(shipBuilder_vehicleitemavionics_40)

    shipBuilder_vehicleitemavionics_41.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitemavionics_41 = save_or_locate(shipBuilder_vehicleitemavionics_41)

    shipBuilder_vehicleitemavionics_42.parentItem = shipBuilder_vehicleitem_72
    shipBuilder_vehicleitemavionics_42 = save_or_locate(shipBuilder_vehicleitemavionics_42)

    shipBuilder_vehicleitemavionics_43.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitemavionics_43 = save_or_locate(shipBuilder_vehicleitemavionics_43)

    shipBuilder_vehicleitemavionics_44.parentItem = shipBuilder_vehicleitem_77
    shipBuilder_vehicleitemavionics_44 = save_or_locate(shipBuilder_vehicleitemavionics_44)

    shipBuilder_vehicleitemavionics_45.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemavionics_45 = save_or_locate(shipBuilder_vehicleitemavionics_45)

    shipBuilder_vehicleitemavionics_46.parentItem = shipBuilder_vehicleitem_82
    shipBuilder_vehicleitemavionics_46 = save_or_locate(shipBuilder_vehicleitemavionics_46)

    shipBuilder_vehicleitemavionics_47.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemavionics_47 = save_or_locate(shipBuilder_vehicleitemavionics_47)

    shipBuilder_vehicleitemavionics_48.parentItem = shipBuilder_vehicleitem_83
    shipBuilder_vehicleitemavionics_48 = save_or_locate(shipBuilder_vehicleitemavionics_48)

    shipBuilder_vehicleitemavionics_49.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemavionics_49 = save_or_locate(shipBuilder_vehicleitemavionics_49)

    shipBuilder_vehicleitemavionics_50.parentItem = shipBuilder_vehicleitem_84
    shipBuilder_vehicleitemavionics_50 = save_or_locate(shipBuilder_vehicleitemavionics_50)

    shipBuilder_vehicleitemavionics_51.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemavionics_51 = save_or_locate(shipBuilder_vehicleitemavionics_51)

    shipBuilder_vehicleitemavionics_52.parentItem = shipBuilder_vehicleitem_85
    shipBuilder_vehicleitemavionics_52 = save_or_locate(shipBuilder_vehicleitemavionics_52)

    shipBuilder_vehicleitemavionics_53.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitemavionics_53 = save_or_locate(shipBuilder_vehicleitemavionics_53)

    shipBuilder_vehicleitemavionics_54.parentItem = shipBuilder_vehicleitem_89
    shipBuilder_vehicleitemavionics_54 = save_or_locate(shipBuilder_vehicleitemavionics_54)

    shipBuilder_vehicleitemavionics_55.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitemavionics_55 = save_or_locate(shipBuilder_vehicleitemavionics_55)

    shipBuilder_vehicleitemavionics_56.parentItem = shipBuilder_vehicleitem_90
    shipBuilder_vehicleitemavionics_56 = save_or_locate(shipBuilder_vehicleitemavionics_56)

    #Re-processing model: VehicleItem

    #Re-processing model: ItemPort

    shipBuilder_itemport_1.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_1 = save_or_locate(shipBuilder_itemport_1)

    shipBuilder_itemport_2.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_2 = save_or_locate(shipBuilder_itemport_2)

    shipBuilder_itemport_3.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_3 = save_or_locate(shipBuilder_itemport_3)

    shipBuilder_itemport_4.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_4 = save_or_locate(shipBuilder_itemport_4)

    shipBuilder_itemport_5.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_5 = save_or_locate(shipBuilder_itemport_5)

    shipBuilder_itemport_6.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_6 = save_or_locate(shipBuilder_itemport_6)

    shipBuilder_itemport_7.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_7 = save_or_locate(shipBuilder_itemport_7)

    shipBuilder_itemport_8.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_8 = save_or_locate(shipBuilder_itemport_8)

    shipBuilder_itemport_9.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_9 = save_or_locate(shipBuilder_itemport_9)

    shipBuilder_itemport_10.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_10 = save_or_locate(shipBuilder_itemport_10)

    shipBuilder_itemport_11.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_11 = save_or_locate(shipBuilder_itemport_11)

    shipBuilder_itemport_12.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_12 = save_or_locate(shipBuilder_itemport_12)

    shipBuilder_itemport_13.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_13 = save_or_locate(shipBuilder_itemport_13)

    shipBuilder_itemport_14.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_14 = save_or_locate(shipBuilder_itemport_14)

    shipBuilder_itemport_15.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_15 = save_or_locate(shipBuilder_itemport_15)

    shipBuilder_itemport_16.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_16 = save_or_locate(shipBuilder_itemport_16)

    shipBuilder_itemport_17.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_17 = save_or_locate(shipBuilder_itemport_17)

    shipBuilder_itemport_18.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_18 = save_or_locate(shipBuilder_itemport_18)

    shipBuilder_itemport_19.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_19 = save_or_locate(shipBuilder_itemport_19)

    shipBuilder_itemport_20.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_20 = save_or_locate(shipBuilder_itemport_20)

    shipBuilder_itemport_21.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_21 = save_or_locate(shipBuilder_itemport_21)

    shipBuilder_itemport_22.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_22 = save_or_locate(shipBuilder_itemport_22)

    shipBuilder_itemport_23.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_23 = save_or_locate(shipBuilder_itemport_23)

    shipBuilder_itemport_24.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_24 = save_or_locate(shipBuilder_itemport_24)

    shipBuilder_itemport_25.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_25 = save_or_locate(shipBuilder_itemport_25)

    shipBuilder_itemport_26.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_26 = save_or_locate(shipBuilder_itemport_26)

    shipBuilder_itemport_27.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_27 = save_or_locate(shipBuilder_itemport_27)

    shipBuilder_itemport_28.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_28 = save_or_locate(shipBuilder_itemport_28)

    shipBuilder_itemport_29.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_29 = save_or_locate(shipBuilder_itemport_29)

    shipBuilder_itemport_30.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_30 = save_or_locate(shipBuilder_itemport_30)

    shipBuilder_itemport_31.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_31 = save_or_locate(shipBuilder_itemport_31)

    shipBuilder_itemport_32.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_32 = save_or_locate(shipBuilder_itemport_32)

    shipBuilder_itemport_33.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_33 = save_or_locate(shipBuilder_itemport_33)

    shipBuilder_itemport_34.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_34 = save_or_locate(shipBuilder_itemport_34)

    shipBuilder_itemport_35.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_35 = save_or_locate(shipBuilder_itemport_35)

    shipBuilder_itemport_36.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_36 = save_or_locate(shipBuilder_itemport_36)

    shipBuilder_itemport_37.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_37 = save_or_locate(shipBuilder_itemport_37)

    shipBuilder_itemport_38.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_38 = save_or_locate(shipBuilder_itemport_38)

    shipBuilder_itemport_39.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_39 = save_or_locate(shipBuilder_itemport_39)

    shipBuilder_itemport_40.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_40 = save_or_locate(shipBuilder_itemport_40)

    shipBuilder_itemport_41.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_41 = save_or_locate(shipBuilder_itemport_41)

    shipBuilder_itemport_42.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_42 = save_or_locate(shipBuilder_itemport_42)

    shipBuilder_itemport_43.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_43 = save_or_locate(shipBuilder_itemport_43)

    shipBuilder_itemport_44.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_44 = save_or_locate(shipBuilder_itemport_44)

    shipBuilder_itemport_45.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_45 = save_or_locate(shipBuilder_itemport_45)

    shipBuilder_itemport_46.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_46 = save_or_locate(shipBuilder_itemport_46)

    shipBuilder_itemport_47.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_47 = save_or_locate(shipBuilder_itemport_47)

    shipBuilder_itemport_48.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_48 = save_or_locate(shipBuilder_itemport_48)

    shipBuilder_itemport_49.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_49 = save_or_locate(shipBuilder_itemport_49)

    shipBuilder_itemport_50.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_50 = save_or_locate(shipBuilder_itemport_50)

    shipBuilder_itemport_51.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_51 = save_or_locate(shipBuilder_itemport_51)

    shipBuilder_itemport_52.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_52 = save_or_locate(shipBuilder_itemport_52)

    shipBuilder_itemport_53.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_53 = save_or_locate(shipBuilder_itemport_53)

    shipBuilder_itemport_54.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_54 = save_or_locate(shipBuilder_itemport_54)

    shipBuilder_itemport_55.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_55 = save_or_locate(shipBuilder_itemport_55)

    shipBuilder_itemport_56.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_56 = save_or_locate(shipBuilder_itemport_56)

    shipBuilder_itemport_57.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_57 = save_or_locate(shipBuilder_itemport_57)

    shipBuilder_itemport_58.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_58 = save_or_locate(shipBuilder_itemport_58)

    shipBuilder_itemport_59.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_59 = save_or_locate(shipBuilder_itemport_59)

    shipBuilder_itemport_60.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_60 = save_or_locate(shipBuilder_itemport_60)

    shipBuilder_itemport_61.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_61 = save_or_locate(shipBuilder_itemport_61)

    shipBuilder_itemport_62.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_62 = save_or_locate(shipBuilder_itemport_62)

    shipBuilder_itemport_63.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_63 = save_or_locate(shipBuilder_itemport_63)

    shipBuilder_itemport_64.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_64 = save_or_locate(shipBuilder_itemport_64)

    shipBuilder_itemport_65.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_65 = save_or_locate(shipBuilder_itemport_65)

    shipBuilder_itemport_66.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_66 = save_or_locate(shipBuilder_itemport_66)

    shipBuilder_itemport_67.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_67 = save_or_locate(shipBuilder_itemport_67)

    shipBuilder_itemport_68.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_68 = save_or_locate(shipBuilder_itemport_68)

    shipBuilder_itemport_69.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_69 = save_or_locate(shipBuilder_itemport_69)

    shipBuilder_itemport_70.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_70 = save_or_locate(shipBuilder_itemport_70)

    shipBuilder_itemport_71.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_71 = save_or_locate(shipBuilder_itemport_71)

    shipBuilder_itemport_72.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_72 = save_or_locate(shipBuilder_itemport_72)

    shipBuilder_itemport_73.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_73 = save_or_locate(shipBuilder_itemport_73)

    shipBuilder_itemport_74.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_74 = save_or_locate(shipBuilder_itemport_74)

    shipBuilder_itemport_75.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_75 = save_or_locate(shipBuilder_itemport_75)

    shipBuilder_itemport_76.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_76 = save_or_locate(shipBuilder_itemport_76)

    shipBuilder_itemport_77.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_77 = save_or_locate(shipBuilder_itemport_77)

    shipBuilder_itemport_78.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_78 = save_or_locate(shipBuilder_itemport_78)

    shipBuilder_itemport_79.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_79 = save_or_locate(shipBuilder_itemport_79)

    shipBuilder_itemport_80.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_80 = save_or_locate(shipBuilder_itemport_80)

    shipBuilder_itemport_81.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_81 = save_or_locate(shipBuilder_itemport_81)

    shipBuilder_itemport_82.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_82 = save_or_locate(shipBuilder_itemport_82)

    shipBuilder_itemport_83.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_83 = save_or_locate(shipBuilder_itemport_83)

    shipBuilder_itemport_84.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_84 = save_or_locate(shipBuilder_itemport_84)

    shipBuilder_itemport_85.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_85 = save_or_locate(shipBuilder_itemport_85)

    shipBuilder_itemport_86.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_86 = save_or_locate(shipBuilder_itemport_86)

    shipBuilder_itemport_87.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_87 = save_or_locate(shipBuilder_itemport_87)

    shipBuilder_itemport_88.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_88 = save_or_locate(shipBuilder_itemport_88)

    shipBuilder_itemport_89.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_89 = save_or_locate(shipBuilder_itemport_89)

    shipBuilder_itemport_90.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_90 = save_or_locate(shipBuilder_itemport_90)

    shipBuilder_itemport_91.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_91 = save_or_locate(shipBuilder_itemport_91)

    shipBuilder_itemport_92.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_92 = save_or_locate(shipBuilder_itemport_92)

    shipBuilder_itemport_93.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_93 = save_or_locate(shipBuilder_itemport_93)

    shipBuilder_itemport_94.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_94 = save_or_locate(shipBuilder_itemport_94)

    shipBuilder_itemport_95.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_95 = save_or_locate(shipBuilder_itemport_95)

    shipBuilder_itemport_96.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_96 = save_or_locate(shipBuilder_itemport_96)

    shipBuilder_itemport_97.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_97 = save_or_locate(shipBuilder_itemport_97)

    shipBuilder_itemport_98.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_98 = save_or_locate(shipBuilder_itemport_98)

    shipBuilder_itemport_99.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_99 = save_or_locate(shipBuilder_itemport_99)

    shipBuilder_itemport_100.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_100 = save_or_locate(shipBuilder_itemport_100)

    shipBuilder_itemport_101.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_101 = save_or_locate(shipBuilder_itemport_101)

    shipBuilder_itemport_102.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_102 = save_or_locate(shipBuilder_itemport_102)

    shipBuilder_itemport_103.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_103 = save_or_locate(shipBuilder_itemport_103)

    shipBuilder_itemport_104.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_104 = save_or_locate(shipBuilder_itemport_104)

    shipBuilder_itemport_105.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_105 = save_or_locate(shipBuilder_itemport_105)

    shipBuilder_itemport_106.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_106 = save_or_locate(shipBuilder_itemport_106)

    shipBuilder_itemport_107.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_107 = save_or_locate(shipBuilder_itemport_107)

    shipBuilder_itemport_108.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_108 = save_or_locate(shipBuilder_itemport_108)

    shipBuilder_itemport_109.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_109 = save_or_locate(shipBuilder_itemport_109)

    shipBuilder_itemport_110.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_110 = save_or_locate(shipBuilder_itemport_110)

    shipBuilder_itemport_111.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_111 = save_or_locate(shipBuilder_itemport_111)

    shipBuilder_itemport_112.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_112 = save_or_locate(shipBuilder_itemport_112)

    shipBuilder_itemport_113.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_113 = save_or_locate(shipBuilder_itemport_113)

    shipBuilder_itemport_114.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_114 = save_or_locate(shipBuilder_itemport_114)

    shipBuilder_itemport_115.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_115 = save_or_locate(shipBuilder_itemport_115)

    shipBuilder_itemport_116.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_116 = save_or_locate(shipBuilder_itemport_116)

    shipBuilder_itemport_117.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_117 = save_or_locate(shipBuilder_itemport_117)

    shipBuilder_itemport_118.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_118 = save_or_locate(shipBuilder_itemport_118)

    shipBuilder_itemport_119.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_119 = save_or_locate(shipBuilder_itemport_119)

    shipBuilder_itemport_120.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_120 = save_or_locate(shipBuilder_itemport_120)

    shipBuilder_itemport_121.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_121 = save_or_locate(shipBuilder_itemport_121)

    shipBuilder_itemport_122.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_122 = save_or_locate(shipBuilder_itemport_122)

    shipBuilder_itemport_123.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_123 = save_or_locate(shipBuilder_itemport_123)

    shipBuilder_itemport_124.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_124 = save_or_locate(shipBuilder_itemport_124)

    shipBuilder_itemport_125.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_125 = save_or_locate(shipBuilder_itemport_125)

    shipBuilder_itemport_126.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_126 = save_or_locate(shipBuilder_itemport_126)

    shipBuilder_itemport_127.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_127 = save_or_locate(shipBuilder_itemport_127)

    shipBuilder_itemport_128.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_128 = save_or_locate(shipBuilder_itemport_128)

    shipBuilder_itemport_129.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_129 = save_or_locate(shipBuilder_itemport_129)

    shipBuilder_itemport_130.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_130 = save_or_locate(shipBuilder_itemport_130)

    shipBuilder_itemport_131.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_131 = save_or_locate(shipBuilder_itemport_131)

    shipBuilder_itemport_132.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_132 = save_or_locate(shipBuilder_itemport_132)

    shipBuilder_itemport_133.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_133 = save_or_locate(shipBuilder_itemport_133)

    shipBuilder_itemport_134.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_134 = save_or_locate(shipBuilder_itemport_134)

    shipBuilder_itemport_135.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_135 = save_or_locate(shipBuilder_itemport_135)

    shipBuilder_itemport_136.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_136 = save_or_locate(shipBuilder_itemport_136)

    shipBuilder_itemport_137.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_137 = save_or_locate(shipBuilder_itemport_137)

    shipBuilder_itemport_138.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_138 = save_or_locate(shipBuilder_itemport_138)

    shipBuilder_itemport_139.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_139 = save_or_locate(shipBuilder_itemport_139)

    shipBuilder_itemport_140.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_140 = save_or_locate(shipBuilder_itemport_140)

    shipBuilder_itemport_141.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_141 = save_or_locate(shipBuilder_itemport_141)

    shipBuilder_itemport_142.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_142 = save_or_locate(shipBuilder_itemport_142)

    shipBuilder_itemport_143.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_143 = save_or_locate(shipBuilder_itemport_143)

    shipBuilder_itemport_144.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_144 = save_or_locate(shipBuilder_itemport_144)

    shipBuilder_itemport_145.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_145 = save_or_locate(shipBuilder_itemport_145)

    shipBuilder_itemport_146.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_146 = save_or_locate(shipBuilder_itemport_146)

    shipBuilder_itemport_147.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_147 = save_or_locate(shipBuilder_itemport_147)

    shipBuilder_itemport_148.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_148 = save_or_locate(shipBuilder_itemport_148)

    shipBuilder_itemport_149.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_149 = save_or_locate(shipBuilder_itemport_149)

    shipBuilder_itemport_150.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_150 = save_or_locate(shipBuilder_itemport_150)

    shipBuilder_itemport_151.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_151 = save_or_locate(shipBuilder_itemport_151)

    shipBuilder_itemport_152.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_152 = save_or_locate(shipBuilder_itemport_152)

    shipBuilder_itemport_153.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_153 = save_or_locate(shipBuilder_itemport_153)

    shipBuilder_itemport_154.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_154 = save_or_locate(shipBuilder_itemport_154)

    shipBuilder_itemport_155.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_155 = save_or_locate(shipBuilder_itemport_155)

    shipBuilder_itemport_156.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_156 = save_or_locate(shipBuilder_itemport_156)

    shipBuilder_itemport_157.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_157 = save_or_locate(shipBuilder_itemport_157)

    shipBuilder_itemport_158.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_158 = save_or_locate(shipBuilder_itemport_158)

    shipBuilder_itemport_159.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_159 = save_or_locate(shipBuilder_itemport_159)

    shipBuilder_itemport_160.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_160 = save_or_locate(shipBuilder_itemport_160)

    shipBuilder_itemport_161.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_161 = save_or_locate(shipBuilder_itemport_161)

    shipBuilder_itemport_162.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_162 = save_or_locate(shipBuilder_itemport_162)

    shipBuilder_itemport_163.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_163 = save_or_locate(shipBuilder_itemport_163)

    shipBuilder_itemport_164.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_164 = save_or_locate(shipBuilder_itemport_164)

    shipBuilder_itemport_165.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_165 = save_or_locate(shipBuilder_itemport_165)

    shipBuilder_itemport_166.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_166 = save_or_locate(shipBuilder_itemport_166)

    shipBuilder_itemport_167.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_167 = save_or_locate(shipBuilder_itemport_167)

    shipBuilder_itemport_168.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_168 = save_or_locate(shipBuilder_itemport_168)

    shipBuilder_itemport_169.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_169 = save_or_locate(shipBuilder_itemport_169)

    shipBuilder_itemport_170.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_170 = save_or_locate(shipBuilder_itemport_170)

    shipBuilder_itemport_171.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_171 = save_or_locate(shipBuilder_itemport_171)

    shipBuilder_itemport_172.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_172 = save_or_locate(shipBuilder_itemport_172)

    shipBuilder_itemport_173.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_173 = save_or_locate(shipBuilder_itemport_173)

    shipBuilder_itemport_174.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_174 = save_or_locate(shipBuilder_itemport_174)

    shipBuilder_itemport_175.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_175 = save_or_locate(shipBuilder_itemport_175)

    shipBuilder_itemport_176.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_176 = save_or_locate(shipBuilder_itemport_176)

    shipBuilder_itemport_177.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_177 = save_or_locate(shipBuilder_itemport_177)

    shipBuilder_itemport_178.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_178 = save_or_locate(shipBuilder_itemport_178)

    shipBuilder_itemport_179.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_179 = save_or_locate(shipBuilder_itemport_179)

    shipBuilder_itemport_180.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_180 = save_or_locate(shipBuilder_itemport_180)

    shipBuilder_itemport_181.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_181 = save_or_locate(shipBuilder_itemport_181)

    shipBuilder_itemport_182.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_182 = save_or_locate(shipBuilder_itemport_182)

    shipBuilder_itemport_183.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_183 = save_or_locate(shipBuilder_itemport_183)

    shipBuilder_itemport_184.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_184 = save_or_locate(shipBuilder_itemport_184)

    shipBuilder_itemport_185.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_185 = save_or_locate(shipBuilder_itemport_185)

    shipBuilder_itemport_186.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_186 = save_or_locate(shipBuilder_itemport_186)

    shipBuilder_itemport_187.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_187 = save_or_locate(shipBuilder_itemport_187)

    shipBuilder_itemport_188.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_188 = save_or_locate(shipBuilder_itemport_188)

    shipBuilder_itemport_189.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_189 = save_or_locate(shipBuilder_itemport_189)

    shipBuilder_itemport_190.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_190 = save_or_locate(shipBuilder_itemport_190)

    shipBuilder_itemport_191.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_191 = save_or_locate(shipBuilder_itemport_191)

    shipBuilder_itemport_192.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_192 = save_or_locate(shipBuilder_itemport_192)

    shipBuilder_itemport_193.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_193 = save_or_locate(shipBuilder_itemport_193)

    shipBuilder_itemport_194.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_194 = save_or_locate(shipBuilder_itemport_194)

    shipBuilder_itemport_195.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_195 = save_or_locate(shipBuilder_itemport_195)

    shipBuilder_itemport_196.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_196 = save_or_locate(shipBuilder_itemport_196)

    shipBuilder_itemport_197.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_197 = save_or_locate(shipBuilder_itemport_197)

    shipBuilder_itemport_198.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_198 = save_or_locate(shipBuilder_itemport_198)

    shipBuilder_itemport_199.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_199 = save_or_locate(shipBuilder_itemport_199)

    shipBuilder_itemport_200.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_200 = save_or_locate(shipBuilder_itemport_200)

    shipBuilder_itemport_201.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_201 = save_or_locate(shipBuilder_itemport_201)

    shipBuilder_itemport_202.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_202 = save_or_locate(shipBuilder_itemport_202)

    shipBuilder_itemport_203.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_203 = save_or_locate(shipBuilder_itemport_203)

    shipBuilder_itemport_204.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_204 = save_or_locate(shipBuilder_itemport_204)

    shipBuilder_itemport_205.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_205 = save_or_locate(shipBuilder_itemport_205)

    shipBuilder_itemport_206.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_206 = save_or_locate(shipBuilder_itemport_206)

    shipBuilder_itemport_207.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_207 = save_or_locate(shipBuilder_itemport_207)

    shipBuilder_itemport_208.parentVehicle = shipBuilder_vehicle_13
    shipBuilder_itemport_208 = save_or_locate(shipBuilder_itemport_208)

    shipBuilder_itemport_209.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_209 = save_or_locate(shipBuilder_itemport_209)

    shipBuilder_itemport_210.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_210 = save_or_locate(shipBuilder_itemport_210)

    shipBuilder_itemport_211.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_211 = save_or_locate(shipBuilder_itemport_211)

    shipBuilder_itemport_212.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_212 = save_or_locate(shipBuilder_itemport_212)

    shipBuilder_itemport_213.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_213 = save_or_locate(shipBuilder_itemport_213)

    shipBuilder_itemport_214.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_214 = save_or_locate(shipBuilder_itemport_214)

    shipBuilder_itemport_215.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_215 = save_or_locate(shipBuilder_itemport_215)

    shipBuilder_itemport_216.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_216 = save_or_locate(shipBuilder_itemport_216)

    shipBuilder_itemport_217.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_217 = save_or_locate(shipBuilder_itemport_217)

    shipBuilder_itemport_218.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_218 = save_or_locate(shipBuilder_itemport_218)

    shipBuilder_itemport_219.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_219 = save_or_locate(shipBuilder_itemport_219)

    shipBuilder_itemport_220.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_220 = save_or_locate(shipBuilder_itemport_220)

    shipBuilder_itemport_221.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_221 = save_or_locate(shipBuilder_itemport_221)

    shipBuilder_itemport_222.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_222 = save_or_locate(shipBuilder_itemport_222)

    shipBuilder_itemport_223.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_223 = save_or_locate(shipBuilder_itemport_223)

    shipBuilder_itemport_224.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_224 = save_or_locate(shipBuilder_itemport_224)

    shipBuilder_itemport_225.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_225 = save_or_locate(shipBuilder_itemport_225)

    shipBuilder_itemport_226.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_226 = save_or_locate(shipBuilder_itemport_226)

    shipBuilder_itemport_227.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_227 = save_or_locate(shipBuilder_itemport_227)

    shipBuilder_itemport_228.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_228 = save_or_locate(shipBuilder_itemport_228)

    shipBuilder_itemport_229.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_229 = save_or_locate(shipBuilder_itemport_229)

    shipBuilder_itemport_230.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_230 = save_or_locate(shipBuilder_itemport_230)

    shipBuilder_itemport_231.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_231 = save_or_locate(shipBuilder_itemport_231)

    shipBuilder_itemport_232.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_232 = save_or_locate(shipBuilder_itemport_232)

    shipBuilder_itemport_233.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_233 = save_or_locate(shipBuilder_itemport_233)

    shipBuilder_itemport_234.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_234 = save_or_locate(shipBuilder_itemport_234)

    shipBuilder_itemport_235.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_235 = save_or_locate(shipBuilder_itemport_235)

    shipBuilder_itemport_236.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_236 = save_or_locate(shipBuilder_itemport_236)

    shipBuilder_itemport_237.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_237 = save_or_locate(shipBuilder_itemport_237)

    shipBuilder_itemport_238.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_238 = save_or_locate(shipBuilder_itemport_238)

    shipBuilder_itemport_239.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_239 = save_or_locate(shipBuilder_itemport_239)

    shipBuilder_itemport_240.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_240 = save_or_locate(shipBuilder_itemport_240)

    shipBuilder_itemport_241.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_241 = save_or_locate(shipBuilder_itemport_241)

    shipBuilder_itemport_242.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_242 = save_or_locate(shipBuilder_itemport_242)

    shipBuilder_itemport_243.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_243 = save_or_locate(shipBuilder_itemport_243)

    shipBuilder_itemport_244.parentVehicle = shipBuilder_vehicle_14
    shipBuilder_itemport_244 = save_or_locate(shipBuilder_itemport_244)







    shipBuilder_itemport_251.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_251 = save_or_locate(shipBuilder_itemport_251)

    shipBuilder_itemport_252.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_252 = save_or_locate(shipBuilder_itemport_252)

    shipBuilder_itemport_253.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_253 = save_or_locate(shipBuilder_itemport_253)

    shipBuilder_itemport_254.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_254 = save_or_locate(shipBuilder_itemport_254)

    shipBuilder_itemport_255.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_255 = save_or_locate(shipBuilder_itemport_255)

    shipBuilder_itemport_256.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_256 = save_or_locate(shipBuilder_itemport_256)

    shipBuilder_itemport_257.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_257 = save_or_locate(shipBuilder_itemport_257)

    shipBuilder_itemport_258.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_258 = save_or_locate(shipBuilder_itemport_258)

    shipBuilder_itemport_259.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_259 = save_or_locate(shipBuilder_itemport_259)

    shipBuilder_itemport_260.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_260 = save_or_locate(shipBuilder_itemport_260)

    shipBuilder_itemport_261.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_261 = save_or_locate(shipBuilder_itemport_261)

    shipBuilder_itemport_262.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_262 = save_or_locate(shipBuilder_itemport_262)

    shipBuilder_itemport_263.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_263 = save_or_locate(shipBuilder_itemport_263)

    shipBuilder_itemport_264.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_264 = save_or_locate(shipBuilder_itemport_264)

    shipBuilder_itemport_265.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_265 = save_or_locate(shipBuilder_itemport_265)

    shipBuilder_itemport_266.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_266 = save_or_locate(shipBuilder_itemport_266)

    shipBuilder_itemport_267.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_267 = save_or_locate(shipBuilder_itemport_267)

    shipBuilder_itemport_268.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_268 = save_or_locate(shipBuilder_itemport_268)

    shipBuilder_itemport_269.parentVehicle = shipBuilder_vehicle_15
    shipBuilder_itemport_269 = save_or_locate(shipBuilder_itemport_269)

    shipBuilder_itemport_270.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_270 = save_or_locate(shipBuilder_itemport_270)

    shipBuilder_itemport_271.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_271 = save_or_locate(shipBuilder_itemport_271)

    shipBuilder_itemport_272.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_272 = save_or_locate(shipBuilder_itemport_272)

    shipBuilder_itemport_273.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_273 = save_or_locate(shipBuilder_itemport_273)

    shipBuilder_itemport_274.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_274 = save_or_locate(shipBuilder_itemport_274)

    shipBuilder_itemport_275.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_275 = save_or_locate(shipBuilder_itemport_275)

    shipBuilder_itemport_276.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_276 = save_or_locate(shipBuilder_itemport_276)

    shipBuilder_itemport_277.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_277 = save_or_locate(shipBuilder_itemport_277)

    shipBuilder_itemport_278.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_278 = save_or_locate(shipBuilder_itemport_278)

    shipBuilder_itemport_279.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_279 = save_or_locate(shipBuilder_itemport_279)

    shipBuilder_itemport_280.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_280 = save_or_locate(shipBuilder_itemport_280)

    shipBuilder_itemport_281.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_281 = save_or_locate(shipBuilder_itemport_281)

    shipBuilder_itemport_282.parentVehicle = shipBuilder_vehicle_16
    shipBuilder_itemport_282 = save_or_locate(shipBuilder_itemport_282)

    shipBuilder_itemport_283.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_283 = save_or_locate(shipBuilder_itemport_283)

    shipBuilder_itemport_284.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_284 = save_or_locate(shipBuilder_itemport_284)

    shipBuilder_itemport_285.parentVehicle = shipBuilder_vehicle_17
    shipBuilder_itemport_285 = save_or_locate(shipBuilder_itemport_285)

    #Re-processing model: VehicleCategory

    #Re-processing model: Vehicle

    #Re-processing model: HardpointTag

    #Re-processing model: VariantItem

    #Re-processing model: Variant

    #Re-processing model: GameUpdate

    #Re-processing model: GameUpdateChange

    #Re-processing model: Hangar

    #Re-processing model: MigrationHistory

    #Re-processing model: LogEntry

    #Re-processing model: Item

    #Re-processing model: CargoModData

    #Re-processing model: Hardpoint

    #Re-processing model: BuildHardpoint

    #Re-processing model: BuildEngineMod

    #Re-processing model: BuildHullMod

    #Re-processing model: Build

    #Re-processing model: LocalizedDescriptionVehicle

    #Re-processing model: LocalizedDescriptionVehicleItem

    #Re-processing model: VehicleItemParams

    #Re-processing model: PipeState

    #Re-processing model: VehicleItemPipe

    #Re-processing model: VehicleItemPower

    #Re-processing model: VehicleItemHeat

