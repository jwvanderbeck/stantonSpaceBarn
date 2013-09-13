# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ItemPort.topLeft'
        db.add_column(u'shipBuilder_itemport', 'topLeft',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ItemPort.topRight'
        db.add_column(u'shipBuilder_itemport', 'topRight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ItemPort.bottomLeft'
        db.add_column(u'shipBuilder_itemport', 'bottomLeft',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ItemPort.bottomRight'
        db.add_column(u'shipBuilder_itemport', 'bottomRight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'ItemPort.tagLocationY'
        db.alter_column(u'shipBuilder_itemport', 'tagLocationY', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'ItemPort.tagLocationX'
        db.alter_column(u'shipBuilder_itemport', 'tagLocationX', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):
        # Deleting field 'ItemPort.topLeft'
        db.delete_column(u'shipBuilder_itemport', 'topLeft')

        # Deleting field 'ItemPort.topRight'
        db.delete_column(u'shipBuilder_itemport', 'topRight')

        # Deleting field 'ItemPort.bottomLeft'
        db.delete_column(u'shipBuilder_itemport', 'bottomLeft')

        # Deleting field 'ItemPort.bottomRight'
        db.delete_column(u'shipBuilder_itemport', 'bottomRight')


        # Changing field 'ItemPort.tagLocationY'
        db.alter_column(u'shipBuilder_itemport', 'tagLocationY', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'ItemPort.tagLocationX'
        db.alter_column(u'shipBuilder_itemport', 'tagLocationX', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'shipBuilder.build': {
            'Meta': {'object_name': 'Build'},
            'base_ship': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cargo_mod': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'build_cargo_hold'", 'null': 'True', 'blank': 'True', 'to': u"orm['shipBuilder.Item']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'down_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'engine_intake': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'build_engine_intake'", 'null': 'True', 'blank': 'True', 'to': u"orm['shipBuilder.Item']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_thruster': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'build_main_thruster'", 'null': 'True', 'blank': 'True', 'to': u"orm['shipBuilder.Item']"}),
            'manufacturer_variant': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'powerplant': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'build_powerplant'", 'null': 'True', 'blank': 'True', 'to': u"orm['shipBuilder.Item']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'shield': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'build_shield'", 'null': 'True', 'blank': 'True', 'to': u"orm['shipBuilder.Item']"}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Ship']"}),
            'up_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'shipBuilder.buildenginemod': {
            'Meta': {'object_name': 'BuildEngineMod'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['shipBuilder.Item']", 'null': 'True', 'blank': 'True'})
        },
        u'shipBuilder.buildhardpoint': {
            'Meta': {'object_name': 'BuildHardpoint'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Build']"}),
            'hardpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Hardpoint']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['shipBuilder.Item']", 'null': 'True', 'blank': 'True'})
        },
        u'shipBuilder.buildhullmod': {
            'Meta': {'object_name': 'BuildHullMod'},
            'build': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Build']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['shipBuilder.Item']", 'null': 'True', 'blank': 'True'})
        },
        u'shipBuilder.cargomoddata': {
            'Meta': {'object_name': 'CargoModData'},
            'cargo_capacity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'supported_ships': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['shipBuilder.Ship']", 'symmetrical': 'False'})
        },
        u'shipBuilder.engineintakedata': {
            'Meta': {'object_name': 'EngineIntakeData'},
            'fuel_efficiency': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'shipBuilder.hardpoint': {
            'Meta': {'object_name': 'Hardpoint'},
            'hardpoint_class': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['shipBuilder.Image']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'overlay_location_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'overlay_location_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Ship']"}),
            'tag_location_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tag_location_y': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'shipBuilder.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Ship']"}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'})
        },
        u'shipBuilder.item': {
            'Meta': {'object_name': 'Item'},
            'cargo_mod_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.CargoModData']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'energy': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'engine_intake_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.EngineIntakeData']", 'null': 'True', 'blank': 'True'}),
            'hardpoint_class': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.ItemCategory']"}),
            'item_type': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['shipBuilder.ItemType']"}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Manufacturer']"}),
            'mass': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'memory': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'power': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'powerplant_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.PowerplantData']", 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'shield_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.ShieldData']", 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'supported_hardpoints': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.Hardpoint']", 'null': 'True', 'blank': 'True'}),
            'thruster_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.ThrusterData']", 'null': 'True', 'blank': 'True'}),
            'upgrade_slots': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'weapon_data': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.WeaponData']", 'null': 'True', 'blank': 'True'})
        },
        u'shipBuilder.itemcategory': {
            'Meta': {'object_name': 'ItemCategory'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'shipBuilder.itemport': {
            'Meta': {'object_name': 'ItemPort'},
            'bottomLeft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bottomRight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'displayName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'flags': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Image']", 'null': 'True', 'blank': 'True'}),
            'maxSize': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'minSize': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parentVehicle': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Vehicle']", 'null': 'True', 'blank': 'True'}),
            'portClass': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'supportedSubTypes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.VehicleItemSubType']", 'null': 'True', 'blank': 'True'}),
            'supportedTypes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.VehicleItemType']", 'null': 'True', 'blank': 'True'}),
            'tagLocationX': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'tagLocationY': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'topLeft': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'topRight': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'shipBuilder.itemtype': {
            'Meta': {'object_name': 'ItemType'},
            'hardpoint_type': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'shipBuilder.manufacturer': {
            'Meta': {'object_name': 'Manufacturer'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'})
        },
        u'shipBuilder.powerplantdata': {
            'Meta': {'object_name': 'PowerplantData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'power_rating': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'powerplant_class': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'shipBuilder.shielddata': {
            'Meta': {'object_name': 'ShieldData'},
            'absorption': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'shipBuilder.ship': {
            'Meta': {'object_name': 'Ship'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'control_thruster_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '8'}),
            'control_thruster_max_rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'empty_mass': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'main_thruster_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'main_thruster_max_rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Manufacturer']"}),
            'maximum_crew': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'memory_capacity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'powerplant_class_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'ship_class': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'}),
            'upgrade_capacity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'width': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'shipBuilder.thrusterdata': {
            'Meta': {'object_name': 'ThrusterData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thrust_generated': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'thrust_rating': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'shipBuilder.vehicle': {
            'Meta': {'object_name': 'Vehicle'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.VehicleCategory']"}),
            'displayName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'empty_mass': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'height': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layoutImageBottomLeft': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'layoutImageBottomRight': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'layoutImageTopLeft': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'layoutImageTopRight': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Manufacturer']", 'null': 'True', 'blank': 'True'}),
            'maximum_crew': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'upgradeSlots': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'vehicleClass': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'width': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'shipBuilder.vehiclecategory': {
            'Meta': {'object_name': 'VehicleCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shipBuilder.vehicleimage': {
            'Meta': {'object_name': 'VehicleImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'ship': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Vehicle']"}),
            'url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200'})
        },
        u'shipBuilder.vehicleitem': {
            'Meta': {'object_name': 'VehicleItem'},
            'avionics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.VehicleItemAvionics']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'displayName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'heat': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.VehicleItemHeat']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemClass': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'itemSize': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'itemStats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.VehicleItemParams']", 'null': 'True', 'blank': 'True'}),
            'itemSubType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.VehicleItemSubType']"}),
            'itemType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.VehicleItemType']"}),
            'manufacturer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.Manufacturer']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'power': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['shipBuilder.VehicleItemPower']", 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'shipBuilder.vehicleitemavionics': {
            'Meta': {'object_name': 'VehicleItemAvionics'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shipBuilder.vehicleitemheat': {
            'Meta': {'object_name': 'VehicleItemHeat'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shipBuilder.vehicleitemparams': {
            'Meta': {'object_name': 'VehicleItemParams'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'shipBuilder.vehicleitempower': {
            'Meta': {'object_name': 'VehicleItemPower'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shipBuilder.vehicleitemsubtype': {
            'Meta': {'object_name': 'VehicleItemSubType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['shipBuilder.VehicleItemType']"}),
            'subTypeName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shipBuilder.vehicleitemtype': {
            'Meta': {'object_name': 'VehicleItemType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'typeName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'shipBuilder.weapondata': {
            'Meta': {'object_name': 'WeaponData'},
            'damage': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'explosive_radius': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'missile_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rate_of_fire': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'velocity': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        }
    }

    complete_apps = ['shipBuilder']