from django.db import models
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.name

class ItemCategory(models.Model):
    description = models.CharField(max_length=30, default='')
    
    def __unicode__(self):
        return self.description

class ItemType(models.Model):
    name = models.CharField(max_length=30, default='')
    hardpoint_type = models.BooleanField(default=False)

    def __unicode__(self):
        if self.hardpoint_type:
            return "%s (Hardpoint)" % (self.name)
        else:
            return self.name

class Item(models.Model):
    name = models.CharField(max_length = 30, default='')
    rating = models.PositiveIntegerField(default=1)
    size = models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=True)
    manufacturer = models.ForeignKey(Manufacturer)
    item_category = models.ForeignKey(ItemCategory)
    hardpoint_class = models.PositiveIntegerField(default=0,blank=True,null=True)
    supported_hardpoints = models.ManyToManyField('Hardpoint', blank=True, null=True)
    mass = models.FloatField(default=0.0)
    item_type = models.ForeignKey('ItemType', default=0)
    power = models.FloatField(default=0.0)
    energy = models.FloatField(default=0.0)
    memory = models.FloatField(default=0.0)
    upgrade_slots = models.PositiveIntegerField(default=1)
    weapon_data = models.ForeignKey('WeaponData', null=True, blank=True)
    cargo_mod_data = models.ForeignKey('CargoModData', null=True, blank=True)
    powerplant_data = models.ForeignKey('PowerplantData', null=True, blank=True)
    thruster_data = models.ForeignKey('ThrusterData', null=True, blank=True)
    shield_data = models.ForeignKey('ShieldData', null=True, blank=True)
    engine_intake_data = models.ForeignKey('EngineIntakeData', null=True, blank=True)
    
    # These field definitions are used to make the code everywhere else cleaner and easier to maintain
    #   Any time the model changes, these fields need to be updated -- but at least it is all in one spot!
    trackedFields = {
        'item' : [
            'id',
            'manufacturer',
            'name',
            'mass',
            'power',
            'memory',
            'upgrade_slots'
            ],
        'Cargo Expansion' : [
            'cargo_capacity'
        ],
        'Powerplant' : [
            'power_rating',
            'powerplant_class'
        ],
        'Main Thruster' : [
            'thrust_rating'
        ]
    }
    displayedFields = {
        'item' : [
            'manufacturer',
            'name',
            'mass',
            'power',
            'memory',
            'upgrade_slots'
        ],
        'Gun' : [
            'rate_of_fire',
            'damage'
        ],
        'Missile Launcher' : [
            'rate_of_fire',
            'damage',
            'explosive_radius',
            'missile_count'
        ],
        'Shield' : [
            'absorption'
        ],
        'Cargo Expansion' : [
            'cargo_capacity'
        ],
        'Powerplant' : [
            'powerplant_class',
            'power_rating'
        ],
        'Main Thruster' : [
            'thrust_rating',
            'thrust_generated'
        ]
    }
    
    def __unicode__(self):
        category = self.item_category.description
        linkedData = None
        if category == 'Gun':
            linkedData = self.weapon_data
        elif category == 'Missile Launcher':
            linkedData = self.weapon_data
        elif category == 'Shield':
            linkedData = self.shield_data
        elif category == 'Cargo Expansion':
            linkedData = self.cargo_mod_data
        elif category == 'Powerplant':
            linkedData = self.powerplant_data
        elif category == 'Main Thruster':
            linkedData = self.thruster_data
        base = u"%s (%s/%s)" % (self.name, self.item_type.name, self.item_category.description)
        if linkedData:
            return base + ': %s' % linkedData
        else:
            return base

    def tableHeader(self):
        output = "<thead><tr>"
        for field in self.displayedFields['item']:
            output = output + str.format("<th>{0}</th>", field.replace('_', ' '))
        if self.item_type.hardpoint_type:
            output = output + str.format("<th>Hardpoint Class</th>")

        if self.item_category.description in self.displayedFields:
            for field in self.displayedFields[self.item_category.description]:
                output = output + str.format("<th>{0}</th>", field.replace('_', ' '))

        output = output + '</tr></thead>'
        return mark_safe(output)


    def asTableRow(self):
        category = self.item_category.description
        itemType = self.item_type.name
        linkedData = None
        if category == 'Gun':
            linkedData = self.weapon_data
        elif category == 'Missile Launcher':
            linkedData = self.weapon_data
        elif category == 'Shield':
            linkedData = self.shield_data
        elif category == 'Cargo Expansion':
            linkedData = self.cargo_mod_data
        elif category == 'Powerplant':
            linkedData = self.powerplant_data
        elif category == 'Main Thruster':
            linkedData = self.thruster_data

        # Data tracked fields
        output = "<tr "
        if self.item_type.hardpoint_type:
            output = output + "class='hardpoint-item'"
        else:
            output = output + "class='datablock-item'"
        for field in self.trackedFields['item']:
            output = output + str.format(" data-item-{0}='{1}'", field.replace('_', '-'), getattr(self, field))
        if linkedData and category in self.trackedFields:
            for field in self.trackedFields[category]:
                output = output + str.format(" data-item-{0}='{1}'", field.replace('_', '-'), getattr(linkedData, field))
        output = output + ">"

        # Displayed fields
        for field in self.displayedFields['item']:
            output = output + str.format("<td>{0}</td>", getattr(self, field))

        if self.item_type.hardpoint_type:
            output = output + str.format("<td>{0}</td>", getattr(self, 'hardpoint_class'))

        if linkedData and category in self.displayedFields:
            for field in self.displayedFields[category]:
                output = output + str.format("<td>{0}</td>", getattr(linkedData, field))
        output = output + '</tr>'

        return mark_safe(output)


class WeaponData(models.Model):
    rate_of_fire = models.FloatField(default=0.0,blank=True,null=True)
    explosive_radius = models.FloatField(default=0.0,blank=True,null=True)
    missile_count = models.PositiveIntegerField(blank=True, null=True)
    # Fields seen in Hangar Video
    # Looks like they display as bargraphs, so might want to normalize
    # values at say 0-100
    damage = models.FloatField(default=0.0,blank=True,null=True)
    velocity = models.FloatField(default=0.0)

    def __unicode__(self):
        if self.rate_of_fire >= 0.1:
            return u"RoF: %.2fs, Damage: %.2f, Radius: %.2f Meters, DPS: %.2f" % (self.rate_of_fire, self.damage, self.explosive_radius, (1.0 / self.rate_of_fire) * self.damage)
        else:
            return u"RoF: %.2fs, Damage: %.2f, Radius: %.2f Meters, DPS: 0" % (self.rate_of_fire, self.damage, self.explosive_radius)

class CargoModData(models.Model):
    cargo_capacity = models.PositiveIntegerField(default=0)
    supported_ships = models.ManyToManyField('Ship')

    def __unicode__(self):
        return u"Capacity: %d" % self.cargo_capacity

class PowerplantData(models.Model):
    powerplant_class = models.PositiveIntegerField(default=1)
    power_rating = models.FloatField(default=0.0)
    # supported_ships = models.ManyToManyField('Ship', null=True, blank=True, default=0)

    def __unicode__(self):
        return u"Class %s (%.2f MW)" % (self.powerplant_class, self.power_rating)

class ThrusterData(models.Model):
    thrust_generated = models.FloatField(default=0.0)
    thrust_rating = models.PositiveIntegerField(default=1)
    # supported_ships = models.ManyToManyField('Ship', null=True, blank=True, default=0)

    def __unicode__(self):
        return u"%.2fN TR%d" % (self.thrust_generated, self.thrust_rating)

class ShieldData(models.Model):
    absorption = models.FloatField(default=0.0)
    # supported_ships = models.ManyToManyField('Ship', null=True, blank=True, default=0)

    def __unicode__(self):
        return u"%.2f Absorption" % (self.absorption)

class EngineIntakeData(models.Model):
    fuel_efficiency = models.FloatField(default=0.0)
    # supported_ships = models.ManyToManyField('Ship', null=True, blank=True, default=0)

    def __unicode__(self):
        return u"%.2f Efficiency Rating" % (self.fuel_efficiency)

class Ship(models.Model):
    # The Ship model stores the cmmon stock information
    # about the BASE unmodified ships available in the game
    # The Build model is what stores the ship plus all the mods
    name = models.CharField(max_length = 30, default='')
    manufacturer = models.ForeignKey(Manufacturer)
    description = models.TextField(max_length=255, blank=True)
    maximum_crew = models.PositiveIntegerField(default=1)
    empty_mass = models.BigIntegerField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    height = models.FloatField(default=0)
    upgrade_capacity = models.PositiveIntegerField(default=1)
    memory_capacity = models.PositiveIntegerField(default=0)
    main_thruster_count = models.PositiveIntegerField(default=1)
    main_thruster_max_rating = models.PositiveIntegerField(default=1)
    control_thruster_count = models.PositiveIntegerField(default=8)
    control_thruster_max_rating = models.PositiveIntegerField(default=1)
    powerplant_class_max = models.PositiveIntegerField(default=1)
    thumbnail = models.URLField(default='')
    available = models.BooleanField(default=False)
    ship_class = models.PositiveIntegerField(default=1)
    
    def __unicode__(self):
        return self.name

class Hardpoint(models.Model):
    name = models.CharField(max_length = 30, default='', blank=True)
    hardpoint_class = models.PositiveIntegerField(default=1)
    overlay_location_x = models.IntegerField(default=0)
    overlay_location_y = models.IntegerField(default=0)
    tag_location_x = models.IntegerField(default=0)
    tag_location_y = models.IntegerField(default=0)
    ship = models.ForeignKey(Ship)
    image = models.ForeignKey('Image', default=0, null=True, blank=True)
    
    def __unicode__(self):
        return "%s: %s, Class %d Hardpoint" % (self.ship.name, self.name, self.hardpoint_class)

class Image(models.Model):
    url = models.URLField(default='')
    name = models.CharField(max_length=30, default='')
    ship = models.ForeignKey(Ship)
    
    def __unicode__(self):
        return self.name
    
class BuildHardpoint(models.Model):
    # This table defines the links between item->hardpoint->build
    build = models.ForeignKey('Build')
    hardpoint = models.ForeignKey('Hardpoint')
    item = models.ForeignKey('Item', blank=True, null=True, default=None)

    def __unicode__(self):
        return "%s:%s:Hardpoint ID#%d:%s" % (self.build.ship.name, self.build.name, self.hardpoint.id, self.item)

class BuildEngineMod(models.Model):
    build = models.ForeignKey('Build');
    item = models.ForeignKey('Item', blank=True, null=True, default=None)
    def __unicode__(self):
        return "%s:%s:Engine Mod:%s" % (self.build.ship.name, self.build.name, self.item)

class BuildHullMod(models.Model):
    build = models.ForeignKey('Build');
    item = models.ForeignKey('Item', blank=True, null=True, default=None)
    def __unicode__(self):
        return "%s:%s:Hull Mod:%s" % (self.build.ship.name, self.build.name, self.item)


class Build(models.Model):
    created_by = models.ForeignKey(User, blank=True, null=True, default=None)
    name = models.CharField(max_length=30, default='')
    role = models.CharField(max_length=30, blank=True)
    ship = models.ForeignKey(Ship)
    manufacturer_variant = models.BooleanField(default=False)
    engine_intake = models.ForeignKey('Item', blank=True, null=True, default=None, related_name='build_engine_intake')
    powerplant = models.ForeignKey('Item', blank=True, null=True, default=None, related_name='build_powerplant')
    main_thruster = models.ForeignKey('Item', blank=True, null=True, default=None, related_name='build_main_thruster')
    shield = models.ForeignKey('Item', blank=True, null=True, default=None, related_name='build_shield')
    cargo_mod = models.ForeignKey('Item', blank=True, null=True, default=None, related_name='build_cargo_hold')
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    base_ship = models.BooleanField(default=False)


    def __unicode__(self):
        return "%s %s variant:%s" % (self.ship.name, self.role, self.name)


######################################################
## Phase 2
## New models based on actual game data rather than
## best guesses!
######################################################

### Vehicle Items

class VehicleItemType(models.Model):
    typeName = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.typeName

class VehicleItemSubType(models.Model):
    subTypeName = models.CharField(max_length = 255)
    parent = models.ForeignKey('VehicleItemType')

    def __unicode__(self):
        return self.subTypeName

class VehicleItemParams(models.Model):
    name = models.CharField(max_length = 255)
    value = models.FloatField(default = 0.0)
    parentItem = models.ForeignKey('VehicleItem')

    def __unicode__(self):
        return u"%s - %s:%.2f" % (self.parentItem.name, self.name, self.value)

class VehicleItemPower(models.Model):
    state = models.CharField(max_length = 128)
    # Value couldbe a packed value curve
    value = models.CharField(max_length = 255)
    parentItem = models.ForeignKey('VehicleItem')

    def __unicode__(self):
        return u"(%s)%s - %s" % (self.parentItem.name, self.state, self.value)

class VehicleItemHeat(models.Model):
    state = models.CharField(max_length = 128)
    # Value couldbe a packed value curve
    value = models.CharField(max_length = 255)
    parentItem = models.ForeignKey('VehicleItem')

    def __unicode__(self):
        return u"(%s)%s - %s" % (self.parentItem.name, self.state, self.value)

class VehicleItemAvionics(models.Model):
    state = models.CharField(max_length = 128)
    # Value couldbe a packed value curve
    value = models.CharField(max_length = 255)
    parentItem = models.ForeignKey('VehicleItem')

    def __unicode__(self):
        return u"(%s)%s - %s" % (self.parentItem.name, self.state, self.value)

class VehicleItem(models.Model):
    itemClass = models.PositiveIntegerField(default = 1)
    description = models.TextField(blank = True)
    name = models.CharField(max_length = 255)
    displayName = models.CharField(max_length = 255, blank = True)
    itemType = models.ForeignKey('VehicleItemType')
    itemSubType = models.ForeignKey('VehicleItemSubType')
    manufacturer = models.ForeignKey('Manufacturer')
    itemSize = models.PositiveIntegerField(default = 0)
    # Additional fields required for The Barn
    views = models.PositiveIntegerField(default = 0)

    def __unicode__(self):
        return u"%s" % (self.name)

### Vehicles
class VehicleImage(models.Model):
    url = models.URLField(default = '')
    name = models.CharField(max_length = 255, default = '')
    ship = models.ForeignKey('Vehicle')
    tags = models.ManyToManyField('HardpointTag', blank = True, null = True)
    
    def __unicode__(self):
        return self.name

class ItemPort(models.Model):
    # Basic fields as required by game model
    displayName = models.CharField(max_length = 255, blank = True)
    name = models.CharField(max_length = 255)
    flags = models.CharField(max_length = 512, blank = True)
    maxSize = models.PositiveIntegerField(default = 1)
    minSize = models.PositiveIntegerField(default = 0)
    supportedTypes = models.ManyToManyField('VehicleItemType', blank = True, null = True) 
    supportedSubTypes = models.ManyToManyField('VehicleItemSubType', blank = True, null = True)
    parentVehicle = models.ForeignKey('Vehicle', blank = True, null = True)
    parentItem = models.ForeignKey('VehicleItem', blank = True, null = True)
    # Added just in case the game starts using it
    portClass = models.PositiveIntegerField(default = 0)
    # Additional fields required for The Barn
    # 1 = TopRight, 2 = TopLeft, 3 = BottomRightLeft, 4 = BottomRight
    parentImage = models.PositiveIntegerField(default = 0)
    image = models.ForeignKey('Image', null = True, blank = True)
    tagLocationX = models.FloatField(default = 0.0)
    tagLocationY = models.FloatField(default = 0.0)

    def __unicode__(self):
        if self.displayName and self.displayName != "":
            name = self.displayName
        else:
            name = self.name
        return u"%s: %s (%d-%d) %s" % (self.parentVehicle, name, self.minSize, self.maxSize, self.supportedTypes.all())

class VehicleCategory(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

class Vehicle(models.Model):
    # Basic fields as required by game model
    vehicleClass = models.PositiveIntegerField(default = 1)
    category = models.ForeignKey('VehicleCategory')
    displayName = models.CharField(max_length = 255, blank = True)
    name = models.CharField(max_length = 255)
    # Additional fields required for The Barn
    views = models.PositiveIntegerField(default = 0)
    upgradeSlots = models.PositiveIntegerField(default = 0)
    maximum_crew = models.PositiveIntegerField(default = 1)
    empty_mass = models.BigIntegerField(default = 0)
    length = models.FloatField(default = 0)
    width = models.FloatField(default = 0)
    height = models.FloatField(default = 0)
    thumbnail = models.URLField(default='', blank = True)
    available = models.BooleanField(default = False)
    manufacturer = models.ForeignKey('Manufacturer', blank = True, null = True)
    layoutImageTopRight = models.URLField(blank = True)
    layoutImageTopLeft = models.URLField(blank = True)
    layoutImageBottomRight = models.URLField(blank = True)
    layoutImageBottomLeft = models.URLField(blank = True)

    def __unicode__(self):
        if self.displayName and self.displayName != "":
            name = self.displayName
        else:
            name = self.name
        return u"%s Class %d %s" % (name, self.vehicleClass, self.category)
            
class HardpointTag(models.Model):
    hardpoint = models.ForeignKey('ItemPort', blank = True, null = True);
    locationX = models.FloatField(default = 0)
    locationY = models.FloatField(default = 0)

class VariantItem(models.Model):
    variant = models.ForeignKey("Variant", blank=True, null=True)
    item = models.CharField(max_length = 255, blank=True)
    port = models.CharField(max_length = 255, blank=True)
    parentPort = models.CharField(max_length = 255, blank=True)
    parentItem = models.CharField(max_length = 255, blank=True)

class Variant(models.Model):
    baseVehicle = models.ForeignKey('Vehicle', blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, default=None)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, default='', blank=True)
    role = models.CharField(max_length=30, blank=True)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default = 0)

class GameUpdate(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return u"%s" % (self.name)

class GameUpdateEntity(models.Model):
    name = models.CharField(max_length = 255)
    update = models.ForeignKey('GameUpdate')

    def __unicode__(self):
        return u"%s(%s)" % (self.name, self.update.name)

class GameUpdateChange(models.Model):
    description = models.TextField()
    entity = models.ForeignKey('GameUpdateEntity')

    def __unicode__(self):
        return u"%s(%s):%s" % (self.entity.name, self.entity.update.name, self.description)


