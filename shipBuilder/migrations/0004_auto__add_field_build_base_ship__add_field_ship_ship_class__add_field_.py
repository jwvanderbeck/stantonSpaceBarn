# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Build.base_ship'
        db.add_column(u'shipBuilder_build', 'base_ship',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Ship.ship_class'
        db.add_column(u'shipBuilder_ship', 'ship_class',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'WeaponData.velocity'
        db.add_column(u'shipBuilder_weapondata', 'velocity',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Item.rating'
        db.add_column(u'shipBuilder_item', 'rating',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Item.size'
        db.add_column(u'shipBuilder_item', 'size',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Item.energy'
        db.add_column(u'shipBuilder_item', 'energy',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Build.base_ship'
        db.delete_column(u'shipBuilder_build', 'base_ship')

        # Deleting field 'Ship.ship_class'
        db.delete_column(u'shipBuilder_ship', 'ship_class')

        # Deleting field 'WeaponData.velocity'
        db.delete_column(u'shipBuilder_weapondata', 'velocity')

        # Deleting field 'Item.rating'
        db.delete_column(u'shipBuilder_item', 'rating')

        # Deleting field 'Item.size'
        db.delete_column(u'shipBuilder_item', 'size')

        # Deleting field 'Item.energy'
        db.delete_column(u'shipBuilder_item', 'energy')


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