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



    #Processing model: Group

    from django.contrib.auth.models import Group


    #Processing model: User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = u'pbkdf2_sha256$10000$xnOm0fg1ulnF$gHGF5Ap8epEJ3gqXcnKUejyOAqA5qJP+kPePkx7tYrw='
    auth_user_1.last_login = datetime.datetime(2013, 9, 13, 1, 21, 54)
    auth_user_1.is_superuser = True
    auth_user_1.username = u'agathorn'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'jwvanderbeck@gmail.com'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = datetime.datetime(2013, 9, 7, 3, 2, 42)
    auth_user_1 = importer.save_or_locate(auth_user_1)

    auth_user_2 = User()
    auth_user_2.password = u'pbkdf2_sha256$10000$baYmWrdhPmTU$mWpBQdWtwy+nMCcvKXNm+DbCQUCr/oivoBvGSKLGzD4='
    auth_user_2.last_login = datetime.datetime(2013, 9, 7, 4, 23, 59)
    auth_user_2.is_superuser = False
    auth_user_2.username = u'danredda'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.date_joined = datetime.datetime(2013, 9, 7, 4, 23, 58)
    auth_user_2 = importer.save_or_locate(auth_user_2)

    auth_user_3 = User()
    auth_user_3.password = u'pbkdf2_sha256$10000$fxtMeqhGed19$0FNJR6d9f3gOxDK2mVVFcvc7AuCP6frrjWadxCnY+Fk='
    auth_user_3.last_login = datetime.datetime(2013, 9, 12, 21, 44, 49)
    auth_user_3.is_superuser = False
    auth_user_3.username = u'erickpasta'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.is_staff = False
    auth_user_3.is_active = True
    auth_user_3.date_joined = datetime.datetime(2013, 9, 7, 4, 26, 28)
    auth_user_3 = importer.save_or_locate(auth_user_3)

    auth_user_4 = User()
    auth_user_4.password = u'pbkdf2_sha256$10000$Tg7nYHkLz5Ko$Jkxq4xDaDxCeDPFLAyNArO4E2Pb5qRPUiKWjemqbWUE='
    auth_user_4.last_login = datetime.datetime(2013, 9, 7, 10, 59, 30)
    auth_user_4.is_superuser = False
    auth_user_4.username = u'ColMustang'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.is_staff = False
    auth_user_4.is_active = True
    auth_user_4.date_joined = datetime.datetime(2013, 9, 7, 10, 59, 30)
    auth_user_4 = importer.save_or_locate(auth_user_4)

    auth_user_5 = User()
    auth_user_5.password = u'pbkdf2_sha256$10000$mcqXny0QsvGH$aPoFTEMTtMomVIAq1t9FroRopIBGOAwj1a3gqr919KY='
    auth_user_5.last_login = datetime.datetime(2013, 9, 7, 11, 8, 32)
    auth_user_5.is_superuser = False
    auth_user_5.username = u'xrail'
    auth_user_5.first_name = u''
    auth_user_5.last_name = u''
    auth_user_5.email = u''
    auth_user_5.is_staff = False
    auth_user_5.is_active = True
    auth_user_5.date_joined = datetime.datetime(2013, 9, 7, 11, 8, 32)
    auth_user_5 = importer.save_or_locate(auth_user_5)

    auth_user_6 = User()
    auth_user_6.password = u'pbkdf2_sha256$10000$kEPUBxia8o38$l9FhgLzaOcr6XO4q8hTbRWDQWkVqq+wVFo8QVppq7u8='
    auth_user_6.last_login = datetime.datetime(2013, 9, 7, 14, 21, 42)
    auth_user_6.is_superuser = False
    auth_user_6.username = u'arioch'
    auth_user_6.first_name = u''
    auth_user_6.last_name = u''
    auth_user_6.email = u''
    auth_user_6.is_staff = False
    auth_user_6.is_active = True
    auth_user_6.date_joined = datetime.datetime(2013, 9, 7, 14, 21, 42)
    auth_user_6 = importer.save_or_locate(auth_user_6)

    auth_user_7 = User()
    auth_user_7.password = u'pbkdf2_sha256$10000$R2GyhSf24OKb$PN/hS+INCZ1rlwXXIQRYh8+efA/EEpST48rW3ad7FQ4='
    auth_user_7.last_login = datetime.datetime(2013, 9, 13, 15, 14, 53)
    auth_user_7.is_superuser = False
    auth_user_7.username = u'Damo'
    auth_user_7.first_name = u''
    auth_user_7.last_name = u''
    auth_user_7.email = u''
    auth_user_7.is_staff = False
    auth_user_7.is_active = True
    auth_user_7.date_joined = datetime.datetime(2013, 9, 7, 14, 59, 45)
    auth_user_7 = importer.save_or_locate(auth_user_7)

    auth_user_8 = User()
    auth_user_8.password = u'pbkdf2_sha256$10000$1RTc7oYxnxXa$alwqSm1bSoN4TtwpiTtLIUo09MbMOGodSl8dFDobh/U='
    auth_user_8.last_login = datetime.datetime(2013, 9, 7, 19, 11, 47)
    auth_user_8.is_superuser = False
    auth_user_8.username = u'Anon6_Wolfie'
    auth_user_8.first_name = u''
    auth_user_8.last_name = u''
    auth_user_8.email = u''
    auth_user_8.is_staff = False
    auth_user_8.is_active = True
    auth_user_8.date_joined = datetime.datetime(2013, 9, 7, 19, 11, 47)
    auth_user_8 = importer.save_or_locate(auth_user_8)

    auth_user_9 = User()
    auth_user_9.password = u'pbkdf2_sha256$10000$a0kzXkLoBUQG$UDJ4Az8lhkHIWrcRkp2ixfzMt1j8C8LLRmi4W0devPc='
    auth_user_9.last_login = datetime.datetime(2013, 9, 7, 19, 46, 11)
    auth_user_9.is_superuser = False
    auth_user_9.username = u'Raven'
    auth_user_9.first_name = u''
    auth_user_9.last_name = u''
    auth_user_9.email = u''
    auth_user_9.is_staff = False
    auth_user_9.is_active = True
    auth_user_9.date_joined = datetime.datetime(2013, 9, 7, 19, 46, 11)
    auth_user_9 = importer.save_or_locate(auth_user_9)

    auth_user_10 = User()
    auth_user_10.password = u'pbkdf2_sha256$10000$jlzKCNs7917B$hBn1bzjeiq6t/MeE8Qe9iSV0NL7e3OQNGQkE9e8QpOc='
    auth_user_10.last_login = datetime.datetime(2013, 9, 7, 20, 7, 24)
    auth_user_10.is_superuser = False
    auth_user_10.username = u'Kafelnikov'
    auth_user_10.first_name = u''
    auth_user_10.last_name = u''
    auth_user_10.email = u''
    auth_user_10.is_staff = False
    auth_user_10.is_active = True
    auth_user_10.date_joined = datetime.datetime(2013, 9, 7, 20, 7, 24)
    auth_user_10 = importer.save_or_locate(auth_user_10)

    auth_user_11 = User()
    auth_user_11.password = u'pbkdf2_sha256$10000$OsrUmoUXladl$qBXaUxAwTw+l1Noi5Tm9kDMQ+AKgiTSvwYdrtHjoDzY='
    auth_user_11.last_login = datetime.datetime(2013, 9, 8, 21, 23, 45)
    auth_user_11.is_superuser = False
    auth_user_11.username = u'Villaovi'
    auth_user_11.first_name = u''
    auth_user_11.last_name = u''
    auth_user_11.email = u''
    auth_user_11.is_staff = False
    auth_user_11.is_active = True
    auth_user_11.date_joined = datetime.datetime(2013, 9, 8, 21, 23, 45)
    auth_user_11 = importer.save_or_locate(auth_user_11)

    auth_user_12 = User()
    auth_user_12.password = u'pbkdf2_sha256$10000$uVD9wFG42PNH$2mUMSlQG35j8RN62g/X9d3QNM9anHGYVLtoR16LIMc0='
    auth_user_12.last_login = datetime.datetime(2013, 9, 8, 23, 57, 30)
    auth_user_12.is_superuser = False
    auth_user_12.username = u'moofie'
    auth_user_12.first_name = u''
    auth_user_12.last_name = u''
    auth_user_12.email = u''
    auth_user_12.is_staff = False
    auth_user_12.is_active = True
    auth_user_12.date_joined = datetime.datetime(2013, 9, 8, 23, 57, 30)
    auth_user_12 = importer.save_or_locate(auth_user_12)

    auth_user_13 = User()
    auth_user_13.password = u'pbkdf2_sha256$10000$dxI6v3sFCmNb$7x4MsoGWm25sIAFiA5jJJmgjDVq4KWZC0WgR/K1rvic='
    auth_user_13.last_login = datetime.datetime(2013, 9, 9, 2, 53, 13)
    auth_user_13.is_superuser = False
    auth_user_13.username = u'max thorn'
    auth_user_13.first_name = u''
    auth_user_13.last_name = u''
    auth_user_13.email = u''
    auth_user_13.is_staff = False
    auth_user_13.is_active = True
    auth_user_13.date_joined = datetime.datetime(2013, 9, 9, 2, 53, 13)
    auth_user_13 = importer.save_or_locate(auth_user_13)

    auth_user_14 = User()
    auth_user_14.password = u'pbkdf2_sha256$10000$PoAtlc2o7P8l$o5p4G3Co0a0iZU4/p19a298UDZKvMjtEfGTENtUNkrk='
    auth_user_14.last_login = datetime.datetime(2013, 9, 9, 23, 49, 27)
    auth_user_14.is_superuser = False
    auth_user_14.username = u'Menthro05'
    auth_user_14.first_name = u''
    auth_user_14.last_name = u''
    auth_user_14.email = u''
    auth_user_14.is_staff = False
    auth_user_14.is_active = True
    auth_user_14.date_joined = datetime.datetime(2013, 9, 9, 23, 49, 27)
    auth_user_14 = importer.save_or_locate(auth_user_14)

    auth_user_15 = User()
    auth_user_15.password = u'pbkdf2_sha256$10000$faNZAqNhNgON$1izpu6hwaULvj/Co+Y30Pl8w4FPADOyhJcDjXMcPE44='
    auth_user_15.last_login = datetime.datetime(2013, 9, 10, 0, 2, 9)
    auth_user_15.is_superuser = False
    auth_user_15.username = u'Phredco'
    auth_user_15.first_name = u''
    auth_user_15.last_name = u''
    auth_user_15.email = u''
    auth_user_15.is_staff = False
    auth_user_15.is_active = True
    auth_user_15.date_joined = datetime.datetime(2013, 9, 10, 0, 2, 9)
    auth_user_15 = importer.save_or_locate(auth_user_15)

    auth_user_16 = User()
    auth_user_16.password = u'pbkdf2_sha256$10000$DAxj3Hv8OySi$UU6wE5MbHuFdGe3hUhCSh5Pf+0DWJX+8Ct8RBSUfLpA='
    auth_user_16.last_login = datetime.datetime(2013, 9, 10, 2, 21, 52)
    auth_user_16.is_superuser = False
    auth_user_16.username = u'Di Tar'
    auth_user_16.first_name = u''
    auth_user_16.last_name = u''
    auth_user_16.email = u''
    auth_user_16.is_staff = False
    auth_user_16.is_active = True
    auth_user_16.date_joined = datetime.datetime(2013, 9, 10, 2, 21, 25)
    auth_user_16 = importer.save_or_locate(auth_user_16)

    auth_user_17 = User()
    auth_user_17.password = u'pbkdf2_sha256$10000$GGxu5wV5sQgN$YkkB3QI/IqFMpN/N/AX8Xr50ny5dmk3J7B4pjxyfxQM='
    auth_user_17.last_login = datetime.datetime(2013, 9, 10, 12, 55, 3)
    auth_user_17.is_superuser = False
    auth_user_17.username = u'mhe'
    auth_user_17.first_name = u''
    auth_user_17.last_name = u''
    auth_user_17.email = u''
    auth_user_17.is_staff = False
    auth_user_17.is_active = True
    auth_user_17.date_joined = datetime.datetime(2013, 9, 10, 12, 55, 3)
    auth_user_17 = importer.save_or_locate(auth_user_17)

    auth_user_18 = User()
    auth_user_18.password = u'pbkdf2_sha256$10000$oU9H0GRMEve2$p5vSK7n813H/9jAhTz6T2dIiqbfYeEh1qfy2zIcsOR8='
    auth_user_18.last_login = datetime.datetime(2013, 9, 11, 11, 0)
    auth_user_18.is_superuser = False
    auth_user_18.username = u'Siege'
    auth_user_18.first_name = u''
    auth_user_18.last_name = u''
    auth_user_18.email = u''
    auth_user_18.is_staff = False
    auth_user_18.is_active = True
    auth_user_18.date_joined = datetime.datetime(2013, 9, 11, 11, 0)
    auth_user_18 = importer.save_or_locate(auth_user_18)

    auth_user_19 = User()
    auth_user_19.password = u'pbkdf2_sha256$10000$bJYwxIeAMmIH$v4M3IPlyR3eg3PI3CyK6zuMZ22qBM/JLMEE9G/8QNAs='
    auth_user_19.last_login = datetime.datetime(2013, 9, 11, 15, 6, 28)
    auth_user_19.is_superuser = False
    auth_user_19.username = u'dbennette'
    auth_user_19.first_name = u''
    auth_user_19.last_name = u''
    auth_user_19.email = u''
    auth_user_19.is_staff = False
    auth_user_19.is_active = True
    auth_user_19.date_joined = datetime.datetime(2013, 9, 11, 15, 6, 28)
    auth_user_19 = importer.save_or_locate(auth_user_19)

    auth_user_20 = User()
    auth_user_20.password = u'pbkdf2_sha256$10000$1mPfPZdArnki$aEUod7bqSuBvWYXTMkkyYDCfQxf9vOXny+pwzTgY2OM='
    auth_user_20.last_login = datetime.datetime(2013, 9, 11, 23, 41, 51)
    auth_user_20.is_superuser = False
    auth_user_20.username = u'Cryptikality'
    auth_user_20.first_name = u''
    auth_user_20.last_name = u''
    auth_user_20.email = u''
    auth_user_20.is_staff = False
    auth_user_20.is_active = True
    auth_user_20.date_joined = datetime.datetime(2013, 9, 11, 23, 41, 51)
    auth_user_20 = importer.save_or_locate(auth_user_20)

    auth_user_21 = User()
    auth_user_21.password = u'pbkdf2_sha256$10000$Zo9up7LxNXKZ$Go3gmFwbjanSC7tQk5xIv4MGESZ62BraFnnkfFBLBRs='
    auth_user_21.last_login = datetime.datetime(2013, 9, 12, 14, 23, 19)
    auth_user_21.is_superuser = False
    auth_user_21.username = u'Bohbo'
    auth_user_21.first_name = u''
    auth_user_21.last_name = u''
    auth_user_21.email = u''
    auth_user_21.is_staff = False
    auth_user_21.is_active = True
    auth_user_21.date_joined = datetime.datetime(2013, 9, 12, 14, 23, 19)
    auth_user_21 = importer.save_or_locate(auth_user_21)

    auth_user_22 = User()
    auth_user_22.password = u'pbkdf2_sha256$10000$wtkpVdEfEtVk$laVcKM5G5nAOoC8xpC4kmzQz/6pQbkdzuAiQ0heZqFU='
    auth_user_22.last_login = datetime.datetime(2013, 9, 12, 20, 56, 41)
    auth_user_22.is_superuser = False
    auth_user_22.username = u'Athanasius'
    auth_user_22.first_name = u''
    auth_user_22.last_name = u''
    auth_user_22.email = u''
    auth_user_22.is_staff = False
    auth_user_22.is_active = True
    auth_user_22.date_joined = datetime.datetime(2013, 9, 12, 20, 56, 41)
    auth_user_22 = importer.save_or_locate(auth_user_22)

    auth_user_23 = User()
    auth_user_23.password = u'pbkdf2_sha256$10000$I2AhXEXdHfTK$y1wlXYzUEq4toLNDetTRSRXfc1mOsYa+4UCtrT8040E='
    auth_user_23.last_login = datetime.datetime(2013, 9, 12, 21, 10, 25)
    auth_user_23.is_superuser = False
    auth_user_23.username = u'Kean96'
    auth_user_23.first_name = u''
    auth_user_23.last_name = u''
    auth_user_23.email = u''
    auth_user_23.is_staff = False
    auth_user_23.is_active = True
    auth_user_23.date_joined = datetime.datetime(2013, 9, 12, 21, 10, 24)
    auth_user_23 = importer.save_or_locate(auth_user_23)

    auth_user_24 = User()
    auth_user_24.password = u'pbkdf2_sha256$10000$WKvGnyQXirxC$j6/sW9hOm79LXvUbS9RoUex4BIAvfeitHJ6iC+1R5/A='
    auth_user_24.last_login = datetime.datetime(2013, 9, 12, 21, 19, 41)
    auth_user_24.is_superuser = False
    auth_user_24.username = u'Silveryn1313'
    auth_user_24.first_name = u''
    auth_user_24.last_name = u''
    auth_user_24.email = u''
    auth_user_24.is_staff = False
    auth_user_24.is_active = True
    auth_user_24.date_joined = datetime.datetime(2013, 9, 12, 21, 19, 40)
    auth_user_24 = importer.save_or_locate(auth_user_24)

    auth_user_25 = User()
    auth_user_25.password = u'pbkdf2_sha256$10000$eAuQOR7fUAt7$k7xyNVDyEIWbHkb+EbPr79FcCbncDM0DjJzgbWUrNv0='
    auth_user_25.last_login = datetime.datetime(2013, 9, 12, 21, 23, 48)
    auth_user_25.is_superuser = False
    auth_user_25.username = u'Cyber556'
    auth_user_25.first_name = u''
    auth_user_25.last_name = u''
    auth_user_25.email = u''
    auth_user_25.is_staff = False
    auth_user_25.is_active = True
    auth_user_25.date_joined = datetime.datetime(2013, 9, 12, 21, 23, 48)
    auth_user_25 = importer.save_or_locate(auth_user_25)

    auth_user_26 = User()
    auth_user_26.password = u'pbkdf2_sha256$10000$JWp5EcMVdhjJ$55tASQ/5ND3nGbW/j5CShdvYye0k8e5h+0QuFuuBkXw='
    auth_user_26.last_login = datetime.datetime(2013, 9, 12, 21, 31, 10)
    auth_user_26.is_superuser = False
    auth_user_26.username = u'silvock'
    auth_user_26.first_name = u''
    auth_user_26.last_name = u''
    auth_user_26.email = u''
    auth_user_26.is_staff = False
    auth_user_26.is_active = True
    auth_user_26.date_joined = datetime.datetime(2013, 9, 12, 21, 31, 10)
    auth_user_26 = importer.save_or_locate(auth_user_26)

    auth_user_27 = User()
    auth_user_27.password = u'pbkdf2_sha256$10000$51hduLR3Riod$wokIbLB7DBt6ByGogr/23FjjKn9mZq3oUcfrs6gGrlA='
    auth_user_27.last_login = datetime.datetime(2013, 9, 12, 21, 43, 4)
    auth_user_27.is_superuser = False
    auth_user_27.username = u'DC5102916'
    auth_user_27.first_name = u''
    auth_user_27.last_name = u''
    auth_user_27.email = u''
    auth_user_27.is_staff = False
    auth_user_27.is_active = True
    auth_user_27.date_joined = datetime.datetime(2013, 9, 12, 21, 43, 4)
    auth_user_27 = importer.save_or_locate(auth_user_27)

    auth_user_28 = User()
    auth_user_28.password = u'pbkdf2_sha256$10000$5BrM3RRxrrdV$dDYgGSlhNCxmi4iCMC6Jp6+Heldxj8/jz/lDZvHvdho='
    auth_user_28.last_login = datetime.datetime(2013, 9, 12, 21, 51, 35)
    auth_user_28.is_superuser = False
    auth_user_28.username = u'pancakemaster808'
    auth_user_28.first_name = u''
    auth_user_28.last_name = u''
    auth_user_28.email = u''
    auth_user_28.is_staff = False
    auth_user_28.is_active = True
    auth_user_28.date_joined = datetime.datetime(2013, 9, 12, 21, 51, 35)
    auth_user_28 = importer.save_or_locate(auth_user_28)

    auth_user_29 = User()
    auth_user_29.password = u'pbkdf2_sha256$10000$dUB84mLRgKqJ$zLkzYa6RmPDtPW4oNsXlAjQXr0Ha11uwd8Dl01zCrRA='
    auth_user_29.last_login = datetime.datetime(2013, 9, 12, 22, 2, 2)
    auth_user_29.is_superuser = False
    auth_user_29.username = u'Stat8iS'
    auth_user_29.first_name = u''
    auth_user_29.last_name = u''
    auth_user_29.email = u''
    auth_user_29.is_staff = False
    auth_user_29.is_active = True
    auth_user_29.date_joined = datetime.datetime(2013, 9, 12, 22, 2, 1)
    auth_user_29 = importer.save_or_locate(auth_user_29)

    auth_user_30 = User()
    auth_user_30.password = u'pbkdf2_sha256$10000$PcmOkImIpN24$+oDDmldkrJkJi25EJbY/MyjXCJB3hE2ve78z23mrbSc='
    auth_user_30.last_login = datetime.datetime(2013, 9, 12, 22, 2, 8)
    auth_user_30.is_superuser = False
    auth_user_30.username = u'RutgerM'
    auth_user_30.first_name = u''
    auth_user_30.last_name = u''
    auth_user_30.email = u''
    auth_user_30.is_staff = False
    auth_user_30.is_active = True
    auth_user_30.date_joined = datetime.datetime(2013, 9, 12, 22, 2, 8)
    auth_user_30 = importer.save_or_locate(auth_user_30)

    auth_user_31 = User()
    auth_user_31.password = u'pbkdf2_sha256$10000$m3td1qxYqglD$hILXVztCihYfLb763SRE8GJgBn9y8VdiTHptkG1O4nY='
    auth_user_31.last_login = datetime.datetime(2013, 9, 12, 22, 4, 59)
    auth_user_31.is_superuser = False
    auth_user_31.username = u'kaelnovar'
    auth_user_31.first_name = u''
    auth_user_31.last_name = u''
    auth_user_31.email = u''
    auth_user_31.is_staff = False
    auth_user_31.is_active = True
    auth_user_31.date_joined = datetime.datetime(2013, 9, 12, 22, 4, 59)
    auth_user_31 = importer.save_or_locate(auth_user_31)

    auth_user_32 = User()
    auth_user_32.password = u'pbkdf2_sha256$10000$l4uFdA9ih2RF$8RGet8b4gAAAH214Dc2vzb4m6tqBa8MB8iNDaWpyxqY='
    auth_user_32.last_login = datetime.datetime(2013, 9, 12, 22, 12, 21)
    auth_user_32.is_superuser = False
    auth_user_32.username = u'i3ullit'
    auth_user_32.first_name = u''
    auth_user_32.last_name = u''
    auth_user_32.email = u''
    auth_user_32.is_staff = False
    auth_user_32.is_active = True
    auth_user_32.date_joined = datetime.datetime(2013, 9, 12, 22, 12, 21)
    auth_user_32 = importer.save_or_locate(auth_user_32)

    auth_user_33 = User()
    auth_user_33.password = u'pbkdf2_sha256$10000$5Hgu3ICNNfW0$vRZrJrveEW8xNBUkNhO62gCFKmezqUpKE/99IobrcZk='
    auth_user_33.last_login = datetime.datetime(2013, 9, 12, 22, 44, 13)
    auth_user_33.is_superuser = False
    auth_user_33.username = u'longbow656'
    auth_user_33.first_name = u''
    auth_user_33.last_name = u''
    auth_user_33.email = u''
    auth_user_33.is_staff = False
    auth_user_33.is_active = True
    auth_user_33.date_joined = datetime.datetime(2013, 9, 12, 22, 13, 6)
    auth_user_33 = importer.save_or_locate(auth_user_33)

    auth_user_34 = User()
    auth_user_34.password = u'pbkdf2_sha256$10000$6p3maqsbNwjC$95zfHvm5no0ZT2VvsoyVnBtp9FaODc8XI90rFA4R4Hw='
    auth_user_34.last_login = datetime.datetime(2013, 9, 12, 22, 25, 18)
    auth_user_34.is_superuser = False
    auth_user_34.username = u'Othelious'
    auth_user_34.first_name = u''
    auth_user_34.last_name = u''
    auth_user_34.email = u''
    auth_user_34.is_staff = False
    auth_user_34.is_active = True
    auth_user_34.date_joined = datetime.datetime(2013, 9, 12, 22, 25, 18)
    auth_user_34 = importer.save_or_locate(auth_user_34)

    auth_user_35 = User()
    auth_user_35.password = u'pbkdf2_sha256$10000$TfYVYMnoBCfv$57lsNd1NBbnwkeFiVKGl8KtQqZFPZrnGP+Xqk2S8854='
    auth_user_35.last_login = datetime.datetime(2013, 9, 12, 22, 34, 48)
    auth_user_35.is_superuser = False
    auth_user_35.username = u'kmav101'
    auth_user_35.first_name = u''
    auth_user_35.last_name = u''
    auth_user_35.email = u''
    auth_user_35.is_staff = False
    auth_user_35.is_active = True
    auth_user_35.date_joined = datetime.datetime(2013, 9, 12, 22, 34, 48)
    auth_user_35 = importer.save_or_locate(auth_user_35)

    auth_user_36 = User()
    auth_user_36.password = u'pbkdf2_sha256$10000$MdPz7EHx7THY$3gCh+Tpoftdbvl9cPE7yspUC/PEo+J3kmcPU/Qn/uZo='
    auth_user_36.last_login = datetime.datetime(2013, 9, 12, 22, 42, 32)
    auth_user_36.is_superuser = False
    auth_user_36.username = u'SubSpace666'
    auth_user_36.first_name = u''
    auth_user_36.last_name = u''
    auth_user_36.email = u''
    auth_user_36.is_staff = False
    auth_user_36.is_active = True
    auth_user_36.date_joined = datetime.datetime(2013, 9, 12, 22, 42, 32)
    auth_user_36 = importer.save_or_locate(auth_user_36)

    auth_user_37 = User()
    auth_user_37.password = u'pbkdf2_sha256$10000$MbJdUX46ardE$qkDTUlxRkyTsf6JNzX2hXRXDvoDqTllSi4i07MQp/J4='
    auth_user_37.last_login = datetime.datetime(2013, 9, 12, 22, 54, 9)
    auth_user_37.is_superuser = False
    auth_user_37.username = u'Leu'
    auth_user_37.first_name = u''
    auth_user_37.last_name = u''
    auth_user_37.email = u''
    auth_user_37.is_staff = False
    auth_user_37.is_active = True
    auth_user_37.date_joined = datetime.datetime(2013, 9, 12, 22, 54, 9)
    auth_user_37 = importer.save_or_locate(auth_user_37)

    auth_user_38 = User()
    auth_user_38.password = u'pbkdf2_sha256$10000$3Y6N1PDuDvj3$omgY3T+TAQYcZ/RPEYVFHbpHPkkkqVrVTpNFDtdVGSI='
    auth_user_38.last_login = datetime.datetime(2013, 9, 12, 22, 56)
    auth_user_38.is_superuser = False
    auth_user_38.username = u'LethalInterjection'
    auth_user_38.first_name = u''
    auth_user_38.last_name = u''
    auth_user_38.email = u''
    auth_user_38.is_staff = False
    auth_user_38.is_active = True
    auth_user_38.date_joined = datetime.datetime(2013, 9, 12, 22, 56)
    auth_user_38 = importer.save_or_locate(auth_user_38)

    auth_user_39 = User()
    auth_user_39.password = u'pbkdf2_sha256$10000$Lk4A1S6qMewU$lIPCQeZS0XpA37/6B/BCQItyl/oN/ouDKHGiuNc5Glw='
    auth_user_39.last_login = datetime.datetime(2013, 9, 12, 22, 59, 39)
    auth_user_39.is_superuser = False
    auth_user_39.username = u'Thomas-Blood'
    auth_user_39.first_name = u''
    auth_user_39.last_name = u''
    auth_user_39.email = u''
    auth_user_39.is_staff = False
    auth_user_39.is_active = True
    auth_user_39.date_joined = datetime.datetime(2013, 9, 12, 22, 59, 39)
    auth_user_39 = importer.save_or_locate(auth_user_39)

    auth_user_40 = User()
    auth_user_40.password = u'pbkdf2_sha256$10000$4wsmr5Xdm0uo$Fn3QyHA7ehGnXR0Ov9GG4jwqmPrxVOtt6TaKBCQ0TIY='
    auth_user_40.last_login = datetime.datetime(2013, 9, 12, 23, 10, 50)
    auth_user_40.is_superuser = False
    auth_user_40.username = u'Tzet'
    auth_user_40.first_name = u''
    auth_user_40.last_name = u''
    auth_user_40.email = u''
    auth_user_40.is_staff = False
    auth_user_40.is_active = True
    auth_user_40.date_joined = datetime.datetime(2013, 9, 12, 23, 10, 50)
    auth_user_40 = importer.save_or_locate(auth_user_40)

    auth_user_41 = User()
    auth_user_41.password = u'pbkdf2_sha256$10000$qmBe9nttHl7U$7YlFQy22ur0Vv/76dMbkLLerWF18f1dmCYkVj8R4Jv0='
    auth_user_41.last_login = datetime.datetime(2013, 9, 12, 23, 23, 4)
    auth_user_41.is_superuser = False
    auth_user_41.username = u'Nev3rmor3'
    auth_user_41.first_name = u''
    auth_user_41.last_name = u''
    auth_user_41.email = u''
    auth_user_41.is_staff = False
    auth_user_41.is_active = True
    auth_user_41.date_joined = datetime.datetime(2013, 9, 12, 23, 22, 57)
    auth_user_41 = importer.save_or_locate(auth_user_41)

    auth_user_42 = User()
    auth_user_42.password = u'pbkdf2_sha256$10000$ynba1WNtnY4o$SW2wgC3swxBhUb2qPMMOdtheYyC7G45xGxXwgyV+aTU='
    auth_user_42.last_login = datetime.datetime(2013, 9, 12, 23, 23, 11)
    auth_user_42.is_superuser = False
    auth_user_42.username = u'Zrail'
    auth_user_42.first_name = u''
    auth_user_42.last_name = u''
    auth_user_42.email = u''
    auth_user_42.is_staff = False
    auth_user_42.is_active = True
    auth_user_42.date_joined = datetime.datetime(2013, 9, 12, 23, 23, 10)
    auth_user_42 = importer.save_or_locate(auth_user_42)

    auth_user_43 = User()
    auth_user_43.password = u'pbkdf2_sha256$10000$agq19DUMrV92$WO+aqrJDrWGq01cfzgjYF8gHGLr/+22n4OZxyRV6UHc='
    auth_user_43.last_login = datetime.datetime(2013, 9, 12, 23, 35, 49)
    auth_user_43.is_superuser = False
    auth_user_43.username = u'dapperry14'
    auth_user_43.first_name = u''
    auth_user_43.last_name = u''
    auth_user_43.email = u''
    auth_user_43.is_staff = False
    auth_user_43.is_active = True
    auth_user_43.date_joined = datetime.datetime(2013, 9, 12, 23, 35, 49)
    auth_user_43 = importer.save_or_locate(auth_user_43)

    auth_user_44 = User()
    auth_user_44.password = u'pbkdf2_sha256$10000$5gHM6hNpsn54$v35VoYqoMwLqACnPHSfSWRfKfPygOPmyd3mFNdZnYgQ='
    auth_user_44.last_login = datetime.datetime(2013, 9, 12, 23, 44, 19)
    auth_user_44.is_superuser = False
    auth_user_44.username = u'awev'
    auth_user_44.first_name = u''
    auth_user_44.last_name = u''
    auth_user_44.email = u''
    auth_user_44.is_staff = False
    auth_user_44.is_active = True
    auth_user_44.date_joined = datetime.datetime(2013, 9, 12, 23, 44, 19)
    auth_user_44 = importer.save_or_locate(auth_user_44)

    auth_user_45 = User()
    auth_user_45.password = u'pbkdf2_sha256$10000$oWs1ukDG2PcJ$bzQRKZ1ZJy/cSfR3nV2rJ6jWzg66vdA/5NDCuZhweKU='
    auth_user_45.last_login = datetime.datetime(2013, 9, 12, 23, 50, 36)
    auth_user_45.is_superuser = False
    auth_user_45.username = u'durron'
    auth_user_45.first_name = u''
    auth_user_45.last_name = u''
    auth_user_45.email = u''
    auth_user_45.is_staff = False
    auth_user_45.is_active = True
    auth_user_45.date_joined = datetime.datetime(2013, 9, 12, 23, 50, 35)
    auth_user_45 = importer.save_or_locate(auth_user_45)

    auth_user_46 = User()
    auth_user_46.password = u'pbkdf2_sha256$10000$dfg5Zn12LkhT$FD8qCW+hcpv2sIzT+2zfm8LD+LSgMeSkpDkAMrJcshw='
    auth_user_46.last_login = datetime.datetime(2013, 9, 13, 1, 4, 32)
    auth_user_46.is_superuser = False
    auth_user_46.username = u'Delta26'
    auth_user_46.first_name = u''
    auth_user_46.last_name = u''
    auth_user_46.email = u''
    auth_user_46.is_staff = False
    auth_user_46.is_active = True
    auth_user_46.date_joined = datetime.datetime(2013, 9, 13, 1, 4, 31)
    auth_user_46 = importer.save_or_locate(auth_user_46)

    auth_user_47 = User()
    auth_user_47.password = u'pbkdf2_sha256$10000$v31WEAOz7tVm$tomWvMWgP/1Dedc6Gxj6vLVw6VV4sSsJm417iIu3Aqc='
    auth_user_47.last_login = datetime.datetime(2013, 9, 13, 1, 23, 55)
    auth_user_47.is_superuser = False
    auth_user_47.username = u'Shanigami'
    auth_user_47.first_name = u''
    auth_user_47.last_name = u''
    auth_user_47.email = u''
    auth_user_47.is_staff = False
    auth_user_47.is_active = True
    auth_user_47.date_joined = datetime.datetime(2013, 9, 13, 1, 23, 55)
    auth_user_47 = importer.save_or_locate(auth_user_47)

    auth_user_48 = User()
    auth_user_48.password = u'pbkdf2_sha256$10000$MXQDQQgLmM3o$Bguhf05NtlH4PmNlxfixaDmqDC8W0HNDgXX6oBvr1RQ='
    auth_user_48.last_login = datetime.datetime(2013, 9, 13, 1, 48, 20)
    auth_user_48.is_superuser = False
    auth_user_48.username = u'someguy24'
    auth_user_48.first_name = u''
    auth_user_48.last_name = u''
    auth_user_48.email = u''
    auth_user_48.is_staff = False
    auth_user_48.is_active = True
    auth_user_48.date_joined = datetime.datetime(2013, 9, 13, 1, 48, 20)
    auth_user_48 = importer.save_or_locate(auth_user_48)

    auth_user_49 = User()
    auth_user_49.password = u'pbkdf2_sha256$10000$RkpK08ay6pJ3$+p2jyPfFb3153p3f0GF+clP6FNyZ8g67wQByVi56Y5s='
    auth_user_49.last_login = datetime.datetime(2013, 9, 13, 1, 49, 50)
    auth_user_49.is_superuser = False
    auth_user_49.username = u'Shire_Folk'
    auth_user_49.first_name = u''
    auth_user_49.last_name = u''
    auth_user_49.email = u''
    auth_user_49.is_staff = False
    auth_user_49.is_active = True
    auth_user_49.date_joined = datetime.datetime(2013, 9, 13, 1, 49, 50)
    auth_user_49 = importer.save_or_locate(auth_user_49)

    auth_user_50 = User()
    auth_user_50.password = u'pbkdf2_sha256$10000$j0ENAIm3FPa3$t9KHL8+e7MTGpTusI7hbga1wYyVPRjkgF3wgM6+f0WM='
    auth_user_50.last_login = datetime.datetime(2013, 9, 13, 2, 0, 33)
    auth_user_50.is_superuser = False
    auth_user_50.username = u'TheDefender'
    auth_user_50.first_name = u''
    auth_user_50.last_name = u''
    auth_user_50.email = u''
    auth_user_50.is_staff = False
    auth_user_50.is_active = True
    auth_user_50.date_joined = datetime.datetime(2013, 9, 13, 2, 0, 33)
    auth_user_50 = importer.save_or_locate(auth_user_50)

    auth_user_51 = User()
    auth_user_51.password = u'pbkdf2_sha256$10000$jDAAFSFEtFmC$tJosUqRrZmp4N7ybkMfdOgEELIf5VkvfgEtLO8Rv7F0='
    auth_user_51.last_login = datetime.datetime(2013, 9, 13, 2, 8, 4)
    auth_user_51.is_superuser = False
    auth_user_51.username = u'zib'
    auth_user_51.first_name = u''
    auth_user_51.last_name = u''
    auth_user_51.email = u''
    auth_user_51.is_staff = False
    auth_user_51.is_active = True
    auth_user_51.date_joined = datetime.datetime(2013, 9, 13, 2, 8, 4)
    auth_user_51 = importer.save_or_locate(auth_user_51)

    auth_user_52 = User()
    auth_user_52.password = u'pbkdf2_sha256$10000$K5hES6bshXrW$oyuCpaQeHholRsSR+jRjKJSG1IBP5oZTHIRXKw6p7oo='
    auth_user_52.last_login = datetime.datetime(2013, 9, 13, 2, 43, 43)
    auth_user_52.is_superuser = False
    auth_user_52.username = u'Beren_Valari'
    auth_user_52.first_name = u''
    auth_user_52.last_name = u''
    auth_user_52.email = u''
    auth_user_52.is_staff = False
    auth_user_52.is_active = True
    auth_user_52.date_joined = datetime.datetime(2013, 9, 13, 2, 40, 8)
    auth_user_52 = importer.save_or_locate(auth_user_52)

    auth_user_53 = User()
    auth_user_53.password = u'pbkdf2_sha256$10000$xTxFiXAuEpmW$rfKgVvl7rgZHZU1qmKoQs3gP6WTrMgbRDUAoMrM5qG8='
    auth_user_53.last_login = datetime.datetime(2013, 9, 13, 2, 47, 48)
    auth_user_53.is_superuser = False
    auth_user_53.username = u'Ronbocop'
    auth_user_53.first_name = u''
    auth_user_53.last_name = u''
    auth_user_53.email = u''
    auth_user_53.is_staff = False
    auth_user_53.is_active = True
    auth_user_53.date_joined = datetime.datetime(2013, 9, 13, 2, 47, 48)
    auth_user_53 = importer.save_or_locate(auth_user_53)

    auth_user_54 = User()
    auth_user_54.password = u'pbkdf2_sha256$10000$VJEP9FbsiLTV$cpe+GwHWcZK2nKt+ohr+g4cg7oNPBqdH4kr4f8t1+RY='
    auth_user_54.last_login = datetime.datetime(2013, 9, 13, 2, 49, 14)
    auth_user_54.is_superuser = False
    auth_user_54.username = u'sterley'
    auth_user_54.first_name = u''
    auth_user_54.last_name = u''
    auth_user_54.email = u''
    auth_user_54.is_staff = False
    auth_user_54.is_active = True
    auth_user_54.date_joined = datetime.datetime(2013, 9, 13, 2, 49, 14)
    auth_user_54 = importer.save_or_locate(auth_user_54)

    auth_user_55 = User()
    auth_user_55.password = u'pbkdf2_sha256$10000$klwPIPsPcWRG$VzUUu9EcArWj8MkjoUiboZfmwKAf9wXE5TO3ljRvzJU='
    auth_user_55.last_login = datetime.datetime(2013, 9, 13, 3, 8, 17)
    auth_user_55.is_superuser = False
    auth_user_55.username = u'pujinimsae'
    auth_user_55.first_name = u''
    auth_user_55.last_name = u''
    auth_user_55.email = u''
    auth_user_55.is_staff = False
    auth_user_55.is_active = True
    auth_user_55.date_joined = datetime.datetime(2013, 9, 13, 3, 8, 17)
    auth_user_55 = importer.save_or_locate(auth_user_55)

    auth_user_56 = User()
    auth_user_56.password = u'pbkdf2_sha256$10000$4RZUflqGDuGN$uRbHcPV/3JI3LAkdq7aFPrsIjomyCHsB5HBz9nUvRNo='
    auth_user_56.last_login = datetime.datetime(2013, 9, 13, 3, 27, 56)
    auth_user_56.is_superuser = False
    auth_user_56.username = u'thedraygonninja'
    auth_user_56.first_name = u''
    auth_user_56.last_name = u''
    auth_user_56.email = u''
    auth_user_56.is_staff = False
    auth_user_56.is_active = True
    auth_user_56.date_joined = datetime.datetime(2013, 9, 13, 3, 27, 56)
    auth_user_56 = importer.save_or_locate(auth_user_56)

    auth_user_57 = User()
    auth_user_57.password = u'pbkdf2_sha256$10000$cjkmG8w8xHTq$NJ70GtemX72MUw4yo4ywJj7EUddALUDYx25uIHRQHBs='
    auth_user_57.last_login = datetime.datetime(2013, 9, 13, 4, 24, 43)
    auth_user_57.is_superuser = False
    auth_user_57.username = u'DrEG'
    auth_user_57.first_name = u''
    auth_user_57.last_name = u''
    auth_user_57.email = u''
    auth_user_57.is_staff = False
    auth_user_57.is_active = True
    auth_user_57.date_joined = datetime.datetime(2013, 9, 13, 4, 24, 43)
    auth_user_57 = importer.save_or_locate(auth_user_57)

    auth_user_58 = User()
    auth_user_58.password = u'pbkdf2_sha256$10000$htmJfOD4pFAB$xU3lbPIaTSRnnhKjY2rA1g4mmWJO1ng84SlSZJz7BT8='
    auth_user_58.last_login = datetime.datetime(2013, 9, 13, 4, 27, 46)
    auth_user_58.is_superuser = False
    auth_user_58.username = u'xigunder'
    auth_user_58.first_name = u''
    auth_user_58.last_name = u''
    auth_user_58.email = u''
    auth_user_58.is_staff = False
    auth_user_58.is_active = True
    auth_user_58.date_joined = datetime.datetime(2013, 9, 13, 4, 27, 46)
    auth_user_58 = importer.save_or_locate(auth_user_58)

    auth_user_59 = User()
    auth_user_59.password = u'pbkdf2_sha256$10000$VGJzoKNjGlFw$dR4UgxBgZYwQ02/kq1bBuRbS9yMLf2aoU7GnOz1SdvU='
    auth_user_59.last_login = datetime.datetime(2013, 9, 13, 6, 1, 8)
    auth_user_59.is_superuser = False
    auth_user_59.username = u'Harphy'
    auth_user_59.first_name = u''
    auth_user_59.last_name = u''
    auth_user_59.email = u''
    auth_user_59.is_staff = False
    auth_user_59.is_active = True
    auth_user_59.date_joined = datetime.datetime(2013, 9, 13, 6, 1, 8)
    auth_user_59 = importer.save_or_locate(auth_user_59)

    auth_user_60 = User()
    auth_user_60.password = u'pbkdf2_sha256$10000$au1a2wcQxR08$PZX3+aZkvFsNrPEiBnavTZOi889qW5XnuJAxJgp5myE='
    auth_user_60.last_login = datetime.datetime(2013, 9, 13, 6, 25, 49)
    auth_user_60.is_superuser = False
    auth_user_60.username = u'Akumaro'
    auth_user_60.first_name = u''
    auth_user_60.last_name = u''
    auth_user_60.email = u''
    auth_user_60.is_staff = False
    auth_user_60.is_active = True
    auth_user_60.date_joined = datetime.datetime(2013, 9, 13, 6, 25, 48)
    auth_user_60 = importer.save_or_locate(auth_user_60)

    auth_user_61 = User()
    auth_user_61.password = u'pbkdf2_sha256$10000$OR0vBfpaurCq$OqOyegtud0b8KjVziI1X58knvxxBNRIm18zKjNrmAhA='
    auth_user_61.last_login = datetime.datetime(2013, 9, 13, 6, 32, 8)
    auth_user_61.is_superuser = False
    auth_user_61.username = u'Beaver17'
    auth_user_61.first_name = u''
    auth_user_61.last_name = u''
    auth_user_61.email = u''
    auth_user_61.is_staff = False
    auth_user_61.is_active = True
    auth_user_61.date_joined = datetime.datetime(2013, 9, 13, 6, 32, 8)
    auth_user_61 = importer.save_or_locate(auth_user_61)

    auth_user_62 = User()
    auth_user_62.password = u'pbkdf2_sha256$10000$f8NRl0JFCjRS$unKNu0JYAboBJ5XHLoL8fzN2Qtch7hJZvip0sgF6VaY='
    auth_user_62.last_login = datetime.datetime(2013, 9, 13, 6, 50, 59)
    auth_user_62.is_superuser = False
    auth_user_62.username = u'mick4'
    auth_user_62.first_name = u''
    auth_user_62.last_name = u''
    auth_user_62.email = u''
    auth_user_62.is_staff = False
    auth_user_62.is_active = True
    auth_user_62.date_joined = datetime.datetime(2013, 9, 13, 6, 50, 59)
    auth_user_62 = importer.save_or_locate(auth_user_62)

    auth_user_63 = User()
    auth_user_63.password = u'pbkdf2_sha256$10000$zFo7BvUzU8bQ$Xdygg6d5U4qu25hMPhVFA1dbRVNwUnkF7uBcEF7I38k='
    auth_user_63.last_login = datetime.datetime(2013, 9, 13, 6, 58, 41)
    auth_user_63.is_superuser = False
    auth_user_63.username = u'BigBrutal64'
    auth_user_63.first_name = u''
    auth_user_63.last_name = u''
    auth_user_63.email = u''
    auth_user_63.is_staff = False
    auth_user_63.is_active = True
    auth_user_63.date_joined = datetime.datetime(2013, 9, 13, 6, 58, 41)
    auth_user_63 = importer.save_or_locate(auth_user_63)

    auth_user_64 = User()
    auth_user_64.password = u'pbkdf2_sha256$10000$UtIz7FiYOp4N$nQrTfcIGmoDBwksAhCALZ3PwhZNCvZaM9F0keW4mHeE='
    auth_user_64.last_login = datetime.datetime(2013, 9, 13, 8, 21, 58)
    auth_user_64.is_superuser = False
    auth_user_64.username = u'kave'
    auth_user_64.first_name = u''
    auth_user_64.last_name = u''
    auth_user_64.email = u''
    auth_user_64.is_staff = False
    auth_user_64.is_active = True
    auth_user_64.date_joined = datetime.datetime(2013, 9, 13, 8, 21, 58)
    auth_user_64 = importer.save_or_locate(auth_user_64)

    auth_user_65 = User()
    auth_user_65.password = u'pbkdf2_sha256$10000$VdCfX1oPdDvU$NIXSx6+qWh6TFIrmW9RyEswVJseDsAp8MvZF3XlI6rY='
    auth_user_65.last_login = datetime.datetime(2013, 9, 13, 8, 27, 32)
    auth_user_65.is_superuser = False
    auth_user_65.username = u'Stonka'
    auth_user_65.first_name = u''
    auth_user_65.last_name = u''
    auth_user_65.email = u''
    auth_user_65.is_staff = False
    auth_user_65.is_active = True
    auth_user_65.date_joined = datetime.datetime(2013, 9, 13, 8, 27, 32)
    auth_user_65 = importer.save_or_locate(auth_user_65)

    auth_user_66 = User()
    auth_user_66.password = u'pbkdf2_sha256$10000$7DX2q74h5MYR$yXE5GozAJp544igygz/WBzbiTe9uxqG2VQAtXn6i5Jo='
    auth_user_66.last_login = datetime.datetime(2013, 9, 13, 8, 42, 19)
    auth_user_66.is_superuser = False
    auth_user_66.username = u'Warden'
    auth_user_66.first_name = u''
    auth_user_66.last_name = u''
    auth_user_66.email = u''
    auth_user_66.is_staff = False
    auth_user_66.is_active = True
    auth_user_66.date_joined = datetime.datetime(2013, 9, 13, 8, 42, 19)
    auth_user_66 = importer.save_or_locate(auth_user_66)

    auth_user_67 = User()
    auth_user_67.password = u'pbkdf2_sha256$10000$1W8iPZfoIfG7$Iss0xywR6NruYkWvJOFY3oyGZy66VjoyTH7GmOoOiRA='
    auth_user_67.last_login = datetime.datetime(2013, 9, 13, 9, 47, 57)
    auth_user_67.is_superuser = False
    auth_user_67.username = u'Don_Minister'
    auth_user_67.first_name = u''
    auth_user_67.last_name = u''
    auth_user_67.email = u''
    auth_user_67.is_staff = False
    auth_user_67.is_active = True
    auth_user_67.date_joined = datetime.datetime(2013, 9, 13, 9, 47, 57)
    auth_user_67 = importer.save_or_locate(auth_user_67)

    auth_user_68 = User()
    auth_user_68.password = u'pbkdf2_sha256$10000$4tJwH7TiejuR$XuxSxyOs14286S6LS+wFTQs93Qpr42PUp34G42tR+9g='
    auth_user_68.last_login = datetime.datetime(2013, 9, 13, 10, 28, 49)
    auth_user_68.is_superuser = False
    auth_user_68.username = u'tamvegas'
    auth_user_68.first_name = u''
    auth_user_68.last_name = u''
    auth_user_68.email = u''
    auth_user_68.is_staff = False
    auth_user_68.is_active = True
    auth_user_68.date_joined = datetime.datetime(2013, 9, 13, 10, 27, 43)
    auth_user_68 = importer.save_or_locate(auth_user_68)

    auth_user_69 = User()
    auth_user_69.password = u'pbkdf2_sha256$10000$ra7D4hqbjMaD$uKksJ85hrvTrtqPy8CTOjJpfZ7Ex+3tfwEUNcOueKO0='
    auth_user_69.last_login = datetime.datetime(2013, 9, 13, 10, 53, 8)
    auth_user_69.is_superuser = False
    auth_user_69.username = u'Misterdelle96'
    auth_user_69.first_name = u''
    auth_user_69.last_name = u''
    auth_user_69.email = u''
    auth_user_69.is_staff = False
    auth_user_69.is_active = True
    auth_user_69.date_joined = datetime.datetime(2013, 9, 13, 10, 53, 8)
    auth_user_69 = importer.save_or_locate(auth_user_69)

    auth_user_70 = User()
    auth_user_70.password = u'pbkdf2_sha256$10000$1cF8SvDH75Vu$AIXC+xtJd/qMC9bZOnhRaxQ+0vAfunkWctoKjHrzaSw='
    auth_user_70.last_login = datetime.datetime(2013, 9, 13, 12, 8, 38)
    auth_user_70.is_superuser = False
    auth_user_70.username = u'ALoS'
    auth_user_70.first_name = u''
    auth_user_70.last_name = u''
    auth_user_70.email = u''
    auth_user_70.is_staff = False
    auth_user_70.is_active = True
    auth_user_70.date_joined = datetime.datetime(2013, 9, 13, 12, 7, 58)
    auth_user_70 = importer.save_or_locate(auth_user_70)

    auth_user_71 = User()
    auth_user_71.password = u'pbkdf2_sha256$10000$FpdlC7hPRuVM$b05SbNP9uqN9CDORqSysZVuUVwyt2Uv8ZB47p0RjDTE='
    auth_user_71.last_login = datetime.datetime(2013, 9, 13, 12, 8, 13)
    auth_user_71.is_superuser = False
    auth_user_71.username = u'nano'
    auth_user_71.first_name = u''
    auth_user_71.last_name = u''
    auth_user_71.email = u''
    auth_user_71.is_staff = False
    auth_user_71.is_active = True
    auth_user_71.date_joined = datetime.datetime(2013, 9, 13, 12, 8, 12)
    auth_user_71 = importer.save_or_locate(auth_user_71)

    auth_user_72 = User()
    auth_user_72.password = u'pbkdf2_sha256$10000$n4axW1aVkFr4$HH8EPXDUksOjOIcWfTbLCOnPd/Y8TcjP3AneqFvmj+I='
    auth_user_72.last_login = datetime.datetime(2013, 9, 13, 13, 34, 4)
    auth_user_72.is_superuser = False
    auth_user_72.username = u'Hypperzz22'
    auth_user_72.first_name = u''
    auth_user_72.last_name = u''
    auth_user_72.email = u''
    auth_user_72.is_staff = False
    auth_user_72.is_active = True
    auth_user_72.date_joined = datetime.datetime(2013, 9, 13, 13, 34, 3)
    auth_user_72 = importer.save_or_locate(auth_user_72)

    auth_user_73 = User()
    auth_user_73.password = u'pbkdf2_sha256$10000$KNshL6iCaoCJ$7MVoPAIckFif3FPAhXsBjIe2+YV4LSEGipwJ0bq6AUU='
    auth_user_73.last_login = datetime.datetime(2013, 9, 13, 14, 55, 43)
    auth_user_73.is_superuser = False
    auth_user_73.username = u'hogbola'
    auth_user_73.first_name = u''
    auth_user_73.last_name = u''
    auth_user_73.email = u''
    auth_user_73.is_staff = False
    auth_user_73.is_active = True
    auth_user_73.date_joined = datetime.datetime(2013, 9, 13, 14, 32, 18)
    auth_user_73 = importer.save_or_locate(auth_user_73)

    auth_user_74 = User()
    auth_user_74.password = u'pbkdf2_sha256$10000$WHMuL5ZufiSb$qMdluZlzGTnsAxjfRsnYsfkiC+vBqS+6ZQ2Gdc5EtxY='
    auth_user_74.last_login = datetime.datetime(2013, 9, 13, 14, 57, 4)
    auth_user_74.is_superuser = False
    auth_user_74.username = u'Lorby'
    auth_user_74.first_name = u''
    auth_user_74.last_name = u''
    auth_user_74.email = u''
    auth_user_74.is_staff = False
    auth_user_74.is_active = True
    auth_user_74.date_joined = datetime.datetime(2013, 9, 13, 14, 57, 4)
    auth_user_74 = importer.save_or_locate(auth_user_74)

    auth_user_75 = User()
    auth_user_75.password = u'pbkdf2_sha256$10000$NE75WsdWx5f9$ckLDXg9Qk+nfHvmc9KyEBcCmxYX9Ml1jAu0M3uL/5CM='
    auth_user_75.last_login = datetime.datetime(2013, 9, 13, 15, 2, 19)
    auth_user_75.is_superuser = False
    auth_user_75.username = u'LordofNaught'
    auth_user_75.first_name = u''
    auth_user_75.last_name = u''
    auth_user_75.email = u''
    auth_user_75.is_staff = False
    auth_user_75.is_active = True
    auth_user_75.date_joined = datetime.datetime(2013, 9, 13, 15, 2, 19)
    auth_user_75 = importer.save_or_locate(auth_user_75)

    auth_user_76 = User()
    auth_user_76.password = u'pbkdf2_sha256$10000$uq03c1wjDoKv$oJNSmna0FjHhZnNR1s2BcOGg8GJaz6wOPsBaaLCIQsE='
    auth_user_76.last_login = datetime.datetime(2013, 9, 13, 15, 4, 44)
    auth_user_76.is_superuser = False
    auth_user_76.username = u'Braddass'
    auth_user_76.first_name = u''
    auth_user_76.last_name = u''
    auth_user_76.email = u''
    auth_user_76.is_staff = False
    auth_user_76.is_active = True
    auth_user_76.date_joined = datetime.datetime(2013, 9, 13, 15, 4, 44)
    auth_user_76 = importer.save_or_locate(auth_user_76)

    auth_user_77 = User()
    auth_user_77.password = u'pbkdf2_sha256$10000$erD570Nu1iv2$jbnQt/0fDfJtc+y6VNTq2P0n+n7RK8HiLQlZvZxJNM8='
    auth_user_77.last_login = datetime.datetime(2013, 9, 13, 15, 31, 14)
    auth_user_77.is_superuser = False
    auth_user_77.username = u'maphughes'
    auth_user_77.first_name = u''
    auth_user_77.last_name = u''
    auth_user_77.email = u''
    auth_user_77.is_staff = False
    auth_user_77.is_active = True
    auth_user_77.date_joined = datetime.datetime(2013, 9, 13, 15, 31, 14)
    auth_user_77 = importer.save_or_locate(auth_user_77)

    auth_user_78 = User()
    auth_user_78.password = u'pbkdf2_sha256$10000$Ftgjc0g5VFfK$T0I6/EhQwA4zQNpZLKU8UnzAqGAwml2kKFZ0LPJW+cM='
    auth_user_78.last_login = datetime.datetime(2013, 9, 13, 16, 33, 57)
    auth_user_78.is_superuser = False
    auth_user_78.username = u'patback66'
    auth_user_78.first_name = u''
    auth_user_78.last_name = u''
    auth_user_78.email = u''
    auth_user_78.is_staff = False
    auth_user_78.is_active = True
    auth_user_78.date_joined = datetime.datetime(2013, 9, 13, 16, 33, 57)
    auth_user_78 = importer.save_or_locate(auth_user_78)

    auth_user_79 = User()
    auth_user_79.password = u'pbkdf2_sha256$10000$SffMIbFc2qR0$+2xFxpXN/Gvooko5jE8xKvZQRqXQZ0XqkQRUM1y1YeE='
    auth_user_79.last_login = datetime.datetime(2013, 9, 13, 17, 45, 19)
    auth_user_79.is_superuser = False
    auth_user_79.username = u'thecomputerdude'
    auth_user_79.first_name = u''
    auth_user_79.last_name = u''
    auth_user_79.email = u''
    auth_user_79.is_staff = False
    auth_user_79.is_active = True
    auth_user_79.date_joined = datetime.datetime(2013, 9, 13, 17, 45, 19)
    auth_user_79 = importer.save_or_locate(auth_user_79)

    auth_user_80 = User()
    auth_user_80.password = u'pbkdf2_sha256$10000$D45moN6ShSz1$Yn9/2NHOly3G4WD1E8Nb3NDCGoFa58dp5hQE9DnM2zE='
    auth_user_80.last_login = datetime.datetime(2013, 9, 13, 18, 52, 6)
    auth_user_80.is_superuser = False
    auth_user_80.username = u'Blorthag'
    auth_user_80.first_name = u''
    auth_user_80.last_name = u''
    auth_user_80.email = u''
    auth_user_80.is_staff = False
    auth_user_80.is_active = True
    auth_user_80.date_joined = datetime.datetime(2013, 9, 13, 18, 52, 5)
    auth_user_80 = importer.save_or_locate(auth_user_80)

    auth_user_81 = User()
    auth_user_81.password = u'pbkdf2_sha256$10000$wGbIdJwqBhSE$QsLJETlkH3nlLtwQUvA68hjw7iPaAquwI5pbz3hqZaQ='
    auth_user_81.last_login = datetime.datetime(2013, 9, 13, 18, 54, 16)
    auth_user_81.is_superuser = False
    auth_user_81.username = u'dudejmass'
    auth_user_81.first_name = u''
    auth_user_81.last_name = u''
    auth_user_81.email = u''
    auth_user_81.is_staff = False
    auth_user_81.is_active = True
    auth_user_81.date_joined = datetime.datetime(2013, 9, 13, 18, 54, 16)
    auth_user_81 = importer.save_or_locate(auth_user_81)

    auth_user_82 = User()
    auth_user_82.password = u'pbkdf2_sha256$10000$2ulhr465qc5g$WYCdSuK0DkCcWpcRkxyIiQ5FvJBtsbRYPNYjruubFvI='
    auth_user_82.last_login = datetime.datetime(2013, 9, 13, 20, 51, 50)
    auth_user_82.is_superuser = False
    auth_user_82.username = u'MrG'
    auth_user_82.first_name = u''
    auth_user_82.last_name = u''
    auth_user_82.email = u''
    auth_user_82.is_staff = False
    auth_user_82.is_active = True
    auth_user_82.date_joined = datetime.datetime(2013, 9, 13, 20, 51, 50)
    auth_user_82 = importer.save_or_locate(auth_user_82)

    auth_user_83 = User()
    auth_user_83.password = u'pbkdf2_sha256$10000$Oa1r1acC1zSe$GaoSGkHOTQpAdSUZcfNpmQjx/r9qh2qRo1e4lWza/AQ='
    auth_user_83.last_login = datetime.datetime(2013, 9, 13, 22, 51, 4)
    auth_user_83.is_superuser = False
    auth_user_83.username = u'Sathorus'
    auth_user_83.first_name = u''
    auth_user_83.last_name = u''
    auth_user_83.email = u''
    auth_user_83.is_staff = False
    auth_user_83.is_active = True
    auth_user_83.date_joined = datetime.datetime(2013, 9, 13, 22, 51, 4)
    auth_user_83 = importer.save_or_locate(auth_user_83)

    auth_user_84 = User()
    auth_user_84.password = u'pbkdf2_sha256$10000$0Infseet8AaE$gQBTTFEeVt0MxNR1cMpKjXiWcZQnm9MeTk3NjfUDenM='
    auth_user_84.last_login = datetime.datetime(2013, 9, 13, 23, 30, 7)
    auth_user_84.is_superuser = False
    auth_user_84.username = u'TheGreymane'
    auth_user_84.first_name = u''
    auth_user_84.last_name = u''
    auth_user_84.email = u''
    auth_user_84.is_staff = False
    auth_user_84.is_active = True
    auth_user_84.date_joined = datetime.datetime(2013, 9, 13, 23, 30, 7)
    auth_user_84 = importer.save_or_locate(auth_user_84)

    auth_user_85 = User()
    auth_user_85.password = u'pbkdf2_sha256$10000$mj38n9nFJKpq$63IXTPy0FrZROahRJuJWRl5bPoH6shdUBWRZfv1exkI='
    auth_user_85.last_login = datetime.datetime(2013, 9, 14, 0, 42, 55)
    auth_user_85.is_superuser = False
    auth_user_85.username = u'moxobuk'
    auth_user_85.first_name = u''
    auth_user_85.last_name = u''
    auth_user_85.email = u''
    auth_user_85.is_staff = False
    auth_user_85.is_active = True
    auth_user_85.date_joined = datetime.datetime(2013, 9, 14, 0, 42, 55)
    auth_user_85 = importer.save_or_locate(auth_user_85)

    auth_user_86 = User()
    auth_user_86.password = u'pbkdf2_sha256$10000$cd63AwlK1t8p$YReJKnjhcYeXsx6f8HA5mP4nrlnIUsISuXXgfq6UUtc='
    auth_user_86.last_login = datetime.datetime(2013, 9, 14, 1, 27)
    auth_user_86.is_superuser = False
    auth_user_86.username = u'Breygon'
    auth_user_86.first_name = u''
    auth_user_86.last_name = u''
    auth_user_86.email = u''
    auth_user_86.is_staff = False
    auth_user_86.is_active = True
    auth_user_86.date_joined = datetime.datetime(2013, 9, 14, 1, 27)
    auth_user_86 = importer.save_or_locate(auth_user_86)

    auth_user_87 = User()
    auth_user_87.password = u'pbkdf2_sha256$10000$Nt64fwZsNsc2$Qt7/VGcOfYR6tDqI4o3JG3PKEBqcXf23dkgB7GYISH8='
    auth_user_87.last_login = datetime.datetime(2013, 9, 14, 3, 3, 40)
    auth_user_87.is_superuser = False
    auth_user_87.username = u'MadHadad'
    auth_user_87.first_name = u''
    auth_user_87.last_name = u''
    auth_user_87.email = u''
    auth_user_87.is_staff = False
    auth_user_87.is_active = True
    auth_user_87.date_joined = datetime.datetime(2013, 9, 14, 3, 3, 39)
    auth_user_87 = importer.save_or_locate(auth_user_87)

    auth_user_88 = User()
    auth_user_88.password = u'pbkdf2_sha256$10000$l3pDclnjXm4V$ZHMwMGqMzZIBVhVg564+F1y+bLm4DolO/ip8qWMKO/w='
    auth_user_88.last_login = datetime.datetime(2013, 9, 14, 10, 46, 8)
    auth_user_88.is_superuser = False
    auth_user_88.username = u'backwardscancan'
    auth_user_88.first_name = u''
    auth_user_88.last_name = u''
    auth_user_88.email = u''
    auth_user_88.is_staff = False
    auth_user_88.is_active = True
    auth_user_88.date_joined = datetime.datetime(2013, 9, 14, 10, 46, 8)
    auth_user_88 = importer.save_or_locate(auth_user_88)

    auth_user_89 = User()
    auth_user_89.password = u'pbkdf2_sha256$10000$P967QLuMRHFy$pmIl+u3FIt8FBRiDPRgVreRpu/TDaEQXkIUGCDYTrPE='
    auth_user_89.last_login = datetime.datetime(2013, 9, 14, 11, 21, 27)
    auth_user_89.is_superuser = False
    auth_user_89.username = u'Filifjonka'
    auth_user_89.first_name = u''
    auth_user_89.last_name = u''
    auth_user_89.email = u''
    auth_user_89.is_staff = False
    auth_user_89.is_active = True
    auth_user_89.date_joined = datetime.datetime(2013, 9, 14, 11, 21, 27)
    auth_user_89 = importer.save_or_locate(auth_user_89)

    auth_user_90 = User()
    auth_user_90.password = u'pbkdf2_sha256$10000$Um4VZ5A3ZRBX$UiG/3Oz9PwEkCmPqwCiuAEshEybqdr8fhW6F5dhhiCk='
    auth_user_90.last_login = datetime.datetime(2013, 9, 14, 11, 54, 49)
    auth_user_90.is_superuser = False
    auth_user_90.username = u'Skypilot343'
    auth_user_90.first_name = u''
    auth_user_90.last_name = u''
    auth_user_90.email = u''
    auth_user_90.is_staff = False
    auth_user_90.is_active = True
    auth_user_90.date_joined = datetime.datetime(2013, 9, 14, 11, 54, 49)
    auth_user_90 = importer.save_or_locate(auth_user_90)

    auth_user_91 = User()
    auth_user_91.password = u'pbkdf2_sha256$10000$faB81MTzPZah$MnTmahB5n7+yVU3XEJCHwDe1MAqhRq0FvU1Bimz3DoM='
    auth_user_91.last_login = datetime.datetime(2013, 9, 14, 14, 11, 43)
    auth_user_91.is_superuser = False
    auth_user_91.username = u'smartrunner'
    auth_user_91.first_name = u''
    auth_user_91.last_name = u''
    auth_user_91.email = u''
    auth_user_91.is_staff = False
    auth_user_91.is_active = True
    auth_user_91.date_joined = datetime.datetime(2013, 9, 14, 14, 11, 43)
    auth_user_91 = importer.save_or_locate(auth_user_91)

    auth_user_92 = User()
    auth_user_92.password = u'pbkdf2_sha256$10000$F0JkN24Kks1I$UrHf0QxpMeoKc96QtmDJIsowoAFlaZ2jKiQ8XSZLYQc='
    auth_user_92.last_login = datetime.datetime(2013, 9, 14, 15, 59, 14)
    auth_user_92.is_superuser = False
    auth_user_92.username = u'Broadway'
    auth_user_92.first_name = u''
    auth_user_92.last_name = u''
    auth_user_92.email = u''
    auth_user_92.is_staff = False
    auth_user_92.is_active = True
    auth_user_92.date_joined = datetime.datetime(2013, 9, 14, 15, 59, 14)
    auth_user_92 = importer.save_or_locate(auth_user_92)

    auth_user_93 = User()
    auth_user_93.password = u'pbkdf2_sha256$10000$virmuAp3SMLB$hW6/yHKA9z9oMgemswUTgruGyFK/MrvqBPPqXz87fY0='
    auth_user_93.last_login = datetime.datetime(2013, 9, 14, 20, 22, 11)
    auth_user_93.is_superuser = False
    auth_user_93.username = u'vulcan6'
    auth_user_93.first_name = u''
    auth_user_93.last_name = u''
    auth_user_93.email = u''
    auth_user_93.is_staff = False
    auth_user_93.is_active = True
    auth_user_93.date_joined = datetime.datetime(2013, 9, 14, 20, 22, 10)
    auth_user_93 = importer.save_or_locate(auth_user_93)

    auth_user_94 = User()
    auth_user_94.password = u'pbkdf2_sha256$10000$emBfyH5sc4QN$rerLDDn2WgTxpkqBtcGwDxb2OqSDJkHL3Zpcalc/j6o='
    auth_user_94.last_login = datetime.datetime(2013, 9, 14, 20, 59, 24)
    auth_user_94.is_superuser = False
    auth_user_94.username = u'Mooseay'
    auth_user_94.first_name = u''
    auth_user_94.last_name = u''
    auth_user_94.email = u''
    auth_user_94.is_staff = False
    auth_user_94.is_active = True
    auth_user_94.date_joined = datetime.datetime(2013, 9, 14, 20, 59, 24)
    auth_user_94 = importer.save_or_locate(auth_user_94)

    auth_user_95 = User()
    auth_user_95.password = u'pbkdf2_sha256$10000$vJVXNGF5wwkS$kHmJ2P43R9o/0gnKrH6J01LYJWuIUpIXdsScdthca6o='
    auth_user_95.last_login = datetime.datetime(2013, 9, 14, 21, 45, 46)
    auth_user_95.is_superuser = False
    auth_user_95.username = u'pawk'
    auth_user_95.first_name = u''
    auth_user_95.last_name = u''
    auth_user_95.email = u''
    auth_user_95.is_staff = False
    auth_user_95.is_active = True
    auth_user_95.date_joined = datetime.datetime(2013, 9, 14, 21, 45, 46)
    auth_user_95 = importer.save_or_locate(auth_user_95)

    auth_user_96 = User()
    auth_user_96.password = u'pbkdf2_sha256$10000$O9qfHoi2mLHs$symhHzcJ26j8a0+KpjprclgJB4foCD3nSsuOVIV4pAY='
    auth_user_96.last_login = datetime.datetime(2013, 9, 14, 23, 28, 14)
    auth_user_96.is_superuser = False
    auth_user_96.username = u'jako800'
    auth_user_96.first_name = u''
    auth_user_96.last_name = u''
    auth_user_96.email = u''
    auth_user_96.is_staff = False
    auth_user_96.is_active = True
    auth_user_96.date_joined = datetime.datetime(2013, 9, 14, 23, 28, 14)
    auth_user_96 = importer.save_or_locate(auth_user_96)

    auth_user_97 = User()
    auth_user_97.password = u'pbkdf2_sha256$10000$8OZCjgLcT4WD$9aSs85KGYiLETWGdsHqBOZM/J33Xe0zC16IimQJuTWQ='
    auth_user_97.last_login = datetime.datetime(2013, 9, 15, 1, 10, 34)
    auth_user_97.is_superuser = False
    auth_user_97.username = u'Invictia'
    auth_user_97.first_name = u''
    auth_user_97.last_name = u''
    auth_user_97.email = u''
    auth_user_97.is_staff = False
    auth_user_97.is_active = True
    auth_user_97.date_joined = datetime.datetime(2013, 9, 15, 1, 10, 33)
    auth_user_97 = importer.save_or_locate(auth_user_97)

    auth_user_98 = User()
    auth_user_98.password = u'pbkdf2_sha256$10000$OXNk0LPYQSjf$NFkd+m37zThSneZLfaRpybJH22XCCC+usenR0o375rA='
    auth_user_98.last_login = datetime.datetime(2013, 9, 15, 1, 20, 43)
    auth_user_98.is_superuser = False
    auth_user_98.username = u'paf1701'
    auth_user_98.first_name = u''
    auth_user_98.last_name = u''
    auth_user_98.email = u''
    auth_user_98.is_staff = False
    auth_user_98.is_active = True
    auth_user_98.date_joined = datetime.datetime(2013, 9, 15, 1, 20, 43)
    auth_user_98 = importer.save_or_locate(auth_user_98)

    auth_user_99 = User()
    auth_user_99.password = u'pbkdf2_sha256$10000$ATyFzEYUuzLx$CAOZ23V36hiertR/w1mXIRrthBE0P6gmflaG3zkEOKE='
    auth_user_99.last_login = datetime.datetime(2013, 9, 15, 6, 55, 35)
    auth_user_99.is_superuser = False
    auth_user_99.username = u'Looth'
    auth_user_99.first_name = u''
    auth_user_99.last_name = u''
    auth_user_99.email = u''
    auth_user_99.is_staff = False
    auth_user_99.is_active = True
    auth_user_99.date_joined = datetime.datetime(2013, 9, 15, 6, 55, 34)
    auth_user_99 = importer.save_or_locate(auth_user_99)

    auth_user_100 = User()
    auth_user_100.password = u'pbkdf2_sha256$10000$kkTZyjTdWI49$AQLLpADyMV9XgLvk6Kc/btRQNToatTWRrvkYk6K5niY='
    auth_user_100.last_login = datetime.datetime(2013, 9, 15, 7, 38, 22)
    auth_user_100.is_superuser = False
    auth_user_100.username = u'Burrich'
    auth_user_100.first_name = u''
    auth_user_100.last_name = u''
    auth_user_100.email = u''
    auth_user_100.is_staff = False
    auth_user_100.is_active = True
    auth_user_100.date_joined = datetime.datetime(2013, 9, 15, 7, 38, 22)
    auth_user_100 = importer.save_or_locate(auth_user_100)

    auth_user_101 = User()
    auth_user_101.password = u'pbkdf2_sha256$10000$psz6tXsLzKHi$jdLiEJ6yyAUD6l2h1y6UVaxso4J3Nb5Q2pDI+Q04Koc='
    auth_user_101.last_login = datetime.datetime(2013, 9, 15, 10, 19, 46)
    auth_user_101.is_superuser = False
    auth_user_101.username = u'Soban'
    auth_user_101.first_name = u''
    auth_user_101.last_name = u''
    auth_user_101.email = u''
    auth_user_101.is_staff = False
    auth_user_101.is_active = True
    auth_user_101.date_joined = datetime.datetime(2013, 9, 15, 10, 19, 46)
    auth_user_101 = importer.save_or_locate(auth_user_101)

    auth_user_102 = User()
    auth_user_102.password = u'pbkdf2_sha256$10000$Z8t9cVW53a5h$UyOPx7H8zm4YjuSAU2hEhjZPEq+xLcRLt3uH87IVv8U='
    auth_user_102.last_login = datetime.datetime(2013, 9, 15, 14, 16, 32)
    auth_user_102.is_superuser = False
    auth_user_102.username = u'mason4300'
    auth_user_102.first_name = u''
    auth_user_102.last_name = u''
    auth_user_102.email = u''
    auth_user_102.is_staff = False
    auth_user_102.is_active = True
    auth_user_102.date_joined = datetime.datetime(2013, 9, 15, 14, 16, 32)
    auth_user_102 = importer.save_or_locate(auth_user_102)

    auth_user_103 = User()
    auth_user_103.password = u'pbkdf2_sha256$10000$Ff2Z6S6OLT7n$wcBWLWg2JA9AUbw43mW1L/6bUVDePXOyZZWNowkXUeE='
    auth_user_103.last_login = datetime.datetime(2013, 9, 15, 14, 20, 26)
    auth_user_103.is_superuser = False
    auth_user_103.username = u'Steeler'
    auth_user_103.first_name = u''
    auth_user_103.last_name = u''
    auth_user_103.email = u''
    auth_user_103.is_staff = False
    auth_user_103.is_active = True
    auth_user_103.date_joined = datetime.datetime(2013, 9, 15, 14, 20, 26)
    auth_user_103 = importer.save_or_locate(auth_user_103)

    auth_user_104 = User()
    auth_user_104.password = u'pbkdf2_sha256$10000$SYwkNDEPOZDH$A2rVW/GqLm36nsCo3a1XlYcgNg1q5f0fcv7kjPGoXAk='
    auth_user_104.last_login = datetime.datetime(2013, 9, 15, 17, 4, 51)
    auth_user_104.is_superuser = False
    auth_user_104.username = u'Ryu Saga'
    auth_user_104.first_name = u''
    auth_user_104.last_name = u''
    auth_user_104.email = u''
    auth_user_104.is_staff = False
    auth_user_104.is_active = True
    auth_user_104.date_joined = datetime.datetime(2013, 9, 15, 17, 4, 51)
    auth_user_104 = importer.save_or_locate(auth_user_104)

    auth_user_105 = User()
    auth_user_105.password = u'pbkdf2_sha256$10000$Xgn4G4RqIfya$yuMfFAoXEjIVV8ZSoqfIhBPvwiBGJrwGohN3cXag2Zc='
    auth_user_105.last_login = datetime.datetime(2013, 9, 15, 18, 16, 59)
    auth_user_105.is_superuser = False
    auth_user_105.username = u'Nighthawk666'
    auth_user_105.first_name = u''
    auth_user_105.last_name = u''
    auth_user_105.email = u''
    auth_user_105.is_staff = False
    auth_user_105.is_active = True
    auth_user_105.date_joined = datetime.datetime(2013, 9, 15, 18, 16, 58)
    auth_user_105 = importer.save_or_locate(auth_user_105)

    auth_user_106 = User()
    auth_user_106.password = u'pbkdf2_sha256$10000$79avs5RzU8zO$yiKftETAh/3OE6YHKVdbnmtScbDF1MOBAHdSWJjzNJI='
    auth_user_106.last_login = datetime.datetime(2013, 9, 15, 18, 56, 7)
    auth_user_106.is_superuser = False
    auth_user_106.username = u'Timeshock'
    auth_user_106.first_name = u''
    auth_user_106.last_name = u''
    auth_user_106.email = u''
    auth_user_106.is_staff = False
    auth_user_106.is_active = True
    auth_user_106.date_joined = datetime.datetime(2013, 9, 15, 18, 56, 7)
    auth_user_106 = importer.save_or_locate(auth_user_106)

    auth_user_107 = User()
    auth_user_107.password = u'pbkdf2_sha256$10000$qPBHTeT2aam1$UDwALRESE7HnbVBIkwXYsyiqIKcCS2sjfoXOohkZPDY='
    auth_user_107.last_login = datetime.datetime(2013, 9, 15, 20, 16, 28)
    auth_user_107.is_superuser = False
    auth_user_107.username = u'Taw'
    auth_user_107.first_name = u''
    auth_user_107.last_name = u''
    auth_user_107.email = u''
    auth_user_107.is_staff = False
    auth_user_107.is_active = True
    auth_user_107.date_joined = datetime.datetime(2013, 9, 15, 20, 16, 28)
    auth_user_107 = importer.save_or_locate(auth_user_107)

    auth_user_108 = User()
    auth_user_108.password = u'pbkdf2_sha256$10000$BVNZmUdHmJHL$29WcA7nJzYuojxzXmvDDUjpmQrovF6/QDzQ4mROX2gA='
    auth_user_108.last_login = datetime.datetime(2013, 9, 15, 21, 33, 38)
    auth_user_108.is_superuser = False
    auth_user_108.username = u'gbsilverio'
    auth_user_108.first_name = u''
    auth_user_108.last_name = u''
    auth_user_108.email = u''
    auth_user_108.is_staff = False
    auth_user_108.is_active = True
    auth_user_108.date_joined = datetime.datetime(2013, 9, 15, 21, 33, 38)
    auth_user_108 = importer.save_or_locate(auth_user_108)

    auth_user_109 = User()
    auth_user_109.password = u'pbkdf2_sha256$10000$2pG79WKdf2Xo$hPbcaAsIV+aGvNndUNoFCrMokdEj8tdJ25InoT4EasU='
    auth_user_109.last_login = datetime.datetime(2013, 9, 15, 22, 10, 7)
    auth_user_109.is_superuser = False
    auth_user_109.username = u'Phoenix'
    auth_user_109.first_name = u''
    auth_user_109.last_name = u''
    auth_user_109.email = u''
    auth_user_109.is_staff = False
    auth_user_109.is_active = True
    auth_user_109.date_joined = datetime.datetime(2013, 9, 15, 22, 10, 7)
    auth_user_109 = importer.save_or_locate(auth_user_109)

    auth_user_110 = User()
    auth_user_110.password = u'pbkdf2_sha256$10000$xjllVPwxXaNW$VRzTcGZL839oNgrJUt6ykoXma6VgUjaQkRufV/g1wWU='
    auth_user_110.last_login = datetime.datetime(2013, 9, 15, 23, 49, 25)
    auth_user_110.is_superuser = False
    auth_user_110.username = u'FeralBadger'
    auth_user_110.first_name = u''
    auth_user_110.last_name = u''
    auth_user_110.email = u''
    auth_user_110.is_staff = False
    auth_user_110.is_active = True
    auth_user_110.date_joined = datetime.datetime(2013, 9, 15, 23, 49, 25)
    auth_user_110 = importer.save_or_locate(auth_user_110)

    auth_user_111 = User()
    auth_user_111.password = u'pbkdf2_sha256$10000$y8yvcgegSHiv$O5jq+z7sWStrlwn+OTA+Ee4HZjaG8HmjzE292wSMPKw='
    auth_user_111.last_login = datetime.datetime(2013, 9, 16, 0, 38, 38)
    auth_user_111.is_superuser = False
    auth_user_111.username = u'Fazno'
    auth_user_111.first_name = u''
    auth_user_111.last_name = u''
    auth_user_111.email = u''
    auth_user_111.is_staff = False
    auth_user_111.is_active = True
    auth_user_111.date_joined = datetime.datetime(2013, 9, 16, 0, 38, 38)
    auth_user_111 = importer.save_or_locate(auth_user_111)

    auth_user_112 = User()
    auth_user_112.password = u'pbkdf2_sha256$10000$65WT2ZIQ7na5$0qQ6QI7Mfgsew42DCQzg8HZ5rovqPUsyKFPJBl6OlF8='
    auth_user_112.last_login = datetime.datetime(2013, 9, 16, 1, 4, 3)
    auth_user_112.is_superuser = False
    auth_user_112.username = u'JoseGasparilla'
    auth_user_112.first_name = u''
    auth_user_112.last_name = u''
    auth_user_112.email = u''
    auth_user_112.is_staff = False
    auth_user_112.is_active = True
    auth_user_112.date_joined = datetime.datetime(2013, 9, 16, 1, 4, 3)
    auth_user_112 = importer.save_or_locate(auth_user_112)

    auth_user_113 = User()
    auth_user_113.password = u'pbkdf2_sha256$10000$lsdg0N1AdZyK$OexEe0zNsXIXhfsAOjqFgEY7kvFLFzHZPT/+12F6vEk='
    auth_user_113.last_login = datetime.datetime(2013, 9, 16, 9, 35, 57)
    auth_user_113.is_superuser = False
    auth_user_113.username = u'FF-Darkhalf'
    auth_user_113.first_name = u''
    auth_user_113.last_name = u''
    auth_user_113.email = u''
    auth_user_113.is_staff = False
    auth_user_113.is_active = True
    auth_user_113.date_joined = datetime.datetime(2013, 9, 16, 9, 35, 57)
    auth_user_113 = importer.save_or_locate(auth_user_113)

    auth_user_114 = User()
    auth_user_114.password = u'pbkdf2_sha256$10000$Iw1de46Ia6IM$X27a01jee6ALATZOhzc0uK0P+fAq6nsn4AVspJGZOQY='
    auth_user_114.last_login = datetime.datetime(2013, 9, 16, 16, 31, 26)
    auth_user_114.is_superuser = False
    auth_user_114.username = u'Tector'
    auth_user_114.first_name = u''
    auth_user_114.last_name = u''
    auth_user_114.email = u''
    auth_user_114.is_staff = False
    auth_user_114.is_active = True
    auth_user_114.date_joined = datetime.datetime(2013, 9, 16, 16, 31, 26)
    auth_user_114 = importer.save_or_locate(auth_user_114)

    auth_user_115 = User()
    auth_user_115.password = u'pbkdf2_sha256$10000$xmpQm3wGf2ld$vJ6SxIlcgOEJl3SygZQQlrztbUd1kR8pVUm+mPI/bf0='
    auth_user_115.last_login = datetime.datetime(2013, 9, 16, 17, 38, 17)
    auth_user_115.is_superuser = False
    auth_user_115.username = u'Holyvision'
    auth_user_115.first_name = u''
    auth_user_115.last_name = u''
    auth_user_115.email = u''
    auth_user_115.is_staff = False
    auth_user_115.is_active = True
    auth_user_115.date_joined = datetime.datetime(2013, 9, 16, 17, 38, 16)
    auth_user_115 = importer.save_or_locate(auth_user_115)

    auth_user_116 = User()
    auth_user_116.password = u'pbkdf2_sha256$10000$Zho6VeA6zK75$K6ks0+t/M5XjIx9Ba0//pUFN8Hugyu8R+roDZvIn+dg='
    auth_user_116.last_login = datetime.datetime(2013, 9, 16, 20, 58, 17)
    auth_user_116.is_superuser = False
    auth_user_116.username = u'That Lighting Guy'
    auth_user_116.first_name = u''
    auth_user_116.last_name = u''
    auth_user_116.email = u''
    auth_user_116.is_staff = False
    auth_user_116.is_active = True
    auth_user_116.date_joined = datetime.datetime(2013, 9, 16, 20, 58, 17)
    auth_user_116 = importer.save_or_locate(auth_user_116)

    auth_user_117 = User()
    auth_user_117.password = u'pbkdf2_sha256$10000$NQZbMV8w1Fr2$XUKc13s1mCNR4qAbERae9Fm4YyetrrbTuNDOLzK7F9M='
    auth_user_117.last_login = datetime.datetime(2013, 9, 17, 2, 51, 30)
    auth_user_117.is_superuser = False
    auth_user_117.username = u'blritsema'
    auth_user_117.first_name = u''
    auth_user_117.last_name = u''
    auth_user_117.email = u''
    auth_user_117.is_staff = False
    auth_user_117.is_active = True
    auth_user_117.date_joined = datetime.datetime(2013, 9, 17, 2, 51, 30)
    auth_user_117 = importer.save_or_locate(auth_user_117)

    auth_user_118 = User()
    auth_user_118.password = u'pbkdf2_sha256$10000$9G6J0ytCpusX$O2qflim3QR/z34xNssx5H6+nnKovOyam4n4xYKqvuvk='
    auth_user_118.last_login = datetime.datetime(2013, 9, 17, 4, 8, 53)
    auth_user_118.is_superuser = False
    auth_user_118.username = u'Texas Red'
    auth_user_118.first_name = u''
    auth_user_118.last_name = u''
    auth_user_118.email = u''
    auth_user_118.is_staff = False
    auth_user_118.is_active = True
    auth_user_118.date_joined = datetime.datetime(2013, 9, 17, 4, 8, 53)
    auth_user_118 = importer.save_or_locate(auth_user_118)

    auth_user_119 = User()
    auth_user_119.password = u'pbkdf2_sha256$10000$1zjshhqgefXB$4sFo7gh1J5sx2GprhA8d6qdGJCXRNQxjU+evZWd4fDE='
    auth_user_119.last_login = datetime.datetime(2013, 9, 17, 15, 1, 53)
    auth_user_119.is_superuser = False
    auth_user_119.username = u'JMosthaf'
    auth_user_119.first_name = u''
    auth_user_119.last_name = u''
    auth_user_119.email = u''
    auth_user_119.is_staff = False
    auth_user_119.is_active = True
    auth_user_119.date_joined = datetime.datetime(2013, 9, 17, 15, 1, 53)
    auth_user_119 = importer.save_or_locate(auth_user_119)

    auth_user_120 = User()
    auth_user_120.password = u'pbkdf2_sha256$10000$e9bTLuNMmJU6$/oywcnIGSERyeCp2SswAbfmnbYYbKnDvHiYD0jr7HhY='
    auth_user_120.last_login = datetime.datetime(2013, 9, 17, 15, 37, 50)
    auth_user_120.is_superuser = False
    auth_user_120.username = u'Togerah'
    auth_user_120.first_name = u''
    auth_user_120.last_name = u''
    auth_user_120.email = u''
    auth_user_120.is_staff = False
    auth_user_120.is_active = True
    auth_user_120.date_joined = datetime.datetime(2013, 9, 17, 15, 37, 50)
    auth_user_120 = importer.save_or_locate(auth_user_120)

    auth_user_121 = User()
    auth_user_121.password = u'pbkdf2_sha256$10000$PfMhVLvZlZvP$RioZWIw7euN7Pfq784DMtT2DcciziLdpP8DSQWJFrYo='
    auth_user_121.last_login = datetime.datetime(2013, 9, 17, 18, 28, 45)
    auth_user_121.is_superuser = False
    auth_user_121.username = u'Molehawk'
    auth_user_121.first_name = u''
    auth_user_121.last_name = u''
    auth_user_121.email = u''
    auth_user_121.is_staff = False
    auth_user_121.is_active = True
    auth_user_121.date_joined = datetime.datetime(2013, 9, 17, 18, 28, 45)
    auth_user_121 = importer.save_or_locate(auth_user_121)

    auth_user_122 = User()
    auth_user_122.password = u'pbkdf2_sha256$10000$tMUQOMRzaYNM$IUJaaeRSweLwex8dcB+2i0a6x0LbICujmDcL9JsICDE='
    auth_user_122.last_login = datetime.datetime(2013, 9, 17, 18, 53, 26)
    auth_user_122.is_superuser = False
    auth_user_122.username = u'waxpatriot'
    auth_user_122.first_name = u''
    auth_user_122.last_name = u''
    auth_user_122.email = u''
    auth_user_122.is_staff = False
    auth_user_122.is_active = True
    auth_user_122.date_joined = datetime.datetime(2013, 9, 17, 18, 53, 26)
    auth_user_122 = importer.save_or_locate(auth_user_122)

    auth_user_123 = User()
    auth_user_123.password = u'pbkdf2_sha256$10000$pLAM5KbdMKnY$nZrcGDuYAX5l951ycuv4K6PPP+4pJxAtZyW67aAMW98='
    auth_user_123.last_login = datetime.datetime(2013, 9, 17, 21, 18, 35)
    auth_user_123.is_superuser = False
    auth_user_123.username = u'Sawbones'
    auth_user_123.first_name = u''
    auth_user_123.last_name = u''
    auth_user_123.email = u''
    auth_user_123.is_staff = False
    auth_user_123.is_active = True
    auth_user_123.date_joined = datetime.datetime(2013, 9, 17, 21, 18, 35)
    auth_user_123 = importer.save_or_locate(auth_user_123)

    auth_user_124 = User()
    auth_user_124.password = u'pbkdf2_sha256$10000$aI3VfLw1zc4G$HH4rcBq+bfCb9tUvu7D6+dJPJo/yUZGg/HRAakd2gRs='
    auth_user_124.last_login = datetime.datetime(2013, 9, 17, 22, 16, 37)
    auth_user_124.is_superuser = False
    auth_user_124.username = u'dieside666'
    auth_user_124.first_name = u''
    auth_user_124.last_name = u''
    auth_user_124.email = u''
    auth_user_124.is_staff = False
    auth_user_124.is_active = True
    auth_user_124.date_joined = datetime.datetime(2013, 9, 17, 22, 16, 37)
    auth_user_124 = importer.save_or_locate(auth_user_124)

    auth_user_125 = User()
    auth_user_125.password = u'pbkdf2_sha256$10000$kkPd1Hw8XONz$Turl1iboI0+yR0bJBapxUZE47hafCImSU14VtRb0htQ='
    auth_user_125.last_login = datetime.datetime(2013, 9, 17, 23, 11, 10)
    auth_user_125.is_superuser = False
    auth_user_125.username = u'PoorRichard'
    auth_user_125.first_name = u''
    auth_user_125.last_name = u''
    auth_user_125.email = u''
    auth_user_125.is_staff = False
    auth_user_125.is_active = True
    auth_user_125.date_joined = datetime.datetime(2013, 9, 17, 23, 11, 10)
    auth_user_125 = importer.save_or_locate(auth_user_125)

    auth_user_126 = User()
    auth_user_126.password = u'pbkdf2_sha256$10000$uT0oYWfrHpzs$4R2FolZTygr/pWBrJJpSdn0VMCsSjvYtujwm/Z5rzs4='
    auth_user_126.last_login = datetime.datetime(2013, 9, 18, 4, 8, 13)
    auth_user_126.is_superuser = False
    auth_user_126.username = u'kin0025'
    auth_user_126.first_name = u''
    auth_user_126.last_name = u''
    auth_user_126.email = u''
    auth_user_126.is_staff = False
    auth_user_126.is_active = True
    auth_user_126.date_joined = datetime.datetime(2013, 9, 18, 4, 8, 12)
    auth_user_126 = importer.save_or_locate(auth_user_126)

    auth_user_127 = User()
    auth_user_127.password = u'pbkdf2_sha256$10000$SWJBp0vg4AWh$aDbDme1zscaFGPlupQyjIFXtk8CVB2nvRY0+evCyNLw='
    auth_user_127.last_login = datetime.datetime(2013, 9, 18, 4, 18, 18)
    auth_user_127.is_superuser = False
    auth_user_127.username = u'Pelenor'
    auth_user_127.first_name = u''
    auth_user_127.last_name = u''
    auth_user_127.email = u''
    auth_user_127.is_staff = False
    auth_user_127.is_active = True
    auth_user_127.date_joined = datetime.datetime(2013, 9, 18, 4, 18, 18)
    auth_user_127 = importer.save_or_locate(auth_user_127)

    auth_user_128 = User()
    auth_user_128.password = u'pbkdf2_sha256$10000$naJ5vfhQYoSr$yJX4nzwp3KfyxwGu5ALqPelrjzB3QyV3GayplWcwUbc='
    auth_user_128.last_login = datetime.datetime(2013, 9, 18, 11, 54, 4)
    auth_user_128.is_superuser = False
    auth_user_128.username = u'Hyku'
    auth_user_128.first_name = u''
    auth_user_128.last_name = u''
    auth_user_128.email = u''
    auth_user_128.is_staff = False
    auth_user_128.is_active = True
    auth_user_128.date_joined = datetime.datetime(2013, 9, 18, 11, 54, 4)
    auth_user_128 = importer.save_or_locate(auth_user_128)

    auth_user_129 = User()
    auth_user_129.password = u'pbkdf2_sha256$10000$HMT3vAGyamYa$Haeko6en+yVl3G2I3l+k58h/Gs99lMjH0Zlu2dNq334='
    auth_user_129.last_login = datetime.datetime(2013, 9, 18, 18, 58, 54)
    auth_user_129.is_superuser = False
    auth_user_129.username = u'cyberhedz'
    auth_user_129.first_name = u''
    auth_user_129.last_name = u''
    auth_user_129.email = u''
    auth_user_129.is_staff = False
    auth_user_129.is_active = True
    auth_user_129.date_joined = datetime.datetime(2013, 9, 18, 18, 58, 32)
    auth_user_129 = importer.save_or_locate(auth_user_129)

    auth_user_130 = User()
    auth_user_130.password = u'pbkdf2_sha256$10000$8GBzy9MCQmwv$uKZNyMIDf5dYfAe1eHBejzs9W4rwiILwqTDju7MLBHQ='
    auth_user_130.last_login = datetime.datetime(2013, 9, 19, 14, 19, 31)
    auth_user_130.is_superuser = False
    auth_user_130.username = u'SWRT'
    auth_user_130.first_name = u''
    auth_user_130.last_name = u''
    auth_user_130.email = u''
    auth_user_130.is_staff = False
    auth_user_130.is_active = True
    auth_user_130.date_joined = datetime.datetime(2013, 9, 19, 14, 19, 31)
    auth_user_130 = importer.save_or_locate(auth_user_130)

    auth_user_131 = User()
    auth_user_131.password = u'pbkdf2_sha256$10000$RmYSraFwIn6r$+DtVXki//xvj/r4VXNhtZbC9mEBnwEFk2r/mjVl1Q58='
    auth_user_131.last_login = datetime.datetime(2013, 9, 19, 15, 40, 59)
    auth_user_131.is_superuser = False
    auth_user_131.username = u'Snark'
    auth_user_131.first_name = u''
    auth_user_131.last_name = u''
    auth_user_131.email = u''
    auth_user_131.is_staff = False
    auth_user_131.is_active = True
    auth_user_131.date_joined = datetime.datetime(2013, 9, 19, 15, 40, 59)
    auth_user_131 = importer.save_or_locate(auth_user_131)

    auth_user_132 = User()
    auth_user_132.password = u'pbkdf2_sha256$10000$VgusbRYxwSvE$lmNg7ddblxF1ZZ/pKwdoCZqOaaQxUyg6ZWkfbAIKYiM='
    auth_user_132.last_login = datetime.datetime(2013, 9, 19, 18, 35, 47)
    auth_user_132.is_superuser = False
    auth_user_132.username = u'Death'
    auth_user_132.first_name = u''
    auth_user_132.last_name = u''
    auth_user_132.email = u''
    auth_user_132.is_staff = False
    auth_user_132.is_active = True
    auth_user_132.date_joined = datetime.datetime(2013, 9, 19, 18, 35, 47)
    auth_user_132 = importer.save_or_locate(auth_user_132)

    auth_user_133 = User()
    auth_user_133.password = u'pbkdf2_sha256$10000$S2l0pOSXwS2g$etnLGzxi++tcLTuYxSDQAyNn6xb9fapfAPBpnPMhg8U='
    auth_user_133.last_login = datetime.datetime(2013, 9, 20, 5, 21, 17)
    auth_user_133.is_superuser = False
    auth_user_133.username = u'evavictoria'
    auth_user_133.first_name = u''
    auth_user_133.last_name = u''
    auth_user_133.email = u''
    auth_user_133.is_staff = False
    auth_user_133.is_active = True
    auth_user_133.date_joined = datetime.datetime(2013, 9, 20, 3, 45, 17)
    auth_user_133 = importer.save_or_locate(auth_user_133)

    auth_user_134 = User()
    auth_user_134.password = u'pbkdf2_sha256$10000$QQPsZjH4yUCO$bkyRJEYhRdpGwLfy6c/V7rOOI+n1g5IkB36RHgoHzsI='
    auth_user_134.last_login = datetime.datetime(2013, 9, 21, 11, 11, 33)
    auth_user_134.is_superuser = False
    auth_user_134.username = u'markotb'
    auth_user_134.first_name = u''
    auth_user_134.last_name = u''
    auth_user_134.email = u''
    auth_user_134.is_staff = False
    auth_user_134.is_active = True
    auth_user_134.date_joined = datetime.datetime(2013, 9, 21, 11, 11, 33)
    auth_user_134 = importer.save_or_locate(auth_user_134)

    auth_user_135 = User()
    auth_user_135.password = u'pbkdf2_sha256$10000$sdyVUEjrYZ2p$lwXSQHmz58Ho0c+IOx08gN7L0Umbg5R/FvViJtWjJWk='
    auth_user_135.last_login = datetime.datetime(2013, 9, 21, 16, 31, 1)
    auth_user_135.is_superuser = False
    auth_user_135.username = u'Ironhawk'
    auth_user_135.first_name = u''
    auth_user_135.last_name = u''
    auth_user_135.email = u''
    auth_user_135.is_staff = False
    auth_user_135.is_active = True
    auth_user_135.date_joined = datetime.datetime(2013, 9, 21, 16, 31, 1)
    auth_user_135 = importer.save_or_locate(auth_user_135)

    auth_user_136 = User()
    auth_user_136.password = u'pbkdf2_sha256$10000$2CPXudSYJt6A$9gIa3D07cAb9QK5HH8adyMgP6B9HhPPVYxceVpRa5ZU='
    auth_user_136.last_login = datetime.datetime(2013, 9, 21, 18, 12, 25)
    auth_user_136.is_superuser = False
    auth_user_136.username = u'DrOwnz'
    auth_user_136.first_name = u''
    auth_user_136.last_name = u''
    auth_user_136.email = u''
    auth_user_136.is_staff = False
    auth_user_136.is_active = True
    auth_user_136.date_joined = datetime.datetime(2013, 9, 21, 18, 12, 25)
    auth_user_136 = importer.save_or_locate(auth_user_136)

    #Processing model: Session

    from django.contrib.sessions.models import Session

    django_session_1 = Session()
    django_session_1.session_key = u'005inc29naybfj35fbve1jcy1ppacwpr'
    django_session_1.session_data = u'MjYwMmZhMGRlNTQxNjY1NDFlZjE1MGQ1M2JjNjYyNGE1OWY3OTNhNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATl1Lg=='
    django_session_1.expire_date = datetime.datetime(2013, 9, 27, 4, 24, 43)
    django_session_1 = importer.save_or_locate(django_session_1)

    django_session_2 = Session()
    django_session_2.session_key = u'02loky3x5ijyerj68dvbjydl6jlxhhuy'
    django_session_2.session_data = u'Nzk2OWI1NTQyM2RmYmE1MWE5YjAwMDJiZGVhYzE0Nzg4MTcwZTA5YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoYAdS4='
    django_session_2.expire_date = datetime.datetime(2013, 10, 5, 11, 11, 33)
    django_session_2 = importer.save_or_locate(django_session_2)

    django_session_3 = Session()
    django_session_3.session_key = u'09htfyqfgiu8yvdupp83ifxfv9ns62yi'
    django_session_3.session_data = u'MWQ4NWE1YzIzZDEzOTQ5ZDc0Mzg2YTFjNjgxY2QyOTc3ZGRiZWNkZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAS51Lg=='
    django_session_3.expire_date = datetime.datetime(2013, 9, 27, 1, 4, 32)
    django_session_3 = importer.save_or_locate(django_session_3)

    django_session_4 = Session()
    django_session_4.session_key = u'0lkv4glsp7vub6pzjulr5tkbjwlfvfnz'
    django_session_4.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_4.expire_date = datetime.datetime(2013, 9, 21, 20, 51, 53)
    django_session_4 = importer.save_or_locate(django_session_4)

    django_session_5 = Session()
    django_session_5.session_key = u'0vvuwhpdmtr9yuyoeucnx4a5pb8x6crk'
    django_session_5.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_5.expire_date = datetime.datetime(2013, 9, 27, 2, 21, 45)
    django_session_5 = importer.save_or_locate(django_session_5)

    django_session_6 = Session()
    django_session_6.session_key = u'17gig1fjkacpshg5h1kl2k9emm81wbct'
    django_session_6.session_data = u'ZTlhZTVlNGE0ZGExMGYxYzQ0ZmEzYjljOTcwNzI2MTFhYmU1MzU3NTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWp1Lg=='
    django_session_6.expire_date = datetime.datetime(2013, 9, 29, 18, 56, 7)
    django_session_6 = importer.save_or_locate(django_session_6)

    django_session_7 = Session()
    django_session_7.session_key = u'19fdkvht0vj3p78oap985s5c2emmukzq'
    django_session_7.session_data = u'OTQ5N2U3ZjMwNjY0YWEzZTBhYzJhYmZkMWQ5OTc5N2RiYjg2YzJiYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAT91Lg=='
    django_session_7.expire_date = datetime.datetime(2013, 9, 27, 6, 58, 41)
    django_session_7 = importer.save_or_locate(django_session_7)

    django_session_8 = Session()
    django_session_8.session_key = u'1bf1nsyegcs7cw4v7h27yfqxndvo6epz'
    django_session_8.session_data = u'MzZiMjEwYTAyYTIzNDU0YmIzN2MzMWY4YzJhZDVmNThiMDAxNGQwZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWJ1Lg=='
    django_session_8.expire_date = datetime.datetime(2013, 9, 29, 1, 20, 43)
    django_session_8 = importer.save_or_locate(django_session_8)

    django_session_9 = Session()
    django_session_9.session_key = u'2f57zqu33c75ivqjugg9kj9vepi6d6yg'
    django_session_9.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_9.expire_date = datetime.datetime(2013, 9, 28, 17, 55, 21)
    django_session_9 = importer.save_or_locate(django_session_9)

    django_session_10 = Session()
    django_session_10.session_key = u'2ft4fe6pgyczvr5efs7j9pcbi00uymvt'
    django_session_10.session_data = u'ZGFjNGFiZjc5NThlYzYyZDhkNmVlOWRjZGMzNWUyNzJjZGU4MzAwYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASB1Lg=='
    django_session_10.expire_date = datetime.datetime(2013, 9, 26, 22, 12, 21)
    django_session_10 = importer.save_or_locate(django_session_10)

    django_session_11 = Session()
    django_session_11.session_key = u'2gvscuq0pw4g1nmzpvl48898ym2psuoj'
    django_session_11.session_data = u'ZjFmMjMzZDA2OWFhOGYxZDUyZjJjZjNiZTllMWU2NWU0OWJlMjhlMzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAV11Lg=='
    django_session_11.expire_date = datetime.datetime(2013, 9, 28, 20, 22, 11)
    django_session_11 = importer.save_or_locate(django_session_11)

    django_session_12 = Session()
    django_session_12.session_key = u'2h0ok53wp9fb6nbxfp0xu773tqj6gdlq'
    django_session_12.session_data = u'ZDlmMDZmZGMwMTA0OTYxZTE0YmNlMGE2NDYyMjBmOWYzOGFmODAyNTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXp1Lg=='
    django_session_12.expire_date = datetime.datetime(2013, 10, 1, 18, 53, 26)
    django_session_12 = importer.save_or_locate(django_session_12)

    django_session_13 = Session()
    django_session_13.session_key = u'2llbj2b4yapgzwaxz0rxolvo5b1dyc1s'
    django_session_13.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_13.expire_date = datetime.datetime(2013, 9, 22, 1, 23, 23)
    django_session_13 = importer.save_or_locate(django_session_13)

    django_session_14 = Session()
    django_session_14.session_key = u'30a6w8gqz3afyk9avmhr6o9k3wyip45e'
    django_session_14.session_data = u'N2JkMDcxNWIxZjkyZDQwYWI5ZWE3NGFjY2Q1NTlkNTUzY2QyNWE4YTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASF1Lg=='
    django_session_14.expire_date = datetime.datetime(2013, 9, 26, 22, 44, 13)
    django_session_14 = importer.save_or_locate(django_session_14)

    django_session_15 = Session()
    django_session_15.session_key = u'30oypm93sj7e8x2yng0uopn9apduzj5d'
    django_session_15.session_data = u'ZWU2NjEzNjhlZTZhYmJhMjUwYTlkMDA0ZDVmYTQ2MGFlMWYzODU2ZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAS11Lg=='
    django_session_15.expire_date = datetime.datetime(2013, 9, 26, 23, 50, 36)
    django_session_15 = importer.save_or_locate(django_session_15)

    django_session_16 = Session()
    django_session_16.session_key = u'3476db9hvglvdxi1v4hvfus7oqa5zpd0'
    django_session_16.session_data = u'ODFhMjQ1YmZmMTlhZDViMDE1YjA3YjJhMTU2ZGNlNmM5Yjk3YzAyMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASp1Lg=='
    django_session_16.expire_date = datetime.datetime(2013, 9, 26, 23, 23, 11)
    django_session_16 = importer.save_or_locate(django_session_16)

    django_session_17 = Session()
    django_session_17.session_key = u'35ckizcfmm88gm5mw5ss7aogex3q88fm'
    django_session_17.session_data = u'ODVlODNkOWZiYzE5ZjYyMWEzMGViZTk2ODNjZWRlNzIzODcyYzFkYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAX51Lg=='
    django_session_17.expire_date = datetime.datetime(2013, 10, 2, 4, 8, 13)
    django_session_17 = importer.save_or_locate(django_session_17)

    django_session_18 = Session()
    django_session_18.session_key = u'3czli24j43i93y06qogj9exfp6epcpw0'
    django_session_18.session_data = u'OWVjNWQxYzJiNTRjMTdlMTFkNmZjMmY1ZTY0MmNhNzFmMDVmMmRkZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARx1Lg=='
    django_session_18.expire_date = datetime.datetime(2013, 9, 26, 21, 51, 35)
    django_session_18 = importer.save_or_locate(django_session_18)

    django_session_19 = Session()
    django_session_19.session_key = u'3faob5ghi62ggs7j6vmkcp8lldbfm3s4'
    django_session_19.session_data = u'ZDc4YjU2OTc2MjJhYWFhOTlkMWNlZmQzODgzYTE1YjRkNjFhYThmNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARB1Lg=='
    django_session_19.expire_date = datetime.datetime(2013, 9, 24, 2, 21, 52)
    django_session_19 = importer.save_or_locate(django_session_19)

    django_session_20 = Session()
    django_session_20.session_key = u'3zubo8t4vv8iskq7yp10h7ivu4s6bln7'
    django_session_20.session_data = u'N2JkMDcxNWIxZjkyZDQwYWI5ZWE3NGFjY2Q1NTlkNTUzY2QyNWE4YTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASF1Lg=='
    django_session_20.expire_date = datetime.datetime(2013, 9, 26, 22, 13, 6)
    django_session_20 = importer.save_or_locate(django_session_20)

    django_session_21 = Session()
    django_session_21.session_key = u'40efvlcg6m3sowjmhrem6qc5d1570jys'
    django_session_21.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_21.expire_date = datetime.datetime(2013, 9, 21, 22, 30, 17)
    django_session_21 = importer.save_or_locate(django_session_21)

    django_session_22 = Session()
    django_session_22.session_key = u'4gpet5ilcskg3ng8nqzbj66u7wsrwupy'
    django_session_22.session_data = u'MDg3OTJhY2U4OTUzYTJjNjg0MmNiYzNmZDg5NDFjNjM4MzA4YmZjZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARJ1Lg=='
    django_session_22.expire_date = datetime.datetime(2013, 9, 25, 11, 0)
    django_session_22 = importer.save_or_locate(django_session_22)

    django_session_23 = Session()
    django_session_23.session_key = u'4hplif0h3lol7kxsqkokoya7mm7g93e1'
    django_session_23.session_data = u'MWI3NWMwNjk0NGQ5ZWZhYTY1YmI2MDI4Yzk1YjBhYTUwZjIzNDZiYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQZ1Lg=='
    django_session_23.expire_date = datetime.datetime(2013, 9, 21, 14, 21, 42)
    django_session_23 = importer.save_or_locate(django_session_23)

    django_session_24 = Session()
    django_session_24.session_key = u'4obu2s9ewkasdkizexsy37ttgz89x9kz'
    django_session_24.session_data = u'ZDEzZDJiMzgyOTQ0MDA4Yzc3Mjg2YTI1MGFjN2Y0MDA0NDRlMTNjZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVF1Lg=='
    django_session_24.expire_date = datetime.datetime(2013, 9, 27, 18, 54, 16)
    django_session_24 = importer.save_or_locate(django_session_24)

    django_session_25 = Session()
    django_session_25.session_key = u'4v21bsva1i7tro2yihsputciu8no019i'
    django_session_25.session_data = u'NjYxNjkwODAyMTAyM2ZiNTVlYjYyYzI1OTcyY2JkYWNjYTNhYzA4MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVt1Lg=='
    django_session_25.expire_date = datetime.datetime(2013, 9, 28, 14, 11, 43)
    django_session_25 = importer.save_or_locate(django_session_25)

    django_session_26 = Session()
    django_session_26.session_key = u'4ylzlps24fz1codrnyx2uhm781gpr63b'
    django_session_26.session_data = u'NGFjN2EyOTU4NmQ2ZmMxYjkxMjA4MGFlZDNlZDYzZDU3M2ExYWU4NDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARR1Lg=='
    django_session_26.expire_date = datetime.datetime(2013, 9, 25, 23, 41, 51)
    django_session_26 = importer.save_or_locate(django_session_26)

    django_session_27 = Session()
    django_session_27.session_key = u'53w1tfux1a9xaxba0t4e5a99qymep3hs'
    django_session_27.session_data = u'ODg2NzU0YzU2YTRiMjVkMmE4MDg1NzVlOWJjNjBjODI3MjAxNjZhZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAR51Lg=='
    django_session_27.expire_date = datetime.datetime(2013, 9, 26, 22, 2, 8)
    django_session_27 = importer.save_or_locate(django_session_27)

    django_session_28 = Session()
    django_session_28.session_key = u'5pqsaywc4r3rmjizrh2g2hzqsjj4ecap'
    django_session_28.session_data = u'MzU5NGI5NmY5YzVkYjM0NzAwYTNmOTJjNTFlMjNiMTQzOWQ1NDZmMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUB1Lg=='
    django_session_28.expire_date = datetime.datetime(2013, 9, 27, 8, 21, 58)
    django_session_28 = importer.save_or_locate(django_session_28)

    django_session_29 = Session()
    django_session_29.session_key = u'5urm0oa7lna8j0vz2qyuae8nmp9o2w0o'
    django_session_29.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_29.expire_date = datetime.datetime(2013, 9, 25, 20, 25, 57)
    django_session_29 = importer.save_or_locate(django_session_29)

    django_session_30 = Session()
    django_session_30.session_key = u'628eg4h88wec0f5wq1mwroqoexwrhpvh'
    django_session_30.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_30.expire_date = datetime.datetime(2013, 9, 27, 16, 47, 57)
    django_session_30 = importer.save_or_locate(django_session_30)

    django_session_31 = Session()
    django_session_31.session_key = u'66cjoqpn5jocr95fr3wajv6zu8usy3qp'
    django_session_31.session_data = u'MmU2MmE3NDQ4YTEzZGFiYzJkNGZlNGUwOGQ5OGEwNGY0MTgxZmZlZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXh1Lg=='
    django_session_31.expire_date = datetime.datetime(2013, 10, 1, 15, 37, 50)
    django_session_31 = importer.save_or_locate(django_session_31)

    django_session_32 = Session()
    django_session_32.session_key = u'6l00glhx7r8en6c76dqqgxepu3bwjz2c'
    django_session_32.session_data = u'OWVhMmNlZmYzZWRiNzc0Yzk1MWFiY2M4Njc2ZWM4ZDFjMTA2ZjcyZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVN1Lg=='
    django_session_32.expire_date = datetime.datetime(2013, 9, 27, 22, 51, 4)
    django_session_32 = importer.save_or_locate(django_session_32)

    django_session_33 = Session()
    django_session_33.session_key = u'6l2fsk9huut5mzco14rqsj6icwa589iy'
    django_session_33.session_data = u'N2U4ZWVmMWQ4N2NhZTBjMDM2NGNjYTQ0YzY2M2FlOTg0MzgxZjA3MDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATR1Lg=='
    django_session_33.expire_date = datetime.datetime(2013, 9, 27, 2, 43, 43)
    django_session_33 = importer.save_or_locate(django_session_33)

    django_session_34 = Session()
    django_session_34.session_key = u'6msanvxepeed9zqzszh6x2qx3e1udqa1'
    django_session_34.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_34.expire_date = datetime.datetime(2013, 9, 27, 15, 48, 59)
    django_session_34 = importer.save_or_locate(django_session_34)

    django_session_35 = Session()
    django_session_35.session_key = u'6nuxzhebim8pquj4pwg26ccdtrblibph'
    django_session_35.session_data = u'ZGQ5YjFjMjdhOWZiMzg5NmU5MmIxMTYwZmI0ZDJhZmM5MDY4ZmY3ZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg=='
    django_session_35.expire_date = datetime.datetime(2013, 9, 21, 4, 26, 29)
    django_session_35 = importer.save_or_locate(django_session_35)

    django_session_36 = Session()
    django_session_36.session_key = u'6usmalijzc3smcoy5b4jbt572yax8bq1'
    django_session_36.session_data = u'YmQzMzFkMDUxNmI2Zjk4YjNhM2I2MDExNDRlYmYxNjJiMjI5MjNlYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXJ1Lg=='
    django_session_36.expire_date = datetime.datetime(2013, 9, 30, 16, 31, 26)
    django_session_36 = importer.save_or_locate(django_session_36)

    django_session_37 = Session()
    django_session_37.session_key = u'6wal4wsbtxzx2v9epx4kkvfl3nbglezl'
    django_session_37.session_data = u'MzA0ZWRjNTgwZDZjMzEyZjhhMGYwNzAwNTg0ZWYzMDdmNWUxYWZmMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAR11Lg=='
    django_session_37.expire_date = datetime.datetime(2013, 9, 26, 22, 2, 2)
    django_session_37 = importer.save_or_locate(django_session_37)

    django_session_38 = Session()
    django_session_38.session_key = u'7bqd7i8wfqv2cseubm4wxkna6h9y0pug'
    django_session_38.session_data = u'YTQ4ZTQ5MGFjNzg3NTRlMWJjZTljMDY4NzUyM2RkYjliZGY0Y2EwNDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVR1Lg=='
    django_session_38.expire_date = datetime.datetime(2013, 9, 27, 23, 30, 7)
    django_session_38 = importer.save_or_locate(django_session_38)

    django_session_39 = Session()
    django_session_39.session_key = u'7h18db4q4yicligk9m6gc203hjvdseho'
    django_session_39.session_data = u'NTA2MjIwNGRjOWUwYjc0NzAyZDJhMmI2MDlhM2RjN2JmY2JmMWIxYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVV1Lg=='
    django_session_39.expire_date = datetime.datetime(2013, 9, 28, 0, 42, 55)
    django_session_39 = importer.save_or_locate(django_session_39)

    django_session_40 = Session()
    django_session_40.session_key = u'7k1chgem20pedl9rlx4sz5ldx4px0rb5'
    django_session_40.session_data = u'NDE2MDhjMmNkNTc5OWM0YjQ1NzQyY2I0NWU0NmY5ZGYyNjdhMmEyOTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWd1Lg=='
    django_session_40.expire_date = datetime.datetime(2013, 9, 29, 14, 20, 26)
    django_session_40 = importer.save_or_locate(django_session_40)

    django_session_41 = Session()
    django_session_41.session_key = u'7kl77t06yg0jky4779znb6t8izp0m6aw'
    django_session_41.session_data = u'Y2NkNmRiOGYwNjgxNmZlZGRlYjAzMjNmOTI2NmMwZmJjN2JmNWEyMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoMAdS4='
    django_session_41.expire_date = datetime.datetime(2013, 10, 3, 15, 40, 59)
    django_session_41 = importer.save_or_locate(django_session_41)

    django_session_42 = Session()
    django_session_42.session_key = u'7zu6638gpfvg3uync0krfag9c3in9hma'
    django_session_42.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_42.expire_date = datetime.datetime(2013, 9, 29, 17, 59, 37)
    django_session_42 = importer.save_or_locate(django_session_42)

    django_session_43 = Session()
    django_session_43.session_key = u'81ay04d9u0quipp7rmivqoqi72ambmfe'
    django_session_43.session_data = u'ZGQ5YjFjMjdhOWZiMzg5NmU5MmIxMTYwZmI0ZDJhZmM5MDY4ZmY3ZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg=='
    django_session_43.expire_date = datetime.datetime(2013, 9, 26, 21, 44, 49)
    django_session_43 = importer.save_or_locate(django_session_43)

    django_session_44 = Session()
    django_session_44.session_key = u'8jwluilotzld80g23asa2pf97euu0byg'
    django_session_44.session_data = u'NWQzY2Y4MmVjZjg0ZGIzNTQwYzcyMTk5MzVlMTNjNTUxZTI3YTY4MjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASd1Lg=='
    django_session_44.expire_date = datetime.datetime(2013, 9, 26, 22, 59, 39)
    django_session_44 = importer.save_or_locate(django_session_44)

    django_session_45 = Session()
    django_session_45.session_key = u'8nnil7jpi0gix91wdm2az157qdrfwgmj'
    django_session_45.session_data = u'ZTU2NGE1YmZhZjA4M2YxMDM2ZmI5MGY0MmU5OGFmYjQyZTNjM2YyMzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWR1Lg=='
    django_session_45.expire_date = datetime.datetime(2013, 9, 29, 7, 38, 22)
    django_session_45 = importer.save_or_locate(django_session_45)

    django_session_46 = Session()
    django_session_46.session_key = u'8p9l1ujfislne26qdgh7gsnv9e7t35al'
    django_session_46.session_data = u'Zjk1N2M1MjgyNGI1YTQ5MmZhY2Q4YzM0ZjQ4NzljODY3YzkxZTdjMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXV1Lg=='
    django_session_46.expire_date = datetime.datetime(2013, 10, 1, 2, 51, 30)
    django_session_46 = importer.save_or_locate(django_session_46)

    django_session_47 = Session()
    django_session_47.session_key = u'8rsb3kph6f14283o2c6q59r2xuj3yuw6'
    django_session_47.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_47.expire_date = datetime.datetime(2013, 9, 28, 15, 36, 39)
    django_session_47 = importer.save_or_locate(django_session_47)

    django_session_48 = Session()
    django_session_48.session_key = u'943qcifxxhw7ghwirym5upl5ylb2t2pa'
    django_session_48.session_data = u'OGFlY2U3ZjcwYWVkMDZjZTQ1ZTRlNzc0Zjk4OTI5MGZkY2M1ZDI2NDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASt1Lg=='
    django_session_48.expire_date = datetime.datetime(2013, 9, 26, 23, 35, 49)
    django_session_48 = importer.save_or_locate(django_session_48)

    django_session_49 = Session()
    django_session_49.session_key = u'a53ra3mt2q3v1ze6vjp3sg3hn15lywev'
    django_session_49.session_data = u'YThiN2E5OWRlODIwNWI5YWFiMjYyODQxMGE0MWRmMWZhZWM1OWE3NzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUp1Lg=='
    django_session_49.expire_date = datetime.datetime(2013, 9, 27, 14, 57, 4)
    django_session_49 = importer.save_or_locate(django_session_49)

    django_session_50 = Session()
    django_session_50.session_key = u'akv7dl2fjnox7a102aao9iz2qu0ky7z5'
    django_session_50.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_50.expire_date = datetime.datetime(2013, 9, 25, 19, 25, 26)
    django_session_50 = importer.save_or_locate(django_session_50)

    django_session_51 = Session()
    django_session_51.session_key = u'bcy0p339iwk59uywju3hr83zg47woudc'
    django_session_51.session_data = u'MjQ3MGI1MDlhMjY1YzZiYmVhNjhiMjA3YTQzZGFhZTFiMGRkNGZkNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASR1Lg=='
    django_session_51.expire_date = datetime.datetime(2013, 9, 26, 22, 42, 32)
    django_session_51 = importer.save_or_locate(django_session_51)

    django_session_52 = Session()
    django_session_52.session_key = u'be4v87596rlf0j3hlrsrlf1oinf1mlsu'
    django_session_52.session_data = u'YTM3Nzk4ZDcyZjllZDFkMjk5YTAzNjQyOTkzN2NkNTMyYmZhYTQ3NDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWx1Lg=='
    django_session_52.expire_date = datetime.datetime(2013, 9, 29, 21, 33, 38)
    django_session_52 = importer.save_or_locate(django_session_52)

    django_session_53 = Session()
    django_session_53.session_key = u'brg3jgvlolpp40i5243v8okw6btmkmme'
    django_session_53.session_data = u'MjQzMzQ3NDFkM2ZkOTQxNjgxYTRlZWExMDZhZDFjNTI1OWExMDgyMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUl1Lg=='
    django_session_53.expire_date = datetime.datetime(2013, 9, 27, 14, 55, 43)
    django_session_53 = importer.save_or_locate(django_session_53)

    django_session_54 = Session()
    django_session_54.session_key = u'c0knggfkup3h2bwhyhsgcqv0tubu8ku8'
    django_session_54.session_data = u'ODAxYjU2ZTkzOWEwODI5ZWQ2NmQxYWQzY2EwNzJlNWE1MWM0NGIxMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASl1Lg=='
    django_session_54.expire_date = datetime.datetime(2013, 9, 26, 23, 23, 4)
    django_session_54 = importer.save_or_locate(django_session_54)

    django_session_55 = Session()
    django_session_55.session_key = u'c6nf6vdn9o2mkig2zwccakb2bg1bknav'
    django_session_55.session_data = u'OGM2NDVjZjRiMDA2MWM1NDcxOGQyNGI5MjIyNWFhZGNhNWQ0Zjc3ZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASV1Lg=='
    django_session_55.expire_date = datetime.datetime(2013, 9, 26, 22, 54, 9)
    django_session_55 = importer.save_or_locate(django_session_55)

    django_session_56 = Session()
    django_session_56.session_key = u'c892c2m03tb5uzryowrzzokizoybvjct'
    django_session_56.session_data = u'MDJlZTg4MzZiM2Q2YWI4NzI3ZTI1ZTFmYzBjZGNiYTQyZTJhN2I5YzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUx1Lg=='
    django_session_56.expire_date = datetime.datetime(2013, 9, 27, 15, 4, 44)
    django_session_56 = importer.save_or_locate(django_session_56)

    django_session_57 = Session()
    django_session_57.session_key = u'cnv76nfdh0cflymgg905o8uxr39cpilj'
    django_session_57.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_57.expire_date = datetime.datetime(2013, 9, 27, 6, 11, 38)
    django_session_57 = importer.save_or_locate(django_session_57)

    django_session_58 = Session()
    django_session_58.session_key = u'd1fqyc6r5x00u2hc8l0thf9g6kj5u0fr'
    django_session_58.session_data = u'MmE5MTJjN2JiNjFhYjlhYzYwOThkYzM3MmZjZDFkYTI4Nzc4NTI1YTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUN1Lg=='
    django_session_58.expire_date = datetime.datetime(2013, 9, 27, 9, 47, 57)
    django_session_58 = importer.save_or_locate(django_session_58)

    django_session_59 = Session()
    django_session_59.session_key = u'd3ei95nyx4372ssv81n38goatuytzpnb'
    django_session_59.session_data = u'NzFkNGFmNjkyNzM0NmFmNzQ2YTA4ZGZkZmUyY2RjMzk1ZGMxMGQyMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUh1Lg=='
    django_session_59.expire_date = datetime.datetime(2013, 9, 27, 13, 34, 4)
    django_session_59 = importer.save_or_locate(django_session_59)

    django_session_60 = Session()
    django_session_60.session_key = u'd5n3hqhi8gdqc1sftgnjgmp4djlt6lzt'
    django_session_60.session_data = u'ZTA2NjliODExN2YyNWZiYjA4OWMzMWM4NjQ0MjYwNzU5ZGU1ZDZkYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAU91Lg=='
    django_session_60.expire_date = datetime.datetime(2013, 9, 27, 17, 45, 19)
    django_session_60 = importer.save_or_locate(django_session_60)

    django_session_61 = Session()
    django_session_61.session_key = u'dibh5ala8d25xqh9oakxb5cz1x3uo475'
    django_session_61.session_data = u'NjQ2NTQ3YzA1MjQyNTEyZTA3YjlkOGQwZjdhZjdmMDc2ZTljYzE4NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQh1Lg=='
    django_session_61.expire_date = datetime.datetime(2013, 9, 21, 19, 11, 47)
    django_session_61 = importer.save_or_locate(django_session_61)

    django_session_62 = Session()
    django_session_62.session_key = u'dui9p04gjcr1x32x1e8olr13tjrpn3z3'
    django_session_62.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_62.expire_date = datetime.datetime(2013, 10, 1, 18, 39, 25)
    django_session_62 = importer.save_or_locate(django_session_62)

    django_session_63 = Session()
    django_session_63.session_key = u'e79f36gkb1258wer044zcfvtvkeervd4'
    django_session_63.session_data = u'M2ZkZmU1ZDAzMmZmM2I5ZWE0YjE2ZDJiNTAxN2RjN2QyYWJhYzJhMzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQd1Lg=='
    django_session_63.expire_date = datetime.datetime(2013, 9, 21, 14, 59, 45)
    django_session_63 = importer.save_or_locate(django_session_63)

    django_session_64 = Session()
    django_session_64.session_key = u'eafxl3b970x3m5h3g7d8jj9adaxmnu34'
    django_session_64.session_data = u'Mjk2NTA2OTU3YjMxZWI5NmNjODI3NTA4MTkyOWY4MGM1MDk2MmNjZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg=='
    django_session_64.expire_date = datetime.datetime(2013, 9, 21, 4, 23, 59)
    django_session_64 = importer.save_or_locate(django_session_64)

    django_session_65 = Session()
    django_session_65.session_key = u'ek1bak27d4sabg99aa8yxbo43tszuj3s'
    django_session_65.session_data = u'ZDBkY2E2ODAyYTI3YzM0NTI4ZGE5MWNmZjQ3NGQwNmFlOTU1ZWM4OTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATp1Lg=='
    django_session_65.expire_date = datetime.datetime(2013, 9, 27, 4, 27, 46)
    django_session_65 = importer.save_or_locate(django_session_65)

    django_session_66 = Session()
    django_session_66.session_key = u'ekcvef1oaa19a2tvvfkidtykd1ks7pt7'
    django_session_66.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_66.expire_date = datetime.datetime(2013, 9, 27, 2, 22, 16)
    django_session_66 = importer.save_or_locate(django_session_66)

    django_session_67 = Session()
    django_session_67.session_key = u'emnriksbr737r2rqo97czvbke8ox7w65'
    django_session_67.session_data = u'MzQ3OTFkM2Y2YmUwMThhMWU3NDAxNTUwZWEwNDgxYTVlMjJkZTFmMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXt1Lg=='
    django_session_67.expire_date = datetime.datetime(2013, 10, 1, 21, 18, 35)
    django_session_67 = importer.save_or_locate(django_session_67)

    django_session_68 = Session()
    django_session_68.session_key = u'eo5ez6cyx3l4iovxzc3qxt6cto1m2yqw'
    django_session_68.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_68.expire_date = datetime.datetime(2013, 9, 22, 21, 24, 20)
    django_session_68 = importer.save_or_locate(django_session_68)

    django_session_69 = Session()
    django_session_69.session_key = u'erncn8lhqg4ac3xv6y8f0xy0vv9l9voh'
    django_session_69.session_data = u'ZDQ5ZjlhNTI3YmVkNTYzNDZmMDM0NWJiNTIwMDU4OTVlZTE3Zjk1MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoUAdS4='
    django_session_69.expire_date = datetime.datetime(2013, 10, 4, 5, 21, 17)
    django_session_69 = importer.save_or_locate(django_session_69)

    django_session_70 = Session()
    django_session_70.session_key = u'et7gd3az9l11fcfpqy7symz744st4hhr'
    django_session_70.session_data = u'MjllMDIxZDJmMDAzMWIwNDI2YWZhMGFjZGU2YmMzMjgzMWQyOTJlNzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARl1Lg=='
    django_session_70.expire_date = datetime.datetime(2013, 9, 26, 21, 23, 48)
    django_session_70 = importer.save_or_locate(django_session_70)

    django_session_71 = Session()
    django_session_71.session_key = u'euwur33drbsqv0uy23bfz00l80lka8rd'
    django_session_71.session_data = u'ODlhNGVmZmU3NzRkNDAwMmM4ZWM3YzNlNWFhMjhkNDhmMmU5MDVjZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWB1Lg=='
    django_session_71.expire_date = datetime.datetime(2013, 9, 28, 23, 28, 14)
    django_session_71 = importer.save_or_locate(django_session_71)

    django_session_72 = Session()
    django_session_72.session_key = u'ew2ucaqh41xqt67rc4eiu595qsgg78ov'
    django_session_72.session_data = u'M2ZkZmU1ZDAzMmZmM2I5ZWE0YjE2ZDJiNTAxN2RjN2QyYWJhYzJhMzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQd1Lg=='
    django_session_72.expire_date = datetime.datetime(2013, 9, 27, 15, 14, 53)
    django_session_72 = importer.save_or_locate(django_session_72)

    django_session_73 = Session()
    django_session_73.session_key = u'f268tp6hiwdo9y7zrynjai9tdx5hhlr2'
    django_session_73.session_data = u'ZWUyY2MxOGFiM2VmMjZhZDdjODYwYTcwNWY5NDkwNjNhZTA2NTQ0MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAT11Lg=='
    django_session_73.expire_date = datetime.datetime(2013, 9, 27, 6, 32, 8)
    django_session_73 = importer.save_or_locate(django_session_73)

    django_session_74 = Session()
    django_session_74.session_key = u'f2tsrzhw4yz4wdkzrfcz1wc09zct1n28'
    django_session_74.session_data = u'MmMxODIxN2E3OGNlZDYyYWM0OWM5YzJlMjFkOGM3NTZiMjMwOGUwZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAW51Lg=='
    django_session_74.expire_date = datetime.datetime(2013, 9, 29, 23, 49, 25)
    django_session_74 = importer.save_or_locate(django_session_74)

    django_session_75 = Session()
    django_session_75.session_key = u'fm2246qzynxau0buwprgu0b1ep5b98l5'
    django_session_75.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_75.expire_date = datetime.datetime(2013, 10, 1, 20, 52, 20)
    django_session_75 = importer.save_or_locate(django_session_75)

    django_session_76 = Session()
    django_session_76.session_key = u'foq915hhoctbas3emukw9axofg2nkl7j'
    django_session_76.session_data = u'NzhmM2Q0ODc5MjQ4ZmRkZTkzMGNlMWNhMmU1ZTg5MTYzYjM4NjBjYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVx1Lg=='
    django_session_76.expire_date = datetime.datetime(2013, 9, 28, 15, 59, 14)
    django_session_76 = importer.save_or_locate(django_session_76)

    django_session_77 = Session()
    django_session_77.session_key = u'fsjxh87an9jvt56rw6qhe7lp3gmqh0vz'
    django_session_77.session_data = u'ZDFlMjk5NzUzN2UzMGM4MjE3ZjFmNTE3MDM4YzQzYzYzMDk5OTM1YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVl1Lg=='
    django_session_77.expire_date = datetime.datetime(2013, 9, 28, 11, 21, 27)
    django_session_77 = importer.save_or_locate(django_session_77)

    django_session_78 = Session()
    django_session_78.session_key = u'g83tefi2qk8dowvvrk68xspek3xspqkl'
    django_session_78.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_78.expire_date = datetime.datetime(2013, 9, 27, 0, 21, 55)
    django_session_78 = importer.save_or_locate(django_session_78)

    django_session_79 = Session()
    django_session_79.session_key = u'gb20idd6mnor2bpdzbd8xwtz2gryp52k'
    django_session_79.session_data = u'YTEwNjI0OTUzMDAyZjNkOTUxOGQzMjYzY2M4OTkxMmI1OTFhNGI2YzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASh1Lg=='
    django_session_79.expire_date = datetime.datetime(2013, 9, 26, 23, 10, 50)
    django_session_79 = importer.save_or_locate(django_session_79)

    django_session_80 = Session()
    django_session_80.session_key = u'gb71jew5xz06mssqvhr8oq9i5vf53c13'
    django_session_80.session_data = u'NTdjNDYwOGEyZTM3NmVjNGQxMDRkYzNlY2VjZWIwMjRlMjVhYThlNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVB1Lg=='
    django_session_80.expire_date = datetime.datetime(2013, 9, 27, 18, 52, 6)
    django_session_80 = importer.save_or_locate(django_session_80)

    django_session_81 = Session()
    django_session_81.session_key = u'gd4kdt0aaprwza9pg8xizwmi76el9vlg'
    django_session_81.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_81.expire_date = datetime.datetime(2013, 9, 22, 16, 35, 38)
    django_session_81 = importer.save_or_locate(django_session_81)

    django_session_82 = Session()
    django_session_82.session_key = u'gk6hyut26xhx2eug37324xgd5ttjqefw'
    django_session_82.session_data = u'NjY2OTg5N2U2ZGYxMTI0ZDE5M2NhMjQ2ZDk0YjYwZGY2MGQ1NGRmMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAU51Lg=='
    django_session_82.expire_date = datetime.datetime(2013, 9, 27, 16, 33, 57)
    django_session_82 = importer.save_or_locate(django_session_82)

    django_session_83 = Session()
    django_session_83.session_key = u'gozwoi00xaeeofm44rrm69pus6zfrdpp'
    django_session_83.session_data = u'MGRmZWEzMjg4MzVlYmE4OWMzMjcwNWYzZmU5Yzk0NzRlZjQxNTMxMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATx1Lg=='
    django_session_83.expire_date = datetime.datetime(2013, 9, 27, 6, 25, 49)
    django_session_83 = importer.save_or_locate(django_session_83)

    django_session_84 = Session()
    django_session_84.session_key = u'gsbcgwmoxj1n16ofpngyuwxd6sv4pc23'
    django_session_84.session_data = u'ODgyOGUwNGI0NWVkNmYxMDBiYTg1YjQxYjFhMDI0OGUwYTcxMDhlNDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAU11Lg=='
    django_session_84.expire_date = datetime.datetime(2013, 9, 27, 15, 31, 14)
    django_session_84 = importer.save_or_locate(django_session_84)

    django_session_85 = Session()
    django_session_85.session_key = u'gsibveg0v78n2vqzac2rp9sncrxscro9'
    django_session_85.session_data = u'YjJmYTFhZDlkMGVhNWRmMjdjNmM5NDgwYTc0YmRlZTEyZWEzZjFkMzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoAAdS4='
    django_session_85.expire_date = datetime.datetime(2013, 10, 2, 11, 54, 4)
    django_session_85 = importer.save_or_locate(django_session_85)

    django_session_86 = Session()
    django_session_86.session_key = u'guc62fpwrvyo1zzp33v46btlxnddducw'
    django_session_86.session_data = u'OGE2NzFkOWNiODljZDhmODUxMzBkMzViMWVlMzUzMTI3ODBkNmI4YzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUZ1Lg=='
    django_session_86.expire_date = datetime.datetime(2013, 9, 27, 12, 8, 38)
    django_session_86 = importer.save_or_locate(django_session_86)

    django_session_87 = Session()
    django_session_87.session_key = u'h157wzozcxv2ho2hsw1l1qpyl3j6zcqx'
    django_session_87.session_data = u'YmFkMzk3Y2VkNDMyNWI0ZDAwMThkMjZmYzhmZWQ5YzFmZjEzYmYwODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARd1Lg=='
    django_session_87.expire_date = datetime.datetime(2013, 9, 26, 21, 10, 25)
    django_session_87 = importer.save_or_locate(django_session_87)

    django_session_88 = Session()
    django_session_88.session_key = u'hdmiccmsd2p7d83805a777e5b7yvhbe9'
    django_session_88.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_88.expire_date = datetime.datetime(2013, 9, 26, 4, 45, 50)
    django_session_88 = importer.save_or_locate(django_session_88)

    django_session_89 = Session()
    django_session_89.session_key = u'hib8i7p0rcvs10sefg4a2a829kca2gby'
    django_session_89.session_data = u'YTI3NTM5ZjhhMzJmZTM0OTUxZjllMWRjNjdiYmQyZTJmNjBiZTQyYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQV1Lg=='
    django_session_89.expire_date = datetime.datetime(2013, 9, 21, 11, 8, 32)
    django_session_89 = importer.save_or_locate(django_session_89)

    django_session_90 = Session()
    django_session_90.session_key = u'hndafit1kaoiwqm38ra1io4at4a15w22'
    django_session_90.session_data = u'ZjI1ZDc5Mzg5NjhkZmVlOTA4OGQ5ZmRiYTc3NGNlYTZlNzlkMGY0NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUd1Lg=='
    django_session_90.expire_date = datetime.datetime(2013, 9, 27, 12, 8, 13)
    django_session_90 = importer.save_or_locate(django_session_90)

    django_session_91 = Session()
    django_session_91.session_key = u'hvvcg9lnbmuzznfq6fitcor5lmdys0vf'
    django_session_91.session_data = u'YzhmOTkxMjc4ZWNkZDIwYjY2NDRhNmNkMjkxNzRjZjY2MTI1ODdlODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATh1Lg=='
    django_session_91.expire_date = datetime.datetime(2013, 9, 27, 3, 27, 56)
    django_session_91 = importer.save_or_locate(django_session_91)

    django_session_92 = Session()
    django_session_92.session_key = u'i5xi41hy9ieaky8g4r5w1jr7b6cb5cel'
    django_session_92.session_data = u'N2UyYWRiOWNmMGNlMjY2ZjZkNmZiNDc3YzEzYzNhMDkxZjNjNThiYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAogAdS4='
    django_session_92.expire_date = datetime.datetime(2013, 10, 5, 18, 12, 25)
    django_session_92 = importer.save_or_locate(django_session_92)

    django_session_93 = Session()
    django_session_93.session_key = u'ill01aayjqp352o6nei3a3q8e7w78b11'
    django_session_93.session_data = u'YWY3YTM3NDJhYzcwMDlkNDQ3MjNhZGM3OGU0YTMxMjY1ZmM4MDJlNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARF1Lg=='
    django_session_93.expire_date = datetime.datetime(2013, 9, 24, 12, 55, 3)
    django_session_93 = importer.save_or_locate(django_session_93)

    django_session_94 = Session()
    django_session_94.session_key = u'imypwspjqhazcd94nyyjtrt5geg1yxd4'
    django_session_94.session_data = u'YWJlOTMyMDllNGJjZjZmMjBjMTExMTk1NTk2ZjY1MGM3Yjg0MGEwMTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUJ1Lg=='
    django_session_94.expire_date = datetime.datetime(2013, 9, 27, 8, 42, 19)
    django_session_94 = importer.save_or_locate(django_session_94)

    django_session_95 = Session()
    django_session_95.session_key = u'ipy30ogiys6q865t9gkdctr0ryaxibf0'
    django_session_95.session_data = u'NDQxYTk1NWRlOTk0MjlmNmZlNTU4ZmQyMWYxYmFmMTE2ZTg3ODY5NDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAV91Lg=='
    django_session_95.expire_date = datetime.datetime(2013, 9, 28, 21, 45, 46)
    django_session_95 = importer.save_or_locate(django_session_95)

    django_session_96 = Session()
    django_session_96.session_key = u'jp02x15xx9bbi17vi6zpd9vtvcls1xow'
    django_session_96.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_96.expire_date = datetime.datetime(2013, 9, 22, 21, 21, 39)
    django_session_96 = importer.save_or_locate(django_session_96)

    django_session_97 = Session()
    django_session_97.session_key = u'jqc5a7ap8vkzmiq3yd0tck6an1kwy4wd'
    django_session_97.session_data = u'YWRhZGY3ZDNlMmViMTgzYWEzOWE0NThjZmU1ZTdlNTkzOTYwZGE4YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQ51Lg=='
    django_session_97.expire_date = datetime.datetime(2013, 9, 23, 23, 49, 27)
    django_session_97 = importer.save_or_locate(django_session_97)

    django_session_98 = Session()
    django_session_98.session_key = u'jsuympsk8jru3ktqrvl5287mgj1fi4vz'
    django_session_98.session_data = u'NjU0YzkwYWY5ZWY0YWJjN2JhZGRhYmE3ZTA4ZDI5N2Q2OTg3YTA0YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXd1Lg=='
    django_session_98.expire_date = datetime.datetime(2013, 10, 1, 15, 1, 53)
    django_session_98 = importer.save_or_locate(django_session_98)

    django_session_99 = Session()
    django_session_99.session_key = u'ju8nz3kyvg36vn16fhgu3nt60l300bq8'
    django_session_99.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_99.expire_date = datetime.datetime(2013, 9, 21, 4, 37, 56)
    django_session_99 = importer.save_or_locate(django_session_99)

    django_session_100 = Session()
    django_session_100.session_key = u'jv76jj4ixn20yr9b0y4o1e47g6m8swg9'
    django_session_100.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_100.expire_date = datetime.datetime(2013, 9, 22, 9, 44, 42)
    django_session_100 = importer.save_or_locate(django_session_100)

    django_session_101 = Session()
    django_session_101.session_key = u'jxinvlktwu05kts3ip0sfrfedwq3moi2'
    django_session_101.session_data = u'ZjI3NGRkZGY1YmM0ODMzZjdjMDM4MmUxOWQyNWYyYjUwY2EwYThkMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXN1Lg=='
    django_session_101.expire_date = datetime.datetime(2013, 9, 30, 17, 38, 17)
    django_session_101 = importer.save_or_locate(django_session_101)

    django_session_102 = Session()
    django_session_102.session_key = u'k0bgzyd9mha7flj8x2457vj3c2yn6d5m'
    django_session_102.session_data = u'NDcwM2U4MmNhMWMxNjU2MzA1YjhjZGIwYTgyYzgyNjJjMTg4YzVkYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQx1Lg=='
    django_session_102.expire_date = datetime.datetime(2013, 9, 22, 23, 57, 30)
    django_session_102 = importer.save_or_locate(django_session_102)

    django_session_103 = Session()
    django_session_103.session_key = u'k16ay3o7xnwmy5dyvoggbrifos2y93qc'
    django_session_103.session_data = u'NzZjYTQ4YTQ0YmUwN2JjMWY0ZGI4MGU0MDYwYmQ3YmQwOWRiMTg5NjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARt1Lg=='
    django_session_103.expire_date = datetime.datetime(2013, 9, 26, 21, 43, 4)
    django_session_103 = importer.save_or_locate(django_session_103)

    django_session_104 = Session()
    django_session_104.session_key = u'k3sr0c0299wc08tch0bcqfrc6jxg1ir8'
    django_session_104.session_data = u'ZDc4NjM3Y2Q4ZTczYmU4ZTMwOTM0ZDU0OWE5NDc1ODlmYTNiMmQ2MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWN1Lg=='
    django_session_104.expire_date = datetime.datetime(2013, 9, 29, 6, 55, 35)
    django_session_104 = importer.save_or_locate(django_session_104)

    django_session_105 = Session()
    django_session_105.session_key = u'k44e1t2zjdmgblwhabbwv47qdq9klurt'
    django_session_105.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_105.expire_date = datetime.datetime(2013, 9, 24, 18, 50, 51)
    django_session_105 = importer.save_or_locate(django_session_105)

    django_session_106 = Session()
    django_session_106.session_key = u'kwo0tkfndhal6424q146qf31wt87d1kl'
    django_session_106.session_data = u'MTkyZmJlZGIxNjFkODRiOGRhMmFiNzNjYTNjOWE0NjI4NDYwNmI4YjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWl1Lg=='
    django_session_106.expire_date = datetime.datetime(2013, 9, 29, 18, 16, 59)
    django_session_106 = importer.save_or_locate(django_session_106)

    django_session_107 = Session()
    django_session_107.session_key = u'l1aoleuj6054l8rcdmlvevf7evus00me'
    django_session_107.session_data = u'ZGRkZDRhNWU1YmIwOWMxZGIwNTQ1OGMxZGRlNjY3Njg0ZTZiZDUwODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAocAdS4='
    django_session_107.expire_date = datetime.datetime(2013, 10, 5, 16, 31, 1)
    django_session_107 = importer.save_or_locate(django_session_107)

    django_session_108 = Session()
    django_session_108.session_key = u'le2s85rasno6beq6z9pm5aixq7yho3wf'
    django_session_108.session_data = u'MjY1ZGEwMWY3NGU3Y2VkMzdmMWZlNTc2YjI3YmFjZDllYjdkZjJiZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoEAdS4='
    django_session_108.expire_date = datetime.datetime(2013, 10, 2, 18, 58, 54)
    django_session_108 = importer.save_or_locate(django_session_108)

    django_session_109 = Session()
    django_session_109.session_key = u'lfr7zg7cpvbnk6xo8sidcmxjnoo0w8ba'
    django_session_109.session_data = u'YmM5YWQyOGQyN2E0ZjI3ODA4ZmI1YzQxYWE5NTE5NzI4YzQ3ODhjYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAR91Lg=='
    django_session_109.expire_date = datetime.datetime(2013, 9, 26, 22, 4, 59)
    django_session_109 = importer.save_or_locate(django_session_109)

    django_session_110 = Session()
    django_session_110.session_key = u'lpuyfq37gnybebjzd0cia0bewj8tnzwj'
    django_session_110.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_110.expire_date = datetime.datetime(2013, 9, 23, 7, 52, 41)
    django_session_110 = importer.save_or_locate(django_session_110)

    django_session_111 = Session()
    django_session_111.session_key = u'lr7eruznkxqnp6bniy5f1a8owhd3vs5n'
    django_session_111.session_data = u'NzdlODc4NzlhMjFkNDJjYjRiYmU1OTE4MDMzZWJiNGYzMjYzZjgxYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQ11Lg=='
    django_session_111.expire_date = datetime.datetime(2013, 9, 23, 2, 53, 13)
    django_session_111 = importer.save_or_locate(django_session_111)

    django_session_112 = Session()
    django_session_112.session_key = u'lv3l10f6ah45elqh7q7d8j3anx768z16'
    django_session_112.session_data = u'YzE4ZTljYTIwOThkYTRiODhmMWQ2NGJmYzc4NjJkNWJhYjllMmExMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARZ1Lg=='
    django_session_112.expire_date = datetime.datetime(2013, 9, 26, 20, 56, 41)
    django_session_112 = importer.save_or_locate(django_session_112)

    django_session_113 = Session()
    django_session_113.session_key = u'm0b9obxfhjta39d4ick7iwv77g4aigcp'
    django_session_113.session_data = u'Zjk0NjM2MmUzZDYzMTY3ZjE0MzVjNTM5Y2FiNzExYzU5Y2MzMWM2ZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASx1Lg=='
    django_session_113.expire_date = datetime.datetime(2013, 9, 26, 23, 44, 19)
    django_session_113 = importer.save_or_locate(django_session_113)

    django_session_114 = Session()
    django_session_114.session_key = u'm2dv03sthhjue74ed2zzn4164yhmvq0f'
    django_session_114.session_data = u'YjI5YzMwZTQ4MDQzYjI3NTRiZGY2MzRlNWQ2Y2I4ZmUyZjRmYTY0MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVZ1Lg=='
    django_session_114.expire_date = datetime.datetime(2013, 9, 28, 1, 27)
    django_session_114 = importer.save_or_locate(django_session_114)

    django_session_115 = Session()
    django_session_115.session_key = u'm3oijrf9dxt66hkutm7iyor386n9scs1'
    django_session_115.session_data = u'MjIxNzE5MWZhNDNiZjBmYjRlMDkwYTIxMGRiZmM4MzZjNjIxNGVmYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVJ1Lg=='
    django_session_115.expire_date = datetime.datetime(2013, 9, 27, 20, 51, 50)
    django_session_115 = importer.save_or_locate(django_session_115)

    django_session_116 = Session()
    django_session_116.session_key = u'm4ro6nw95m3ix4rfxsacwbwr4yjca0dr'
    django_session_116.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_116.expire_date = datetime.datetime(2013, 9, 22, 4, 39, 43)
    django_session_116 = importer.save_or_locate(django_session_116)

    django_session_117 = Session()
    django_session_117.session_key = u'm5mka1v33rt8kx2o36c4znyu19fzxyar'
    django_session_117.session_data = u'NWY3YTkwYTg4YzIzZWFiOGY1ZmQ2Y2RlNjcyOTExNWQyMTgzYTNlMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWV1Lg=='
    django_session_117.expire_date = datetime.datetime(2013, 9, 29, 10, 19, 46)
    django_session_117 = importer.save_or_locate(django_session_117)

    django_session_118 = Session()
    django_session_118.session_key = u'm64357c2bcjn6q1odryg844c2ehdek6n'
    django_session_118.session_data = u'NmZkMzk1ODBmOGMxNGZjZTJiMTY4MDIwY2ZjZTVjNWM2M2EwMDY2MjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARN1Lg=='
    django_session_118.expire_date = datetime.datetime(2013, 9, 25, 15, 6, 28)
    django_session_118 = importer.save_or_locate(django_session_118)

    django_session_119 = Session()
    django_session_119.session_key = u'mf1dt04125rdfdebsqzdjmorv3egvnt0'
    django_session_119.session_data = u'NGIxNjk3NGZhYzMxYzRiNTUxNGY2YmYwNWVjOGJlZDM4MDQ2YTJhZjqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg=='
    django_session_119.expire_date = datetime.datetime(2013, 9, 26, 23, 9, 52)
    django_session_119 = importer.save_or_locate(django_session_119)

    django_session_120 = Session()
    django_session_120.session_key = u'my4e8jcd26qnjco0hsptua279fqavbqg'
    django_session_120.session_data = u'N2U4ZWVmMWQ4N2NhZTBjMDM2NGNjYTQ0YzY2M2FlOTg0MzgxZjA3MDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATR1Lg=='
    django_session_120.expire_date = datetime.datetime(2013, 9, 27, 2, 40, 8)
    django_session_120 = importer.save_or_locate(django_session_120)

    django_session_121 = Session()
    django_session_121.session_key = u'n9uk0jdaq5c50kzifvs3gk836glhjrtn'
    django_session_121.session_data = u'NmNhM2MwZmM1YWJkYmU5NzViZGEyNGM3YTRhM2FlZWViZmU2OTU3MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWh1Lg=='
    django_session_121.expire_date = datetime.datetime(2013, 9, 29, 17, 4, 51)
    django_session_121 = importer.save_or_locate(django_session_121)

    django_session_122 = Session()
    django_session_122.session_key = u'nd6ksewrhrwkxu5ff1zny1opsc4fjqil'
    django_session_122.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_122.expire_date = datetime.datetime(2013, 9, 25, 10, 17, 30)
    django_session_122 = importer.save_or_locate(django_session_122)

    django_session_123 = Session()
    django_session_123.session_key = u'ndcf0j4st4f4b85etnywvt76ar7u8lnw'
    django_session_123.session_data = u'YTBmNGUxZjZjMTY1ZmEyZWZiMDlmY2Y1NTI3OWE4ODExYzdmMTZhMzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXF1Lg=='
    django_session_123.expire_date = datetime.datetime(2013, 9, 30, 9, 35, 57)
    django_session_123 = importer.save_or_locate(django_session_123)

    django_session_124 = Session()
    django_session_124.session_key = u'njqu2vlr7dg6pw2i9x1wjkghr48rp7w4'
    django_session_124.session_data = u'YWIxNWIzZWFiYTc3N2U1YWQ2ZTkyYWIzNTkwZDI0MjA5N2Q1YzRiMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg=='
    django_session_124.expire_date = datetime.datetime(2013, 9, 21, 14, 56, 17)
    django_session_124 = importer.save_or_locate(django_session_124)

    django_session_125 = Session()
    django_session_125.session_key = u'npp2fsd9w0xg23avo47wih6133tkbh49'
    django_session_125.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_125.expire_date = datetime.datetime(2013, 9, 26, 22, 29, 16)
    django_session_125 = importer.save_or_locate(django_session_125)

    django_session_126 = Session()
    django_session_126.session_key = u'nqwu1dntqce8fs6c9p8li53qz6pofg5i'
    django_session_126.session_data = u'ZDYzYzUxZGU2ZGE2ODQ5OTcxNmM2YzdhYjI0ODRmYmVhODc2MzUxMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAX91Lg=='
    django_session_126.expire_date = datetime.datetime(2013, 10, 2, 4, 18, 18)
    django_session_126 = importer.save_or_locate(django_session_126)

    django_session_127 = Session()
    django_session_127.session_key = u'nzchdr3p6fz1a1a9fil46jjjxfhv06k6'
    django_session_127.session_data = u'MjQzMzQ3NDFkM2ZkOTQxNjgxYTRlZWExMDZhZDFjNTI1OWExMDgyMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUl1Lg=='
    django_session_127.expire_date = datetime.datetime(2013, 9, 27, 14, 32, 18)
    django_session_127 = importer.save_or_locate(django_session_127)

    django_session_128 = Session()
    django_session_128.session_key = u'oqf6skxz0wrd7ep7ua9l1u5ecw5qy35i'
    django_session_128.session_data = u'YWIxNWIzZWFiYTc3N2U1YWQ2ZTkyYWIzNTkwZDI0MjA5N2Q1YzRiMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg=='
    django_session_128.expire_date = datetime.datetime(2013, 9, 22, 20, 34, 7)
    django_session_128 = importer.save_or_locate(django_session_128)

    django_session_129 = Session()
    django_session_129.session_key = u'ouzz6btm53lb2yf44r33eha8s2k6ofv2'
    django_session_129.session_data = u'ZDQ5ZjlhNTI3YmVkNTYzNDZmMDM0NWJiNTIwMDU4OTVlZTE3Zjk1MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoUAdS4='
    django_session_129.expire_date = datetime.datetime(2013, 10, 4, 3, 45, 17)
    django_session_129 = importer.save_or_locate(django_session_129)

    django_session_130 = Session()
    django_session_130.session_key = u'owycqty0qixtuhec91r8t9kch4mfqckg'
    django_session_130.session_data = u'Y2JlN2FmZjFmNzc5Nzg1ZmI2Zjg4NWYwMzNiM2Q5NzAzOTI2Y2NhOTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAS91Lg=='
    django_session_130.expire_date = datetime.datetime(2013, 9, 27, 1, 23, 55)
    django_session_130 = importer.save_or_locate(django_session_130)

    django_session_131 = Session()
    django_session_131.session_key = u'oxwx168u8fuunul9ezju50rq8xdez5mo'
    django_session_131.session_data = u'YTViYWRkNmYyNjY4NTdjODk4YzIyNWI2NTE5YTBiMzBhOTY0YzI0ZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATd1Lg=='
    django_session_131.expire_date = datetime.datetime(2013, 9, 27, 3, 8, 17)
    django_session_131 = importer.save_or_locate(django_session_131)

    django_session_132 = Session()
    django_session_132.session_key = u'ozb8wgvirixt70bpbuadgq910geyxua9'
    django_session_132.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_132.expire_date = datetime.datetime(2013, 9, 25, 16, 50, 9)
    django_session_132 = importer.save_or_locate(django_session_132)

    django_session_133 = Session()
    django_session_133.session_key = u'p6lsmhcq5wxbk8i7l1q8plk24gr1njse'
    django_session_133.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_133.expire_date = datetime.datetime(2013, 9, 27, 11, 6, 39)
    django_session_133 = importer.save_or_locate(django_session_133)

    django_session_134 = Session()
    django_session_134.session_key = u'pivzde0nwp7whiprxjbsutdpiaejkh9c'
    django_session_134.session_data = u'ZmJiZDc1MWZkODk0ZTEwNDg5ODU0YWY0ZmM1ZWY1M2RkOWFmMzg1MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASJ1Lg=='
    django_session_134.expire_date = datetime.datetime(2013, 9, 26, 22, 25, 18)
    django_session_134 = importer.save_or_locate(django_session_134)

    django_session_135 = Session()
    django_session_135.session_key = u'pqyfmsy3kxidbcf7j6vujozk3hzqm06k'
    django_session_135.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_135.expire_date = datetime.datetime(2013, 9, 21, 3, 50, 36)
    django_session_135 = importer.save_or_locate(django_session_135)

    django_session_136 = Session()
    django_session_136.session_key = u'py5e5l1fp6cvw4r1xlk21u7qcen0ll70'
    django_session_136.session_data = u'ZWFhYzljMzlhZTM0Zjk1MjgzY2NjOTc4ZjA5MGU1OTlkYjNmYTBlYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASN1Lg=='
    django_session_136.expire_date = datetime.datetime(2013, 9, 26, 22, 34, 48)
    django_session_136 = importer.save_or_locate(django_session_136)

    django_session_137 = Session()
    django_session_137.session_key = u'q4a4l7uy6uyahrk0hqmxb05eyd97k600'
    django_session_137.session_data = u'Y2ViNjYwZGVjNzY2YjNjYzQwYWYxOTI1MzhiZDgzYTFlZjVlY2M2MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVp1Lg=='
    django_session_137.expire_date = datetime.datetime(2013, 9, 28, 11, 54, 49)
    django_session_137 = importer.save_or_locate(django_session_137)

    django_session_138 = Session()
    django_session_138.session_key = u'qglue73r1nxk81et39kkypd73uvxtvqw'
    django_session_138.session_data = u'YmFmYTBjY2FjNjYzMjM1NGIyZjdlMzU0MjJiMDg5YjJmMTM2MjYxZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXZ1Lg=='
    django_session_138.expire_date = datetime.datetime(2013, 10, 1, 4, 8, 53)
    django_session_138 = importer.save_or_locate(django_session_138)

    django_session_139 = Session()
    django_session_139.session_key = u'qjmxnrmzv3p1eg5doau9gjzgvjn4chnv'
    django_session_139.session_data = u'NTdlODQyNGNjNGMwZDFiYjdlMmNlNDBmODlkMzE5ZDhmMThmNzdhZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWt1Lg=='
    django_session_139.expire_date = datetime.datetime(2013, 9, 29, 20, 16, 28)
    django_session_139 = importer.save_or_locate(django_session_139)

    django_session_140 = Session()
    django_session_140.session_key = u'qkc3i0b97fw7ns5jglhk1yy9g4ykcruu'
    django_session_140.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_140.expire_date = datetime.datetime(2013, 9, 21, 22, 50, 49)
    django_session_140 = importer.save_or_locate(django_session_140)

    django_session_141 = Session()
    django_session_141.session_key = u'qvrsafa8oa4zsgw6ihzmfq6vetgatst7'
    django_session_141.session_data = u'YWIxNWIzZWFiYTc3N2U1YWQ2ZTkyYWIzNTkwZDI0MjA5N2Q1YzRiMjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg=='
    django_session_141.expire_date = datetime.datetime(2013, 9, 27, 1, 21, 54)
    django_session_141 = importer.save_or_locate(django_session_141)

    django_session_142 = Session()
    django_session_142.session_key = u'r482d7bwhiey3hjgck0z52xcge0667ht'
    django_session_142.session_data = u'YmVjNGUwNDQwZGY4NGY5YTNmMTA0ZDc4YjM4ZjkzZTJlYmUxMTA5ZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVh1Lg=='
    django_session_142.expire_date = datetime.datetime(2013, 9, 28, 10, 46, 8)
    django_session_142 = importer.save_or_locate(django_session_142)

    django_session_143 = Session()
    django_session_143.session_key = u'r5se2cd8f2lfzi25qbbsz9jlw55o3nuy'
    django_session_143.session_data = u'Mjk0ODYzMDBiYzRhOWZjMjU3MzY4MjJkODliOGY1MGNmNjdjYjcyYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWZ1Lg=='
    django_session_143.expire_date = datetime.datetime(2013, 9, 29, 14, 16, 32)
    django_session_143 = importer.save_or_locate(django_session_143)

    django_session_144 = Session()
    django_session_144.session_key = u'r74r4glc0poe7sns6lpo357nyv8djuq7'
    django_session_144.session_data = u'MGNkNmJjNTFmM2Q3MzUyYmY0ZDE5ZDIxOGQyMTM1ODNmNjhlYTRiZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUF1Lg=='
    django_session_144.expire_date = datetime.datetime(2013, 9, 27, 8, 27, 32)
    django_session_144 = importer.save_or_locate(django_session_144)

    django_session_145 = Session()
    django_session_145.session_key = u'rlafcube6jr5ifnn38oj0u260ilbox0v'
    django_session_145.session_data = u'YTkxMmQzNmNiMmJhNTk1ZTJkMTgxNzE1Y2M1ZjFjNWI3OTU0NmQyZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXx1Lg=='
    django_session_145.expire_date = datetime.datetime(2013, 10, 1, 22, 16, 37)
    django_session_145 = importer.save_or_locate(django_session_145)

    django_session_146 = Session()
    django_session_146.session_key = u'ror0nd04a9m1l2uxfba4aeibkdgp4hpp'
    django_session_146.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_146.expire_date = datetime.datetime(2013, 9, 27, 3, 31, 50)
    django_session_146 = importer.save_or_locate(django_session_146)

    django_session_147 = Session()
    django_session_147.session_key = u'rrtxx7xdo3qh8pnhjif206b50ean0tdw'
    django_session_147.session_data = u'MjM3YzZiNGY3MDI2MGYzZmE4OWNlMjliNmFlOWE3NWU0ZDQ5ZDM1NTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQR1Lg=='
    django_session_147.expire_date = datetime.datetime(2013, 9, 21, 10, 59, 30)
    django_session_147 = importer.save_or_locate(django_session_147)

    django_session_148 = Session()
    django_session_148.session_key = u's3a9pmetsy6glzc5gxd7lv6lcxrw8xr4'
    django_session_148.session_data = u'NjRhMjZlMmMzNTk3N2Q2ZDFjZjA2ZWY1NjE1MmIyZmE2NWQ1MmZlZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUt1Lg=='
    django_session_148.expire_date = datetime.datetime(2013, 9, 27, 15, 2, 19)
    django_session_148 = importer.save_or_locate(django_session_148)

    django_session_149 = Session()
    django_session_149.session_key = u'skpqvfeinrzjccw65o0cne38gtp537bf'
    django_session_149.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_149.expire_date = datetime.datetime(2013, 9, 22, 10, 45, 42)
    django_session_149 = importer.save_or_locate(django_session_149)

    django_session_150 = Session()
    django_session_150.session_key = u'sqrf7fkwt2lm9btc0otsiszwap46ybak'
    django_session_150.session_data = u'NDJkOTgyNzg5ZWVlMzNmMzNhMGFiNTY2NTkyNWQxNmE0ZDg0MWQ3MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATJ1Lg=='
    django_session_150.expire_date = datetime.datetime(2013, 9, 27, 2, 0, 33)
    django_session_150 = importer.save_or_locate(django_session_150)

    django_session_151 = Session()
    django_session_151.session_key = u'srwc8eb08z9rbq9mffkyymlf64w8h0w5'
    django_session_151.session_data = u'MzdjN2VkMjRhZmRjMzU5YzVkN2M4OWM3MGJhNjUyNTQxOTU1YTZiNTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoQAdS4='
    django_session_151.expire_date = datetime.datetime(2013, 10, 3, 18, 35, 47)
    django_session_151 = importer.save_or_locate(django_session_151)

    django_session_152 = Session()
    django_session_152.session_key = u'sybmf0dx0qayvurpaz1500028olyuq1j'
    django_session_152.session_data = u'NWM3ZGQyODUwNjdmNGY4NTYxYmMxM2Q5ODYyMzExNmEwMmMzYTM0MzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAT51Lg=='
    django_session_152.expire_date = datetime.datetime(2013, 9, 27, 6, 50, 59)
    django_session_152 = importer.save_or_locate(django_session_152)

    django_session_153 = Session()
    django_session_153.session_key = u'sykwqyabytqwugfhy986jdmhspsnq64p'
    django_session_153.session_data = u'YTUxMmZlZmRlMGY4ZTIzZjBkZmEzYzA1ZTRjZjAzNzU4YjczMTJiOTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAV51Lg=='
    django_session_153.expire_date = datetime.datetime(2013, 9, 28, 20, 59, 24)
    django_session_153 = importer.save_or_locate(django_session_153)

    django_session_154 = Session()
    django_session_154.session_key = u'tezouyngns26suac2nlv23wrfzclqe2n'
    django_session_154.session_data = u'N2ZhZmJlMDkzNTZhZTJjMzQ1NjAyNTk1MTUyNGM5NTJiMzM4NGU1MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARh1Lg=='
    django_session_154.expire_date = datetime.datetime(2013, 9, 26, 21, 19, 41)
    django_session_154 = importer.save_or_locate(django_session_154)

    django_session_155 = Session()
    django_session_155.session_key = u'tlafto4c0gu1gsgkirw6fai3z1nud146'
    django_session_155.session_data = u'YWY3ODM3ZjAyYWE0MDIyN2ZhZjczNGFlNGNmODI3YjI5MmRkZjRhYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXB1Lg=='
    django_session_155.expire_date = datetime.datetime(2013, 9, 30, 1, 4, 3)
    django_session_155 = importer.save_or_locate(django_session_155)

    django_session_156 = Session()
    django_session_156.session_key = u'tp3kaahfpv4v62sgb2nvcy89zxopn80y'
    django_session_156.session_data = u'NDcwM2Y1OGY4MjI5M2JhMTJkNDJkZWFjMjQxYTlhMWIzZWUwY2Q5YzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAW11Lg=='
    django_session_156.expire_date = datetime.datetime(2013, 9, 29, 22, 10, 7)
    django_session_156 = importer.save_or_locate(django_session_156)

    django_session_157 = Session()
    django_session_157.session_key = u'tpzruzgpi205tkybmupldpfc1iqry6rz'
    django_session_157.session_data = u'MzBmYjc0Mzc0Y2E5MDRjMmMyMGUyZDFmZjEzZTRiNTg1Yzc0NWZmNjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATB1Lg=='
    django_session_157.expire_date = datetime.datetime(2013, 9, 27, 1, 48, 20)
    django_session_157 = importer.save_or_locate(django_session_157)

    django_session_158 = Session()
    django_session_158.session_key = u'u03taa9eq9oxqqo5xfkko96wm55qbrgp'
    django_session_158.session_data = u'YTJjNWI1MDMxN2ViMDY2NTMyNTgzNjEwMjNkNzU1ZjdmMWY3YjFiYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAW91Lg=='
    django_session_158.expire_date = datetime.datetime(2013, 9, 30, 0, 38, 38)
    django_session_158 = importer.save_or_locate(django_session_158)

    django_session_159 = Session()
    django_session_159.session_key = u'u2dak9jne5a6lotjp2hi8jxpg82htnyr'
    django_session_159.session_data = u'YTBiZjgwM2Q2NWNjOGJmY2E0ZWZmM2ZlOWVmMmRlMmU0N2Y2ZjI3NTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUV1Lg=='
    django_session_159.expire_date = datetime.datetime(2013, 9, 27, 10, 53, 8)
    django_session_159 = importer.save_or_locate(django_session_159)

    django_session_160 = Session()
    django_session_160.session_key = u'ud63jn37riferjewy4znscn4qenbjlrk'
    django_session_160.session_data = u'ZTkwNjk4MGM0ZGFhZDFjY2FmZjI5ZmFjY2E2YjZmNDRiY2I5NmRlZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQp1Lg=='
    django_session_160.expire_date = datetime.datetime(2013, 9, 21, 20, 7, 24)
    django_session_160 = importer.save_or_locate(django_session_160)

    django_session_161 = Session()
    django_session_161.session_key = u'uqpscba15h3sinjuby3zwb9wku4cz58u'
    django_session_161.session_data = u'MTY1MDhiYTRiZTBlMjQwZGJkYzk2MGYyYmU4MDA5NGM4MzYyZTA4NDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATV1Lg=='
    django_session_161.expire_date = datetime.datetime(2013, 9, 27, 2, 47, 48)
    django_session_161 = importer.save_or_locate(django_session_161)

    django_session_162 = Session()
    django_session_162.session_key = u'v74m8vg5wt6ek8dxdq9b8zc9l01eh4hn'
    django_session_162.session_data = u'YTExZTdhNGM0NTZkMjc0MzE3MDg2NjYxY2Q3NTJlOTQyY2EwNGRkZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAX11Lg=='
    django_session_162.expire_date = datetime.datetime(2013, 10, 1, 23, 11, 10)
    django_session_162 = importer.save_or_locate(django_session_162)

    django_session_163 = Session()
    django_session_163.session_key = u'v8k5cj4x1tmajz6h87o7upi72pwas03y'
    django_session_163.session_data = u'ZDVhZmIzNDQ0YmY1ZDYyNjI5YmQ1MTRlYjdiYzUzZjQxZTE0ODU0MTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAUR1Lg=='
    django_session_163.expire_date = datetime.datetime(2013, 9, 27, 10, 28, 49)
    django_session_163 = importer.save_or_locate(django_session_163)

    django_session_164 = Session()
    django_session_164.session_key = u'vcis7jbrhdxq551ho5x1o3pwtibumk5x'
    django_session_164.session_data = u'YmJiYTEzNDc3NjEyMDQzZTgxYTIzYjI5ZWNlYmZjMmViNzQ4NTJiZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAoIAdS4='
    django_session_164.expire_date = datetime.datetime(2013, 10, 3, 14, 19, 31)
    django_session_164 = importer.save_or_locate(django_session_164)

    django_session_165 = Session()
    django_session_165.session_key = u'vg4dx22vkx7rzmrtpblzvlzxqtmm2lgm'
    django_session_165.session_data = u'YmQxZmU5ZDhhNDk2ZmE1YzExM2UyMDc3NWI0MjEzYWI3MTVkNmFhMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATZ1Lg=='
    django_session_165.expire_date = datetime.datetime(2013, 9, 27, 2, 49, 14)
    django_session_165 = importer.save_or_locate(django_session_165)

    django_session_166 = Session()
    django_session_166.session_key = u'vpwgn8m4hlvutjql8td1yzf4f91ymumf'
    django_session_166.session_data = u'N2Y1Zjc3MmI1YjE2ZjI0ZmRkOTYwYThiYTY2ZmY2ODdlM2Q5ZGMxMDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAXR1Lg=='
    django_session_166.expire_date = datetime.datetime(2013, 9, 30, 20, 58, 17)
    django_session_166 = importer.save_or_locate(django_session_166)

    django_session_167 = Session()
    django_session_167.session_key = u'wdmkoobb7ip455gb2nmjvmrljltyipd6'
    django_session_167.session_data = u'NmRjNjMxYzVkMzk2NzRkMWM2NzkwNGMzYmEzMDk1NGM3YzlmYTUwZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAWF1Lg=='
    django_session_167.expire_date = datetime.datetime(2013, 9, 29, 1, 10, 34)
    django_session_167 = importer.save_or_locate(django_session_167)

    django_session_168 = Session()
    django_session_168.session_key = u'wivm4tu2iyvmq3cin9ag3vnatpvrrstc'
    django_session_168.session_data = u'YzAxYTUxNDdiMWU2YjgzMWEyNGE2NTIxOGRhOTI2MWJhNjdjZmIxYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARV1Lg=='
    django_session_168.expire_date = datetime.datetime(2013, 9, 26, 14, 23, 19)
    django_session_168 = importer.save_or_locate(django_session_168)

    django_session_169 = Session()
    django_session_169.session_key = u'wltt3o003wfkyjlb1xbnetox03d2pdpu'
    django_session_169.session_data = u'MzczZWVlNTYyM2FhYmY5Y2RjMzcxZDVjMmNkOTk1YzgxODIxMGQ0ZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATN1Lg=='
    django_session_169.expire_date = datetime.datetime(2013, 9, 27, 2, 8, 4)
    django_session_169 = importer.save_or_locate(django_session_169)

    django_session_170 = Session()
    django_session_170.session_key = u'x1w2wv4d4ro7emm099coy1csxxlmlc93'
    django_session_170.session_data = u'M2Y2NTQwYzcwMmM5Yzg5ZTJhMTFkMjM4NmY0NzM2OTRiMTkxZWRiNTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAVd1Lg=='
    django_session_170.expire_date = datetime.datetime(2013, 9, 28, 3, 3, 40)
    django_session_170 = importer.save_or_locate(django_session_170)

    django_session_171 = Session()
    django_session_171.session_key = u'xr0cibwj1c4wsi8go1ecg5bmfh3vr6ic'
    django_session_171.session_data = u'OWIxNDJiODFkOGE2ODFhZmM4NzVmYzhjYTQyYTU4ZWI2Y2Y2ODY4ZDqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKASZ1Lg=='
    django_session_171.expire_date = datetime.datetime(2013, 9, 26, 22, 56)
    django_session_171 = importer.save_or_locate(django_session_171)

    django_session_172 = Session()
    django_session_172.session_key = u'xz30nxv3uuscshhur22ge9l3n5uupndr'
    django_session_172.session_data = u'NjBhNmYxZmUxMWYzZTJjN2QzMDZhZjdmOGY5ZjI3MzY0ZWQ1OGQ0ZjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQl1Lg=='
    django_session_172.expire_date = datetime.datetime(2013, 9, 21, 19, 46, 11)
    django_session_172 = importer.save_or_locate(django_session_172)

    django_session_173 = Session()
    django_session_173.session_key = u'ywcw0v5mgkyqowj887bqmpwfz41qnbne'
    django_session_173.session_data = u'ZWFhM2FkYzE5MzI5NTljYmU2MWRmMzI3NGZlOGU0ZDY5ZWQ4Y2UxYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARp1Lg=='
    django_session_173.expire_date = datetime.datetime(2013, 9, 26, 21, 31, 10)
    django_session_173 = importer.save_or_locate(django_session_173)

    django_session_174 = Session()
    django_session_174.session_key = u'z2e0amjasgex1oa1l7ulga07gpc34rfk'
    django_session_174.session_data = u'MWJmOTBlMDQ2ZWYyZDY2ZTc3ZTkxYTkwZDczYTQ1OWIxMzc5OTlmNTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKATF1Lg=='
    django_session_174.expire_date = datetime.datetime(2013, 9, 27, 1, 49, 50)
    django_session_174 = importer.save_or_locate(django_session_174)

    django_session_175 = Session()
    django_session_175.session_key = u'zi78peca5j84ihbsur7gg1xn4bop6671'
    django_session_175.session_data = u'MTgwNDUzN2Q4NTVlNmU4MWVkN2FlMjQ5MDY3YjI4ODI1MmEyZmYyYTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQ91Lg=='
    django_session_175.expire_date = datetime.datetime(2013, 9, 24, 0, 2, 9)
    django_session_175 = importer.save_or_locate(django_session_175)

    django_session_176 = Session()
    django_session_176.session_key = u'zt3ajqfmitmmfyk5neijgd9pqv4p3b4s'
    django_session_176.session_data = u'ODdhNzY0NDVlZWNjZjBjM2JlMmJhZGU3MDlhZDk2YjE1NDQwN2JiMTqAAn1xAS4='
    django_session_176.expire_date = datetime.datetime(2013, 9, 23, 4, 26, 37)
    django_session_176 = importer.save_or_locate(django_session_176)

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

    shipBuilder_manufacturer_47 = Manufacturer()
    shipBuilder_manufacturer_47.name = u'MISC'
    shipBuilder_manufacturer_47.description = u''
    shipBuilder_manufacturer_47 = importer.save_or_locate(shipBuilder_manufacturer_47)

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

    shipBuilder_vehicleitemsubtype_20 = VehicleItemSubType()
    shipBuilder_vehicleitemsubtype_20.subTypeName = u'Tractor'
    shipBuilder_vehicleitemsubtype_20.parent = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitemsubtype_20 = importer.save_or_locate(shipBuilder_vehicleitemsubtype_20)

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
    shipBuilder_vehicleitempower_1.state = u'Default'
    shipBuilder_vehicleitempower_1.value = u'100'
    shipBuilder_vehicleitempower_1 = importer.save_or_locate(shipBuilder_vehicleitempower_1)

    shipBuilder_vehicleitempower_2 = VehicleItemPower()
    shipBuilder_vehicleitempower_2.state = u'Default'
    shipBuilder_vehicleitempower_2.value = u'100'
    shipBuilder_vehicleitempower_2 = importer.save_or_locate(shipBuilder_vehicleitempower_2)

    shipBuilder_vehicleitempower_3 = VehicleItemPower()
    shipBuilder_vehicleitempower_3.state = u'Default'
    shipBuilder_vehicleitempower_3.value = u'100'
    shipBuilder_vehicleitempower_3 = importer.save_or_locate(shipBuilder_vehicleitempower_3)

    shipBuilder_vehicleitempower_4 = VehicleItemPower()
    shipBuilder_vehicleitempower_4.state = u'Active'
    shipBuilder_vehicleitempower_4.value = u'-10'
    shipBuilder_vehicleitempower_4 = importer.save_or_locate(shipBuilder_vehicleitempower_4)

    shipBuilder_vehicleitempower_5 = VehicleItemPower()
    shipBuilder_vehicleitempower_5.state = u'Idle'
    shipBuilder_vehicleitempower_5.value = u'-3'
    shipBuilder_vehicleitempower_5 = importer.save_or_locate(shipBuilder_vehicleitempower_5)

    shipBuilder_vehicleitempower_6 = VehicleItemPower()
    shipBuilder_vehicleitempower_6.state = u'Shooting'
    shipBuilder_vehicleitempower_6.value = u'-30'
    shipBuilder_vehicleitempower_6 = importer.save_or_locate(shipBuilder_vehicleitempower_6)

    shipBuilder_vehicleitempower_7 = VehicleItemPower()
    shipBuilder_vehicleitempower_7.state = u'Default'
    shipBuilder_vehicleitempower_7.value = u'100'
    shipBuilder_vehicleitempower_7 = importer.save_or_locate(shipBuilder_vehicleitempower_7)

    shipBuilder_vehicleitempower_8 = VehicleItemPower()
    shipBuilder_vehicleitempower_8.state = u'Active'
    shipBuilder_vehicleitempower_8.value = u'-10'
    shipBuilder_vehicleitempower_8 = importer.save_or_locate(shipBuilder_vehicleitempower_8)

    shipBuilder_vehicleitempower_9 = VehicleItemPower()
    shipBuilder_vehicleitempower_9.state = u'Idle'
    shipBuilder_vehicleitempower_9.value = u'-3'
    shipBuilder_vehicleitempower_9 = importer.save_or_locate(shipBuilder_vehicleitempower_9)

    shipBuilder_vehicleitempower_10 = VehicleItemPower()
    shipBuilder_vehicleitempower_10.state = u'Targeting'
    shipBuilder_vehicleitempower_10.value = u'-30'
    shipBuilder_vehicleitempower_10 = importer.save_or_locate(shipBuilder_vehicleitempower_10)

    shipBuilder_vehicleitempower_11 = VehicleItemPower()
    shipBuilder_vehicleitempower_11.state = u'Default'
    shipBuilder_vehicleitempower_11.value = u'100'
    shipBuilder_vehicleitempower_11 = importer.save_or_locate(shipBuilder_vehicleitempower_11)

    shipBuilder_vehicleitempower_12 = VehicleItemPower()
    shipBuilder_vehicleitempower_12.state = u'Active'
    shipBuilder_vehicleitempower_12.value = u'-10'
    shipBuilder_vehicleitempower_12 = importer.save_or_locate(shipBuilder_vehicleitempower_12)

    shipBuilder_vehicleitempower_13 = VehicleItemPower()
    shipBuilder_vehicleitempower_13.state = u'Idle'
    shipBuilder_vehicleitempower_13.value = u'-3'
    shipBuilder_vehicleitempower_13 = importer.save_or_locate(shipBuilder_vehicleitempower_13)

    shipBuilder_vehicleitempower_14 = VehicleItemPower()
    shipBuilder_vehicleitempower_14.state = u'Targeting'
    shipBuilder_vehicleitempower_14.value = u'-80'
    shipBuilder_vehicleitempower_14 = importer.save_or_locate(shipBuilder_vehicleitempower_14)

    shipBuilder_vehicleitempower_15 = VehicleItemPower()
    shipBuilder_vehicleitempower_15.state = u'Active'
    shipBuilder_vehicleitempower_15.value = u'-10'
    shipBuilder_vehicleitempower_15 = importer.save_or_locate(shipBuilder_vehicleitempower_15)

    shipBuilder_vehicleitempower_16 = VehicleItemPower()
    shipBuilder_vehicleitempower_16.state = u'Idle'
    shipBuilder_vehicleitempower_16.value = u'-10'
    shipBuilder_vehicleitempower_16 = importer.save_or_locate(shipBuilder_vehicleitempower_16)

    shipBuilder_vehicleitempower_17 = VehicleItemPower()
    shipBuilder_vehicleitempower_17.state = u'Shooting'
    shipBuilder_vehicleitempower_17.value = u'-80'
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
    shipBuilder_vehicleitempower_20.state = u'Targeting'
    shipBuilder_vehicleitempower_20.value = u'-30'
    shipBuilder_vehicleitempower_20 = importer.save_or_locate(shipBuilder_vehicleitempower_20)

    shipBuilder_vehicleitempower_21 = VehicleItemPower()
    shipBuilder_vehicleitempower_21.state = u'Active'
    shipBuilder_vehicleitempower_21.value = u'-10'
    shipBuilder_vehicleitempower_21 = importer.save_or_locate(shipBuilder_vehicleitempower_21)

    shipBuilder_vehicleitempower_22 = VehicleItemPower()
    shipBuilder_vehicleitempower_22.state = u'Idle'
    shipBuilder_vehicleitempower_22.value = u'-3'
    shipBuilder_vehicleitempower_22 = importer.save_or_locate(shipBuilder_vehicleitempower_22)

    shipBuilder_vehicleitempower_23 = VehicleItemPower()
    shipBuilder_vehicleitempower_23.state = u'Shooting'
    shipBuilder_vehicleitempower_23.value = u'-30'
    shipBuilder_vehicleitempower_23 = importer.save_or_locate(shipBuilder_vehicleitempower_23)

    shipBuilder_vehicleitempower_24 = VehicleItemPower()
    shipBuilder_vehicleitempower_24.state = u'Default'
    shipBuilder_vehicleitempower_24.value = u'100'
    shipBuilder_vehicleitempower_24 = importer.save_or_locate(shipBuilder_vehicleitempower_24)

    shipBuilder_vehicleitempower_25 = VehicleItemPower()
    shipBuilder_vehicleitempower_25.state = u'Active'
    shipBuilder_vehicleitempower_25.value = u'-10'
    shipBuilder_vehicleitempower_25 = importer.save_or_locate(shipBuilder_vehicleitempower_25)

    shipBuilder_vehicleitempower_26 = VehicleItemPower()
    shipBuilder_vehicleitempower_26.state = u'Idle'
    shipBuilder_vehicleitempower_26.value = u'-3'
    shipBuilder_vehicleitempower_26 = importer.save_or_locate(shipBuilder_vehicleitempower_26)

    shipBuilder_vehicleitempower_27 = VehicleItemPower()
    shipBuilder_vehicleitempower_27.state = u'Shooting'
    shipBuilder_vehicleitempower_27.value = u'-30'
    shipBuilder_vehicleitempower_27 = importer.save_or_locate(shipBuilder_vehicleitempower_27)

    shipBuilder_vehicleitempower_28 = VehicleItemPower()
    shipBuilder_vehicleitempower_28.state = u'Default'
    shipBuilder_vehicleitempower_28.value = u'100'
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
    shipBuilder_vehicleitempower_31.state = u'Shooting'
    shipBuilder_vehicleitempower_31.value = u'-30'
    shipBuilder_vehicleitempower_31 = importer.save_or_locate(shipBuilder_vehicleitempower_31)

    shipBuilder_vehicleitempower_32 = VehicleItemPower()
    shipBuilder_vehicleitempower_32.state = u'Active'
    shipBuilder_vehicleitempower_32.value = u'-10'
    shipBuilder_vehicleitempower_32 = importer.save_or_locate(shipBuilder_vehicleitempower_32)

    shipBuilder_vehicleitempower_33 = VehicleItemPower()
    shipBuilder_vehicleitempower_33.state = u'Idle'
    shipBuilder_vehicleitempower_33.value = u'-3'
    shipBuilder_vehicleitempower_33 = importer.save_or_locate(shipBuilder_vehicleitempower_33)

    shipBuilder_vehicleitempower_34 = VehicleItemPower()
    shipBuilder_vehicleitempower_34.state = u'Targeting'
    shipBuilder_vehicleitempower_34.value = u'-30'
    shipBuilder_vehicleitempower_34 = importer.save_or_locate(shipBuilder_vehicleitempower_34)

    shipBuilder_vehicleitempower_35 = VehicleItemPower()
    shipBuilder_vehicleitempower_35.state = u'Default'
    shipBuilder_vehicleitempower_35.value = u'100'
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
    shipBuilder_vehicleitempower_39.state = u'Targeting'
    shipBuilder_vehicleitempower_39.value = u'-30'
    shipBuilder_vehicleitempower_39 = importer.save_or_locate(shipBuilder_vehicleitempower_39)

    shipBuilder_vehicleitempower_40 = VehicleItemPower()
    shipBuilder_vehicleitempower_40.state = u'Default'
    shipBuilder_vehicleitempower_40.value = u'100'
    shipBuilder_vehicleitempower_40 = importer.save_or_locate(shipBuilder_vehicleitempower_40)

    shipBuilder_vehicleitempower_41 = VehicleItemPower()
    shipBuilder_vehicleitempower_41.state = u'Active'
    shipBuilder_vehicleitempower_41.value = u'-10'
    shipBuilder_vehicleitempower_41 = importer.save_or_locate(shipBuilder_vehicleitempower_41)

    shipBuilder_vehicleitempower_42 = VehicleItemPower()
    shipBuilder_vehicleitempower_42.state = u'Idle'
    shipBuilder_vehicleitempower_42.value = u'-3'
    shipBuilder_vehicleitempower_42 = importer.save_or_locate(shipBuilder_vehicleitempower_42)

    shipBuilder_vehicleitempower_43 = VehicleItemPower()
    shipBuilder_vehicleitempower_43.state = u'Shooting'
    shipBuilder_vehicleitempower_43.value = u'-30'
    shipBuilder_vehicleitempower_43 = importer.save_or_locate(shipBuilder_vehicleitempower_43)

    shipBuilder_vehicleitempower_44 = VehicleItemPower()
    shipBuilder_vehicleitempower_44.state = u'Active'
    shipBuilder_vehicleitempower_44.value = u'-10'
    shipBuilder_vehicleitempower_44 = importer.save_or_locate(shipBuilder_vehicleitempower_44)

    shipBuilder_vehicleitempower_45 = VehicleItemPower()
    shipBuilder_vehicleitempower_45.state = u'Idle'
    shipBuilder_vehicleitempower_45.value = u'-3'
    shipBuilder_vehicleitempower_45 = importer.save_or_locate(shipBuilder_vehicleitempower_45)

    shipBuilder_vehicleitempower_46 = VehicleItemPower()
    shipBuilder_vehicleitempower_46.state = u'Targeting'
    shipBuilder_vehicleitempower_46.value = u'-30'
    shipBuilder_vehicleitempower_46 = importer.save_or_locate(shipBuilder_vehicleitempower_46)

    shipBuilder_vehicleitempower_47 = VehicleItemPower()
    shipBuilder_vehicleitempower_47.state = u'Active'
    shipBuilder_vehicleitempower_47.value = u'-10'
    shipBuilder_vehicleitempower_47 = importer.save_or_locate(shipBuilder_vehicleitempower_47)

    shipBuilder_vehicleitempower_48 = VehicleItemPower()
    shipBuilder_vehicleitempower_48.state = u'Idle'
    shipBuilder_vehicleitempower_48.value = u'-3'
    shipBuilder_vehicleitempower_48 = importer.save_or_locate(shipBuilder_vehicleitempower_48)

    shipBuilder_vehicleitempower_49 = VehicleItemPower()
    shipBuilder_vehicleitempower_49.state = u'Shooting'
    shipBuilder_vehicleitempower_49.value = u'-30'
    shipBuilder_vehicleitempower_49 = importer.save_or_locate(shipBuilder_vehicleitempower_49)

    shipBuilder_vehicleitempower_50 = VehicleItemPower()
    shipBuilder_vehicleitempower_50.state = u'Active'
    shipBuilder_vehicleitempower_50.value = u'-10'
    shipBuilder_vehicleitempower_50 = importer.save_or_locate(shipBuilder_vehicleitempower_50)

    shipBuilder_vehicleitempower_51 = VehicleItemPower()
    shipBuilder_vehicleitempower_51.state = u'Idle'
    shipBuilder_vehicleitempower_51.value = u'-3'
    shipBuilder_vehicleitempower_51 = importer.save_or_locate(shipBuilder_vehicleitempower_51)

    shipBuilder_vehicleitempower_52 = VehicleItemPower()
    shipBuilder_vehicleitempower_52.state = u'Shooting'
    shipBuilder_vehicleitempower_52.value = u'-30'
    shipBuilder_vehicleitempower_52 = importer.save_or_locate(shipBuilder_vehicleitempower_52)

    shipBuilder_vehicleitempower_53 = VehicleItemPower()
    shipBuilder_vehicleitempower_53.state = u'Active'
    shipBuilder_vehicleitempower_53.value = u'-10'
    shipBuilder_vehicleitempower_53 = importer.save_or_locate(shipBuilder_vehicleitempower_53)

    shipBuilder_vehicleitempower_54 = VehicleItemPower()
    shipBuilder_vehicleitempower_54.state = u'Idle'
    shipBuilder_vehicleitempower_54.value = u'-3'
    shipBuilder_vehicleitempower_54 = importer.save_or_locate(shipBuilder_vehicleitempower_54)

    shipBuilder_vehicleitempower_55 = VehicleItemPower()
    shipBuilder_vehicleitempower_55.state = u'Shooting'
    shipBuilder_vehicleitempower_55.value = u'-30'
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
    shipBuilder_vehicleitempower_59.state = u'Default'
    shipBuilder_vehicleitempower_59.value = u'100'
    shipBuilder_vehicleitempower_59 = importer.save_or_locate(shipBuilder_vehicleitempower_59)

    shipBuilder_vehicleitempower_60 = VehicleItemPower()
    shipBuilder_vehicleitempower_60.state = u'Active'
    shipBuilder_vehicleitempower_60.value = u'-10'
    shipBuilder_vehicleitempower_60 = importer.save_or_locate(shipBuilder_vehicleitempower_60)

    shipBuilder_vehicleitempower_61 = VehicleItemPower()
    shipBuilder_vehicleitempower_61.state = u'Idle'
    shipBuilder_vehicleitempower_61.value = u'-3'
    shipBuilder_vehicleitempower_61 = importer.save_or_locate(shipBuilder_vehicleitempower_61)

    shipBuilder_vehicleitempower_62 = VehicleItemPower()
    shipBuilder_vehicleitempower_62.state = u'Shooting'
    shipBuilder_vehicleitempower_62.value = u'-30'
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
    shipBuilder_vehicleitempower_67.state = u'Active'
    shipBuilder_vehicleitempower_67.value = u'-10'
    shipBuilder_vehicleitempower_67 = importer.save_or_locate(shipBuilder_vehicleitempower_67)

    shipBuilder_vehicleitempower_68 = VehicleItemPower()
    shipBuilder_vehicleitempower_68.state = u'Idle'
    shipBuilder_vehicleitempower_68.value = u'-3'
    shipBuilder_vehicleitempower_68 = importer.save_or_locate(shipBuilder_vehicleitempower_68)

    shipBuilder_vehicleitempower_69 = VehicleItemPower()
    shipBuilder_vehicleitempower_69.state = u'Shooting'
    shipBuilder_vehicleitempower_69.value = u'-30'
    shipBuilder_vehicleitempower_69 = importer.save_or_locate(shipBuilder_vehicleitempower_69)

    shipBuilder_vehicleitempower_70 = VehicleItemPower()
    shipBuilder_vehicleitempower_70.state = u'Default'
    shipBuilder_vehicleitempower_70.value = u'100'
    shipBuilder_vehicleitempower_70 = importer.save_or_locate(shipBuilder_vehicleitempower_70)

    shipBuilder_vehicleitempower_71 = VehicleItemPower()
    shipBuilder_vehicleitempower_71.state = u'Default'
    shipBuilder_vehicleitempower_71.value = u'100'
    shipBuilder_vehicleitempower_71 = importer.save_or_locate(shipBuilder_vehicleitempower_71)

    shipBuilder_vehicleitempower_72 = VehicleItemPower()
    shipBuilder_vehicleitempower_72.state = u'Default'
    shipBuilder_vehicleitempower_72.value = u'100'
    shipBuilder_vehicleitempower_72 = importer.save_or_locate(shipBuilder_vehicleitempower_72)

    shipBuilder_vehicleitempower_73 = VehicleItemPower()
    shipBuilder_vehicleitempower_73.state = u'Default'
    shipBuilder_vehicleitempower_73.value = u'100'
    shipBuilder_vehicleitempower_73 = importer.save_or_locate(shipBuilder_vehicleitempower_73)

    shipBuilder_vehicleitempower_74 = VehicleItemPower()
    shipBuilder_vehicleitempower_74.state = u'Active'
    shipBuilder_vehicleitempower_74.value = u'-10'
    shipBuilder_vehicleitempower_74 = importer.save_or_locate(shipBuilder_vehicleitempower_74)

    shipBuilder_vehicleitempower_75 = VehicleItemPower()
    shipBuilder_vehicleitempower_75.state = u'Idle'
    shipBuilder_vehicleitempower_75.value = u'-3'
    shipBuilder_vehicleitempower_75 = importer.save_or_locate(shipBuilder_vehicleitempower_75)

    shipBuilder_vehicleitempower_76 = VehicleItemPower()
    shipBuilder_vehicleitempower_76.state = u'Targeting'
    shipBuilder_vehicleitempower_76.value = u'-30'
    shipBuilder_vehicleitempower_76 = importer.save_or_locate(shipBuilder_vehicleitempower_76)

    shipBuilder_vehicleitempower_77 = VehicleItemPower()
    shipBuilder_vehicleitempower_77.state = u'Active'
    shipBuilder_vehicleitempower_77.value = u'-10'
    shipBuilder_vehicleitempower_77 = importer.save_or_locate(shipBuilder_vehicleitempower_77)

    shipBuilder_vehicleitempower_78 = VehicleItemPower()
    shipBuilder_vehicleitempower_78.state = u'Idle'
    shipBuilder_vehicleitempower_78.value = u'-3'
    shipBuilder_vehicleitempower_78 = importer.save_or_locate(shipBuilder_vehicleitempower_78)

    shipBuilder_vehicleitempower_79 = VehicleItemPower()
    shipBuilder_vehicleitempower_79.state = u'Shooting'
    shipBuilder_vehicleitempower_79.value = u'-30'
    shipBuilder_vehicleitempower_79 = importer.save_or_locate(shipBuilder_vehicleitempower_79)

    shipBuilder_vehicleitempower_80 = VehicleItemPower()
    shipBuilder_vehicleitempower_80.state = u'Default'
    shipBuilder_vehicleitempower_80.value = u'100'
    shipBuilder_vehicleitempower_80 = importer.save_or_locate(shipBuilder_vehicleitempower_80)

    shipBuilder_vehicleitempower_81 = VehicleItemPower()
    shipBuilder_vehicleitempower_81.state = u'Default'
    shipBuilder_vehicleitempower_81.value = u'100'
    shipBuilder_vehicleitempower_81 = importer.save_or_locate(shipBuilder_vehicleitempower_81)

    shipBuilder_vehicleitempower_82 = VehicleItemPower()
    shipBuilder_vehicleitempower_82.state = u'Default'
    shipBuilder_vehicleitempower_82.value = u'100'
    shipBuilder_vehicleitempower_82 = importer.save_or_locate(shipBuilder_vehicleitempower_82)

    shipBuilder_vehicleitempower_83 = VehicleItemPower()
    shipBuilder_vehicleitempower_83.state = u'Active'
    shipBuilder_vehicleitempower_83.value = u'-10'
    shipBuilder_vehicleitempower_83 = importer.save_or_locate(shipBuilder_vehicleitempower_83)

    shipBuilder_vehicleitempower_84 = VehicleItemPower()
    shipBuilder_vehicleitempower_84.state = u'Idle'
    shipBuilder_vehicleitempower_84.value = u'-3'
    shipBuilder_vehicleitempower_84 = importer.save_or_locate(shipBuilder_vehicleitempower_84)

    shipBuilder_vehicleitempower_85 = VehicleItemPower()
    shipBuilder_vehicleitempower_85.state = u'Shooting'
    shipBuilder_vehicleitempower_85.value = u'-30'
    shipBuilder_vehicleitempower_85 = importer.save_or_locate(shipBuilder_vehicleitempower_85)

    shipBuilder_vehicleitempower_86 = VehicleItemPower()
    shipBuilder_vehicleitempower_86.state = u'Default'
    shipBuilder_vehicleitempower_86.value = u'100'
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
    shipBuilder_vehicleitempower_89.value = u'-30'
    shipBuilder_vehicleitempower_89 = importer.save_or_locate(shipBuilder_vehicleitempower_89)

    shipBuilder_vehicleitempower_90 = VehicleItemPower()
    shipBuilder_vehicleitempower_90.state = u'Active'
    shipBuilder_vehicleitempower_90.value = u'-10'
    shipBuilder_vehicleitempower_90 = importer.save_or_locate(shipBuilder_vehicleitempower_90)

    shipBuilder_vehicleitempower_91 = VehicleItemPower()
    shipBuilder_vehicleitempower_91.state = u'Idle'
    shipBuilder_vehicleitempower_91.value = u'-3'
    shipBuilder_vehicleitempower_91 = importer.save_or_locate(shipBuilder_vehicleitempower_91)

    shipBuilder_vehicleitempower_92 = VehicleItemPower()
    shipBuilder_vehicleitempower_92.state = u'Shooting'
    shipBuilder_vehicleitempower_92.value = u'-80'
    shipBuilder_vehicleitempower_92 = importer.save_or_locate(shipBuilder_vehicleitempower_92)

    shipBuilder_vehicleitempower_93 = VehicleItemPower()
    shipBuilder_vehicleitempower_93.state = u'Default'
    shipBuilder_vehicleitempower_93.value = u'100'
    shipBuilder_vehicleitempower_93 = importer.save_or_locate(shipBuilder_vehicleitempower_93)

    shipBuilder_vehicleitempower_94 = VehicleItemPower()
    shipBuilder_vehicleitempower_94.state = u'Active'
    shipBuilder_vehicleitempower_94.value = u'-10'
    shipBuilder_vehicleitempower_94 = importer.save_or_locate(shipBuilder_vehicleitempower_94)

    shipBuilder_vehicleitempower_95 = VehicleItemPower()
    shipBuilder_vehicleitempower_95.state = u'Idle'
    shipBuilder_vehicleitempower_95.value = u'-10'
    shipBuilder_vehicleitempower_95 = importer.save_or_locate(shipBuilder_vehicleitempower_95)

    shipBuilder_vehicleitempower_96 = VehicleItemPower()
    shipBuilder_vehicleitempower_96.state = u'Shooting'
    shipBuilder_vehicleitempower_96.value = u'-80'
    shipBuilder_vehicleitempower_96 = importer.save_or_locate(shipBuilder_vehicleitempower_96)

    shipBuilder_vehicleitempower_97 = VehicleItemPower()
    shipBuilder_vehicleitempower_97.state = u'Active'
    shipBuilder_vehicleitempower_97.value = u'-10'
    shipBuilder_vehicleitempower_97 = importer.save_or_locate(shipBuilder_vehicleitempower_97)

    shipBuilder_vehicleitempower_98 = VehicleItemPower()
    shipBuilder_vehicleitempower_98.state = u'Idle'
    shipBuilder_vehicleitempower_98.value = u'-3'
    shipBuilder_vehicleitempower_98 = importer.save_or_locate(shipBuilder_vehicleitempower_98)

    shipBuilder_vehicleitempower_99 = VehicleItemPower()
    shipBuilder_vehicleitempower_99.state = u'Shooting'
    shipBuilder_vehicleitempower_99.value = u'-30'
    shipBuilder_vehicleitempower_99 = importer.save_or_locate(shipBuilder_vehicleitempower_99)

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
    shipBuilder_vehicleitem_1.views = 358L
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
    shipBuilder_vehicleitem_2.views = 237L
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
    shipBuilder_vehicleitem_3.views = 809L
    shipBuilder_vehicleitem_3 = importer.save_or_locate(shipBuilder_vehicleitem_3)

    shipBuilder_vehicleitem_3.power.add(shipBuilder_vehicleitempower_4)
    shipBuilder_vehicleitem_3.power.add(shipBuilder_vehicleitempower_5)
    shipBuilder_vehicleitem_3.power.add(shipBuilder_vehicleitempower_6)
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
    shipBuilder_vehicleitem_4.views = 256L
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
    shipBuilder_vehicleitem_5.views = 318L
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
    shipBuilder_vehicleitem_6.views = 263L
    shipBuilder_vehicleitem_6 = importer.save_or_locate(shipBuilder_vehicleitem_6)

    shipBuilder_vehicleitem_6.power.add(shipBuilder_vehicleitempower_7)

    shipBuilder_vehicleitem_7 = VehicleItem()
    shipBuilder_vehicleitem_7.itemClass = 3L
    shipBuilder_vehicleitem_7.description = u"The Behring Marksman heat seeking missile utilizes an enemy's heat signature to obtain and maintain a lock on the target. This tried-and-true method of target acquisition has a few drawbacks: it is easily confused by flares and it may be difficult to establish lock on ships with low heat signatures. These issues aside, the Marksman is the go-to missile of choice for many independent operators and pilots. Rack of four (4)."
    shipBuilder_vehicleitem_7.name = u'Behring_Marksman_HS_Platform_x4'
    shipBuilder_vehicleitem_7.displayName = u'Behring Marksman HS Quad Platform'
    shipBuilder_vehicleitem_7.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_7.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_7.manufacturer = shipBuilder_manufacturer_2
    shipBuilder_vehicleitem_7.itemSize = 2L
    shipBuilder_vehicleitem_7.views = 422L
    shipBuilder_vehicleitem_7 = importer.save_or_locate(shipBuilder_vehicleitem_7)

    shipBuilder_vehicleitem_7.power.add(shipBuilder_vehicleitempower_8)
    shipBuilder_vehicleitem_7.power.add(shipBuilder_vehicleitempower_9)
    shipBuilder_vehicleitem_7.power.add(shipBuilder_vehicleitempower_10)
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
    shipBuilder_vehicleitem_8.views = 314L
    shipBuilder_vehicleitem_8 = importer.save_or_locate(shipBuilder_vehicleitem_8)

    shipBuilder_vehicleitem_8.power.add(shipBuilder_vehicleitempower_11)

    shipBuilder_vehicleitem_9 = VehicleItem()
    shipBuilder_vehicleitem_9.itemClass = 0L
    shipBuilder_vehicleitem_9.description = u''
    shipBuilder_vehicleitem_9.name = u'RSI_MissileBay'
    shipBuilder_vehicleitem_9.displayName = u'Missile Bay'
    shipBuilder_vehicleitem_9.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_9.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_9.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_9.itemSize = 2L
    shipBuilder_vehicleitem_9.views = 253L
    shipBuilder_vehicleitem_9 = importer.save_or_locate(shipBuilder_vehicleitem_9)

    shipBuilder_vehicleitem_9.power.add(shipBuilder_vehicleitempower_12)
    shipBuilder_vehicleitem_9.power.add(shipBuilder_vehicleitempower_13)
    shipBuilder_vehicleitem_9.power.add(shipBuilder_vehicleitempower_14)
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
    shipBuilder_vehicleitem_10.views = 215L
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
    shipBuilder_vehicleitem_11.views = 293L
    shipBuilder_vehicleitem_11 = importer.save_or_locate(shipBuilder_vehicleitem_11)

    shipBuilder_vehicleitem_11.power.add(shipBuilder_vehicleitempower_15)
    shipBuilder_vehicleitem_11.power.add(shipBuilder_vehicleitempower_16)
    shipBuilder_vehicleitem_11.power.add(shipBuilder_vehicleitempower_17)
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
    shipBuilder_vehicleitem_12.views = 386L
    shipBuilder_vehicleitem_12 = importer.save_or_locate(shipBuilder_vehicleitem_12)

    shipBuilder_vehicleitem_12.power.add(shipBuilder_vehicleitempower_18)
    shipBuilder_vehicleitem_12.power.add(shipBuilder_vehicleitempower_19)
    shipBuilder_vehicleitem_12.power.add(shipBuilder_vehicleitempower_20)
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
    shipBuilder_vehicleitem_13.views = 177L
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
    shipBuilder_vehicleitem_14.views = 485L
    shipBuilder_vehicleitem_14 = importer.save_or_locate(shipBuilder_vehicleitem_14)

    shipBuilder_vehicleitem_14.power.add(shipBuilder_vehicleitempower_21)
    shipBuilder_vehicleitem_14.power.add(shipBuilder_vehicleitempower_22)
    shipBuilder_vehicleitem_14.power.add(shipBuilder_vehicleitempower_23)
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
    shipBuilder_vehicleitem_15.views = 171L
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
    shipBuilder_vehicleitem_16.views = 121L
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
    shipBuilder_vehicleitem_17.views = 128L
    shipBuilder_vehicleitem_17 = importer.save_or_locate(shipBuilder_vehicleitem_17)

    shipBuilder_vehicleitem_17.power.add(shipBuilder_vehicleitempower_24)

    shipBuilder_vehicleitem_18 = VehicleItem()
    shipBuilder_vehicleitem_18.itemClass = 1L
    shipBuilder_vehicleitem_18.description = u'The Omnisky VI is the mid-sized laser cannon from manufacturer A&R. It boasts increased damage and range and power consumption over its smaller brother, the Omnisky III, and utilizes many of the same components resulting in middle-of-the-road power efficiency.'
    shipBuilder_vehicleitem_18.name = u'Omnisky_VI_Laser'
    shipBuilder_vehicleitem_18.displayName = u'Omnisky VI Laser Cannon'
    shipBuilder_vehicleitem_18.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_18.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_18.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_18.itemSize = 2L
    shipBuilder_vehicleitem_18.views = 689L
    shipBuilder_vehicleitem_18 = importer.save_or_locate(shipBuilder_vehicleitem_18)

    shipBuilder_vehicleitem_18.power.add(shipBuilder_vehicleitempower_25)
    shipBuilder_vehicleitem_18.power.add(shipBuilder_vehicleitempower_26)
    shipBuilder_vehicleitem_18.power.add(shipBuilder_vehicleitempower_27)
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
    shipBuilder_vehicleitem_19.views = 141L
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
    shipBuilder_vehicleitem_20.views = 63L
    shipBuilder_vehicleitem_20 = importer.save_or_locate(shipBuilder_vehicleitem_20)

    shipBuilder_vehicleitem_20.power.add(shipBuilder_vehicleitempower_28)

    shipBuilder_vehicleitem_21 = VehicleItem()
    shipBuilder_vehicleitem_21.itemClass = 1L
    shipBuilder_vehicleitem_21.description = u'Featuring a three-barrel sequential fire design, the Klaus & Werner CF-007 Bulldog repeater is capable of high rates of fire while maintaining accuracy. It has low damage per projectile and, although it has relatively low power consumption over-all, several publications have commented on its somewhat lackluster efficiency. Even so, the CF-007 remains a favorite among new pilots who are outfitting their first ship.'
    shipBuilder_vehicleitem_21.name = u'K_and_W_CF-007_Bulldog_Repeater'
    shipBuilder_vehicleitem_21.displayName = u'CF-007 Bulldog Repeater'
    shipBuilder_vehicleitem_21.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_21.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_21.manufacturer = shipBuilder_manufacturer_3
    shipBuilder_vehicleitem_21.itemSize = 1L
    shipBuilder_vehicleitem_21.views = 336L
    shipBuilder_vehicleitem_21 = importer.save_or_locate(shipBuilder_vehicleitem_21)

    shipBuilder_vehicleitem_21.power.add(shipBuilder_vehicleitempower_29)
    shipBuilder_vehicleitem_21.power.add(shipBuilder_vehicleitempower_30)
    shipBuilder_vehicleitem_21.power.add(shipBuilder_vehicleitempower_31)
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
    shipBuilder_vehicleitem_22.views = 130L
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
    shipBuilder_vehicleitem_23.views = 360L
    shipBuilder_vehicleitem_23 = importer.save_or_locate(shipBuilder_vehicleitem_23)

    shipBuilder_vehicleitem_23.power.add(shipBuilder_vehicleitempower_32)
    shipBuilder_vehicleitem_23.power.add(shipBuilder_vehicleitempower_33)
    shipBuilder_vehicleitem_23.power.add(shipBuilder_vehicleitempower_34)
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
    shipBuilder_vehicleitem_24.views = 225L
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
    shipBuilder_vehicleitem_25.views = 247L
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
    shipBuilder_vehicleitem_26.views = 64L
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
    shipBuilder_vehicleitem_27.views = 144L
    shipBuilder_vehicleitem_27 = importer.save_or_locate(shipBuilder_vehicleitem_27)

    shipBuilder_vehicleitem_27.power.add(shipBuilder_vehicleitempower_35)

    shipBuilder_vehicleitem_28 = VehicleItem()
    shipBuilder_vehicleitem_28.itemClass = 3L
    shipBuilder_vehicleitem_28.description = u'Talon Stalker missiles track and lock their target by use of highly sensitive optical cameras and image processing software. Although they have an increased lock time over other missile types, they are much more difficult for targets to shake once lock is attained. Rack of four (4).'
    shipBuilder_vehicleitem_28.name = u'Talon_Stalker_Quad'
    shipBuilder_vehicleitem_28.displayName = u'Talon Stalker Quad Rack'
    shipBuilder_vehicleitem_28.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_28.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_28.manufacturer = shipBuilder_manufacturer_4
    shipBuilder_vehicleitem_28.itemSize = 3L
    shipBuilder_vehicleitem_28.views = 275L
    shipBuilder_vehicleitem_28 = importer.save_or_locate(shipBuilder_vehicleitem_28)

    shipBuilder_vehicleitem_28.power.add(shipBuilder_vehicleitempower_37)
    shipBuilder_vehicleitem_28.power.add(shipBuilder_vehicleitempower_38)
    shipBuilder_vehicleitem_28.power.add(shipBuilder_vehicleitempower_39)
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
    shipBuilder_vehicleitem_29.views = 95L
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
    shipBuilder_vehicleitem_30.views = 197L
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
    shipBuilder_vehicleitem_31.views = 80L
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
    shipBuilder_vehicleitem_32.views = 226L
    shipBuilder_vehicleitem_32 = importer.save_or_locate(shipBuilder_vehicleitem_32)

    shipBuilder_vehicleitem_32.power.add(shipBuilder_vehicleitempower_40)

    shipBuilder_vehicleitem_33 = VehicleItem()
    shipBuilder_vehicleitem_33.itemClass = 0L
    shipBuilder_vehicleitem_33.description = u''
    shipBuilder_vehicleitem_33.name = u'RSI_DefaultWeaponDisplay'
    shipBuilder_vehicleitem_33.displayName = u'RSI Weapon Display'
    shipBuilder_vehicleitem_33.itemType = shipBuilder_vehicleitemtype_6
    shipBuilder_vehicleitem_33.itemSubType = shipBuilder_vehicleitemsubtype_12
    shipBuilder_vehicleitem_33.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_33.itemSize = 1L
    shipBuilder_vehicleitem_33.views = 164L
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
    shipBuilder_vehicleitem_34.views = 149L
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
    shipBuilder_vehicleitem_35.views = 283L
    shipBuilder_vehicleitem_35 = importer.save_or_locate(shipBuilder_vehicleitem_35)

    shipBuilder_vehicleitem_35.power.add(shipBuilder_vehicleitempower_41)
    shipBuilder_vehicleitem_35.power.add(shipBuilder_vehicleitempower_42)
    shipBuilder_vehicleitem_35.power.add(shipBuilder_vehicleitempower_43)
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
    shipBuilder_vehicleitem_36.views = 249L
    shipBuilder_vehicleitem_36 = importer.save_or_locate(shipBuilder_vehicleitem_36)

    shipBuilder_vehicleitem_36.power.add(shipBuilder_vehicleitempower_44)
    shipBuilder_vehicleitem_36.power.add(shipBuilder_vehicleitempower_45)
    shipBuilder_vehicleitem_36.power.add(shipBuilder_vehicleitempower_46)
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
    shipBuilder_vehicleitem_37.views = 61L
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
    shipBuilder_vehicleitem_38.views = 382L
    shipBuilder_vehicleitem_38 = importer.save_or_locate(shipBuilder_vehicleitem_38)

    shipBuilder_vehicleitem_38.power.add(shipBuilder_vehicleitempower_47)
    shipBuilder_vehicleitem_38.power.add(shipBuilder_vehicleitempower_48)
    shipBuilder_vehicleitem_38.power.add(shipBuilder_vehicleitempower_49)
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
    shipBuilder_vehicleitem_39.views = 378L
    shipBuilder_vehicleitem_39 = importer.save_or_locate(shipBuilder_vehicleitem_39)

    shipBuilder_vehicleitem_39.power.add(shipBuilder_vehicleitempower_50)
    shipBuilder_vehicleitem_39.power.add(shipBuilder_vehicleitempower_51)
    shipBuilder_vehicleitem_39.power.add(shipBuilder_vehicleitempower_52)
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
    shipBuilder_vehicleitem_40.views = 1L
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
    shipBuilder_vehicleitem_41.views = 153L
    shipBuilder_vehicleitem_41 = importer.save_or_locate(shipBuilder_vehicleitem_41)

    shipBuilder_vehicleitem_41.power.add(shipBuilder_vehicleitempower_53)
    shipBuilder_vehicleitem_41.power.add(shipBuilder_vehicleitempower_54)
    shipBuilder_vehicleitem_41.power.add(shipBuilder_vehicleitempower_55)
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
    shipBuilder_vehicleitem_42.views = 176L
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
    shipBuilder_vehicleitem_43.views = 508L
    shipBuilder_vehicleitem_43 = importer.save_or_locate(shipBuilder_vehicleitem_43)

    shipBuilder_vehicleitem_43.power.add(shipBuilder_vehicleitempower_56)
    shipBuilder_vehicleitem_43.power.add(shipBuilder_vehicleitempower_57)
    shipBuilder_vehicleitem_43.power.add(shipBuilder_vehicleitempower_58)
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
    shipBuilder_vehicleitem_44.views = 161L
    shipBuilder_vehicleitem_44 = importer.save_or_locate(shipBuilder_vehicleitem_44)

    shipBuilder_vehicleitem_44.power.add(shipBuilder_vehicleitempower_59)

    shipBuilder_vehicleitem_45 = VehicleItem()
    shipBuilder_vehicleitem_45.itemClass = 0L
    shipBuilder_vehicleitem_45.description = u''
    shipBuilder_vehicleitem_45.name = u'PhalanxTurret'
    shipBuilder_vehicleitem_45.displayName = u''
    shipBuilder_vehicleitem_45.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_45.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_45.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_45.itemSize = 2L
    shipBuilder_vehicleitem_45.views = 168L
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
    shipBuilder_vehicleitem_46.views = 617L
    shipBuilder_vehicleitem_46 = importer.save_or_locate(shipBuilder_vehicleitem_46)

    shipBuilder_vehicleitem_46.power.add(shipBuilder_vehicleitempower_60)
    shipBuilder_vehicleitem_46.power.add(shipBuilder_vehicleitempower_61)
    shipBuilder_vehicleitem_46.power.add(shipBuilder_vehicleitempower_62)
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
    shipBuilder_vehicleitem_47.views = 428L
    shipBuilder_vehicleitem_47 = importer.save_or_locate(shipBuilder_vehicleitem_47)

    shipBuilder_vehicleitem_47.power.add(shipBuilder_vehicleitempower_63)
    shipBuilder_vehicleitem_47.power.add(shipBuilder_vehicleitempower_64)
    shipBuilder_vehicleitem_47.power.add(shipBuilder_vehicleitempower_65)
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
    shipBuilder_vehicleitem_48.views = 339L
    shipBuilder_vehicleitem_48 = importer.save_or_locate(shipBuilder_vehicleitem_48)

    shipBuilder_vehicleitem_48.power.add(shipBuilder_vehicleitempower_66)

    shipBuilder_vehicleitem_49 = VehicleItem()
    shipBuilder_vehicleitem_49.itemClass = 0L
    shipBuilder_vehicleitem_49.description = u''
    shipBuilder_vehicleitem_49.name = u'Anvil_Flex_Thruster_TR2_Back_Right'
    shipBuilder_vehicleitem_49.displayName = u'Anvil TR2 Flex Thruster'
    shipBuilder_vehicleitem_49.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_49.itemSubType = shipBuilder_vehicleitemsubtype_8
    shipBuilder_vehicleitem_49.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_49.itemSize = 2L
    shipBuilder_vehicleitem_49.views = 71L
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
    shipBuilder_vehicleitem_50.views = 536L
    shipBuilder_vehicleitem_50 = importer.save_or_locate(shipBuilder_vehicleitem_50)

    shipBuilder_vehicleitem_50.power.add(shipBuilder_vehicleitempower_67)
    shipBuilder_vehicleitem_50.power.add(shipBuilder_vehicleitempower_68)
    shipBuilder_vehicleitem_50.power.add(shipBuilder_vehicleitempower_69)
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
    shipBuilder_vehicleitem_51.views = 188L
    shipBuilder_vehicleitem_51 = importer.save_or_locate(shipBuilder_vehicleitem_51)

    shipBuilder_vehicleitem_51.power.add(shipBuilder_vehicleitempower_1)

    shipBuilder_vehicleitem_52 = VehicleItem()
    shipBuilder_vehicleitem_52.itemClass = 0L
    shipBuilder_vehicleitem_52.description = u''
    shipBuilder_vehicleitem_52.name = u'STSTurret'
    shipBuilder_vehicleitem_52.displayName = u''
    shipBuilder_vehicleitem_52.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_52.itemSubType = shipBuilder_vehicleitemsubtype_7
    shipBuilder_vehicleitem_52.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_52.itemSize = 2L
    shipBuilder_vehicleitem_52.views = 114L
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
    shipBuilder_vehicleitem_53.views = 121L
    shipBuilder_vehicleitem_53 = importer.save_or_locate(shipBuilder_vehicleitem_53)

    shipBuilder_vehicleitem_53.power.add(shipBuilder_vehicleitempower_70)

    shipBuilder_vehicleitem_54 = VehicleItem()
    shipBuilder_vehicleitem_54.itemClass = 0L
    shipBuilder_vehicleitem_54.description = u"Capable of powering a medium class vessel, the HM4.4 is all speed and no caution. It's main selling point, the heavy output, becomes its biggest detriment as the engine flash will make conventional countermeasures useless when attempting to distract missiles. But, like the ad says, if it's speed you want..."
    shipBuilder_vehicleitem_54.name = u'Hammer_Propulsion_HM_4.4'
    shipBuilder_vehicleitem_54.displayName = u'Hammer Propulsion HMX 4.4'
    shipBuilder_vehicleitem_54.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_54.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_54.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_54.itemSize = 4L
    shipBuilder_vehicleitem_54.views = 232L
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
    shipBuilder_vehicleitem_55.views = 205L
    shipBuilder_vehicleitem_55 = importer.save_or_locate(shipBuilder_vehicleitem_55)

    shipBuilder_vehicleitem_55.power.add(shipBuilder_vehicleitempower_71)

    shipBuilder_vehicleitem_56 = VehicleItem()
    shipBuilder_vehicleitem_56.itemClass = 0L
    shipBuilder_vehicleitem_56.description = u''
    shipBuilder_vehicleitem_56.name = u'ScytheMissileRacks'
    shipBuilder_vehicleitem_56.displayName = u''
    shipBuilder_vehicleitem_56.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_56.itemSubType = shipBuilder_vehicleitemsubtype_6
    shipBuilder_vehicleitem_56.manufacturer = shipBuilder_manufacturer_42
    shipBuilder_vehicleitem_56.itemSize = 2L
    shipBuilder_vehicleitem_56.views = 132L
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
    shipBuilder_vehicleitem_57.views = 128L
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
    shipBuilder_vehicleitem_58.views = 187L
    shipBuilder_vehicleitem_58 = importer.save_or_locate(shipBuilder_vehicleitem_58)

    shipBuilder_vehicleitem_58.power.add(shipBuilder_vehicleitempower_72)

    shipBuilder_vehicleitem_59 = VehicleItem()
    shipBuilder_vehicleitem_59.itemClass = 0L
    shipBuilder_vehicleitem_59.description = u'The STC Blue by perrenial thruster manufacturer Dragon Stellar Transit Company offers high output and low emissions, great for pilots wishing to close the distance while maintaining a low profile. The smallest thruster in the STC lineup, the Blue has a thrust rating of 2.'
    shipBuilder_vehicleitem_59.name = u'Dragon_STC_Blue'
    shipBuilder_vehicleitem_59.displayName = u'Dragon STC Blue Main Engine'
    shipBuilder_vehicleitem_59.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_59.itemSubType = shipBuilder_vehicleitemsubtype_11
    shipBuilder_vehicleitem_59.manufacturer = shipBuilder_manufacturer_41
    shipBuilder_vehicleitem_59.itemSize = 2L
    shipBuilder_vehicleitem_59.views = 83L
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
    shipBuilder_vehicleitem_60.views = 216L
    shipBuilder_vehicleitem_60 = importer.save_or_locate(shipBuilder_vehicleitem_60)

    shipBuilder_vehicleitem_60.power.add(shipBuilder_vehicleitempower_74)
    shipBuilder_vehicleitem_60.power.add(shipBuilder_vehicleitempower_75)
    shipBuilder_vehicleitem_60.power.add(shipBuilder_vehicleitempower_76)
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
    shipBuilder_vehicleitem_61.views = 235L
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
    shipBuilder_vehicleitem_62.views = 148L
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
    shipBuilder_vehicleitem_63.views = 373L
    shipBuilder_vehicleitem_63 = importer.save_or_locate(shipBuilder_vehicleitem_63)

    shipBuilder_vehicleitem_63.power.add(shipBuilder_vehicleitempower_77)
    shipBuilder_vehicleitem_63.power.add(shipBuilder_vehicleitempower_78)
    shipBuilder_vehicleitem_63.power.add(shipBuilder_vehicleitempower_79)
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
    shipBuilder_vehicleitem_64.views = 148L
    shipBuilder_vehicleitem_64 = importer.save_or_locate(shipBuilder_vehicleitem_64)

    shipBuilder_vehicleitem_64.power.add(shipBuilder_vehicleitempower_80)

    shipBuilder_vehicleitem_65 = VehicleItem()
    shipBuilder_vehicleitem_65.itemClass = 0L
    shipBuilder_vehicleitem_65.description = u''
    shipBuilder_vehicleitem_65.name = u'RSI_DefaultRadarDisplay'
    shipBuilder_vehicleitem_65.displayName = u'RSI Radar Display'
    shipBuilder_vehicleitem_65.itemType = shipBuilder_vehicleitemtype_6
    shipBuilder_vehicleitem_65.itemSubType = shipBuilder_vehicleitemsubtype_15
    shipBuilder_vehicleitem_65.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_65.itemSize = 1L
    shipBuilder_vehicleitem_65.views = 168L
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
    shipBuilder_vehicleitem_66.views = 377L
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
    shipBuilder_vehicleitem_67.views = 190L
    shipBuilder_vehicleitem_67 = importer.save_or_locate(shipBuilder_vehicleitem_67)

    shipBuilder_vehicleitem_67.power.add(shipBuilder_vehicleitempower_81)

    shipBuilder_vehicleitem_68 = VehicleItem()
    shipBuilder_vehicleitem_68.itemClass = 0L
    shipBuilder_vehicleitem_68.description = u''
    shipBuilder_vehicleitem_68.name = u'Anvil_Joint_Thruster_TR2'
    shipBuilder_vehicleitem_68.displayName = u'Anvil TR2 Jointed Thruster'
    shipBuilder_vehicleitem_68.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_68.itemSubType = shipBuilder_vehicleitemsubtype_10
    shipBuilder_vehicleitem_68.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicleitem_68.itemSize = 2L
    shipBuilder_vehicleitem_68.views = 53L
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
    shipBuilder_vehicleitem_69.views = 87L
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
    shipBuilder_vehicleitem_70.views = 105L
    shipBuilder_vehicleitem_70 = importer.save_or_locate(shipBuilder_vehicleitem_70)

    shipBuilder_vehicleitem_70.power.add(shipBuilder_vehicleitempower_82)

    shipBuilder_vehicleitem_71 = VehicleItem()
    shipBuilder_vehicleitem_71.itemClass = 0L
    shipBuilder_vehicleitem_71.description = u'The Mantis GT-220 is a hydraulically-driven Gatling-type rotary cannon designed to deliver smaller rounds at a very high rate of fire. The Mantis is designed to shred armor on very fast targets, sacrificing power for absolute saturation of the target area.'
    shipBuilder_vehicleitem_71.name = u'Mantis_GT-220'
    shipBuilder_vehicleitem_71.displayName = u'Mantis GT-220'
    shipBuilder_vehicleitem_71.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_71.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_71.manufacturer = shipBuilder_manufacturer_31
    shipBuilder_vehicleitem_71.itemSize = 2L
    shipBuilder_vehicleitem_71.views = 242L
    shipBuilder_vehicleitem_71 = importer.save_or_locate(shipBuilder_vehicleitem_71)

    shipBuilder_vehicleitem_71.power.add(shipBuilder_vehicleitempower_83)
    shipBuilder_vehicleitem_71.power.add(shipBuilder_vehicleitempower_84)
    shipBuilder_vehicleitem_71.power.add(shipBuilder_vehicleitempower_85)
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
    shipBuilder_vehicleitem_72.views = 65L
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
    shipBuilder_vehicleitem_73.description = u"Designed in conjunction with the engineers at RSI, the A and R LR-5 Max OverDrive features the same great engine you've come to expect from A and R, but with higher quality parts built with the care and dedication that you've come to expect from the company that's been taking humanity to the stars since 2075."
    shipBuilder_vehicleitem_73.name = u'A_and_R_LR-5_MAX_OverDrive'
    shipBuilder_vehicleitem_73.displayName = u'A&R LR-5 MAX OverDrive'
    shipBuilder_vehicleitem_73.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_73.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_73.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_73.itemSize = 1L
    shipBuilder_vehicleitem_73.views = 84L
    shipBuilder_vehicleitem_73 = importer.save_or_locate(shipBuilder_vehicleitem_73)

    shipBuilder_vehicleitem_73.power.add(shipBuilder_vehicleitempower_3)

    shipBuilder_vehicleitem_74 = VehicleItem()
    shipBuilder_vehicleitem_74.itemClass = 0L
    shipBuilder_vehicleitem_74.description = u''
    shipBuilder_vehicleitem_74.name = u'RSI_DefaultPowerPlant'
    shipBuilder_vehicleitem_74.displayName = u'RSI Power Supply'
    shipBuilder_vehicleitem_74.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_74.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_74.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_74.itemSize = 1L
    shipBuilder_vehicleitem_74.views = 76L
    shipBuilder_vehicleitem_74 = importer.save_or_locate(shipBuilder_vehicleitem_74)

    shipBuilder_vehicleitem_74.power.add(shipBuilder_vehicleitempower_86)

    shipBuilder_vehicleitem_75 = VehicleItem()
    shipBuilder_vehicleitem_75.itemClass = 1L
    shipBuilder_vehicleitem_75.description = u"The entry level weapon of the Sword-series, the Longsword fires a 35mm round designed for use against a variety of armored targets. Don't let shields slow down your domination of the galaxy."
    shipBuilder_vehicleitem_75.name = u'Knightbridge_9_Series_Longsword'
    shipBuilder_vehicleitem_75.displayName = u'9-Series Longsword'
    shipBuilder_vehicleitem_75.itemType = shipBuilder_vehicleitemtype_2
    shipBuilder_vehicleitem_75.itemSubType = shipBuilder_vehicleitemsubtype_2
    shipBuilder_vehicleitem_75.manufacturer = shipBuilder_manufacturer_44
    shipBuilder_vehicleitem_75.itemSize = 1L
    shipBuilder_vehicleitem_75.views = 287L
    shipBuilder_vehicleitem_75 = importer.save_or_locate(shipBuilder_vehicleitem_75)

    shipBuilder_vehicleitem_75.power.add(shipBuilder_vehicleitempower_87)
    shipBuilder_vehicleitem_75.power.add(shipBuilder_vehicleitempower_88)
    shipBuilder_vehicleitem_75.power.add(shipBuilder_vehicleitempower_89)
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
    shipBuilder_vehicleitem_76.itemSubType = shipBuilder_vehicleitemsubtype_20
    shipBuilder_vehicleitem_76.manufacturer = shipBuilder_manufacturer_29
    shipBuilder_vehicleitem_76.itemSize = 1L
    shipBuilder_vehicleitem_76.views = 200L
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
    shipBuilder_vehicleitem_77.views = 313L
    shipBuilder_vehicleitem_77 = importer.save_or_locate(shipBuilder_vehicleitem_77)

    shipBuilder_vehicleitem_77.power.add(shipBuilder_vehicleitempower_90)
    shipBuilder_vehicleitem_77.power.add(shipBuilder_vehicleitempower_91)
    shipBuilder_vehicleitem_77.power.add(shipBuilder_vehicleitempower_92)
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
    shipBuilder_vehicleitem_78.views = 65L
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
    shipBuilder_vehicleitem_79.views = 250L
    shipBuilder_vehicleitem_79 = importer.save_or_locate(shipBuilder_vehicleitem_79)

    shipBuilder_vehicleitem_79.power.add(shipBuilder_vehicleitempower_93)

    shipBuilder_vehicleitem_80 = VehicleItem()
    shipBuilder_vehicleitem_80.itemClass = 0L
    shipBuilder_vehicleitem_80.description = u"The luxury version of the HM4.3, Hammer Propulsion's HMX4.3 engine system features customized racing parts from some of the league's top engineers to help weather corrosion and general part decay."
    shipBuilder_vehicleitem_80.name = u'Hammer_Propulsion_HMX_4.3'
    shipBuilder_vehicleitem_80.displayName = u'Hammer Propulsion HMX 4.3'
    shipBuilder_vehicleitem_80.itemType = shipBuilder_vehicleitemtype_3
    shipBuilder_vehicleitem_80.itemSubType = shipBuilder_vehicleitemsubtype_3
    shipBuilder_vehicleitem_80.manufacturer = shipBuilder_manufacturer_11
    shipBuilder_vehicleitem_80.itemSize = 3L
    shipBuilder_vehicleitem_80.views = 119L
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
    shipBuilder_vehicleitem_81.views = 88L
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
    shipBuilder_vehicleitem_82.views = 195L
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
    shipBuilder_vehicleitem_83.views = 207L
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
    shipBuilder_vehicleitem_84.views = 220L
    shipBuilder_vehicleitem_84 = importer.save_or_locate(shipBuilder_vehicleitem_84)

    shipBuilder_vehicleitem_84.power.add(shipBuilder_vehicleitempower_94)
    shipBuilder_vehicleitem_84.power.add(shipBuilder_vehicleitempower_95)
    shipBuilder_vehicleitem_84.power.add(shipBuilder_vehicleitempower_96)
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
    shipBuilder_vehicleitem_85.views = 69L
    shipBuilder_vehicleitem_85 = importer.save_or_locate(shipBuilder_vehicleitem_85)

    shipBuilder_vehicleitem_85.power.add(shipBuilder_vehicleitempower_2)

    shipBuilder_vehicleitem_86 = VehicleItem()
    shipBuilder_vehicleitem_86.itemClass = 0L
    shipBuilder_vehicleitem_86.description = u''
    shipBuilder_vehicleitem_86.name = u'RSI_DefaultBattery'
    shipBuilder_vehicleitem_86.displayName = u'RSI Battery'
    shipBuilder_vehicleitem_86.itemType = shipBuilder_vehicleitemtype_10
    shipBuilder_vehicleitem_86.itemSubType = shipBuilder_vehicleitemsubtype_18
    shipBuilder_vehicleitem_86.manufacturer = shipBuilder_manufacturer_38
    shipBuilder_vehicleitem_86.itemSize = 1L
    shipBuilder_vehicleitem_86.views = 194L
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
    shipBuilder_vehicleitem_87.views = 136L
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
    shipBuilder_vehicleitem_88.views = 487L
    shipBuilder_vehicleitem_88 = importer.save_or_locate(shipBuilder_vehicleitem_88)

    shipBuilder_vehicleitem_88.power.add(shipBuilder_vehicleitempower_97)
    shipBuilder_vehicleitem_88.power.add(shipBuilder_vehicleitempower_98)
    shipBuilder_vehicleitem_88.power.add(shipBuilder_vehicleitempower_99)
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
    shipBuilder_vehicleitem_89.views = 347L
    shipBuilder_vehicleitem_89 = importer.save_or_locate(shipBuilder_vehicleitem_89)

    shipBuilder_vehicleitem_90 = VehicleItem()
    shipBuilder_vehicleitem_90.itemClass = 0L
    shipBuilder_vehicleitem_90.description = u"The LR-7 ULTRA OverDrive is the patriarch of the LR series. Capable of handling any number of hauling or commercial needs, the LR-7 features a reinforced plasma-core to combat the increased heat signature. Odds are, if you need a monster of a power plant like this, your ship isn't hiding."
    shipBuilder_vehicleitem_90.name = u'A_and_R-7_ULTRA_OverDrive'
    shipBuilder_vehicleitem_90.displayName = u'A and R LR-7 ULTRA OverDrive'
    shipBuilder_vehicleitem_90.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_90.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_90.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_90.itemSize = 3L
    shipBuilder_vehicleitem_90.views = 283L
    shipBuilder_vehicleitem_90 = importer.save_or_locate(shipBuilder_vehicleitem_90)

    shipBuilder_vehicleitem_90.power.add(shipBuilder_vehicleitempower_36)

    shipBuilder_vehicleitem_91 = VehicleItem()
    shipBuilder_vehicleitem_91.itemClass = 0L
    shipBuilder_vehicleitem_91.description = u"A and R's LR-5 OverDrive is your gateway to the world of fusion-based power plants. Designed to be a rugged, high-output alternative to other power sources, the LR-5 OverDrive does suffer from an above average generation of heat."
    shipBuilder_vehicleitem_91.name = u'A_and_R-5_OverDrive'
    shipBuilder_vehicleitem_91.displayName = u'A&R LR-5 OverDrive'
    shipBuilder_vehicleitem_91.itemType = shipBuilder_vehicleitemtype_4
    shipBuilder_vehicleitem_91.itemSubType = shipBuilder_vehicleitemsubtype_5
    shipBuilder_vehicleitem_91.manufacturer = shipBuilder_manufacturer_36
    shipBuilder_vehicleitem_91.itemSize = 1L
    shipBuilder_vehicleitem_91.views = 79L
    shipBuilder_vehicleitem_91 = importer.save_or_locate(shipBuilder_vehicleitem_91)

    shipBuilder_vehicleitem_91.power.add(shipBuilder_vehicleitempower_73)

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
    shipBuilder_vehicle_1.views = 415L
    shipBuilder_vehicle_1.upgradeSlots = 0L
    shipBuilder_vehicle_1.maximum_crew = 1L
    shipBuilder_vehicle_1.empty_mass = 0L
    shipBuilder_vehicle_1.length = 0.0
    shipBuilder_vehicle_1.width = 0.0
    shipBuilder_vehicle_1.height = 0.0
    shipBuilder_vehicle_1.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/freelancer.jpg'
    shipBuilder_vehicle_1.available = False
    shipBuilder_vehicle_1.manufacturer = shipBuilder_manufacturer_47
    shipBuilder_vehicle_1.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/freelancer-top-right.jpeg'
    shipBuilder_vehicle_1.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/freelancer-top-left.jpeg'
    shipBuilder_vehicle_1.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/freelancer-bottom-right.jpeg'
    shipBuilder_vehicle_1.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/freelancer-bottom-left.jpeg'
    shipBuilder_vehicle_1 = importer.save_or_locate(shipBuilder_vehicle_1)

    shipBuilder_vehicle_2 = Vehicle()
    shipBuilder_vehicle_2.vehicleClass = 2L
    shipBuilder_vehicle_2.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_2.displayName = u'Anvil Hornet'
    shipBuilder_vehicle_2.name = u'Anvil_Hornet'
    shipBuilder_vehicle_2.views = 267L
    shipBuilder_vehicle_2.upgradeSlots = 0L
    shipBuilder_vehicle_2.maximum_crew = 1L
    shipBuilder_vehicle_2.empty_mass = 0L
    shipBuilder_vehicle_2.length = 0.0
    shipBuilder_vehicle_2.width = 0.0
    shipBuilder_vehicle_2.height = 0.0
    shipBuilder_vehicle_2.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/hornet.jpg'
    shipBuilder_vehicle_2.available = False
    shipBuilder_vehicle_2.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicle_2.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-top-right.jpeg'
    shipBuilder_vehicle_2.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-top-left.jpeg'
    shipBuilder_vehicle_2.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-bottom-right.jpeg'
    shipBuilder_vehicle_2.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-bottom-left.jpeg'
    shipBuilder_vehicle_2 = importer.save_or_locate(shipBuilder_vehicle_2)

    shipBuilder_vehicle_3 = Vehicle()
    shipBuilder_vehicle_3.vehicleClass = 3L
    shipBuilder_vehicle_3.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_3.displayName = u'RSI Constellation'
    shipBuilder_vehicle_3.name = u'RSI_Constellation'
    shipBuilder_vehicle_3.views = 344L
    shipBuilder_vehicle_3.upgradeSlots = 0L
    shipBuilder_vehicle_3.maximum_crew = 1L
    shipBuilder_vehicle_3.empty_mass = 0L
    shipBuilder_vehicle_3.length = 0.0
    shipBuilder_vehicle_3.width = 0.0
    shipBuilder_vehicle_3.height = 0.0
    shipBuilder_vehicle_3.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/constellation.jpg'
    shipBuilder_vehicle_3.available = False
    shipBuilder_vehicle_3.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_vehicle_3.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/constellation-top-right.jpeg'
    shipBuilder_vehicle_3.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/constellation-top-left.jpeg'
    shipBuilder_vehicle_3.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/constellation-bottom-right.jpeg'
    shipBuilder_vehicle_3.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/constellation-bottom-left.jpeg'
    shipBuilder_vehicle_3 = importer.save_or_locate(shipBuilder_vehicle_3)

    shipBuilder_vehicle_4 = Vehicle()
    shipBuilder_vehicle_4.vehicleClass = 1L
    shipBuilder_vehicle_4.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_4.displayName = u'RSI Aurora LX'
    shipBuilder_vehicle_4.name = u'RSI_Aurora_LX'
    shipBuilder_vehicle_4.views = 152L
    shipBuilder_vehicle_4.upgradeSlots = 0L
    shipBuilder_vehicle_4.maximum_crew = 1L
    shipBuilder_vehicle_4.empty_mass = 0L
    shipBuilder_vehicle_4.length = 0.0
    shipBuilder_vehicle_4.width = 0.0
    shipBuilder_vehicle_4.height = 0.0
    shipBuilder_vehicle_4.thumbnail = u''
    shipBuilder_vehicle_4.available = False
    shipBuilder_vehicle_4.manufacturer = None
    shipBuilder_vehicle_4.layoutImageTopRight = None
    shipBuilder_vehicle_4.layoutImageTopLeft = None
    shipBuilder_vehicle_4.layoutImageBottomRight = None
    shipBuilder_vehicle_4.layoutImageBottomLeft = None
    shipBuilder_vehicle_4 = importer.save_or_locate(shipBuilder_vehicle_4)

    shipBuilder_vehicle_5 = Vehicle()
    shipBuilder_vehicle_5.vehicleClass = 1L
    shipBuilder_vehicle_5.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_5.displayName = u'RSI Aurora ES'
    shipBuilder_vehicle_5.name = u'RSI_Aurora_ES'
    shipBuilder_vehicle_5.views = 103L
    shipBuilder_vehicle_5.upgradeSlots = 0L
    shipBuilder_vehicle_5.maximum_crew = 1L
    shipBuilder_vehicle_5.empty_mass = 0L
    shipBuilder_vehicle_5.length = 0.0
    shipBuilder_vehicle_5.width = 0.0
    shipBuilder_vehicle_5.height = 0.0
    shipBuilder_vehicle_5.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/auroraes.jpg'
    shipBuilder_vehicle_5.available = False
    shipBuilder_vehicle_5.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_vehicle_5.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/aurora_es-top-right.jpeg'
    shipBuilder_vehicle_5.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/aurora_es-top-left.jpeg'
    shipBuilder_vehicle_5.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/aurora_es-bottom-right.jpeg'
    shipBuilder_vehicle_5.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/aurora_es-bottom-left.jpeg'
    shipBuilder_vehicle_5 = importer.save_or_locate(shipBuilder_vehicle_5)

    shipBuilder_vehicle_6 = Vehicle()
    shipBuilder_vehicle_6.vehicleClass = 2L
    shipBuilder_vehicle_6.category = shipBuilder_vehiclecategory_3
    shipBuilder_vehicle_6.displayName = u'Anvil Hornet F7C'
    shipBuilder_vehicle_6.name = u'Anvil_Hornet_F7C'
    shipBuilder_vehicle_6.views = 190L
    shipBuilder_vehicle_6.upgradeSlots = 0L
    shipBuilder_vehicle_6.maximum_crew = 1L
    shipBuilder_vehicle_6.empty_mass = 0L
    shipBuilder_vehicle_6.length = 0.0
    shipBuilder_vehicle_6.width = 0.0
    shipBuilder_vehicle_6.height = 0.0
    shipBuilder_vehicle_6.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/hornet.jpg'
    shipBuilder_vehicle_6.available = False
    shipBuilder_vehicle_6.manufacturer = shipBuilder_manufacturer_27
    shipBuilder_vehicle_6.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-top-right.jpeg'
    shipBuilder_vehicle_6.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-top-left.jpeg'
    shipBuilder_vehicle_6.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-bottom-right.jpeg'
    shipBuilder_vehicle_6.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/hornet-bottom-left.jpeg'
    shipBuilder_vehicle_6 = importer.save_or_locate(shipBuilder_vehicle_6)

    shipBuilder_vehicle_7 = Vehicle()
    shipBuilder_vehicle_7.vehicleClass = 2L
    shipBuilder_vehicle_7.category = shipBuilder_vehiclecategory_3
    shipBuilder_vehicle_7.displayName = u'Origin Jumpworks 350r'
    shipBuilder_vehicle_7.name = u'OJ_350r'
    shipBuilder_vehicle_7.views = 209L
    shipBuilder_vehicle_7.upgradeSlots = 0L
    shipBuilder_vehicle_7.maximum_crew = 1L
    shipBuilder_vehicle_7.empty_mass = 0L
    shipBuilder_vehicle_7.length = 0.0
    shipBuilder_vehicle_7.width = 0.0
    shipBuilder_vehicle_7.height = 0.0
    shipBuilder_vehicle_7.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/350r.jpg'
    shipBuilder_vehicle_7.available = False
    shipBuilder_vehicle_7.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_vehicle_7.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/350r-top-right.jpeg'
    shipBuilder_vehicle_7.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/350r-top-left.jpeg'
    shipBuilder_vehicle_7.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/350r-bottom-right.jpeg'
    shipBuilder_vehicle_7.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/350r-bottom-left.jpeg'
    shipBuilder_vehicle_7 = importer.save_or_locate(shipBuilder_vehicle_7)

    shipBuilder_vehicle_8 = Vehicle()
    shipBuilder_vehicle_8.vehicleClass = 3L
    shipBuilder_vehicle_8.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_8.displayName = u'Origin JumpWorks 315p'
    shipBuilder_vehicle_8.name = u'OJ_315p'
    shipBuilder_vehicle_8.views = 196L
    shipBuilder_vehicle_8.upgradeSlots = 0L
    shipBuilder_vehicle_8.maximum_crew = 1L
    shipBuilder_vehicle_8.empty_mass = 0L
    shipBuilder_vehicle_8.length = 0.0
    shipBuilder_vehicle_8.width = 0.0
    shipBuilder_vehicle_8.height = 0.0
    shipBuilder_vehicle_8.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/300ijpg'
    shipBuilder_vehicle_8.available = False
    shipBuilder_vehicle_8.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_vehicle_8.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/315p-top-right.jpeg'
    shipBuilder_vehicle_8.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/315p-top-left.jpeg'
    shipBuilder_vehicle_8.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/315p-bottom-right.jpeg'
    shipBuilder_vehicle_8.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/315p-bottom-left.jpeg'
    shipBuilder_vehicle_8 = importer.save_or_locate(shipBuilder_vehicle_8)

    shipBuilder_vehicle_9 = Vehicle()
    shipBuilder_vehicle_9.vehicleClass = 1L
    shipBuilder_vehicle_9.category = shipBuilder_vehiclecategory_3
    shipBuilder_vehicle_9.displayName = u'RSI Aurora MR'
    shipBuilder_vehicle_9.name = u'RSI_Aurora_MR'
    shipBuilder_vehicle_9.views = 90L
    shipBuilder_vehicle_9.upgradeSlots = 0L
    shipBuilder_vehicle_9.maximum_crew = 1L
    shipBuilder_vehicle_9.empty_mass = 0L
    shipBuilder_vehicle_9.length = 0.0
    shipBuilder_vehicle_9.width = 0.0
    shipBuilder_vehicle_9.height = 0.0
    shipBuilder_vehicle_9.thumbnail = u''
    shipBuilder_vehicle_9.available = False
    shipBuilder_vehicle_9.manufacturer = None
    shipBuilder_vehicle_9.layoutImageTopRight = None
    shipBuilder_vehicle_9.layoutImageTopLeft = None
    shipBuilder_vehicle_9.layoutImageBottomRight = None
    shipBuilder_vehicle_9.layoutImageBottomLeft = None
    shipBuilder_vehicle_9 = importer.save_or_locate(shipBuilder_vehicle_9)

    shipBuilder_vehicle_10 = Vehicle()
    shipBuilder_vehicle_10.vehicleClass = 3L
    shipBuilder_vehicle_10.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_10.displayName = u'Origin JumpWorks 300i'
    shipBuilder_vehicle_10.name = u'OJ_300i'
    shipBuilder_vehicle_10.views = 149L
    shipBuilder_vehicle_10.upgradeSlots = 0L
    shipBuilder_vehicle_10.maximum_crew = 1L
    shipBuilder_vehicle_10.empty_mass = 0L
    shipBuilder_vehicle_10.length = 0.0
    shipBuilder_vehicle_10.width = 0.0
    shipBuilder_vehicle_10.height = 0.0
    shipBuilder_vehicle_10.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/300i.jpg'
    shipBuilder_vehicle_10.available = False
    shipBuilder_vehicle_10.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_vehicle_10.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/300i-top-right.jpeg'
    shipBuilder_vehicle_10.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/300i-top-left.jpeg'
    shipBuilder_vehicle_10.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/300i-bottom-right.jpeg'
    shipBuilder_vehicle_10.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/300i-bottom-left.jpeg'
    shipBuilder_vehicle_10 = importer.save_or_locate(shipBuilder_vehicle_10)

    shipBuilder_vehicle_11 = Vehicle()
    shipBuilder_vehicle_11.vehicleClass = 1L
    shipBuilder_vehicle_11.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_11.displayName = u'RSI Aurora CL'
    shipBuilder_vehicle_11.name = u'RSI_Aurora_CL'
    shipBuilder_vehicle_11.views = 118L
    shipBuilder_vehicle_11.upgradeSlots = 0L
    shipBuilder_vehicle_11.maximum_crew = 1L
    shipBuilder_vehicle_11.empty_mass = 0L
    shipBuilder_vehicle_11.length = 0.0
    shipBuilder_vehicle_11.width = 0.0
    shipBuilder_vehicle_11.height = 0.0
    shipBuilder_vehicle_11.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/auroracl.jpg'
    shipBuilder_vehicle_11.available = False
    shipBuilder_vehicle_11.manufacturer = shipBuilder_manufacturer_6
    shipBuilder_vehicle_11.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/aurora_cl-top-right.png'
    shipBuilder_vehicle_11.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/aurora_cl-top-left.png'
    shipBuilder_vehicle_11.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/aurora_cl-bottom-right.png'
    shipBuilder_vehicle_11.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/aurora_cl-bottom-left.png'
    shipBuilder_vehicle_11 = importer.save_or_locate(shipBuilder_vehicle_11)

    shipBuilder_vehicle_12 = Vehicle()
    shipBuilder_vehicle_12.vehicleClass = 3L
    shipBuilder_vehicle_12.category = shipBuilder_vehiclecategory_2
    shipBuilder_vehicle_12.displayName = u'Origin JumpWorks 325a'
    shipBuilder_vehicle_12.name = u'OJ_325a'
    shipBuilder_vehicle_12.views = 230L
    shipBuilder_vehicle_12.upgradeSlots = 0L
    shipBuilder_vehicle_12.maximum_crew = 1L
    shipBuilder_vehicle_12.empty_mass = 0L
    shipBuilder_vehicle_12.length = 0.0
    shipBuilder_vehicle_12.width = 0.0
    shipBuilder_vehicle_12.height = 0.0
    shipBuilder_vehicle_12.thumbnail = u'https://www.stantonspacebarn.com/static/images/ship_thumbnails/300i.jpg'
    shipBuilder_vehicle_12.available = False
    shipBuilder_vehicle_12.manufacturer = shipBuilder_manufacturer_1
    shipBuilder_vehicle_12.layoutImageTopRight = u'https://www.stantonspacebarn.com/static/images/ship_images/325a-top-right.jpeg'
    shipBuilder_vehicle_12.layoutImageTopLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/325a-top-left.jpeg'
    shipBuilder_vehicle_12.layoutImageBottomRight = u'https://www.stantonspacebarn.com/static/images/ship_images/325a-bottom-right.jpeg'
    shipBuilder_vehicle_12.layoutImageBottomLeft = u'https://www.stantonspacebarn.com/static/images/ship_images/325a-bottom-left.jpeg'
    shipBuilder_vehicle_12 = importer.save_or_locate(shipBuilder_vehicle_12)

    #Processing model: MigrationHistory

    from south.models import MigrationHistory

    south_migrationhistory_1 = MigrationHistory()
    south_migrationhistory_1.app_name = u'shipBuilder'
    south_migrationhistory_1.migration = u'0001_initial'
    south_migrationhistory_1.applied = datetime.datetime(2013, 9, 7, 21, 40, 43)
    south_migrationhistory_1 = importer.save_or_locate(south_migrationhistory_1)

    south_migrationhistory_2 = MigrationHistory()
    south_migrationhistory_2.app_name = u'shipBuilder'
    south_migrationhistory_2.migration = u'0002_auto__add_field_itemport_parentImage'
    south_migrationhistory_2.applied = datetime.datetime(2013, 9, 8, 20, 36, 46)
    south_migrationhistory_2 = importer.save_or_locate(south_migrationhistory_2)

    #Processing model: LogEntry

    from django.contrib.admin.models import LogEntry

    django_admin_log_1 = LogEntry()
    django_admin_log_1.action_time = datetime.datetime(2013, 9, 13, 2, 53, 27)
    django_admin_log_1.user = auth_user_1
    django_admin_log_1.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_1.object_id = u'308'
    django_admin_log_1.object_repr = u'RSI Aurora CL Class 1 StarFighter: Right Whisker Class 1 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_1.action_flag = 2
    django_admin_log_1.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_1 = importer.save_or_locate(django_admin_log_1)

    django_admin_log_2 = LogEntry()
    django_admin_log_2.action_time = datetime.datetime(2013, 9, 13, 2, 52, 53)
    django_admin_log_2.user = auth_user_1
    django_admin_log_2.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_2.object_id = u'307'
    django_admin_log_2.object_repr = u'RSI Aurora CL Class 1 StarFighter: Left Whisker Class 1 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_2.action_flag = 2
    django_admin_log_2.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_2 = importer.save_or_locate(django_admin_log_2)

    django_admin_log_3 = LogEntry()
    django_admin_log_3.action_time = datetime.datetime(2013, 9, 13, 2, 39, 53)
    django_admin_log_3.user = auth_user_1
    django_admin_log_3.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_3.object_id = u'306'
    django_admin_log_3.object_repr = u'RSI Aurora CL Class 1 StarFighter: Class 3 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_3.action_flag = 2
    django_admin_log_3.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_3 = importer.save_or_locate(django_admin_log_3)

    django_admin_log_4 = LogEntry()
    django_admin_log_4.action_time = datetime.datetime(2013, 9, 13, 2, 38, 58)
    django_admin_log_4.user = auth_user_1
    django_admin_log_4.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_4.object_id = u'299'
    django_admin_log_4.object_repr = u'RSI Aurora CL Class 1 StarFighter: hardpoint_engine_attach (2-3) [<VehicleItemType: Thruster>]'
    django_admin_log_4.action_flag = 2
    django_admin_log_4.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_4 = importer.save_or_locate(django_admin_log_4)

    django_admin_log_5 = LogEntry()
    django_admin_log_5.action_time = datetime.datetime(2013, 9, 13, 2, 35, 9)
    django_admin_log_5.user = auth_user_1
    django_admin_log_5.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_5.object_id = u'11'
    django_admin_log_5.object_repr = u'RSI Aurora CL Class 1 StarFighter'
    django_admin_log_5.action_flag = 2
    django_admin_log_5.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_5 = importer.save_or_locate(django_admin_log_5)

    django_admin_log_6 = LogEntry()
    django_admin_log_6.action_time = datetime.datetime(2013, 9, 13, 1, 22, 11)
    django_admin_log_6.user = auth_user_1
    django_admin_log_6.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_6.object_id = u'10'
    django_admin_log_6.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter'
    django_admin_log_6.action_flag = 2
    django_admin_log_6.change_message = u'Changed layoutImageTopLeft.'
    django_admin_log_6 = importer.save_or_locate(django_admin_log_6)

    django_admin_log_7 = LogEntry()
    django_admin_log_7.action_time = datetime.datetime(2013, 9, 12, 0, 59, 38)
    django_admin_log_7.user = auth_user_1
    django_admin_log_7.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_7.object_id = u'323'
    django_admin_log_7.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_7.action_flag = 2
    django_admin_log_7.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_7 = importer.save_or_locate(django_admin_log_7)

    django_admin_log_8 = LogEntry()
    django_admin_log_8.action_time = datetime.datetime(2013, 9, 12, 0, 59, 18)
    django_admin_log_8.user = auth_user_1
    django_admin_log_8.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_8.object_id = u'323'
    django_admin_log_8.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_8.action_flag = 2
    django_admin_log_8.change_message = u'Changed tagLocationY.'
    django_admin_log_8 = importer.save_or_locate(django_admin_log_8)

    django_admin_log_9 = LogEntry()
    django_admin_log_9.action_time = datetime.datetime(2013, 9, 12, 0, 58, 57)
    django_admin_log_9.user = auth_user_1
    django_admin_log_9.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_9.object_id = u'323'
    django_admin_log_9.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_9.action_flag = 2
    django_admin_log_9.change_message = u'Changed tagLocationY.'
    django_admin_log_9 = importer.save_or_locate(django_admin_log_9)

    django_admin_log_10 = LogEntry()
    django_admin_log_10.action_time = datetime.datetime(2013, 9, 12, 0, 58, 43)
    django_admin_log_10.user = auth_user_1
    django_admin_log_10.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_10.object_id = u'323'
    django_admin_log_10.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_10.action_flag = 2
    django_admin_log_10.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_10 = importer.save_or_locate(django_admin_log_10)

    django_admin_log_11 = LogEntry()
    django_admin_log_11.action_time = datetime.datetime(2013, 9, 12, 0, 58, 13)
    django_admin_log_11.user = auth_user_1
    django_admin_log_11.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_11.object_id = u'325'
    django_admin_log_11.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_11.action_flag = 2
    django_admin_log_11.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_11 = importer.save_or_locate(django_admin_log_11)

    django_admin_log_12 = LogEntry()
    django_admin_log_12.action_time = datetime.datetime(2013, 9, 12, 0, 57, 33)
    django_admin_log_12.user = auth_user_1
    django_admin_log_12.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_12.object_id = u'324'
    django_admin_log_12.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Left Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_12.action_flag = 2
    django_admin_log_12.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_12 = importer.save_or_locate(django_admin_log_12)

    django_admin_log_13 = LogEntry()
    django_admin_log_13.action_time = datetime.datetime(2013, 9, 12, 0, 56, 59)
    django_admin_log_13.user = auth_user_1
    django_admin_log_13.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_13.object_id = u'327'
    django_admin_log_13.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Right Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_13.action_flag = 2
    django_admin_log_13.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_13 = importer.save_or_locate(django_admin_log_13)

    django_admin_log_14 = LogEntry()
    django_admin_log_14.action_time = datetime.datetime(2013, 9, 12, 0, 56, 34)
    django_admin_log_14.user = auth_user_1
    django_admin_log_14.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_14.object_id = u'326'
    django_admin_log_14.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Right Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_14.action_flag = 2
    django_admin_log_14.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_14 = importer.save_or_locate(django_admin_log_14)

    django_admin_log_15 = LogEntry()
    django_admin_log_15.action_time = datetime.datetime(2013, 9, 12, 0, 56, 1)
    django_admin_log_15.user = auth_user_1
    django_admin_log_15.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_15.object_id = u'310'
    django_admin_log_15.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_15.action_flag = 2
    django_admin_log_15.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_15 = importer.save_or_locate(django_admin_log_15)

    django_admin_log_16 = LogEntry()
    django_admin_log_16.action_time = datetime.datetime(2013, 9, 12, 0, 55, 26)
    django_admin_log_16.user = auth_user_1
    django_admin_log_16.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_16.object_id = u'12'
    django_admin_log_16.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter'
    django_admin_log_16.action_flag = 2
    django_admin_log_16.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_16 = importer.save_or_locate(django_admin_log_16)

    django_admin_log_17 = LogEntry()
    django_admin_log_17.action_time = datetime.datetime(2013, 9, 12, 0, 54, 40)
    django_admin_log_17.user = auth_user_1
    django_admin_log_17.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_17.object_id = u'309'
    django_admin_log_17.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter: Power Plant (2-3) [<VehicleItemType: PowerPlant>]'
    django_admin_log_17.action_flag = 2
    django_admin_log_17.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_17 = importer.save_or_locate(django_admin_log_17)

    django_admin_log_18 = LogEntry()
    django_admin_log_18.action_time = datetime.datetime(2013, 9, 12, 0, 53, 53)
    django_admin_log_18.user = auth_user_1
    django_admin_log_18.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_18.object_id = u'12'
    django_admin_log_18.object_repr = u'Origin JumpWorks 325a Class 3 StarFighter'
    django_admin_log_18.action_flag = 2
    django_admin_log_18.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_18 = importer.save_or_locate(django_admin_log_18)

    django_admin_log_19 = LogEntry()
    django_admin_log_19.action_time = datetime.datetime(2013, 9, 11, 22, 57, 38)
    django_admin_log_19.user = auth_user_1
    django_admin_log_19.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_19.object_id = u'223'
    django_admin_log_19.object_repr = u'Anvil Hornet F7C Class 2 Star Fighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_19.action_flag = 2
    django_admin_log_19.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_19 = importer.save_or_locate(django_admin_log_19)

    django_admin_log_20 = LogEntry()
    django_admin_log_20.action_time = datetime.datetime(2013, 9, 11, 22, 56, 52)
    django_admin_log_20.user = auth_user_1
    django_admin_log_20.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_20.object_id = u'222'
    django_admin_log_20.object_repr = u'Anvil Hornet F7C Class 2 Star Fighter: Power Plant (2-3) [<VehicleItemType: PowerPlant>]'
    django_admin_log_20.action_flag = 2
    django_admin_log_20.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_20 = importer.save_or_locate(django_admin_log_20)

    django_admin_log_21 = LogEntry()
    django_admin_log_21.action_time = datetime.datetime(2013, 9, 11, 22, 56, 8)
    django_admin_log_21.user = auth_user_1
    django_admin_log_21.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_21.object_id = u'221'
    django_admin_log_21.object_repr = u'Anvil Hornet F7C Class 2 Star Fighter: Left Nose Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_21.action_flag = 2
    django_admin_log_21.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_21 = importer.save_or_locate(django_admin_log_21)

    django_admin_log_22 = LogEntry()
    django_admin_log_22.action_time = datetime.datetime(2013, 9, 11, 22, 55, 9)
    django_admin_log_22.user = auth_user_1
    django_admin_log_22.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_22.object_id = u'6'
    django_admin_log_22.object_repr = u'Anvil Hornet F7C Class 2 Star Fighter'
    django_admin_log_22.action_flag = 2
    django_admin_log_22.change_message = u'Changed layoutImageBottomRight.'
    django_admin_log_22 = importer.save_or_locate(django_admin_log_22)

    django_admin_log_23 = LogEntry()
    django_admin_log_23.action_time = datetime.datetime(2013, 9, 11, 22, 36, 39)
    django_admin_log_23.user = auth_user_1
    django_admin_log_23.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_23.object_id = u'220'
    django_admin_log_23.object_repr = u'Anvil Hornet F7C Class 2 Star Fighter: Right Nose Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_23.action_flag = 2
    django_admin_log_23.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_23 = importer.save_or_locate(django_admin_log_23)

    django_admin_log_24 = LogEntry()
    django_admin_log_24.action_time = datetime.datetime(2013, 9, 11, 22, 33, 20)
    django_admin_log_24.user = auth_user_1
    django_admin_log_24.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_24.object_id = u'6'
    django_admin_log_24.object_repr = u'Anvil Hornet F7C Class 2 Star Fighter'
    django_admin_log_24.action_flag = 2
    django_admin_log_24.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_24 = importer.save_or_locate(django_admin_log_24)

    django_admin_log_25 = LogEntry()
    django_admin_log_25.action_time = datetime.datetime(2013, 9, 11, 22, 8)
    django_admin_log_25.user = auth_user_1
    django_admin_log_25.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_25.object_id = u'1'
    django_admin_log_25.object_repr = u'MISC Freelancer Class 3 Transport'
    django_admin_log_25.action_flag = 2
    django_admin_log_25.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_25 = importer.save_or_locate(django_admin_log_25)

    django_admin_log_26 = LogEntry()
    django_admin_log_26.action_time = datetime.datetime(2013, 9, 11, 22, 7, 19)
    django_admin_log_26.user = auth_user_1
    django_admin_log_26.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_26.object_id = u'3'
    django_admin_log_26.object_repr = u'RSI Constellation Class 3 StarFighter'
    django_admin_log_26.action_flag = 2
    django_admin_log_26.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_26 = importer.save_or_locate(django_admin_log_26)

    django_admin_log_27 = LogEntry()
    django_admin_log_27.action_time = datetime.datetime(2013, 9, 11, 22, 5, 53)
    django_admin_log_27.user = auth_user_1
    django_admin_log_27.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_27.object_id = u'5'
    django_admin_log_27.object_repr = u'RSI Aurora ES Class 1 StarFighter'
    django_admin_log_27.action_flag = 2
    django_admin_log_27.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_27 = importer.save_or_locate(django_admin_log_27)

    django_admin_log_28 = LogEntry()
    django_admin_log_28.action_time = datetime.datetime(2013, 9, 11, 22, 5, 2)
    django_admin_log_28.user = auth_user_1
    django_admin_log_28.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_28.object_id = u'7'
    django_admin_log_28.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter'
    django_admin_log_28.action_flag = 2
    django_admin_log_28.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_28 = importer.save_or_locate(django_admin_log_28)

    django_admin_log_29 = LogEntry()
    django_admin_log_29.action_time = datetime.datetime(2013, 9, 11, 22, 4, 20)
    django_admin_log_29.user = auth_user_1
    django_admin_log_29.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_29.object_id = u'8'
    django_admin_log_29.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter'
    django_admin_log_29.action_flag = 2
    django_admin_log_29.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_29 = importer.save_or_locate(django_admin_log_29)

    django_admin_log_30 = LogEntry()
    django_admin_log_30.action_time = datetime.datetime(2013, 9, 11, 22, 3, 28)
    django_admin_log_30.user = auth_user_1
    django_admin_log_30.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_30.object_id = u'10'
    django_admin_log_30.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter'
    django_admin_log_30.action_flag = 2
    django_admin_log_30.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_30 = importer.save_or_locate(django_admin_log_30)

    django_admin_log_31 = LogEntry()
    django_admin_log_31.action_time = datetime.datetime(2013, 9, 11, 21, 47, 15)
    django_admin_log_31.user = auth_user_1
    django_admin_log_31.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_31.object_id = u'2'
    django_admin_log_31.object_repr = u'Anvil Hornet Class 2 StarFighter'
    django_admin_log_31.action_flag = 2
    django_admin_log_31.change_message = u'Changed layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_31 = importer.save_or_locate(django_admin_log_31)

    django_admin_log_32 = LogEntry()
    django_admin_log_32.action_time = datetime.datetime(2013, 9, 11, 18, 4, 6)
    django_admin_log_32.user = auth_user_1
    django_admin_log_32.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_32.object_id = u'269'
    django_admin_log_32.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Right Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_32.action_flag = 2
    django_admin_log_32.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_32 = importer.save_or_locate(django_admin_log_32)

    django_admin_log_33 = LogEntry()
    django_admin_log_33.action_time = datetime.datetime(2013, 9, 11, 18, 3, 39)
    django_admin_log_33.user = auth_user_1
    django_admin_log_33.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_33.object_id = u'268'
    django_admin_log_33.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Right Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_33.action_flag = 2
    django_admin_log_33.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_33 = importer.save_or_locate(django_admin_log_33)

    django_admin_log_34 = LogEntry()
    django_admin_log_34.action_time = datetime.datetime(2013, 9, 11, 18, 3, 4)
    django_admin_log_34.user = auth_user_1
    django_admin_log_34.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_34.object_id = u'267'
    django_admin_log_34.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_34.action_flag = 2
    django_admin_log_34.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_34 = importer.save_or_locate(django_admin_log_34)

    django_admin_log_35 = LogEntry()
    django_admin_log_35.action_time = datetime.datetime(2013, 9, 11, 18, 2, 27)
    django_admin_log_35.user = auth_user_1
    django_admin_log_35.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_35.object_id = u'266'
    django_admin_log_35.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Left Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_35.action_flag = 2
    django_admin_log_35.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_35 = importer.save_or_locate(django_admin_log_35)

    django_admin_log_36 = LogEntry()
    django_admin_log_36.action_time = datetime.datetime(2013, 9, 11, 18, 2, 8)
    django_admin_log_36.user = auth_user_1
    django_admin_log_36.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_36.object_id = u'266'
    django_admin_log_36.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Left Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_36.action_flag = 2
    django_admin_log_36.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_36 = importer.save_or_locate(django_admin_log_36)

    django_admin_log_37 = LogEntry()
    django_admin_log_37.action_time = datetime.datetime(2013, 9, 11, 18, 1, 33)
    django_admin_log_37.user = auth_user_1
    django_admin_log_37.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_37.object_id = u'265'
    django_admin_log_37.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_37.action_flag = 2
    django_admin_log_37.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_37 = importer.save_or_locate(django_admin_log_37)

    django_admin_log_38 = LogEntry()
    django_admin_log_38.action_time = datetime.datetime(2013, 9, 11, 17, 59, 41)
    django_admin_log_38.user = auth_user_1
    django_admin_log_38.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_38.object_id = u'252'
    django_admin_log_38.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_38.action_flag = 2
    django_admin_log_38.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_38 = importer.save_or_locate(django_admin_log_38)

    django_admin_log_39 = LogEntry()
    django_admin_log_39.action_time = datetime.datetime(2013, 9, 11, 17, 58, 42)
    django_admin_log_39.user = auth_user_1
    django_admin_log_39.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_39.object_id = u'251'
    django_admin_log_39.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter: Power Plant (2-3) [<VehicleItemType: PowerPlant>]'
    django_admin_log_39.action_flag = 2
    django_admin_log_39.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_39 = importer.save_or_locate(django_admin_log_39)

    django_admin_log_40 = LogEntry()
    django_admin_log_40.action_time = datetime.datetime(2013, 9, 11, 17, 57, 51)
    django_admin_log_40.user = auth_user_1
    django_admin_log_40.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_40.object_id = u'8'
    django_admin_log_40.object_repr = u'Origin JumpWorks 315p Class 3 StarFighter'
    django_admin_log_40.action_flag = 2
    django_admin_log_40.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_40 = importer.save_or_locate(django_admin_log_40)

    django_admin_log_41 = LogEntry()
    django_admin_log_41.action_time = datetime.datetime(2013, 9, 11, 15, 49, 37)
    django_admin_log_41.user = auth_user_1
    django_admin_log_41.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_41.object_id = u'219'
    django_admin_log_41.object_repr = u'RSI Aurora ES Class 1 StarFighter: Right Whisker Class 1 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_41.action_flag = 2
    django_admin_log_41.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_41 = importer.save_or_locate(django_admin_log_41)

    django_admin_log_42 = LogEntry()
    django_admin_log_42.action_time = datetime.datetime(2013, 9, 11, 15, 49, 6)
    django_admin_log_42.user = auth_user_1
    django_admin_log_42.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_42.object_id = u'218'
    django_admin_log_42.object_repr = u'RSI Aurora ES Class 1 StarFighter: Left Whisker Class 1 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_42.action_flag = 2
    django_admin_log_42.change_message = u'Changed tagLocationY.'
    django_admin_log_42 = importer.save_or_locate(django_admin_log_42)

    django_admin_log_43 = LogEntry()
    django_admin_log_43.action_time = datetime.datetime(2013, 9, 11, 15, 48, 51)
    django_admin_log_43.user = auth_user_1
    django_admin_log_43.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_43.object_id = u'218'
    django_admin_log_43.object_repr = u'RSI Aurora ES Class 1 StarFighter: Left Whisker Class 1 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_43.action_flag = 2
    django_admin_log_43.change_message = u'Changed tagLocationY.'
    django_admin_log_43 = importer.save_or_locate(django_admin_log_43)

    django_admin_log_44 = LogEntry()
    django_admin_log_44.action_time = datetime.datetime(2013, 9, 11, 15, 48, 35)
    django_admin_log_44.user = auth_user_1
    django_admin_log_44.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_44.object_id = u'218'
    django_admin_log_44.object_repr = u'RSI Aurora ES Class 1 StarFighter: Left Whisker Class 1 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_44.action_flag = 2
    django_admin_log_44.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_44 = importer.save_or_locate(django_admin_log_44)

    django_admin_log_45 = LogEntry()
    django_admin_log_45.action_time = datetime.datetime(2013, 9, 11, 15, 47, 53)
    django_admin_log_45.user = auth_user_1
    django_admin_log_45.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_45.object_id = u'217'
    django_admin_log_45.object_repr = u'RSI Aurora ES Class 1 StarFighter: Class 3 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_45.action_flag = 2
    django_admin_log_45.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_45 = importer.save_or_locate(django_admin_log_45)

    django_admin_log_46 = LogEntry()
    django_admin_log_46.action_time = datetime.datetime(2013, 9, 11, 15, 47, 34)
    django_admin_log_46.user = auth_user_1
    django_admin_log_46.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_46.object_id = u'217'
    django_admin_log_46.object_repr = u'RSI Aurora ES Class 1 StarFighter: Class 3 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_46.action_flag = 2
    django_admin_log_46.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_46 = importer.save_or_locate(django_admin_log_46)

    django_admin_log_47 = LogEntry()
    django_admin_log_47.action_time = datetime.datetime(2013, 9, 11, 15, 47, 15)
    django_admin_log_47.user = auth_user_1
    django_admin_log_47.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_47.object_id = u'217'
    django_admin_log_47.object_repr = u'RSI Aurora ES Class 1 StarFighter: Class 3 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_47.action_flag = 2
    django_admin_log_47.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_47 = importer.save_or_locate(django_admin_log_47)

    django_admin_log_48 = LogEntry()
    django_admin_log_48.action_time = datetime.datetime(2013, 9, 11, 15, 46)
    django_admin_log_48.user = auth_user_1
    django_admin_log_48.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_48.object_id = u'210'
    django_admin_log_48.object_repr = u'RSI Aurora ES Class 1 StarFighter: hardpoint_engine_attach (2-3) [<VehicleItemType: Thruster>]'
    django_admin_log_48.action_flag = 2
    django_admin_log_48.change_message = u'Changed tagLocationY.'
    django_admin_log_48 = importer.save_or_locate(django_admin_log_48)

    django_admin_log_49 = LogEntry()
    django_admin_log_49.action_time = datetime.datetime(2013, 9, 11, 15, 45, 31)
    django_admin_log_49.user = auth_user_1
    django_admin_log_49.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_49.object_id = u'210'
    django_admin_log_49.object_repr = u'RSI Aurora ES Class 1 StarFighter: hardpoint_engine_attach (2-3) [<VehicleItemType: Thruster>]'
    django_admin_log_49.action_flag = 2
    django_admin_log_49.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_49 = importer.save_or_locate(django_admin_log_49)

    django_admin_log_50 = LogEntry()
    django_admin_log_50.action_time = datetime.datetime(2013, 9, 11, 15, 42, 42)
    django_admin_log_50.user = auth_user_1
    django_admin_log_50.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_50.object_id = u'5'
    django_admin_log_50.object_repr = u'RSI Aurora ES Class 1 StarFighter'
    django_admin_log_50.action_flag = 2
    django_admin_log_50.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_50 = importer.save_or_locate(django_admin_log_50)

    django_admin_log_51 = LogEntry()
    django_admin_log_51.action_time = datetime.datetime(2013, 9, 9, 23, 37, 28)
    django_admin_log_51.user = auth_user_1
    django_admin_log_51.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_51.object_id = u'298'
    django_admin_log_51.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Right Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_51.action_flag = 2
    django_admin_log_51.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_51 = importer.save_or_locate(django_admin_log_51)

    django_admin_log_52 = LogEntry()
    django_admin_log_52.action_time = datetime.datetime(2013, 9, 9, 23, 36, 46)
    django_admin_log_52.user = auth_user_1
    django_admin_log_52.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_52.object_id = u'297'
    django_admin_log_52.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Right Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_52.action_flag = 2
    django_admin_log_52.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_52 = importer.save_or_locate(django_admin_log_52)

    django_admin_log_53 = LogEntry()
    django_admin_log_53.action_time = datetime.datetime(2013, 9, 9, 23, 36, 26)
    django_admin_log_53.user = auth_user_1
    django_admin_log_53.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_53.object_id = u'297'
    django_admin_log_53.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Right Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_53.action_flag = 2
    django_admin_log_53.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_53 = importer.save_or_locate(django_admin_log_53)

    django_admin_log_54 = LogEntry()
    django_admin_log_54.action_time = datetime.datetime(2013, 9, 9, 23, 35, 36)
    django_admin_log_54.user = auth_user_1
    django_admin_log_54.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_54.object_id = u'296'
    django_admin_log_54.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_54.action_flag = 2
    django_admin_log_54.change_message = u'Changed tagLocationX.'
    django_admin_log_54 = importer.save_or_locate(django_admin_log_54)

    django_admin_log_55 = LogEntry()
    django_admin_log_55.action_time = datetime.datetime(2013, 9, 9, 23, 35, 16)
    django_admin_log_55.user = auth_user_1
    django_admin_log_55.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_55.object_id = u'296'
    django_admin_log_55.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_55.action_flag = 2
    django_admin_log_55.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_55 = importer.save_or_locate(django_admin_log_55)

    django_admin_log_56 = LogEntry()
    django_admin_log_56.action_time = datetime.datetime(2013, 9, 9, 23, 34, 55)
    django_admin_log_56.user = auth_user_1
    django_admin_log_56.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_56.object_id = u'296'
    django_admin_log_56.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_56.action_flag = 2
    django_admin_log_56.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_56 = importer.save_or_locate(django_admin_log_56)

    django_admin_log_57 = LogEntry()
    django_admin_log_57.action_time = datetime.datetime(2013, 9, 9, 23, 34, 18)
    django_admin_log_57.user = auth_user_1
    django_admin_log_57.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_57.object_id = u'295'
    django_admin_log_57.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Left Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_57.action_flag = 2
    django_admin_log_57.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_57 = importer.save_or_locate(django_admin_log_57)

    django_admin_log_58 = LogEntry()
    django_admin_log_58.action_time = datetime.datetime(2013, 9, 9, 23, 33, 23)
    django_admin_log_58.user = auth_user_1
    django_admin_log_58.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_58.object_id = u'294'
    django_admin_log_58.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_58.action_flag = 2
    django_admin_log_58.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_58 = importer.save_or_locate(django_admin_log_58)

    django_admin_log_59 = LogEntry()
    django_admin_log_59.action_time = datetime.datetime(2013, 9, 9, 23, 32, 15)
    django_admin_log_59.user = auth_user_1
    django_admin_log_59.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_59.object_id = u'281'
    django_admin_log_59.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_59.action_flag = 2
    django_admin_log_59.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_59 = importer.save_or_locate(django_admin_log_59)

    django_admin_log_60 = LogEntry()
    django_admin_log_60.action_time = datetime.datetime(2013, 9, 9, 23, 31, 55)
    django_admin_log_60.user = auth_user_1
    django_admin_log_60.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_60.object_id = u'281'
    django_admin_log_60.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_60.action_flag = 2
    django_admin_log_60.change_message = u'Changed tagLocationX.'
    django_admin_log_60 = importer.save_or_locate(django_admin_log_60)

    django_admin_log_61 = LogEntry()
    django_admin_log_61.action_time = datetime.datetime(2013, 9, 9, 23, 31, 36)
    django_admin_log_61.user = auth_user_1
    django_admin_log_61.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_61.object_id = u'281'
    django_admin_log_61.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_61.action_flag = 2
    django_admin_log_61.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_61 = importer.save_or_locate(django_admin_log_61)

    django_admin_log_62 = LogEntry()
    django_admin_log_62.action_time = datetime.datetime(2013, 9, 9, 23, 31, 13)
    django_admin_log_62.user = auth_user_1
    django_admin_log_62.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_62.object_id = u'281'
    django_admin_log_62.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_62.action_flag = 2
    django_admin_log_62.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_62 = importer.save_or_locate(django_admin_log_62)

    django_admin_log_63 = LogEntry()
    django_admin_log_63.action_time = datetime.datetime(2013, 9, 9, 23, 30, 48)
    django_admin_log_63.user = auth_user_1
    django_admin_log_63.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_63.object_id = u'281'
    django_admin_log_63.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_63.action_flag = 2
    django_admin_log_63.change_message = u'Changed tagLocationY.'
    django_admin_log_63 = importer.save_or_locate(django_admin_log_63)

    django_admin_log_64 = LogEntry()
    django_admin_log_64.action_time = datetime.datetime(2013, 9, 9, 23, 30, 24)
    django_admin_log_64.user = auth_user_1
    django_admin_log_64.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_64.object_id = u'281'
    django_admin_log_64.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_64.action_flag = 2
    django_admin_log_64.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_64 = importer.save_or_locate(django_admin_log_64)

    django_admin_log_65 = LogEntry()
    django_admin_log_65.action_time = datetime.datetime(2013, 9, 9, 23, 29, 37)
    django_admin_log_65.user = auth_user_1
    django_admin_log_65.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_65.object_id = u'280'
    django_admin_log_65.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Power Plant (2-3) [<VehicleItemType: PowerPlant>]'
    django_admin_log_65.action_flag = 2
    django_admin_log_65.change_message = u'Changed tagLocationY.'
    django_admin_log_65 = importer.save_or_locate(django_admin_log_65)

    django_admin_log_66 = LogEntry()
    django_admin_log_66.action_time = datetime.datetime(2013, 9, 9, 23, 29, 5)
    django_admin_log_66.user = auth_user_1
    django_admin_log_66.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_66.object_id = u'280'
    django_admin_log_66.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter: Power Plant (2-3) [<VehicleItemType: PowerPlant>]'
    django_admin_log_66.action_flag = 2
    django_admin_log_66.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_66 = importer.save_or_locate(django_admin_log_66)

    django_admin_log_67 = LogEntry()
    django_admin_log_67.action_time = datetime.datetime(2013, 9, 9, 23, 27, 58)
    django_admin_log_67.user = auth_user_1
    django_admin_log_67.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_67.object_id = u'10'
    django_admin_log_67.object_repr = u'Origin JumpWorks 300i Class 3 StarFighter'
    django_admin_log_67.action_flag = 2
    django_admin_log_67.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_67 = importer.save_or_locate(django_admin_log_67)

    django_admin_log_68 = LogEntry()
    django_admin_log_68.action_time = datetime.datetime(2013, 9, 9, 13, 54, 16)
    django_admin_log_68.user = auth_user_1
    django_admin_log_68.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_68.object_id = u'199'
    django_admin_log_68.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Upper Right Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_68.action_flag = 2
    django_admin_log_68.change_message = u'Changed tagLocationY.'
    django_admin_log_68 = importer.save_or_locate(django_admin_log_68)

    django_admin_log_69 = LogEntry()
    django_admin_log_69.action_time = datetime.datetime(2013, 9, 9, 13, 54, 3)
    django_admin_log_69.user = auth_user_1
    django_admin_log_69.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_69.object_id = u'199'
    django_admin_log_69.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Upper Right Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_69.action_flag = 2
    django_admin_log_69.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_69 = importer.save_or_locate(django_admin_log_69)

    django_admin_log_70 = LogEntry()
    django_admin_log_70.action_time = datetime.datetime(2013, 9, 9, 13, 53, 48)
    django_admin_log_70.user = auth_user_1
    django_admin_log_70.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_70.object_id = u'199'
    django_admin_log_70.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Upper Right Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_70.action_flag = 2
    django_admin_log_70.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_70 = importer.save_or_locate(django_admin_log_70)

    django_admin_log_71 = LogEntry()
    django_admin_log_71.action_time = datetime.datetime(2013, 9, 9, 13, 53, 7)
    django_admin_log_71.user = auth_user_1
    django_admin_log_71.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_71.object_id = u'198'
    django_admin_log_71.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Lower Right Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_71.action_flag = 2
    django_admin_log_71.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_71 = importer.save_or_locate(django_admin_log_71)

    django_admin_log_72 = LogEntry()
    django_admin_log_72.action_time = datetime.datetime(2013, 9, 9, 13, 52, 27)
    django_admin_log_72.user = auth_user_1
    django_admin_log_72.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_72.object_id = u'197'
    django_admin_log_72.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Upper Left Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_72.action_flag = 2
    django_admin_log_72.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_72 = importer.save_or_locate(django_admin_log_72)

    django_admin_log_73 = LogEntry()
    django_admin_log_73.action_time = datetime.datetime(2013, 9, 9, 13, 52, 9)
    django_admin_log_73.user = auth_user_1
    django_admin_log_73.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_73.object_id = u'197'
    django_admin_log_73.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Upper Left Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_73.action_flag = 2
    django_admin_log_73.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_73 = importer.save_or_locate(django_admin_log_73)

    django_admin_log_74 = LogEntry()
    django_admin_log_74.action_time = datetime.datetime(2013, 9, 9, 13, 51, 14)
    django_admin_log_74.user = auth_user_1
    django_admin_log_74.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_74.object_id = u'196'
    django_admin_log_74.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Lower Left Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_74.action_flag = 2
    django_admin_log_74.change_message = u'Changed parentImage.'
    django_admin_log_74 = importer.save_or_locate(django_admin_log_74)

    django_admin_log_75 = LogEntry()
    django_admin_log_75.action_time = datetime.datetime(2013, 9, 9, 13, 50, 42)
    django_admin_log_75.user = auth_user_1
    django_admin_log_75.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_75.object_id = u'196'
    django_admin_log_75.object_repr = u'RSI Constellation Class 3 StarFighter: Class 2 Lower Left Nacelle (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_75.action_flag = 2
    django_admin_log_75.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_75 = importer.save_or_locate(django_admin_log_75)

    django_admin_log_76 = LogEntry()
    django_admin_log_76.action_time = datetime.datetime(2013, 9, 9, 13, 49)
    django_admin_log_76.user = auth_user_1
    django_admin_log_76.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_76.object_id = u'3'
    django_admin_log_76.object_repr = u'RSI Constellation Class 3 StarFighter'
    django_admin_log_76.action_flag = 2
    django_admin_log_76.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_76 = importer.save_or_locate(django_admin_log_76)

    django_admin_log_77 = LogEntry()
    django_admin_log_77.action_time = datetime.datetime(2013, 9, 9, 4, 46, 25)
    django_admin_log_77.user = auth_user_1
    django_admin_log_77.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_77.object_id = u'182'
    django_admin_log_77.object_repr = u'MISC Freelancer Class 3 Transport: Right Class 2 Mount Bottom (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_77.action_flag = 2
    django_admin_log_77.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_77 = importer.save_or_locate(django_admin_log_77)

    django_admin_log_78 = LogEntry()
    django_admin_log_78.action_time = datetime.datetime(2013, 9, 9, 4, 46, 4)
    django_admin_log_78.user = auth_user_1
    django_admin_log_78.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_78.object_id = u'182'
    django_admin_log_78.object_repr = u'MISC Freelancer Class 3 Transport: Right Class 2 Mount Bottom (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_78.action_flag = 2
    django_admin_log_78.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_78 = importer.save_or_locate(django_admin_log_78)

    django_admin_log_79 = LogEntry()
    django_admin_log_79.action_time = datetime.datetime(2013, 9, 9, 4, 45, 14)
    django_admin_log_79.user = auth_user_1
    django_admin_log_79.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_79.object_id = u'181'
    django_admin_log_79.object_repr = u'MISC Freelancer Class 3 Transport: Right Class 2 Mount Top (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_79.action_flag = 2
    django_admin_log_79.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_79 = importer.save_or_locate(django_admin_log_79)

    django_admin_log_80 = LogEntry()
    django_admin_log_80.action_time = datetime.datetime(2013, 9, 9, 4, 44, 56)
    django_admin_log_80.user = auth_user_1
    django_admin_log_80.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_80.object_id = u'181'
    django_admin_log_80.object_repr = u'MISC Freelancer Class 3 Transport: Right Class 2 Mount Top (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_80.action_flag = 2
    django_admin_log_80.change_message = u'Changed tagLocationX.'
    django_admin_log_80 = importer.save_or_locate(django_admin_log_80)

    django_admin_log_81 = LogEntry()
    django_admin_log_81.action_time = datetime.datetime(2013, 9, 9, 4, 44, 41)
    django_admin_log_81.user = auth_user_1
    django_admin_log_81.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_81.object_id = u'181'
    django_admin_log_81.object_repr = u'MISC Freelancer Class 3 Transport: Right Class 2 Mount Top (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_81.action_flag = 2
    django_admin_log_81.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_81 = importer.save_or_locate(django_admin_log_81)

    django_admin_log_82 = LogEntry()
    django_admin_log_82.action_time = datetime.datetime(2013, 9, 9, 4, 43, 32)
    django_admin_log_82.user = auth_user_1
    django_admin_log_82.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_82.object_id = u'180'
    django_admin_log_82.object_repr = u'MISC Freelancer Class 3 Transport: Left Class 2 Mount Bottom (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_82.action_flag = 2
    django_admin_log_82.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_82 = importer.save_or_locate(django_admin_log_82)

    django_admin_log_83 = LogEntry()
    django_admin_log_83.action_time = datetime.datetime(2013, 9, 9, 4, 43, 9)
    django_admin_log_83.user = auth_user_1
    django_admin_log_83.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_83.object_id = u'180'
    django_admin_log_83.object_repr = u'MISC Freelancer Class 3 Transport: Left Class 2 Mount Bottom (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_83.action_flag = 2
    django_admin_log_83.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_83 = importer.save_or_locate(django_admin_log_83)

    django_admin_log_84 = LogEntry()
    django_admin_log_84.action_time = datetime.datetime(2013, 9, 9, 4, 41, 53)
    django_admin_log_84.user = auth_user_1
    django_admin_log_84.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_84.object_id = u'179'
    django_admin_log_84.object_repr = u'MISC Freelancer Class 3 Transport: Left Class 2 Mount Top (3-5) [<VehicleItemType: Weapon>]'
    django_admin_log_84.action_flag = 2
    django_admin_log_84.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_84 = importer.save_or_locate(django_admin_log_84)

    django_admin_log_85 = LogEntry()
    django_admin_log_85.action_time = datetime.datetime(2013, 9, 9, 4, 39, 57)
    django_admin_log_85.user = auth_user_1
    django_admin_log_85.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_85.object_id = u'166'
    django_admin_log_85.object_repr = u'MISC Freelancer Class 3 Transport: hardpoint_engine_attach (4-5) [<VehicleItemType: Thruster>]'
    django_admin_log_85.action_flag = 2
    django_admin_log_85.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_85 = importer.save_or_locate(django_admin_log_85)

    django_admin_log_86 = LogEntry()
    django_admin_log_86.action_time = datetime.datetime(2013, 9, 9, 4, 36, 50)
    django_admin_log_86.user = auth_user_1
    django_admin_log_86.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_86.object_id = u'165'
    django_admin_log_86.object_repr = u'MISC Freelancer Class 3 Transport: Power Plant (3-5) [<VehicleItemType: PowerPlant>]'
    django_admin_log_86.action_flag = 2
    django_admin_log_86.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_86 = importer.save_or_locate(django_admin_log_86)

    django_admin_log_87 = LogEntry()
    django_admin_log_87.action_time = datetime.datetime(2013, 9, 9, 4, 35, 40)
    django_admin_log_87.user = auth_user_1
    django_admin_log_87.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_87.object_id = u'1'
    django_admin_log_87.object_repr = u'MISC Freelancer Class 3 Transport'
    django_admin_log_87.action_flag = 2
    django_admin_log_87.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_87 = importer.save_or_locate(django_admin_log_87)

    django_admin_log_88 = LogEntry()
    django_admin_log_88.action_time = datetime.datetime(2013, 9, 9, 4, 35, 28)
    django_admin_log_88.user = auth_user_1
    django_admin_log_88.content_type = ContentType.objects.get(app_label="shipBuilder", model="manufacturer")
    django_admin_log_88.object_id = u'47'
    django_admin_log_88.object_repr = u'MISC'
    django_admin_log_88.action_flag = 1
    django_admin_log_88.change_message = u''
    django_admin_log_88 = importer.save_or_locate(django_admin_log_88)

    django_admin_log_89 = LogEntry()
    django_admin_log_89.action_time = datetime.datetime(2013, 9, 9, 4, 33, 16)
    django_admin_log_89.user = auth_user_1
    django_admin_log_89.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_89.object_id = u'165'
    django_admin_log_89.object_repr = u'MISC Freelancer Class 3 Transport: Power Plant (3-5) [<VehicleItemType: PowerPlant>]'
    django_admin_log_89.action_flag = 2
    django_admin_log_89.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_89 = importer.save_or_locate(django_admin_log_89)

    django_admin_log_90 = LogEntry()
    django_admin_log_90.action_time = datetime.datetime(2013, 9, 9, 4, 26, 41)
    django_admin_log_90.user = auth_user_1
    django_admin_log_90.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_90.object_id = u'250'
    django_admin_log_90.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Right Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_90.action_flag = 2
    django_admin_log_90.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_90 = importer.save_or_locate(django_admin_log_90)

    django_admin_log_91 = LogEntry()
    django_admin_log_91.action_time = datetime.datetime(2013, 9, 9, 4, 25, 55)
    django_admin_log_91.user = auth_user_1
    django_admin_log_91.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_91.object_id = u'249'
    django_admin_log_91.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Right Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_91.action_flag = 2
    django_admin_log_91.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_91 = importer.save_or_locate(django_admin_log_91)

    django_admin_log_92 = LogEntry()
    django_admin_log_92.action_time = datetime.datetime(2013, 9, 9, 4, 24, 35)
    django_admin_log_92.user = auth_user_1
    django_admin_log_92.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_92.object_id = u'248'
    django_admin_log_92.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_92.action_flag = 2
    django_admin_log_92.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_92 = importer.save_or_locate(django_admin_log_92)

    django_admin_log_93 = LogEntry()
    django_admin_log_93.action_time = datetime.datetime(2013, 9, 9, 4, 24, 12)
    django_admin_log_93.user = auth_user_1
    django_admin_log_93.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_93.object_id = u'248'
    django_admin_log_93.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_93.action_flag = 2
    django_admin_log_93.change_message = u'Changed tagLocationX.'
    django_admin_log_93 = importer.save_or_locate(django_admin_log_93)

    django_admin_log_94 = LogEntry()
    django_admin_log_94.action_time = datetime.datetime(2013, 9, 9, 4, 23, 48)
    django_admin_log_94.user = auth_user_1
    django_admin_log_94.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_94.object_id = u'248'
    django_admin_log_94.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_94.action_flag = 2
    django_admin_log_94.change_message = u'Changed tagLocationX.'
    django_admin_log_94 = importer.save_or_locate(django_admin_log_94)

    django_admin_log_95 = LogEntry()
    django_admin_log_95.action_time = datetime.datetime(2013, 9, 9, 4, 23, 19)
    django_admin_log_95.user = auth_user_1
    django_admin_log_95.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_95.object_id = u'248'
    django_admin_log_95.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Left Wing Class 1 Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_95.action_flag = 2
    django_admin_log_95.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_95 = importer.save_or_locate(django_admin_log_95)

    django_admin_log_96 = LogEntry()
    django_admin_log_96.action_time = datetime.datetime(2013, 9, 9, 4, 21, 20)
    django_admin_log_96.user = auth_user_1
    django_admin_log_96.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_96.object_id = u'247'
    django_admin_log_96.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Left Wing Pylon (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_96.action_flag = 2
    django_admin_log_96.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_96 = importer.save_or_locate(django_admin_log_96)

    django_admin_log_97 = LogEntry()
    django_admin_log_97.action_time = datetime.datetime(2013, 9, 9, 4, 18, 28)
    django_admin_log_97.user = auth_user_1
    django_admin_log_97.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_97.object_id = u'246'
    django_admin_log_97.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_97.action_flag = 2
    django_admin_log_97.change_message = u'No fields changed.'
    django_admin_log_97 = importer.save_or_locate(django_admin_log_97)

    django_admin_log_98 = LogEntry()
    django_admin_log_98.action_time = datetime.datetime(2013, 9, 9, 4, 18, 25)
    django_admin_log_98.user = auth_user_1
    django_admin_log_98.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_98.object_id = u'246'
    django_admin_log_98.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_98.action_flag = 2
    django_admin_log_98.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_98 = importer.save_or_locate(django_admin_log_98)

    django_admin_log_99 = LogEntry()
    django_admin_log_99.action_time = datetime.datetime(2013, 9, 9, 4, 18, 2)
    django_admin_log_99.user = auth_user_1
    django_admin_log_99.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_99.object_id = u'246'
    django_admin_log_99.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_99.action_flag = 2
    django_admin_log_99.change_message = u'Changed tagLocationX and tagLocationY.'
    django_admin_log_99 = importer.save_or_locate(django_admin_log_99)

    django_admin_log_100 = LogEntry()
    django_admin_log_100.action_time = datetime.datetime(2013, 9, 9, 4, 17, 35)
    django_admin_log_100.user = auth_user_1
    django_admin_log_100.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_100.object_id = u'246'
    django_admin_log_100.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_100.action_flag = 2
    django_admin_log_100.change_message = u'Changed tagLocationX.'
    django_admin_log_100 = importer.save_or_locate(django_admin_log_100)

    django_admin_log_101 = LogEntry()
    django_admin_log_101.action_time = datetime.datetime(2013, 9, 9, 4, 17, 12)
    django_admin_log_101.user = auth_user_1
    django_admin_log_101.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_101.object_id = u'246'
    django_admin_log_101.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Nose Class 2 Slot (1-2) [<VehicleItemType: Weapon>]'
    django_admin_log_101.action_flag = 2
    django_admin_log_101.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_101 = importer.save_or_locate(django_admin_log_101)

    django_admin_log_102 = LogEntry()
    django_admin_log_102.action_time = datetime.datetime(2013, 9, 9, 4, 14, 27)
    django_admin_log_102.user = auth_user_1
    django_admin_log_102.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_102.object_id = u'233'
    django_admin_log_102.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: hardpoint_engine_attach (3-4) [<VehicleItemType: Thruster>]'
    django_admin_log_102.action_flag = 2
    django_admin_log_102.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_102 = importer.save_or_locate(django_admin_log_102)

    django_admin_log_103 = LogEntry()
    django_admin_log_103.action_time = datetime.datetime(2013, 9, 9, 4, 12, 32)
    django_admin_log_103.user = auth_user_1
    django_admin_log_103.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_103.object_id = u'232'
    django_admin_log_103.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter: Power Plant (2-4) [<VehicleItemType: PowerPlant>]'
    django_admin_log_103.action_flag = 2
    django_admin_log_103.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_103 = importer.save_or_locate(django_admin_log_103)

    django_admin_log_104 = LogEntry()
    django_admin_log_104.action_time = datetime.datetime(2013, 9, 9, 4, 10, 37)
    django_admin_log_104.user = auth_user_1
    django_admin_log_104.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_104.object_id = u'7'
    django_admin_log_104.object_repr = u'Origin Jumpworks 350r Class 2 Star Fighter'
    django_admin_log_104.action_flag = 2
    django_admin_log_104.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_104 = importer.save_or_locate(django_admin_log_104)

    django_admin_log_105 = LogEntry()
    django_admin_log_105.action_time = datetime.datetime(2013, 9, 8, 20, 43, 51)
    django_admin_log_105.user = auth_user_1
    django_admin_log_105.content_type = ContentType.objects.get(app_label="shipBuilder", model="vehicle")
    django_admin_log_105.object_id = u'2'
    django_admin_log_105.object_repr = u'Anvil Hornet Class 2 StarFighter'
    django_admin_log_105.action_flag = 2
    django_admin_log_105.change_message = u'Changed thumbnail, manufacturer, layoutImageTopRight, layoutImageTopLeft, layoutImageBottomRight and layoutImageBottomLeft.'
    django_admin_log_105 = importer.save_or_locate(django_admin_log_105)

    django_admin_log_106 = LogEntry()
    django_admin_log_106.action_time = datetime.datetime(2013, 9, 8, 20, 41, 58)
    django_admin_log_106.user = auth_user_1
    django_admin_log_106.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_106.object_id = u'187'
    django_admin_log_106.object_repr = u'Anvil Hornet Class 2 StarFighter: Port_Thruster_Main_TR4 (4-4) [<VehicleItemType: Thruster>]'
    django_admin_log_106.action_flag = 2
    django_admin_log_106.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_106 = importer.save_or_locate(django_admin_log_106)

    django_admin_log_107 = LogEntry()
    django_admin_log_107.action_time = datetime.datetime(2013, 9, 8, 20, 41, 36)
    django_admin_log_107.user = auth_user_1
    django_admin_log_107.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_107.object_id = u'186'
    django_admin_log_107.object_repr = u'Anvil Hornet Class 2 StarFighter: Power Plant (1-4) [<VehicleItemType: PowerPlant>]'
    django_admin_log_107.action_flag = 2
    django_admin_log_107.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_107 = importer.save_or_locate(django_admin_log_107)

    django_admin_log_108 = LogEntry()
    django_admin_log_108.action_time = datetime.datetime(2013, 9, 8, 20, 41, 13)
    django_admin_log_108.user = auth_user_1
    django_admin_log_108.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_108.object_id = u'185'
    django_admin_log_108.object_repr = u'Anvil Hornet Class 2 StarFighter: Right Bay Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_108.action_flag = 2
    django_admin_log_108.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_108 = importer.save_or_locate(django_admin_log_108)

    django_admin_log_109 = LogEntry()
    django_admin_log_109.action_time = datetime.datetime(2013, 9, 8, 20, 40, 45)
    django_admin_log_109.user = auth_user_1
    django_admin_log_109.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_109.object_id = u'184'
    django_admin_log_109.object_repr = u'Anvil Hornet Class 2 StarFighter: Left Bay Slot (1-3) [<VehicleItemType: Weapon>]'
    django_admin_log_109.action_flag = 2
    django_admin_log_109.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_109 = importer.save_or_locate(django_admin_log_109)

    django_admin_log_110 = LogEntry()
    django_admin_log_110.action_time = datetime.datetime(2013, 9, 8, 20, 40, 20)
    django_admin_log_110.user = auth_user_1
    django_admin_log_110.content_type = ContentType.objects.get(app_label="shipBuilder", model="itemport")
    django_admin_log_110.object_id = u'183'
    django_admin_log_110.object_repr = u'Anvil Hornet Class 2 StarFighter: Top Turret Slot (1-4) [<VehicleItemType: Weapon>, <VehicleItemType: Radar>]'
    django_admin_log_110.action_flag = 2
    django_admin_log_110.change_message = u'Changed parentImage, tagLocationX and tagLocationY.'
    django_admin_log_110 = importer.save_or_locate(django_admin_log_110)

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
    shipBuilder_itemport_1.parentImage = 0L
    shipBuilder_itemport_1.image = None
    shipBuilder_itemport_1.tagLocationX = 0.0
    shipBuilder_itemport_1.tagLocationY = 0.0
    shipBuilder_itemport_1 = importer.save_or_locate(shipBuilder_itemport_1)

    shipBuilder_itemport_2 = ItemPort()
    shipBuilder_itemport_2.displayName = u'Power Plant'
    shipBuilder_itemport_2.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_2.flags = u'main rear'
    shipBuilder_itemport_2.maxSize = 5L
    shipBuilder_itemport_2.minSize = 3L
    shipBuilder_itemport_2.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_2.portClass = 0L
    shipBuilder_itemport_2.parentImage = 2L
    shipBuilder_itemport_2.image = None
    shipBuilder_itemport_2.tagLocationX = 55.0
    shipBuilder_itemport_2.tagLocationY = 33.5
    shipBuilder_itemport_2 = importer.save_or_locate(shipBuilder_itemport_2)

    shipBuilder_itemport_2.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_2.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_3 = ItemPort()
    shipBuilder_itemport_3.displayName = None
    shipBuilder_itemport_3.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_3.flags = u'main rear'
    shipBuilder_itemport_3.maxSize = 5L
    shipBuilder_itemport_3.minSize = 4L
    shipBuilder_itemport_3.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_3.portClass = 0L
    shipBuilder_itemport_3.parentImage = 2L
    shipBuilder_itemport_3.image = None
    shipBuilder_itemport_3.tagLocationX = 70.0
    shipBuilder_itemport_3.tagLocationY = 38.7
    shipBuilder_itemport_3 = importer.save_or_locate(shipBuilder_itemport_3)

    shipBuilder_itemport_3.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_3.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_3.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_3.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_3.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_4 = ItemPort()
    shipBuilder_itemport_4.displayName = None
    shipBuilder_itemport_4.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_4.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_4.maxSize = 2L
    shipBuilder_itemport_4.minSize = 1L
    shipBuilder_itemport_4.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_4.portClass = 0L
    shipBuilder_itemport_4.parentImage = 0L
    shipBuilder_itemport_4.image = None
    shipBuilder_itemport_4.tagLocationX = 0.0
    shipBuilder_itemport_4.tagLocationY = 0.0
    shipBuilder_itemport_4 = importer.save_or_locate(shipBuilder_itemport_4)

    shipBuilder_itemport_4.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_4.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_4.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_4.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_4.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_5 = ItemPort()
    shipBuilder_itemport_5.displayName = None
    shipBuilder_itemport_5.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_5.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_5.maxSize = 2L
    shipBuilder_itemport_5.minSize = 1L
    shipBuilder_itemport_5.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_5.portClass = 0L
    shipBuilder_itemport_5.parentImage = 0L
    shipBuilder_itemport_5.image = None
    shipBuilder_itemport_5.tagLocationX = 0.0
    shipBuilder_itemport_5.tagLocationY = 0.0
    shipBuilder_itemport_5 = importer.save_or_locate(shipBuilder_itemport_5)

    shipBuilder_itemport_5.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_5.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_5.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_5.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_5.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_6 = ItemPort()
    shipBuilder_itemport_6.displayName = None
    shipBuilder_itemport_6.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_6.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_6.maxSize = 2L
    shipBuilder_itemport_6.minSize = 1L
    shipBuilder_itemport_6.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_6.portClass = 0L
    shipBuilder_itemport_6.parentImage = 0L
    shipBuilder_itemport_6.image = None
    shipBuilder_itemport_6.tagLocationX = 0.0
    shipBuilder_itemport_6.tagLocationY = 0.0
    shipBuilder_itemport_6 = importer.save_or_locate(shipBuilder_itemport_6)

    shipBuilder_itemport_6.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_6.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_6.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_6.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_6.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_7 = ItemPort()
    shipBuilder_itemport_7.displayName = None
    shipBuilder_itemport_7.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_7.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_7.maxSize = 2L
    shipBuilder_itemport_7.minSize = 1L
    shipBuilder_itemport_7.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_7.portClass = 0L
    shipBuilder_itemport_7.parentImage = 0L
    shipBuilder_itemport_7.image = None
    shipBuilder_itemport_7.tagLocationX = 0.0
    shipBuilder_itemport_7.tagLocationY = 0.0
    shipBuilder_itemport_7 = importer.save_or_locate(shipBuilder_itemport_7)

    shipBuilder_itemport_7.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_7.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_7.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_7.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_7.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_8 = ItemPort()
    shipBuilder_itemport_8.displayName = None
    shipBuilder_itemport_8.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_8.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_8.maxSize = 2L
    shipBuilder_itemport_8.minSize = 1L
    shipBuilder_itemport_8.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_8.portClass = 0L
    shipBuilder_itemport_8.parentImage = 0L
    shipBuilder_itemport_8.image = None
    shipBuilder_itemport_8.tagLocationX = 0.0
    shipBuilder_itemport_8.tagLocationY = 0.0
    shipBuilder_itemport_8 = importer.save_or_locate(shipBuilder_itemport_8)

    shipBuilder_itemport_8.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_8.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_8.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_8.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_8.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_9 = ItemPort()
    shipBuilder_itemport_9.displayName = None
    shipBuilder_itemport_9.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_9.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_9.maxSize = 2L
    shipBuilder_itemport_9.minSize = 1L
    shipBuilder_itemport_9.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_9.portClass = 0L
    shipBuilder_itemport_9.parentImage = 0L
    shipBuilder_itemport_9.image = None
    shipBuilder_itemport_9.tagLocationX = 0.0
    shipBuilder_itemport_9.tagLocationY = 0.0
    shipBuilder_itemport_9 = importer.save_or_locate(shipBuilder_itemport_9)

    shipBuilder_itemport_9.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_9.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_9.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_9.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_9.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_10 = ItemPort()
    shipBuilder_itemport_10.displayName = None
    shipBuilder_itemport_10.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_10.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_10.maxSize = 2L
    shipBuilder_itemport_10.minSize = 1L
    shipBuilder_itemport_10.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_10.portClass = 0L
    shipBuilder_itemport_10.parentImage = 0L
    shipBuilder_itemport_10.image = None
    shipBuilder_itemport_10.tagLocationX = 0.0
    shipBuilder_itemport_10.tagLocationY = 0.0
    shipBuilder_itemport_10 = importer.save_or_locate(shipBuilder_itemport_10)

    shipBuilder_itemport_10.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_10.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_10.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_10.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_10.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_11 = ItemPort()
    shipBuilder_itemport_11.displayName = None
    shipBuilder_itemport_11.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_11.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_11.maxSize = 2L
    shipBuilder_itemport_11.minSize = 1L
    shipBuilder_itemport_11.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_11.portClass = 0L
    shipBuilder_itemport_11.parentImage = 0L
    shipBuilder_itemport_11.image = None
    shipBuilder_itemport_11.tagLocationX = 0.0
    shipBuilder_itemport_11.tagLocationY = 0.0
    shipBuilder_itemport_11 = importer.save_or_locate(shipBuilder_itemport_11)

    shipBuilder_itemport_11.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_11.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_11.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_11.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_11.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_12 = ItemPort()
    shipBuilder_itemport_12.displayName = None
    shipBuilder_itemport_12.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_12.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_12.maxSize = 2L
    shipBuilder_itemport_12.minSize = 1L
    shipBuilder_itemport_12.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_12.portClass = 0L
    shipBuilder_itemport_12.parentImage = 0L
    shipBuilder_itemport_12.image = None
    shipBuilder_itemport_12.tagLocationX = 0.0
    shipBuilder_itemport_12.tagLocationY = 0.0
    shipBuilder_itemport_12 = importer.save_or_locate(shipBuilder_itemport_12)

    shipBuilder_itemport_12.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_12.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_12.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_12.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_12.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_13 = ItemPort()
    shipBuilder_itemport_13.displayName = None
    shipBuilder_itemport_13.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_13.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_13.maxSize = 2L
    shipBuilder_itemport_13.minSize = 1L
    shipBuilder_itemport_13.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_13.portClass = 0L
    shipBuilder_itemport_13.parentImage = 0L
    shipBuilder_itemport_13.image = None
    shipBuilder_itemport_13.tagLocationX = 0.0
    shipBuilder_itemport_13.tagLocationY = 0.0
    shipBuilder_itemport_13 = importer.save_or_locate(shipBuilder_itemport_13)

    shipBuilder_itemport_13.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_13.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_13.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_13.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_13.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_14 = ItemPort()
    shipBuilder_itemport_14.displayName = None
    shipBuilder_itemport_14.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_14.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_14.maxSize = 2L
    shipBuilder_itemport_14.minSize = 1L
    shipBuilder_itemport_14.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_14.portClass = 0L
    shipBuilder_itemport_14.parentImage = 0L
    shipBuilder_itemport_14.image = None
    shipBuilder_itemport_14.tagLocationX = 0.0
    shipBuilder_itemport_14.tagLocationY = 0.0
    shipBuilder_itemport_14 = importer.save_or_locate(shipBuilder_itemport_14)

    shipBuilder_itemport_14.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_14.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_14.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_14.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_14.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_15 = ItemPort()
    shipBuilder_itemport_15.displayName = None
    shipBuilder_itemport_15.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_15.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_15.maxSize = 2L
    shipBuilder_itemport_15.minSize = 1L
    shipBuilder_itemport_15.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_15.portClass = 0L
    shipBuilder_itemport_15.parentImage = 0L
    shipBuilder_itemport_15.image = None
    shipBuilder_itemport_15.tagLocationX = 0.0
    shipBuilder_itemport_15.tagLocationY = 0.0
    shipBuilder_itemport_15 = importer.save_or_locate(shipBuilder_itemport_15)

    shipBuilder_itemport_15.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_15.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_15.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_15.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_15.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_16 = ItemPort()
    shipBuilder_itemport_16.displayName = u'Left Class 2 Mount Top'
    shipBuilder_itemport_16.name = u'Freelancer_side_cannon_L_Hardpoint'
    shipBuilder_itemport_16.flags = u'left side top'
    shipBuilder_itemport_16.maxSize = 5L
    shipBuilder_itemport_16.minSize = 3L
    shipBuilder_itemport_16.parentVehicle = shipBuilder_vehicle_1
    shipBuilder_itemport_16.portClass = 0L
    shipBuilder_itemport_16.parentImage = 2L
    shipBuilder_itemport_16.image = None
    shipBuilder_itemport_16.tagLocationX = 56.8
    shipBuilder_itemport_16.tagLocationY = 53.5
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
    shipBuilder_itemport_17.parentImage = 4L
    shipBuilder_itemport_17.image = None
    shipBuilder_itemport_17.tagLocationX = 57.9
    shipBuilder_itemport_17.tagLocationY = 42.5
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
    shipBuilder_itemport_18.parentImage = 1L
    shipBuilder_itemport_18.image = None
    shipBuilder_itemport_18.tagLocationX = 43.0
    shipBuilder_itemport_18.tagLocationY = 52.0
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
    shipBuilder_itemport_19.parentImage = 3L
    shipBuilder_itemport_19.image = None
    shipBuilder_itemport_19.tagLocationX = 43.0
    shipBuilder_itemport_19.tagLocationY = 43.0
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
    shipBuilder_itemport_20.parentImage = 1L
    shipBuilder_itemport_20.image = None
    shipBuilder_itemport_20.tagLocationX = 49.5
    shipBuilder_itemport_20.tagLocationY = 27.0
    shipBuilder_itemport_20 = importer.save_or_locate(shipBuilder_itemport_20)

    shipBuilder_itemport_20.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_20.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_9)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_17)
    shipBuilder_itemport_20.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_19)

    shipBuilder_itemport_21 = ItemPort()
    shipBuilder_itemport_21.displayName = u'Left Bay Slot'
    shipBuilder_itemport_21.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_21.flags = u'left bottom'
    shipBuilder_itemport_21.maxSize = 3L
    shipBuilder_itemport_21.minSize = 1L
    shipBuilder_itemport_21.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_21.portClass = 0L
    shipBuilder_itemport_21.parentImage = 2L
    shipBuilder_itemport_21.image = None
    shipBuilder_itemport_21.tagLocationX = 52.0
    shipBuilder_itemport_21.tagLocationY = 38.5
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
    shipBuilder_itemport_22.parentImage = 1L
    shipBuilder_itemport_22.image = None
    shipBuilder_itemport_22.tagLocationX = 46.5
    shipBuilder_itemport_22.tagLocationY = 38.0
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
    shipBuilder_itemport_23.parentImage = 3L
    shipBuilder_itemport_23.image = None
    shipBuilder_itemport_23.tagLocationX = 51.0
    shipBuilder_itemport_23.tagLocationY = 58.0
    shipBuilder_itemport_23 = importer.save_or_locate(shipBuilder_itemport_23)

    shipBuilder_itemport_23.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_23.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_24 = ItemPort()
    shipBuilder_itemport_24.displayName = None
    shipBuilder_itemport_24.name = u'Port_Thruster_Main_TR4'
    shipBuilder_itemport_24.flags = u'main rear'
    shipBuilder_itemport_24.maxSize = 4L
    shipBuilder_itemport_24.minSize = 4L
    shipBuilder_itemport_24.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_24.portClass = 0L
    shipBuilder_itemport_24.parentImage = 3L
    shipBuilder_itemport_24.image = None
    shipBuilder_itemport_24.tagLocationX = 42.9
    shipBuilder_itemport_24.tagLocationY = 58.7
    shipBuilder_itemport_24 = importer.save_or_locate(shipBuilder_itemport_24)

    shipBuilder_itemport_24.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_24.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_24.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_24.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_24.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_25 = ItemPort()
    shipBuilder_itemport_25.displayName = None
    shipBuilder_itemport_25.name = u'Port_Thruster_Bottom_Left_Back'
    shipBuilder_itemport_25.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_25.maxSize = 2L
    shipBuilder_itemport_25.minSize = 1L
    shipBuilder_itemport_25.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_25.portClass = 0L
    shipBuilder_itemport_25.parentImage = 0L
    shipBuilder_itemport_25.image = None
    shipBuilder_itemport_25.tagLocationX = 0.0
    shipBuilder_itemport_25.tagLocationY = 0.0
    shipBuilder_itemport_25 = importer.save_or_locate(shipBuilder_itemport_25)

    shipBuilder_itemport_25.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_25.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_25.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_25.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_25.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_26 = ItemPort()
    shipBuilder_itemport_26.displayName = None
    shipBuilder_itemport_26.name = u'Port_Thruster_Bottom_Right_Back'
    shipBuilder_itemport_26.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_26.maxSize = 2L
    shipBuilder_itemport_26.minSize = 1L
    shipBuilder_itemport_26.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_26.portClass = 0L
    shipBuilder_itemport_26.parentImage = 0L
    shipBuilder_itemport_26.image = None
    shipBuilder_itemport_26.tagLocationX = 0.0
    shipBuilder_itemport_26.tagLocationY = 0.0
    shipBuilder_itemport_26 = importer.save_or_locate(shipBuilder_itemport_26)

    shipBuilder_itemport_26.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_26.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_26.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_26.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_26.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_27 = ItemPort()
    shipBuilder_itemport_27.displayName = None
    shipBuilder_itemport_27.name = u'Port_Thruster_Bottom_Left_Front'
    shipBuilder_itemport_27.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_27.maxSize = 2L
    shipBuilder_itemport_27.minSize = 1L
    shipBuilder_itemport_27.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_27.portClass = 0L
    shipBuilder_itemport_27.parentImage = 0L
    shipBuilder_itemport_27.image = None
    shipBuilder_itemport_27.tagLocationX = 0.0
    shipBuilder_itemport_27.tagLocationY = 0.0
    shipBuilder_itemport_27 = importer.save_or_locate(shipBuilder_itemport_27)

    shipBuilder_itemport_27.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_27.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_27.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_27.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_27.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_28 = ItemPort()
    shipBuilder_itemport_28.displayName = None
    shipBuilder_itemport_28.name = u'Port_Thruster_Bottom_Right_Front'
    shipBuilder_itemport_28.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_28.maxSize = 2L
    shipBuilder_itemport_28.minSize = 1L
    shipBuilder_itemport_28.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_28.portClass = 0L
    shipBuilder_itemport_28.parentImage = 0L
    shipBuilder_itemport_28.image = None
    shipBuilder_itemport_28.tagLocationX = 0.0
    shipBuilder_itemport_28.tagLocationY = 0.0
    shipBuilder_itemport_28 = importer.save_or_locate(shipBuilder_itemport_28)

    shipBuilder_itemport_28.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_28.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_28.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_28.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_28.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_29 = ItemPort()
    shipBuilder_itemport_29.displayName = None
    shipBuilder_itemport_29.name = u'Port_Thruster_Upper_Right_Front'
    shipBuilder_itemport_29.flags = u'maneuver orientation retro -X -Z upper front right'
    shipBuilder_itemport_29.maxSize = 2L
    shipBuilder_itemport_29.minSize = 1L
    shipBuilder_itemport_29.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_29.portClass = 0L
    shipBuilder_itemport_29.parentImage = 0L
    shipBuilder_itemport_29.image = None
    shipBuilder_itemport_29.tagLocationX = 0.0
    shipBuilder_itemport_29.tagLocationY = 0.0
    shipBuilder_itemport_29 = importer.save_or_locate(shipBuilder_itemport_29)

    shipBuilder_itemport_29.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_29.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_29.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_29.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_29.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_30 = ItemPort()
    shipBuilder_itemport_30.displayName = None
    shipBuilder_itemport_30.name = u'Port_Thruster_Upper_Left_Front'
    shipBuilder_itemport_30.flags = u'maneuver orientation retro +X -Z upper front left'
    shipBuilder_itemport_30.maxSize = 2L
    shipBuilder_itemport_30.minSize = 1L
    shipBuilder_itemport_30.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_30.portClass = 0L
    shipBuilder_itemport_30.parentImage = 0L
    shipBuilder_itemport_30.image = None
    shipBuilder_itemport_30.tagLocationX = 0.0
    shipBuilder_itemport_30.tagLocationY = 0.0
    shipBuilder_itemport_30 = importer.save_or_locate(shipBuilder_itemport_30)

    shipBuilder_itemport_30.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_30.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_30.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_30.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_30.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_31 = ItemPort()
    shipBuilder_itemport_31.displayName = None
    shipBuilder_itemport_31.name = u'Port_Thruster_Upper_Right_Back'
    shipBuilder_itemport_31.flags = u'maneuver orientation -X -Z upper rear right'
    shipBuilder_itemport_31.maxSize = 2L
    shipBuilder_itemport_31.minSize = 1L
    shipBuilder_itemport_31.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_31.portClass = 0L
    shipBuilder_itemport_31.parentImage = 0L
    shipBuilder_itemport_31.image = None
    shipBuilder_itemport_31.tagLocationX = 0.0
    shipBuilder_itemport_31.tagLocationY = 0.0
    shipBuilder_itemport_31 = importer.save_or_locate(shipBuilder_itemport_31)

    shipBuilder_itemport_31.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_31.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_31.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_31.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_31.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_32 = ItemPort()
    shipBuilder_itemport_32.displayName = None
    shipBuilder_itemport_32.name = u'Port_Thruster_Upper_Left_Back'
    shipBuilder_itemport_32.flags = u'maneuver orientation +X -Z upper rear left'
    shipBuilder_itemport_32.maxSize = 2L
    shipBuilder_itemport_32.minSize = 1L
    shipBuilder_itemport_32.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_32.portClass = 0L
    shipBuilder_itemport_32.parentImage = 0L
    shipBuilder_itemport_32.image = None
    shipBuilder_itemport_32.tagLocationX = 0.0
    shipBuilder_itemport_32.tagLocationY = 0.0
    shipBuilder_itemport_32 = importer.save_or_locate(shipBuilder_itemport_32)

    shipBuilder_itemport_32.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_32.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_32.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_32.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_32.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_33 = ItemPort()
    shipBuilder_itemport_33.displayName = u'Class 2 Lower Left Nacelle'
    shipBuilder_itemport_33.name = u'Hardpoint_Class_2_Laser_bottom_left'
    shipBuilder_itemport_33.flags = u'Lower Left'
    shipBuilder_itemport_33.maxSize = 2L
    shipBuilder_itemport_33.minSize = 1L
    shipBuilder_itemport_33.parentVehicle = shipBuilder_vehicle_3
    shipBuilder_itemport_33.portClass = 0L
    shipBuilder_itemport_33.parentImage = 4L
    shipBuilder_itemport_33.image = None
    shipBuilder_itemport_33.tagLocationX = 90.0
    shipBuilder_itemport_33.tagLocationY = 78.0
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
    shipBuilder_itemport_34.parentImage = 2L
    shipBuilder_itemport_34.image = None
    shipBuilder_itemport_34.tagLocationX = 81.0
    shipBuilder_itemport_34.tagLocationY = 16.0
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
    shipBuilder_itemport_35.parentImage = 3L
    shipBuilder_itemport_35.image = None
    shipBuilder_itemport_35.tagLocationX = 9.0
    shipBuilder_itemport_35.tagLocationY = 78.0
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
    shipBuilder_itemport_36.parentImage = 1L
    shipBuilder_itemport_36.image = None
    shipBuilder_itemport_36.tagLocationX = 17.5
    shipBuilder_itemport_36.tagLocationY = 15.5
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
    shipBuilder_itemport_37.parentImage = 0L
    shipBuilder_itemport_37.image = None
    shipBuilder_itemport_37.tagLocationX = 0.0
    shipBuilder_itemport_37.tagLocationY = 0.0
    shipBuilder_itemport_37 = importer.save_or_locate(shipBuilder_itemport_37)

    shipBuilder_itemport_37.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_37.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_37.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_37.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_37.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_38 = ItemPort()
    shipBuilder_itemport_38.displayName = None
    shipBuilder_itemport_38.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_38.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_38.maxSize = 1L
    shipBuilder_itemport_38.minSize = 1L
    shipBuilder_itemport_38.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_38.portClass = 0L
    shipBuilder_itemport_38.parentImage = 0L
    shipBuilder_itemport_38.image = None
    shipBuilder_itemport_38.tagLocationX = 0.0
    shipBuilder_itemport_38.tagLocationY = 0.0
    shipBuilder_itemport_38 = importer.save_or_locate(shipBuilder_itemport_38)

    shipBuilder_itemport_38.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_38.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_38.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_38.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_38.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_39 = ItemPort()
    shipBuilder_itemport_39.displayName = None
    shipBuilder_itemport_39.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_39.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_39.maxSize = 1L
    shipBuilder_itemport_39.minSize = 1L
    shipBuilder_itemport_39.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_39.portClass = 0L
    shipBuilder_itemport_39.parentImage = 0L
    shipBuilder_itemport_39.image = None
    shipBuilder_itemport_39.tagLocationX = 0.0
    shipBuilder_itemport_39.tagLocationY = 0.0
    shipBuilder_itemport_39 = importer.save_or_locate(shipBuilder_itemport_39)

    shipBuilder_itemport_39.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_39.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_39.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_39.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_39.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_40 = ItemPort()
    shipBuilder_itemport_40.displayName = None
    shipBuilder_itemport_40.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_40.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_40.maxSize = 1L
    shipBuilder_itemport_40.minSize = 1L
    shipBuilder_itemport_40.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_40.portClass = 0L
    shipBuilder_itemport_40.parentImage = 0L
    shipBuilder_itemport_40.image = None
    shipBuilder_itemport_40.tagLocationX = 0.0
    shipBuilder_itemport_40.tagLocationY = 0.0
    shipBuilder_itemport_40 = importer.save_or_locate(shipBuilder_itemport_40)

    shipBuilder_itemport_40.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_40.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_40.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_40.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_40.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_41 = ItemPort()
    shipBuilder_itemport_41.displayName = None
    shipBuilder_itemport_41.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_41.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_41.maxSize = 1L
    shipBuilder_itemport_41.minSize = 1L
    shipBuilder_itemport_41.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_41.portClass = 0L
    shipBuilder_itemport_41.parentImage = 0L
    shipBuilder_itemport_41.image = None
    shipBuilder_itemport_41.tagLocationX = 0.0
    shipBuilder_itemport_41.tagLocationY = 0.0
    shipBuilder_itemport_41 = importer.save_or_locate(shipBuilder_itemport_41)

    shipBuilder_itemport_41.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_41.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_41.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_41.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_41.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_42 = ItemPort()
    shipBuilder_itemport_42.displayName = None
    shipBuilder_itemport_42.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_42.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_42.maxSize = 1L
    shipBuilder_itemport_42.minSize = 1L
    shipBuilder_itemport_42.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_42.portClass = 0L
    shipBuilder_itemport_42.parentImage = 0L
    shipBuilder_itemport_42.image = None
    shipBuilder_itemport_42.tagLocationX = 0.0
    shipBuilder_itemport_42.tagLocationY = 0.0
    shipBuilder_itemport_42 = importer.save_or_locate(shipBuilder_itemport_42)

    shipBuilder_itemport_42.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_42.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_42.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_42.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_42.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_43 = ItemPort()
    shipBuilder_itemport_43.displayName = None
    shipBuilder_itemport_43.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_43.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_43.maxSize = 1L
    shipBuilder_itemport_43.minSize = 1L
    shipBuilder_itemport_43.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_43.portClass = 0L
    shipBuilder_itemport_43.parentImage = 0L
    shipBuilder_itemport_43.image = None
    shipBuilder_itemport_43.tagLocationX = 0.0
    shipBuilder_itemport_43.tagLocationY = 0.0
    shipBuilder_itemport_43 = importer.save_or_locate(shipBuilder_itemport_43)

    shipBuilder_itemport_43.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_43.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_43.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_43.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_43.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_44 = ItemPort()
    shipBuilder_itemport_44.displayName = u'Class 3 Slot'
    shipBuilder_itemport_44.name = u'hardpoint_class_3'
    shipBuilder_itemport_44.flags = u'top mid'
    shipBuilder_itemport_44.maxSize = 3L
    shipBuilder_itemport_44.minSize = 2L
    shipBuilder_itemport_44.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_44.portClass = 0L
    shipBuilder_itemport_44.parentImage = 0L
    shipBuilder_itemport_44.image = None
    shipBuilder_itemport_44.tagLocationX = 0.0
    shipBuilder_itemport_44.tagLocationY = 0.0
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
    shipBuilder_itemport_45.parentImage = 0L
    shipBuilder_itemport_45.image = None
    shipBuilder_itemport_45.tagLocationX = 0.0
    shipBuilder_itemport_45.tagLocationY = 0.0
    shipBuilder_itemport_45 = importer.save_or_locate(shipBuilder_itemport_45)

    shipBuilder_itemport_45.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_45.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_46 = ItemPort()
    shipBuilder_itemport_46.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_46.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_46.flags = u'right'
    shipBuilder_itemport_46.maxSize = 2L
    shipBuilder_itemport_46.minSize = 1L
    shipBuilder_itemport_46.parentVehicle = shipBuilder_vehicle_4
    shipBuilder_itemport_46.portClass = 0L
    shipBuilder_itemport_46.parentImage = 0L
    shipBuilder_itemport_46.image = None
    shipBuilder_itemport_46.tagLocationX = 0.0
    shipBuilder_itemport_46.tagLocationY = 0.0
    shipBuilder_itemport_46 = importer.save_or_locate(shipBuilder_itemport_46)

    shipBuilder_itemport_46.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_46.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_47 = ItemPort()
    shipBuilder_itemport_47.displayName = None
    shipBuilder_itemport_47.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_47.flags = u'main rear'
    shipBuilder_itemport_47.maxSize = 3L
    shipBuilder_itemport_47.minSize = 2L
    shipBuilder_itemport_47.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_47.portClass = 0L
    shipBuilder_itemport_47.parentImage = 3L
    shipBuilder_itemport_47.image = None
    shipBuilder_itemport_47.tagLocationX = 16.2
    shipBuilder_itemport_47.tagLocationY = 46.5
    shipBuilder_itemport_47 = importer.save_or_locate(shipBuilder_itemport_47)

    shipBuilder_itemport_47.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_47.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_47.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_47.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_47.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_48 = ItemPort()
    shipBuilder_itemport_48.displayName = None
    shipBuilder_itemport_48.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_48.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_48.maxSize = 1L
    shipBuilder_itemport_48.minSize = 1L
    shipBuilder_itemport_48.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_48.portClass = 0L
    shipBuilder_itemport_48.parentImage = 0L
    shipBuilder_itemport_48.image = None
    shipBuilder_itemport_48.tagLocationX = 0.0
    shipBuilder_itemport_48.tagLocationY = 0.0
    shipBuilder_itemport_48 = importer.save_or_locate(shipBuilder_itemport_48)

    shipBuilder_itemport_48.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_48.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_48.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_48.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_48.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_49 = ItemPort()
    shipBuilder_itemport_49.displayName = None
    shipBuilder_itemport_49.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_49.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_49.maxSize = 1L
    shipBuilder_itemport_49.minSize = 1L
    shipBuilder_itemport_49.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_49.portClass = 0L
    shipBuilder_itemport_49.parentImage = 0L
    shipBuilder_itemport_49.image = None
    shipBuilder_itemport_49.tagLocationX = 0.0
    shipBuilder_itemport_49.tagLocationY = 0.0
    shipBuilder_itemport_49 = importer.save_or_locate(shipBuilder_itemport_49)

    shipBuilder_itemport_49.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_49.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_49.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_49.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_49.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_50 = ItemPort()
    shipBuilder_itemport_50.displayName = None
    shipBuilder_itemport_50.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_50.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_50.maxSize = 1L
    shipBuilder_itemport_50.minSize = 1L
    shipBuilder_itemport_50.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_50.portClass = 0L
    shipBuilder_itemport_50.parentImage = 0L
    shipBuilder_itemport_50.image = None
    shipBuilder_itemport_50.tagLocationX = 0.0
    shipBuilder_itemport_50.tagLocationY = 0.0
    shipBuilder_itemport_50 = importer.save_or_locate(shipBuilder_itemport_50)

    shipBuilder_itemport_50.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_50.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_50.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_50.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_50.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_51 = ItemPort()
    shipBuilder_itemport_51.displayName = None
    shipBuilder_itemport_51.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_51.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_51.maxSize = 1L
    shipBuilder_itemport_51.minSize = 1L
    shipBuilder_itemport_51.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_51.portClass = 0L
    shipBuilder_itemport_51.parentImage = 0L
    shipBuilder_itemport_51.image = None
    shipBuilder_itemport_51.tagLocationX = 0.0
    shipBuilder_itemport_51.tagLocationY = 0.0
    shipBuilder_itemport_51 = importer.save_or_locate(shipBuilder_itemport_51)

    shipBuilder_itemport_51.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_51.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_51.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_51.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_51.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_52 = ItemPort()
    shipBuilder_itemport_52.displayName = None
    shipBuilder_itemport_52.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_52.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_52.maxSize = 1L
    shipBuilder_itemport_52.minSize = 1L
    shipBuilder_itemport_52.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_52.portClass = 0L
    shipBuilder_itemport_52.parentImage = 0L
    shipBuilder_itemport_52.image = None
    shipBuilder_itemport_52.tagLocationX = 0.0
    shipBuilder_itemport_52.tagLocationY = 0.0
    shipBuilder_itemport_52 = importer.save_or_locate(shipBuilder_itemport_52)

    shipBuilder_itemport_52.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_52.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_52.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_52.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_52.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_53 = ItemPort()
    shipBuilder_itemport_53.displayName = None
    shipBuilder_itemport_53.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_53.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_53.maxSize = 1L
    shipBuilder_itemport_53.minSize = 1L
    shipBuilder_itemport_53.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_53.portClass = 0L
    shipBuilder_itemport_53.parentImage = 0L
    shipBuilder_itemport_53.image = None
    shipBuilder_itemport_53.tagLocationX = 0.0
    shipBuilder_itemport_53.tagLocationY = 0.0
    shipBuilder_itemport_53 = importer.save_or_locate(shipBuilder_itemport_53)

    shipBuilder_itemport_53.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_53.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_53.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_53.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_53.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_54 = ItemPort()
    shipBuilder_itemport_54.displayName = u'Class 3 Slot'
    shipBuilder_itemport_54.name = u'hardpoint_class_3'
    shipBuilder_itemport_54.flags = u'top mid'
    shipBuilder_itemport_54.maxSize = 3L
    shipBuilder_itemport_54.minSize = 1L
    shipBuilder_itemport_54.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_54.portClass = 0L
    shipBuilder_itemport_54.parentImage = 1L
    shipBuilder_itemport_54.image = None
    shipBuilder_itemport_54.tagLocationX = 46.5
    shipBuilder_itemport_54.tagLocationY = 11.6
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
    shipBuilder_itemport_55.parentImage = 2L
    shipBuilder_itemport_55.image = None
    shipBuilder_itemport_55.tagLocationX = 59.4
    shipBuilder_itemport_55.tagLocationY = 82.5
    shipBuilder_itemport_55 = importer.save_or_locate(shipBuilder_itemport_55)

    shipBuilder_itemport_55.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_55.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_55.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_55.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_55.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_55.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_56 = ItemPort()
    shipBuilder_itemport_56.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_56.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_56.flags = u'right'
    shipBuilder_itemport_56.maxSize = 2L
    shipBuilder_itemport_56.minSize = 1L
    shipBuilder_itemport_56.parentVehicle = shipBuilder_vehicle_5
    shipBuilder_itemport_56.portClass = 0L
    shipBuilder_itemport_56.parentImage = 1L
    shipBuilder_itemport_56.image = None
    shipBuilder_itemport_56.tagLocationX = 54.5
    shipBuilder_itemport_56.tagLocationY = 72.9
    shipBuilder_itemport_56 = importer.save_or_locate(shipBuilder_itemport_56)

    shipBuilder_itemport_56.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_56.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_56.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_56.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_56.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_56.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_57 = ItemPort()
    shipBuilder_itemport_57.displayName = u'Right Nose Slot'
    shipBuilder_itemport_57.name = u'hardpoint_class_1_nose_right'
    shipBuilder_itemport_57.flags = u'nose right'
    shipBuilder_itemport_57.maxSize = 2L
    shipBuilder_itemport_57.minSize = 1L
    shipBuilder_itemport_57.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_57.portClass = 0L
    shipBuilder_itemport_57.parentImage = 3L
    shipBuilder_itemport_57.image = None
    shipBuilder_itemport_57.tagLocationX = 67.0
    shipBuilder_itemport_57.tagLocationY = 57.0
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
    shipBuilder_itemport_58.parentImage = 4L
    shipBuilder_itemport_58.image = None
    shipBuilder_itemport_58.tagLocationX = 29.8
    shipBuilder_itemport_58.tagLocationY = 56.7
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
    shipBuilder_itemport_59.parentImage = 3L
    shipBuilder_itemport_59.image = None
    shipBuilder_itemport_59.tagLocationX = 50.4
    shipBuilder_itemport_59.tagLocationY = 50.8
    shipBuilder_itemport_59 = importer.save_or_locate(shipBuilder_itemport_59)

    shipBuilder_itemport_59.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_59.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_60 = ItemPort()
    shipBuilder_itemport_60.displayName = None
    shipBuilder_itemport_60.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_60.flags = u'main rear'
    shipBuilder_itemport_60.maxSize = 4L
    shipBuilder_itemport_60.minSize = 3L
    shipBuilder_itemport_60.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_60.portClass = 0L
    shipBuilder_itemport_60.parentImage = 3L
    shipBuilder_itemport_60.image = None
    shipBuilder_itemport_60.tagLocationX = 41.7
    shipBuilder_itemport_60.tagLocationY = 56.4
    shipBuilder_itemport_60 = importer.save_or_locate(shipBuilder_itemport_60)

    shipBuilder_itemport_60.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_60.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_60.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_60.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_60.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_61 = ItemPort()
    shipBuilder_itemport_61.displayName = None
    shipBuilder_itemport_61.name = u'hardpoint_thruster_bottom_back_left'
    shipBuilder_itemport_61.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_61.maxSize = 2L
    shipBuilder_itemport_61.minSize = 1L
    shipBuilder_itemport_61.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_61.portClass = 0L
    shipBuilder_itemport_61.parentImage = 0L
    shipBuilder_itemport_61.image = None
    shipBuilder_itemport_61.tagLocationX = 0.0
    shipBuilder_itemport_61.tagLocationY = 0.0
    shipBuilder_itemport_61 = importer.save_or_locate(shipBuilder_itemport_61)

    shipBuilder_itemport_61.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_61.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_61.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_61.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_61.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_62 = ItemPort()
    shipBuilder_itemport_62.displayName = None
    shipBuilder_itemport_62.name = u'hardpoint_thruster_bottom_back_right'
    shipBuilder_itemport_62.flags = u'maneuver orientation +Z lower rear right'
    shipBuilder_itemport_62.maxSize = 2L
    shipBuilder_itemport_62.minSize = 1L
    shipBuilder_itemport_62.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_62.portClass = 0L
    shipBuilder_itemport_62.parentImage = 0L
    shipBuilder_itemport_62.image = None
    shipBuilder_itemport_62.tagLocationX = 0.0
    shipBuilder_itemport_62.tagLocationY = 0.0
    shipBuilder_itemport_62 = importer.save_or_locate(shipBuilder_itemport_62)

    shipBuilder_itemport_62.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_62.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_62.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_62.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_62.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_63 = ItemPort()
    shipBuilder_itemport_63.displayName = None
    shipBuilder_itemport_63.name = u'hardpoint_thruster_bottom_front_left'
    shipBuilder_itemport_63.flags = u'maneuver orientation +Z retro lower front left'
    shipBuilder_itemport_63.maxSize = 2L
    shipBuilder_itemport_63.minSize = 1L
    shipBuilder_itemport_63.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_63.portClass = 0L
    shipBuilder_itemport_63.parentImage = 0L
    shipBuilder_itemport_63.image = None
    shipBuilder_itemport_63.tagLocationX = 0.0
    shipBuilder_itemport_63.tagLocationY = 0.0
    shipBuilder_itemport_63 = importer.save_or_locate(shipBuilder_itemport_63)

    shipBuilder_itemport_63.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_63.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_63.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_63.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_63.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_64 = ItemPort()
    shipBuilder_itemport_64.displayName = None
    shipBuilder_itemport_64.name = u'hardpoint_thruster_bottom_front_right'
    shipBuilder_itemport_64.flags = u'maneuver orientation +Z retro lower front right'
    shipBuilder_itemport_64.maxSize = 2L
    shipBuilder_itemport_64.minSize = 1L
    shipBuilder_itemport_64.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_64.portClass = 0L
    shipBuilder_itemport_64.parentImage = 0L
    shipBuilder_itemport_64.image = None
    shipBuilder_itemport_64.tagLocationX = 0.0
    shipBuilder_itemport_64.tagLocationY = 0.0
    shipBuilder_itemport_64 = importer.save_or_locate(shipBuilder_itemport_64)

    shipBuilder_itemport_64.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_64.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_64.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_64.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_64.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_65 = ItemPort()
    shipBuilder_itemport_65.displayName = None
    shipBuilder_itemport_65.name = u'hardpoint_thruster_top_front_right'
    shipBuilder_itemport_65.flags = u'maneuver orientation retro -X -Z top front right'
    shipBuilder_itemport_65.maxSize = 2L
    shipBuilder_itemport_65.minSize = 1L
    shipBuilder_itemport_65.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_65.portClass = 0L
    shipBuilder_itemport_65.parentImage = 0L
    shipBuilder_itemport_65.image = None
    shipBuilder_itemport_65.tagLocationX = 0.0
    shipBuilder_itemport_65.tagLocationY = 0.0
    shipBuilder_itemport_65 = importer.save_or_locate(shipBuilder_itemport_65)

    shipBuilder_itemport_65.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_65.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_65.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_65.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_65.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_66 = ItemPort()
    shipBuilder_itemport_66.displayName = None
    shipBuilder_itemport_66.name = u'hardpoint_thruster_top_front_left'
    shipBuilder_itemport_66.flags = u'maneuver orientation retro +X -Z top front left'
    shipBuilder_itemport_66.maxSize = 2L
    shipBuilder_itemport_66.minSize = 1L
    shipBuilder_itemport_66.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_66.portClass = 0L
    shipBuilder_itemport_66.parentImage = 0L
    shipBuilder_itemport_66.image = None
    shipBuilder_itemport_66.tagLocationX = 0.0
    shipBuilder_itemport_66.tagLocationY = 0.0
    shipBuilder_itemport_66 = importer.save_or_locate(shipBuilder_itemport_66)

    shipBuilder_itemport_66.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_66.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_66.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_66.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_66.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_67 = ItemPort()
    shipBuilder_itemport_67.displayName = None
    shipBuilder_itemport_67.name = u'hardpoint_thruster_top_back_right'
    shipBuilder_itemport_67.flags = u'maneuver orientation -X -Z top rear right'
    shipBuilder_itemport_67.maxSize = 2L
    shipBuilder_itemport_67.minSize = 1L
    shipBuilder_itemport_67.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_67.portClass = 0L
    shipBuilder_itemport_67.parentImage = 0L
    shipBuilder_itemport_67.image = None
    shipBuilder_itemport_67.tagLocationX = 0.0
    shipBuilder_itemport_67.tagLocationY = 0.0
    shipBuilder_itemport_67 = importer.save_or_locate(shipBuilder_itemport_67)

    shipBuilder_itemport_67.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_67.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_67.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_67.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_67.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_68 = ItemPort()
    shipBuilder_itemport_68.displayName = None
    shipBuilder_itemport_68.name = u'hardpoint_thruster_top_back_left'
    shipBuilder_itemport_68.flags = u'maneuver orientation +X -Z top rear left'
    shipBuilder_itemport_68.maxSize = 2L
    shipBuilder_itemport_68.minSize = 1L
    shipBuilder_itemport_68.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_68.portClass = 0L
    shipBuilder_itemport_68.parentImage = 0L
    shipBuilder_itemport_68.image = None
    shipBuilder_itemport_68.tagLocationX = 0.0
    shipBuilder_itemport_68.tagLocationY = 0.0
    shipBuilder_itemport_68 = importer.save_or_locate(shipBuilder_itemport_68)

    shipBuilder_itemport_68.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_68.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_68.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_68.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_68.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_69 = ItemPort()
    shipBuilder_itemport_69.displayName = u'Power Plant'
    shipBuilder_itemport_69.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_69.flags = u'main rear'
    shipBuilder_itemport_69.maxSize = 4L
    shipBuilder_itemport_69.minSize = 2L
    shipBuilder_itemport_69.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_69.portClass = 0L
    shipBuilder_itemport_69.parentImage = 4L
    shipBuilder_itemport_69.image = None
    shipBuilder_itemport_69.tagLocationX = 49.5
    shipBuilder_itemport_69.tagLocationY = 50.0
    shipBuilder_itemport_69 = importer.save_or_locate(shipBuilder_itemport_69)

    shipBuilder_itemport_69.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_69.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_70 = ItemPort()
    shipBuilder_itemport_70.displayName = None
    shipBuilder_itemport_70.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_70.flags = u'main rear'
    shipBuilder_itemport_70.maxSize = 4L
    shipBuilder_itemport_70.minSize = 3L
    shipBuilder_itemport_70.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_70.portClass = 0L
    shipBuilder_itemport_70.parentImage = 1L
    shipBuilder_itemport_70.image = None
    shipBuilder_itemport_70.tagLocationX = 38.3
    shipBuilder_itemport_70.tagLocationY = 25.2
    shipBuilder_itemport_70 = importer.save_or_locate(shipBuilder_itemport_70)

    shipBuilder_itemport_70.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_70.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_70.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_70.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_70.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_71 = ItemPort()
    shipBuilder_itemport_71.displayName = None
    shipBuilder_itemport_71.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_71.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_71.maxSize = 1L
    shipBuilder_itemport_71.minSize = 1L
    shipBuilder_itemport_71.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_71.portClass = 0L
    shipBuilder_itemport_71.parentImage = 0L
    shipBuilder_itemport_71.image = None
    shipBuilder_itemport_71.tagLocationX = 0.0
    shipBuilder_itemport_71.tagLocationY = 0.0
    shipBuilder_itemport_71 = importer.save_or_locate(shipBuilder_itemport_71)

    shipBuilder_itemport_71.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_71.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_71.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_71.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_71.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_72 = ItemPort()
    shipBuilder_itemport_72.displayName = None
    shipBuilder_itemport_72.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_72.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_72.maxSize = 1L
    shipBuilder_itemport_72.minSize = 1L
    shipBuilder_itemport_72.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_72.portClass = 0L
    shipBuilder_itemport_72.parentImage = 0L
    shipBuilder_itemport_72.image = None
    shipBuilder_itemport_72.tagLocationX = 0.0
    shipBuilder_itemport_72.tagLocationY = 0.0
    shipBuilder_itemport_72 = importer.save_or_locate(shipBuilder_itemport_72)

    shipBuilder_itemport_72.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_72.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_72.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_72.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_72.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_73 = ItemPort()
    shipBuilder_itemport_73.displayName = None
    shipBuilder_itemport_73.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_73.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_73.maxSize = 1L
    shipBuilder_itemport_73.minSize = 1L
    shipBuilder_itemport_73.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_73.portClass = 0L
    shipBuilder_itemport_73.parentImage = 0L
    shipBuilder_itemport_73.image = None
    shipBuilder_itemport_73.tagLocationX = 0.0
    shipBuilder_itemport_73.tagLocationY = 0.0
    shipBuilder_itemport_73 = importer.save_or_locate(shipBuilder_itemport_73)

    shipBuilder_itemport_73.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_73.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_73.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_73.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_73.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_74 = ItemPort()
    shipBuilder_itemport_74.displayName = None
    shipBuilder_itemport_74.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_74.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_74.maxSize = 1L
    shipBuilder_itemport_74.minSize = 1L
    shipBuilder_itemport_74.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_74.portClass = 0L
    shipBuilder_itemport_74.parentImage = 0L
    shipBuilder_itemport_74.image = None
    shipBuilder_itemport_74.tagLocationX = 0.0
    shipBuilder_itemport_74.tagLocationY = 0.0
    shipBuilder_itemport_74 = importer.save_or_locate(shipBuilder_itemport_74)

    shipBuilder_itemport_74.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_74.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_74.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_74.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_74.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_75 = ItemPort()
    shipBuilder_itemport_75.displayName = None
    shipBuilder_itemport_75.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_75.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_75.maxSize = 1L
    shipBuilder_itemport_75.minSize = 1L
    shipBuilder_itemport_75.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_75.portClass = 0L
    shipBuilder_itemport_75.parentImage = 0L
    shipBuilder_itemport_75.image = None
    shipBuilder_itemport_75.tagLocationX = 0.0
    shipBuilder_itemport_75.tagLocationY = 0.0
    shipBuilder_itemport_75 = importer.save_or_locate(shipBuilder_itemport_75)

    shipBuilder_itemport_75.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_75.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_75.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_75.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_75.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_76 = ItemPort()
    shipBuilder_itemport_76.displayName = None
    shipBuilder_itemport_76.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_76.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_76.maxSize = 1L
    shipBuilder_itemport_76.minSize = 1L
    shipBuilder_itemport_76.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_76.portClass = 0L
    shipBuilder_itemport_76.parentImage = 0L
    shipBuilder_itemport_76.image = None
    shipBuilder_itemport_76.tagLocationX = 0.0
    shipBuilder_itemport_76.tagLocationY = 0.0
    shipBuilder_itemport_76 = importer.save_or_locate(shipBuilder_itemport_76)

    shipBuilder_itemport_76.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_76.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_76.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_76.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_76.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_77 = ItemPort()
    shipBuilder_itemport_77.displayName = None
    shipBuilder_itemport_77.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_77.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_77.maxSize = 1L
    shipBuilder_itemport_77.minSize = 1L
    shipBuilder_itemport_77.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_77.portClass = 0L
    shipBuilder_itemport_77.parentImage = 0L
    shipBuilder_itemport_77.image = None
    shipBuilder_itemport_77.tagLocationX = 0.0
    shipBuilder_itemport_77.tagLocationY = 0.0
    shipBuilder_itemport_77 = importer.save_or_locate(shipBuilder_itemport_77)

    shipBuilder_itemport_77.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_77.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_77.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_77.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_77.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_78 = ItemPort()
    shipBuilder_itemport_78.displayName = None
    shipBuilder_itemport_78.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_78.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_78.maxSize = 1L
    shipBuilder_itemport_78.minSize = 1L
    shipBuilder_itemport_78.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_78.portClass = 0L
    shipBuilder_itemport_78.parentImage = 0L
    shipBuilder_itemport_78.image = None
    shipBuilder_itemport_78.tagLocationX = 0.0
    shipBuilder_itemport_78.tagLocationY = 0.0
    shipBuilder_itemport_78 = importer.save_or_locate(shipBuilder_itemport_78)

    shipBuilder_itemport_78.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_78.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_78.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_78.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_78.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_79 = ItemPort()
    shipBuilder_itemport_79.displayName = None
    shipBuilder_itemport_79.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_79.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_79.maxSize = 1L
    shipBuilder_itemport_79.minSize = 1L
    shipBuilder_itemport_79.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_79.portClass = 0L
    shipBuilder_itemport_79.parentImage = 0L
    shipBuilder_itemport_79.image = None
    shipBuilder_itemport_79.tagLocationX = 0.0
    shipBuilder_itemport_79.tagLocationY = 0.0
    shipBuilder_itemport_79 = importer.save_or_locate(shipBuilder_itemport_79)

    shipBuilder_itemport_79.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_79.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_79.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_79.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_79.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_80 = ItemPort()
    shipBuilder_itemport_80.displayName = None
    shipBuilder_itemport_80.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_80.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_80.maxSize = 1L
    shipBuilder_itemport_80.minSize = 1L
    shipBuilder_itemport_80.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_80.portClass = 0L
    shipBuilder_itemport_80.parentImage = 0L
    shipBuilder_itemport_80.image = None
    shipBuilder_itemport_80.tagLocationX = 0.0
    shipBuilder_itemport_80.tagLocationY = 0.0
    shipBuilder_itemport_80 = importer.save_or_locate(shipBuilder_itemport_80)

    shipBuilder_itemport_80.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_80.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_80.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_80.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_80.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_81 = ItemPort()
    shipBuilder_itemport_81.displayName = None
    shipBuilder_itemport_81.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_81.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_81.maxSize = 1L
    shipBuilder_itemport_81.minSize = 1L
    shipBuilder_itemport_81.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_81.portClass = 0L
    shipBuilder_itemport_81.parentImage = 0L
    shipBuilder_itemport_81.image = None
    shipBuilder_itemport_81.tagLocationX = 0.0
    shipBuilder_itemport_81.tagLocationY = 0.0
    shipBuilder_itemport_81 = importer.save_or_locate(shipBuilder_itemport_81)

    shipBuilder_itemport_81.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_81.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_81.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_81.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_81.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_82 = ItemPort()
    shipBuilder_itemport_82.displayName = None
    shipBuilder_itemport_82.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_82.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_82.maxSize = 1L
    shipBuilder_itemport_82.minSize = 1L
    shipBuilder_itemport_82.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_82.portClass = 0L
    shipBuilder_itemport_82.parentImage = 0L
    shipBuilder_itemport_82.image = None
    shipBuilder_itemport_82.tagLocationX = 0.0
    shipBuilder_itemport_82.tagLocationY = 0.0
    shipBuilder_itemport_82 = importer.save_or_locate(shipBuilder_itemport_82)

    shipBuilder_itemport_82.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_82.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_82.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_82.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_82.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_83 = ItemPort()
    shipBuilder_itemport_83.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_83.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_83.flags = u'nose'
    shipBuilder_itemport_83.maxSize = 2L
    shipBuilder_itemport_83.minSize = 1L
    shipBuilder_itemport_83.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_83.portClass = 0L
    shipBuilder_itemport_83.parentImage = 3L
    shipBuilder_itemport_83.image = None
    shipBuilder_itemport_83.tagLocationX = 73.0
    shipBuilder_itemport_83.tagLocationY = 38.0
    shipBuilder_itemport_83 = importer.save_or_locate(shipBuilder_itemport_83)

    shipBuilder_itemport_83.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_83.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_83.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_83.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_83.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_83.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_84 = ItemPort()
    shipBuilder_itemport_84.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_84.name = u'hardpoint_class3_top_left_wing_350R'
    shipBuilder_itemport_84.flags = u'upper left wing'
    shipBuilder_itemport_84.maxSize = 3L
    shipBuilder_itemport_84.minSize = 1L
    shipBuilder_itemport_84.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_84.portClass = 0L
    shipBuilder_itemport_84.parentImage = 2L
    shipBuilder_itemport_84.image = None
    shipBuilder_itemport_84.tagLocationX = 72.6
    shipBuilder_itemport_84.tagLocationY = 22.7
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
    shipBuilder_itemport_85.parentImage = 2L
    shipBuilder_itemport_85.image = None
    shipBuilder_itemport_85.tagLocationX = 78.0
    shipBuilder_itemport_85.tagLocationY = 35.5
    shipBuilder_itemport_85 = importer.save_or_locate(shipBuilder_itemport_85)

    shipBuilder_itemport_85.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_85.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_86 = ItemPort()
    shipBuilder_itemport_86.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_86.name = u'hardpoint_class3_top_right_wing_350R'
    shipBuilder_itemport_86.flags = u'upper right wing'
    shipBuilder_itemport_86.maxSize = 3L
    shipBuilder_itemport_86.minSize = 1L
    shipBuilder_itemport_86.parentVehicle = shipBuilder_vehicle_7
    shipBuilder_itemport_86.portClass = 0L
    shipBuilder_itemport_86.parentImage = 1L
    shipBuilder_itemport_86.image = None
    shipBuilder_itemport_86.tagLocationX = 28.6
    shipBuilder_itemport_86.tagLocationY = 22.7
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
    shipBuilder_itemport_87.parentImage = 1L
    shipBuilder_itemport_87.image = None
    shipBuilder_itemport_87.tagLocationX = 21.6
    shipBuilder_itemport_87.tagLocationY = 36.0
    shipBuilder_itemport_87 = importer.save_or_locate(shipBuilder_itemport_87)

    shipBuilder_itemport_87.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_87.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_88 = ItemPort()
    shipBuilder_itemport_88.displayName = u'Power Plant'
    shipBuilder_itemport_88.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_88.flags = u'main rear'
    shipBuilder_itemport_88.maxSize = 3L
    shipBuilder_itemport_88.minSize = 2L
    shipBuilder_itemport_88.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_88.portClass = 0L
    shipBuilder_itemport_88.parentImage = 1L
    shipBuilder_itemport_88.image = None
    shipBuilder_itemport_88.tagLocationX = 40.5
    shipBuilder_itemport_88.tagLocationY = 24.7
    shipBuilder_itemport_88 = importer.save_or_locate(shipBuilder_itemport_88)

    shipBuilder_itemport_88.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_88.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_89 = ItemPort()
    shipBuilder_itemport_89.displayName = None
    shipBuilder_itemport_89.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_89.flags = u'main rear'
    shipBuilder_itemport_89.maxSize = 4L
    shipBuilder_itemport_89.minSize = 3L
    shipBuilder_itemport_89.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_89.portClass = 0L
    shipBuilder_itemport_89.parentImage = 1L
    shipBuilder_itemport_89.image = None
    shipBuilder_itemport_89.tagLocationX = 34.5
    shipBuilder_itemport_89.tagLocationY = 20.3
    shipBuilder_itemport_89 = importer.save_or_locate(shipBuilder_itemport_89)

    shipBuilder_itemport_89.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_89.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_89.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_89.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_89.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_90 = ItemPort()
    shipBuilder_itemport_90.displayName = None
    shipBuilder_itemport_90.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_90.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_90.maxSize = 1L
    shipBuilder_itemport_90.minSize = 1L
    shipBuilder_itemport_90.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_90.portClass = 0L
    shipBuilder_itemport_90.parentImage = 0L
    shipBuilder_itemport_90.image = None
    shipBuilder_itemport_90.tagLocationX = 0.0
    shipBuilder_itemport_90.tagLocationY = 0.0
    shipBuilder_itemport_90 = importer.save_or_locate(shipBuilder_itemport_90)

    shipBuilder_itemport_90.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_90.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_90.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_90.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_90.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_91 = ItemPort()
    shipBuilder_itemport_91.displayName = None
    shipBuilder_itemport_91.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_91.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_91.maxSize = 1L
    shipBuilder_itemport_91.minSize = 1L
    shipBuilder_itemport_91.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_91.portClass = 0L
    shipBuilder_itemport_91.parentImage = 0L
    shipBuilder_itemport_91.image = None
    shipBuilder_itemport_91.tagLocationX = 0.0
    shipBuilder_itemport_91.tagLocationY = 0.0
    shipBuilder_itemport_91 = importer.save_or_locate(shipBuilder_itemport_91)

    shipBuilder_itemport_91.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_91.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_91.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_91.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_91.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_92 = ItemPort()
    shipBuilder_itemport_92.displayName = None
    shipBuilder_itemport_92.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_92.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_92.maxSize = 1L
    shipBuilder_itemport_92.minSize = 1L
    shipBuilder_itemport_92.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_92.portClass = 0L
    shipBuilder_itemport_92.parentImage = 0L
    shipBuilder_itemport_92.image = None
    shipBuilder_itemport_92.tagLocationX = 0.0
    shipBuilder_itemport_92.tagLocationY = 0.0
    shipBuilder_itemport_92 = importer.save_or_locate(shipBuilder_itemport_92)

    shipBuilder_itemport_92.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_92.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_92.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_92.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_92.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_93 = ItemPort()
    shipBuilder_itemport_93.displayName = None
    shipBuilder_itemport_93.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_93.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_93.maxSize = 1L
    shipBuilder_itemport_93.minSize = 1L
    shipBuilder_itemport_93.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_93.portClass = 0L
    shipBuilder_itemport_93.parentImage = 0L
    shipBuilder_itemport_93.image = None
    shipBuilder_itemport_93.tagLocationX = 0.0
    shipBuilder_itemport_93.tagLocationY = 0.0
    shipBuilder_itemport_93 = importer.save_or_locate(shipBuilder_itemport_93)

    shipBuilder_itemport_93.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_93.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_93.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_93.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_93.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_94 = ItemPort()
    shipBuilder_itemport_94.displayName = None
    shipBuilder_itemport_94.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_94.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_94.maxSize = 1L
    shipBuilder_itemport_94.minSize = 1L
    shipBuilder_itemport_94.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_94.portClass = 0L
    shipBuilder_itemport_94.parentImage = 0L
    shipBuilder_itemport_94.image = None
    shipBuilder_itemport_94.tagLocationX = 0.0
    shipBuilder_itemport_94.tagLocationY = 0.0
    shipBuilder_itemport_94 = importer.save_or_locate(shipBuilder_itemport_94)

    shipBuilder_itemport_94.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_94.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_94.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_94.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_94.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_95 = ItemPort()
    shipBuilder_itemport_95.displayName = None
    shipBuilder_itemport_95.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_95.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_95.maxSize = 1L
    shipBuilder_itemport_95.minSize = 1L
    shipBuilder_itemport_95.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_95.portClass = 0L
    shipBuilder_itemport_95.parentImage = 0L
    shipBuilder_itemport_95.image = None
    shipBuilder_itemport_95.tagLocationX = 0.0
    shipBuilder_itemport_95.tagLocationY = 0.0
    shipBuilder_itemport_95 = importer.save_or_locate(shipBuilder_itemport_95)

    shipBuilder_itemport_95.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_95.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_95.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_95.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_95.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_96 = ItemPort()
    shipBuilder_itemport_96.displayName = None
    shipBuilder_itemport_96.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_96.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_96.maxSize = 1L
    shipBuilder_itemport_96.minSize = 1L
    shipBuilder_itemport_96.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_96.portClass = 0L
    shipBuilder_itemport_96.parentImage = 0L
    shipBuilder_itemport_96.image = None
    shipBuilder_itemport_96.tagLocationX = 0.0
    shipBuilder_itemport_96.tagLocationY = 0.0
    shipBuilder_itemport_96 = importer.save_or_locate(shipBuilder_itemport_96)

    shipBuilder_itemport_96.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_96.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_96.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_96.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_96.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_97 = ItemPort()
    shipBuilder_itemport_97.displayName = None
    shipBuilder_itemport_97.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_97.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_97.maxSize = 1L
    shipBuilder_itemport_97.minSize = 1L
    shipBuilder_itemport_97.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_97.portClass = 0L
    shipBuilder_itemport_97.parentImage = 0L
    shipBuilder_itemport_97.image = None
    shipBuilder_itemport_97.tagLocationX = 0.0
    shipBuilder_itemport_97.tagLocationY = 0.0
    shipBuilder_itemport_97 = importer.save_or_locate(shipBuilder_itemport_97)

    shipBuilder_itemport_97.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_97.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_97.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_97.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_97.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_98 = ItemPort()
    shipBuilder_itemport_98.displayName = None
    shipBuilder_itemport_98.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_98.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_98.maxSize = 1L
    shipBuilder_itemport_98.minSize = 1L
    shipBuilder_itemport_98.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_98.portClass = 0L
    shipBuilder_itemport_98.parentImage = 0L
    shipBuilder_itemport_98.image = None
    shipBuilder_itemport_98.tagLocationX = 0.0
    shipBuilder_itemport_98.tagLocationY = 0.0
    shipBuilder_itemport_98 = importer.save_or_locate(shipBuilder_itemport_98)

    shipBuilder_itemport_98.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_98.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_98.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_98.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_98.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_99 = ItemPort()
    shipBuilder_itemport_99.displayName = None
    shipBuilder_itemport_99.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_99.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_99.maxSize = 1L
    shipBuilder_itemport_99.minSize = 1L
    shipBuilder_itemport_99.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_99.portClass = 0L
    shipBuilder_itemport_99.parentImage = 0L
    shipBuilder_itemport_99.image = None
    shipBuilder_itemport_99.tagLocationX = 0.0
    shipBuilder_itemport_99.tagLocationY = 0.0
    shipBuilder_itemport_99 = importer.save_or_locate(shipBuilder_itemport_99)

    shipBuilder_itemport_99.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_99.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_99.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_99.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_99.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_100 = ItemPort()
    shipBuilder_itemport_100.displayName = None
    shipBuilder_itemport_100.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_100.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_100.maxSize = 1L
    shipBuilder_itemport_100.minSize = 1L
    shipBuilder_itemport_100.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_100.portClass = 0L
    shipBuilder_itemport_100.parentImage = 0L
    shipBuilder_itemport_100.image = None
    shipBuilder_itemport_100.tagLocationX = 0.0
    shipBuilder_itemport_100.tagLocationY = 0.0
    shipBuilder_itemport_100 = importer.save_or_locate(shipBuilder_itemport_100)

    shipBuilder_itemport_100.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_100.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_100.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_100.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_100.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_101 = ItemPort()
    shipBuilder_itemport_101.displayName = None
    shipBuilder_itemport_101.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_101.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_101.maxSize = 1L
    shipBuilder_itemport_101.minSize = 1L
    shipBuilder_itemport_101.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_101.portClass = 0L
    shipBuilder_itemport_101.parentImage = 0L
    shipBuilder_itemport_101.image = None
    shipBuilder_itemport_101.tagLocationX = 0.0
    shipBuilder_itemport_101.tagLocationY = 0.0
    shipBuilder_itemport_101 = importer.save_or_locate(shipBuilder_itemport_101)

    shipBuilder_itemport_101.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_101.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_101.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_101.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_101.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_102 = ItemPort()
    shipBuilder_itemport_102.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_102.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_102.flags = u'nose'
    shipBuilder_itemport_102.maxSize = 2L
    shipBuilder_itemport_102.minSize = 1L
    shipBuilder_itemport_102.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_102.portClass = 0L
    shipBuilder_itemport_102.parentImage = 3L
    shipBuilder_itemport_102.image = None
    shipBuilder_itemport_102.tagLocationX = 66.4
    shipBuilder_itemport_102.tagLocationY = 41.2
    shipBuilder_itemport_102 = importer.save_or_locate(shipBuilder_itemport_102)

    shipBuilder_itemport_102.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_102.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_102.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_102.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_102.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_102.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_103 = ItemPort()
    shipBuilder_itemport_103.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_103.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_103.flags = u'upper left wing'
    shipBuilder_itemport_103.maxSize = 3L
    shipBuilder_itemport_103.minSize = 1L
    shipBuilder_itemport_103.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_103.portClass = 0L
    shipBuilder_itemport_103.parentImage = 2L
    shipBuilder_itemport_103.image = None
    shipBuilder_itemport_103.tagLocationX = 71.6
    shipBuilder_itemport_103.tagLocationY = 18.9
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
    shipBuilder_itemport_104.parentImage = 2L
    shipBuilder_itemport_104.image = None
    shipBuilder_itemport_104.tagLocationX = 81.8
    shipBuilder_itemport_104.tagLocationY = 32.4
    shipBuilder_itemport_104 = importer.save_or_locate(shipBuilder_itemport_104)

    shipBuilder_itemport_104.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_104.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_105 = ItemPort()
    shipBuilder_itemport_105.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_105.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_105.flags = u'upper right wing'
    shipBuilder_itemport_105.maxSize = 3L
    shipBuilder_itemport_105.minSize = 1L
    shipBuilder_itemport_105.parentVehicle = shipBuilder_vehicle_8
    shipBuilder_itemport_105.portClass = 0L
    shipBuilder_itemport_105.parentImage = 1L
    shipBuilder_itemport_105.image = None
    shipBuilder_itemport_105.tagLocationX = 29.1
    shipBuilder_itemport_105.tagLocationY = 18.9
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
    shipBuilder_itemport_106.parentImage = 1L
    shipBuilder_itemport_106.image = None
    shipBuilder_itemport_106.tagLocationX = 21.3
    shipBuilder_itemport_106.tagLocationY = 31.5
    shipBuilder_itemport_106 = importer.save_or_locate(shipBuilder_itemport_106)

    shipBuilder_itemport_106.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_106.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_107 = ItemPort()
    shipBuilder_itemport_107.displayName = None
    shipBuilder_itemport_107.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_107.flags = u'main rear'
    shipBuilder_itemport_107.maxSize = 3L
    shipBuilder_itemport_107.minSize = 2L
    shipBuilder_itemport_107.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_107.portClass = 0L
    shipBuilder_itemport_107.parentImage = 0L
    shipBuilder_itemport_107.image = None
    shipBuilder_itemport_107.tagLocationX = 0.0
    shipBuilder_itemport_107.tagLocationY = 0.0
    shipBuilder_itemport_107 = importer.save_or_locate(shipBuilder_itemport_107)

    shipBuilder_itemport_107.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_107.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_107.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_107.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_107.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_108 = ItemPort()
    shipBuilder_itemport_108.displayName = None
    shipBuilder_itemport_108.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_108.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_108.maxSize = 1L
    shipBuilder_itemport_108.minSize = 1L
    shipBuilder_itemport_108.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_108.portClass = 0L
    shipBuilder_itemport_108.parentImage = 0L
    shipBuilder_itemport_108.image = None
    shipBuilder_itemport_108.tagLocationX = 0.0
    shipBuilder_itemport_108.tagLocationY = 0.0
    shipBuilder_itemport_108 = importer.save_or_locate(shipBuilder_itemport_108)

    shipBuilder_itemport_108.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_108.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_108.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_108.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_108.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_109 = ItemPort()
    shipBuilder_itemport_109.displayName = None
    shipBuilder_itemport_109.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_109.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_109.maxSize = 1L
    shipBuilder_itemport_109.minSize = 1L
    shipBuilder_itemport_109.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_109.portClass = 0L
    shipBuilder_itemport_109.parentImage = 0L
    shipBuilder_itemport_109.image = None
    shipBuilder_itemport_109.tagLocationX = 0.0
    shipBuilder_itemport_109.tagLocationY = 0.0
    shipBuilder_itemport_109 = importer.save_or_locate(shipBuilder_itemport_109)

    shipBuilder_itemport_109.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_109.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_109.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_109.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_109.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_110 = ItemPort()
    shipBuilder_itemport_110.displayName = None
    shipBuilder_itemport_110.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_110.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_110.maxSize = 1L
    shipBuilder_itemport_110.minSize = 1L
    shipBuilder_itemport_110.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_110.portClass = 0L
    shipBuilder_itemport_110.parentImage = 0L
    shipBuilder_itemport_110.image = None
    shipBuilder_itemport_110.tagLocationX = 0.0
    shipBuilder_itemport_110.tagLocationY = 0.0
    shipBuilder_itemport_110 = importer.save_or_locate(shipBuilder_itemport_110)

    shipBuilder_itemport_110.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_110.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_110.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_110.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_110.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_111 = ItemPort()
    shipBuilder_itemport_111.displayName = None
    shipBuilder_itemport_111.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_111.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_111.maxSize = 1L
    shipBuilder_itemport_111.minSize = 1L
    shipBuilder_itemport_111.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_111.portClass = 0L
    shipBuilder_itemport_111.parentImage = 0L
    shipBuilder_itemport_111.image = None
    shipBuilder_itemport_111.tagLocationX = 0.0
    shipBuilder_itemport_111.tagLocationY = 0.0
    shipBuilder_itemport_111 = importer.save_or_locate(shipBuilder_itemport_111)

    shipBuilder_itemport_111.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_111.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_111.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_111.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_111.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_112 = ItemPort()
    shipBuilder_itemport_112.displayName = None
    shipBuilder_itemport_112.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_112.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_112.maxSize = 1L
    shipBuilder_itemport_112.minSize = 1L
    shipBuilder_itemport_112.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_112.portClass = 0L
    shipBuilder_itemport_112.parentImage = 0L
    shipBuilder_itemport_112.image = None
    shipBuilder_itemport_112.tagLocationX = 0.0
    shipBuilder_itemport_112.tagLocationY = 0.0
    shipBuilder_itemport_112 = importer.save_or_locate(shipBuilder_itemport_112)

    shipBuilder_itemport_112.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_112.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_112.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_112.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_112.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_113 = ItemPort()
    shipBuilder_itemport_113.displayName = None
    shipBuilder_itemport_113.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_113.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_113.maxSize = 2L
    shipBuilder_itemport_113.minSize = 1L
    shipBuilder_itemport_113.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_113.portClass = 0L
    shipBuilder_itemport_113.parentImage = 0L
    shipBuilder_itemport_113.image = None
    shipBuilder_itemport_113.tagLocationX = 0.0
    shipBuilder_itemport_113.tagLocationY = 0.0
    shipBuilder_itemport_113 = importer.save_or_locate(shipBuilder_itemport_113)

    shipBuilder_itemport_113.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_113.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_113.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_113.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_113.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_114 = ItemPort()
    shipBuilder_itemport_114.displayName = u'Class 3 Slot'
    shipBuilder_itemport_114.name = u'hardpoint_class_3'
    shipBuilder_itemport_114.flags = u'top mid'
    shipBuilder_itemport_114.maxSize = 3L
    shipBuilder_itemport_114.minSize = 1L
    shipBuilder_itemport_114.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_114.portClass = 0L
    shipBuilder_itemport_114.parentImage = 0L
    shipBuilder_itemport_114.image = None
    shipBuilder_itemport_114.tagLocationX = 0.0
    shipBuilder_itemport_114.tagLocationY = 0.0
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
    shipBuilder_itemport_115.parentImage = 0L
    shipBuilder_itemport_115.image = None
    shipBuilder_itemport_115.tagLocationX = 0.0
    shipBuilder_itemport_115.tagLocationY = 0.0
    shipBuilder_itemport_115 = importer.save_or_locate(shipBuilder_itemport_115)

    shipBuilder_itemport_115.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_115.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_116 = ItemPort()
    shipBuilder_itemport_116.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_116.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_116.flags = u'right'
    shipBuilder_itemport_116.maxSize = 2L
    shipBuilder_itemport_116.minSize = 1L
    shipBuilder_itemport_116.parentVehicle = shipBuilder_vehicle_9
    shipBuilder_itemport_116.portClass = 0L
    shipBuilder_itemport_116.parentImage = 0L
    shipBuilder_itemport_116.image = None
    shipBuilder_itemport_116.tagLocationX = 0.0
    shipBuilder_itemport_116.tagLocationY = 0.0
    shipBuilder_itemport_116 = importer.save_or_locate(shipBuilder_itemport_116)

    shipBuilder_itemport_116.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_116.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_117 = ItemPort()
    shipBuilder_itemport_117.displayName = u'Power Plant'
    shipBuilder_itemport_117.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_117.flags = u'main rear'
    shipBuilder_itemport_117.maxSize = 3L
    shipBuilder_itemport_117.minSize = 2L
    shipBuilder_itemport_117.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_117.portClass = 0L
    shipBuilder_itemport_117.parentImage = 3L
    shipBuilder_itemport_117.image = None
    shipBuilder_itemport_117.tagLocationX = 45.0
    shipBuilder_itemport_117.tagLocationY = 48.0
    shipBuilder_itemport_117 = importer.save_or_locate(shipBuilder_itemport_117)

    shipBuilder_itemport_117.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_117.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_118 = ItemPort()
    shipBuilder_itemport_118.displayName = None
    shipBuilder_itemport_118.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_118.flags = u'main rear'
    shipBuilder_itemport_118.maxSize = 4L
    shipBuilder_itemport_118.minSize = 3L
    shipBuilder_itemport_118.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_118.portClass = 0L
    shipBuilder_itemport_118.parentImage = 3L
    shipBuilder_itemport_118.image = None
    shipBuilder_itemport_118.tagLocationX = 29.5
    shipBuilder_itemport_118.tagLocationY = 39.5
    shipBuilder_itemport_118 = importer.save_or_locate(shipBuilder_itemport_118)

    shipBuilder_itemport_118.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_118.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_118.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_118.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_118.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_119 = ItemPort()
    shipBuilder_itemport_119.displayName = None
    shipBuilder_itemport_119.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_119.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_119.maxSize = 1L
    shipBuilder_itemport_119.minSize = 1L
    shipBuilder_itemport_119.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_119.portClass = 0L
    shipBuilder_itemport_119.parentImage = 0L
    shipBuilder_itemport_119.image = None
    shipBuilder_itemport_119.tagLocationX = 0.0
    shipBuilder_itemport_119.tagLocationY = 0.0
    shipBuilder_itemport_119 = importer.save_or_locate(shipBuilder_itemport_119)

    shipBuilder_itemport_119.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_119.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_119.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_119.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_119.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_120 = ItemPort()
    shipBuilder_itemport_120.displayName = None
    shipBuilder_itemport_120.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_120.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_120.maxSize = 1L
    shipBuilder_itemport_120.minSize = 1L
    shipBuilder_itemport_120.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_120.portClass = 0L
    shipBuilder_itemport_120.parentImage = 0L
    shipBuilder_itemport_120.image = None
    shipBuilder_itemport_120.tagLocationX = 0.0
    shipBuilder_itemport_120.tagLocationY = 0.0
    shipBuilder_itemport_120 = importer.save_or_locate(shipBuilder_itemport_120)

    shipBuilder_itemport_120.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_120.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_120.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_120.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_120.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_121 = ItemPort()
    shipBuilder_itemport_121.displayName = None
    shipBuilder_itemport_121.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_121.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_121.maxSize = 1L
    shipBuilder_itemport_121.minSize = 1L
    shipBuilder_itemport_121.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_121.portClass = 0L
    shipBuilder_itemport_121.parentImage = 0L
    shipBuilder_itemport_121.image = None
    shipBuilder_itemport_121.tagLocationX = 0.0
    shipBuilder_itemport_121.tagLocationY = 0.0
    shipBuilder_itemport_121 = importer.save_or_locate(shipBuilder_itemport_121)

    shipBuilder_itemport_121.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_121.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_121.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_121.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_121.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_122 = ItemPort()
    shipBuilder_itemport_122.displayName = None
    shipBuilder_itemport_122.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_122.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_122.maxSize = 1L
    shipBuilder_itemport_122.minSize = 1L
    shipBuilder_itemport_122.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_122.portClass = 0L
    shipBuilder_itemport_122.parentImage = 0L
    shipBuilder_itemport_122.image = None
    shipBuilder_itemport_122.tagLocationX = 0.0
    shipBuilder_itemport_122.tagLocationY = 0.0
    shipBuilder_itemport_122 = importer.save_or_locate(shipBuilder_itemport_122)

    shipBuilder_itemport_122.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_122.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_122.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_122.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_122.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_123 = ItemPort()
    shipBuilder_itemport_123.displayName = None
    shipBuilder_itemport_123.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_123.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_123.maxSize = 1L
    shipBuilder_itemport_123.minSize = 1L
    shipBuilder_itemport_123.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_123.portClass = 0L
    shipBuilder_itemport_123.parentImage = 0L
    shipBuilder_itemport_123.image = None
    shipBuilder_itemport_123.tagLocationX = 0.0
    shipBuilder_itemport_123.tagLocationY = 0.0
    shipBuilder_itemport_123 = importer.save_or_locate(shipBuilder_itemport_123)

    shipBuilder_itemport_123.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_123.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_123.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_123.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_123.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_124 = ItemPort()
    shipBuilder_itemport_124.displayName = None
    shipBuilder_itemport_124.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_124.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_124.maxSize = 1L
    shipBuilder_itemport_124.minSize = 1L
    shipBuilder_itemport_124.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_124.portClass = 0L
    shipBuilder_itemport_124.parentImage = 0L
    shipBuilder_itemport_124.image = None
    shipBuilder_itemport_124.tagLocationX = 0.0
    shipBuilder_itemport_124.tagLocationY = 0.0
    shipBuilder_itemport_124 = importer.save_or_locate(shipBuilder_itemport_124)

    shipBuilder_itemport_124.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_124.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_124.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_124.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_124.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_125 = ItemPort()
    shipBuilder_itemport_125.displayName = None
    shipBuilder_itemport_125.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_125.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_125.maxSize = 1L
    shipBuilder_itemport_125.minSize = 1L
    shipBuilder_itemport_125.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_125.portClass = 0L
    shipBuilder_itemport_125.parentImage = 0L
    shipBuilder_itemport_125.image = None
    shipBuilder_itemport_125.tagLocationX = 0.0
    shipBuilder_itemport_125.tagLocationY = 0.0
    shipBuilder_itemport_125 = importer.save_or_locate(shipBuilder_itemport_125)

    shipBuilder_itemport_125.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_125.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_125.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_125.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_125.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_126 = ItemPort()
    shipBuilder_itemport_126.displayName = None
    shipBuilder_itemport_126.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_126.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_126.maxSize = 1L
    shipBuilder_itemport_126.minSize = 1L
    shipBuilder_itemport_126.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_126.portClass = 0L
    shipBuilder_itemport_126.parentImage = 0L
    shipBuilder_itemport_126.image = None
    shipBuilder_itemport_126.tagLocationX = 0.0
    shipBuilder_itemport_126.tagLocationY = 0.0
    shipBuilder_itemport_126 = importer.save_or_locate(shipBuilder_itemport_126)

    shipBuilder_itemport_126.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_126.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_126.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_126.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_126.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_127 = ItemPort()
    shipBuilder_itemport_127.displayName = None
    shipBuilder_itemport_127.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_127.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_127.maxSize = 1L
    shipBuilder_itemport_127.minSize = 1L
    shipBuilder_itemport_127.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_127.portClass = 0L
    shipBuilder_itemport_127.parentImage = 0L
    shipBuilder_itemport_127.image = None
    shipBuilder_itemport_127.tagLocationX = 0.0
    shipBuilder_itemport_127.tagLocationY = 0.0
    shipBuilder_itemport_127 = importer.save_or_locate(shipBuilder_itemport_127)

    shipBuilder_itemport_127.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_127.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_127.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_127.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_127.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_128 = ItemPort()
    shipBuilder_itemport_128.displayName = None
    shipBuilder_itemport_128.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_128.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_128.maxSize = 1L
    shipBuilder_itemport_128.minSize = 1L
    shipBuilder_itemport_128.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_128.portClass = 0L
    shipBuilder_itemport_128.parentImage = 0L
    shipBuilder_itemport_128.image = None
    shipBuilder_itemport_128.tagLocationX = 0.0
    shipBuilder_itemport_128.tagLocationY = 0.0
    shipBuilder_itemport_128 = importer.save_or_locate(shipBuilder_itemport_128)

    shipBuilder_itemport_128.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_128.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_128.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_128.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_128.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_129 = ItemPort()
    shipBuilder_itemport_129.displayName = None
    shipBuilder_itemport_129.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_129.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_129.maxSize = 1L
    shipBuilder_itemport_129.minSize = 1L
    shipBuilder_itemport_129.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_129.portClass = 0L
    shipBuilder_itemport_129.parentImage = 0L
    shipBuilder_itemport_129.image = None
    shipBuilder_itemport_129.tagLocationX = 0.0
    shipBuilder_itemport_129.tagLocationY = 0.0
    shipBuilder_itemport_129 = importer.save_or_locate(shipBuilder_itemport_129)

    shipBuilder_itemport_129.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_129.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_129.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_129.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_129.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_130 = ItemPort()
    shipBuilder_itemport_130.displayName = None
    shipBuilder_itemport_130.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_130.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_130.maxSize = 1L
    shipBuilder_itemport_130.minSize = 1L
    shipBuilder_itemport_130.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_130.portClass = 0L
    shipBuilder_itemport_130.parentImage = 0L
    shipBuilder_itemport_130.image = None
    shipBuilder_itemport_130.tagLocationX = 0.0
    shipBuilder_itemport_130.tagLocationY = 0.0
    shipBuilder_itemport_130 = importer.save_or_locate(shipBuilder_itemport_130)

    shipBuilder_itemport_130.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_130.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_130.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_130.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_130.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_131 = ItemPort()
    shipBuilder_itemport_131.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_131.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_131.flags = u'nose'
    shipBuilder_itemport_131.maxSize = 2L
    shipBuilder_itemport_131.minSize = 1L
    shipBuilder_itemport_131.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_131.portClass = 0L
    shipBuilder_itemport_131.parentImage = 3L
    shipBuilder_itemport_131.image = None
    shipBuilder_itemport_131.tagLocationX = 71.3
    shipBuilder_itemport_131.tagLocationY = 41.2
    shipBuilder_itemport_131 = importer.save_or_locate(shipBuilder_itemport_131)

    shipBuilder_itemport_131.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_131.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_131.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_131.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_131.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_131.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_132 = ItemPort()
    shipBuilder_itemport_132.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_132.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_132.flags = u'upper left wing'
    shipBuilder_itemport_132.maxSize = 3L
    shipBuilder_itemport_132.minSize = 1L
    shipBuilder_itemport_132.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_132.portClass = 0L
    shipBuilder_itemport_132.parentImage = 2L
    shipBuilder_itemport_132.image = None
    shipBuilder_itemport_132.tagLocationX = 75.3
    shipBuilder_itemport_132.tagLocationY = 21.4
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
    shipBuilder_itemport_133.parentImage = 2L
    shipBuilder_itemport_133.image = None
    shipBuilder_itemport_133.tagLocationX = 84.0
    shipBuilder_itemport_133.tagLocationY = 35.0
    shipBuilder_itemport_133 = importer.save_or_locate(shipBuilder_itemport_133)

    shipBuilder_itemport_133.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_133.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_134 = ItemPort()
    shipBuilder_itemport_134.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_134.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_134.flags = u'upper right wing'
    shipBuilder_itemport_134.maxSize = 3L
    shipBuilder_itemport_134.minSize = 1L
    shipBuilder_itemport_134.parentVehicle = shipBuilder_vehicle_10
    shipBuilder_itemport_134.portClass = 0L
    shipBuilder_itemport_134.parentImage = 1L
    shipBuilder_itemport_134.image = None
    shipBuilder_itemport_134.tagLocationX = 30.8
    shipBuilder_itemport_134.tagLocationY = 19.6
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
    shipBuilder_itemport_135.parentImage = 1L
    shipBuilder_itemport_135.image = None
    shipBuilder_itemport_135.tagLocationX = 23.8
    shipBuilder_itemport_135.tagLocationY = 33.1
    shipBuilder_itemport_135 = importer.save_or_locate(shipBuilder_itemport_135)

    shipBuilder_itemport_135.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_135.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_136 = ItemPort()
    shipBuilder_itemport_136.displayName = None
    shipBuilder_itemport_136.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_136.flags = u'main rear'
    shipBuilder_itemport_136.maxSize = 3L
    shipBuilder_itemport_136.minSize = 2L
    shipBuilder_itemport_136.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_136.portClass = 0L
    shipBuilder_itemport_136.parentImage = 3L
    shipBuilder_itemport_136.image = None
    shipBuilder_itemport_136.tagLocationX = 15.2
    shipBuilder_itemport_136.tagLocationY = 44.1
    shipBuilder_itemport_136 = importer.save_or_locate(shipBuilder_itemport_136)

    shipBuilder_itemport_136.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_136.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_136.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_136.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_136.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_137 = ItemPort()
    shipBuilder_itemport_137.displayName = None
    shipBuilder_itemport_137.name = u'hardpoint_thruster_rear_mid_right'
    shipBuilder_itemport_137.flags = u'maneuver orientation +Z -Z rear mid right'
    shipBuilder_itemport_137.maxSize = 1L
    shipBuilder_itemport_137.minSize = 1L
    shipBuilder_itemport_137.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_137.portClass = 0L
    shipBuilder_itemport_137.parentImage = 0L
    shipBuilder_itemport_137.image = None
    shipBuilder_itemport_137.tagLocationX = 0.0
    shipBuilder_itemport_137.tagLocationY = 0.0
    shipBuilder_itemport_137 = importer.save_or_locate(shipBuilder_itemport_137)

    shipBuilder_itemport_137.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_137.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_137.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_137.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_137.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_138 = ItemPort()
    shipBuilder_itemport_138.displayName = None
    shipBuilder_itemport_138.name = u'hardpoint_thruster_rear_mid_left'
    shipBuilder_itemport_138.flags = u'maneuver orientation +Z -Z rear mid left'
    shipBuilder_itemport_138.maxSize = 1L
    shipBuilder_itemport_138.minSize = 1L
    shipBuilder_itemport_138.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_138.portClass = 0L
    shipBuilder_itemport_138.parentImage = 0L
    shipBuilder_itemport_138.image = None
    shipBuilder_itemport_138.tagLocationX = 0.0
    shipBuilder_itemport_138.tagLocationY = 0.0
    shipBuilder_itemport_138 = importer.save_or_locate(shipBuilder_itemport_138)

    shipBuilder_itemport_138.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_138.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_138.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_138.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_138.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_139 = ItemPort()
    shipBuilder_itemport_139.displayName = None
    shipBuilder_itemport_139.name = u'hardpoint_thruster_front_mid_right'
    shipBuilder_itemport_139.flags = u'maneuver orientation +Z -Z front mid right'
    shipBuilder_itemport_139.maxSize = 1L
    shipBuilder_itemport_139.minSize = 1L
    shipBuilder_itemport_139.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_139.portClass = 0L
    shipBuilder_itemport_139.parentImage = 0L
    shipBuilder_itemport_139.image = None
    shipBuilder_itemport_139.tagLocationX = 0.0
    shipBuilder_itemport_139.tagLocationY = 0.0
    shipBuilder_itemport_139 = importer.save_or_locate(shipBuilder_itemport_139)

    shipBuilder_itemport_139.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_139.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_139.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_139.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_139.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_140 = ItemPort()
    shipBuilder_itemport_140.displayName = None
    shipBuilder_itemport_140.name = u'hardpoint_thruster_front_mid_left'
    shipBuilder_itemport_140.flags = u'maneuver orientation +Z -Z front mid left'
    shipBuilder_itemport_140.maxSize = 1L
    shipBuilder_itemport_140.minSize = 1L
    shipBuilder_itemport_140.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_140.portClass = 0L
    shipBuilder_itemport_140.parentImage = 0L
    shipBuilder_itemport_140.image = None
    shipBuilder_itemport_140.tagLocationX = 0.0
    shipBuilder_itemport_140.tagLocationY = 0.0
    shipBuilder_itemport_140 = importer.save_or_locate(shipBuilder_itemport_140)

    shipBuilder_itemport_140.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_140.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_140.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_140.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_140.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_141 = ItemPort()
    shipBuilder_itemport_141.displayName = None
    shipBuilder_itemport_141.name = u'hardpoint_thruster_front_top'
    shipBuilder_itemport_141.flags = u'maneuver orientation +Z -Y front top'
    shipBuilder_itemport_141.maxSize = 1L
    shipBuilder_itemport_141.minSize = 1L
    shipBuilder_itemport_141.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_141.portClass = 0L
    shipBuilder_itemport_141.parentImage = 0L
    shipBuilder_itemport_141.image = None
    shipBuilder_itemport_141.tagLocationX = 0.0
    shipBuilder_itemport_141.tagLocationY = 0.0
    shipBuilder_itemport_141 = importer.save_or_locate(shipBuilder_itemport_141)

    shipBuilder_itemport_141.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_141.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_141.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_141.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_141.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_142 = ItemPort()
    shipBuilder_itemport_142.displayName = None
    shipBuilder_itemport_142.name = u'hardpoint_thruster_front_bottom'
    shipBuilder_itemport_142.flags = u'maneuver orientation -Z -Y front bottom'
    shipBuilder_itemport_142.maxSize = 1L
    shipBuilder_itemport_142.minSize = 1L
    shipBuilder_itemport_142.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_142.portClass = 0L
    shipBuilder_itemport_142.parentImage = 0L
    shipBuilder_itemport_142.image = None
    shipBuilder_itemport_142.tagLocationX = 0.0
    shipBuilder_itemport_142.tagLocationY = 0.0
    shipBuilder_itemport_142 = importer.save_or_locate(shipBuilder_itemport_142)

    shipBuilder_itemport_142.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_142.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_142.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_142.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_142.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_143 = ItemPort()
    shipBuilder_itemport_143.displayName = u'Class 3 Slot'
    shipBuilder_itemport_143.name = u'hardpoint_class_3'
    shipBuilder_itemport_143.flags = u'top mid'
    shipBuilder_itemport_143.maxSize = 3L
    shipBuilder_itemport_143.minSize = 1L
    shipBuilder_itemport_143.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_143.portClass = 0L
    shipBuilder_itemport_143.parentImage = 1L
    shipBuilder_itemport_143.image = None
    shipBuilder_itemport_143.tagLocationX = 47.0
    shipBuilder_itemport_143.tagLocationY = 11.6
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
    shipBuilder_itemport_144.parentImage = 2L
    shipBuilder_itemport_144.image = None
    shipBuilder_itemport_144.tagLocationX = 59.1
    shipBuilder_itemport_144.tagLocationY = 79.7
    shipBuilder_itemport_144 = importer.save_or_locate(shipBuilder_itemport_144)

    shipBuilder_itemport_144.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_144.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_144.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_144.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_144.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_144.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_145 = ItemPort()
    shipBuilder_itemport_145.displayName = u'Right Whisker Class 1 Slot'
    shipBuilder_itemport_145.name = u'hardpoint_class_1_right_whisker'
    shipBuilder_itemport_145.flags = u'right'
    shipBuilder_itemport_145.maxSize = 2L
    shipBuilder_itemport_145.minSize = 1L
    shipBuilder_itemport_145.parentVehicle = shipBuilder_vehicle_11
    shipBuilder_itemport_145.portClass = 0L
    shipBuilder_itemport_145.parentImage = 1L
    shipBuilder_itemport_145.image = None
    shipBuilder_itemport_145.tagLocationX = 53.4
    shipBuilder_itemport_145.tagLocationY = 69.2
    shipBuilder_itemport_145 = importer.save_or_locate(shipBuilder_itemport_145)

    shipBuilder_itemport_145.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_145.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_145.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_145.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_145.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_145.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_146 = ItemPort()
    shipBuilder_itemport_146.displayName = u'Power Plant'
    shipBuilder_itemport_146.name = u'hardpoint_power_plant_attach'
    shipBuilder_itemport_146.flags = u'main rear'
    shipBuilder_itemport_146.maxSize = 3L
    shipBuilder_itemport_146.minSize = 2L
    shipBuilder_itemport_146.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_146.portClass = 0L
    shipBuilder_itemport_146.parentImage = 1L
    shipBuilder_itemport_146.image = None
    shipBuilder_itemport_146.tagLocationX = 42.8
    shipBuilder_itemport_146.tagLocationY = 19.5
    shipBuilder_itemport_146 = importer.save_or_locate(shipBuilder_itemport_146)

    shipBuilder_itemport_146.supportedTypes.add(shipBuilder_vehicleitemtype_4)
    shipBuilder_itemport_146.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_5)

    shipBuilder_itemport_147 = ItemPort()
    shipBuilder_itemport_147.displayName = None
    shipBuilder_itemport_147.name = u'hardpoint_engine_attach'
    shipBuilder_itemport_147.flags = u'main rear'
    shipBuilder_itemport_147.maxSize = 4L
    shipBuilder_itemport_147.minSize = 3L
    shipBuilder_itemport_147.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_147.portClass = 0L
    shipBuilder_itemport_147.parentImage = 1L
    shipBuilder_itemport_147.image = None
    shipBuilder_itemport_147.tagLocationX = 36.2
    shipBuilder_itemport_147.tagLocationY = 21.0
    shipBuilder_itemport_147 = importer.save_or_locate(shipBuilder_itemport_147)

    shipBuilder_itemport_147.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_147.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_147.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_147.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_147.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_148 = ItemPort()
    shipBuilder_itemport_148.displayName = None
    shipBuilder_itemport_148.name = u'hardpoint_thruster_rear_right_bottom'
    shipBuilder_itemport_148.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_148.maxSize = 1L
    shipBuilder_itemport_148.minSize = 1L
    shipBuilder_itemport_148.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_148.portClass = 0L
    shipBuilder_itemport_148.parentImage = 0L
    shipBuilder_itemport_148.image = None
    shipBuilder_itemport_148.tagLocationX = 0.0
    shipBuilder_itemport_148.tagLocationY = 0.0
    shipBuilder_itemport_148 = importer.save_or_locate(shipBuilder_itemport_148)

    shipBuilder_itemport_148.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_148.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_148.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_148.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_148.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_149 = ItemPort()
    shipBuilder_itemport_149.displayName = None
    shipBuilder_itemport_149.name = u'hardpoint_thruster_rear_right_mid'
    shipBuilder_itemport_149.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_149.maxSize = 1L
    shipBuilder_itemport_149.minSize = 1L
    shipBuilder_itemport_149.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_149.portClass = 0L
    shipBuilder_itemport_149.parentImage = 0L
    shipBuilder_itemport_149.image = None
    shipBuilder_itemport_149.tagLocationX = 0.0
    shipBuilder_itemport_149.tagLocationY = 0.0
    shipBuilder_itemport_149 = importer.save_or_locate(shipBuilder_itemport_149)

    shipBuilder_itemport_149.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_149.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_149.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_149.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_149.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_150 = ItemPort()
    shipBuilder_itemport_150.displayName = None
    shipBuilder_itemport_150.name = u'hardpoint_thruster_rear_right_upper'
    shipBuilder_itemport_150.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_150.maxSize = 1L
    shipBuilder_itemport_150.minSize = 1L
    shipBuilder_itemport_150.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_150.portClass = 0L
    shipBuilder_itemport_150.parentImage = 0L
    shipBuilder_itemport_150.image = None
    shipBuilder_itemport_150.tagLocationX = 0.0
    shipBuilder_itemport_150.tagLocationY = 0.0
    shipBuilder_itemport_150 = importer.save_or_locate(shipBuilder_itemport_150)

    shipBuilder_itemport_150.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_150.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_150.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_150.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_150.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_151 = ItemPort()
    shipBuilder_itemport_151.displayName = None
    shipBuilder_itemport_151.name = u'hardpoint_thruster_rear_left_bottom'
    shipBuilder_itemport_151.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_151.maxSize = 1L
    shipBuilder_itemport_151.minSize = 1L
    shipBuilder_itemport_151.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_151.portClass = 0L
    shipBuilder_itemport_151.parentImage = 0L
    shipBuilder_itemport_151.image = None
    shipBuilder_itemport_151.tagLocationX = 0.0
    shipBuilder_itemport_151.tagLocationY = 0.0
    shipBuilder_itemport_151 = importer.save_or_locate(shipBuilder_itemport_151)

    shipBuilder_itemport_151.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_151.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_151.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_151.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_151.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_152 = ItemPort()
    shipBuilder_itemport_152.displayName = None
    shipBuilder_itemport_152.name = u'hardpoint_thruster_rear_left_mid'
    shipBuilder_itemport_152.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_152.maxSize = 1L
    shipBuilder_itemport_152.minSize = 1L
    shipBuilder_itemport_152.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_152.portClass = 0L
    shipBuilder_itemport_152.parentImage = 0L
    shipBuilder_itemport_152.image = None
    shipBuilder_itemport_152.tagLocationX = 0.0
    shipBuilder_itemport_152.tagLocationY = 0.0
    shipBuilder_itemport_152 = importer.save_or_locate(shipBuilder_itemport_152)

    shipBuilder_itemport_152.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_152.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_152.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_152.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_152.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_153 = ItemPort()
    shipBuilder_itemport_153.displayName = None
    shipBuilder_itemport_153.name = u'hardpoint_thruster_rear_left_upper'
    shipBuilder_itemport_153.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_153.maxSize = 1L
    shipBuilder_itemport_153.minSize = 1L
    shipBuilder_itemport_153.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_153.portClass = 0L
    shipBuilder_itemport_153.parentImage = 0L
    shipBuilder_itemport_153.image = None
    shipBuilder_itemport_153.tagLocationX = 0.0
    shipBuilder_itemport_153.tagLocationY = 0.0
    shipBuilder_itemport_153 = importer.save_or_locate(shipBuilder_itemport_153)

    shipBuilder_itemport_153.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_153.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_153.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_153.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_153.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_154 = ItemPort()
    shipBuilder_itemport_154.displayName = None
    shipBuilder_itemport_154.name = u'hardpoint_thruster_front_right_bottom'
    shipBuilder_itemport_154.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_154.maxSize = 1L
    shipBuilder_itemport_154.minSize = 1L
    shipBuilder_itemport_154.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_154.portClass = 0L
    shipBuilder_itemport_154.parentImage = 0L
    shipBuilder_itemport_154.image = None
    shipBuilder_itemport_154.tagLocationX = 0.0
    shipBuilder_itemport_154.tagLocationY = 0.0
    shipBuilder_itemport_154 = importer.save_or_locate(shipBuilder_itemport_154)

    shipBuilder_itemport_154.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_154.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_154.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_154.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_154.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_155 = ItemPort()
    shipBuilder_itemport_155.displayName = None
    shipBuilder_itemport_155.name = u'hardpoint_thruster_front_right_upper'
    shipBuilder_itemport_155.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_155.maxSize = 1L
    shipBuilder_itemport_155.minSize = 1L
    shipBuilder_itemport_155.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_155.portClass = 0L
    shipBuilder_itemport_155.parentImage = 0L
    shipBuilder_itemport_155.image = None
    shipBuilder_itemport_155.tagLocationX = 0.0
    shipBuilder_itemport_155.tagLocationY = 0.0
    shipBuilder_itemport_155 = importer.save_or_locate(shipBuilder_itemport_155)

    shipBuilder_itemport_155.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_155.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_155.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_155.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_155.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_156 = ItemPort()
    shipBuilder_itemport_156.displayName = None
    shipBuilder_itemport_156.name = u'hardpoint_thruster_front_right_mid'
    shipBuilder_itemport_156.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_156.maxSize = 1L
    shipBuilder_itemport_156.minSize = 1L
    shipBuilder_itemport_156.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_156.portClass = 0L
    shipBuilder_itemport_156.parentImage = 0L
    shipBuilder_itemport_156.image = None
    shipBuilder_itemport_156.tagLocationX = 0.0
    shipBuilder_itemport_156.tagLocationY = 0.0
    shipBuilder_itemport_156 = importer.save_or_locate(shipBuilder_itemport_156)

    shipBuilder_itemport_156.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_156.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_156.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_156.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_156.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_157 = ItemPort()
    shipBuilder_itemport_157.displayName = None
    shipBuilder_itemport_157.name = u'hardpoint_thruster_front_left_bottom'
    shipBuilder_itemport_157.flags = u'maneuver orientation +Z lower rear left'
    shipBuilder_itemport_157.maxSize = 1L
    shipBuilder_itemport_157.minSize = 1L
    shipBuilder_itemport_157.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_157.portClass = 0L
    shipBuilder_itemport_157.parentImage = 0L
    shipBuilder_itemport_157.image = None
    shipBuilder_itemport_157.tagLocationX = 0.0
    shipBuilder_itemport_157.tagLocationY = 0.0
    shipBuilder_itemport_157 = importer.save_or_locate(shipBuilder_itemport_157)

    shipBuilder_itemport_157.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_157.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_157.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_157.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_157.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_158 = ItemPort()
    shipBuilder_itemport_158.displayName = None
    shipBuilder_itemport_158.name = u'hardpoint_thruster_front_left_upper'
    shipBuilder_itemport_158.flags = u'maneuver orientation +Z upper rear left'
    shipBuilder_itemport_158.maxSize = 1L
    shipBuilder_itemport_158.minSize = 1L
    shipBuilder_itemport_158.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_158.portClass = 0L
    shipBuilder_itemport_158.parentImage = 0L
    shipBuilder_itemport_158.image = None
    shipBuilder_itemport_158.tagLocationX = 0.0
    shipBuilder_itemport_158.tagLocationY = 0.0
    shipBuilder_itemport_158 = importer.save_or_locate(shipBuilder_itemport_158)

    shipBuilder_itemport_158.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_158.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_158.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_158.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_158.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_159 = ItemPort()
    shipBuilder_itemport_159.displayName = None
    shipBuilder_itemport_159.name = u'hardpoint_thruster_front_left_mid'
    shipBuilder_itemport_159.flags = u'maneuver orientation +Z mid rear left'
    shipBuilder_itemport_159.maxSize = 1L
    shipBuilder_itemport_159.minSize = 1L
    shipBuilder_itemport_159.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_159.portClass = 0L
    shipBuilder_itemport_159.parentImage = 0L
    shipBuilder_itemport_159.image = None
    shipBuilder_itemport_159.tagLocationX = 0.0
    shipBuilder_itemport_159.tagLocationY = 0.0
    shipBuilder_itemport_159 = importer.save_or_locate(shipBuilder_itemport_159)

    shipBuilder_itemport_159.supportedTypes.add(shipBuilder_vehicleitemtype_3)
    shipBuilder_itemport_159.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_3)
    shipBuilder_itemport_159.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_8)
    shipBuilder_itemport_159.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_10)
    shipBuilder_itemport_159.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_11)

    shipBuilder_itemport_160 = ItemPort()
    shipBuilder_itemport_160.displayName = u'Nose Class 2 Slot'
    shipBuilder_itemport_160.name = u'hardpoint_class_2_nose'
    shipBuilder_itemport_160.flags = u'nose'
    shipBuilder_itemport_160.maxSize = 2L
    shipBuilder_itemport_160.minSize = 1L
    shipBuilder_itemport_160.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_160.portClass = 0L
    shipBuilder_itemport_160.parentImage = 3L
    shipBuilder_itemport_160.image = None
    shipBuilder_itemport_160.tagLocationX = 70.5
    shipBuilder_itemport_160.tagLocationY = 37.0
    shipBuilder_itemport_160 = importer.save_or_locate(shipBuilder_itemport_160)

    shipBuilder_itemport_160.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_160.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)
    shipBuilder_itemport_160.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_160.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)
    shipBuilder_itemport_160.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_160.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_20)

    shipBuilder_itemport_161 = ItemPort()
    shipBuilder_itemport_161.displayName = u'Left Wing Pylon'
    shipBuilder_itemport_161.name = u'hardpoint_class_3_top_left_wing'
    shipBuilder_itemport_161.flags = u'upper left wing'
    shipBuilder_itemport_161.maxSize = 3L
    shipBuilder_itemport_161.minSize = 1L
    shipBuilder_itemport_161.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_161.portClass = 0L
    shipBuilder_itemport_161.parentImage = 2L
    shipBuilder_itemport_161.image = None
    shipBuilder_itemport_161.tagLocationX = 72.7
    shipBuilder_itemport_161.tagLocationY = 18.7
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
    shipBuilder_itemport_162.parentImage = 2L
    shipBuilder_itemport_162.image = None
    shipBuilder_itemport_162.tagLocationX = 81.7
    shipBuilder_itemport_162.tagLocationY = 30.6
    shipBuilder_itemport_162 = importer.save_or_locate(shipBuilder_itemport_162)

    shipBuilder_itemport_162.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_162.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_163 = ItemPort()
    shipBuilder_itemport_163.displayName = u'Right Wing Pylon'
    shipBuilder_itemport_163.name = u'hardpoint_class_3_top_right_wing'
    shipBuilder_itemport_163.flags = u'upper right wing'
    shipBuilder_itemport_163.maxSize = 3L
    shipBuilder_itemport_163.minSize = 1L
    shipBuilder_itemport_163.parentVehicle = shipBuilder_vehicle_12
    shipBuilder_itemport_163.portClass = 0L
    shipBuilder_itemport_163.parentImage = 1L
    shipBuilder_itemport_163.image = None
    shipBuilder_itemport_163.tagLocationX = 28.8
    shipBuilder_itemport_163.tagLocationY = 17.8
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
    shipBuilder_itemport_164.parentImage = 1L
    shipBuilder_itemport_164.image = None
    shipBuilder_itemport_164.tagLocationX = 20.7
    shipBuilder_itemport_164.tagLocationY = 31.1
    shipBuilder_itemport_164 = importer.save_or_locate(shipBuilder_itemport_164)

    shipBuilder_itemport_164.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_164.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_165 = ItemPort()
    shipBuilder_itemport_165.displayName = u'Left Display'
    shipBuilder_itemport_165.name = u'left_movil_lower_rotor'
    shipBuilder_itemport_165.flags = u'left lower'
    shipBuilder_itemport_165.maxSize = 1L
    shipBuilder_itemport_165.minSize = 1L
    shipBuilder_itemport_165.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_165.portClass = 0L
    shipBuilder_itemport_165.parentImage = 0L
    shipBuilder_itemport_165.image = None
    shipBuilder_itemport_165.tagLocationX = 0.0
    shipBuilder_itemport_165.tagLocationY = 0.0
    shipBuilder_itemport_165 = importer.save_or_locate(shipBuilder_itemport_165)

    shipBuilder_itemport_165.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_165.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_165.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_166 = ItemPort()
    shipBuilder_itemport_166.displayName = u'Right Display'
    shipBuilder_itemport_166.name = u'right_movil_lower_rotor'
    shipBuilder_itemport_166.flags = u'right lower'
    shipBuilder_itemport_166.maxSize = 1L
    shipBuilder_itemport_166.minSize = 1L
    shipBuilder_itemport_166.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_166.portClass = 0L
    shipBuilder_itemport_166.parentImage = 0L
    shipBuilder_itemport_166.image = None
    shipBuilder_itemport_166.tagLocationX = 0.0
    shipBuilder_itemport_166.tagLocationY = 0.0
    shipBuilder_itemport_166 = importer.save_or_locate(shipBuilder_itemport_166)

    shipBuilder_itemport_166.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_166.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_166.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_167 = ItemPort()
    shipBuilder_itemport_167.displayName = u'Top Left Display'
    shipBuilder_itemport_167.name = u'top_left_movil_lower_rotor'
    shipBuilder_itemport_167.flags = u'left upper'
    shipBuilder_itemport_167.maxSize = 1L
    shipBuilder_itemport_167.minSize = 1L
    shipBuilder_itemport_167.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_167.portClass = 0L
    shipBuilder_itemport_167.parentImage = 0L
    shipBuilder_itemport_167.image = None
    shipBuilder_itemport_167.tagLocationX = 0.0
    shipBuilder_itemport_167.tagLocationY = 0.0
    shipBuilder_itemport_167 = importer.save_or_locate(shipBuilder_itemport_167)

    shipBuilder_itemport_167.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_167.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_167.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_168 = ItemPort()
    shipBuilder_itemport_168.displayName = u'Top Right Display'
    shipBuilder_itemport_168.name = u'top_right_movil_lower_rotor'
    shipBuilder_itemport_168.flags = u'right upper'
    shipBuilder_itemport_168.maxSize = 1L
    shipBuilder_itemport_168.minSize = 1L
    shipBuilder_itemport_168.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_168.portClass = 0L
    shipBuilder_itemport_168.parentImage = 0L
    shipBuilder_itemport_168.image = None
    shipBuilder_itemport_168.tagLocationX = 0.0
    shipBuilder_itemport_168.tagLocationY = 0.0
    shipBuilder_itemport_168 = importer.save_or_locate(shipBuilder_itemport_168)

    shipBuilder_itemport_168.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_168.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_168.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_169 = ItemPort()
    shipBuilder_itemport_169.displayName = u'Front Slot'
    shipBuilder_itemport_169.name = u'hardpoint_class_4_nose'
    shipBuilder_itemport_169.flags = u'front nose'
    shipBuilder_itemport_169.maxSize = 4L
    shipBuilder_itemport_169.minSize = 1L
    shipBuilder_itemport_169.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_169.portClass = 0L
    shipBuilder_itemport_169.parentImage = 0L
    shipBuilder_itemport_169.image = None
    shipBuilder_itemport_169.tagLocationX = 0.0
    shipBuilder_itemport_169.tagLocationY = 0.0
    shipBuilder_itemport_169 = importer.save_or_locate(shipBuilder_itemport_169)

    shipBuilder_itemport_169.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_169.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_169.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_169.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_169.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_9)
    shipBuilder_itemport_169.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_17)
    shipBuilder_itemport_169.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_19)

    shipBuilder_itemport_170 = ItemPort()
    shipBuilder_itemport_170.displayName = u'Left Wing Slot'
    shipBuilder_itemport_170.name = u'hardpoint_class_2_left_wing'
    shipBuilder_itemport_170.flags = u'left wing bottom'
    shipBuilder_itemport_170.maxSize = 4L
    shipBuilder_itemport_170.minSize = 1L
    shipBuilder_itemport_170.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_170.portClass = 0L
    shipBuilder_itemport_170.parentImage = 0L
    shipBuilder_itemport_170.image = None
    shipBuilder_itemport_170.tagLocationX = 0.0
    shipBuilder_itemport_170.tagLocationY = 0.0
    shipBuilder_itemport_170 = importer.save_or_locate(shipBuilder_itemport_170)

    shipBuilder_itemport_170.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_170.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_171 = ItemPort()
    shipBuilder_itemport_171.displayName = u'Right Wing Slot'
    shipBuilder_itemport_171.name = u'hardpoint_class_2_right_wing'
    shipBuilder_itemport_171.flags = u'right wing bottom'
    shipBuilder_itemport_171.maxSize = 4L
    shipBuilder_itemport_171.minSize = 1L
    shipBuilder_itemport_171.parentVehicle = shipBuilder_vehicle_2
    shipBuilder_itemport_171.portClass = 0L
    shipBuilder_itemport_171.parentImage = 0L
    shipBuilder_itemport_171.image = None
    shipBuilder_itemport_171.tagLocationX = 0.0
    shipBuilder_itemport_171.tagLocationY = 0.0
    shipBuilder_itemport_171 = importer.save_or_locate(shipBuilder_itemport_171)

    shipBuilder_itemport_171.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_171.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_172 = ItemPort()
    shipBuilder_itemport_172.displayName = u'Top Turret Slot'
    shipBuilder_itemport_172.name = u'hardpoint_class_4_center'
    shipBuilder_itemport_172.flags = u'center'
    shipBuilder_itemport_172.maxSize = 4L
    shipBuilder_itemport_172.minSize = 2L
    shipBuilder_itemport_172.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_172.portClass = 0L
    shipBuilder_itemport_172.parentImage = 0L
    shipBuilder_itemport_172.image = None
    shipBuilder_itemport_172.tagLocationX = 0.0
    shipBuilder_itemport_172.tagLocationY = 0.0
    shipBuilder_itemport_172 = importer.save_or_locate(shipBuilder_itemport_172)

    shipBuilder_itemport_172.supportedTypes.add(shipBuilder_vehicleitemtype_1)
    shipBuilder_itemport_172.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_172.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_172.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_1)
    shipBuilder_itemport_172.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_172.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_172.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_9)
    shipBuilder_itemport_172.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_17)
    shipBuilder_itemport_172.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_19)

    shipBuilder_itemport_173 = ItemPort()
    shipBuilder_itemport_173.displayName = u'Left Bay Slot'
    shipBuilder_itemport_173.name = u'hardpoint_class_3_left_bay_door'
    shipBuilder_itemport_173.flags = u'left bottom'
    shipBuilder_itemport_173.maxSize = 3L
    shipBuilder_itemport_173.minSize = 1L
    shipBuilder_itemport_173.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_173.portClass = 0L
    shipBuilder_itemport_173.parentImage = 0L
    shipBuilder_itemport_173.image = None
    shipBuilder_itemport_173.tagLocationX = 0.0
    shipBuilder_itemport_173.tagLocationY = 0.0
    shipBuilder_itemport_173 = importer.save_or_locate(shipBuilder_itemport_173)

    shipBuilder_itemport_173.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_173.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_174 = ItemPort()
    shipBuilder_itemport_174.displayName = u'Right Bay Slot'
    shipBuilder_itemport_174.name = u'hardpoint_class_3_right_bay_door'
    shipBuilder_itemport_174.flags = u'right bottom'
    shipBuilder_itemport_174.maxSize = 3L
    shipBuilder_itemport_174.minSize = 1L
    shipBuilder_itemport_174.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_174.portClass = 0L
    shipBuilder_itemport_174.parentImage = 0L
    shipBuilder_itemport_174.image = None
    shipBuilder_itemport_174.tagLocationX = 0.0
    shipBuilder_itemport_174.tagLocationY = 0.0
    shipBuilder_itemport_174 = importer.save_or_locate(shipBuilder_itemport_174)

    shipBuilder_itemport_174.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_174.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_6)

    shipBuilder_itemport_175 = ItemPort()
    shipBuilder_itemport_175.displayName = u'Front Slot'
    shipBuilder_itemport_175.name = u'hardpoint_class_4_nose'
    shipBuilder_itemport_175.flags = u'front nose'
    shipBuilder_itemport_175.maxSize = 3L
    shipBuilder_itemport_175.minSize = 1L
    shipBuilder_itemport_175.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_175.portClass = 0L
    shipBuilder_itemport_175.parentImage = 0L
    shipBuilder_itemport_175.image = None
    shipBuilder_itemport_175.tagLocationX = 0.0
    shipBuilder_itemport_175.tagLocationY = 0.0
    shipBuilder_itemport_175 = importer.save_or_locate(shipBuilder_itemport_175)

    shipBuilder_itemport_175.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_175.supportedTypes.add(shipBuilder_vehicleitemtype_5)
    shipBuilder_itemport_175.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_4)
    shipBuilder_itemport_175.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_7)
    shipBuilder_itemport_175.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_9)
    shipBuilder_itemport_175.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_17)
    shipBuilder_itemport_175.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_19)

    shipBuilder_itemport_176 = ItemPort()
    shipBuilder_itemport_176.displayName = u'Left Display'
    shipBuilder_itemport_176.name = u'left_movil_lower_rotor'
    shipBuilder_itemport_176.flags = u'left lower'
    shipBuilder_itemport_176.maxSize = 1L
    shipBuilder_itemport_176.minSize = 1L
    shipBuilder_itemport_176.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_176.portClass = 0L
    shipBuilder_itemport_176.parentImage = 0L
    shipBuilder_itemport_176.image = None
    shipBuilder_itemport_176.tagLocationX = 0.0
    shipBuilder_itemport_176.tagLocationY = 0.0
    shipBuilder_itemport_176 = importer.save_or_locate(shipBuilder_itemport_176)

    shipBuilder_itemport_176.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_176.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_176.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_177 = ItemPort()
    shipBuilder_itemport_177.displayName = u'Right Display'
    shipBuilder_itemport_177.name = u'right_movil_lower_rotor'
    shipBuilder_itemport_177.flags = u'right lower'
    shipBuilder_itemport_177.maxSize = 1L
    shipBuilder_itemport_177.minSize = 1L
    shipBuilder_itemport_177.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_177.portClass = 0L
    shipBuilder_itemport_177.parentImage = 0L
    shipBuilder_itemport_177.image = None
    shipBuilder_itemport_177.tagLocationX = 0.0
    shipBuilder_itemport_177.tagLocationY = 0.0
    shipBuilder_itemport_177 = importer.save_or_locate(shipBuilder_itemport_177)

    shipBuilder_itemport_177.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_177.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_177.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_178 = ItemPort()
    shipBuilder_itemport_178.displayName = u'Top Left Display'
    shipBuilder_itemport_178.name = u'top_left_movil_lower_rotor'
    shipBuilder_itemport_178.flags = u'left upper'
    shipBuilder_itemport_178.maxSize = 1L
    shipBuilder_itemport_178.minSize = 1L
    shipBuilder_itemport_178.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_178.portClass = 0L
    shipBuilder_itemport_178.parentImage = 0L
    shipBuilder_itemport_178.image = None
    shipBuilder_itemport_178.tagLocationX = 0.0
    shipBuilder_itemport_178.tagLocationY = 0.0
    shipBuilder_itemport_178 = importer.save_or_locate(shipBuilder_itemport_178)

    shipBuilder_itemport_178.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_178.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_178.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_179 = ItemPort()
    shipBuilder_itemport_179.displayName = u'Top Right Display'
    shipBuilder_itemport_179.name = u'top_right_movil_lower_rotor'
    shipBuilder_itemport_179.flags = u'right upper'
    shipBuilder_itemport_179.maxSize = 1L
    shipBuilder_itemport_179.minSize = 1L
    shipBuilder_itemport_179.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_179.portClass = 0L
    shipBuilder_itemport_179.parentImage = 0L
    shipBuilder_itemport_179.image = None
    shipBuilder_itemport_179.tagLocationX = 0.0
    shipBuilder_itemport_179.tagLocationY = 0.0
    shipBuilder_itemport_179 = importer.save_or_locate(shipBuilder_itemport_179)

    shipBuilder_itemport_179.supportedTypes.add(shipBuilder_vehicleitemtype_6)
    shipBuilder_itemport_179.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_12)
    shipBuilder_itemport_179.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_15)

    shipBuilder_itemport_180 = ItemPort()
    shipBuilder_itemport_180.displayName = u'Left Wing Slot'
    shipBuilder_itemport_180.name = u'hardpoint_class_2_left_wing'
    shipBuilder_itemport_180.flags = u'left wing bottom'
    shipBuilder_itemport_180.maxSize = 3L
    shipBuilder_itemport_180.minSize = 1L
    shipBuilder_itemport_180.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_180.portClass = 0L
    shipBuilder_itemport_180.parentImage = 0L
    shipBuilder_itemport_180.image = None
    shipBuilder_itemport_180.tagLocationX = 0.0
    shipBuilder_itemport_180.tagLocationY = 0.0
    shipBuilder_itemport_180 = importer.save_or_locate(shipBuilder_itemport_180)

    shipBuilder_itemport_180.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_180.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

    shipBuilder_itemport_181 = ItemPort()
    shipBuilder_itemport_181.displayName = u'Right Wing Slot'
    shipBuilder_itemport_181.name = u'hardpoint_class_2_right_wing'
    shipBuilder_itemport_181.flags = u'right wing bottom'
    shipBuilder_itemport_181.maxSize = 3L
    shipBuilder_itemport_181.minSize = 1L
    shipBuilder_itemport_181.parentVehicle = shipBuilder_vehicle_6
    shipBuilder_itemport_181.portClass = 0L
    shipBuilder_itemport_181.parentImage = 0L
    shipBuilder_itemport_181.image = None
    shipBuilder_itemport_181.tagLocationX = 0.0
    shipBuilder_itemport_181.tagLocationY = 0.0
    shipBuilder_itemport_181 = importer.save_or_locate(shipBuilder_itemport_181)

    shipBuilder_itemport_181.supportedTypes.add(shipBuilder_vehicleitemtype_2)
    shipBuilder_itemport_181.supportedSubTypes.add(shipBuilder_vehicleitemsubtype_2)

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

    shipBuilder_build_1 = Build()
    shipBuilder_build_1.created_by = auth_user_32
    shipBuilder_build_1.name = u'Explorat0r'
    shipBuilder_build_1.role = u'Exploration'
    shipBuilder_build_1.ship = shipBuilder_ship_7
    shipBuilder_build_1.manufacturer_variant = True
    shipBuilder_build_1.engine_intake = None
    shipBuilder_build_1.powerplant = None
    shipBuilder_build_1.main_thruster = None
    shipBuilder_build_1.shield = None
    shipBuilder_build_1.cargo_mod = None
    shipBuilder_build_1.up_votes = 0L
    shipBuilder_build_1.down_votes = 0L
    shipBuilder_build_1.creation_date = datetime.datetime(2013, 9, 12, 22, 12, 47)
    shipBuilder_build_1.base_ship = False
    shipBuilder_build_1 = importer.save_or_locate(shipBuilder_build_1)

    shipBuilder_build_2 = Build()
    shipBuilder_build_2.created_by = auth_user_33
    shipBuilder_build_2.name = u'john 1'
    shipBuilder_build_2.role = u'Interdiction'
    shipBuilder_build_2.ship = shipBuilder_ship_8
    shipBuilder_build_2.manufacturer_variant = True
    shipBuilder_build_2.engine_intake = None
    shipBuilder_build_2.powerplant = None
    shipBuilder_build_2.main_thruster = None
    shipBuilder_build_2.shield = None
    shipBuilder_build_2.cargo_mod = None
    shipBuilder_build_2.up_votes = 0L
    shipBuilder_build_2.down_votes = 0L
    shipBuilder_build_2.creation_date = datetime.datetime(2013, 9, 12, 22, 44, 33)
    shipBuilder_build_2.base_ship = False
    shipBuilder_build_2 = importer.save_or_locate(shipBuilder_build_2)

    shipBuilder_build_3 = Build()
    shipBuilder_build_3.created_by = auth_user_38
    shipBuilder_build_3.name = u'Lethal Heavy Industries Connie'
    shipBuilder_build_3.role = u'Exploration'
    shipBuilder_build_3.ship = shipBuilder_ship_3
    shipBuilder_build_3.manufacturer_variant = True
    shipBuilder_build_3.engine_intake = None
    shipBuilder_build_3.powerplant = shipBuilder_item_12
    shipBuilder_build_3.main_thruster = shipBuilder_item_24
    shipBuilder_build_3.shield = shipBuilder_item_27
    shipBuilder_build_3.cargo_mod = shipBuilder_item_33
    shipBuilder_build_3.up_votes = 0L
    shipBuilder_build_3.down_votes = 0L
    shipBuilder_build_3.creation_date = datetime.datetime(2013, 9, 12, 22, 56, 39)
    shipBuilder_build_3.base_ship = False
    shipBuilder_build_3 = importer.save_or_locate(shipBuilder_build_3)

    shipBuilder_build_4 = Build()
    shipBuilder_build_4.created_by = auth_user_38
    shipBuilder_build_4.name = u'LHI Interceptor'
    shipBuilder_build_4.role = u'Interdiction'
    shipBuilder_build_4.ship = shipBuilder_ship_8
    shipBuilder_build_4.manufacturer_variant = True
    shipBuilder_build_4.engine_intake = None
    shipBuilder_build_4.powerplant = shipBuilder_item_3
    shipBuilder_build_4.main_thruster = shipBuilder_item_15
    shipBuilder_build_4.shield = shipBuilder_item_27
    shipBuilder_build_4.cargo_mod = shipBuilder_item_33
    shipBuilder_build_4.up_votes = 0L
    shipBuilder_build_4.down_votes = 0L
    shipBuilder_build_4.creation_date = datetime.datetime(2013, 9, 12, 22, 59, 22)
    shipBuilder_build_4.base_ship = False
    shipBuilder_build_4 = importer.save_or_locate(shipBuilder_build_4)

    shipBuilder_build_5 = Build()
    shipBuilder_build_5.created_by = auth_user_38
    shipBuilder_build_5.name = u'LHI Nighthawk'
    shipBuilder_build_5.role = u'Bounty Hunting'
    shipBuilder_build_5.ship = shipBuilder_ship_6
    shipBuilder_build_5.manufacturer_variant = True
    shipBuilder_build_5.engine_intake = None
    shipBuilder_build_5.powerplant = shipBuilder_item_6
    shipBuilder_build_5.main_thruster = shipBuilder_item_24
    shipBuilder_build_5.shield = shipBuilder_item_27
    shipBuilder_build_5.cargo_mod = shipBuilder_item_33
    shipBuilder_build_5.up_votes = 0L
    shipBuilder_build_5.down_votes = 0L
    shipBuilder_build_5.creation_date = datetime.datetime(2013, 9, 12, 23, 1, 23)
    shipBuilder_build_5.base_ship = False
    shipBuilder_build_5 = importer.save_or_locate(shipBuilder_build_5)

    shipBuilder_build_6 = Build()
    shipBuilder_build_6.created_by = auth_user_39
    shipBuilder_build_6.name = u'315p custom'
    shipBuilder_build_6.role = u'Exploration'
    shipBuilder_build_6.ship = shipBuilder_ship_1
    shipBuilder_build_6.manufacturer_variant = True
    shipBuilder_build_6.engine_intake = None
    shipBuilder_build_6.powerplant = shipBuilder_item_5
    shipBuilder_build_6.main_thruster = shipBuilder_item_20
    shipBuilder_build_6.shield = shipBuilder_item_29
    shipBuilder_build_6.cargo_mod = None
    shipBuilder_build_6.up_votes = 0L
    shipBuilder_build_6.down_votes = 0L
    shipBuilder_build_6.creation_date = datetime.datetime(2013, 9, 12, 23, 7, 57)
    shipBuilder_build_6.base_ship = False
    shipBuilder_build_6 = importer.save_or_locate(shipBuilder_build_6)

    shipBuilder_build_7 = Build()
    shipBuilder_build_7.created_by = auth_user_48
    shipBuilder_build_7.name = u'300 variant 1'
    shipBuilder_build_7.role = u'Exploration'
    shipBuilder_build_7.ship = shipBuilder_ship_1
    shipBuilder_build_7.manufacturer_variant = True
    shipBuilder_build_7.engine_intake = None
    shipBuilder_build_7.powerplant = None
    shipBuilder_build_7.main_thruster = None
    shipBuilder_build_7.shield = None
    shipBuilder_build_7.cargo_mod = None
    shipBuilder_build_7.up_votes = 0L
    shipBuilder_build_7.down_votes = 0L
    shipBuilder_build_7.creation_date = datetime.datetime(2013, 9, 13, 1, 49, 2)
    shipBuilder_build_7.base_ship = False
    shipBuilder_build_7 = importer.save_or_locate(shipBuilder_build_7)

    shipBuilder_build_8 = Build()
    shipBuilder_build_8.created_by = auth_user_49
    shipBuilder_build_8.name = u'328 Knight'
    shipBuilder_build_8.role = u'Escort'
    shipBuilder_build_8.ship = shipBuilder_ship_1
    shipBuilder_build_8.manufacturer_variant = True
    shipBuilder_build_8.engine_intake = None
    shipBuilder_build_8.powerplant = shipBuilder_item_7
    shipBuilder_build_8.main_thruster = shipBuilder_item_22
    shipBuilder_build_8.shield = shipBuilder_item_31
    shipBuilder_build_8.cargo_mod = None
    shipBuilder_build_8.up_votes = 0L
    shipBuilder_build_8.down_votes = 0L
    shipBuilder_build_8.creation_date = datetime.datetime(2013, 9, 13, 1, 56, 24)
    shipBuilder_build_8.base_ship = False
    shipBuilder_build_8 = importer.save_or_locate(shipBuilder_build_8)

    shipBuilder_build_9 = Build()
    shipBuilder_build_9.created_by = auth_user_49
    shipBuilder_build_9.name = u'Mercury'
    shipBuilder_build_9.role = u'Transport'
    shipBuilder_build_9.ship = shipBuilder_ship_2
    shipBuilder_build_9.manufacturer_variant = True
    shipBuilder_build_9.engine_intake = None
    shipBuilder_build_9.powerplant = shipBuilder_item_1
    shipBuilder_build_9.main_thruster = shipBuilder_item_16
    shipBuilder_build_9.shield = shipBuilder_item_30
    shipBuilder_build_9.cargo_mod = shipBuilder_item_32
    shipBuilder_build_9.up_votes = 0L
    shipBuilder_build_9.down_votes = 0L
    shipBuilder_build_9.creation_date = datetime.datetime(2013, 9, 13, 1, 59, 58)
    shipBuilder_build_9.base_ship = False
    shipBuilder_build_9 = importer.save_or_locate(shipBuilder_build_9)

    shipBuilder_build_10 = Build()
    shipBuilder_build_10.created_by = auth_user_57
    shipBuilder_build_10.name = u'315p custom'
    shipBuilder_build_10.role = u'Exploration'
    shipBuilder_build_10.ship = shipBuilder_ship_1
    shipBuilder_build_10.manufacturer_variant = True
    shipBuilder_build_10.engine_intake = None
    shipBuilder_build_10.powerplant = shipBuilder_item_5
    shipBuilder_build_10.main_thruster = shipBuilder_item_20
    shipBuilder_build_10.shield = shipBuilder_item_29
    shipBuilder_build_10.cargo_mod = None
    shipBuilder_build_10.up_votes = 0L
    shipBuilder_build_10.down_votes = 0L
    shipBuilder_build_10.creation_date = datetime.datetime(2013, 9, 13, 4, 25, 11)
    shipBuilder_build_10.base_ship = False
    shipBuilder_build_10 = importer.save_or_locate(shipBuilder_build_10)

    shipBuilder_build_11 = Build()
    shipBuilder_build_11.created_by = auth_user_57
    shipBuilder_build_11.name = u'Freelancer (Base)'
    shipBuilder_build_11.role = u'Interdiction'
    shipBuilder_build_11.ship = shipBuilder_ship_7
    shipBuilder_build_11.manufacturer_variant = True
    shipBuilder_build_11.engine_intake = None
    shipBuilder_build_11.powerplant = None
    shipBuilder_build_11.main_thruster = None
    shipBuilder_build_11.shield = None
    shipBuilder_build_11.cargo_mod = None
    shipBuilder_build_11.up_votes = 0L
    shipBuilder_build_11.down_votes = 0L
    shipBuilder_build_11.creation_date = datetime.datetime(2013, 9, 13, 4, 27, 2)
    shipBuilder_build_11.base_ship = False
    shipBuilder_build_11 = importer.save_or_locate(shipBuilder_build_11)

    shipBuilder_build_12 = Build()
    shipBuilder_build_12.created_by = auth_user_60
    shipBuilder_build_12.name = u'325A Oh Yeah'
    shipBuilder_build_12.role = u'Piracy'
    shipBuilder_build_12.ship = shipBuilder_ship_1
    shipBuilder_build_12.manufacturer_variant = True
    shipBuilder_build_12.engine_intake = None
    shipBuilder_build_12.powerplant = shipBuilder_item_5
    shipBuilder_build_12.main_thruster = shipBuilder_item_22
    shipBuilder_build_12.shield = shipBuilder_item_31
    shipBuilder_build_12.cargo_mod = shipBuilder_item_33
    shipBuilder_build_12.up_votes = 0L
    shipBuilder_build_12.down_votes = 0L
    shipBuilder_build_12.creation_date = datetime.datetime(2013, 9, 13, 6, 27, 14)
    shipBuilder_build_12.base_ship = False
    shipBuilder_build_12 = importer.save_or_locate(shipBuilder_build_12)

    shipBuilder_build_13 = Build()
    shipBuilder_build_13.created_by = auth_user_73
    shipBuilder_build_13.name = u'1'
    shipBuilder_build_13.role = u'Interdiction'
    shipBuilder_build_13.ship = shipBuilder_ship_3
    shipBuilder_build_13.manufacturer_variant = True
    shipBuilder_build_13.engine_intake = None
    shipBuilder_build_13.powerplant = None
    shipBuilder_build_13.main_thruster = None
    shipBuilder_build_13.shield = None
    shipBuilder_build_13.cargo_mod = None
    shipBuilder_build_13.up_votes = 0L
    shipBuilder_build_13.down_votes = 0L
    shipBuilder_build_13.creation_date = datetime.datetime(2013, 9, 13, 14, 34, 19)
    shipBuilder_build_13.base_ship = False
    shipBuilder_build_13 = importer.save_or_locate(shipBuilder_build_13)

    shipBuilder_build_14 = Build()
    shipBuilder_build_14.created_by = auth_user_73
    shipBuilder_build_14.name = u'2'
    shipBuilder_build_14.role = u'Interdiction'
    shipBuilder_build_14.ship = shipBuilder_ship_2
    shipBuilder_build_14.manufacturer_variant = True
    shipBuilder_build_14.engine_intake = None
    shipBuilder_build_14.powerplant = None
    shipBuilder_build_14.main_thruster = None
    shipBuilder_build_14.shield = None
    shipBuilder_build_14.cargo_mod = None
    shipBuilder_build_14.up_votes = 0L
    shipBuilder_build_14.down_votes = 0L
    shipBuilder_build_14.creation_date = datetime.datetime(2013, 9, 13, 14, 34, 57)
    shipBuilder_build_14.base_ship = False
    shipBuilder_build_14 = importer.save_or_locate(shipBuilder_build_14)

    shipBuilder_build_15 = Build()
    shipBuilder_build_15.created_by = auth_user_75
    shipBuilder_build_15.name = u'Freelancer HVYCOM'
    shipBuilder_build_15.role = u'Interdiction'
    shipBuilder_build_15.ship = shipBuilder_ship_7
    shipBuilder_build_15.manufacturer_variant = True
    shipBuilder_build_15.engine_intake = None
    shipBuilder_build_15.powerplant = shipBuilder_item_3
    shipBuilder_build_15.main_thruster = shipBuilder_item_17
    shipBuilder_build_15.shield = shipBuilder_item_27
    shipBuilder_build_15.cargo_mod = None
    shipBuilder_build_15.up_votes = 0L
    shipBuilder_build_15.down_votes = 0L
    shipBuilder_build_15.creation_date = datetime.datetime(2013, 9, 13, 15, 13, 4)
    shipBuilder_build_15.base_ship = False
    shipBuilder_build_15 = importer.save_or_locate(shipBuilder_build_15)

    shipBuilder_build_16 = Build()
    shipBuilder_build_16.created_by = auth_user_77
    shipBuilder_build_16.name = u'350r Escort'
    shipBuilder_build_16.role = u'Escort'
    shipBuilder_build_16.ship = shipBuilder_ship_4
    shipBuilder_build_16.manufacturer_variant = True
    shipBuilder_build_16.engine_intake = None
    shipBuilder_build_16.powerplant = None
    shipBuilder_build_16.main_thruster = None
    shipBuilder_build_16.shield = None
    shipBuilder_build_16.cargo_mod = None
    shipBuilder_build_16.up_votes = 0L
    shipBuilder_build_16.down_votes = 0L
    shipBuilder_build_16.creation_date = datetime.datetime(2013, 9, 13, 15, 31, 46)
    shipBuilder_build_16.base_ship = False
    shipBuilder_build_16 = importer.save_or_locate(shipBuilder_build_16)

    shipBuilder_build_17 = Build()
    shipBuilder_build_17.created_by = auth_user_77
    shipBuilder_build_17.name = u'My Lancer'
    shipBuilder_build_17.role = u'Exploration'
    shipBuilder_build_17.ship = shipBuilder_ship_7
    shipBuilder_build_17.manufacturer_variant = True
    shipBuilder_build_17.engine_intake = None
    shipBuilder_build_17.powerplant = shipBuilder_item_3
    shipBuilder_build_17.main_thruster = shipBuilder_item_20
    shipBuilder_build_17.shield = shipBuilder_item_28
    shipBuilder_build_17.cargo_mod = None
    shipBuilder_build_17.up_votes = 0L
    shipBuilder_build_17.down_votes = 0L
    shipBuilder_build_17.creation_date = datetime.datetime(2013, 9, 13, 15, 41, 39)
    shipBuilder_build_17.base_ship = False
    shipBuilder_build_17 = importer.save_or_locate(shipBuilder_build_17)

    shipBuilder_build_18 = Build()
    shipBuilder_build_18.created_by = auth_user_78
    shipBuilder_build_18.name = u'Swordfish'
    shipBuilder_build_18.role = u'Bounty Hunting'
    shipBuilder_build_18.ship = shipBuilder_ship_6
    shipBuilder_build_18.manufacturer_variant = True
    shipBuilder_build_18.engine_intake = None
    shipBuilder_build_18.powerplant = shipBuilder_item_6
    shipBuilder_build_18.main_thruster = shipBuilder_item_24
    shipBuilder_build_18.shield = shipBuilder_item_27
    shipBuilder_build_18.cargo_mod = None
    shipBuilder_build_18.up_votes = 0L
    shipBuilder_build_18.down_votes = 0L
    shipBuilder_build_18.creation_date = datetime.datetime(2013, 9, 13, 16, 34, 25)
    shipBuilder_build_18.base_ship = False
    shipBuilder_build_18 = importer.save_or_locate(shipBuilder_build_18)

    shipBuilder_build_19 = Build()
    shipBuilder_build_19.created_by = auth_user_78
    shipBuilder_build_19.name = u'LX'
    shipBuilder_build_19.role = u'Exploration'
    shipBuilder_build_19.ship = shipBuilder_ship_2
    shipBuilder_build_19.manufacturer_variant = True
    shipBuilder_build_19.engine_intake = None
    shipBuilder_build_19.powerplant = shipBuilder_item_4
    shipBuilder_build_19.main_thruster = shipBuilder_item_18
    shipBuilder_build_19.shield = shipBuilder_item_30
    shipBuilder_build_19.cargo_mod = shipBuilder_item_32
    shipBuilder_build_19.up_votes = 0L
    shipBuilder_build_19.down_votes = 0L
    shipBuilder_build_19.creation_date = datetime.datetime(2013, 9, 13, 16, 42, 30)
    shipBuilder_build_19.base_ship = False
    shipBuilder_build_19 = importer.save_or_locate(shipBuilder_build_19)

    shipBuilder_build_20 = Build()
    shipBuilder_build_20.created_by = auth_user_84
    shipBuilder_build_20.name = u'300EC'
    shipBuilder_build_20.role = u'Escort'
    shipBuilder_build_20.ship = shipBuilder_ship_1
    shipBuilder_build_20.manufacturer_variant = True
    shipBuilder_build_20.engine_intake = None
    shipBuilder_build_20.powerplant = None
    shipBuilder_build_20.main_thruster = None
    shipBuilder_build_20.shield = None
    shipBuilder_build_20.cargo_mod = None
    shipBuilder_build_20.up_votes = 0L
    shipBuilder_build_20.down_votes = 0L
    shipBuilder_build_20.creation_date = datetime.datetime(2013, 9, 13, 23, 30, 52)
    shipBuilder_build_20.base_ship = False
    shipBuilder_build_20 = importer.save_or_locate(shipBuilder_build_20)

    shipBuilder_build_21 = Build()
    shipBuilder_build_21.created_by = auth_user_85
    shipBuilder_build_21.name = u'reaper'
    shipBuilder_build_21.role = u'Piracy'
    shipBuilder_build_21.ship = shipBuilder_ship_7
    shipBuilder_build_21.manufacturer_variant = True
    shipBuilder_build_21.engine_intake = None
    shipBuilder_build_21.powerplant = None
    shipBuilder_build_21.main_thruster = None
    shipBuilder_build_21.shield = None
    shipBuilder_build_21.cargo_mod = None
    shipBuilder_build_21.up_votes = 0L
    shipBuilder_build_21.down_votes = 0L
    shipBuilder_build_21.creation_date = datetime.datetime(2013, 9, 14, 0, 43, 12)
    shipBuilder_build_21.base_ship = False
    shipBuilder_build_21 = importer.save_or_locate(shipBuilder_build_21)

    shipBuilder_build_22 = Build()
    shipBuilder_build_22.created_by = auth_user_85
    shipBuilder_build_22.name = u'void exploration'
    shipBuilder_build_22.role = u'Exploration'
    shipBuilder_build_22.ship = shipBuilder_ship_3
    shipBuilder_build_22.manufacturer_variant = True
    shipBuilder_build_22.engine_intake = None
    shipBuilder_build_22.powerplant = None
    shipBuilder_build_22.main_thruster = None
    shipBuilder_build_22.shield = None
    shipBuilder_build_22.cargo_mod = None
    shipBuilder_build_22.up_votes = 0L
    shipBuilder_build_22.down_votes = 0L
    shipBuilder_build_22.creation_date = datetime.datetime(2013, 9, 14, 0, 44, 1)
    shipBuilder_build_22.base_ship = False
    shipBuilder_build_22 = importer.save_or_locate(shipBuilder_build_22)

    shipBuilder_build_23 = Build()
    shipBuilder_build_23.created_by = auth_user_86
    shipBuilder_build_23.name = u'325BA'
    shipBuilder_build_23.role = u'Interdiction'
    shipBuilder_build_23.ship = shipBuilder_ship_1
    shipBuilder_build_23.manufacturer_variant = True
    shipBuilder_build_23.engine_intake = None
    shipBuilder_build_23.powerplant = shipBuilder_item_6
    shipBuilder_build_23.main_thruster = shipBuilder_item_22
    shipBuilder_build_23.shield = shipBuilder_item_27
    shipBuilder_build_23.cargo_mod = shipBuilder_item_33
    shipBuilder_build_23.up_votes = 0L
    shipBuilder_build_23.down_votes = 0L
    shipBuilder_build_23.creation_date = datetime.datetime(2013, 9, 14, 1, 33, 30)
    shipBuilder_build_23.base_ship = False
    shipBuilder_build_23 = importer.save_or_locate(shipBuilder_build_23)

    shipBuilder_build_24 = Build()
    shipBuilder_build_24.created_by = auth_user_70
    shipBuilder_build_24.name = u'315p'
    shipBuilder_build_24.role = u'Exploration'
    shipBuilder_build_24.ship = shipBuilder_ship_1
    shipBuilder_build_24.manufacturer_variant = True
    shipBuilder_build_24.engine_intake = None
    shipBuilder_build_24.powerplant = shipBuilder_item_2
    shipBuilder_build_24.main_thruster = shipBuilder_item_20
    shipBuilder_build_24.shield = shipBuilder_item_30
    shipBuilder_build_24.cargo_mod = shipBuilder_item_32
    shipBuilder_build_24.up_votes = 0L
    shipBuilder_build_24.down_votes = 0L
    shipBuilder_build_24.creation_date = datetime.datetime(2013, 9, 14, 12, 48, 38)
    shipBuilder_build_24.base_ship = False
    shipBuilder_build_24 = importer.save_or_locate(shipBuilder_build_24)

    shipBuilder_build_25 = Build()
    shipBuilder_build_25.created_by = auth_user_97
    shipBuilder_build_25.name = u'Sicarus'
    shipBuilder_build_25.role = u'Bounty Hunting'
    shipBuilder_build_25.ship = shipBuilder_ship_7
    shipBuilder_build_25.manufacturer_variant = True
    shipBuilder_build_25.engine_intake = None
    shipBuilder_build_25.powerplant = None
    shipBuilder_build_25.main_thruster = None
    shipBuilder_build_25.shield = None
    shipBuilder_build_25.cargo_mod = None
    shipBuilder_build_25.up_votes = 0L
    shipBuilder_build_25.down_votes = 0L
    shipBuilder_build_25.creation_date = datetime.datetime(2013, 9, 15, 1, 11, 13)
    shipBuilder_build_25.base_ship = False
    shipBuilder_build_25 = importer.save_or_locate(shipBuilder_build_25)

    shipBuilder_build_26 = Build()
    shipBuilder_build_26.created_by = auth_user_101
    shipBuilder_build_26.name = u'Freccia di Hiigara'
    shipBuilder_build_26.role = u'Exploration'
    shipBuilder_build_26.ship = shipBuilder_ship_1
    shipBuilder_build_26.manufacturer_variant = True
    shipBuilder_build_26.engine_intake = None
    shipBuilder_build_26.powerplant = None
    shipBuilder_build_26.main_thruster = None
    shipBuilder_build_26.shield = None
    shipBuilder_build_26.cargo_mod = None
    shipBuilder_build_26.up_votes = 0L
    shipBuilder_build_26.down_votes = 0L
    shipBuilder_build_26.creation_date = datetime.datetime(2013, 9, 15, 10, 21, 22)
    shipBuilder_build_26.base_ship = False
    shipBuilder_build_26 = importer.save_or_locate(shipBuilder_build_26)

    shipBuilder_build_27 = Build()
    shipBuilder_build_27.created_by = auth_user_102
    shipBuilder_build_27.name = u'Explorer V1'
    shipBuilder_build_27.role = u'Exploration'
    shipBuilder_build_27.ship = shipBuilder_ship_7
    shipBuilder_build_27.manufacturer_variant = True
    shipBuilder_build_27.engine_intake = None
    shipBuilder_build_27.powerplant = None
    shipBuilder_build_27.main_thruster = None
    shipBuilder_build_27.shield = None
    shipBuilder_build_27.cargo_mod = None
    shipBuilder_build_27.up_votes = 0L
    shipBuilder_build_27.down_votes = 0L
    shipBuilder_build_27.creation_date = datetime.datetime(2013, 9, 15, 14, 17, 8)
    shipBuilder_build_27.base_ship = False
    shipBuilder_build_27 = importer.save_or_locate(shipBuilder_build_27)

    shipBuilder_build_28 = Build()
    shipBuilder_build_28.created_by = auth_user_103
    shipBuilder_build_28.name = u'Seeker'
    shipBuilder_build_28.role = u'Bounty Hunting'
    shipBuilder_build_28.ship = shipBuilder_ship_3
    shipBuilder_build_28.manufacturer_variant = True
    shipBuilder_build_28.engine_intake = None
    shipBuilder_build_28.powerplant = shipBuilder_item_12
    shipBuilder_build_28.main_thruster = shipBuilder_item_20
    shipBuilder_build_28.shield = shipBuilder_item_27
    shipBuilder_build_28.cargo_mod = shipBuilder_item_33
    shipBuilder_build_28.up_votes = 0L
    shipBuilder_build_28.down_votes = 0L
    shipBuilder_build_28.creation_date = datetime.datetime(2013, 9, 15, 14, 35, 46)
    shipBuilder_build_28.base_ship = False
    shipBuilder_build_28 = importer.save_or_locate(shipBuilder_build_28)

    shipBuilder_build_29 = Build()
    shipBuilder_build_29.created_by = auth_user_110
    shipBuilder_build_29.name = u'Pirate Freelancer'
    shipBuilder_build_29.role = u'Piracy'
    shipBuilder_build_29.ship = shipBuilder_ship_7
    shipBuilder_build_29.manufacturer_variant = True
    shipBuilder_build_29.engine_intake = None
    shipBuilder_build_29.powerplant = shipBuilder_item_3
    shipBuilder_build_29.main_thruster = shipBuilder_item_23
    shipBuilder_build_29.shield = shipBuilder_item_27
    shipBuilder_build_29.cargo_mod = None
    shipBuilder_build_29.up_votes = 0L
    shipBuilder_build_29.down_votes = 0L
    shipBuilder_build_29.creation_date = datetime.datetime(2013, 9, 15, 23, 50, 3)
    shipBuilder_build_29.base_ship = False
    shipBuilder_build_29 = importer.save_or_locate(shipBuilder_build_29)

    shipBuilder_build_30 = Build()
    shipBuilder_build_30.created_by = auth_user_39
    shipBuilder_build_30.name = u'v2'
    shipBuilder_build_30.role = u'Exploration'
    shipBuilder_build_30.ship = shipBuilder_ship_1
    shipBuilder_build_30.manufacturer_variant = True
    shipBuilder_build_30.engine_intake = None
    shipBuilder_build_30.powerplant = shipBuilder_item_5
    shipBuilder_build_30.main_thruster = shipBuilder_item_20
    shipBuilder_build_30.shield = shipBuilder_item_29
    shipBuilder_build_30.cargo_mod = None
    shipBuilder_build_30.up_votes = 0L
    shipBuilder_build_30.down_votes = 0L
    shipBuilder_build_30.creation_date = datetime.datetime(2013, 9, 16, 20, 11, 4)
    shipBuilder_build_30.base_ship = False
    shipBuilder_build_30 = importer.save_or_locate(shipBuilder_build_30)

    shipBuilder_build_31 = Build()
    shipBuilder_build_31.created_by = auth_user_116
    shipBuilder_build_31.name = u'Armed Merchant'
    shipBuilder_build_31.role = u'Transport'
    shipBuilder_build_31.ship = shipBuilder_ship_7
    shipBuilder_build_31.manufacturer_variant = True
    shipBuilder_build_31.engine_intake = None
    shipBuilder_build_31.powerplant = shipBuilder_item_3
    shipBuilder_build_31.main_thruster = shipBuilder_item_24
    shipBuilder_build_31.shield = shipBuilder_item_27
    shipBuilder_build_31.cargo_mod = shipBuilder_item_33
    shipBuilder_build_31.up_votes = 0L
    shipBuilder_build_31.down_votes = 0L
    shipBuilder_build_31.creation_date = datetime.datetime(2013, 9, 16, 21, 2, 49)
    shipBuilder_build_31.base_ship = False
    shipBuilder_build_31 = importer.save_or_locate(shipBuilder_build_31)

    shipBuilder_build_32 = Build()
    shipBuilder_build_32.created_by = auth_user_116
    shipBuilder_build_32.name = u'300A Escort/Retrieval'
    shipBuilder_build_32.role = u'Escort'
    shipBuilder_build_32.ship = shipBuilder_ship_1
    shipBuilder_build_32.manufacturer_variant = True
    shipBuilder_build_32.engine_intake = None
    shipBuilder_build_32.powerplant = shipBuilder_item_6
    shipBuilder_build_32.main_thruster = shipBuilder_item_22
    shipBuilder_build_32.shield = shipBuilder_item_27
    shipBuilder_build_32.cargo_mod = shipBuilder_item_33
    shipBuilder_build_32.up_votes = 0L
    shipBuilder_build_32.down_votes = 0L
    shipBuilder_build_32.creation_date = datetime.datetime(2013, 9, 16, 21, 5, 52)
    shipBuilder_build_32.base_ship = False
    shipBuilder_build_32 = importer.save_or_locate(shipBuilder_build_32)

    shipBuilder_build_33 = Build()
    shipBuilder_build_33.created_by = auth_user_118
    shipBuilder_build_33.name = u'The outlaw'
    shipBuilder_build_33.role = u'Exploration'
    shipBuilder_build_33.ship = shipBuilder_ship_6
    shipBuilder_build_33.manufacturer_variant = True
    shipBuilder_build_33.engine_intake = None
    shipBuilder_build_33.powerplant = shipBuilder_item_7
    shipBuilder_build_33.main_thruster = shipBuilder_item_20
    shipBuilder_build_33.shield = shipBuilder_item_31
    shipBuilder_build_33.cargo_mod = None
    shipBuilder_build_33.up_votes = 0L
    shipBuilder_build_33.down_votes = 0L
    shipBuilder_build_33.creation_date = datetime.datetime(2013, 9, 17, 5, 42, 1)
    shipBuilder_build_33.base_ship = False
    shipBuilder_build_33 = importer.save_or_locate(shipBuilder_build_33)

    shipBuilder_build_34 = Build()
    shipBuilder_build_34.created_by = auth_user_121
    shipBuilder_build_34.name = u'Shrike-1'
    shipBuilder_build_34.role = u'Interdiction'
    shipBuilder_build_34.ship = shipBuilder_ship_1
    shipBuilder_build_34.manufacturer_variant = True
    shipBuilder_build_34.engine_intake = None
    shipBuilder_build_34.powerplant = None
    shipBuilder_build_34.main_thruster = None
    shipBuilder_build_34.shield = None
    shipBuilder_build_34.cargo_mod = None
    shipBuilder_build_34.up_votes = 0L
    shipBuilder_build_34.down_votes = 0L
    shipBuilder_build_34.creation_date = datetime.datetime(2013, 9, 17, 18, 29, 24)
    shipBuilder_build_34.base_ship = False
    shipBuilder_build_34 = importer.save_or_locate(shipBuilder_build_34)

    shipBuilder_build_35 = Build()
    shipBuilder_build_35.created_by = auth_user_121
    shipBuilder_build_35.name = u'Shrike-2'
    shipBuilder_build_35.role = u'Racing'
    shipBuilder_build_35.ship = shipBuilder_ship_1
    shipBuilder_build_35.manufacturer_variant = True
    shipBuilder_build_35.engine_intake = None
    shipBuilder_build_35.powerplant = shipBuilder_item_5
    shipBuilder_build_35.main_thruster = shipBuilder_item_21
    shipBuilder_build_35.shield = shipBuilder_item_29
    shipBuilder_build_35.cargo_mod = shipBuilder_item_32
    shipBuilder_build_35.up_votes = 0L
    shipBuilder_build_35.down_votes = 0L
    shipBuilder_build_35.creation_date = datetime.datetime(2013, 9, 17, 18, 33, 51)
    shipBuilder_build_35.base_ship = False
    shipBuilder_build_35 = importer.save_or_locate(shipBuilder_build_35)

    shipBuilder_build_36 = Build()
    shipBuilder_build_36.created_by = auth_user_121
    shipBuilder_build_36.name = u'Shrike-3'
    shipBuilder_build_36.role = u'Transport'
    shipBuilder_build_36.ship = shipBuilder_ship_1
    shipBuilder_build_36.manufacturer_variant = True
    shipBuilder_build_36.engine_intake = None
    shipBuilder_build_36.powerplant = None
    shipBuilder_build_36.main_thruster = None
    shipBuilder_build_36.shield = None
    shipBuilder_build_36.cargo_mod = None
    shipBuilder_build_36.up_votes = 0L
    shipBuilder_build_36.down_votes = 0L
    shipBuilder_build_36.creation_date = datetime.datetime(2013, 9, 17, 18, 37, 11)
    shipBuilder_build_36.base_ship = False
    shipBuilder_build_36 = importer.save_or_locate(shipBuilder_build_36)

    shipBuilder_build_37 = Build()
    shipBuilder_build_37.created_by = auth_user_119
    shipBuilder_build_37.name = u'325A'
    shipBuilder_build_37.role = u'Interdiction'
    shipBuilder_build_37.ship = shipBuilder_ship_1
    shipBuilder_build_37.manufacturer_variant = True
    shipBuilder_build_37.engine_intake = None
    shipBuilder_build_37.powerplant = shipBuilder_item_6
    shipBuilder_build_37.main_thruster = shipBuilder_item_22
    shipBuilder_build_37.shield = shipBuilder_item_27
    shipBuilder_build_37.cargo_mod = shipBuilder_item_33
    shipBuilder_build_37.up_votes = 0L
    shipBuilder_build_37.down_votes = 0L
    shipBuilder_build_37.creation_date = datetime.datetime(2013, 9, 17, 19, 39, 15)
    shipBuilder_build_37.base_ship = False
    shipBuilder_build_37 = importer.save_or_locate(shipBuilder_build_37)

    shipBuilder_build_38 = Build()
    shipBuilder_build_38.created_by = auth_user_130
    shipBuilder_build_38.name = u'Freelancer J'
    shipBuilder_build_38.role = u'Transport'
    shipBuilder_build_38.ship = shipBuilder_ship_7
    shipBuilder_build_38.manufacturer_variant = True
    shipBuilder_build_38.engine_intake = None
    shipBuilder_build_38.powerplant = shipBuilder_item_13
    shipBuilder_build_38.main_thruster = shipBuilder_item_25
    shipBuilder_build_38.shield = shipBuilder_item_31
    shipBuilder_build_38.cargo_mod = shipBuilder_item_33
    shipBuilder_build_38.up_votes = 0L
    shipBuilder_build_38.down_votes = 0L
    shipBuilder_build_38.creation_date = datetime.datetime(2013, 9, 19, 14, 19, 51)
    shipBuilder_build_38.base_ship = False
    shipBuilder_build_38 = importer.save_or_locate(shipBuilder_build_38)

    shipBuilder_build_39 = Build()
    shipBuilder_build_39.created_by = auth_user_132
    shipBuilder_build_39.name = u'Wall'
    shipBuilder_build_39.role = u'Escort'
    shipBuilder_build_39.ship = shipBuilder_ship_3
    shipBuilder_build_39.manufacturer_variant = True
    shipBuilder_build_39.engine_intake = None
    shipBuilder_build_39.powerplant = shipBuilder_item_12
    shipBuilder_build_39.main_thruster = shipBuilder_item_24
    shipBuilder_build_39.shield = shipBuilder_item_27
    shipBuilder_build_39.cargo_mod = shipBuilder_item_33
    shipBuilder_build_39.up_votes = 0L
    shipBuilder_build_39.down_votes = 0L
    shipBuilder_build_39.creation_date = datetime.datetime(2013, 9, 19, 19, 2, 40)
    shipBuilder_build_39.base_ship = False
    shipBuilder_build_39 = importer.save_or_locate(shipBuilder_build_39)

    shipBuilder_build_40 = Build()
    shipBuilder_build_40.created_by = auth_user_132
    shipBuilder_build_40.name = u'Owned'
    shipBuilder_build_40.role = u'Bounty Hunting'
    shipBuilder_build_40.ship = shipBuilder_ship_3
    shipBuilder_build_40.manufacturer_variant = True
    shipBuilder_build_40.engine_intake = None
    shipBuilder_build_40.powerplant = shipBuilder_item_12
    shipBuilder_build_40.main_thruster = shipBuilder_item_24
    shipBuilder_build_40.shield = shipBuilder_item_27
    shipBuilder_build_40.cargo_mod = shipBuilder_item_33
    shipBuilder_build_40.up_votes = 0L
    shipBuilder_build_40.down_votes = 0L
    shipBuilder_build_40.creation_date = datetime.datetime(2013, 9, 19, 19, 4, 17)
    shipBuilder_build_40.base_ship = False
    shipBuilder_build_40 = importer.save_or_locate(shipBuilder_build_40)

    shipBuilder_build_41 = Build()
    shipBuilder_build_41.created_by = auth_user_133
    shipBuilder_build_41.name = u'Stock Constellation'
    shipBuilder_build_41.role = u'Transport'
    shipBuilder_build_41.ship = shipBuilder_ship_3
    shipBuilder_build_41.manufacturer_variant = True
    shipBuilder_build_41.engine_intake = None
    shipBuilder_build_41.powerplant = shipBuilder_item_12
    shipBuilder_build_41.main_thruster = shipBuilder_item_24
    shipBuilder_build_41.shield = shipBuilder_item_27
    shipBuilder_build_41.cargo_mod = shipBuilder_item_33
    shipBuilder_build_41.up_votes = 0L
    shipBuilder_build_41.down_votes = 0L
    shipBuilder_build_41.creation_date = datetime.datetime(2013, 9, 21, 5, 56, 39)
    shipBuilder_build_41.base_ship = False
    shipBuilder_build_41 = importer.save_or_locate(shipBuilder_build_41)

    #Processing model: BuildHardpoint

    from shipBuilder.models import BuildHardpoint

    shipBuilder_buildhardpoint_1 = BuildHardpoint()
    shipBuilder_buildhardpoint_1.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_1.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_1.item = None
    shipBuilder_buildhardpoint_1 = importer.save_or_locate(shipBuilder_buildhardpoint_1)

    shipBuilder_buildhardpoint_2 = BuildHardpoint()
    shipBuilder_buildhardpoint_2.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_2.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_2.item = None
    shipBuilder_buildhardpoint_2 = importer.save_or_locate(shipBuilder_buildhardpoint_2)

    shipBuilder_buildhardpoint_3 = BuildHardpoint()
    shipBuilder_buildhardpoint_3.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_3.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_3.item = None
    shipBuilder_buildhardpoint_3 = importer.save_or_locate(shipBuilder_buildhardpoint_3)

    shipBuilder_buildhardpoint_4 = BuildHardpoint()
    shipBuilder_buildhardpoint_4.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_4.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_4.item = None
    shipBuilder_buildhardpoint_4 = importer.save_or_locate(shipBuilder_buildhardpoint_4)

    shipBuilder_buildhardpoint_5 = BuildHardpoint()
    shipBuilder_buildhardpoint_5.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_5.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_5.item = None
    shipBuilder_buildhardpoint_5 = importer.save_or_locate(shipBuilder_buildhardpoint_5)

    shipBuilder_buildhardpoint_6 = BuildHardpoint()
    shipBuilder_buildhardpoint_6.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_6.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_6.item = None
    shipBuilder_buildhardpoint_6 = importer.save_or_locate(shipBuilder_buildhardpoint_6)

    shipBuilder_buildhardpoint_7 = BuildHardpoint()
    shipBuilder_buildhardpoint_7.build = shipBuilder_build_1
    shipBuilder_buildhardpoint_7.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_7.item = None
    shipBuilder_buildhardpoint_7 = importer.save_or_locate(shipBuilder_buildhardpoint_7)

    shipBuilder_buildhardpoint_8 = BuildHardpoint()
    shipBuilder_buildhardpoint_8.build = shipBuilder_build_2
    shipBuilder_buildhardpoint_8.hardpoint = shipBuilder_hardpoint_38
    shipBuilder_buildhardpoint_8.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_8 = importer.save_or_locate(shipBuilder_buildhardpoint_8)

    shipBuilder_buildhardpoint_9 = BuildHardpoint()
    shipBuilder_buildhardpoint_9.build = shipBuilder_build_2
    shipBuilder_buildhardpoint_9.hardpoint = shipBuilder_hardpoint_39
    shipBuilder_buildhardpoint_9.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_9 = importer.save_or_locate(shipBuilder_buildhardpoint_9)

    shipBuilder_buildhardpoint_10 = BuildHardpoint()
    shipBuilder_buildhardpoint_10.build = shipBuilder_build_2
    shipBuilder_buildhardpoint_10.hardpoint = shipBuilder_hardpoint_40
    shipBuilder_buildhardpoint_10.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_10 = importer.save_or_locate(shipBuilder_buildhardpoint_10)

    shipBuilder_buildhardpoint_11 = BuildHardpoint()
    shipBuilder_buildhardpoint_11.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_11.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_11.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_11 = importer.save_or_locate(shipBuilder_buildhardpoint_11)

    shipBuilder_buildhardpoint_12 = BuildHardpoint()
    shipBuilder_buildhardpoint_12.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_12.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_12.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_12 = importer.save_or_locate(shipBuilder_buildhardpoint_12)

    shipBuilder_buildhardpoint_13 = BuildHardpoint()
    shipBuilder_buildhardpoint_13.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_13.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_13.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_13 = importer.save_or_locate(shipBuilder_buildhardpoint_13)

    shipBuilder_buildhardpoint_14 = BuildHardpoint()
    shipBuilder_buildhardpoint_14.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_14.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_14.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_14 = importer.save_or_locate(shipBuilder_buildhardpoint_14)

    shipBuilder_buildhardpoint_15 = BuildHardpoint()
    shipBuilder_buildhardpoint_15.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_15.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_15.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_15 = importer.save_or_locate(shipBuilder_buildhardpoint_15)

    shipBuilder_buildhardpoint_16 = BuildHardpoint()
    shipBuilder_buildhardpoint_16.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_16.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_16.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_16 = importer.save_or_locate(shipBuilder_buildhardpoint_16)

    shipBuilder_buildhardpoint_17 = BuildHardpoint()
    shipBuilder_buildhardpoint_17.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_17.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_17.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_17 = importer.save_or_locate(shipBuilder_buildhardpoint_17)

    shipBuilder_buildhardpoint_18 = BuildHardpoint()
    shipBuilder_buildhardpoint_18.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_18.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_18.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_18 = importer.save_or_locate(shipBuilder_buildhardpoint_18)

    shipBuilder_buildhardpoint_19 = BuildHardpoint()
    shipBuilder_buildhardpoint_19.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_19.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_19.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_19 = importer.save_or_locate(shipBuilder_buildhardpoint_19)

    shipBuilder_buildhardpoint_20 = BuildHardpoint()
    shipBuilder_buildhardpoint_20.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_20.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_20.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_20 = importer.save_or_locate(shipBuilder_buildhardpoint_20)

    shipBuilder_buildhardpoint_21 = BuildHardpoint()
    shipBuilder_buildhardpoint_21.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_21.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_21.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_21 = importer.save_or_locate(shipBuilder_buildhardpoint_21)

    shipBuilder_buildhardpoint_22 = BuildHardpoint()
    shipBuilder_buildhardpoint_22.build = shipBuilder_build_3
    shipBuilder_buildhardpoint_22.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_22.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_22 = importer.save_or_locate(shipBuilder_buildhardpoint_22)

    shipBuilder_buildhardpoint_23 = BuildHardpoint()
    shipBuilder_buildhardpoint_23.build = shipBuilder_build_4
    shipBuilder_buildhardpoint_23.hardpoint = shipBuilder_hardpoint_38
    shipBuilder_buildhardpoint_23.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_23 = importer.save_or_locate(shipBuilder_buildhardpoint_23)

    shipBuilder_buildhardpoint_24 = BuildHardpoint()
    shipBuilder_buildhardpoint_24.build = shipBuilder_build_4
    shipBuilder_buildhardpoint_24.hardpoint = shipBuilder_hardpoint_39
    shipBuilder_buildhardpoint_24.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_24 = importer.save_or_locate(shipBuilder_buildhardpoint_24)

    shipBuilder_buildhardpoint_25 = BuildHardpoint()
    shipBuilder_buildhardpoint_25.build = shipBuilder_build_4
    shipBuilder_buildhardpoint_25.hardpoint = shipBuilder_hardpoint_40
    shipBuilder_buildhardpoint_25.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_25 = importer.save_or_locate(shipBuilder_buildhardpoint_25)

    shipBuilder_buildhardpoint_26 = BuildHardpoint()
    shipBuilder_buildhardpoint_26.build = shipBuilder_build_5
    shipBuilder_buildhardpoint_26.hardpoint = shipBuilder_hardpoint_26
    shipBuilder_buildhardpoint_26.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_26 = importer.save_or_locate(shipBuilder_buildhardpoint_26)

    shipBuilder_buildhardpoint_27 = BuildHardpoint()
    shipBuilder_buildhardpoint_27.build = shipBuilder_build_5
    shipBuilder_buildhardpoint_27.hardpoint = shipBuilder_hardpoint_27
    shipBuilder_buildhardpoint_27.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_27 = importer.save_or_locate(shipBuilder_buildhardpoint_27)

    shipBuilder_buildhardpoint_28 = BuildHardpoint()
    shipBuilder_buildhardpoint_28.build = shipBuilder_build_5
    shipBuilder_buildhardpoint_28.hardpoint = shipBuilder_hardpoint_28
    shipBuilder_buildhardpoint_28.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_28 = importer.save_or_locate(shipBuilder_buildhardpoint_28)

    shipBuilder_buildhardpoint_29 = BuildHardpoint()
    shipBuilder_buildhardpoint_29.build = shipBuilder_build_5
    shipBuilder_buildhardpoint_29.hardpoint = shipBuilder_hardpoint_29
    shipBuilder_buildhardpoint_29.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_29 = importer.save_or_locate(shipBuilder_buildhardpoint_29)

    shipBuilder_buildhardpoint_30 = BuildHardpoint()
    shipBuilder_buildhardpoint_30.build = shipBuilder_build_5
    shipBuilder_buildhardpoint_30.hardpoint = shipBuilder_hardpoint_30
    shipBuilder_buildhardpoint_30.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_30 = importer.save_or_locate(shipBuilder_buildhardpoint_30)

    shipBuilder_buildhardpoint_31 = BuildHardpoint()
    shipBuilder_buildhardpoint_31.build = shipBuilder_build_6
    shipBuilder_buildhardpoint_31.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_31.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_31 = importer.save_or_locate(shipBuilder_buildhardpoint_31)

    shipBuilder_buildhardpoint_32 = BuildHardpoint()
    shipBuilder_buildhardpoint_32.build = shipBuilder_build_6
    shipBuilder_buildhardpoint_32.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_32.item = None
    shipBuilder_buildhardpoint_32 = importer.save_or_locate(shipBuilder_buildhardpoint_32)

    shipBuilder_buildhardpoint_33 = BuildHardpoint()
    shipBuilder_buildhardpoint_33.build = shipBuilder_build_6
    shipBuilder_buildhardpoint_33.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_33.item = None
    shipBuilder_buildhardpoint_33 = importer.save_or_locate(shipBuilder_buildhardpoint_33)

    shipBuilder_buildhardpoint_34 = BuildHardpoint()
    shipBuilder_buildhardpoint_34.build = shipBuilder_build_6
    shipBuilder_buildhardpoint_34.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_34.item = shipBuilder_item_41
    shipBuilder_buildhardpoint_34 = importer.save_or_locate(shipBuilder_buildhardpoint_34)

    shipBuilder_buildhardpoint_35 = BuildHardpoint()
    shipBuilder_buildhardpoint_35.build = shipBuilder_build_6
    shipBuilder_buildhardpoint_35.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_35.item = shipBuilder_item_48
    shipBuilder_buildhardpoint_35 = importer.save_or_locate(shipBuilder_buildhardpoint_35)

    shipBuilder_buildhardpoint_36 = BuildHardpoint()
    shipBuilder_buildhardpoint_36.build = shipBuilder_build_7
    shipBuilder_buildhardpoint_36.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_36.item = None
    shipBuilder_buildhardpoint_36 = importer.save_or_locate(shipBuilder_buildhardpoint_36)

    shipBuilder_buildhardpoint_37 = BuildHardpoint()
    shipBuilder_buildhardpoint_37.build = shipBuilder_build_7
    shipBuilder_buildhardpoint_37.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_37.item = None
    shipBuilder_buildhardpoint_37 = importer.save_or_locate(shipBuilder_buildhardpoint_37)

    shipBuilder_buildhardpoint_38 = BuildHardpoint()
    shipBuilder_buildhardpoint_38.build = shipBuilder_build_7
    shipBuilder_buildhardpoint_38.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_38.item = None
    shipBuilder_buildhardpoint_38 = importer.save_or_locate(shipBuilder_buildhardpoint_38)

    shipBuilder_buildhardpoint_39 = BuildHardpoint()
    shipBuilder_buildhardpoint_39.build = shipBuilder_build_7
    shipBuilder_buildhardpoint_39.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_39.item = None
    shipBuilder_buildhardpoint_39 = importer.save_or_locate(shipBuilder_buildhardpoint_39)

    shipBuilder_buildhardpoint_40 = BuildHardpoint()
    shipBuilder_buildhardpoint_40.build = shipBuilder_build_7
    shipBuilder_buildhardpoint_40.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_40.item = None
    shipBuilder_buildhardpoint_40 = importer.save_or_locate(shipBuilder_buildhardpoint_40)

    shipBuilder_buildhardpoint_41 = BuildHardpoint()
    shipBuilder_buildhardpoint_41.build = shipBuilder_build_8
    shipBuilder_buildhardpoint_41.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_41.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_41 = importer.save_or_locate(shipBuilder_buildhardpoint_41)

    shipBuilder_buildhardpoint_42 = BuildHardpoint()
    shipBuilder_buildhardpoint_42.build = shipBuilder_build_8
    shipBuilder_buildhardpoint_42.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_42.item = shipBuilder_item_42
    shipBuilder_buildhardpoint_42 = importer.save_or_locate(shipBuilder_buildhardpoint_42)

    shipBuilder_buildhardpoint_43 = BuildHardpoint()
    shipBuilder_buildhardpoint_43.build = shipBuilder_build_8
    shipBuilder_buildhardpoint_43.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_43.item = shipBuilder_item_42
    shipBuilder_buildhardpoint_43 = importer.save_or_locate(shipBuilder_buildhardpoint_43)

    shipBuilder_buildhardpoint_44 = BuildHardpoint()
    shipBuilder_buildhardpoint_44.build = shipBuilder_build_8
    shipBuilder_buildhardpoint_44.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_44.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_44 = importer.save_or_locate(shipBuilder_buildhardpoint_44)

    shipBuilder_buildhardpoint_45 = BuildHardpoint()
    shipBuilder_buildhardpoint_45.build = shipBuilder_build_8
    shipBuilder_buildhardpoint_45.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_45.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_45 = importer.save_or_locate(shipBuilder_buildhardpoint_45)

    shipBuilder_buildhardpoint_46 = BuildHardpoint()
    shipBuilder_buildhardpoint_46.build = shipBuilder_build_9
    shipBuilder_buildhardpoint_46.hardpoint = shipBuilder_hardpoint_6
    shipBuilder_buildhardpoint_46.item = shipBuilder_item_40
    shipBuilder_buildhardpoint_46 = importer.save_or_locate(shipBuilder_buildhardpoint_46)

    shipBuilder_buildhardpoint_47 = BuildHardpoint()
    shipBuilder_buildhardpoint_47.build = shipBuilder_build_9
    shipBuilder_buildhardpoint_47.hardpoint = shipBuilder_hardpoint_7
    shipBuilder_buildhardpoint_47.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_47 = importer.save_or_locate(shipBuilder_buildhardpoint_47)

    shipBuilder_buildhardpoint_48 = BuildHardpoint()
    shipBuilder_buildhardpoint_48.build = shipBuilder_build_9
    shipBuilder_buildhardpoint_48.hardpoint = shipBuilder_hardpoint_8
    shipBuilder_buildhardpoint_48.item = shipBuilder_item_40
    shipBuilder_buildhardpoint_48 = importer.save_or_locate(shipBuilder_buildhardpoint_48)

    shipBuilder_buildhardpoint_49 = BuildHardpoint()
    shipBuilder_buildhardpoint_49.build = shipBuilder_build_10
    shipBuilder_buildhardpoint_49.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_49.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_49 = importer.save_or_locate(shipBuilder_buildhardpoint_49)

    shipBuilder_buildhardpoint_50 = BuildHardpoint()
    shipBuilder_buildhardpoint_50.build = shipBuilder_build_10
    shipBuilder_buildhardpoint_50.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_50.item = None
    shipBuilder_buildhardpoint_50 = importer.save_or_locate(shipBuilder_buildhardpoint_50)

    shipBuilder_buildhardpoint_51 = BuildHardpoint()
    shipBuilder_buildhardpoint_51.build = shipBuilder_build_10
    shipBuilder_buildhardpoint_51.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_51.item = None
    shipBuilder_buildhardpoint_51 = importer.save_or_locate(shipBuilder_buildhardpoint_51)

    shipBuilder_buildhardpoint_52 = BuildHardpoint()
    shipBuilder_buildhardpoint_52.build = shipBuilder_build_10
    shipBuilder_buildhardpoint_52.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_52.item = shipBuilder_item_41
    shipBuilder_buildhardpoint_52 = importer.save_or_locate(shipBuilder_buildhardpoint_52)

    shipBuilder_buildhardpoint_53 = BuildHardpoint()
    shipBuilder_buildhardpoint_53.build = shipBuilder_build_10
    shipBuilder_buildhardpoint_53.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_53.item = shipBuilder_item_48
    shipBuilder_buildhardpoint_53 = importer.save_or_locate(shipBuilder_buildhardpoint_53)

    shipBuilder_buildhardpoint_54 = BuildHardpoint()
    shipBuilder_buildhardpoint_54.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_54.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_54.item = None
    shipBuilder_buildhardpoint_54 = importer.save_or_locate(shipBuilder_buildhardpoint_54)

    shipBuilder_buildhardpoint_55 = BuildHardpoint()
    shipBuilder_buildhardpoint_55.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_55.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_55.item = None
    shipBuilder_buildhardpoint_55 = importer.save_or_locate(shipBuilder_buildhardpoint_55)

    shipBuilder_buildhardpoint_56 = BuildHardpoint()
    shipBuilder_buildhardpoint_56.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_56.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_56.item = None
    shipBuilder_buildhardpoint_56 = importer.save_or_locate(shipBuilder_buildhardpoint_56)

    shipBuilder_buildhardpoint_57 = BuildHardpoint()
    shipBuilder_buildhardpoint_57.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_57.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_57.item = None
    shipBuilder_buildhardpoint_57 = importer.save_or_locate(shipBuilder_buildhardpoint_57)

    shipBuilder_buildhardpoint_58 = BuildHardpoint()
    shipBuilder_buildhardpoint_58.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_58.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_58.item = None
    shipBuilder_buildhardpoint_58 = importer.save_or_locate(shipBuilder_buildhardpoint_58)

    shipBuilder_buildhardpoint_59 = BuildHardpoint()
    shipBuilder_buildhardpoint_59.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_59.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_59.item = None
    shipBuilder_buildhardpoint_59 = importer.save_or_locate(shipBuilder_buildhardpoint_59)

    shipBuilder_buildhardpoint_60 = BuildHardpoint()
    shipBuilder_buildhardpoint_60.build = shipBuilder_build_11
    shipBuilder_buildhardpoint_60.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_60.item = None
    shipBuilder_buildhardpoint_60 = importer.save_or_locate(shipBuilder_buildhardpoint_60)

    shipBuilder_buildhardpoint_61 = BuildHardpoint()
    shipBuilder_buildhardpoint_61.build = shipBuilder_build_12
    shipBuilder_buildhardpoint_61.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_61.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_61 = importer.save_or_locate(shipBuilder_buildhardpoint_61)

    shipBuilder_buildhardpoint_62 = BuildHardpoint()
    shipBuilder_buildhardpoint_62.build = shipBuilder_build_12
    shipBuilder_buildhardpoint_62.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_62.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_62 = importer.save_or_locate(shipBuilder_buildhardpoint_62)

    shipBuilder_buildhardpoint_63 = BuildHardpoint()
    shipBuilder_buildhardpoint_63.build = shipBuilder_build_12
    shipBuilder_buildhardpoint_63.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_63.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_63 = importer.save_or_locate(shipBuilder_buildhardpoint_63)

    shipBuilder_buildhardpoint_64 = BuildHardpoint()
    shipBuilder_buildhardpoint_64.build = shipBuilder_build_12
    shipBuilder_buildhardpoint_64.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_64.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_64 = importer.save_or_locate(shipBuilder_buildhardpoint_64)

    shipBuilder_buildhardpoint_65 = BuildHardpoint()
    shipBuilder_buildhardpoint_65.build = shipBuilder_build_12
    shipBuilder_buildhardpoint_65.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_65.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_65 = importer.save_or_locate(shipBuilder_buildhardpoint_65)

    shipBuilder_buildhardpoint_66 = BuildHardpoint()
    shipBuilder_buildhardpoint_66.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_66.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_66.item = None
    shipBuilder_buildhardpoint_66 = importer.save_or_locate(shipBuilder_buildhardpoint_66)

    shipBuilder_buildhardpoint_67 = BuildHardpoint()
    shipBuilder_buildhardpoint_67.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_67.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_67.item = None
    shipBuilder_buildhardpoint_67 = importer.save_or_locate(shipBuilder_buildhardpoint_67)

    shipBuilder_buildhardpoint_68 = BuildHardpoint()
    shipBuilder_buildhardpoint_68.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_68.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_68.item = None
    shipBuilder_buildhardpoint_68 = importer.save_or_locate(shipBuilder_buildhardpoint_68)

    shipBuilder_buildhardpoint_69 = BuildHardpoint()
    shipBuilder_buildhardpoint_69.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_69.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_69.item = None
    shipBuilder_buildhardpoint_69 = importer.save_or_locate(shipBuilder_buildhardpoint_69)

    shipBuilder_buildhardpoint_70 = BuildHardpoint()
    shipBuilder_buildhardpoint_70.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_70.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_70.item = None
    shipBuilder_buildhardpoint_70 = importer.save_or_locate(shipBuilder_buildhardpoint_70)

    shipBuilder_buildhardpoint_71 = BuildHardpoint()
    shipBuilder_buildhardpoint_71.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_71.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_71.item = None
    shipBuilder_buildhardpoint_71 = importer.save_or_locate(shipBuilder_buildhardpoint_71)

    shipBuilder_buildhardpoint_72 = BuildHardpoint()
    shipBuilder_buildhardpoint_72.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_72.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_72.item = None
    shipBuilder_buildhardpoint_72 = importer.save_or_locate(shipBuilder_buildhardpoint_72)

    shipBuilder_buildhardpoint_73 = BuildHardpoint()
    shipBuilder_buildhardpoint_73.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_73.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_73.item = None
    shipBuilder_buildhardpoint_73 = importer.save_or_locate(shipBuilder_buildhardpoint_73)

    shipBuilder_buildhardpoint_74 = BuildHardpoint()
    shipBuilder_buildhardpoint_74.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_74.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_74.item = None
    shipBuilder_buildhardpoint_74 = importer.save_or_locate(shipBuilder_buildhardpoint_74)

    shipBuilder_buildhardpoint_75 = BuildHardpoint()
    shipBuilder_buildhardpoint_75.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_75.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_75.item = None
    shipBuilder_buildhardpoint_75 = importer.save_or_locate(shipBuilder_buildhardpoint_75)

    shipBuilder_buildhardpoint_76 = BuildHardpoint()
    shipBuilder_buildhardpoint_76.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_76.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_76.item = None
    shipBuilder_buildhardpoint_76 = importer.save_or_locate(shipBuilder_buildhardpoint_76)

    shipBuilder_buildhardpoint_77 = BuildHardpoint()
    shipBuilder_buildhardpoint_77.build = shipBuilder_build_13
    shipBuilder_buildhardpoint_77.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_77.item = None
    shipBuilder_buildhardpoint_77 = importer.save_or_locate(shipBuilder_buildhardpoint_77)

    shipBuilder_buildhardpoint_78 = BuildHardpoint()
    shipBuilder_buildhardpoint_78.build = shipBuilder_build_14
    shipBuilder_buildhardpoint_78.hardpoint = shipBuilder_hardpoint_6
    shipBuilder_buildhardpoint_78.item = None
    shipBuilder_buildhardpoint_78 = importer.save_or_locate(shipBuilder_buildhardpoint_78)

    shipBuilder_buildhardpoint_79 = BuildHardpoint()
    shipBuilder_buildhardpoint_79.build = shipBuilder_build_14
    shipBuilder_buildhardpoint_79.hardpoint = shipBuilder_hardpoint_7
    shipBuilder_buildhardpoint_79.item = None
    shipBuilder_buildhardpoint_79 = importer.save_or_locate(shipBuilder_buildhardpoint_79)

    shipBuilder_buildhardpoint_80 = BuildHardpoint()
    shipBuilder_buildhardpoint_80.build = shipBuilder_build_14
    shipBuilder_buildhardpoint_80.hardpoint = shipBuilder_hardpoint_8
    shipBuilder_buildhardpoint_80.item = None
    shipBuilder_buildhardpoint_80 = importer.save_or_locate(shipBuilder_buildhardpoint_80)

    shipBuilder_buildhardpoint_81 = BuildHardpoint()
    shipBuilder_buildhardpoint_81.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_81.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_81.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_81 = importer.save_or_locate(shipBuilder_buildhardpoint_81)

    shipBuilder_buildhardpoint_82 = BuildHardpoint()
    shipBuilder_buildhardpoint_82.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_82.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_82.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_82 = importer.save_or_locate(shipBuilder_buildhardpoint_82)

    shipBuilder_buildhardpoint_83 = BuildHardpoint()
    shipBuilder_buildhardpoint_83.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_83.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_83.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_83 = importer.save_or_locate(shipBuilder_buildhardpoint_83)

    shipBuilder_buildhardpoint_84 = BuildHardpoint()
    shipBuilder_buildhardpoint_84.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_84.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_84.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_84 = importer.save_or_locate(shipBuilder_buildhardpoint_84)

    shipBuilder_buildhardpoint_85 = BuildHardpoint()
    shipBuilder_buildhardpoint_85.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_85.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_85.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_85 = importer.save_or_locate(shipBuilder_buildhardpoint_85)

    shipBuilder_buildhardpoint_86 = BuildHardpoint()
    shipBuilder_buildhardpoint_86.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_86.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_86.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_86 = importer.save_or_locate(shipBuilder_buildhardpoint_86)

    shipBuilder_buildhardpoint_87 = BuildHardpoint()
    shipBuilder_buildhardpoint_87.build = shipBuilder_build_15
    shipBuilder_buildhardpoint_87.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_87.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_87 = importer.save_or_locate(shipBuilder_buildhardpoint_87)

    shipBuilder_buildhardpoint_88 = BuildHardpoint()
    shipBuilder_buildhardpoint_88.build = shipBuilder_build_16
    shipBuilder_buildhardpoint_88.hardpoint = shipBuilder_hardpoint_15
    shipBuilder_buildhardpoint_88.item = None
    shipBuilder_buildhardpoint_88 = importer.save_or_locate(shipBuilder_buildhardpoint_88)

    shipBuilder_buildhardpoint_89 = BuildHardpoint()
    shipBuilder_buildhardpoint_89.build = shipBuilder_build_16
    shipBuilder_buildhardpoint_89.hardpoint = shipBuilder_hardpoint_16
    shipBuilder_buildhardpoint_89.item = None
    shipBuilder_buildhardpoint_89 = importer.save_or_locate(shipBuilder_buildhardpoint_89)

    shipBuilder_buildhardpoint_90 = BuildHardpoint()
    shipBuilder_buildhardpoint_90.build = shipBuilder_build_16
    shipBuilder_buildhardpoint_90.hardpoint = shipBuilder_hardpoint_17
    shipBuilder_buildhardpoint_90.item = None
    shipBuilder_buildhardpoint_90 = importer.save_or_locate(shipBuilder_buildhardpoint_90)

    shipBuilder_buildhardpoint_91 = BuildHardpoint()
    shipBuilder_buildhardpoint_91.build = shipBuilder_build_16
    shipBuilder_buildhardpoint_91.hardpoint = shipBuilder_hardpoint_18
    shipBuilder_buildhardpoint_91.item = None
    shipBuilder_buildhardpoint_91 = importer.save_or_locate(shipBuilder_buildhardpoint_91)

    shipBuilder_buildhardpoint_92 = BuildHardpoint()
    shipBuilder_buildhardpoint_92.build = shipBuilder_build_16
    shipBuilder_buildhardpoint_92.hardpoint = shipBuilder_hardpoint_19
    shipBuilder_buildhardpoint_92.item = None
    shipBuilder_buildhardpoint_92 = importer.save_or_locate(shipBuilder_buildhardpoint_92)

    shipBuilder_buildhardpoint_93 = BuildHardpoint()
    shipBuilder_buildhardpoint_93.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_93.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_93.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_93 = importer.save_or_locate(shipBuilder_buildhardpoint_93)

    shipBuilder_buildhardpoint_94 = BuildHardpoint()
    shipBuilder_buildhardpoint_94.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_94.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_94.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_94 = importer.save_or_locate(shipBuilder_buildhardpoint_94)

    shipBuilder_buildhardpoint_95 = BuildHardpoint()
    shipBuilder_buildhardpoint_95.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_95.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_95.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_95 = importer.save_or_locate(shipBuilder_buildhardpoint_95)

    shipBuilder_buildhardpoint_96 = BuildHardpoint()
    shipBuilder_buildhardpoint_96.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_96.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_96.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_96 = importer.save_or_locate(shipBuilder_buildhardpoint_96)

    shipBuilder_buildhardpoint_97 = BuildHardpoint()
    shipBuilder_buildhardpoint_97.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_97.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_97.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_97 = importer.save_or_locate(shipBuilder_buildhardpoint_97)

    shipBuilder_buildhardpoint_98 = BuildHardpoint()
    shipBuilder_buildhardpoint_98.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_98.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_98.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_98 = importer.save_or_locate(shipBuilder_buildhardpoint_98)

    shipBuilder_buildhardpoint_99 = BuildHardpoint()
    shipBuilder_buildhardpoint_99.build = shipBuilder_build_17
    shipBuilder_buildhardpoint_99.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_99.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_99 = importer.save_or_locate(shipBuilder_buildhardpoint_99)

    shipBuilder_buildhardpoint_100 = BuildHardpoint()
    shipBuilder_buildhardpoint_100.build = shipBuilder_build_18
    shipBuilder_buildhardpoint_100.hardpoint = shipBuilder_hardpoint_26
    shipBuilder_buildhardpoint_100.item = shipBuilder_item_48
    shipBuilder_buildhardpoint_100 = importer.save_or_locate(shipBuilder_buildhardpoint_100)

    shipBuilder_buildhardpoint_101 = BuildHardpoint()
    shipBuilder_buildhardpoint_101.build = shipBuilder_build_18
    shipBuilder_buildhardpoint_101.hardpoint = shipBuilder_hardpoint_27
    shipBuilder_buildhardpoint_101.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_101 = importer.save_or_locate(shipBuilder_buildhardpoint_101)

    shipBuilder_buildhardpoint_102 = BuildHardpoint()
    shipBuilder_buildhardpoint_102.build = shipBuilder_build_18
    shipBuilder_buildhardpoint_102.hardpoint = shipBuilder_hardpoint_28
    shipBuilder_buildhardpoint_102.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_102 = importer.save_or_locate(shipBuilder_buildhardpoint_102)

    shipBuilder_buildhardpoint_103 = BuildHardpoint()
    shipBuilder_buildhardpoint_103.build = shipBuilder_build_18
    shipBuilder_buildhardpoint_103.hardpoint = shipBuilder_hardpoint_29
    shipBuilder_buildhardpoint_103.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_103 = importer.save_or_locate(shipBuilder_buildhardpoint_103)

    shipBuilder_buildhardpoint_104 = BuildHardpoint()
    shipBuilder_buildhardpoint_104.build = shipBuilder_build_18
    shipBuilder_buildhardpoint_104.hardpoint = shipBuilder_hardpoint_30
    shipBuilder_buildhardpoint_104.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_104 = importer.save_or_locate(shipBuilder_buildhardpoint_104)

    shipBuilder_buildhardpoint_105 = BuildHardpoint()
    shipBuilder_buildhardpoint_105.build = shipBuilder_build_19
    shipBuilder_buildhardpoint_105.hardpoint = shipBuilder_hardpoint_6
    shipBuilder_buildhardpoint_105.item = shipBuilder_item_40
    shipBuilder_buildhardpoint_105 = importer.save_or_locate(shipBuilder_buildhardpoint_105)

    shipBuilder_buildhardpoint_106 = BuildHardpoint()
    shipBuilder_buildhardpoint_106.build = shipBuilder_build_19
    shipBuilder_buildhardpoint_106.hardpoint = shipBuilder_hardpoint_7
    shipBuilder_buildhardpoint_106.item = shipBuilder_item_42
    shipBuilder_buildhardpoint_106 = importer.save_or_locate(shipBuilder_buildhardpoint_106)

    shipBuilder_buildhardpoint_107 = BuildHardpoint()
    shipBuilder_buildhardpoint_107.build = shipBuilder_build_19
    shipBuilder_buildhardpoint_107.hardpoint = shipBuilder_hardpoint_8
    shipBuilder_buildhardpoint_107.item = shipBuilder_item_40
    shipBuilder_buildhardpoint_107 = importer.save_or_locate(shipBuilder_buildhardpoint_107)

    shipBuilder_buildhardpoint_108 = BuildHardpoint()
    shipBuilder_buildhardpoint_108.build = shipBuilder_build_20
    shipBuilder_buildhardpoint_108.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_108.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_108 = importer.save_or_locate(shipBuilder_buildhardpoint_108)

    shipBuilder_buildhardpoint_109 = BuildHardpoint()
    shipBuilder_buildhardpoint_109.build = shipBuilder_build_20
    shipBuilder_buildhardpoint_109.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_109.item = shipBuilder_item_53
    shipBuilder_buildhardpoint_109 = importer.save_or_locate(shipBuilder_buildhardpoint_109)

    shipBuilder_buildhardpoint_110 = BuildHardpoint()
    shipBuilder_buildhardpoint_110.build = shipBuilder_build_20
    shipBuilder_buildhardpoint_110.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_110.item = shipBuilder_item_53
    shipBuilder_buildhardpoint_110 = importer.save_or_locate(shipBuilder_buildhardpoint_110)

    shipBuilder_buildhardpoint_111 = BuildHardpoint()
    shipBuilder_buildhardpoint_111.build = shipBuilder_build_20
    shipBuilder_buildhardpoint_111.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_111.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_111 = importer.save_or_locate(shipBuilder_buildhardpoint_111)

    shipBuilder_buildhardpoint_112 = BuildHardpoint()
    shipBuilder_buildhardpoint_112.build = shipBuilder_build_20
    shipBuilder_buildhardpoint_112.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_112.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_112 = importer.save_or_locate(shipBuilder_buildhardpoint_112)

    shipBuilder_buildhardpoint_113 = BuildHardpoint()
    shipBuilder_buildhardpoint_113.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_113.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_113.item = None
    shipBuilder_buildhardpoint_113 = importer.save_or_locate(shipBuilder_buildhardpoint_113)

    shipBuilder_buildhardpoint_114 = BuildHardpoint()
    shipBuilder_buildhardpoint_114.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_114.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_114.item = None
    shipBuilder_buildhardpoint_114 = importer.save_or_locate(shipBuilder_buildhardpoint_114)

    shipBuilder_buildhardpoint_115 = BuildHardpoint()
    shipBuilder_buildhardpoint_115.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_115.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_115.item = None
    shipBuilder_buildhardpoint_115 = importer.save_or_locate(shipBuilder_buildhardpoint_115)

    shipBuilder_buildhardpoint_116 = BuildHardpoint()
    shipBuilder_buildhardpoint_116.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_116.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_116.item = None
    shipBuilder_buildhardpoint_116 = importer.save_or_locate(shipBuilder_buildhardpoint_116)

    shipBuilder_buildhardpoint_117 = BuildHardpoint()
    shipBuilder_buildhardpoint_117.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_117.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_117.item = None
    shipBuilder_buildhardpoint_117 = importer.save_or_locate(shipBuilder_buildhardpoint_117)

    shipBuilder_buildhardpoint_118 = BuildHardpoint()
    shipBuilder_buildhardpoint_118.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_118.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_118.item = None
    shipBuilder_buildhardpoint_118 = importer.save_or_locate(shipBuilder_buildhardpoint_118)

    shipBuilder_buildhardpoint_119 = BuildHardpoint()
    shipBuilder_buildhardpoint_119.build = shipBuilder_build_21
    shipBuilder_buildhardpoint_119.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_119.item = None
    shipBuilder_buildhardpoint_119 = importer.save_or_locate(shipBuilder_buildhardpoint_119)

    shipBuilder_buildhardpoint_120 = BuildHardpoint()
    shipBuilder_buildhardpoint_120.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_120.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_120.item = None
    shipBuilder_buildhardpoint_120 = importer.save_or_locate(shipBuilder_buildhardpoint_120)

    shipBuilder_buildhardpoint_121 = BuildHardpoint()
    shipBuilder_buildhardpoint_121.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_121.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_121.item = None
    shipBuilder_buildhardpoint_121 = importer.save_or_locate(shipBuilder_buildhardpoint_121)

    shipBuilder_buildhardpoint_122 = BuildHardpoint()
    shipBuilder_buildhardpoint_122.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_122.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_122.item = None
    shipBuilder_buildhardpoint_122 = importer.save_or_locate(shipBuilder_buildhardpoint_122)

    shipBuilder_buildhardpoint_123 = BuildHardpoint()
    shipBuilder_buildhardpoint_123.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_123.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_123.item = None
    shipBuilder_buildhardpoint_123 = importer.save_or_locate(shipBuilder_buildhardpoint_123)

    shipBuilder_buildhardpoint_124 = BuildHardpoint()
    shipBuilder_buildhardpoint_124.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_124.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_124.item = None
    shipBuilder_buildhardpoint_124 = importer.save_or_locate(shipBuilder_buildhardpoint_124)

    shipBuilder_buildhardpoint_125 = BuildHardpoint()
    shipBuilder_buildhardpoint_125.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_125.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_125.item = None
    shipBuilder_buildhardpoint_125 = importer.save_or_locate(shipBuilder_buildhardpoint_125)

    shipBuilder_buildhardpoint_126 = BuildHardpoint()
    shipBuilder_buildhardpoint_126.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_126.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_126.item = None
    shipBuilder_buildhardpoint_126 = importer.save_or_locate(shipBuilder_buildhardpoint_126)

    shipBuilder_buildhardpoint_127 = BuildHardpoint()
    shipBuilder_buildhardpoint_127.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_127.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_127.item = None
    shipBuilder_buildhardpoint_127 = importer.save_or_locate(shipBuilder_buildhardpoint_127)

    shipBuilder_buildhardpoint_128 = BuildHardpoint()
    shipBuilder_buildhardpoint_128.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_128.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_128.item = None
    shipBuilder_buildhardpoint_128 = importer.save_or_locate(shipBuilder_buildhardpoint_128)

    shipBuilder_buildhardpoint_129 = BuildHardpoint()
    shipBuilder_buildhardpoint_129.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_129.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_129.item = None
    shipBuilder_buildhardpoint_129 = importer.save_or_locate(shipBuilder_buildhardpoint_129)

    shipBuilder_buildhardpoint_130 = BuildHardpoint()
    shipBuilder_buildhardpoint_130.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_130.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_130.item = None
    shipBuilder_buildhardpoint_130 = importer.save_or_locate(shipBuilder_buildhardpoint_130)

    shipBuilder_buildhardpoint_131 = BuildHardpoint()
    shipBuilder_buildhardpoint_131.build = shipBuilder_build_22
    shipBuilder_buildhardpoint_131.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_131.item = None
    shipBuilder_buildhardpoint_131 = importer.save_or_locate(shipBuilder_buildhardpoint_131)

    shipBuilder_buildhardpoint_132 = BuildHardpoint()
    shipBuilder_buildhardpoint_132.build = shipBuilder_build_23
    shipBuilder_buildhardpoint_132.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_132.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_132 = importer.save_or_locate(shipBuilder_buildhardpoint_132)

    shipBuilder_buildhardpoint_133 = BuildHardpoint()
    shipBuilder_buildhardpoint_133.build = shipBuilder_build_23
    shipBuilder_buildhardpoint_133.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_133.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_133 = importer.save_or_locate(shipBuilder_buildhardpoint_133)

    shipBuilder_buildhardpoint_134 = BuildHardpoint()
    shipBuilder_buildhardpoint_134.build = shipBuilder_build_23
    shipBuilder_buildhardpoint_134.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_134.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_134 = importer.save_or_locate(shipBuilder_buildhardpoint_134)

    shipBuilder_buildhardpoint_135 = BuildHardpoint()
    shipBuilder_buildhardpoint_135.build = shipBuilder_build_23
    shipBuilder_buildhardpoint_135.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_135.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_135 = importer.save_or_locate(shipBuilder_buildhardpoint_135)

    shipBuilder_buildhardpoint_136 = BuildHardpoint()
    shipBuilder_buildhardpoint_136.build = shipBuilder_build_23
    shipBuilder_buildhardpoint_136.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_136.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_136 = importer.save_or_locate(shipBuilder_buildhardpoint_136)

    shipBuilder_buildhardpoint_137 = BuildHardpoint()
    shipBuilder_buildhardpoint_137.build = shipBuilder_build_24
    shipBuilder_buildhardpoint_137.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_137.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_137 = importer.save_or_locate(shipBuilder_buildhardpoint_137)

    shipBuilder_buildhardpoint_138 = BuildHardpoint()
    shipBuilder_buildhardpoint_138.build = shipBuilder_build_24
    shipBuilder_buildhardpoint_138.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_138.item = shipBuilder_item_42
    shipBuilder_buildhardpoint_138 = importer.save_or_locate(shipBuilder_buildhardpoint_138)

    shipBuilder_buildhardpoint_139 = BuildHardpoint()
    shipBuilder_buildhardpoint_139.build = shipBuilder_build_24
    shipBuilder_buildhardpoint_139.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_139.item = shipBuilder_item_42
    shipBuilder_buildhardpoint_139 = importer.save_or_locate(shipBuilder_buildhardpoint_139)

    shipBuilder_buildhardpoint_140 = BuildHardpoint()
    shipBuilder_buildhardpoint_140.build = shipBuilder_build_24
    shipBuilder_buildhardpoint_140.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_140.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_140 = importer.save_or_locate(shipBuilder_buildhardpoint_140)

    shipBuilder_buildhardpoint_141 = BuildHardpoint()
    shipBuilder_buildhardpoint_141.build = shipBuilder_build_24
    shipBuilder_buildhardpoint_141.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_141.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_141 = importer.save_or_locate(shipBuilder_buildhardpoint_141)

    shipBuilder_buildhardpoint_142 = BuildHardpoint()
    shipBuilder_buildhardpoint_142.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_142.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_142.item = None
    shipBuilder_buildhardpoint_142 = importer.save_or_locate(shipBuilder_buildhardpoint_142)

    shipBuilder_buildhardpoint_143 = BuildHardpoint()
    shipBuilder_buildhardpoint_143.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_143.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_143.item = None
    shipBuilder_buildhardpoint_143 = importer.save_or_locate(shipBuilder_buildhardpoint_143)

    shipBuilder_buildhardpoint_144 = BuildHardpoint()
    shipBuilder_buildhardpoint_144.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_144.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_144.item = None
    shipBuilder_buildhardpoint_144 = importer.save_or_locate(shipBuilder_buildhardpoint_144)

    shipBuilder_buildhardpoint_145 = BuildHardpoint()
    shipBuilder_buildhardpoint_145.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_145.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_145.item = None
    shipBuilder_buildhardpoint_145 = importer.save_or_locate(shipBuilder_buildhardpoint_145)

    shipBuilder_buildhardpoint_146 = BuildHardpoint()
    shipBuilder_buildhardpoint_146.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_146.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_146.item = None
    shipBuilder_buildhardpoint_146 = importer.save_or_locate(shipBuilder_buildhardpoint_146)

    shipBuilder_buildhardpoint_147 = BuildHardpoint()
    shipBuilder_buildhardpoint_147.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_147.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_147.item = None
    shipBuilder_buildhardpoint_147 = importer.save_or_locate(shipBuilder_buildhardpoint_147)

    shipBuilder_buildhardpoint_148 = BuildHardpoint()
    shipBuilder_buildhardpoint_148.build = shipBuilder_build_25
    shipBuilder_buildhardpoint_148.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_148.item = None
    shipBuilder_buildhardpoint_148 = importer.save_or_locate(shipBuilder_buildhardpoint_148)

    shipBuilder_buildhardpoint_149 = BuildHardpoint()
    shipBuilder_buildhardpoint_149.build = shipBuilder_build_26
    shipBuilder_buildhardpoint_149.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_149.item = None
    shipBuilder_buildhardpoint_149 = importer.save_or_locate(shipBuilder_buildhardpoint_149)

    shipBuilder_buildhardpoint_150 = BuildHardpoint()
    shipBuilder_buildhardpoint_150.build = shipBuilder_build_26
    shipBuilder_buildhardpoint_150.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_150.item = None
    shipBuilder_buildhardpoint_150 = importer.save_or_locate(shipBuilder_buildhardpoint_150)

    shipBuilder_buildhardpoint_151 = BuildHardpoint()
    shipBuilder_buildhardpoint_151.build = shipBuilder_build_26
    shipBuilder_buildhardpoint_151.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_151.item = None
    shipBuilder_buildhardpoint_151 = importer.save_or_locate(shipBuilder_buildhardpoint_151)

    shipBuilder_buildhardpoint_152 = BuildHardpoint()
    shipBuilder_buildhardpoint_152.build = shipBuilder_build_26
    shipBuilder_buildhardpoint_152.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_152.item = None
    shipBuilder_buildhardpoint_152 = importer.save_or_locate(shipBuilder_buildhardpoint_152)

    shipBuilder_buildhardpoint_153 = BuildHardpoint()
    shipBuilder_buildhardpoint_153.build = shipBuilder_build_26
    shipBuilder_buildhardpoint_153.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_153.item = None
    shipBuilder_buildhardpoint_153 = importer.save_or_locate(shipBuilder_buildhardpoint_153)

    shipBuilder_buildhardpoint_154 = BuildHardpoint()
    shipBuilder_buildhardpoint_154.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_154.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_154.item = None
    shipBuilder_buildhardpoint_154 = importer.save_or_locate(shipBuilder_buildhardpoint_154)

    shipBuilder_buildhardpoint_155 = BuildHardpoint()
    shipBuilder_buildhardpoint_155.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_155.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_155.item = None
    shipBuilder_buildhardpoint_155 = importer.save_or_locate(shipBuilder_buildhardpoint_155)

    shipBuilder_buildhardpoint_156 = BuildHardpoint()
    shipBuilder_buildhardpoint_156.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_156.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_156.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_156 = importer.save_or_locate(shipBuilder_buildhardpoint_156)

    shipBuilder_buildhardpoint_157 = BuildHardpoint()
    shipBuilder_buildhardpoint_157.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_157.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_157.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_157 = importer.save_or_locate(shipBuilder_buildhardpoint_157)

    shipBuilder_buildhardpoint_158 = BuildHardpoint()
    shipBuilder_buildhardpoint_158.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_158.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_158.item = shipBuilder_item_39
    shipBuilder_buildhardpoint_158 = importer.save_or_locate(shipBuilder_buildhardpoint_158)

    shipBuilder_buildhardpoint_159 = BuildHardpoint()
    shipBuilder_buildhardpoint_159.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_159.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_159.item = None
    shipBuilder_buildhardpoint_159 = importer.save_or_locate(shipBuilder_buildhardpoint_159)

    shipBuilder_buildhardpoint_160 = BuildHardpoint()
    shipBuilder_buildhardpoint_160.build = shipBuilder_build_27
    shipBuilder_buildhardpoint_160.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_160.item = shipBuilder_item_47
    shipBuilder_buildhardpoint_160 = importer.save_or_locate(shipBuilder_buildhardpoint_160)

    shipBuilder_buildhardpoint_161 = BuildHardpoint()
    shipBuilder_buildhardpoint_161.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_161.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_161.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_161 = importer.save_or_locate(shipBuilder_buildhardpoint_161)

    shipBuilder_buildhardpoint_162 = BuildHardpoint()
    shipBuilder_buildhardpoint_162.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_162.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_162.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_162 = importer.save_or_locate(shipBuilder_buildhardpoint_162)

    shipBuilder_buildhardpoint_163 = BuildHardpoint()
    shipBuilder_buildhardpoint_163.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_163.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_163.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_163 = importer.save_or_locate(shipBuilder_buildhardpoint_163)

    shipBuilder_buildhardpoint_164 = BuildHardpoint()
    shipBuilder_buildhardpoint_164.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_164.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_164.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_164 = importer.save_or_locate(shipBuilder_buildhardpoint_164)

    shipBuilder_buildhardpoint_165 = BuildHardpoint()
    shipBuilder_buildhardpoint_165.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_165.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_165.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_165 = importer.save_or_locate(shipBuilder_buildhardpoint_165)

    shipBuilder_buildhardpoint_166 = BuildHardpoint()
    shipBuilder_buildhardpoint_166.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_166.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_166.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_166 = importer.save_or_locate(shipBuilder_buildhardpoint_166)

    shipBuilder_buildhardpoint_167 = BuildHardpoint()
    shipBuilder_buildhardpoint_167.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_167.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_167.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_167 = importer.save_or_locate(shipBuilder_buildhardpoint_167)

    shipBuilder_buildhardpoint_168 = BuildHardpoint()
    shipBuilder_buildhardpoint_168.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_168.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_168.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_168 = importer.save_or_locate(shipBuilder_buildhardpoint_168)

    shipBuilder_buildhardpoint_169 = BuildHardpoint()
    shipBuilder_buildhardpoint_169.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_169.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_169.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_169 = importer.save_or_locate(shipBuilder_buildhardpoint_169)

    shipBuilder_buildhardpoint_170 = BuildHardpoint()
    shipBuilder_buildhardpoint_170.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_170.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_170.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_170 = importer.save_or_locate(shipBuilder_buildhardpoint_170)

    shipBuilder_buildhardpoint_171 = BuildHardpoint()
    shipBuilder_buildhardpoint_171.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_171.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_171.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_171 = importer.save_or_locate(shipBuilder_buildhardpoint_171)

    shipBuilder_buildhardpoint_172 = BuildHardpoint()
    shipBuilder_buildhardpoint_172.build = shipBuilder_build_28
    shipBuilder_buildhardpoint_172.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_172.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_172 = importer.save_or_locate(shipBuilder_buildhardpoint_172)

    shipBuilder_buildhardpoint_173 = BuildHardpoint()
    shipBuilder_buildhardpoint_173.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_173.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_173.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_173 = importer.save_or_locate(shipBuilder_buildhardpoint_173)

    shipBuilder_buildhardpoint_174 = BuildHardpoint()
    shipBuilder_buildhardpoint_174.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_174.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_174.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_174 = importer.save_or_locate(shipBuilder_buildhardpoint_174)

    shipBuilder_buildhardpoint_175 = BuildHardpoint()
    shipBuilder_buildhardpoint_175.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_175.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_175.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_175 = importer.save_or_locate(shipBuilder_buildhardpoint_175)

    shipBuilder_buildhardpoint_176 = BuildHardpoint()
    shipBuilder_buildhardpoint_176.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_176.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_176.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_176 = importer.save_or_locate(shipBuilder_buildhardpoint_176)

    shipBuilder_buildhardpoint_177 = BuildHardpoint()
    shipBuilder_buildhardpoint_177.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_177.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_177.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_177 = importer.save_or_locate(shipBuilder_buildhardpoint_177)

    shipBuilder_buildhardpoint_178 = BuildHardpoint()
    shipBuilder_buildhardpoint_178.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_178.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_178.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_178 = importer.save_or_locate(shipBuilder_buildhardpoint_178)

    shipBuilder_buildhardpoint_179 = BuildHardpoint()
    shipBuilder_buildhardpoint_179.build = shipBuilder_build_29
    shipBuilder_buildhardpoint_179.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_179.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_179 = importer.save_or_locate(shipBuilder_buildhardpoint_179)

    shipBuilder_buildhardpoint_180 = BuildHardpoint()
    shipBuilder_buildhardpoint_180.build = shipBuilder_build_30
    shipBuilder_buildhardpoint_180.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_180.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_180 = importer.save_or_locate(shipBuilder_buildhardpoint_180)

    shipBuilder_buildhardpoint_181 = BuildHardpoint()
    shipBuilder_buildhardpoint_181.build = shipBuilder_build_30
    shipBuilder_buildhardpoint_181.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_181.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_181 = importer.save_or_locate(shipBuilder_buildhardpoint_181)

    shipBuilder_buildhardpoint_182 = BuildHardpoint()
    shipBuilder_buildhardpoint_182.build = shipBuilder_build_30
    shipBuilder_buildhardpoint_182.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_182.item = None
    shipBuilder_buildhardpoint_182 = importer.save_or_locate(shipBuilder_buildhardpoint_182)

    shipBuilder_buildhardpoint_183 = BuildHardpoint()
    shipBuilder_buildhardpoint_183.build = shipBuilder_build_30
    shipBuilder_buildhardpoint_183.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_183.item = shipBuilder_item_41
    shipBuilder_buildhardpoint_183 = importer.save_or_locate(shipBuilder_buildhardpoint_183)

    shipBuilder_buildhardpoint_184 = BuildHardpoint()
    shipBuilder_buildhardpoint_184.build = shipBuilder_build_30
    shipBuilder_buildhardpoint_184.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_184.item = shipBuilder_item_41
    shipBuilder_buildhardpoint_184 = importer.save_or_locate(shipBuilder_buildhardpoint_184)

    shipBuilder_buildhardpoint_185 = BuildHardpoint()
    shipBuilder_buildhardpoint_185.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_185.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_185.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_185 = importer.save_or_locate(shipBuilder_buildhardpoint_185)

    shipBuilder_buildhardpoint_186 = BuildHardpoint()
    shipBuilder_buildhardpoint_186.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_186.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_186.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_186 = importer.save_or_locate(shipBuilder_buildhardpoint_186)

    shipBuilder_buildhardpoint_187 = BuildHardpoint()
    shipBuilder_buildhardpoint_187.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_187.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_187.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_187 = importer.save_or_locate(shipBuilder_buildhardpoint_187)

    shipBuilder_buildhardpoint_188 = BuildHardpoint()
    shipBuilder_buildhardpoint_188.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_188.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_188.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_188 = importer.save_or_locate(shipBuilder_buildhardpoint_188)

    shipBuilder_buildhardpoint_189 = BuildHardpoint()
    shipBuilder_buildhardpoint_189.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_189.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_189.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_189 = importer.save_or_locate(shipBuilder_buildhardpoint_189)

    shipBuilder_buildhardpoint_190 = BuildHardpoint()
    shipBuilder_buildhardpoint_190.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_190.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_190.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_190 = importer.save_or_locate(shipBuilder_buildhardpoint_190)

    shipBuilder_buildhardpoint_191 = BuildHardpoint()
    shipBuilder_buildhardpoint_191.build = shipBuilder_build_31
    shipBuilder_buildhardpoint_191.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_191.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_191 = importer.save_or_locate(shipBuilder_buildhardpoint_191)

    shipBuilder_buildhardpoint_192 = BuildHardpoint()
    shipBuilder_buildhardpoint_192.build = shipBuilder_build_32
    shipBuilder_buildhardpoint_192.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_192.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_192 = importer.save_or_locate(shipBuilder_buildhardpoint_192)

    shipBuilder_buildhardpoint_193 = BuildHardpoint()
    shipBuilder_buildhardpoint_193.build = shipBuilder_build_32
    shipBuilder_buildhardpoint_193.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_193.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_193 = importer.save_or_locate(shipBuilder_buildhardpoint_193)

    shipBuilder_buildhardpoint_194 = BuildHardpoint()
    shipBuilder_buildhardpoint_194.build = shipBuilder_build_32
    shipBuilder_buildhardpoint_194.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_194.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_194 = importer.save_or_locate(shipBuilder_buildhardpoint_194)

    shipBuilder_buildhardpoint_195 = BuildHardpoint()
    shipBuilder_buildhardpoint_195.build = shipBuilder_build_32
    shipBuilder_buildhardpoint_195.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_195.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_195 = importer.save_or_locate(shipBuilder_buildhardpoint_195)

    shipBuilder_buildhardpoint_196 = BuildHardpoint()
    shipBuilder_buildhardpoint_196.build = shipBuilder_build_32
    shipBuilder_buildhardpoint_196.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_196.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_196 = importer.save_or_locate(shipBuilder_buildhardpoint_196)

    shipBuilder_buildhardpoint_197 = BuildHardpoint()
    shipBuilder_buildhardpoint_197.build = shipBuilder_build_33
    shipBuilder_buildhardpoint_197.hardpoint = shipBuilder_hardpoint_26
    shipBuilder_buildhardpoint_197.item = shipBuilder_item_39
    shipBuilder_buildhardpoint_197 = importer.save_or_locate(shipBuilder_buildhardpoint_197)

    shipBuilder_buildhardpoint_198 = BuildHardpoint()
    shipBuilder_buildhardpoint_198.build = shipBuilder_build_33
    shipBuilder_buildhardpoint_198.hardpoint = shipBuilder_hardpoint_27
    shipBuilder_buildhardpoint_198.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_198 = importer.save_or_locate(shipBuilder_buildhardpoint_198)

    shipBuilder_buildhardpoint_199 = BuildHardpoint()
    shipBuilder_buildhardpoint_199.build = shipBuilder_build_33
    shipBuilder_buildhardpoint_199.hardpoint = shipBuilder_hardpoint_28
    shipBuilder_buildhardpoint_199.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_199 = importer.save_or_locate(shipBuilder_buildhardpoint_199)

    shipBuilder_buildhardpoint_200 = BuildHardpoint()
    shipBuilder_buildhardpoint_200.build = shipBuilder_build_33
    shipBuilder_buildhardpoint_200.hardpoint = shipBuilder_hardpoint_29
    shipBuilder_buildhardpoint_200.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_200 = importer.save_or_locate(shipBuilder_buildhardpoint_200)

    shipBuilder_buildhardpoint_201 = BuildHardpoint()
    shipBuilder_buildhardpoint_201.build = shipBuilder_build_33
    shipBuilder_buildhardpoint_201.hardpoint = shipBuilder_hardpoint_30
    shipBuilder_buildhardpoint_201.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_201 = importer.save_or_locate(shipBuilder_buildhardpoint_201)

    shipBuilder_buildhardpoint_202 = BuildHardpoint()
    shipBuilder_buildhardpoint_202.build = shipBuilder_build_34
    shipBuilder_buildhardpoint_202.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_202.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_202 = importer.save_or_locate(shipBuilder_buildhardpoint_202)

    shipBuilder_buildhardpoint_203 = BuildHardpoint()
    shipBuilder_buildhardpoint_203.build = shipBuilder_build_34
    shipBuilder_buildhardpoint_203.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_203.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_203 = importer.save_or_locate(shipBuilder_buildhardpoint_203)

    shipBuilder_buildhardpoint_204 = BuildHardpoint()
    shipBuilder_buildhardpoint_204.build = shipBuilder_build_34
    shipBuilder_buildhardpoint_204.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_204.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_204 = importer.save_or_locate(shipBuilder_buildhardpoint_204)

    shipBuilder_buildhardpoint_205 = BuildHardpoint()
    shipBuilder_buildhardpoint_205.build = shipBuilder_build_34
    shipBuilder_buildhardpoint_205.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_205.item = None
    shipBuilder_buildhardpoint_205 = importer.save_or_locate(shipBuilder_buildhardpoint_205)

    shipBuilder_buildhardpoint_206 = BuildHardpoint()
    shipBuilder_buildhardpoint_206.build = shipBuilder_build_34
    shipBuilder_buildhardpoint_206.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_206.item = None
    shipBuilder_buildhardpoint_206 = importer.save_or_locate(shipBuilder_buildhardpoint_206)

    shipBuilder_buildhardpoint_207 = BuildHardpoint()
    shipBuilder_buildhardpoint_207.build = shipBuilder_build_35
    shipBuilder_buildhardpoint_207.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_207.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_207 = importer.save_or_locate(shipBuilder_buildhardpoint_207)

    shipBuilder_buildhardpoint_208 = BuildHardpoint()
    shipBuilder_buildhardpoint_208.build = shipBuilder_build_35
    shipBuilder_buildhardpoint_208.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_208.item = shipBuilder_item_50
    shipBuilder_buildhardpoint_208 = importer.save_or_locate(shipBuilder_buildhardpoint_208)

    shipBuilder_buildhardpoint_209 = BuildHardpoint()
    shipBuilder_buildhardpoint_209.build = shipBuilder_build_35
    shipBuilder_buildhardpoint_209.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_209.item = shipBuilder_item_44
    shipBuilder_buildhardpoint_209 = importer.save_or_locate(shipBuilder_buildhardpoint_209)

    shipBuilder_buildhardpoint_210 = BuildHardpoint()
    shipBuilder_buildhardpoint_210.build = shipBuilder_build_35
    shipBuilder_buildhardpoint_210.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_210.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_210 = importer.save_or_locate(shipBuilder_buildhardpoint_210)

    shipBuilder_buildhardpoint_211 = BuildHardpoint()
    shipBuilder_buildhardpoint_211.build = shipBuilder_build_35
    shipBuilder_buildhardpoint_211.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_211.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_211 = importer.save_or_locate(shipBuilder_buildhardpoint_211)

    shipBuilder_buildhardpoint_212 = BuildHardpoint()
    shipBuilder_buildhardpoint_212.build = shipBuilder_build_36
    shipBuilder_buildhardpoint_212.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_212.item = None
    shipBuilder_buildhardpoint_212 = importer.save_or_locate(shipBuilder_buildhardpoint_212)

    shipBuilder_buildhardpoint_213 = BuildHardpoint()
    shipBuilder_buildhardpoint_213.build = shipBuilder_build_36
    shipBuilder_buildhardpoint_213.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_213.item = None
    shipBuilder_buildhardpoint_213 = importer.save_or_locate(shipBuilder_buildhardpoint_213)

    shipBuilder_buildhardpoint_214 = BuildHardpoint()
    shipBuilder_buildhardpoint_214.build = shipBuilder_build_36
    shipBuilder_buildhardpoint_214.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_214.item = None
    shipBuilder_buildhardpoint_214 = importer.save_or_locate(shipBuilder_buildhardpoint_214)

    shipBuilder_buildhardpoint_215 = BuildHardpoint()
    shipBuilder_buildhardpoint_215.build = shipBuilder_build_36
    shipBuilder_buildhardpoint_215.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_215.item = None
    shipBuilder_buildhardpoint_215 = importer.save_or_locate(shipBuilder_buildhardpoint_215)

    shipBuilder_buildhardpoint_216 = BuildHardpoint()
    shipBuilder_buildhardpoint_216.build = shipBuilder_build_36
    shipBuilder_buildhardpoint_216.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_216.item = None
    shipBuilder_buildhardpoint_216 = importer.save_or_locate(shipBuilder_buildhardpoint_216)

    shipBuilder_buildhardpoint_217 = BuildHardpoint()
    shipBuilder_buildhardpoint_217.build = shipBuilder_build_37
    shipBuilder_buildhardpoint_217.hardpoint = shipBuilder_hardpoint_1
    shipBuilder_buildhardpoint_217.item = shipBuilder_item_45
    shipBuilder_buildhardpoint_217 = importer.save_or_locate(shipBuilder_buildhardpoint_217)

    shipBuilder_buildhardpoint_218 = BuildHardpoint()
    shipBuilder_buildhardpoint_218.build = shipBuilder_build_37
    shipBuilder_buildhardpoint_218.hardpoint = shipBuilder_hardpoint_2
    shipBuilder_buildhardpoint_218.item = shipBuilder_item_46
    shipBuilder_buildhardpoint_218 = importer.save_or_locate(shipBuilder_buildhardpoint_218)

    shipBuilder_buildhardpoint_219 = BuildHardpoint()
    shipBuilder_buildhardpoint_219.build = shipBuilder_build_37
    shipBuilder_buildhardpoint_219.hardpoint = shipBuilder_hardpoint_3
    shipBuilder_buildhardpoint_219.item = shipBuilder_item_46
    shipBuilder_buildhardpoint_219 = importer.save_or_locate(shipBuilder_buildhardpoint_219)

    shipBuilder_buildhardpoint_220 = BuildHardpoint()
    shipBuilder_buildhardpoint_220.build = shipBuilder_build_37
    shipBuilder_buildhardpoint_220.hardpoint = shipBuilder_hardpoint_4
    shipBuilder_buildhardpoint_220.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_220 = importer.save_or_locate(shipBuilder_buildhardpoint_220)

    shipBuilder_buildhardpoint_221 = BuildHardpoint()
    shipBuilder_buildhardpoint_221.build = shipBuilder_build_37
    shipBuilder_buildhardpoint_221.hardpoint = shipBuilder_hardpoint_5
    shipBuilder_buildhardpoint_221.item = shipBuilder_item_43
    shipBuilder_buildhardpoint_221 = importer.save_or_locate(shipBuilder_buildhardpoint_221)

    shipBuilder_buildhardpoint_222 = BuildHardpoint()
    shipBuilder_buildhardpoint_222.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_222.hardpoint = shipBuilder_hardpoint_31
    shipBuilder_buildhardpoint_222.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_222 = importer.save_or_locate(shipBuilder_buildhardpoint_222)

    shipBuilder_buildhardpoint_223 = BuildHardpoint()
    shipBuilder_buildhardpoint_223.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_223.hardpoint = shipBuilder_hardpoint_32
    shipBuilder_buildhardpoint_223.item = None
    shipBuilder_buildhardpoint_223 = importer.save_or_locate(shipBuilder_buildhardpoint_223)

    shipBuilder_buildhardpoint_224 = BuildHardpoint()
    shipBuilder_buildhardpoint_224.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_224.hardpoint = shipBuilder_hardpoint_33
    shipBuilder_buildhardpoint_224.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_224 = importer.save_or_locate(shipBuilder_buildhardpoint_224)

    shipBuilder_buildhardpoint_225 = BuildHardpoint()
    shipBuilder_buildhardpoint_225.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_225.hardpoint = shipBuilder_hardpoint_34
    shipBuilder_buildhardpoint_225.item = None
    shipBuilder_buildhardpoint_225 = importer.save_or_locate(shipBuilder_buildhardpoint_225)

    shipBuilder_buildhardpoint_226 = BuildHardpoint()
    shipBuilder_buildhardpoint_226.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_226.hardpoint = shipBuilder_hardpoint_35
    shipBuilder_buildhardpoint_226.item = None
    shipBuilder_buildhardpoint_226 = importer.save_or_locate(shipBuilder_buildhardpoint_226)

    shipBuilder_buildhardpoint_227 = BuildHardpoint()
    shipBuilder_buildhardpoint_227.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_227.hardpoint = shipBuilder_hardpoint_36
    shipBuilder_buildhardpoint_227.item = None
    shipBuilder_buildhardpoint_227 = importer.save_or_locate(shipBuilder_buildhardpoint_227)

    shipBuilder_buildhardpoint_228 = BuildHardpoint()
    shipBuilder_buildhardpoint_228.build = shipBuilder_build_38
    shipBuilder_buildhardpoint_228.hardpoint = shipBuilder_hardpoint_37
    shipBuilder_buildhardpoint_228.item = shipBuilder_item_62
    shipBuilder_buildhardpoint_228 = importer.save_or_locate(shipBuilder_buildhardpoint_228)

    shipBuilder_buildhardpoint_229 = BuildHardpoint()
    shipBuilder_buildhardpoint_229.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_229.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_229.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_229 = importer.save_or_locate(shipBuilder_buildhardpoint_229)

    shipBuilder_buildhardpoint_230 = BuildHardpoint()
    shipBuilder_buildhardpoint_230.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_230.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_230.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_230 = importer.save_or_locate(shipBuilder_buildhardpoint_230)

    shipBuilder_buildhardpoint_231 = BuildHardpoint()
    shipBuilder_buildhardpoint_231.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_231.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_231.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_231 = importer.save_or_locate(shipBuilder_buildhardpoint_231)

    shipBuilder_buildhardpoint_232 = BuildHardpoint()
    shipBuilder_buildhardpoint_232.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_232.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_232.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_232 = importer.save_or_locate(shipBuilder_buildhardpoint_232)

    shipBuilder_buildhardpoint_233 = BuildHardpoint()
    shipBuilder_buildhardpoint_233.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_233.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_233.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_233 = importer.save_or_locate(shipBuilder_buildhardpoint_233)

    shipBuilder_buildhardpoint_234 = BuildHardpoint()
    shipBuilder_buildhardpoint_234.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_234.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_234.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_234 = importer.save_or_locate(shipBuilder_buildhardpoint_234)

    shipBuilder_buildhardpoint_235 = BuildHardpoint()
    shipBuilder_buildhardpoint_235.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_235.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_235.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_235 = importer.save_or_locate(shipBuilder_buildhardpoint_235)

    shipBuilder_buildhardpoint_236 = BuildHardpoint()
    shipBuilder_buildhardpoint_236.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_236.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_236.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_236 = importer.save_or_locate(shipBuilder_buildhardpoint_236)

    shipBuilder_buildhardpoint_237 = BuildHardpoint()
    shipBuilder_buildhardpoint_237.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_237.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_237.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_237 = importer.save_or_locate(shipBuilder_buildhardpoint_237)

    shipBuilder_buildhardpoint_238 = BuildHardpoint()
    shipBuilder_buildhardpoint_238.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_238.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_238.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_238 = importer.save_or_locate(shipBuilder_buildhardpoint_238)

    shipBuilder_buildhardpoint_239 = BuildHardpoint()
    shipBuilder_buildhardpoint_239.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_239.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_239.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_239 = importer.save_or_locate(shipBuilder_buildhardpoint_239)

    shipBuilder_buildhardpoint_240 = BuildHardpoint()
    shipBuilder_buildhardpoint_240.build = shipBuilder_build_39
    shipBuilder_buildhardpoint_240.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_240.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_240 = importer.save_or_locate(shipBuilder_buildhardpoint_240)

    shipBuilder_buildhardpoint_241 = BuildHardpoint()
    shipBuilder_buildhardpoint_241.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_241.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_241.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_241 = importer.save_or_locate(shipBuilder_buildhardpoint_241)

    shipBuilder_buildhardpoint_242 = BuildHardpoint()
    shipBuilder_buildhardpoint_242.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_242.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_242.item = shipBuilder_item_49
    shipBuilder_buildhardpoint_242 = importer.save_or_locate(shipBuilder_buildhardpoint_242)

    shipBuilder_buildhardpoint_243 = BuildHardpoint()
    shipBuilder_buildhardpoint_243.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_243.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_243.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_243 = importer.save_or_locate(shipBuilder_buildhardpoint_243)

    shipBuilder_buildhardpoint_244 = BuildHardpoint()
    shipBuilder_buildhardpoint_244.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_244.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_244.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_244 = importer.save_or_locate(shipBuilder_buildhardpoint_244)

    shipBuilder_buildhardpoint_245 = BuildHardpoint()
    shipBuilder_buildhardpoint_245.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_245.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_245.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_245 = importer.save_or_locate(shipBuilder_buildhardpoint_245)

    shipBuilder_buildhardpoint_246 = BuildHardpoint()
    shipBuilder_buildhardpoint_246.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_246.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_246.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_246 = importer.save_or_locate(shipBuilder_buildhardpoint_246)

    shipBuilder_buildhardpoint_247 = BuildHardpoint()
    shipBuilder_buildhardpoint_247.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_247.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_247.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_247 = importer.save_or_locate(shipBuilder_buildhardpoint_247)

    shipBuilder_buildhardpoint_248 = BuildHardpoint()
    shipBuilder_buildhardpoint_248.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_248.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_248.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_248 = importer.save_or_locate(shipBuilder_buildhardpoint_248)

    shipBuilder_buildhardpoint_249 = BuildHardpoint()
    shipBuilder_buildhardpoint_249.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_249.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_249.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_249 = importer.save_or_locate(shipBuilder_buildhardpoint_249)

    shipBuilder_buildhardpoint_250 = BuildHardpoint()
    shipBuilder_buildhardpoint_250.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_250.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_250.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_250 = importer.save_or_locate(shipBuilder_buildhardpoint_250)

    shipBuilder_buildhardpoint_251 = BuildHardpoint()
    shipBuilder_buildhardpoint_251.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_251.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_251.item = shipBuilder_item_63
    shipBuilder_buildhardpoint_251 = importer.save_or_locate(shipBuilder_buildhardpoint_251)

    shipBuilder_buildhardpoint_252 = BuildHardpoint()
    shipBuilder_buildhardpoint_252.build = shipBuilder_build_40
    shipBuilder_buildhardpoint_252.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_252.item = shipBuilder_item_52
    shipBuilder_buildhardpoint_252 = importer.save_or_locate(shipBuilder_buildhardpoint_252)

    shipBuilder_buildhardpoint_253 = BuildHardpoint()
    shipBuilder_buildhardpoint_253.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_253.hardpoint = shipBuilder_hardpoint_9
    shipBuilder_buildhardpoint_253.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_253 = importer.save_or_locate(shipBuilder_buildhardpoint_253)

    shipBuilder_buildhardpoint_254 = BuildHardpoint()
    shipBuilder_buildhardpoint_254.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_254.hardpoint = shipBuilder_hardpoint_10
    shipBuilder_buildhardpoint_254.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_254 = importer.save_or_locate(shipBuilder_buildhardpoint_254)

    shipBuilder_buildhardpoint_255 = BuildHardpoint()
    shipBuilder_buildhardpoint_255.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_255.hardpoint = shipBuilder_hardpoint_11
    shipBuilder_buildhardpoint_255.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_255 = importer.save_or_locate(shipBuilder_buildhardpoint_255)

    shipBuilder_buildhardpoint_256 = BuildHardpoint()
    shipBuilder_buildhardpoint_256.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_256.hardpoint = shipBuilder_hardpoint_12
    shipBuilder_buildhardpoint_256.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_256 = importer.save_or_locate(shipBuilder_buildhardpoint_256)

    shipBuilder_buildhardpoint_257 = BuildHardpoint()
    shipBuilder_buildhardpoint_257.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_257.hardpoint = shipBuilder_hardpoint_13
    shipBuilder_buildhardpoint_257.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_257 = importer.save_or_locate(shipBuilder_buildhardpoint_257)

    shipBuilder_buildhardpoint_258 = BuildHardpoint()
    shipBuilder_buildhardpoint_258.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_258.hardpoint = shipBuilder_hardpoint_14
    shipBuilder_buildhardpoint_258.item = shipBuilder_item_55
    shipBuilder_buildhardpoint_258 = importer.save_or_locate(shipBuilder_buildhardpoint_258)

    shipBuilder_buildhardpoint_259 = BuildHardpoint()
    shipBuilder_buildhardpoint_259.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_259.hardpoint = shipBuilder_hardpoint_20
    shipBuilder_buildhardpoint_259.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_259 = importer.save_or_locate(shipBuilder_buildhardpoint_259)

    shipBuilder_buildhardpoint_260 = BuildHardpoint()
    shipBuilder_buildhardpoint_260.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_260.hardpoint = shipBuilder_hardpoint_21
    shipBuilder_buildhardpoint_260.item = shipBuilder_item_51
    shipBuilder_buildhardpoint_260 = importer.save_or_locate(shipBuilder_buildhardpoint_260)

    shipBuilder_buildhardpoint_261 = BuildHardpoint()
    shipBuilder_buildhardpoint_261.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_261.hardpoint = shipBuilder_hardpoint_22
    shipBuilder_buildhardpoint_261.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_261 = importer.save_or_locate(shipBuilder_buildhardpoint_261)

    shipBuilder_buildhardpoint_262 = BuildHardpoint()
    shipBuilder_buildhardpoint_262.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_262.hardpoint = shipBuilder_hardpoint_23
    shipBuilder_buildhardpoint_262.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_262 = importer.save_or_locate(shipBuilder_buildhardpoint_262)

    shipBuilder_buildhardpoint_263 = BuildHardpoint()
    shipBuilder_buildhardpoint_263.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_263.hardpoint = shipBuilder_hardpoint_24
    shipBuilder_buildhardpoint_263.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_263 = importer.save_or_locate(shipBuilder_buildhardpoint_263)

    shipBuilder_buildhardpoint_264 = BuildHardpoint()
    shipBuilder_buildhardpoint_264.build = shipBuilder_build_41
    shipBuilder_buildhardpoint_264.hardpoint = shipBuilder_hardpoint_25
    shipBuilder_buildhardpoint_264.item = shipBuilder_item_56
    shipBuilder_buildhardpoint_264 = importer.save_or_locate(shipBuilder_buildhardpoint_264)

    #Processing model: BuildEngineMod

    from shipBuilder.models import BuildEngineMod

    shipBuilder_buildenginemod_1 = BuildEngineMod()
    shipBuilder_buildenginemod_1.build = shipBuilder_build_1
    shipBuilder_buildenginemod_1.item = None
    shipBuilder_buildenginemod_1 = importer.save_or_locate(shipBuilder_buildenginemod_1)

    shipBuilder_buildenginemod_2 = BuildEngineMod()
    shipBuilder_buildenginemod_2.build = shipBuilder_build_2
    shipBuilder_buildenginemod_2.item = None
    shipBuilder_buildenginemod_2 = importer.save_or_locate(shipBuilder_buildenginemod_2)

    shipBuilder_buildenginemod_3 = BuildEngineMod()
    shipBuilder_buildenginemod_3.build = shipBuilder_build_3
    shipBuilder_buildenginemod_3.item = shipBuilder_item_36
    shipBuilder_buildenginemod_3 = importer.save_or_locate(shipBuilder_buildenginemod_3)

    shipBuilder_buildenginemod_4 = BuildEngineMod()
    shipBuilder_buildenginemod_4.build = shipBuilder_build_4
    shipBuilder_buildenginemod_4.item = None
    shipBuilder_buildenginemod_4 = importer.save_or_locate(shipBuilder_buildenginemod_4)

    shipBuilder_buildenginemod_5 = BuildEngineMod()
    shipBuilder_buildenginemod_5.build = shipBuilder_build_5
    shipBuilder_buildenginemod_5.item = shipBuilder_item_38
    shipBuilder_buildenginemod_5 = importer.save_or_locate(shipBuilder_buildenginemod_5)

    shipBuilder_buildenginemod_6 = BuildEngineMod()
    shipBuilder_buildenginemod_6.build = shipBuilder_build_6
    shipBuilder_buildenginemod_6.item = None
    shipBuilder_buildenginemod_6 = importer.save_or_locate(shipBuilder_buildenginemod_6)

    shipBuilder_buildenginemod_7 = BuildEngineMod()
    shipBuilder_buildenginemod_7.build = shipBuilder_build_7
    shipBuilder_buildenginemod_7.item = None
    shipBuilder_buildenginemod_7 = importer.save_or_locate(shipBuilder_buildenginemod_7)

    shipBuilder_buildenginemod_8 = BuildEngineMod()
    shipBuilder_buildenginemod_8.build = shipBuilder_build_8
    shipBuilder_buildenginemod_8.item = shipBuilder_item_36
    shipBuilder_buildenginemod_8 = importer.save_or_locate(shipBuilder_buildenginemod_8)

    shipBuilder_buildenginemod_9 = BuildEngineMod()
    shipBuilder_buildenginemod_9.build = shipBuilder_build_9
    shipBuilder_buildenginemod_9.item = shipBuilder_item_36
    shipBuilder_buildenginemod_9 = importer.save_or_locate(shipBuilder_buildenginemod_9)

    shipBuilder_buildenginemod_10 = BuildEngineMod()
    shipBuilder_buildenginemod_10.build = shipBuilder_build_10
    shipBuilder_buildenginemod_10.item = None
    shipBuilder_buildenginemod_10 = importer.save_or_locate(shipBuilder_buildenginemod_10)

    shipBuilder_buildenginemod_11 = BuildEngineMod()
    shipBuilder_buildenginemod_11.build = shipBuilder_build_11
    shipBuilder_buildenginemod_11.item = None
    shipBuilder_buildenginemod_11 = importer.save_or_locate(shipBuilder_buildenginemod_11)

    shipBuilder_buildenginemod_12 = BuildEngineMod()
    shipBuilder_buildenginemod_12.build = shipBuilder_build_12
    shipBuilder_buildenginemod_12.item = shipBuilder_item_38
    shipBuilder_buildenginemod_12 = importer.save_or_locate(shipBuilder_buildenginemod_12)

    shipBuilder_buildenginemod_13 = BuildEngineMod()
    shipBuilder_buildenginemod_13.build = shipBuilder_build_12
    shipBuilder_buildenginemod_13.item = shipBuilder_item_38
    shipBuilder_buildenginemod_13 = importer.save_or_locate(shipBuilder_buildenginemod_13)

    shipBuilder_buildenginemod_14 = BuildEngineMod()
    shipBuilder_buildenginemod_14.build = shipBuilder_build_13
    shipBuilder_buildenginemod_14.item = None
    shipBuilder_buildenginemod_14 = importer.save_or_locate(shipBuilder_buildenginemod_14)

    shipBuilder_buildenginemod_15 = BuildEngineMod()
    shipBuilder_buildenginemod_15.build = shipBuilder_build_14
    shipBuilder_buildenginemod_15.item = None
    shipBuilder_buildenginemod_15 = importer.save_or_locate(shipBuilder_buildenginemod_15)

    shipBuilder_buildenginemod_16 = BuildEngineMod()
    shipBuilder_buildenginemod_16.build = shipBuilder_build_15
    shipBuilder_buildenginemod_16.item = shipBuilder_item_38
    shipBuilder_buildenginemod_16 = importer.save_or_locate(shipBuilder_buildenginemod_16)

    shipBuilder_buildenginemod_17 = BuildEngineMod()
    shipBuilder_buildenginemod_17.build = shipBuilder_build_16
    shipBuilder_buildenginemod_17.item = None
    shipBuilder_buildenginemod_17 = importer.save_or_locate(shipBuilder_buildenginemod_17)

    shipBuilder_buildenginemod_18 = BuildEngineMod()
    shipBuilder_buildenginemod_18.build = shipBuilder_build_17
    shipBuilder_buildenginemod_18.item = shipBuilder_item_38
    shipBuilder_buildenginemod_18 = importer.save_or_locate(shipBuilder_buildenginemod_18)

    shipBuilder_buildenginemod_19 = BuildEngineMod()
    shipBuilder_buildenginemod_19.build = shipBuilder_build_18
    shipBuilder_buildenginemod_19.item = shipBuilder_item_36
    shipBuilder_buildenginemod_19 = importer.save_or_locate(shipBuilder_buildenginemod_19)

    shipBuilder_buildenginemod_20 = BuildEngineMod()
    shipBuilder_buildenginemod_20.build = shipBuilder_build_19
    shipBuilder_buildenginemod_20.item = shipBuilder_item_36
    shipBuilder_buildenginemod_20 = importer.save_or_locate(shipBuilder_buildenginemod_20)

    shipBuilder_buildenginemod_21 = BuildEngineMod()
    shipBuilder_buildenginemod_21.build = shipBuilder_build_20
    shipBuilder_buildenginemod_21.item = None
    shipBuilder_buildenginemod_21 = importer.save_or_locate(shipBuilder_buildenginemod_21)

    shipBuilder_buildenginemod_22 = BuildEngineMod()
    shipBuilder_buildenginemod_22.build = shipBuilder_build_21
    shipBuilder_buildenginemod_22.item = None
    shipBuilder_buildenginemod_22 = importer.save_or_locate(shipBuilder_buildenginemod_22)

    shipBuilder_buildenginemod_23 = BuildEngineMod()
    shipBuilder_buildenginemod_23.build = shipBuilder_build_22
    shipBuilder_buildenginemod_23.item = None
    shipBuilder_buildenginemod_23 = importer.save_or_locate(shipBuilder_buildenginemod_23)

    shipBuilder_buildenginemod_24 = BuildEngineMod()
    shipBuilder_buildenginemod_24.build = shipBuilder_build_23
    shipBuilder_buildenginemod_24.item = shipBuilder_item_36
    shipBuilder_buildenginemod_24 = importer.save_or_locate(shipBuilder_buildenginemod_24)

    shipBuilder_buildenginemod_25 = BuildEngineMod()
    shipBuilder_buildenginemod_25.build = shipBuilder_build_23
    shipBuilder_buildenginemod_25.item = shipBuilder_item_36
    shipBuilder_buildenginemod_25 = importer.save_or_locate(shipBuilder_buildenginemod_25)

    shipBuilder_buildenginemod_26 = BuildEngineMod()
    shipBuilder_buildenginemod_26.build = shipBuilder_build_24
    shipBuilder_buildenginemod_26.item = shipBuilder_item_36
    shipBuilder_buildenginemod_26 = importer.save_or_locate(shipBuilder_buildenginemod_26)

    shipBuilder_buildenginemod_27 = BuildEngineMod()
    shipBuilder_buildenginemod_27.build = shipBuilder_build_24
    shipBuilder_buildenginemod_27.item = shipBuilder_item_36
    shipBuilder_buildenginemod_27 = importer.save_or_locate(shipBuilder_buildenginemod_27)

    shipBuilder_buildenginemod_28 = BuildEngineMod()
    shipBuilder_buildenginemod_28.build = shipBuilder_build_25
    shipBuilder_buildenginemod_28.item = None
    shipBuilder_buildenginemod_28 = importer.save_or_locate(shipBuilder_buildenginemod_28)

    shipBuilder_buildenginemod_29 = BuildEngineMod()
    shipBuilder_buildenginemod_29.build = shipBuilder_build_26
    shipBuilder_buildenginemod_29.item = None
    shipBuilder_buildenginemod_29 = importer.save_or_locate(shipBuilder_buildenginemod_29)

    shipBuilder_buildenginemod_30 = BuildEngineMod()
    shipBuilder_buildenginemod_30.build = shipBuilder_build_27
    shipBuilder_buildenginemod_30.item = None
    shipBuilder_buildenginemod_30 = importer.save_or_locate(shipBuilder_buildenginemod_30)

    shipBuilder_buildenginemod_31 = BuildEngineMod()
    shipBuilder_buildenginemod_31.build = shipBuilder_build_28
    shipBuilder_buildenginemod_31.item = shipBuilder_item_38
    shipBuilder_buildenginemod_31 = importer.save_or_locate(shipBuilder_buildenginemod_31)

    shipBuilder_buildenginemod_32 = BuildEngineMod()
    shipBuilder_buildenginemod_32.build = shipBuilder_build_29
    shipBuilder_buildenginemod_32.item = shipBuilder_item_38
    shipBuilder_buildenginemod_32 = importer.save_or_locate(shipBuilder_buildenginemod_32)

    shipBuilder_buildenginemod_33 = BuildEngineMod()
    shipBuilder_buildenginemod_33.build = shipBuilder_build_30
    shipBuilder_buildenginemod_33.item = shipBuilder_item_38
    shipBuilder_buildenginemod_33 = importer.save_or_locate(shipBuilder_buildenginemod_33)

    shipBuilder_buildenginemod_34 = BuildEngineMod()
    shipBuilder_buildenginemod_34.build = shipBuilder_build_31
    shipBuilder_buildenginemod_34.item = shipBuilder_item_36
    shipBuilder_buildenginemod_34 = importer.save_or_locate(shipBuilder_buildenginemod_34)

    shipBuilder_buildenginemod_35 = BuildEngineMod()
    shipBuilder_buildenginemod_35.build = shipBuilder_build_31
    shipBuilder_buildenginemod_35.item = shipBuilder_item_38
    shipBuilder_buildenginemod_35 = importer.save_or_locate(shipBuilder_buildenginemod_35)

    shipBuilder_buildenginemod_36 = BuildEngineMod()
    shipBuilder_buildenginemod_36.build = shipBuilder_build_32
    shipBuilder_buildenginemod_36.item = shipBuilder_item_36
    shipBuilder_buildenginemod_36 = importer.save_or_locate(shipBuilder_buildenginemod_36)

    shipBuilder_buildenginemod_37 = BuildEngineMod()
    shipBuilder_buildenginemod_37.build = shipBuilder_build_32
    shipBuilder_buildenginemod_37.item = shipBuilder_item_38
    shipBuilder_buildenginemod_37 = importer.save_or_locate(shipBuilder_buildenginemod_37)

    shipBuilder_buildenginemod_38 = BuildEngineMod()
    shipBuilder_buildenginemod_38.build = shipBuilder_build_33
    shipBuilder_buildenginemod_38.item = shipBuilder_item_36
    shipBuilder_buildenginemod_38 = importer.save_or_locate(shipBuilder_buildenginemod_38)

    shipBuilder_buildenginemod_39 = BuildEngineMod()
    shipBuilder_buildenginemod_39.build = shipBuilder_build_33
    shipBuilder_buildenginemod_39.item = shipBuilder_item_36
    shipBuilder_buildenginemod_39 = importer.save_or_locate(shipBuilder_buildenginemod_39)

    shipBuilder_buildenginemod_40 = BuildEngineMod()
    shipBuilder_buildenginemod_40.build = shipBuilder_build_33
    shipBuilder_buildenginemod_40.item = shipBuilder_item_38
    shipBuilder_buildenginemod_40 = importer.save_or_locate(shipBuilder_buildenginemod_40)

    shipBuilder_buildenginemod_41 = BuildEngineMod()
    shipBuilder_buildenginemod_41.build = shipBuilder_build_34
    shipBuilder_buildenginemod_41.item = None
    shipBuilder_buildenginemod_41 = importer.save_or_locate(shipBuilder_buildenginemod_41)

    shipBuilder_buildenginemod_42 = BuildEngineMod()
    shipBuilder_buildenginemod_42.build = shipBuilder_build_35
    shipBuilder_buildenginemod_42.item = shipBuilder_item_36
    shipBuilder_buildenginemod_42 = importer.save_or_locate(shipBuilder_buildenginemod_42)

    shipBuilder_buildenginemod_43 = BuildEngineMod()
    shipBuilder_buildenginemod_43.build = shipBuilder_build_36
    shipBuilder_buildenginemod_43.item = None
    shipBuilder_buildenginemod_43 = importer.save_or_locate(shipBuilder_buildenginemod_43)

    shipBuilder_buildenginemod_44 = BuildEngineMod()
    shipBuilder_buildenginemod_44.build = shipBuilder_build_37
    shipBuilder_buildenginemod_44.item = shipBuilder_item_36
    shipBuilder_buildenginemod_44 = importer.save_or_locate(shipBuilder_buildenginemod_44)

    shipBuilder_buildenginemod_45 = BuildEngineMod()
    shipBuilder_buildenginemod_45.build = shipBuilder_build_37
    shipBuilder_buildenginemod_45.item = shipBuilder_item_36
    shipBuilder_buildenginemod_45 = importer.save_or_locate(shipBuilder_buildenginemod_45)

    shipBuilder_buildenginemod_46 = BuildEngineMod()
    shipBuilder_buildenginemod_46.build = shipBuilder_build_38
    shipBuilder_buildenginemod_46.item = shipBuilder_item_38
    shipBuilder_buildenginemod_46 = importer.save_or_locate(shipBuilder_buildenginemod_46)

    shipBuilder_buildenginemod_47 = BuildEngineMod()
    shipBuilder_buildenginemod_47.build = shipBuilder_build_39
    shipBuilder_buildenginemod_47.item = shipBuilder_item_36
    shipBuilder_buildenginemod_47 = importer.save_or_locate(shipBuilder_buildenginemod_47)

    shipBuilder_buildenginemod_48 = BuildEngineMod()
    shipBuilder_buildenginemod_48.build = shipBuilder_build_40
    shipBuilder_buildenginemod_48.item = shipBuilder_item_36
    shipBuilder_buildenginemod_48 = importer.save_or_locate(shipBuilder_buildenginemod_48)

    shipBuilder_buildenginemod_49 = BuildEngineMod()
    shipBuilder_buildenginemod_49.build = shipBuilder_build_41
    shipBuilder_buildenginemod_49.item = shipBuilder_item_36
    shipBuilder_buildenginemod_49 = importer.save_or_locate(shipBuilder_buildenginemod_49)

    #Processing model: BuildHullMod

    from shipBuilder.models import BuildHullMod

    shipBuilder_buildhullmod_1 = BuildHullMod()
    shipBuilder_buildhullmod_1.build = shipBuilder_build_1
    shipBuilder_buildhullmod_1.item = None
    shipBuilder_buildhullmod_1 = importer.save_or_locate(shipBuilder_buildhullmod_1)

    shipBuilder_buildhullmod_2 = BuildHullMod()
    shipBuilder_buildhullmod_2.build = shipBuilder_build_2
    shipBuilder_buildhullmod_2.item = None
    shipBuilder_buildhullmod_2 = importer.save_or_locate(shipBuilder_buildhullmod_2)

    shipBuilder_buildhullmod_3 = BuildHullMod()
    shipBuilder_buildhullmod_3.build = shipBuilder_build_3
    shipBuilder_buildhullmod_3.item = shipBuilder_item_34
    shipBuilder_buildhullmod_3 = importer.save_or_locate(shipBuilder_buildhullmod_3)

    shipBuilder_buildhullmod_4 = BuildHullMod()
    shipBuilder_buildhullmod_4.build = shipBuilder_build_3
    shipBuilder_buildhullmod_4.item = shipBuilder_item_35
    shipBuilder_buildhullmod_4 = importer.save_or_locate(shipBuilder_buildhullmod_4)

    shipBuilder_buildhullmod_5 = BuildHullMod()
    shipBuilder_buildhullmod_5.build = shipBuilder_build_3
    shipBuilder_buildhullmod_5.item = shipBuilder_item_37
    shipBuilder_buildhullmod_5 = importer.save_or_locate(shipBuilder_buildhullmod_5)

    shipBuilder_buildhullmod_6 = BuildHullMod()
    shipBuilder_buildhullmod_6.build = shipBuilder_build_4
    shipBuilder_buildhullmod_6.item = shipBuilder_item_37
    shipBuilder_buildhullmod_6 = importer.save_or_locate(shipBuilder_buildhullmod_6)

    shipBuilder_buildhullmod_7 = BuildHullMod()
    shipBuilder_buildhullmod_7.build = shipBuilder_build_4
    shipBuilder_buildhullmod_7.item = shipBuilder_item_34
    shipBuilder_buildhullmod_7 = importer.save_or_locate(shipBuilder_buildhullmod_7)

    shipBuilder_buildhullmod_8 = BuildHullMod()
    shipBuilder_buildhullmod_8.build = shipBuilder_build_5
    shipBuilder_buildhullmod_8.item = shipBuilder_item_34
    shipBuilder_buildhullmod_8 = importer.save_or_locate(shipBuilder_buildhullmod_8)

    shipBuilder_buildhullmod_9 = BuildHullMod()
    shipBuilder_buildhullmod_9.build = shipBuilder_build_5
    shipBuilder_buildhullmod_9.item = shipBuilder_item_37
    shipBuilder_buildhullmod_9 = importer.save_or_locate(shipBuilder_buildhullmod_9)

    shipBuilder_buildhullmod_10 = BuildHullMod()
    shipBuilder_buildhullmod_10.build = shipBuilder_build_5
    shipBuilder_buildhullmod_10.item = shipBuilder_item_35
    shipBuilder_buildhullmod_10 = importer.save_or_locate(shipBuilder_buildhullmod_10)

    shipBuilder_buildhullmod_11 = BuildHullMod()
    shipBuilder_buildhullmod_11.build = shipBuilder_build_6
    shipBuilder_buildhullmod_11.item = None
    shipBuilder_buildhullmod_11 = importer.save_or_locate(shipBuilder_buildhullmod_11)

    shipBuilder_buildhullmod_12 = BuildHullMod()
    shipBuilder_buildhullmod_12.build = shipBuilder_build_7
    shipBuilder_buildhullmod_12.item = None
    shipBuilder_buildhullmod_12 = importer.save_or_locate(shipBuilder_buildhullmod_12)

    shipBuilder_buildhullmod_13 = BuildHullMod()
    shipBuilder_buildhullmod_13.build = shipBuilder_build_8
    shipBuilder_buildhullmod_13.item = shipBuilder_item_34
    shipBuilder_buildhullmod_13 = importer.save_or_locate(shipBuilder_buildhullmod_13)

    shipBuilder_buildhullmod_14 = BuildHullMod()
    shipBuilder_buildhullmod_14.build = shipBuilder_build_9
    shipBuilder_buildhullmod_14.item = shipBuilder_item_35
    shipBuilder_buildhullmod_14 = importer.save_or_locate(shipBuilder_buildhullmod_14)

    shipBuilder_buildhullmod_15 = BuildHullMod()
    shipBuilder_buildhullmod_15.build = shipBuilder_build_10
    shipBuilder_buildhullmod_15.item = None
    shipBuilder_buildhullmod_15 = importer.save_or_locate(shipBuilder_buildhullmod_15)

    shipBuilder_buildhullmod_16 = BuildHullMod()
    shipBuilder_buildhullmod_16.build = shipBuilder_build_11
    shipBuilder_buildhullmod_16.item = None
    shipBuilder_buildhullmod_16 = importer.save_or_locate(shipBuilder_buildhullmod_16)

    shipBuilder_buildhullmod_17 = BuildHullMod()
    shipBuilder_buildhullmod_17.build = shipBuilder_build_12
    shipBuilder_buildhullmod_17.item = shipBuilder_item_34
    shipBuilder_buildhullmod_17 = importer.save_or_locate(shipBuilder_buildhullmod_17)

    shipBuilder_buildhullmod_18 = BuildHullMod()
    shipBuilder_buildhullmod_18.build = shipBuilder_build_13
    shipBuilder_buildhullmod_18.item = None
    shipBuilder_buildhullmod_18 = importer.save_or_locate(shipBuilder_buildhullmod_18)

    shipBuilder_buildhullmod_19 = BuildHullMod()
    shipBuilder_buildhullmod_19.build = shipBuilder_build_14
    shipBuilder_buildhullmod_19.item = None
    shipBuilder_buildhullmod_19 = importer.save_or_locate(shipBuilder_buildhullmod_19)

    shipBuilder_buildhullmod_20 = BuildHullMod()
    shipBuilder_buildhullmod_20.build = shipBuilder_build_15
    shipBuilder_buildhullmod_20.item = shipBuilder_item_34
    shipBuilder_buildhullmod_20 = importer.save_or_locate(shipBuilder_buildhullmod_20)

    shipBuilder_buildhullmod_21 = BuildHullMod()
    shipBuilder_buildhullmod_21.build = shipBuilder_build_16
    shipBuilder_buildhullmod_21.item = None
    shipBuilder_buildhullmod_21 = importer.save_or_locate(shipBuilder_buildhullmod_21)

    shipBuilder_buildhullmod_22 = BuildHullMod()
    shipBuilder_buildhullmod_22.build = shipBuilder_build_17
    shipBuilder_buildhullmod_22.item = shipBuilder_item_35
    shipBuilder_buildhullmod_22 = importer.save_or_locate(shipBuilder_buildhullmod_22)

    shipBuilder_buildhullmod_23 = BuildHullMod()
    shipBuilder_buildhullmod_23.build = shipBuilder_build_18
    shipBuilder_buildhullmod_23.item = shipBuilder_item_35
    shipBuilder_buildhullmod_23 = importer.save_or_locate(shipBuilder_buildhullmod_23)

    shipBuilder_buildhullmod_24 = BuildHullMod()
    shipBuilder_buildhullmod_24.build = shipBuilder_build_19
    shipBuilder_buildhullmod_24.item = None
    shipBuilder_buildhullmod_24 = importer.save_or_locate(shipBuilder_buildhullmod_24)

    shipBuilder_buildhullmod_25 = BuildHullMod()
    shipBuilder_buildhullmod_25.build = shipBuilder_build_20
    shipBuilder_buildhullmod_25.item = None
    shipBuilder_buildhullmod_25 = importer.save_or_locate(shipBuilder_buildhullmod_25)

    shipBuilder_buildhullmod_26 = BuildHullMod()
    shipBuilder_buildhullmod_26.build = shipBuilder_build_21
    shipBuilder_buildhullmod_26.item = None
    shipBuilder_buildhullmod_26 = importer.save_or_locate(shipBuilder_buildhullmod_26)

    shipBuilder_buildhullmod_27 = BuildHullMod()
    shipBuilder_buildhullmod_27.build = shipBuilder_build_22
    shipBuilder_buildhullmod_27.item = None
    shipBuilder_buildhullmod_27 = importer.save_or_locate(shipBuilder_buildhullmod_27)

    shipBuilder_buildhullmod_28 = BuildHullMod()
    shipBuilder_buildhullmod_28.build = shipBuilder_build_23
    shipBuilder_buildhullmod_28.item = shipBuilder_item_34
    shipBuilder_buildhullmod_28 = importer.save_or_locate(shipBuilder_buildhullmod_28)

    shipBuilder_buildhullmod_29 = BuildHullMod()
    shipBuilder_buildhullmod_29.build = shipBuilder_build_23
    shipBuilder_buildhullmod_29.item = shipBuilder_item_35
    shipBuilder_buildhullmod_29 = importer.save_or_locate(shipBuilder_buildhullmod_29)

    shipBuilder_buildhullmod_30 = BuildHullMod()
    shipBuilder_buildhullmod_30.build = shipBuilder_build_24
    shipBuilder_buildhullmod_30.item = shipBuilder_item_35
    shipBuilder_buildhullmod_30 = importer.save_or_locate(shipBuilder_buildhullmod_30)

    shipBuilder_buildhullmod_31 = BuildHullMod()
    shipBuilder_buildhullmod_31.build = shipBuilder_build_25
    shipBuilder_buildhullmod_31.item = None
    shipBuilder_buildhullmod_31 = importer.save_or_locate(shipBuilder_buildhullmod_31)

    shipBuilder_buildhullmod_32 = BuildHullMod()
    shipBuilder_buildhullmod_32.build = shipBuilder_build_26
    shipBuilder_buildhullmod_32.item = None
    shipBuilder_buildhullmod_32 = importer.save_or_locate(shipBuilder_buildhullmod_32)

    shipBuilder_buildhullmod_33 = BuildHullMod()
    shipBuilder_buildhullmod_33.build = shipBuilder_build_27
    shipBuilder_buildhullmod_33.item = None
    shipBuilder_buildhullmod_33 = importer.save_or_locate(shipBuilder_buildhullmod_33)

    shipBuilder_buildhullmod_34 = BuildHullMod()
    shipBuilder_buildhullmod_34.build = shipBuilder_build_28
    shipBuilder_buildhullmod_34.item = shipBuilder_item_35
    shipBuilder_buildhullmod_34 = importer.save_or_locate(shipBuilder_buildhullmod_34)

    shipBuilder_buildhullmod_35 = BuildHullMod()
    shipBuilder_buildhullmod_35.build = shipBuilder_build_28
    shipBuilder_buildhullmod_35.item = shipBuilder_item_34
    shipBuilder_buildhullmod_35 = importer.save_or_locate(shipBuilder_buildhullmod_35)

    shipBuilder_buildhullmod_36 = BuildHullMod()
    shipBuilder_buildhullmod_36.build = shipBuilder_build_29
    shipBuilder_buildhullmod_36.item = shipBuilder_item_35
    shipBuilder_buildhullmod_36 = importer.save_or_locate(shipBuilder_buildhullmod_36)

    shipBuilder_buildhullmod_37 = BuildHullMod()
    shipBuilder_buildhullmod_37.build = shipBuilder_build_29
    shipBuilder_buildhullmod_37.item = shipBuilder_item_34
    shipBuilder_buildhullmod_37 = importer.save_or_locate(shipBuilder_buildhullmod_37)

    shipBuilder_buildhullmod_38 = BuildHullMod()
    shipBuilder_buildhullmod_38.build = shipBuilder_build_30
    shipBuilder_buildhullmod_38.item = None
    shipBuilder_buildhullmod_38 = importer.save_or_locate(shipBuilder_buildhullmod_38)

    shipBuilder_buildhullmod_39 = BuildHullMod()
    shipBuilder_buildhullmod_39.build = shipBuilder_build_31
    shipBuilder_buildhullmod_39.item = shipBuilder_item_37
    shipBuilder_buildhullmod_39 = importer.save_or_locate(shipBuilder_buildhullmod_39)

    shipBuilder_buildhullmod_40 = BuildHullMod()
    shipBuilder_buildhullmod_40.build = shipBuilder_build_31
    shipBuilder_buildhullmod_40.item = shipBuilder_item_35
    shipBuilder_buildhullmod_40 = importer.save_or_locate(shipBuilder_buildhullmod_40)

    shipBuilder_buildhullmod_41 = BuildHullMod()
    shipBuilder_buildhullmod_41.build = shipBuilder_build_32
    shipBuilder_buildhullmod_41.item = shipBuilder_item_35
    shipBuilder_buildhullmod_41 = importer.save_or_locate(shipBuilder_buildhullmod_41)

    shipBuilder_buildhullmod_42 = BuildHullMod()
    shipBuilder_buildhullmod_42.build = shipBuilder_build_32
    shipBuilder_buildhullmod_42.item = shipBuilder_item_34
    shipBuilder_buildhullmod_42 = importer.save_or_locate(shipBuilder_buildhullmod_42)

    shipBuilder_buildhullmod_43 = BuildHullMod()
    shipBuilder_buildhullmod_43.build = shipBuilder_build_33
    shipBuilder_buildhullmod_43.item = None
    shipBuilder_buildhullmod_43 = importer.save_or_locate(shipBuilder_buildhullmod_43)

    shipBuilder_buildhullmod_44 = BuildHullMod()
    shipBuilder_buildhullmod_44.build = shipBuilder_build_34
    shipBuilder_buildhullmod_44.item = None
    shipBuilder_buildhullmod_44 = importer.save_or_locate(shipBuilder_buildhullmod_44)

    shipBuilder_buildhullmod_45 = BuildHullMod()
    shipBuilder_buildhullmod_45.build = shipBuilder_build_35
    shipBuilder_buildhullmod_45.item = shipBuilder_item_35
    shipBuilder_buildhullmod_45 = importer.save_or_locate(shipBuilder_buildhullmod_45)

    shipBuilder_buildhullmod_46 = BuildHullMod()
    shipBuilder_buildhullmod_46.build = shipBuilder_build_35
    shipBuilder_buildhullmod_46.item = shipBuilder_item_34
    shipBuilder_buildhullmod_46 = importer.save_or_locate(shipBuilder_buildhullmod_46)

    shipBuilder_buildhullmod_47 = BuildHullMod()
    shipBuilder_buildhullmod_47.build = shipBuilder_build_36
    shipBuilder_buildhullmod_47.item = None
    shipBuilder_buildhullmod_47 = importer.save_or_locate(shipBuilder_buildhullmod_47)

    shipBuilder_buildhullmod_48 = BuildHullMod()
    shipBuilder_buildhullmod_48.build = shipBuilder_build_37
    shipBuilder_buildhullmod_48.item = shipBuilder_item_34
    shipBuilder_buildhullmod_48 = importer.save_or_locate(shipBuilder_buildhullmod_48)

    shipBuilder_buildhullmod_49 = BuildHullMod()
    shipBuilder_buildhullmod_49.build = shipBuilder_build_37
    shipBuilder_buildhullmod_49.item = shipBuilder_item_35
    shipBuilder_buildhullmod_49 = importer.save_or_locate(shipBuilder_buildhullmod_49)

    shipBuilder_buildhullmod_50 = BuildHullMod()
    shipBuilder_buildhullmod_50.build = shipBuilder_build_38
    shipBuilder_buildhullmod_50.item = shipBuilder_item_37
    shipBuilder_buildhullmod_50 = importer.save_or_locate(shipBuilder_buildhullmod_50)

    shipBuilder_buildhullmod_51 = BuildHullMod()
    shipBuilder_buildhullmod_51.build = shipBuilder_build_39
    shipBuilder_buildhullmod_51.item = shipBuilder_item_34
    shipBuilder_buildhullmod_51 = importer.save_or_locate(shipBuilder_buildhullmod_51)

    shipBuilder_buildhullmod_52 = BuildHullMod()
    shipBuilder_buildhullmod_52.build = shipBuilder_build_39
    shipBuilder_buildhullmod_52.item = shipBuilder_item_34
    shipBuilder_buildhullmod_52 = importer.save_or_locate(shipBuilder_buildhullmod_52)

    shipBuilder_buildhullmod_53 = BuildHullMod()
    shipBuilder_buildhullmod_53.build = shipBuilder_build_39
    shipBuilder_buildhullmod_53.item = shipBuilder_item_35
    shipBuilder_buildhullmod_53 = importer.save_or_locate(shipBuilder_buildhullmod_53)

    shipBuilder_buildhullmod_54 = BuildHullMod()
    shipBuilder_buildhullmod_54.build = shipBuilder_build_40
    shipBuilder_buildhullmod_54.item = shipBuilder_item_34
    shipBuilder_buildhullmod_54 = importer.save_or_locate(shipBuilder_buildhullmod_54)

    shipBuilder_buildhullmod_55 = BuildHullMod()
    shipBuilder_buildhullmod_55.build = shipBuilder_build_40
    shipBuilder_buildhullmod_55.item = shipBuilder_item_34
    shipBuilder_buildhullmod_55 = importer.save_or_locate(shipBuilder_buildhullmod_55)

    shipBuilder_buildhullmod_56 = BuildHullMod()
    shipBuilder_buildhullmod_56.build = shipBuilder_build_40
    shipBuilder_buildhullmod_56.item = shipBuilder_item_35
    shipBuilder_buildhullmod_56 = importer.save_or_locate(shipBuilder_buildhullmod_56)

    shipBuilder_buildhullmod_57 = BuildHullMod()
    shipBuilder_buildhullmod_57.build = shipBuilder_build_41
    shipBuilder_buildhullmod_57.item = shipBuilder_item_34
    shipBuilder_buildhullmod_57 = importer.save_or_locate(shipBuilder_buildhullmod_57)

    shipBuilder_buildhullmod_58 = BuildHullMod()
    shipBuilder_buildhullmod_58.build = shipBuilder_build_41
    shipBuilder_buildhullmod_58.item = shipBuilder_item_35
    shipBuilder_buildhullmod_58 = importer.save_or_locate(shipBuilder_buildhullmod_58)

    shipBuilder_buildhullmod_59 = BuildHullMod()
    shipBuilder_buildhullmod_59.build = shipBuilder_build_41
    shipBuilder_buildhullmod_59.item = shipBuilder_item_37
    shipBuilder_buildhullmod_59 = importer.save_or_locate(shipBuilder_buildhullmod_59)

