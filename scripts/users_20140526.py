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

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    #initial imports

    #Processing model: Permission

    #Processing model: User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = u'pbkdf2_sha256$10000$xnOm0fg1ulnF$gHGF5Ap8epEJ3gqXcnKUejyOAqA5qJP+kPePkx7tYrw='
    auth_user_1.last_login = dateutil.parser.parse("2014-02-28T02:42:55+00:00")
    auth_user_1.is_superuser = True
    auth_user_1.username = u'agathorn'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'jwvanderbeck@gmail.com'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = dateutil.parser.parse("2013-09-07T10:02:42+00:00")
    auth_user_1 = importer.save_or_locate(auth_user_1)

    auth_user_2 = User()
    auth_user_2.password = u'pbkdf2_sha256$10000$baYmWrdhPmTU$mWpBQdWtwy+nMCcvKXNm+DbCQUCr/oivoBvGSKLGzD4='
    auth_user_2.last_login = dateutil.parser.parse("2013-09-07T11:23:59+00:00")
    auth_user_2.is_superuser = False
    auth_user_2.username = u'danredda'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.date_joined = dateutil.parser.parse("2013-09-07T11:23:58+00:00")
    auth_user_2 = importer.save_or_locate(auth_user_2)

    auth_user_3 = User()
    auth_user_3.password = u'pbkdf2_sha256$10000$fxtMeqhGed19$0FNJR6d9f3gOxDK2mVVFcvc7AuCP6frrjWadxCnY+Fk='
    auth_user_3.last_login = dateutil.parser.parse("2013-09-13T04:44:49+00:00")
    auth_user_3.is_superuser = False
    auth_user_3.username = u'erickpasta'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.is_staff = False
    auth_user_3.is_active = True
    auth_user_3.date_joined = dateutil.parser.parse("2013-09-07T11:26:28+00:00")
    auth_user_3 = importer.save_or_locate(auth_user_3)

    auth_user_4 = User()
    auth_user_4.password = u'pbkdf2_sha256$10000$Tg7nYHkLz5Ko$Jkxq4xDaDxCeDPFLAyNArO4E2Pb5qRPUiKWjemqbWUE='
    auth_user_4.last_login = dateutil.parser.parse("2013-09-07T17:59:30+00:00")
    auth_user_4.is_superuser = False
    auth_user_4.username = u'ColMustang'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.is_staff = False
    auth_user_4.is_active = True
    auth_user_4.date_joined = dateutil.parser.parse("2013-09-07T17:59:30+00:00")
    auth_user_4 = importer.save_or_locate(auth_user_4)

    auth_user_5 = User()
    auth_user_5.password = u'pbkdf2_sha256$10000$mcqXny0QsvGH$aPoFTEMTtMomVIAq1t9FroRopIBGOAwj1a3gqr919KY='
    auth_user_5.last_login = dateutil.parser.parse("2013-09-07T18:08:32+00:00")
    auth_user_5.is_superuser = False
    auth_user_5.username = u'xrail'
    auth_user_5.first_name = u''
    auth_user_5.last_name = u''
    auth_user_5.email = u''
    auth_user_5.is_staff = False
    auth_user_5.is_active = True
    auth_user_5.date_joined = dateutil.parser.parse("2013-09-07T18:08:32+00:00")
    auth_user_5 = importer.save_or_locate(auth_user_5)

    auth_user_6 = User()
    auth_user_6.password = u'pbkdf2_sha256$10000$kEPUBxia8o38$l9FhgLzaOcr6XO4q8hTbRWDQWkVqq+wVFo8QVppq7u8='
    auth_user_6.last_login = dateutil.parser.parse("2013-09-07T21:21:42+00:00")
    auth_user_6.is_superuser = False
    auth_user_6.username = u'arioch'
    auth_user_6.first_name = u''
    auth_user_6.last_name = u''
    auth_user_6.email = u''
    auth_user_6.is_staff = False
    auth_user_6.is_active = True
    auth_user_6.date_joined = dateutil.parser.parse("2013-09-07T21:21:42+00:00")
    auth_user_6 = importer.save_or_locate(auth_user_6)

    auth_user_7 = User()
    auth_user_7.password = u'pbkdf2_sha256$10000$R2GyhSf24OKb$PN/hS+INCZ1rlwXXIQRYh8+efA/EEpST48rW3ad7FQ4='
    auth_user_7.last_login = dateutil.parser.parse("2013-09-13T22:14:53+00:00")
    auth_user_7.is_superuser = False
    auth_user_7.username = u'Damo'
    auth_user_7.first_name = u''
    auth_user_7.last_name = u''
    auth_user_7.email = u''
    auth_user_7.is_staff = False
    auth_user_7.is_active = True
    auth_user_7.date_joined = dateutil.parser.parse("2013-09-07T21:59:45+00:00")
    auth_user_7 = importer.save_or_locate(auth_user_7)

    auth_user_8 = User()
    auth_user_8.password = u'pbkdf2_sha256$10000$1RTc7oYxnxXa$alwqSm1bSoN4TtwpiTtLIUo09MbMOGodSl8dFDobh/U='
    auth_user_8.last_login = dateutil.parser.parse("2013-09-08T02:11:47+00:00")
    auth_user_8.is_superuser = False
    auth_user_8.username = u'Anon6_Wolfie'
    auth_user_8.first_name = u''
    auth_user_8.last_name = u''
    auth_user_8.email = u''
    auth_user_8.is_staff = False
    auth_user_8.is_active = True
    auth_user_8.date_joined = dateutil.parser.parse("2013-09-08T02:11:47+00:00")
    auth_user_8 = importer.save_or_locate(auth_user_8)

    auth_user_9 = User()
    auth_user_9.password = u'pbkdf2_sha256$10000$a0kzXkLoBUQG$UDJ4Az8lhkHIWrcRkp2ixfzMt1j8C8LLRmi4W0devPc='
    auth_user_9.last_login = dateutil.parser.parse("2013-09-08T02:46:11+00:00")
    auth_user_9.is_superuser = False
    auth_user_9.username = u'Raven'
    auth_user_9.first_name = u''
    auth_user_9.last_name = u''
    auth_user_9.email = u''
    auth_user_9.is_staff = False
    auth_user_9.is_active = True
    auth_user_9.date_joined = dateutil.parser.parse("2013-09-08T02:46:11+00:00")
    auth_user_9 = importer.save_or_locate(auth_user_9)

    auth_user_10 = User()
    auth_user_10.password = u'pbkdf2_sha256$10000$jlzKCNs7917B$hBn1bzjeiq6t/MeE8Qe9iSV0NL7e3OQNGQkE9e8QpOc='
    auth_user_10.last_login = dateutil.parser.parse("2013-09-08T03:07:24+00:00")
    auth_user_10.is_superuser = False
    auth_user_10.username = u'Kafelnikov'
    auth_user_10.first_name = u''
    auth_user_10.last_name = u''
    auth_user_10.email = u''
    auth_user_10.is_staff = False
    auth_user_10.is_active = True
    auth_user_10.date_joined = dateutil.parser.parse("2013-09-08T03:07:24+00:00")
    auth_user_10 = importer.save_or_locate(auth_user_10)

    auth_user_11 = User()
    auth_user_11.password = u'pbkdf2_sha256$10000$OsrUmoUXladl$qBXaUxAwTw+l1Noi5Tm9kDMQ+AKgiTSvwYdrtHjoDzY='
    auth_user_11.last_login = dateutil.parser.parse("2013-09-09T04:23:45+00:00")
    auth_user_11.is_superuser = False
    auth_user_11.username = u'Villaovi'
    auth_user_11.first_name = u''
    auth_user_11.last_name = u''
    auth_user_11.email = u''
    auth_user_11.is_staff = False
    auth_user_11.is_active = True
    auth_user_11.date_joined = dateutil.parser.parse("2013-09-09T04:23:45+00:00")
    auth_user_11 = importer.save_or_locate(auth_user_11)

    auth_user_12 = User()
    auth_user_12.password = u'pbkdf2_sha256$10000$uVD9wFG42PNH$2mUMSlQG35j8RN62g/X9d3QNM9anHGYVLtoR16LIMc0='
    auth_user_12.last_login = dateutil.parser.parse("2013-09-09T06:57:30+00:00")
    auth_user_12.is_superuser = False
    auth_user_12.username = u'moofie'
    auth_user_12.first_name = u''
    auth_user_12.last_name = u''
    auth_user_12.email = u''
    auth_user_12.is_staff = False
    auth_user_12.is_active = True
    auth_user_12.date_joined = dateutil.parser.parse("2013-09-09T06:57:30+00:00")
    auth_user_12 = importer.save_or_locate(auth_user_12)

    auth_user_13 = User()
    auth_user_13.password = u'pbkdf2_sha256$10000$dxI6v3sFCmNb$7x4MsoGWm25sIAFiA5jJJmgjDVq4KWZC0WgR/K1rvic='
    auth_user_13.last_login = dateutil.parser.parse("2013-09-09T09:53:13+00:00")
    auth_user_13.is_superuser = False
    auth_user_13.username = u'max thorn'
    auth_user_13.first_name = u''
    auth_user_13.last_name = u''
    auth_user_13.email = u''
    auth_user_13.is_staff = False
    auth_user_13.is_active = True
    auth_user_13.date_joined = dateutil.parser.parse("2013-09-09T09:53:13+00:00")
    auth_user_13 = importer.save_or_locate(auth_user_13)

    auth_user_14 = User()
    auth_user_14.password = u'pbkdf2_sha256$10000$PoAtlc2o7P8l$o5p4G3Co0a0iZU4/p19a298UDZKvMjtEfGTENtUNkrk='
    auth_user_14.last_login = dateutil.parser.parse("2013-09-10T06:49:27+00:00")
    auth_user_14.is_superuser = False
    auth_user_14.username = u'Menthro05'
    auth_user_14.first_name = u''
    auth_user_14.last_name = u''
    auth_user_14.email = u''
    auth_user_14.is_staff = False
    auth_user_14.is_active = True
    auth_user_14.date_joined = dateutil.parser.parse("2013-09-10T06:49:27+00:00")
    auth_user_14 = importer.save_or_locate(auth_user_14)

    auth_user_15 = User()
    auth_user_15.password = u'pbkdf2_sha256$10000$faNZAqNhNgON$1izpu6hwaULvj/Co+Y30Pl8w4FPADOyhJcDjXMcPE44='
    auth_user_15.last_login = dateutil.parser.parse("2013-09-10T07:02:09+00:00")
    auth_user_15.is_superuser = False
    auth_user_15.username = u'Phredco'
    auth_user_15.first_name = u''
    auth_user_15.last_name = u''
    auth_user_15.email = u''
    auth_user_15.is_staff = False
    auth_user_15.is_active = True
    auth_user_15.date_joined = dateutil.parser.parse("2013-09-10T07:02:09+00:00")
    auth_user_15 = importer.save_or_locate(auth_user_15)

    auth_user_16 = User()
    auth_user_16.password = u'pbkdf2_sha256$10000$DAxj3Hv8OySi$UU6wE5MbHuFdGe3hUhCSh5Pf+0DWJX+8Ct8RBSUfLpA='
    auth_user_16.last_login = dateutil.parser.parse("2013-09-10T09:21:52+00:00")
    auth_user_16.is_superuser = False
    auth_user_16.username = u'Di Tar'
    auth_user_16.first_name = u''
    auth_user_16.last_name = u''
    auth_user_16.email = u''
    auth_user_16.is_staff = False
    auth_user_16.is_active = True
    auth_user_16.date_joined = dateutil.parser.parse("2013-09-10T09:21:25+00:00")
    auth_user_16 = importer.save_or_locate(auth_user_16)

    auth_user_17 = User()
    auth_user_17.password = u'pbkdf2_sha256$10000$GGxu5wV5sQgN$YkkB3QI/IqFMpN/N/AX8Xr50ny5dmk3J7B4pjxyfxQM='
    auth_user_17.last_login = dateutil.parser.parse("2013-09-10T19:55:03+00:00")
    auth_user_17.is_superuser = False
    auth_user_17.username = u'mhe'
    auth_user_17.first_name = u''
    auth_user_17.last_name = u''
    auth_user_17.email = u''
    auth_user_17.is_staff = False
    auth_user_17.is_active = True
    auth_user_17.date_joined = dateutil.parser.parse("2013-09-10T19:55:03+00:00")
    auth_user_17 = importer.save_or_locate(auth_user_17)

    auth_user_18 = User()
    auth_user_18.password = u'pbkdf2_sha256$10000$oU9H0GRMEve2$p5vSK7n813H/9jAhTz6T2dIiqbfYeEh1qfy2zIcsOR8='
    auth_user_18.last_login = dateutil.parser.parse("2013-10-12T22:17:28+00:00")
    auth_user_18.is_superuser = False
    auth_user_18.username = u'Siege'
    auth_user_18.first_name = u''
    auth_user_18.last_name = u''
    auth_user_18.email = u''
    auth_user_18.is_staff = False
    auth_user_18.is_active = True
    auth_user_18.date_joined = dateutil.parser.parse("2013-09-11T18:00:00+00:00")
    auth_user_18 = importer.save_or_locate(auth_user_18)

    auth_user_19 = User()
    auth_user_19.password = u'pbkdf2_sha256$10000$bJYwxIeAMmIH$v4M3IPlyR3eg3PI3CyK6zuMZ22qBM/JLMEE9G/8QNAs='
    auth_user_19.last_login = dateutil.parser.parse("2013-09-11T22:06:28+00:00")
    auth_user_19.is_superuser = False
    auth_user_19.username = u'dbennette'
    auth_user_19.first_name = u''
    auth_user_19.last_name = u''
    auth_user_19.email = u''
    auth_user_19.is_staff = False
    auth_user_19.is_active = True
    auth_user_19.date_joined = dateutil.parser.parse("2013-09-11T22:06:28+00:00")
    auth_user_19 = importer.save_or_locate(auth_user_19)

    auth_user_20 = User()
    auth_user_20.password = u'pbkdf2_sha256$10000$1mPfPZdArnki$aEUod7bqSuBvWYXTMkkyYDCfQxf9vOXny+pwzTgY2OM='
    auth_user_20.last_login = dateutil.parser.parse("2013-11-07T08:22:20+00:00")
    auth_user_20.is_superuser = False
    auth_user_20.username = u'Cryptikality'
    auth_user_20.first_name = u''
    auth_user_20.last_name = u''
    auth_user_20.email = u''
    auth_user_20.is_staff = False
    auth_user_20.is_active = True
    auth_user_20.date_joined = dateutil.parser.parse("2013-09-12T06:41:51+00:00")
    auth_user_20 = importer.save_or_locate(auth_user_20)

    auth_user_21 = User()
    auth_user_21.password = u'pbkdf2_sha256$10000$Zo9up7LxNXKZ$Go3gmFwbjanSC7tQk5xIv4MGESZ62BraFnnkfFBLBRs='
    auth_user_21.last_login = dateutil.parser.parse("2013-09-12T21:23:19+00:00")
    auth_user_21.is_superuser = False
    auth_user_21.username = u'Bohbo'
    auth_user_21.first_name = u''
    auth_user_21.last_name = u''
    auth_user_21.email = u''
    auth_user_21.is_staff = False
    auth_user_21.is_active = True
    auth_user_21.date_joined = dateutil.parser.parse("2013-09-12T21:23:19+00:00")
    auth_user_21 = importer.save_or_locate(auth_user_21)

    auth_user_22 = User()
    auth_user_22.password = u'pbkdf2_sha256$10000$wtkpVdEfEtVk$laVcKM5G5nAOoC8xpC4kmzQz/6pQbkdzuAiQ0heZqFU='
    auth_user_22.last_login = dateutil.parser.parse("2013-09-13T03:56:41+00:00")
    auth_user_22.is_superuser = False
    auth_user_22.username = u'Athanasius'
    auth_user_22.first_name = u''
    auth_user_22.last_name = u''
    auth_user_22.email = u''
    auth_user_22.is_staff = False
    auth_user_22.is_active = True
    auth_user_22.date_joined = dateutil.parser.parse("2013-09-13T03:56:41+00:00")
    auth_user_22 = importer.save_or_locate(auth_user_22)

    auth_user_23 = User()
    auth_user_23.password = u'pbkdf2_sha256$10000$I2AhXEXdHfTK$y1wlXYzUEq4toLNDetTRSRXfc1mOsYa+4UCtrT8040E='
    auth_user_23.last_login = dateutil.parser.parse("2013-09-13T04:10:25+00:00")
    auth_user_23.is_superuser = False
    auth_user_23.username = u'Kean96'
    auth_user_23.first_name = u''
    auth_user_23.last_name = u''
    auth_user_23.email = u''
    auth_user_23.is_staff = False
    auth_user_23.is_active = True
    auth_user_23.date_joined = dateutil.parser.parse("2013-09-13T04:10:24+00:00")
    auth_user_23 = importer.save_or_locate(auth_user_23)

    auth_user_24 = User()
    auth_user_24.password = u'pbkdf2_sha256$10000$WKvGnyQXirxC$j6/sW9hOm79LXvUbS9RoUex4BIAvfeitHJ6iC+1R5/A='
    auth_user_24.last_login = dateutil.parser.parse("2013-09-13T04:19:41+00:00")
    auth_user_24.is_superuser = False
    auth_user_24.username = u'Silveryn1313'
    auth_user_24.first_name = u''
    auth_user_24.last_name = u''
    auth_user_24.email = u''
    auth_user_24.is_staff = False
    auth_user_24.is_active = True
    auth_user_24.date_joined = dateutil.parser.parse("2013-09-13T04:19:40+00:00")
    auth_user_24 = importer.save_or_locate(auth_user_24)

    auth_user_25 = User()
    auth_user_25.password = u'pbkdf2_sha256$10000$eAuQOR7fUAt7$k7xyNVDyEIWbHkb+EbPr79FcCbncDM0DjJzgbWUrNv0='
    auth_user_25.last_login = dateutil.parser.parse("2013-09-13T04:23:48+00:00")
    auth_user_25.is_superuser = False
    auth_user_25.username = u'Cyber556'
    auth_user_25.first_name = u''
    auth_user_25.last_name = u''
    auth_user_25.email = u''
    auth_user_25.is_staff = False
    auth_user_25.is_active = True
    auth_user_25.date_joined = dateutil.parser.parse("2013-09-13T04:23:48+00:00")
    auth_user_25 = importer.save_or_locate(auth_user_25)

    auth_user_26 = User()
    auth_user_26.password = u'pbkdf2_sha256$10000$JWp5EcMVdhjJ$55tASQ/5ND3nGbW/j5CShdvYye0k8e5h+0QuFuuBkXw='
    auth_user_26.last_login = dateutil.parser.parse("2013-09-13T04:31:10+00:00")
    auth_user_26.is_superuser = False
    auth_user_26.username = u'silvock'
    auth_user_26.first_name = u''
    auth_user_26.last_name = u''
    auth_user_26.email = u''
    auth_user_26.is_staff = False
    auth_user_26.is_active = True
    auth_user_26.date_joined = dateutil.parser.parse("2013-09-13T04:31:10+00:00")
    auth_user_26 = importer.save_or_locate(auth_user_26)

    auth_user_27 = User()
    auth_user_27.password = u'pbkdf2_sha256$10000$51hduLR3Riod$wokIbLB7DBt6ByGogr/23FjjKn9mZq3oUcfrs6gGrlA='
    auth_user_27.last_login = dateutil.parser.parse("2013-09-13T04:43:04+00:00")
    auth_user_27.is_superuser = False
    auth_user_27.username = u'DC5102916'
    auth_user_27.first_name = u''
    auth_user_27.last_name = u''
    auth_user_27.email = u''
    auth_user_27.is_staff = False
    auth_user_27.is_active = True
    auth_user_27.date_joined = dateutil.parser.parse("2013-09-13T04:43:04+00:00")
    auth_user_27 = importer.save_or_locate(auth_user_27)

    auth_user_28 = User()
    auth_user_28.password = u'pbkdf2_sha256$10000$5BrM3RRxrrdV$dDYgGSlhNCxmi4iCMC6Jp6+Heldxj8/jz/lDZvHvdho='
    auth_user_28.last_login = dateutil.parser.parse("2013-09-13T04:51:35+00:00")
    auth_user_28.is_superuser = False
    auth_user_28.username = u'pancakemaster808'
    auth_user_28.first_name = u''
    auth_user_28.last_name = u''
    auth_user_28.email = u''
    auth_user_28.is_staff = False
    auth_user_28.is_active = True
    auth_user_28.date_joined = dateutil.parser.parse("2013-09-13T04:51:35+00:00")
    auth_user_28 = importer.save_or_locate(auth_user_28)

    auth_user_29 = User()
    auth_user_29.password = u'pbkdf2_sha256$10000$dUB84mLRgKqJ$zLkzYa6RmPDtPW4oNsXlAjQXr0Ha11uwd8Dl01zCrRA='
    auth_user_29.last_login = dateutil.parser.parse("2013-09-13T05:02:02+00:00")
    auth_user_29.is_superuser = False
    auth_user_29.username = u'Stat8iS'
    auth_user_29.first_name = u''
    auth_user_29.last_name = u''
    auth_user_29.email = u''
    auth_user_29.is_staff = False
    auth_user_29.is_active = True
    auth_user_29.date_joined = dateutil.parser.parse("2013-09-13T05:02:01+00:00")
    auth_user_29 = importer.save_or_locate(auth_user_29)

    auth_user_30 = User()
    auth_user_30.password = u'pbkdf2_sha256$10000$PcmOkImIpN24$+oDDmldkrJkJi25EJbY/MyjXCJB3hE2ve78z23mrbSc='
    auth_user_30.last_login = dateutil.parser.parse("2013-09-13T05:02:08+00:00")
    auth_user_30.is_superuser = False
    auth_user_30.username = u'RutgerM'
    auth_user_30.first_name = u''
    auth_user_30.last_name = u''
    auth_user_30.email = u''
    auth_user_30.is_staff = False
    auth_user_30.is_active = True
    auth_user_30.date_joined = dateutil.parser.parse("2013-09-13T05:02:08+00:00")
    auth_user_30 = importer.save_or_locate(auth_user_30)

    auth_user_31 = User()
    auth_user_31.password = u'pbkdf2_sha256$10000$m3td1qxYqglD$hILXVztCihYfLb763SRE8GJgBn9y8VdiTHptkG1O4nY='
    auth_user_31.last_login = dateutil.parser.parse("2013-09-13T05:04:59+00:00")
    auth_user_31.is_superuser = False
    auth_user_31.username = u'kaelnovar'
    auth_user_31.first_name = u''
    auth_user_31.last_name = u''
    auth_user_31.email = u''
    auth_user_31.is_staff = False
    auth_user_31.is_active = True
    auth_user_31.date_joined = dateutil.parser.parse("2013-09-13T05:04:59+00:00")
    auth_user_31 = importer.save_or_locate(auth_user_31)

    auth_user_32 = User()
    auth_user_32.password = u'pbkdf2_sha256$10000$l4uFdA9ih2RF$8RGet8b4gAAAH214Dc2vzb4m6tqBa8MB8iNDaWpyxqY='
    auth_user_32.last_login = dateutil.parser.parse("2013-09-13T05:12:21+00:00")
    auth_user_32.is_superuser = False
    auth_user_32.username = u'i3ullit'
    auth_user_32.first_name = u''
    auth_user_32.last_name = u''
    auth_user_32.email = u''
    auth_user_32.is_staff = False
    auth_user_32.is_active = True
    auth_user_32.date_joined = dateutil.parser.parse("2013-09-13T05:12:21+00:00")
    auth_user_32 = importer.save_or_locate(auth_user_32)

    auth_user_33 = User()
    auth_user_33.password = u'pbkdf2_sha256$10000$5Hgu3ICNNfW0$vRZrJrveEW8xNBUkNhO62gCFKmezqUpKE/99IobrcZk='
    auth_user_33.last_login = dateutil.parser.parse("2013-09-13T05:44:13+00:00")
    auth_user_33.is_superuser = False
    auth_user_33.username = u'longbow656'
    auth_user_33.first_name = u''
    auth_user_33.last_name = u''
    auth_user_33.email = u''
    auth_user_33.is_staff = False
    auth_user_33.is_active = True
    auth_user_33.date_joined = dateutil.parser.parse("2013-09-13T05:13:06+00:00")
    auth_user_33 = importer.save_or_locate(auth_user_33)

    auth_user_34 = User()
    auth_user_34.password = u'pbkdf2_sha256$10000$6p3maqsbNwjC$95zfHvm5no0ZT2VvsoyVnBtp9FaODc8XI90rFA4R4Hw='
    auth_user_34.last_login = dateutil.parser.parse("2013-09-13T05:25:18+00:00")
    auth_user_34.is_superuser = False
    auth_user_34.username = u'Othelious'
    auth_user_34.first_name = u''
    auth_user_34.last_name = u''
    auth_user_34.email = u''
    auth_user_34.is_staff = False
    auth_user_34.is_active = True
    auth_user_34.date_joined = dateutil.parser.parse("2013-09-13T05:25:18+00:00")
    auth_user_34 = importer.save_or_locate(auth_user_34)

    auth_user_35 = User()
    auth_user_35.password = u'pbkdf2_sha256$10000$TfYVYMnoBCfv$57lsNd1NBbnwkeFiVKGl8KtQqZFPZrnGP+Xqk2S8854='
    auth_user_35.last_login = dateutil.parser.parse("2013-09-13T05:34:48+00:00")
    auth_user_35.is_superuser = False
    auth_user_35.username = u'kmav101'
    auth_user_35.first_name = u''
    auth_user_35.last_name = u''
    auth_user_35.email = u''
    auth_user_35.is_staff = False
    auth_user_35.is_active = True
    auth_user_35.date_joined = dateutil.parser.parse("2013-09-13T05:34:48+00:00")
    auth_user_35 = importer.save_or_locate(auth_user_35)

    auth_user_36 = User()
    auth_user_36.password = u'pbkdf2_sha256$10000$MdPz7EHx7THY$3gCh+Tpoftdbvl9cPE7yspUC/PEo+J3kmcPU/Qn/uZo='
    auth_user_36.last_login = dateutil.parser.parse("2013-09-13T05:42:32+00:00")
    auth_user_36.is_superuser = False
    auth_user_36.username = u'SubSpace666'
    auth_user_36.first_name = u''
    auth_user_36.last_name = u''
    auth_user_36.email = u''
    auth_user_36.is_staff = False
    auth_user_36.is_active = True
    auth_user_36.date_joined = dateutil.parser.parse("2013-09-13T05:42:32+00:00")
    auth_user_36 = importer.save_or_locate(auth_user_36)

    auth_user_37 = User()
    auth_user_37.password = u'pbkdf2_sha256$10000$MbJdUX46ardE$qkDTUlxRkyTsf6JNzX2hXRXDvoDqTllSi4i07MQp/J4='
    auth_user_37.last_login = dateutil.parser.parse("2013-09-13T05:54:09+00:00")
    auth_user_37.is_superuser = False
    auth_user_37.username = u'Leu'
    auth_user_37.first_name = u''
    auth_user_37.last_name = u''
    auth_user_37.email = u''
    auth_user_37.is_staff = False
    auth_user_37.is_active = True
    auth_user_37.date_joined = dateutil.parser.parse("2013-09-13T05:54:09+00:00")
    auth_user_37 = importer.save_or_locate(auth_user_37)

    auth_user_38 = User()
    auth_user_38.password = u'pbkdf2_sha256$10000$3Y6N1PDuDvj3$omgY3T+TAQYcZ/RPEYVFHbpHPkkkqVrVTpNFDtdVGSI='
    auth_user_38.last_login = dateutil.parser.parse("2013-09-13T05:56:00+00:00")
    auth_user_38.is_superuser = False
    auth_user_38.username = u'LethalInterjection'
    auth_user_38.first_name = u''
    auth_user_38.last_name = u''
    auth_user_38.email = u''
    auth_user_38.is_staff = False
    auth_user_38.is_active = True
    auth_user_38.date_joined = dateutil.parser.parse("2013-09-13T05:56:00+00:00")
    auth_user_38 = importer.save_or_locate(auth_user_38)

    auth_user_39 = User()
    auth_user_39.password = u'pbkdf2_sha256$10000$Lk4A1S6qMewU$lIPCQeZS0XpA37/6B/BCQItyl/oN/ouDKHGiuNc5Glw='
    auth_user_39.last_login = dateutil.parser.parse("2013-09-13T05:59:39+00:00")
    auth_user_39.is_superuser = False
    auth_user_39.username = u'Thomas-Blood'
    auth_user_39.first_name = u''
    auth_user_39.last_name = u''
    auth_user_39.email = u''
    auth_user_39.is_staff = False
    auth_user_39.is_active = True
    auth_user_39.date_joined = dateutil.parser.parse("2013-09-13T05:59:39+00:00")
    auth_user_39 = importer.save_or_locate(auth_user_39)

    auth_user_40 = User()
    auth_user_40.password = u'pbkdf2_sha256$10000$4wsmr5Xdm0uo$Fn3QyHA7ehGnXR0Ov9GG4jwqmPrxVOtt6TaKBCQ0TIY='
    auth_user_40.last_login = dateutil.parser.parse("2013-09-13T06:10:50+00:00")
    auth_user_40.is_superuser = False
    auth_user_40.username = u'Tzet'
    auth_user_40.first_name = u''
    auth_user_40.last_name = u''
    auth_user_40.email = u''
    auth_user_40.is_staff = False
    auth_user_40.is_active = True
    auth_user_40.date_joined = dateutil.parser.parse("2013-09-13T06:10:50+00:00")
    auth_user_40 = importer.save_or_locate(auth_user_40)

    auth_user_41 = User()
    auth_user_41.password = u'pbkdf2_sha256$10000$qmBe9nttHl7U$7YlFQy22ur0Vv/76dMbkLLerWF18f1dmCYkVj8R4Jv0='
    auth_user_41.last_login = dateutil.parser.parse("2013-09-13T06:23:04+00:00")
    auth_user_41.is_superuser = False
    auth_user_41.username = u'Nev3rmor3'
    auth_user_41.first_name = u''
    auth_user_41.last_name = u''
    auth_user_41.email = u''
    auth_user_41.is_staff = False
    auth_user_41.is_active = True
    auth_user_41.date_joined = dateutil.parser.parse("2013-09-13T06:22:57+00:00")
    auth_user_41 = importer.save_or_locate(auth_user_41)

    auth_user_42 = User()
    auth_user_42.password = u'pbkdf2_sha256$10000$ynba1WNtnY4o$SW2wgC3swxBhUb2qPMMOdtheYyC7G45xGxXwgyV+aTU='
    auth_user_42.last_login = dateutil.parser.parse("2013-09-13T06:23:11+00:00")
    auth_user_42.is_superuser = False
    auth_user_42.username = u'Zrail'
    auth_user_42.first_name = u''
    auth_user_42.last_name = u''
    auth_user_42.email = u''
    auth_user_42.is_staff = False
    auth_user_42.is_active = True
    auth_user_42.date_joined = dateutil.parser.parse("2013-09-13T06:23:10+00:00")
    auth_user_42 = importer.save_or_locate(auth_user_42)

    auth_user_43 = User()
    auth_user_43.password = u'pbkdf2_sha256$10000$agq19DUMrV92$WO+aqrJDrWGq01cfzgjYF8gHGLr/+22n4OZxyRV6UHc='
    auth_user_43.last_login = dateutil.parser.parse("2013-09-13T06:35:49+00:00")
    auth_user_43.is_superuser = False
    auth_user_43.username = u'dapperry14'
    auth_user_43.first_name = u''
    auth_user_43.last_name = u''
    auth_user_43.email = u''
    auth_user_43.is_staff = False
    auth_user_43.is_active = True
    auth_user_43.date_joined = dateutil.parser.parse("2013-09-13T06:35:49+00:00")
    auth_user_43 = importer.save_or_locate(auth_user_43)

    auth_user_44 = User()
    auth_user_44.password = u'pbkdf2_sha256$10000$5gHM6hNpsn54$v35VoYqoMwLqACnPHSfSWRfKfPygOPmyd3mFNdZnYgQ='
    auth_user_44.last_login = dateutil.parser.parse("2013-09-13T06:44:19+00:00")
    auth_user_44.is_superuser = False
    auth_user_44.username = u'awev'
    auth_user_44.first_name = u''
    auth_user_44.last_name = u''
    auth_user_44.email = u''
    auth_user_44.is_staff = False
    auth_user_44.is_active = True
    auth_user_44.date_joined = dateutil.parser.parse("2013-09-13T06:44:19+00:00")
    auth_user_44 = importer.save_or_locate(auth_user_44)

    auth_user_45 = User()
    auth_user_45.password = u'pbkdf2_sha256$10000$oWs1ukDG2PcJ$bzQRKZ1ZJy/cSfR3nV2rJ6jWzg66vdA/5NDCuZhweKU='
    auth_user_45.last_login = dateutil.parser.parse("2013-09-13T06:50:36+00:00")
    auth_user_45.is_superuser = False
    auth_user_45.username = u'durron'
    auth_user_45.first_name = u''
    auth_user_45.last_name = u''
    auth_user_45.email = u''
    auth_user_45.is_staff = False
    auth_user_45.is_active = True
    auth_user_45.date_joined = dateutil.parser.parse("2013-09-13T06:50:35+00:00")
    auth_user_45 = importer.save_or_locate(auth_user_45)

    auth_user_46 = User()
    auth_user_46.password = u'pbkdf2_sha256$10000$dfg5Zn12LkhT$FD8qCW+hcpv2sIzT+2zfm8LD+LSgMeSkpDkAMrJcshw='
    auth_user_46.last_login = dateutil.parser.parse("2013-09-13T08:04:32+00:00")
    auth_user_46.is_superuser = False
    auth_user_46.username = u'Delta26'
    auth_user_46.first_name = u''
    auth_user_46.last_name = u''
    auth_user_46.email = u''
    auth_user_46.is_staff = False
    auth_user_46.is_active = True
    auth_user_46.date_joined = dateutil.parser.parse("2013-09-13T08:04:31+00:00")
    auth_user_46 = importer.save_or_locate(auth_user_46)

    auth_user_47 = User()
    auth_user_47.password = u'pbkdf2_sha256$10000$v31WEAOz7tVm$tomWvMWgP/1Dedc6Gxj6vLVw6VV4sSsJm417iIu3Aqc='
    auth_user_47.last_login = dateutil.parser.parse("2013-09-13T08:23:55+00:00")
    auth_user_47.is_superuser = False
    auth_user_47.username = u'Shanigami'
    auth_user_47.first_name = u''
    auth_user_47.last_name = u''
    auth_user_47.email = u''
    auth_user_47.is_staff = False
    auth_user_47.is_active = True
    auth_user_47.date_joined = dateutil.parser.parse("2013-09-13T08:23:55+00:00")
    auth_user_47 = importer.save_or_locate(auth_user_47)

    auth_user_48 = User()
    auth_user_48.password = u'pbkdf2_sha256$10000$MXQDQQgLmM3o$Bguhf05NtlH4PmNlxfixaDmqDC8W0HNDgXX6oBvr1RQ='
    auth_user_48.last_login = dateutil.parser.parse("2013-09-13T08:48:20+00:00")
    auth_user_48.is_superuser = False
    auth_user_48.username = u'someguy24'
    auth_user_48.first_name = u''
    auth_user_48.last_name = u''
    auth_user_48.email = u''
    auth_user_48.is_staff = False
    auth_user_48.is_active = True
    auth_user_48.date_joined = dateutil.parser.parse("2013-09-13T08:48:20+00:00")
    auth_user_48 = importer.save_or_locate(auth_user_48)

    auth_user_49 = User()
    auth_user_49.password = u'pbkdf2_sha256$10000$RkpK08ay6pJ3$+p2jyPfFb3153p3f0GF+clP6FNyZ8g67wQByVi56Y5s='
    auth_user_49.last_login = dateutil.parser.parse("2013-09-13T08:49:50+00:00")
    auth_user_49.is_superuser = False
    auth_user_49.username = u'Shire_Folk'
    auth_user_49.first_name = u''
    auth_user_49.last_name = u''
    auth_user_49.email = u''
    auth_user_49.is_staff = False
    auth_user_49.is_active = True
    auth_user_49.date_joined = dateutil.parser.parse("2013-09-13T08:49:50+00:00")
    auth_user_49 = importer.save_or_locate(auth_user_49)

    auth_user_50 = User()
    auth_user_50.password = u'pbkdf2_sha256$10000$j0ENAIm3FPa3$t9KHL8+e7MTGpTusI7hbga1wYyVPRjkgF3wgM6+f0WM='
    auth_user_50.last_login = dateutil.parser.parse("2013-09-13T09:00:33+00:00")
    auth_user_50.is_superuser = False
    auth_user_50.username = u'TheDefender'
    auth_user_50.first_name = u''
    auth_user_50.last_name = u''
    auth_user_50.email = u''
    auth_user_50.is_staff = False
    auth_user_50.is_active = True
    auth_user_50.date_joined = dateutil.parser.parse("2013-09-13T09:00:33+00:00")
    auth_user_50 = importer.save_or_locate(auth_user_50)

    auth_user_51 = User()
    auth_user_51.password = u'pbkdf2_sha256$10000$jDAAFSFEtFmC$tJosUqRrZmp4N7ybkMfdOgEELIf5VkvfgEtLO8Rv7F0='
    auth_user_51.last_login = dateutil.parser.parse("2013-09-13T09:08:04+00:00")
    auth_user_51.is_superuser = False
    auth_user_51.username = u'zib'
    auth_user_51.first_name = u''
    auth_user_51.last_name = u''
    auth_user_51.email = u''
    auth_user_51.is_staff = False
    auth_user_51.is_active = True
    auth_user_51.date_joined = dateutil.parser.parse("2013-09-13T09:08:04+00:00")
    auth_user_51 = importer.save_or_locate(auth_user_51)

    auth_user_52 = User()
    auth_user_52.password = u'pbkdf2_sha256$10000$K5hES6bshXrW$oyuCpaQeHholRsSR+jRjKJSG1IBP5oZTHIRXKw6p7oo='
    auth_user_52.last_login = dateutil.parser.parse("2013-09-13T09:43:43+00:00")
    auth_user_52.is_superuser = False
    auth_user_52.username = u'Beren_Valari'
    auth_user_52.first_name = u''
    auth_user_52.last_name = u''
    auth_user_52.email = u''
    auth_user_52.is_staff = False
    auth_user_52.is_active = True
    auth_user_52.date_joined = dateutil.parser.parse("2013-09-13T09:40:08+00:00")
    auth_user_52 = importer.save_or_locate(auth_user_52)

    auth_user_53 = User()
    auth_user_53.password = u'pbkdf2_sha256$10000$xTxFiXAuEpmW$rfKgVvl7rgZHZU1qmKoQs3gP6WTrMgbRDUAoMrM5qG8='
    auth_user_53.last_login = dateutil.parser.parse("2013-09-13T09:47:48+00:00")
    auth_user_53.is_superuser = False
    auth_user_53.username = u'Ronbocop'
    auth_user_53.first_name = u''
    auth_user_53.last_name = u''
    auth_user_53.email = u''
    auth_user_53.is_staff = False
    auth_user_53.is_active = True
    auth_user_53.date_joined = dateutil.parser.parse("2013-09-13T09:47:48+00:00")
    auth_user_53 = importer.save_or_locate(auth_user_53)

    auth_user_54 = User()
    auth_user_54.password = u'pbkdf2_sha256$10000$VJEP9FbsiLTV$cpe+GwHWcZK2nKt+ohr+g4cg7oNPBqdH4kr4f8t1+RY='
    auth_user_54.last_login = dateutil.parser.parse("2013-09-13T09:49:14+00:00")
    auth_user_54.is_superuser = False
    auth_user_54.username = u'sterley'
    auth_user_54.first_name = u''
    auth_user_54.last_name = u''
    auth_user_54.email = u''
    auth_user_54.is_staff = False
    auth_user_54.is_active = True
    auth_user_54.date_joined = dateutil.parser.parse("2013-09-13T09:49:14+00:00")
    auth_user_54 = importer.save_or_locate(auth_user_54)

    auth_user_55 = User()
    auth_user_55.password = u'pbkdf2_sha256$10000$klwPIPsPcWRG$VzUUu9EcArWj8MkjoUiboZfmwKAf9wXE5TO3ljRvzJU='
    auth_user_55.last_login = dateutil.parser.parse("2013-09-13T10:08:17+00:00")
    auth_user_55.is_superuser = False
    auth_user_55.username = u'pujinimsae'
    auth_user_55.first_name = u''
    auth_user_55.last_name = u''
    auth_user_55.email = u''
    auth_user_55.is_staff = False
    auth_user_55.is_active = True
    auth_user_55.date_joined = dateutil.parser.parse("2013-09-13T10:08:17+00:00")
    auth_user_55 = importer.save_or_locate(auth_user_55)

    auth_user_56 = User()
    auth_user_56.password = u'pbkdf2_sha256$10000$4RZUflqGDuGN$uRbHcPV/3JI3LAkdq7aFPrsIjomyCHsB5HBz9nUvRNo='
    auth_user_56.last_login = dateutil.parser.parse("2013-09-13T10:27:56+00:00")
    auth_user_56.is_superuser = False
    auth_user_56.username = u'thedraygonninja'
    auth_user_56.first_name = u''
    auth_user_56.last_name = u''
    auth_user_56.email = u''
    auth_user_56.is_staff = False
    auth_user_56.is_active = True
    auth_user_56.date_joined = dateutil.parser.parse("2013-09-13T10:27:56+00:00")
    auth_user_56 = importer.save_or_locate(auth_user_56)

    auth_user_57 = User()
    auth_user_57.password = u'pbkdf2_sha256$10000$cjkmG8w8xHTq$NJ70GtemX72MUw4yo4ywJj7EUddALUDYx25uIHRQHBs='
    auth_user_57.last_login = dateutil.parser.parse("2013-09-13T11:24:43+00:00")
    auth_user_57.is_superuser = False
    auth_user_57.username = u'DrEG'
    auth_user_57.first_name = u''
    auth_user_57.last_name = u''
    auth_user_57.email = u''
    auth_user_57.is_staff = False
    auth_user_57.is_active = True
    auth_user_57.date_joined = dateutil.parser.parse("2013-09-13T11:24:43+00:00")
    auth_user_57 = importer.save_or_locate(auth_user_57)

    auth_user_58 = User()
    auth_user_58.password = u'pbkdf2_sha256$10000$htmJfOD4pFAB$xU3lbPIaTSRnnhKjY2rA1g4mmWJO1ng84SlSZJz7BT8='
    auth_user_58.last_login = dateutil.parser.parse("2013-09-13T11:27:46+00:00")
    auth_user_58.is_superuser = False
    auth_user_58.username = u'xigunder'
    auth_user_58.first_name = u''
    auth_user_58.last_name = u''
    auth_user_58.email = u''
    auth_user_58.is_staff = False
    auth_user_58.is_active = True
    auth_user_58.date_joined = dateutil.parser.parse("2013-09-13T11:27:46+00:00")
    auth_user_58 = importer.save_or_locate(auth_user_58)

    auth_user_59 = User()
    auth_user_59.password = u'pbkdf2_sha256$10000$VGJzoKNjGlFw$dR4UgxBgZYwQ02/kq1bBuRbS9yMLf2aoU7GnOz1SdvU='
    auth_user_59.last_login = dateutil.parser.parse("2013-09-13T13:01:08+00:00")
    auth_user_59.is_superuser = False
    auth_user_59.username = u'Harphy'
    auth_user_59.first_name = u''
    auth_user_59.last_name = u''
    auth_user_59.email = u''
    auth_user_59.is_staff = False
    auth_user_59.is_active = True
    auth_user_59.date_joined = dateutil.parser.parse("2013-09-13T13:01:08+00:00")
    auth_user_59 = importer.save_or_locate(auth_user_59)

    auth_user_60 = User()
    auth_user_60.password = u'pbkdf2_sha256$10000$au1a2wcQxR08$PZX3+aZkvFsNrPEiBnavTZOi889qW5XnuJAxJgp5myE='
    auth_user_60.last_login = dateutil.parser.parse("2013-09-13T13:25:49+00:00")
    auth_user_60.is_superuser = False
    auth_user_60.username = u'Akumaro'
    auth_user_60.first_name = u''
    auth_user_60.last_name = u''
    auth_user_60.email = u''
    auth_user_60.is_staff = False
    auth_user_60.is_active = True
    auth_user_60.date_joined = dateutil.parser.parse("2013-09-13T13:25:48+00:00")
    auth_user_60 = importer.save_or_locate(auth_user_60)

    auth_user_61 = User()
    auth_user_61.password = u'pbkdf2_sha256$10000$OR0vBfpaurCq$OqOyegtud0b8KjVziI1X58knvxxBNRIm18zKjNrmAhA='
    auth_user_61.last_login = dateutil.parser.parse("2013-09-13T13:32:08+00:00")
    auth_user_61.is_superuser = False
    auth_user_61.username = u'Beaver17'
    auth_user_61.first_name = u''
    auth_user_61.last_name = u''
    auth_user_61.email = u''
    auth_user_61.is_staff = False
    auth_user_61.is_active = True
    auth_user_61.date_joined = dateutil.parser.parse("2013-09-13T13:32:08+00:00")
    auth_user_61 = importer.save_or_locate(auth_user_61)

    auth_user_62 = User()
    auth_user_62.password = u'pbkdf2_sha256$10000$f8NRl0JFCjRS$unKNu0JYAboBJ5XHLoL8fzN2Qtch7hJZvip0sgF6VaY='
    auth_user_62.last_login = dateutil.parser.parse("2013-09-13T13:50:59+00:00")
    auth_user_62.is_superuser = False
    auth_user_62.username = u'mick4'
    auth_user_62.first_name = u''
    auth_user_62.last_name = u''
    auth_user_62.email = u''
    auth_user_62.is_staff = False
    auth_user_62.is_active = True
    auth_user_62.date_joined = dateutil.parser.parse("2013-09-13T13:50:59+00:00")
    auth_user_62 = importer.save_or_locate(auth_user_62)

    auth_user_63 = User()
    auth_user_63.password = u'pbkdf2_sha256$10000$zFo7BvUzU8bQ$Xdygg6d5U4qu25hMPhVFA1dbRVNwUnkF7uBcEF7I38k='
    auth_user_63.last_login = dateutil.parser.parse("2013-09-13T13:58:41+00:00")
    auth_user_63.is_superuser = False
    auth_user_63.username = u'BigBrutal64'
    auth_user_63.first_name = u''
    auth_user_63.last_name = u''
    auth_user_63.email = u''
    auth_user_63.is_staff = False
    auth_user_63.is_active = True
    auth_user_63.date_joined = dateutil.parser.parse("2013-09-13T13:58:41+00:00")
    auth_user_63 = importer.save_or_locate(auth_user_63)

    auth_user_64 = User()
    auth_user_64.password = u'pbkdf2_sha256$10000$UtIz7FiYOp4N$nQrTfcIGmoDBwksAhCALZ3PwhZNCvZaM9F0keW4mHeE='
    auth_user_64.last_login = dateutil.parser.parse("2013-09-26T23:02:10+00:00")
    auth_user_64.is_superuser = False
    auth_user_64.username = u'kave'
    auth_user_64.first_name = u''
    auth_user_64.last_name = u''
    auth_user_64.email = u''
    auth_user_64.is_staff = False
    auth_user_64.is_active = True
    auth_user_64.date_joined = dateutil.parser.parse("2013-09-13T15:21:58+00:00")
    auth_user_64 = importer.save_or_locate(auth_user_64)

    auth_user_65 = User()
    auth_user_65.password = u'pbkdf2_sha256$10000$VdCfX1oPdDvU$NIXSx6+qWh6TFIrmW9RyEswVJseDsAp8MvZF3XlI6rY='
    auth_user_65.last_login = dateutil.parser.parse("2013-09-13T15:27:32+00:00")
    auth_user_65.is_superuser = False
    auth_user_65.username = u'Stonka'
    auth_user_65.first_name = u''
    auth_user_65.last_name = u''
    auth_user_65.email = u''
    auth_user_65.is_staff = False
    auth_user_65.is_active = True
    auth_user_65.date_joined = dateutil.parser.parse("2013-09-13T15:27:32+00:00")
    auth_user_65 = importer.save_or_locate(auth_user_65)

    auth_user_66 = User()
    auth_user_66.password = u'pbkdf2_sha256$10000$7DX2q74h5MYR$yXE5GozAJp544igygz/WBzbiTe9uxqG2VQAtXn6i5Jo='
    auth_user_66.last_login = dateutil.parser.parse("2013-09-13T15:42:19+00:00")
    auth_user_66.is_superuser = False
    auth_user_66.username = u'Warden'
    auth_user_66.first_name = u''
    auth_user_66.last_name = u''
    auth_user_66.email = u''
    auth_user_66.is_staff = False
    auth_user_66.is_active = True
    auth_user_66.date_joined = dateutil.parser.parse("2013-09-13T15:42:19+00:00")
    auth_user_66 = importer.save_or_locate(auth_user_66)

    auth_user_67 = User()
    auth_user_67.password = u'pbkdf2_sha256$10000$1W8iPZfoIfG7$Iss0xywR6NruYkWvJOFY3oyGZy66VjoyTH7GmOoOiRA='
    auth_user_67.last_login = dateutil.parser.parse("2013-09-13T16:47:57+00:00")
    auth_user_67.is_superuser = False
    auth_user_67.username = u'Don_Minister'
    auth_user_67.first_name = u''
    auth_user_67.last_name = u''
    auth_user_67.email = u''
    auth_user_67.is_staff = False
    auth_user_67.is_active = True
    auth_user_67.date_joined = dateutil.parser.parse("2013-09-13T16:47:57+00:00")
    auth_user_67 = importer.save_or_locate(auth_user_67)

    auth_user_68 = User()
    auth_user_68.password = u'pbkdf2_sha256$10000$4tJwH7TiejuR$XuxSxyOs14286S6LS+wFTQs93Qpr42PUp34G42tR+9g='
    auth_user_68.last_login = dateutil.parser.parse("2013-11-06T05:42:24+00:00")
    auth_user_68.is_superuser = False
    auth_user_68.username = u'tamvegas'
    auth_user_68.first_name = u''
    auth_user_68.last_name = u''
    auth_user_68.email = u''
    auth_user_68.is_staff = False
    auth_user_68.is_active = True
    auth_user_68.date_joined = dateutil.parser.parse("2013-09-13T17:27:43+00:00")
    auth_user_68 = importer.save_or_locate(auth_user_68)

    auth_user_69 = User()
    auth_user_69.password = u'pbkdf2_sha256$10000$ra7D4hqbjMaD$uKksJ85hrvTrtqPy8CTOjJpfZ7Ex+3tfwEUNcOueKO0='
    auth_user_69.last_login = dateutil.parser.parse("2013-09-13T17:53:08+00:00")
    auth_user_69.is_superuser = False
    auth_user_69.username = u'Misterdelle96'
    auth_user_69.first_name = u''
    auth_user_69.last_name = u''
    auth_user_69.email = u''
    auth_user_69.is_staff = False
    auth_user_69.is_active = True
    auth_user_69.date_joined = dateutil.parser.parse("2013-09-13T17:53:08+00:00")
    auth_user_69 = importer.save_or_locate(auth_user_69)

    auth_user_70 = User()
    auth_user_70.password = u'pbkdf2_sha256$10000$1cF8SvDH75Vu$AIXC+xtJd/qMC9bZOnhRaxQ+0vAfunkWctoKjHrzaSw='
    auth_user_70.last_login = dateutil.parser.parse("2013-09-13T19:08:38+00:00")
    auth_user_70.is_superuser = False
    auth_user_70.username = u'ALoS'
    auth_user_70.first_name = u''
    auth_user_70.last_name = u''
    auth_user_70.email = u''
    auth_user_70.is_staff = False
    auth_user_70.is_active = True
    auth_user_70.date_joined = dateutil.parser.parse("2013-09-13T19:07:58+00:00")
    auth_user_70 = importer.save_or_locate(auth_user_70)

    auth_user_71 = User()
    auth_user_71.password = u'pbkdf2_sha256$10000$FpdlC7hPRuVM$b05SbNP9uqN9CDORqSysZVuUVwyt2Uv8ZB47p0RjDTE='
    auth_user_71.last_login = dateutil.parser.parse("2013-09-13T19:08:13+00:00")
    auth_user_71.is_superuser = False
    auth_user_71.username = u'nano'
    auth_user_71.first_name = u''
    auth_user_71.last_name = u''
    auth_user_71.email = u''
    auth_user_71.is_staff = False
    auth_user_71.is_active = True
    auth_user_71.date_joined = dateutil.parser.parse("2013-09-13T19:08:12+00:00")
    auth_user_71 = importer.save_or_locate(auth_user_71)

    auth_user_72 = User()
    auth_user_72.password = u'pbkdf2_sha256$10000$n4axW1aVkFr4$HH8EPXDUksOjOIcWfTbLCOnPd/Y8TcjP3AneqFvmj+I='
    auth_user_72.last_login = dateutil.parser.parse("2013-09-13T20:34:04+00:00")
    auth_user_72.is_superuser = False
    auth_user_72.username = u'Hypperzz22'
    auth_user_72.first_name = u''
    auth_user_72.last_name = u''
    auth_user_72.email = u''
    auth_user_72.is_staff = False
    auth_user_72.is_active = True
    auth_user_72.date_joined = dateutil.parser.parse("2013-09-13T20:34:03+00:00")
    auth_user_72 = importer.save_or_locate(auth_user_72)

    auth_user_73 = User()
    auth_user_73.password = u'pbkdf2_sha256$10000$KNshL6iCaoCJ$7MVoPAIckFif3FPAhXsBjIe2+YV4LSEGipwJ0bq6AUU='
    auth_user_73.last_login = dateutil.parser.parse("2013-09-13T21:55:43+00:00")
    auth_user_73.is_superuser = False
    auth_user_73.username = u'hogbola'
    auth_user_73.first_name = u''
    auth_user_73.last_name = u''
    auth_user_73.email = u''
    auth_user_73.is_staff = False
    auth_user_73.is_active = True
    auth_user_73.date_joined = dateutil.parser.parse("2013-09-13T21:32:18+00:00")
    auth_user_73 = importer.save_or_locate(auth_user_73)

    auth_user_74 = User()
    auth_user_74.password = u'pbkdf2_sha256$10000$WHMuL5ZufiSb$qMdluZlzGTnsAxjfRsnYsfkiC+vBqS+6ZQ2Gdc5EtxY='
    auth_user_74.last_login = dateutil.parser.parse("2013-09-13T21:57:04+00:00")
    auth_user_74.is_superuser = False
    auth_user_74.username = u'Lorby'
    auth_user_74.first_name = u''
    auth_user_74.last_name = u''
    auth_user_74.email = u''
    auth_user_74.is_staff = False
    auth_user_74.is_active = True
    auth_user_74.date_joined = dateutil.parser.parse("2013-09-13T21:57:04+00:00")
    auth_user_74 = importer.save_or_locate(auth_user_74)

    auth_user_75 = User()
    auth_user_75.password = u'pbkdf2_sha256$10000$NE75WsdWx5f9$ckLDXg9Qk+nfHvmc9KyEBcCmxYX9Ml1jAu0M3uL/5CM='
    auth_user_75.last_login = dateutil.parser.parse("2013-09-13T22:02:19+00:00")
    auth_user_75.is_superuser = False
    auth_user_75.username = u'LordofNaught'
    auth_user_75.first_name = u''
    auth_user_75.last_name = u''
    auth_user_75.email = u''
    auth_user_75.is_staff = False
    auth_user_75.is_active = True
    auth_user_75.date_joined = dateutil.parser.parse("2013-09-13T22:02:19+00:00")
    auth_user_75 = importer.save_or_locate(auth_user_75)

    auth_user_76 = User()
    auth_user_76.password = u'pbkdf2_sha256$10000$uq03c1wjDoKv$oJNSmna0FjHhZnNR1s2BcOGg8GJaz6wOPsBaaLCIQsE='
    auth_user_76.last_login = dateutil.parser.parse("2013-09-13T22:04:44+00:00")
    auth_user_76.is_superuser = False
    auth_user_76.username = u'Braddass'
    auth_user_76.first_name = u''
    auth_user_76.last_name = u''
    auth_user_76.email = u''
    auth_user_76.is_staff = False
    auth_user_76.is_active = True
    auth_user_76.date_joined = dateutil.parser.parse("2013-09-13T22:04:44+00:00")
    auth_user_76 = importer.save_or_locate(auth_user_76)

    auth_user_77 = User()
    auth_user_77.password = u'pbkdf2_sha256$10000$erD570Nu1iv2$jbnQt/0fDfJtc+y6VNTq2P0n+n7RK8HiLQlZvZxJNM8='
    auth_user_77.last_login = dateutil.parser.parse("2013-09-13T22:31:14+00:00")
    auth_user_77.is_superuser = False
    auth_user_77.username = u'maphughes'
    auth_user_77.first_name = u''
    auth_user_77.last_name = u''
    auth_user_77.email = u''
    auth_user_77.is_staff = False
    auth_user_77.is_active = True
    auth_user_77.date_joined = dateutil.parser.parse("2013-09-13T22:31:14+00:00")
    auth_user_77 = importer.save_or_locate(auth_user_77)

    auth_user_78 = User()
    auth_user_78.password = u'pbkdf2_sha256$10000$Ftgjc0g5VFfK$T0I6/EhQwA4zQNpZLKU8UnzAqGAwml2kKFZ0LPJW+cM='
    auth_user_78.last_login = dateutil.parser.parse("2013-09-13T23:33:57+00:00")
    auth_user_78.is_superuser = False
    auth_user_78.username = u'patback66'
    auth_user_78.first_name = u''
    auth_user_78.last_name = u''
    auth_user_78.email = u''
    auth_user_78.is_staff = False
    auth_user_78.is_active = True
    auth_user_78.date_joined = dateutil.parser.parse("2013-09-13T23:33:57+00:00")
    auth_user_78 = importer.save_or_locate(auth_user_78)

    auth_user_79 = User()
    auth_user_79.password = u'pbkdf2_sha256$10000$SffMIbFc2qR0$+2xFxpXN/Gvooko5jE8xKvZQRqXQZ0XqkQRUM1y1YeE='
    auth_user_79.last_login = dateutil.parser.parse("2013-09-14T00:45:19+00:00")
    auth_user_79.is_superuser = False
    auth_user_79.username = u'thecomputerdude'
    auth_user_79.first_name = u''
    auth_user_79.last_name = u''
    auth_user_79.email = u''
    auth_user_79.is_staff = False
    auth_user_79.is_active = True
    auth_user_79.date_joined = dateutil.parser.parse("2013-09-14T00:45:19+00:00")
    auth_user_79 = importer.save_or_locate(auth_user_79)

    auth_user_80 = User()
    auth_user_80.password = u'pbkdf2_sha256$10000$D45moN6ShSz1$Yn9/2NHOly3G4WD1E8Nb3NDCGoFa58dp5hQE9DnM2zE='
    auth_user_80.last_login = dateutil.parser.parse("2013-09-14T01:52:06+00:00")
    auth_user_80.is_superuser = False
    auth_user_80.username = u'Blorthag'
    auth_user_80.first_name = u''
    auth_user_80.last_name = u''
    auth_user_80.email = u''
    auth_user_80.is_staff = False
    auth_user_80.is_active = True
    auth_user_80.date_joined = dateutil.parser.parse("2013-09-14T01:52:05+00:00")
    auth_user_80 = importer.save_or_locate(auth_user_80)

    auth_user_81 = User()
    auth_user_81.password = u'pbkdf2_sha256$10000$wGbIdJwqBhSE$QsLJETlkH3nlLtwQUvA68hjw7iPaAquwI5pbz3hqZaQ='
    auth_user_81.last_login = dateutil.parser.parse("2013-09-14T01:54:16+00:00")
    auth_user_81.is_superuser = False
    auth_user_81.username = u'dudejmass'
    auth_user_81.first_name = u''
    auth_user_81.last_name = u''
    auth_user_81.email = u''
    auth_user_81.is_staff = False
    auth_user_81.is_active = True
    auth_user_81.date_joined = dateutil.parser.parse("2013-09-14T01:54:16+00:00")
    auth_user_81 = importer.save_or_locate(auth_user_81)

    auth_user_82 = User()
    auth_user_82.password = u'pbkdf2_sha256$10000$2ulhr465qc5g$WYCdSuK0DkCcWpcRkxyIiQ5FvJBtsbRYPNYjruubFvI='
    auth_user_82.last_login = dateutil.parser.parse("2013-09-14T03:51:50+00:00")
    auth_user_82.is_superuser = False
    auth_user_82.username = u'MrG'
    auth_user_82.first_name = u''
    auth_user_82.last_name = u''
    auth_user_82.email = u''
    auth_user_82.is_staff = False
    auth_user_82.is_active = True
    auth_user_82.date_joined = dateutil.parser.parse("2013-09-14T03:51:50+00:00")
    auth_user_82 = importer.save_or_locate(auth_user_82)

    auth_user_83 = User()
    auth_user_83.password = u'pbkdf2_sha256$10000$Oa1r1acC1zSe$GaoSGkHOTQpAdSUZcfNpmQjx/r9qh2qRo1e4lWza/AQ='
    auth_user_83.last_login = dateutil.parser.parse("2013-09-14T05:51:04+00:00")
    auth_user_83.is_superuser = False
    auth_user_83.username = u'Sathorus'
    auth_user_83.first_name = u''
    auth_user_83.last_name = u''
    auth_user_83.email = u''
    auth_user_83.is_staff = False
    auth_user_83.is_active = True
    auth_user_83.date_joined = dateutil.parser.parse("2013-09-14T05:51:04+00:00")
    auth_user_83 = importer.save_or_locate(auth_user_83)

    auth_user_84 = User()
    auth_user_84.password = u'pbkdf2_sha256$10000$0Infseet8AaE$gQBTTFEeVt0MxNR1cMpKjXiWcZQnm9MeTk3NjfUDenM='
    auth_user_84.last_login = dateutil.parser.parse("2013-09-14T06:30:07+00:00")
    auth_user_84.is_superuser = False
    auth_user_84.username = u'TheGreymane'
    auth_user_84.first_name = u''
    auth_user_84.last_name = u''
    auth_user_84.email = u''
    auth_user_84.is_staff = False
    auth_user_84.is_active = True
    auth_user_84.date_joined = dateutil.parser.parse("2013-09-14T06:30:07+00:00")
    auth_user_84 = importer.save_or_locate(auth_user_84)

    auth_user_85 = User()
    auth_user_85.password = u'pbkdf2_sha256$10000$mj38n9nFJKpq$63IXTPy0FrZROahRJuJWRl5bPoH6shdUBWRZfv1exkI='
    auth_user_85.last_login = dateutil.parser.parse("2013-09-14T07:42:55+00:00")
    auth_user_85.is_superuser = False
    auth_user_85.username = u'moxobuk'
    auth_user_85.first_name = u''
    auth_user_85.last_name = u''
    auth_user_85.email = u''
    auth_user_85.is_staff = False
    auth_user_85.is_active = True
    auth_user_85.date_joined = dateutil.parser.parse("2013-09-14T07:42:55+00:00")
    auth_user_85 = importer.save_or_locate(auth_user_85)

    auth_user_86 = User()
    auth_user_86.password = u'pbkdf2_sha256$10000$cd63AwlK1t8p$YReJKnjhcYeXsx6f8HA5mP4nrlnIUsISuXXgfq6UUtc='
    auth_user_86.last_login = dateutil.parser.parse("2013-09-14T08:27:00+00:00")
    auth_user_86.is_superuser = False
    auth_user_86.username = u'Breygon'
    auth_user_86.first_name = u''
    auth_user_86.last_name = u''
    auth_user_86.email = u''
    auth_user_86.is_staff = False
    auth_user_86.is_active = True
    auth_user_86.date_joined = dateutil.parser.parse("2013-09-14T08:27:00+00:00")
    auth_user_86 = importer.save_or_locate(auth_user_86)

    auth_user_87 = User()
    auth_user_87.password = u'pbkdf2_sha256$10000$Nt64fwZsNsc2$Qt7/VGcOfYR6tDqI4o3JG3PKEBqcXf23dkgB7GYISH8='
    auth_user_87.last_login = dateutil.parser.parse("2013-09-14T10:03:40+00:00")
    auth_user_87.is_superuser = False
    auth_user_87.username = u'MadHadad'
    auth_user_87.first_name = u''
    auth_user_87.last_name = u''
    auth_user_87.email = u''
    auth_user_87.is_staff = False
    auth_user_87.is_active = True
    auth_user_87.date_joined = dateutil.parser.parse("2013-09-14T10:03:39+00:00")
    auth_user_87 = importer.save_or_locate(auth_user_87)

    auth_user_88 = User()
    auth_user_88.password = u'pbkdf2_sha256$10000$l3pDclnjXm4V$ZHMwMGqMzZIBVhVg564+F1y+bLm4DolO/ip8qWMKO/w='
    auth_user_88.last_login = dateutil.parser.parse("2013-09-14T17:46:08+00:00")
    auth_user_88.is_superuser = False
    auth_user_88.username = u'backwardscancan'
    auth_user_88.first_name = u''
    auth_user_88.last_name = u''
    auth_user_88.email = u''
    auth_user_88.is_staff = False
    auth_user_88.is_active = True
    auth_user_88.date_joined = dateutil.parser.parse("2013-09-14T17:46:08+00:00")
    auth_user_88 = importer.save_or_locate(auth_user_88)

    auth_user_89 = User()
    auth_user_89.password = u'pbkdf2_sha256$10000$P967QLuMRHFy$pmIl+u3FIt8FBRiDPRgVreRpu/TDaEQXkIUGCDYTrPE='
    auth_user_89.last_login = dateutil.parser.parse("2013-09-14T18:21:27+00:00")
    auth_user_89.is_superuser = False
    auth_user_89.username = u'Filifjonka'
    auth_user_89.first_name = u''
    auth_user_89.last_name = u''
    auth_user_89.email = u''
    auth_user_89.is_staff = False
    auth_user_89.is_active = True
    auth_user_89.date_joined = dateutil.parser.parse("2013-09-14T18:21:27+00:00")
    auth_user_89 = importer.save_or_locate(auth_user_89)

    auth_user_90 = User()
    auth_user_90.password = u'pbkdf2_sha256$10000$Um4VZ5A3ZRBX$UiG/3Oz9PwEkCmPqwCiuAEshEybqdr8fhW6F5dhhiCk='
    auth_user_90.last_login = dateutil.parser.parse("2013-09-14T18:54:49+00:00")
    auth_user_90.is_superuser = False
    auth_user_90.username = u'Skypilot343'
    auth_user_90.first_name = u''
    auth_user_90.last_name = u''
    auth_user_90.email = u''
    auth_user_90.is_staff = False
    auth_user_90.is_active = True
    auth_user_90.date_joined = dateutil.parser.parse("2013-09-14T18:54:49+00:00")
    auth_user_90 = importer.save_or_locate(auth_user_90)

    auth_user_91 = User()
    auth_user_91.password = u'pbkdf2_sha256$10000$faB81MTzPZah$MnTmahB5n7+yVU3XEJCHwDe1MAqhRq0FvU1Bimz3DoM='
    auth_user_91.last_login = dateutil.parser.parse("2013-09-14T21:11:43+00:00")
    auth_user_91.is_superuser = False
    auth_user_91.username = u'smartrunner'
    auth_user_91.first_name = u''
    auth_user_91.last_name = u''
    auth_user_91.email = u''
    auth_user_91.is_staff = False
    auth_user_91.is_active = True
    auth_user_91.date_joined = dateutil.parser.parse("2013-09-14T21:11:43+00:00")
    auth_user_91 = importer.save_or_locate(auth_user_91)

    auth_user_92 = User()
    auth_user_92.password = u'pbkdf2_sha256$10000$F0JkN24Kks1I$UrHf0QxpMeoKc96QtmDJIsowoAFlaZ2jKiQ8XSZLYQc='
    auth_user_92.last_login = dateutil.parser.parse("2013-09-14T22:59:14+00:00")
    auth_user_92.is_superuser = False
    auth_user_92.username = u'Broadway'
    auth_user_92.first_name = u''
    auth_user_92.last_name = u''
    auth_user_92.email = u''
    auth_user_92.is_staff = False
    auth_user_92.is_active = True
    auth_user_92.date_joined = dateutil.parser.parse("2013-09-14T22:59:14+00:00")
    auth_user_92 = importer.save_or_locate(auth_user_92)

    auth_user_93 = User()
    auth_user_93.password = u'pbkdf2_sha256$10000$virmuAp3SMLB$hW6/yHKA9z9oMgemswUTgruGyFK/MrvqBPPqXz87fY0='
    auth_user_93.last_login = dateutil.parser.parse("2013-09-15T03:22:11+00:00")
    auth_user_93.is_superuser = False
    auth_user_93.username = u'vulcan6'
    auth_user_93.first_name = u''
    auth_user_93.last_name = u''
    auth_user_93.email = u''
    auth_user_93.is_staff = False
    auth_user_93.is_active = True
    auth_user_93.date_joined = dateutil.parser.parse("2013-09-15T03:22:10+00:00")
    auth_user_93 = importer.save_or_locate(auth_user_93)

    auth_user_94 = User()
    auth_user_94.password = u'pbkdf2_sha256$10000$emBfyH5sc4QN$rerLDDn2WgTxpkqBtcGwDxb2OqSDJkHL3Zpcalc/j6o='
    auth_user_94.last_login = dateutil.parser.parse("2013-09-15T03:59:24+00:00")
    auth_user_94.is_superuser = False
    auth_user_94.username = u'Mooseay'
    auth_user_94.first_name = u''
    auth_user_94.last_name = u''
    auth_user_94.email = u''
    auth_user_94.is_staff = False
    auth_user_94.is_active = True
    auth_user_94.date_joined = dateutil.parser.parse("2013-09-15T03:59:24+00:00")
    auth_user_94 = importer.save_or_locate(auth_user_94)

    auth_user_95 = User()
    auth_user_95.password = u'pbkdf2_sha256$10000$vJVXNGF5wwkS$kHmJ2P43R9o/0gnKrH6J01LYJWuIUpIXdsScdthca6o='
    auth_user_95.last_login = dateutil.parser.parse("2013-09-15T04:45:46+00:00")
    auth_user_95.is_superuser = False
    auth_user_95.username = u'pawk'
    auth_user_95.first_name = u''
    auth_user_95.last_name = u''
    auth_user_95.email = u''
    auth_user_95.is_staff = False
    auth_user_95.is_active = True
    auth_user_95.date_joined = dateutil.parser.parse("2013-09-15T04:45:46+00:00")
    auth_user_95 = importer.save_or_locate(auth_user_95)

    auth_user_96 = User()
    auth_user_96.password = u'pbkdf2_sha256$10000$O9qfHoi2mLHs$symhHzcJ26j8a0+KpjprclgJB4foCD3nSsuOVIV4pAY='
    auth_user_96.last_login = dateutil.parser.parse("2013-09-15T06:28:14+00:00")
    auth_user_96.is_superuser = False
    auth_user_96.username = u'jako800'
    auth_user_96.first_name = u''
    auth_user_96.last_name = u''
    auth_user_96.email = u''
    auth_user_96.is_staff = False
    auth_user_96.is_active = True
    auth_user_96.date_joined = dateutil.parser.parse("2013-09-15T06:28:14+00:00")
    auth_user_96 = importer.save_or_locate(auth_user_96)

    auth_user_97 = User()
    auth_user_97.password = u'pbkdf2_sha256$10000$8OZCjgLcT4WD$9aSs85KGYiLETWGdsHqBOZM/J33Xe0zC16IimQJuTWQ='
    auth_user_97.last_login = dateutil.parser.parse("2013-09-15T08:10:34+00:00")
    auth_user_97.is_superuser = False
    auth_user_97.username = u'Invictia'
    auth_user_97.first_name = u''
    auth_user_97.last_name = u''
    auth_user_97.email = u''
    auth_user_97.is_staff = False
    auth_user_97.is_active = True
    auth_user_97.date_joined = dateutil.parser.parse("2013-09-15T08:10:33+00:00")
    auth_user_97 = importer.save_or_locate(auth_user_97)

    auth_user_98 = User()
    auth_user_98.password = u'pbkdf2_sha256$10000$OXNk0LPYQSjf$NFkd+m37zThSneZLfaRpybJH22XCCC+usenR0o375rA='
    auth_user_98.last_login = dateutil.parser.parse("2013-09-15T08:20:43+00:00")
    auth_user_98.is_superuser = False
    auth_user_98.username = u'paf1701'
    auth_user_98.first_name = u''
    auth_user_98.last_name = u''
    auth_user_98.email = u''
    auth_user_98.is_staff = False
    auth_user_98.is_active = True
    auth_user_98.date_joined = dateutil.parser.parse("2013-09-15T08:20:43+00:00")
    auth_user_98 = importer.save_or_locate(auth_user_98)

    auth_user_99 = User()
    auth_user_99.password = u'pbkdf2_sha256$10000$ATyFzEYUuzLx$CAOZ23V36hiertR/w1mXIRrthBE0P6gmflaG3zkEOKE='
    auth_user_99.last_login = dateutil.parser.parse("2013-09-15T13:55:35+00:00")
    auth_user_99.is_superuser = False
    auth_user_99.username = u'Looth'
    auth_user_99.first_name = u''
    auth_user_99.last_name = u''
    auth_user_99.email = u''
    auth_user_99.is_staff = False
    auth_user_99.is_active = True
    auth_user_99.date_joined = dateutil.parser.parse("2013-09-15T13:55:34+00:00")
    auth_user_99 = importer.save_or_locate(auth_user_99)

    auth_user_100 = User()
    auth_user_100.password = u'pbkdf2_sha256$10000$kkTZyjTdWI49$AQLLpADyMV9XgLvk6Kc/btRQNToatTWRrvkYk6K5niY='
    auth_user_100.last_login = dateutil.parser.parse("2013-09-15T14:38:22+00:00")
    auth_user_100.is_superuser = False
    auth_user_100.username = u'Burrich'
    auth_user_100.first_name = u''
    auth_user_100.last_name = u''
    auth_user_100.email = u''
    auth_user_100.is_staff = False
    auth_user_100.is_active = True
    auth_user_100.date_joined = dateutil.parser.parse("2013-09-15T14:38:22+00:00")
    auth_user_100 = importer.save_or_locate(auth_user_100)

    auth_user_101 = User()
    auth_user_101.password = u'pbkdf2_sha256$10000$psz6tXsLzKHi$jdLiEJ6yyAUD6l2h1y6UVaxso4J3Nb5Q2pDI+Q04Koc='
    auth_user_101.last_login = dateutil.parser.parse("2013-09-15T17:19:46+00:00")
    auth_user_101.is_superuser = False
    auth_user_101.username = u'Soban'
    auth_user_101.first_name = u''
    auth_user_101.last_name = u''
    auth_user_101.email = u''
    auth_user_101.is_staff = False
    auth_user_101.is_active = True
    auth_user_101.date_joined = dateutil.parser.parse("2013-09-15T17:19:46+00:00")
    auth_user_101 = importer.save_or_locate(auth_user_101)

    auth_user_102 = User()
    auth_user_102.password = u'pbkdf2_sha256$10000$Z8t9cVW53a5h$UyOPx7H8zm4YjuSAU2hEhjZPEq+xLcRLt3uH87IVv8U='
    auth_user_102.last_login = dateutil.parser.parse("2013-09-15T21:16:32+00:00")
    auth_user_102.is_superuser = False
    auth_user_102.username = u'mason4300'
    auth_user_102.first_name = u''
    auth_user_102.last_name = u''
    auth_user_102.email = u''
    auth_user_102.is_staff = False
    auth_user_102.is_active = True
    auth_user_102.date_joined = dateutil.parser.parse("2013-09-15T21:16:32+00:00")
    auth_user_102 = importer.save_or_locate(auth_user_102)

    auth_user_103 = User()
    auth_user_103.password = u'pbkdf2_sha256$10000$Ff2Z6S6OLT7n$wcBWLWg2JA9AUbw43mW1L/6bUVDePXOyZZWNowkXUeE='
    auth_user_103.last_login = dateutil.parser.parse("2013-09-15T21:20:26+00:00")
    auth_user_103.is_superuser = False
    auth_user_103.username = u'Steeler'
    auth_user_103.first_name = u''
    auth_user_103.last_name = u''
    auth_user_103.email = u''
    auth_user_103.is_staff = False
    auth_user_103.is_active = True
    auth_user_103.date_joined = dateutil.parser.parse("2013-09-15T21:20:26+00:00")
    auth_user_103 = importer.save_or_locate(auth_user_103)

    auth_user_104 = User()
    auth_user_104.password = u'pbkdf2_sha256$10000$SYwkNDEPOZDH$A2rVW/GqLm36nsCo3a1XlYcgNg1q5f0fcv7kjPGoXAk='
    auth_user_104.last_login = dateutil.parser.parse("2013-09-16T00:04:51+00:00")
    auth_user_104.is_superuser = False
    auth_user_104.username = u'Ryu Saga'
    auth_user_104.first_name = u''
    auth_user_104.last_name = u''
    auth_user_104.email = u''
    auth_user_104.is_staff = False
    auth_user_104.is_active = True
    auth_user_104.date_joined = dateutil.parser.parse("2013-09-16T00:04:51+00:00")
    auth_user_104 = importer.save_or_locate(auth_user_104)

    auth_user_105 = User()
    auth_user_105.password = u'pbkdf2_sha256$10000$Xgn4G4RqIfya$yuMfFAoXEjIVV8ZSoqfIhBPvwiBGJrwGohN3cXag2Zc='
    auth_user_105.last_login = dateutil.parser.parse("2013-09-16T01:16:59+00:00")
    auth_user_105.is_superuser = False
    auth_user_105.username = u'Nighthawk666'
    auth_user_105.first_name = u''
    auth_user_105.last_name = u''
    auth_user_105.email = u''
    auth_user_105.is_staff = False
    auth_user_105.is_active = True
    auth_user_105.date_joined = dateutil.parser.parse("2013-09-16T01:16:58+00:00")
    auth_user_105 = importer.save_or_locate(auth_user_105)

    auth_user_106 = User()
    auth_user_106.password = u'pbkdf2_sha256$10000$79avs5RzU8zO$yiKftETAh/3OE6YHKVdbnmtScbDF1MOBAHdSWJjzNJI='
    auth_user_106.last_login = dateutil.parser.parse("2013-09-16T01:56:07+00:00")
    auth_user_106.is_superuser = False
    auth_user_106.username = u'Timeshock'
    auth_user_106.first_name = u''
    auth_user_106.last_name = u''
    auth_user_106.email = u''
    auth_user_106.is_staff = False
    auth_user_106.is_active = True
    auth_user_106.date_joined = dateutil.parser.parse("2013-09-16T01:56:07+00:00")
    auth_user_106 = importer.save_or_locate(auth_user_106)

    auth_user_107 = User()
    auth_user_107.password = u'pbkdf2_sha256$10000$qPBHTeT2aam1$UDwALRESE7HnbVBIkwXYsyiqIKcCS2sjfoXOohkZPDY='
    auth_user_107.last_login = dateutil.parser.parse("2013-09-16T03:16:28+00:00")
    auth_user_107.is_superuser = False
    auth_user_107.username = u'Taw'
    auth_user_107.first_name = u''
    auth_user_107.last_name = u''
    auth_user_107.email = u''
    auth_user_107.is_staff = False
    auth_user_107.is_active = True
    auth_user_107.date_joined = dateutil.parser.parse("2013-09-16T03:16:28+00:00")
    auth_user_107 = importer.save_or_locate(auth_user_107)

    auth_user_108 = User()
    auth_user_108.password = u'pbkdf2_sha256$10000$BVNZmUdHmJHL$29WcA7nJzYuojxzXmvDDUjpmQrovF6/QDzQ4mROX2gA='
    auth_user_108.last_login = dateutil.parser.parse("2013-09-16T04:33:38+00:00")
    auth_user_108.is_superuser = False
    auth_user_108.username = u'gbsilverio'
    auth_user_108.first_name = u''
    auth_user_108.last_name = u''
    auth_user_108.email = u''
    auth_user_108.is_staff = False
    auth_user_108.is_active = True
    auth_user_108.date_joined = dateutil.parser.parse("2013-09-16T04:33:38+00:00")
    auth_user_108 = importer.save_or_locate(auth_user_108)

    auth_user_109 = User()
    auth_user_109.password = u'pbkdf2_sha256$10000$2pG79WKdf2Xo$hPbcaAsIV+aGvNndUNoFCrMokdEj8tdJ25InoT4EasU='
    auth_user_109.last_login = dateutil.parser.parse("2013-09-16T05:10:07+00:00")
    auth_user_109.is_superuser = False
    auth_user_109.username = u'Phoenix'
    auth_user_109.first_name = u''
    auth_user_109.last_name = u''
    auth_user_109.email = u''
    auth_user_109.is_staff = False
    auth_user_109.is_active = True
    auth_user_109.date_joined = dateutil.parser.parse("2013-09-16T05:10:07+00:00")
    auth_user_109 = importer.save_or_locate(auth_user_109)

    auth_user_110 = User()
    auth_user_110.password = u'pbkdf2_sha256$10000$xjllVPwxXaNW$VRzTcGZL839oNgrJUt6ykoXma6VgUjaQkRufV/g1wWU='
    auth_user_110.last_login = dateutil.parser.parse("2013-09-16T06:49:25+00:00")
    auth_user_110.is_superuser = False
    auth_user_110.username = u'FeralBadger'
    auth_user_110.first_name = u''
    auth_user_110.last_name = u''
    auth_user_110.email = u''
    auth_user_110.is_staff = False
    auth_user_110.is_active = True
    auth_user_110.date_joined = dateutil.parser.parse("2013-09-16T06:49:25+00:00")
    auth_user_110 = importer.save_or_locate(auth_user_110)

    auth_user_111 = User()
    auth_user_111.password = u'pbkdf2_sha256$10000$y8yvcgegSHiv$O5jq+z7sWStrlwn+OTA+Ee4HZjaG8HmjzE292wSMPKw='
    auth_user_111.last_login = dateutil.parser.parse("2013-09-16T07:38:38+00:00")
    auth_user_111.is_superuser = False
    auth_user_111.username = u'Fazno'
    auth_user_111.first_name = u''
    auth_user_111.last_name = u''
    auth_user_111.email = u''
    auth_user_111.is_staff = False
    auth_user_111.is_active = True
    auth_user_111.date_joined = dateutil.parser.parse("2013-09-16T07:38:38+00:00")
    auth_user_111 = importer.save_or_locate(auth_user_111)

    auth_user_112 = User()
    auth_user_112.password = u'pbkdf2_sha256$10000$65WT2ZIQ7na5$0qQ6QI7Mfgsew42DCQzg8HZ5rovqPUsyKFPJBl6OlF8='
    auth_user_112.last_login = dateutil.parser.parse("2013-09-16T08:04:03+00:00")
    auth_user_112.is_superuser = False
    auth_user_112.username = u'JoseGasparilla'
    auth_user_112.first_name = u''
    auth_user_112.last_name = u''
    auth_user_112.email = u''
    auth_user_112.is_staff = False
    auth_user_112.is_active = True
    auth_user_112.date_joined = dateutil.parser.parse("2013-09-16T08:04:03+00:00")
    auth_user_112 = importer.save_or_locate(auth_user_112)

    auth_user_113 = User()
    auth_user_113.password = u'pbkdf2_sha256$10000$lsdg0N1AdZyK$OexEe0zNsXIXhfsAOjqFgEY7kvFLFzHZPT/+12F6vEk='
    auth_user_113.last_login = dateutil.parser.parse("2013-09-16T16:35:57+00:00")
    auth_user_113.is_superuser = False
    auth_user_113.username = u'FF-Darkhalf'
    auth_user_113.first_name = u''
    auth_user_113.last_name = u''
    auth_user_113.email = u''
    auth_user_113.is_staff = False
    auth_user_113.is_active = True
    auth_user_113.date_joined = dateutil.parser.parse("2013-09-16T16:35:57+00:00")
    auth_user_113 = importer.save_or_locate(auth_user_113)

    auth_user_114 = User()
    auth_user_114.password = u'pbkdf2_sha256$10000$Iw1de46Ia6IM$X27a01jee6ALATZOhzc0uK0P+fAq6nsn4AVspJGZOQY='
    auth_user_114.last_login = dateutil.parser.parse("2013-09-16T23:31:26+00:00")
    auth_user_114.is_superuser = False
    auth_user_114.username = u'Tector'
    auth_user_114.first_name = u''
    auth_user_114.last_name = u''
    auth_user_114.email = u''
    auth_user_114.is_staff = False
    auth_user_114.is_active = True
    auth_user_114.date_joined = dateutil.parser.parse("2013-09-16T23:31:26+00:00")
    auth_user_114 = importer.save_or_locate(auth_user_114)

    auth_user_115 = User()
    auth_user_115.password = u'pbkdf2_sha256$10000$xmpQm3wGf2ld$vJ6SxIlcgOEJl3SygZQQlrztbUd1kR8pVUm+mPI/bf0='
    auth_user_115.last_login = dateutil.parser.parse("2013-09-17T00:38:17+00:00")
    auth_user_115.is_superuser = False
    auth_user_115.username = u'Holyvision'
    auth_user_115.first_name = u''
    auth_user_115.last_name = u''
    auth_user_115.email = u''
    auth_user_115.is_staff = False
    auth_user_115.is_active = True
    auth_user_115.date_joined = dateutil.parser.parse("2013-09-17T00:38:16+00:00")
    auth_user_115 = importer.save_or_locate(auth_user_115)

    auth_user_116 = User()
    auth_user_116.password = u'pbkdf2_sha256$10000$Zho6VeA6zK75$K6ks0+t/M5XjIx9Ba0//pUFN8Hugyu8R+roDZvIn+dg='
    auth_user_116.last_login = dateutil.parser.parse("2013-09-17T03:58:17+00:00")
    auth_user_116.is_superuser = False
    auth_user_116.username = u'That Lighting Guy'
    auth_user_116.first_name = u''
    auth_user_116.last_name = u''
    auth_user_116.email = u''
    auth_user_116.is_staff = False
    auth_user_116.is_active = True
    auth_user_116.date_joined = dateutil.parser.parse("2013-09-17T03:58:17+00:00")
    auth_user_116 = importer.save_or_locate(auth_user_116)

    auth_user_117 = User()
    auth_user_117.password = u'pbkdf2_sha256$10000$NQZbMV8w1Fr2$XUKc13s1mCNR4qAbERae9Fm4YyetrrbTuNDOLzK7F9M='
    auth_user_117.last_login = dateutil.parser.parse("2013-09-17T09:51:30+00:00")
    auth_user_117.is_superuser = False
    auth_user_117.username = u'blritsema'
    auth_user_117.first_name = u''
    auth_user_117.last_name = u''
    auth_user_117.email = u''
    auth_user_117.is_staff = False
    auth_user_117.is_active = True
    auth_user_117.date_joined = dateutil.parser.parse("2013-09-17T09:51:30+00:00")
    auth_user_117 = importer.save_or_locate(auth_user_117)

    auth_user_118 = User()
    auth_user_118.password = u'pbkdf2_sha256$10000$9G6J0ytCpusX$O2qflim3QR/z34xNssx5H6+nnKovOyam4n4xYKqvuvk='
    auth_user_118.last_login = dateutil.parser.parse("2013-09-17T11:08:53+00:00")
    auth_user_118.is_superuser = False
    auth_user_118.username = u'Texas Red'
    auth_user_118.first_name = u''
    auth_user_118.last_name = u''
    auth_user_118.email = u''
    auth_user_118.is_staff = False
    auth_user_118.is_active = True
    auth_user_118.date_joined = dateutil.parser.parse("2013-09-17T11:08:53+00:00")
    auth_user_118 = importer.save_or_locate(auth_user_118)

    auth_user_119 = User()
    auth_user_119.password = u'pbkdf2_sha256$10000$1zjshhqgefXB$4sFo7gh1J5sx2GprhA8d6qdGJCXRNQxjU+evZWd4fDE='
    auth_user_119.last_login = dateutil.parser.parse("2013-09-17T22:01:53+00:00")
    auth_user_119.is_superuser = False
    auth_user_119.username = u'JMosthaf'
    auth_user_119.first_name = u''
    auth_user_119.last_name = u''
    auth_user_119.email = u''
    auth_user_119.is_staff = False
    auth_user_119.is_active = True
    auth_user_119.date_joined = dateutil.parser.parse("2013-09-17T22:01:53+00:00")
    auth_user_119 = importer.save_or_locate(auth_user_119)

    auth_user_120 = User()
    auth_user_120.password = u'pbkdf2_sha256$10000$e9bTLuNMmJU6$/oywcnIGSERyeCp2SswAbfmnbYYbKnDvHiYD0jr7HhY='
    auth_user_120.last_login = dateutil.parser.parse("2013-09-17T22:37:50+00:00")
    auth_user_120.is_superuser = False
    auth_user_120.username = u'Togerah'
    auth_user_120.first_name = u''
    auth_user_120.last_name = u''
    auth_user_120.email = u''
    auth_user_120.is_staff = False
    auth_user_120.is_active = True
    auth_user_120.date_joined = dateutil.parser.parse("2013-09-17T22:37:50+00:00")
    auth_user_120 = importer.save_or_locate(auth_user_120)

    auth_user_121 = User()
    auth_user_121.password = u'pbkdf2_sha256$10000$PfMhVLvZlZvP$RioZWIw7euN7Pfq784DMtT2DcciziLdpP8DSQWJFrYo='
    auth_user_121.last_login = dateutil.parser.parse("2013-09-18T01:28:45+00:00")
    auth_user_121.is_superuser = False
    auth_user_121.username = u'Molehawk'
    auth_user_121.first_name = u''
    auth_user_121.last_name = u''
    auth_user_121.email = u''
    auth_user_121.is_staff = False
    auth_user_121.is_active = True
    auth_user_121.date_joined = dateutil.parser.parse("2013-09-18T01:28:45+00:00")
    auth_user_121 = importer.save_or_locate(auth_user_121)

    auth_user_122 = User()
    auth_user_122.password = u'pbkdf2_sha256$10000$tMUQOMRzaYNM$IUJaaeRSweLwex8dcB+2i0a6x0LbICujmDcL9JsICDE='
    auth_user_122.last_login = dateutil.parser.parse("2013-09-18T01:53:26+00:00")
    auth_user_122.is_superuser = False
    auth_user_122.username = u'waxpatriot'
    auth_user_122.first_name = u''
    auth_user_122.last_name = u''
    auth_user_122.email = u''
    auth_user_122.is_staff = False
    auth_user_122.is_active = True
    auth_user_122.date_joined = dateutil.parser.parse("2013-09-18T01:53:26+00:00")
    auth_user_122 = importer.save_or_locate(auth_user_122)

    auth_user_123 = User()
    auth_user_123.password = u'pbkdf2_sha256$10000$pLAM5KbdMKnY$nZrcGDuYAX5l951ycuv4K6PPP+4pJxAtZyW67aAMW98='
    auth_user_123.last_login = dateutil.parser.parse("2013-09-18T04:18:35+00:00")
    auth_user_123.is_superuser = False
    auth_user_123.username = u'Sawbones'
    auth_user_123.first_name = u''
    auth_user_123.last_name = u''
    auth_user_123.email = u''
    auth_user_123.is_staff = False
    auth_user_123.is_active = True
    auth_user_123.date_joined = dateutil.parser.parse("2013-09-18T04:18:35+00:00")
    auth_user_123 = importer.save_or_locate(auth_user_123)

    auth_user_124 = User()
    auth_user_124.password = u'pbkdf2_sha256$10000$aI3VfLw1zc4G$HH4rcBq+bfCb9tUvu7D6+dJPJo/yUZGg/HRAakd2gRs='
    auth_user_124.last_login = dateutil.parser.parse("2013-09-18T05:16:37+00:00")
    auth_user_124.is_superuser = False
    auth_user_124.username = u'dieside666'
    auth_user_124.first_name = u''
    auth_user_124.last_name = u''
    auth_user_124.email = u''
    auth_user_124.is_staff = False
    auth_user_124.is_active = True
    auth_user_124.date_joined = dateutil.parser.parse("2013-09-18T05:16:37+00:00")
    auth_user_124 = importer.save_or_locate(auth_user_124)

    auth_user_125 = User()
    auth_user_125.password = u'pbkdf2_sha256$10000$kkPd1Hw8XONz$Turl1iboI0+yR0bJBapxUZE47hafCImSU14VtRb0htQ='
    auth_user_125.last_login = dateutil.parser.parse("2013-09-18T06:11:10+00:00")
    auth_user_125.is_superuser = False
    auth_user_125.username = u'PoorRichard'
    auth_user_125.first_name = u''
    auth_user_125.last_name = u''
    auth_user_125.email = u''
    auth_user_125.is_staff = False
    auth_user_125.is_active = True
    auth_user_125.date_joined = dateutil.parser.parse("2013-09-18T06:11:10+00:00")
    auth_user_125 = importer.save_or_locate(auth_user_125)

    auth_user_126 = User()
    auth_user_126.password = u'pbkdf2_sha256$10000$uT0oYWfrHpzs$4R2FolZTygr/pWBrJJpSdn0VMCsSjvYtujwm/Z5rzs4='
    auth_user_126.last_login = dateutil.parser.parse("2013-09-18T11:08:13+00:00")
    auth_user_126.is_superuser = False
    auth_user_126.username = u'kin0025'
    auth_user_126.first_name = u''
    auth_user_126.last_name = u''
    auth_user_126.email = u''
    auth_user_126.is_staff = False
    auth_user_126.is_active = True
    auth_user_126.date_joined = dateutil.parser.parse("2013-09-18T11:08:12+00:00")
    auth_user_126 = importer.save_or_locate(auth_user_126)

    auth_user_127 = User()
    auth_user_127.password = u'pbkdf2_sha256$10000$SWJBp0vg4AWh$aDbDme1zscaFGPlupQyjIFXtk8CVB2nvRY0+evCyNLw='
    auth_user_127.last_login = dateutil.parser.parse("2013-09-18T11:18:18+00:00")
    auth_user_127.is_superuser = False
    auth_user_127.username = u'Pelenor'
    auth_user_127.first_name = u''
    auth_user_127.last_name = u''
    auth_user_127.email = u''
    auth_user_127.is_staff = False
    auth_user_127.is_active = True
    auth_user_127.date_joined = dateutil.parser.parse("2013-09-18T11:18:18+00:00")
    auth_user_127 = importer.save_or_locate(auth_user_127)

    auth_user_128 = User()
    auth_user_128.password = u'pbkdf2_sha256$10000$naJ5vfhQYoSr$yJX4nzwp3KfyxwGu5ALqPelrjzB3QyV3GayplWcwUbc='
    auth_user_128.last_login = dateutil.parser.parse("2013-09-18T18:54:04+00:00")
    auth_user_128.is_superuser = False
    auth_user_128.username = u'Hyku'
    auth_user_128.first_name = u''
    auth_user_128.last_name = u''
    auth_user_128.email = u''
    auth_user_128.is_staff = False
    auth_user_128.is_active = True
    auth_user_128.date_joined = dateutil.parser.parse("2013-09-18T18:54:04+00:00")
    auth_user_128 = importer.save_or_locate(auth_user_128)

    auth_user_129 = User()
    auth_user_129.password = u'pbkdf2_sha256$10000$HMT3vAGyamYa$Haeko6en+yVl3G2I3l+k58h/Gs99lMjH0Zlu2dNq334='
    auth_user_129.last_login = dateutil.parser.parse("2013-09-19T01:58:54+00:00")
    auth_user_129.is_superuser = False
    auth_user_129.username = u'cyberhedz'
    auth_user_129.first_name = u''
    auth_user_129.last_name = u''
    auth_user_129.email = u''
    auth_user_129.is_staff = False
    auth_user_129.is_active = True
    auth_user_129.date_joined = dateutil.parser.parse("2013-09-19T01:58:32+00:00")
    auth_user_129 = importer.save_or_locate(auth_user_129)

    auth_user_130 = User()
    auth_user_130.password = u'pbkdf2_sha256$10000$8GBzy9MCQmwv$uKZNyMIDf5dYfAe1eHBejzs9W4rwiILwqTDju7MLBHQ='
    auth_user_130.last_login = dateutil.parser.parse("2013-09-19T21:19:31+00:00")
    auth_user_130.is_superuser = False
    auth_user_130.username = u'SWRT'
    auth_user_130.first_name = u''
    auth_user_130.last_name = u''
    auth_user_130.email = u''
    auth_user_130.is_staff = False
    auth_user_130.is_active = True
    auth_user_130.date_joined = dateutil.parser.parse("2013-09-19T21:19:31+00:00")
    auth_user_130 = importer.save_or_locate(auth_user_130)

    auth_user_131 = User()
    auth_user_131.password = u'pbkdf2_sha256$10000$RmYSraFwIn6r$+DtVXki//xvj/r4VXNhtZbC9mEBnwEFk2r/mjVl1Q58='
    auth_user_131.last_login = dateutil.parser.parse("2013-09-19T22:40:59+00:00")
    auth_user_131.is_superuser = False
    auth_user_131.username = u'Snark'
    auth_user_131.first_name = u''
    auth_user_131.last_name = u''
    auth_user_131.email = u''
    auth_user_131.is_staff = False
    auth_user_131.is_active = True
    auth_user_131.date_joined = dateutil.parser.parse("2013-09-19T22:40:59+00:00")
    auth_user_131 = importer.save_or_locate(auth_user_131)

    auth_user_132 = User()
    auth_user_132.password = u'pbkdf2_sha256$10000$VgusbRYxwSvE$lmNg7ddblxF1ZZ/pKwdoCZqOaaQxUyg6ZWkfbAIKYiM='
    auth_user_132.last_login = dateutil.parser.parse("2013-09-20T01:35:47+00:00")
    auth_user_132.is_superuser = False
    auth_user_132.username = u'Death'
    auth_user_132.first_name = u''
    auth_user_132.last_name = u''
    auth_user_132.email = u''
    auth_user_132.is_staff = False
    auth_user_132.is_active = True
    auth_user_132.date_joined = dateutil.parser.parse("2013-09-20T01:35:47+00:00")
    auth_user_132 = importer.save_or_locate(auth_user_132)

    auth_user_133 = User()
    auth_user_133.password = u'pbkdf2_sha256$10000$S2l0pOSXwS2g$etnLGzxi++tcLTuYxSDQAyNn6xb9fapfAPBpnPMhg8U='
    auth_user_133.last_login = dateutil.parser.parse("2013-09-20T12:21:17+00:00")
    auth_user_133.is_superuser = False
    auth_user_133.username = u'evavictoria'
    auth_user_133.first_name = u''
    auth_user_133.last_name = u''
    auth_user_133.email = u''
    auth_user_133.is_staff = False
    auth_user_133.is_active = True
    auth_user_133.date_joined = dateutil.parser.parse("2013-09-20T10:45:17+00:00")
    auth_user_133 = importer.save_or_locate(auth_user_133)

    auth_user_134 = User()
    auth_user_134.password = u'pbkdf2_sha256$10000$QQPsZjH4yUCO$bkyRJEYhRdpGwLfy6c/V7rOOI+n1g5IkB36RHgoHzsI='
    auth_user_134.last_login = dateutil.parser.parse("2013-09-21T18:11:33+00:00")
    auth_user_134.is_superuser = False
    auth_user_134.username = u'markotb'
    auth_user_134.first_name = u''
    auth_user_134.last_name = u''
    auth_user_134.email = u''
    auth_user_134.is_staff = False
    auth_user_134.is_active = True
    auth_user_134.date_joined = dateutil.parser.parse("2013-09-21T18:11:33+00:00")
    auth_user_134 = importer.save_or_locate(auth_user_134)

    auth_user_135 = User()
    auth_user_135.password = u'pbkdf2_sha256$10000$sdyVUEjrYZ2p$lwXSQHmz58Ho0c+IOx08gN7L0Umbg5R/FvViJtWjJWk='
    auth_user_135.last_login = dateutil.parser.parse("2013-09-21T23:31:01+00:00")
    auth_user_135.is_superuser = False
    auth_user_135.username = u'Ironhawk'
    auth_user_135.first_name = u''
    auth_user_135.last_name = u''
    auth_user_135.email = u''
    auth_user_135.is_staff = False
    auth_user_135.is_active = True
    auth_user_135.date_joined = dateutil.parser.parse("2013-09-21T23:31:01+00:00")
    auth_user_135 = importer.save_or_locate(auth_user_135)

    auth_user_136 = User()
    auth_user_136.password = u'pbkdf2_sha256$10000$2CPXudSYJt6A$9gIa3D07cAb9QK5HH8adyMgP6B9HhPPVYxceVpRa5ZU='
    auth_user_136.last_login = dateutil.parser.parse("2013-09-22T01:12:25+00:00")
    auth_user_136.is_superuser = False
    auth_user_136.username = u'DrOwnz'
    auth_user_136.first_name = u''
    auth_user_136.last_name = u''
    auth_user_136.email = u''
    auth_user_136.is_staff = False
    auth_user_136.is_active = True
    auth_user_136.date_joined = dateutil.parser.parse("2013-09-22T01:12:25+00:00")
    auth_user_136 = importer.save_or_locate(auth_user_136)

    auth_user_137 = User()
    auth_user_137.password = u'pbkdf2_sha256$10000$G1q8kyVWaVVQ$fvxVItbvAseeMv/38kXAdugHC36GfHb2vLY35dp+6yM='
    auth_user_137.last_login = dateutil.parser.parse("2013-10-02T01:31:56+00:00")
    auth_user_137.is_superuser = False
    auth_user_137.username = u'PaulSt'
    auth_user_137.first_name = u''
    auth_user_137.last_name = u''
    auth_user_137.email = u''
    auth_user_137.is_staff = False
    auth_user_137.is_active = True
    auth_user_137.date_joined = dateutil.parser.parse("2013-09-22T07:48:01+00:00")
    auth_user_137 = importer.save_or_locate(auth_user_137)

    auth_user_138 = User()
    auth_user_138.password = u'pbkdf2_sha256$10000$A9rKbsm5QG6b$q7J6p1sMK41ECRyB7xd2jlswCG64oVtxuGjVmrU+dQU='
    auth_user_138.last_login = dateutil.parser.parse("2013-09-22T18:45:56+00:00")
    auth_user_138.is_superuser = False
    auth_user_138.username = u"Arleeya E'lleastra"
    auth_user_138.first_name = u''
    auth_user_138.last_name = u''
    auth_user_138.email = u''
    auth_user_138.is_staff = False
    auth_user_138.is_active = True
    auth_user_138.date_joined = dateutil.parser.parse("2013-09-22T18:45:56+00:00")
    auth_user_138 = importer.save_or_locate(auth_user_138)

    auth_user_139 = User()
    auth_user_139.password = u'pbkdf2_sha256$10000$gOyz2XftDhhZ$GjJ2wPFtY0wv1It90BbG7SWHodGTSgorM8WzkchkSWU='
    auth_user_139.last_login = dateutil.parser.parse("2013-09-22T23:02:57+00:00")
    auth_user_139.is_superuser = False
    auth_user_139.username = u'AgeCrash'
    auth_user_139.first_name = u''
    auth_user_139.last_name = u''
    auth_user_139.email = u''
    auth_user_139.is_staff = False
    auth_user_139.is_active = True
    auth_user_139.date_joined = dateutil.parser.parse("2013-09-22T23:02:57+00:00")
    auth_user_139 = importer.save_or_locate(auth_user_139)

    auth_user_140 = User()
    auth_user_140.password = u'pbkdf2_sha256$10000$nwnFo0WrWLLT$lEY/bwRN4rTS/oorbP5uG+rlN9N2UrvQS9zM78Plonw='
    auth_user_140.last_login = dateutil.parser.parse("2013-09-23T10:22:34+00:00")
    auth_user_140.is_superuser = False
    auth_user_140.username = u'darkilk'
    auth_user_140.first_name = u''
    auth_user_140.last_name = u''
    auth_user_140.email = u''
    auth_user_140.is_staff = False
    auth_user_140.is_active = True
    auth_user_140.date_joined = dateutil.parser.parse("2013-09-23T10:22:34+00:00")
    auth_user_140 = importer.save_or_locate(auth_user_140)

    auth_user_141 = User()
    auth_user_141.password = u'pbkdf2_sha256$10000$infPaJ9QZSvi$VRqELFbLTYR68VWkUA4ShmK4QSfNU3Zjca9HlgEnZhg='
    auth_user_141.last_login = dateutil.parser.parse("2013-09-23T12:26:41+00:00")
    auth_user_141.is_superuser = False
    auth_user_141.username = u'Mycroft'
    auth_user_141.first_name = u''
    auth_user_141.last_name = u''
    auth_user_141.email = u''
    auth_user_141.is_staff = False
    auth_user_141.is_active = True
    auth_user_141.date_joined = dateutil.parser.parse("2013-09-23T12:26:41+00:00")
    auth_user_141 = importer.save_or_locate(auth_user_141)

    auth_user_142 = User()
    auth_user_142.password = u'pbkdf2_sha256$10000$vrD7oKRO1Zyg$8wgaN+nGgyBUTJe4JsOpzBwdWCTYQm5Rn/E4neEM4co='
    auth_user_142.last_login = dateutil.parser.parse("2013-09-24T09:19:42+00:00")
    auth_user_142.is_superuser = False
    auth_user_142.username = u'dee_dubs'
    auth_user_142.first_name = u''
    auth_user_142.last_name = u''
    auth_user_142.email = u''
    auth_user_142.is_staff = False
    auth_user_142.is_active = True
    auth_user_142.date_joined = dateutil.parser.parse("2013-09-24T09:19:42+00:00")
    auth_user_142 = importer.save_or_locate(auth_user_142)

    auth_user_143 = User()
    auth_user_143.password = u'pbkdf2_sha256$10000$vcXcK2tDvBh9$0xNpMGwIB+flZ/ut5d5TrKT+KSgSHeT+SwerqitWfJs='
    auth_user_143.last_login = dateutil.parser.parse("2013-09-24T09:24:58+00:00")
    auth_user_143.is_superuser = False
    auth_user_143.username = u'RKS1959'
    auth_user_143.first_name = u''
    auth_user_143.last_name = u''
    auth_user_143.email = u''
    auth_user_143.is_staff = False
    auth_user_143.is_active = True
    auth_user_143.date_joined = dateutil.parser.parse("2013-09-24T09:24:58+00:00")
    auth_user_143 = importer.save_or_locate(auth_user_143)

    auth_user_144 = User()
    auth_user_144.password = u'pbkdf2_sha256$10000$5noOdzyjXAeQ$weh0+l556fVAVM32WFTkHtQZkDBs1qFV0sZYt4OhQ0w='
    auth_user_144.last_login = dateutil.parser.parse("2013-09-24T12:23:08+00:00")
    auth_user_144.is_superuser = False
    auth_user_144.username = u'Barthd90'
    auth_user_144.first_name = u''
    auth_user_144.last_name = u''
    auth_user_144.email = u''
    auth_user_144.is_staff = False
    auth_user_144.is_active = True
    auth_user_144.date_joined = dateutil.parser.parse("2013-09-24T12:23:08+00:00")
    auth_user_144 = importer.save_or_locate(auth_user_144)

    auth_user_145 = User()
    auth_user_145.password = u'pbkdf2_sha256$10000$47wSTn4rWeCm$I3R0xWw5zDLSzRsRByohYMsi6F3XZMyJ4fjx4xbu4GQ='
    auth_user_145.last_login = dateutil.parser.parse("2013-09-24T21:17:01+00:00")
    auth_user_145.is_superuser = False
    auth_user_145.username = u'Batau'
    auth_user_145.first_name = u''
    auth_user_145.last_name = u''
    auth_user_145.email = u''
    auth_user_145.is_staff = False
    auth_user_145.is_active = True
    auth_user_145.date_joined = dateutil.parser.parse("2013-09-24T21:17:01+00:00")
    auth_user_145 = importer.save_or_locate(auth_user_145)

    auth_user_146 = User()
    auth_user_146.password = u'pbkdf2_sha256$10000$Zg8O7dQ605g2$pt6ZykdWp176v7u0/qOElhUltjyyHGoU70skTOQlkyo='
    auth_user_146.last_login = dateutil.parser.parse("2013-09-25T01:32:43+00:00")
    auth_user_146.is_superuser = False
    auth_user_146.username = u'steck'
    auth_user_146.first_name = u''
    auth_user_146.last_name = u''
    auth_user_146.email = u''
    auth_user_146.is_staff = False
    auth_user_146.is_active = True
    auth_user_146.date_joined = dateutil.parser.parse("2013-09-25T00:42:03+00:00")
    auth_user_146 = importer.save_or_locate(auth_user_146)

    auth_user_147 = User()
    auth_user_147.password = u'pbkdf2_sha256$10000$9r6mCoEMDsql$S9gfkXIGWGBK+on8tizDSN3lRMk/tJrXBCHGH0To5z8='
    auth_user_147.last_login = dateutil.parser.parse("2013-09-25T03:03:35+00:00")
    auth_user_147.is_superuser = False
    auth_user_147.username = u'Bloodredrecon'
    auth_user_147.first_name = u''
    auth_user_147.last_name = u''
    auth_user_147.email = u''
    auth_user_147.is_staff = False
    auth_user_147.is_active = True
    auth_user_147.date_joined = dateutil.parser.parse("2013-09-25T03:03:35+00:00")
    auth_user_147 = importer.save_or_locate(auth_user_147)

    auth_user_148 = User()
    auth_user_148.password = u'pbkdf2_sha256$10000$UYu0WaWIolOI$139TM4Z5n5hP2nrB8hh50JzNzt9lSW07RfBYpy5x5bA='
    auth_user_148.last_login = dateutil.parser.parse("2013-10-03T02:42:49+00:00")
    auth_user_148.is_superuser = False
    auth_user_148.username = u'rogomacine'
    auth_user_148.first_name = u''
    auth_user_148.last_name = u''
    auth_user_148.email = u''
    auth_user_148.is_staff = False
    auth_user_148.is_active = True
    auth_user_148.date_joined = dateutil.parser.parse("2013-10-03T02:42:49+00:00")
    auth_user_148 = importer.save_or_locate(auth_user_148)

    auth_user_149 = User()
    auth_user_149.password = u'pbkdf2_sha256$10000$gvjx08P92OaY$IoeqgKwb9nTwZV54/8WPc8ytKp1ZJ3BcAN1bs8LJHJo='
    auth_user_149.last_login = dateutil.parser.parse("2013-10-04T19:08:49+00:00")
    auth_user_149.is_superuser = False
    auth_user_149.username = u'Alicatt'
    auth_user_149.first_name = u''
    auth_user_149.last_name = u''
    auth_user_149.email = u''
    auth_user_149.is_staff = False
    auth_user_149.is_active = True
    auth_user_149.date_joined = dateutil.parser.parse("2013-10-04T19:08:49+00:00")
    auth_user_149 = importer.save_or_locate(auth_user_149)

    auth_user_150 = User()
    auth_user_150.password = u'pbkdf2_sha256$10000$dfpPfcNiij5A$ueBq254LnLhphTrpgB1FKNJUzLKRuoXOT+oXWIAGX1g='
    auth_user_150.last_login = dateutil.parser.parse("2013-10-05T01:33:34+00:00")
    auth_user_150.is_superuser = False
    auth_user_150.username = u'Moscow'
    auth_user_150.first_name = u''
    auth_user_150.last_name = u''
    auth_user_150.email = u''
    auth_user_150.is_staff = False
    auth_user_150.is_active = True
    auth_user_150.date_joined = dateutil.parser.parse("2013-10-05T01:33:33+00:00")
    auth_user_150 = importer.save_or_locate(auth_user_150)

    auth_user_151 = User()
    auth_user_151.password = u'pbkdf2_sha256$10000$Kykzwd7NFn32$rTUGcyiFIYAV4Ipqm9UKtWXGkC3ljkpWp2SSomIvHH4='
    auth_user_151.last_login = dateutil.parser.parse("2013-10-05T09:07:44+00:00")
    auth_user_151.is_superuser = False
    auth_user_151.username = u'Theta1106'
    auth_user_151.first_name = u''
    auth_user_151.last_name = u''
    auth_user_151.email = u''
    auth_user_151.is_staff = False
    auth_user_151.is_active = True
    auth_user_151.date_joined = dateutil.parser.parse("2013-10-05T09:07:44+00:00")
    auth_user_151 = importer.save_or_locate(auth_user_151)

    auth_user_152 = User()
    auth_user_152.password = u'pbkdf2_sha256$10000$Qkaki0Hng8j6$wi0ATPreUjHluakCI1veQ0i3p60thBl/alO1fO3cCWc='
    auth_user_152.last_login = dateutil.parser.parse("2013-10-08T22:30:32+00:00")
    auth_user_152.is_superuser = False
    auth_user_152.username = u'darkangel'
    auth_user_152.first_name = u''
    auth_user_152.last_name = u''
    auth_user_152.email = u''
    auth_user_152.is_staff = False
    auth_user_152.is_active = True
    auth_user_152.date_joined = dateutil.parser.parse("2013-10-08T22:30:31+00:00")
    auth_user_152 = importer.save_or_locate(auth_user_152)

    auth_user_153 = User()
    auth_user_153.password = u'pbkdf2_sha256$10000$dNUD8ra2WXiZ$5utscx9wkQhXv2mp2RDPJdiWWZuBh/Sxk4aSlP9Ak8A='
    auth_user_153.last_login = dateutil.parser.parse("2013-10-09T13:27:13+00:00")
    auth_user_153.is_superuser = False
    auth_user_153.username = u'Blacktalen'
    auth_user_153.first_name = u''
    auth_user_153.last_name = u''
    auth_user_153.email = u''
    auth_user_153.is_staff = False
    auth_user_153.is_active = True
    auth_user_153.date_joined = dateutil.parser.parse("2013-10-09T13:27:12+00:00")
    auth_user_153 = importer.save_or_locate(auth_user_153)

    auth_user_154 = User()
    auth_user_154.password = u'pbkdf2_sha256$10000$ne8Cc5V6Uufk$3AUHoBsrCkqW2mHKmdwTI0zYcfIq+BFQOLdQfv0vvfg='
    auth_user_154.last_login = dateutil.parser.parse("2013-10-09T13:54:28+00:00")
    auth_user_154.is_superuser = False
    auth_user_154.username = u'Truck156'
    auth_user_154.first_name = u''
    auth_user_154.last_name = u''
    auth_user_154.email = u''
    auth_user_154.is_staff = False
    auth_user_154.is_active = True
    auth_user_154.date_joined = dateutil.parser.parse("2013-10-09T13:54:28+00:00")
    auth_user_154 = importer.save_or_locate(auth_user_154)

    auth_user_155 = User()
    auth_user_155.password = u'pbkdf2_sha256$10000$4nWQLxDWdI8n$mMVEHxYL0EwJLvcqdSvhrcKYR6hJcCrKKjL/BF2B1bs='
    auth_user_155.last_login = dateutil.parser.parse("2013-10-09T19:10:29+00:00")
    auth_user_155.is_superuser = False
    auth_user_155.username = u'Cyberwolf74'
    auth_user_155.first_name = u''
    auth_user_155.last_name = u''
    auth_user_155.email = u''
    auth_user_155.is_staff = False
    auth_user_155.is_active = True
    auth_user_155.date_joined = dateutil.parser.parse("2013-10-09T19:10:28+00:00")
    auth_user_155 = importer.save_or_locate(auth_user_155)

    auth_user_156 = User()
    auth_user_156.password = u'pbkdf2_sha256$10000$aFxkwOr99hL1$OFNrtBI8VqUph+H+Y09CBXci0rlDtUpmneWBXBX2wls='
    auth_user_156.last_login = dateutil.parser.parse("2013-10-11T16:42:43+00:00")
    auth_user_156.is_superuser = False
    auth_user_156.username = u'Dogshead'
    auth_user_156.first_name = u''
    auth_user_156.last_name = u''
    auth_user_156.email = u''
    auth_user_156.is_staff = False
    auth_user_156.is_active = True
    auth_user_156.date_joined = dateutil.parser.parse("2013-10-11T16:42:43+00:00")
    auth_user_156 = importer.save_or_locate(auth_user_156)

    auth_user_157 = User()
    auth_user_157.password = u'pbkdf2_sha256$10000$GqWEyk5CgTbk$I6iwhtnJCGqgxnqpGdd61aUKJLFxio8t0cNkjhk1yKU='
    auth_user_157.last_login = dateutil.parser.parse("2013-10-13T09:10:41+00:00")
    auth_user_157.is_superuser = False
    auth_user_157.username = u'DangOleBoomhauer'
    auth_user_157.first_name = u''
    auth_user_157.last_name = u''
    auth_user_157.email = u''
    auth_user_157.is_staff = False
    auth_user_157.is_active = True
    auth_user_157.date_joined = dateutil.parser.parse("2013-10-13T09:10:41+00:00")
    auth_user_157 = importer.save_or_locate(auth_user_157)

    auth_user_158 = User()
    auth_user_158.password = u'pbkdf2_sha256$10000$Sdqt31XeMCXb$wsjsa5kubpZHyYPqxTGJyZNwwdLljr4Kud34mjYrt64='
    auth_user_158.last_login = dateutil.parser.parse("2013-10-13T11:58:04+00:00")
    auth_user_158.is_superuser = False
    auth_user_158.username = u'RavenOne'
    auth_user_158.first_name = u''
    auth_user_158.last_name = u''
    auth_user_158.email = u''
    auth_user_158.is_staff = False
    auth_user_158.is_active = True
    auth_user_158.date_joined = dateutil.parser.parse("2013-10-13T11:58:03+00:00")
    auth_user_158 = importer.save_or_locate(auth_user_158)

    auth_user_159 = User()
    auth_user_159.password = u'pbkdf2_sha256$10000$ZpC8Qbs9a3ES$xwpTChn5ju+1mYjd7WOi1mx1PeFwDjCIirezbcsCi/c='
    auth_user_159.last_login = dateutil.parser.parse("2013-10-13T23:30:19+00:00")
    auth_user_159.is_superuser = False
    auth_user_159.username = u'cyphyr'
    auth_user_159.first_name = u''
    auth_user_159.last_name = u''
    auth_user_159.email = u''
    auth_user_159.is_staff = False
    auth_user_159.is_active = True
    auth_user_159.date_joined = dateutil.parser.parse("2013-10-13T23:30:19+00:00")
    auth_user_159 = importer.save_or_locate(auth_user_159)

    auth_user_160 = User()
    auth_user_160.password = u'pbkdf2_sha256$10000$j8sTxMJbTd0u$4VgLX7r8rLT5YOfhJxL5H7ZZ0daTP0FBhm74ioGQS/g='
    auth_user_160.last_login = dateutil.parser.parse("2013-10-14T18:35:48+00:00")
    auth_user_160.is_superuser = False
    auth_user_160.username = u'PurpleBlob'
    auth_user_160.first_name = u''
    auth_user_160.last_name = u''
    auth_user_160.email = u''
    auth_user_160.is_staff = False
    auth_user_160.is_active = True
    auth_user_160.date_joined = dateutil.parser.parse("2013-10-14T18:33:35+00:00")
    auth_user_160 = importer.save_or_locate(auth_user_160)

    auth_user_161 = User()
    auth_user_161.password = u'pbkdf2_sha256$10000$DiFsOyCX2GeI$/63ZsDVf4fbSDLp7QRyuFjI5jZVXsKCR6zWQkXgqIK4='
    auth_user_161.last_login = dateutil.parser.parse("2013-10-15T03:23:18+00:00")
    auth_user_161.is_superuser = False
    auth_user_161.username = u'Wherder  Fugawi'
    auth_user_161.first_name = u''
    auth_user_161.last_name = u''
    auth_user_161.email = u''
    auth_user_161.is_staff = False
    auth_user_161.is_active = True
    auth_user_161.date_joined = dateutil.parser.parse("2013-10-15T03:23:17+00:00")
    auth_user_161 = importer.save_or_locate(auth_user_161)

    auth_user_162 = User()
    auth_user_162.password = u'pbkdf2_sha256$10000$ReigJsTdvuqn$lSTXLpIqDpZORMTBEISvTagwBDhmn/ksZ+PEO56tiq8='
    auth_user_162.last_login = dateutil.parser.parse("2013-10-15T09:32:43+00:00")
    auth_user_162.is_superuser = False
    auth_user_162.username = u'The.Doctor'
    auth_user_162.first_name = u''
    auth_user_162.last_name = u''
    auth_user_162.email = u''
    auth_user_162.is_staff = False
    auth_user_162.is_active = True
    auth_user_162.date_joined = dateutil.parser.parse("2013-10-15T09:32:43+00:00")
    auth_user_162 = importer.save_or_locate(auth_user_162)

    auth_user_163 = User()
    auth_user_163.password = u'pbkdf2_sha256$10000$u4ZlrT32r9pA$pq8Zm5t2AQUnFraZiPXBIq+x+p426I+6VqCYNsLIc18='
    auth_user_163.last_login = dateutil.parser.parse("2013-10-18T11:48:21+00:00")
    auth_user_163.is_superuser = False
    auth_user_163.username = u'MyklGee'
    auth_user_163.first_name = u''
    auth_user_163.last_name = u''
    auth_user_163.email = u''
    auth_user_163.is_staff = False
    auth_user_163.is_active = True
    auth_user_163.date_joined = dateutil.parser.parse("2013-10-18T11:48:21+00:00")
    auth_user_163 = importer.save_or_locate(auth_user_163)

    auth_user_164 = User()
    auth_user_164.password = u'pbkdf2_sha256$10000$NoFL8CmnbEvb$AYK+7PvFEKqx/24vBRLx7zRnTIDVBLMJghmYNnC4mew='
    auth_user_164.last_login = dateutil.parser.parse("2013-10-18T14:44:14+00:00")
    auth_user_164.is_superuser = False
    auth_user_164.username = u'Silver Gun'
    auth_user_164.first_name = u''
    auth_user_164.last_name = u''
    auth_user_164.email = u''
    auth_user_164.is_staff = False
    auth_user_164.is_active = True
    auth_user_164.date_joined = dateutil.parser.parse("2013-10-18T14:44:14+00:00")
    auth_user_164 = importer.save_or_locate(auth_user_164)

    auth_user_165 = User()
    auth_user_165.password = u'pbkdf2_sha256$10000$slZg3FhsHzqz$fjFLSsTtvNKiclN20VAi4K8aEWZ6nkR1l5BwJg3izWU='
    auth_user_165.last_login = dateutil.parser.parse("2013-10-19T04:49:36+00:00")
    auth_user_165.is_superuser = False
    auth_user_165.username = u'viper_two_fires'
    auth_user_165.first_name = u''
    auth_user_165.last_name = u''
    auth_user_165.email = u''
    auth_user_165.is_staff = False
    auth_user_165.is_active = True
    auth_user_165.date_joined = dateutil.parser.parse("2013-10-19T04:49:36+00:00")
    auth_user_165 = importer.save_or_locate(auth_user_165)

    auth_user_166 = User()
    auth_user_166.password = u'pbkdf2_sha256$10000$2w0PXKNEWjTE$1TCnkiQBuqrTw2Xo9Sz7GBJcIZcaYAXU3Tsp1JYDywM='
    auth_user_166.last_login = dateutil.parser.parse("2013-10-28T04:08:15+00:00")
    auth_user_166.is_superuser = False
    auth_user_166.username = u'Mithrim'
    auth_user_166.first_name = u''
    auth_user_166.last_name = u''
    auth_user_166.email = u''
    auth_user_166.is_staff = False
    auth_user_166.is_active = True
    auth_user_166.date_joined = dateutil.parser.parse("2013-10-28T04:07:02+00:00")
    auth_user_166 = importer.save_or_locate(auth_user_166)

    auth_user_167 = User()
    auth_user_167.password = u'pbkdf2_sha256$10000$Al75JPamBnNU$M8ALFX/IOX5FpAyBKHrQReSdVRf8WtDUsu+WUm4EfEM='
    auth_user_167.last_login = dateutil.parser.parse("2013-10-29T13:30:28+00:00")
    auth_user_167.is_superuser = False
    auth_user_167.username = u'xplod'
    auth_user_167.first_name = u''
    auth_user_167.last_name = u''
    auth_user_167.email = u''
    auth_user_167.is_staff = False
    auth_user_167.is_active = True
    auth_user_167.date_joined = dateutil.parser.parse("2013-10-29T13:30:28+00:00")
    auth_user_167 = importer.save_or_locate(auth_user_167)

    auth_user_168 = User()
    auth_user_168.password = u'pbkdf2_sha256$10000$h5dUYl05deuS$8pR5qQLqkY+CMgrOaixR8IO0mtzbbMVjSdxTeYCQUrI='
    auth_user_168.last_login = dateutil.parser.parse("2013-10-31T08:30:43+00:00")
    auth_user_168.is_superuser = False
    auth_user_168.username = u'Theripper749'
    auth_user_168.first_name = u''
    auth_user_168.last_name = u''
    auth_user_168.email = u''
    auth_user_168.is_staff = False
    auth_user_168.is_active = True
    auth_user_168.date_joined = dateutil.parser.parse("2013-10-31T08:30:43+00:00")
    auth_user_168 = importer.save_or_locate(auth_user_168)

    auth_user_169 = User()
    auth_user_169.password = u'pbkdf2_sha256$10000$Bv0vWpEzyAxy$RYNlApVx9WShGCgywbEdSCnMQ6vZW63MPWTd17td2Uo='
    auth_user_169.last_login = dateutil.parser.parse("2013-11-04T00:59:47+00:00")
    auth_user_169.is_superuser = False
    auth_user_169.username = u'ZipZerp'
    auth_user_169.first_name = u''
    auth_user_169.last_name = u''
    auth_user_169.email = u''
    auth_user_169.is_staff = False
    auth_user_169.is_active = True
    auth_user_169.date_joined = dateutil.parser.parse("2013-11-04T00:59:47+00:00")
    auth_user_169 = importer.save_or_locate(auth_user_169)

    auth_user_170 = User()
    auth_user_170.password = u'pbkdf2_sha256$10000$DHUvOMwjQJKL$/3I4Lkhf4MA9eARjnDAjWVidVt74WQKldmg9m8tXrBM='
    auth_user_170.last_login = dateutil.parser.parse("2013-11-08T06:26:27+00:00")
    auth_user_170.is_superuser = False
    auth_user_170.username = u'JackStone'
    auth_user_170.first_name = u''
    auth_user_170.last_name = u''
    auth_user_170.email = u''
    auth_user_170.is_staff = False
    auth_user_170.is_active = True
    auth_user_170.date_joined = dateutil.parser.parse("2013-11-08T06:26:27+00:00")
    auth_user_170 = importer.save_or_locate(auth_user_170)

    auth_user_171 = User()
    auth_user_171.password = u'pbkdf2_sha256$10000$49Xi5y2DuOXY$6o0Ii4cpARfPp7QfohQmeCB1CKt1i/jB4y3ZkHPBINo='
    auth_user_171.last_login = dateutil.parser.parse("2013-11-08T22:57:50+00:00")
    auth_user_171.is_superuser = False
    auth_user_171.username = u'Haragai'
    auth_user_171.first_name = u''
    auth_user_171.last_name = u''
    auth_user_171.email = u''
    auth_user_171.is_staff = False
    auth_user_171.is_active = True
    auth_user_171.date_joined = dateutil.parser.parse("2013-11-08T22:57:50+00:00")
    auth_user_171 = importer.save_or_locate(auth_user_171)

    auth_user_172 = User()
    auth_user_172.password = u'pbkdf2_sha256$10000$M90T9GDckSJP$CleQtWJDuVwhYmgGQ1AuN5FrHu4JWgIxPGtFw4W2D7A='
    auth_user_172.last_login = dateutil.parser.parse("2013-11-10T05:36:32+00:00")
    auth_user_172.is_superuser = False
    auth_user_172.username = u'ledzepplin'
    auth_user_172.first_name = u''
    auth_user_172.last_name = u''
    auth_user_172.email = u''
    auth_user_172.is_staff = False
    auth_user_172.is_active = True
    auth_user_172.date_joined = dateutil.parser.parse("2013-11-10T05:36:32+00:00")
    auth_user_172 = importer.save_or_locate(auth_user_172)

    auth_user_173 = User()
    auth_user_173.password = u'pbkdf2_sha256$10000$JKza0r8aqy9v$3Ennt9sPErSG4N8mG4nWmurpryI/lo0FDJiILScc77M='
    auth_user_173.last_login = dateutil.parser.parse("2013-11-10T19:59:46+00:00")
    auth_user_173.is_superuser = False
    auth_user_173.username = u'turian'
    auth_user_173.first_name = u''
    auth_user_173.last_name = u''
    auth_user_173.email = u''
    auth_user_173.is_staff = False
    auth_user_173.is_active = True
    auth_user_173.date_joined = dateutil.parser.parse("2013-11-10T19:59:45+00:00")
    auth_user_173 = importer.save_or_locate(auth_user_173)

    auth_user_174 = User()
    auth_user_174.password = u'pbkdf2_sha256$10000$VOM9inE1ExYN$hVNlj0cVvqI/2rRN3ptLKX3RjIMMm0gH+cFfS3gs+78='
    auth_user_174.last_login = dateutil.parser.parse("2013-11-12T12:09:10+00:00")
    auth_user_174.is_superuser = False
    auth_user_174.username = u'Aerial_ace'
    auth_user_174.first_name = u''
    auth_user_174.last_name = u''
    auth_user_174.email = u''
    auth_user_174.is_staff = False
    auth_user_174.is_active = True
    auth_user_174.date_joined = dateutil.parser.parse("2013-11-12T12:09:10+00:00")
    auth_user_174 = importer.save_or_locate(auth_user_174)

    auth_user_175 = User()
    auth_user_175.password = u'pbkdf2_sha256$10000$38lsjGFdNmlF$6wms/Jbfquelp2RN4HxqP6Is6hIVyoLTrpMZo9KFpvk='
    auth_user_175.last_login = dateutil.parser.parse("2013-12-02T15:54:23+00:00")
    auth_user_175.is_superuser = False
    auth_user_175.username = u'Barn'
    auth_user_175.first_name = u''
    auth_user_175.last_name = u''
    auth_user_175.email = u''
    auth_user_175.is_staff = False
    auth_user_175.is_active = True
    auth_user_175.date_joined = dateutil.parser.parse("2013-11-13T14:15:38+00:00")
    auth_user_175 = importer.save_or_locate(auth_user_175)

    auth_user_176 = User()
    auth_user_176.password = u'pbkdf2_sha256$10000$aSoVdJ3ytifl$+y+oUuR8cqbd8IPbfweAlHmAY/SKASzqiQOoxvS1IJY='
    auth_user_176.last_login = dateutil.parser.parse("2013-11-13T16:01:25+00:00")
    auth_user_176.is_superuser = False
    auth_user_176.username = u'romantok9@gmail.com'
    auth_user_176.first_name = u''
    auth_user_176.last_name = u''
    auth_user_176.email = u''
    auth_user_176.is_staff = False
    auth_user_176.is_active = True
    auth_user_176.date_joined = dateutil.parser.parse("2013-11-13T16:01:25+00:00")
    auth_user_176 = importer.save_or_locate(auth_user_176)

    auth_user_177 = User()
    auth_user_177.password = u'pbkdf2_sha256$10000$YXWzuu7yHvuv$HYOmNhvc5erJFw/1nyzEKSXiywuceEmoOJkj2y3UePY='
    auth_user_177.last_login = dateutil.parser.parse("2013-11-13T21:00:47+00:00")
    auth_user_177.is_superuser = False
    auth_user_177.username = u'shadows2597'
    auth_user_177.first_name = u''
    auth_user_177.last_name = u''
    auth_user_177.email = u''
    auth_user_177.is_staff = False
    auth_user_177.is_active = True
    auth_user_177.date_joined = dateutil.parser.parse("2013-11-13T21:00:47+00:00")
    auth_user_177 = importer.save_or_locate(auth_user_177)

    auth_user_178 = User()
    auth_user_178.password = u'pbkdf2_sha256$10000$18cETrb3npsn$YFhz/tNQ8RyEBQtm13f8h7Yn6rPCI2Or53EU51KBhRQ='
    auth_user_178.last_login = dateutil.parser.parse("2013-11-13T22:00:19+00:00")
    auth_user_178.is_superuser = False
    auth_user_178.username = u'Schming'
    auth_user_178.first_name = u''
    auth_user_178.last_name = u''
    auth_user_178.email = u''
    auth_user_178.is_staff = False
    auth_user_178.is_active = True
    auth_user_178.date_joined = dateutil.parser.parse("2013-11-13T22:00:19+00:00")
    auth_user_178 = importer.save_or_locate(auth_user_178)

    auth_user_179 = User()
    auth_user_179.password = u'pbkdf2_sha256$10000$lnqRpMFJFtyS$i42Cq8fEFFdL6CMXZVI8lN+HOQkiiADaQwFHxwNfOv4='
    auth_user_179.last_login = dateutil.parser.parse("2013-11-14T04:57:49+00:00")
    auth_user_179.is_superuser = False
    auth_user_179.username = u'Fyremaster'
    auth_user_179.first_name = u''
    auth_user_179.last_name = u''
    auth_user_179.email = u''
    auth_user_179.is_staff = False
    auth_user_179.is_active = True
    auth_user_179.date_joined = dateutil.parser.parse("2013-11-14T04:57:49+00:00")
    auth_user_179 = importer.save_or_locate(auth_user_179)

    auth_user_180 = User()
    auth_user_180.password = u'pbkdf2_sha256$10000$fzdcB0K5ZtLv$7V+1AzTj9vF48QrvDQICnX7NDdcuaZiJCuVvhGiSE8Y='
    auth_user_180.last_login = dateutil.parser.parse("2013-11-22T20:19:47+00:00")
    auth_user_180.is_superuser = False
    auth_user_180.username = u'OzWookiee'
    auth_user_180.first_name = u''
    auth_user_180.last_name = u''
    auth_user_180.email = u''
    auth_user_180.is_staff = False
    auth_user_180.is_active = True
    auth_user_180.date_joined = dateutil.parser.parse("2013-11-22T20:19:47+00:00")
    auth_user_180 = importer.save_or_locate(auth_user_180)

    auth_user_181 = User()
    auth_user_181.password = u'pbkdf2_sha256$10000$EbB8q4q8LqpF$5Gy+Hjy4c+eSAQRcGo52fDucR7DjrF2oGFYjtwdk8KU='
    auth_user_181.last_login = dateutil.parser.parse("2013-11-23T23:33:14+00:00")
    auth_user_181.is_superuser = False
    auth_user_181.username = u'Serpan'
    auth_user_181.first_name = u''
    auth_user_181.last_name = u''
    auth_user_181.email = u''
    auth_user_181.is_staff = False
    auth_user_181.is_active = True
    auth_user_181.date_joined = dateutil.parser.parse("2013-11-23T23:33:14+00:00")
    auth_user_181 = importer.save_or_locate(auth_user_181)

    auth_user_182 = User()
    auth_user_182.password = u'pbkdf2_sha256$10000$XtUSgbp3VwbM$JNcI1dB/3N8pgtpgo966MvUW3+TMMRazzGFbcHdoK5Q='
    auth_user_182.last_login = dateutil.parser.parse("2013-11-28T17:54:50+00:00")
    auth_user_182.is_superuser = False
    auth_user_182.username = u'alsky'
    auth_user_182.first_name = u''
    auth_user_182.last_name = u''
    auth_user_182.email = u''
    auth_user_182.is_staff = False
    auth_user_182.is_active = True
    auth_user_182.date_joined = dateutil.parser.parse("2013-11-28T17:54:50+00:00")
    auth_user_182 = importer.save_or_locate(auth_user_182)

    auth_user_183 = User()
    auth_user_183.password = u'pbkdf2_sha256$10000$P1shgxnI2k5m$nrt4YprBv1BfQEfqlWHembgxvban3mRx9C291PyROAQ='
    auth_user_183.last_login = dateutil.parser.parse("2013-12-01T18:26:11+00:00")
    auth_user_183.is_superuser = False
    auth_user_183.username = u'spetnaz'
    auth_user_183.first_name = u''
    auth_user_183.last_name = u''
    auth_user_183.email = u''
    auth_user_183.is_staff = False
    auth_user_183.is_active = True
    auth_user_183.date_joined = dateutil.parser.parse("2013-12-01T18:26:11+00:00")
    auth_user_183 = importer.save_or_locate(auth_user_183)

    auth_user_184 = User()
    auth_user_184.password = u'pbkdf2_sha256$10000$zpCVVyZb56od$HBjElMRFUQ+0BaX6zH2NKFWw21WldL3K/lx9XxFU9GQ='
    auth_user_184.last_login = dateutil.parser.parse("2013-12-04T17:46:20+00:00")
    auth_user_184.is_superuser = False
    auth_user_184.username = u'mikalis'
    auth_user_184.first_name = u''
    auth_user_184.last_name = u''
    auth_user_184.email = u''
    auth_user_184.is_staff = False
    auth_user_184.is_active = True
    auth_user_184.date_joined = dateutil.parser.parse("2013-12-04T17:46:20+00:00")
    auth_user_184 = importer.save_or_locate(auth_user_184)

    auth_user_185 = User()
    auth_user_185.password = u'pbkdf2_sha256$10000$BrMVILONoHyF$oh2maT5kM7IsJJ0DAx92aZoPaI0iHXMEOkbMy2rBT0c='
    auth_user_185.last_login = dateutil.parser.parse("2013-12-08T19:53:42+00:00")
    auth_user_185.is_superuser = False
    auth_user_185.username = u'xaver26'
    auth_user_185.first_name = u''
    auth_user_185.last_name = u''
    auth_user_185.email = u''
    auth_user_185.is_staff = False
    auth_user_185.is_active = True
    auth_user_185.date_joined = dateutil.parser.parse("2013-12-08T19:53:42+00:00")
    auth_user_185 = importer.save_or_locate(auth_user_185)

    auth_user_186 = User()
    auth_user_186.password = u'pbkdf2_sha256$10000$CSKNkudFeXXY$WOoZLk8n/hqXqN2vtBKeC0paFKbxdA1jgKbc13LhAxI='
    auth_user_186.last_login = dateutil.parser.parse("2013-12-12T10:56:14+00:00")
    auth_user_186.is_superuser = False
    auth_user_186.username = u'dochunt61'
    auth_user_186.first_name = u''
    auth_user_186.last_name = u''
    auth_user_186.email = u''
    auth_user_186.is_staff = False
    auth_user_186.is_active = True
    auth_user_186.date_joined = dateutil.parser.parse("2013-12-12T10:56:14+00:00")
    auth_user_186 = importer.save_or_locate(auth_user_186)

    auth_user_187 = User()
    auth_user_187.password = u'pbkdf2_sha256$10000$x231rO9MMjC5$xLjDgY0t2grtxpXqmZcOkqoRiQKAGMVrMTcEaylEOxk='
    auth_user_187.last_login = dateutil.parser.parse("2013-12-19T10:43:12+00:00")
    auth_user_187.is_superuser = False
    auth_user_187.username = u'TheOTHERmaninblack'
    auth_user_187.first_name = u''
    auth_user_187.last_name = u''
    auth_user_187.email = u''
    auth_user_187.is_staff = False
    auth_user_187.is_active = True
    auth_user_187.date_joined = dateutil.parser.parse("2013-12-19T10:43:12+00:00")
    auth_user_187 = importer.save_or_locate(auth_user_187)

    auth_user_188 = User()
    auth_user_188.password = u'pbkdf2_sha256$10000$qCZLdYkQdFIV$hWBjaxsKDgvzILFR2CZWoGg+XGElRlc+ix/gZ1Jei+A='
    auth_user_188.last_login = dateutil.parser.parse("2014-02-17T01:20:48+00:00")
    auth_user_188.is_superuser = False
    auth_user_188.username = u'Ryujin'
    auth_user_188.first_name = u''
    auth_user_188.last_name = u''
    auth_user_188.email = u''
    auth_user_188.is_staff = False
    auth_user_188.is_active = True
    auth_user_188.date_joined = dateutil.parser.parse("2014-02-17T01:19:22+00:00")
    auth_user_188 = importer.save_or_locate(auth_user_188)

    auth_user_189 = User()
    auth_user_189.password = u'pbkdf2_sha256$10000$MyWFKfwBzB3U$DeLIggFtM6kHz2BkwubsqiC6S7/3EhspR+gHUAwMVHA='
    auth_user_189.last_login = dateutil.parser.parse("2014-05-18T08:48:19+00:00")
    auth_user_189.is_superuser = False
    auth_user_189.username = u'OldBloke'
    auth_user_189.first_name = u''
    auth_user_189.last_name = u''
    auth_user_189.email = u''
    auth_user_189.is_staff = False
    auth_user_189.is_active = True
    auth_user_189.date_joined = dateutil.parser.parse("2014-05-18T08:48:19+00:00")
    auth_user_189 = importer.save_or_locate(auth_user_189)
