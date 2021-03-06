from django.db import models
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

# Create your models here.
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
    manufacturer = models.ForeignKey("Manufacturer")
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
    manufacturer = models.ForeignKey("Manufacturer")
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
class Manufacturer(models.Model):
    name = models.CharField(max_length=30, default='')
    description = models.CharField(max_length=255, blank=True, null = True)
    
    def __unicode__(self):
        return self.name

### Descriptions need to be localized for different languages
class LocalizedDescriptionManufacturer(models.Model):
    languageCode = models.CharField(max_length = 5)
    description = models.TextField()
    parentEntity = models.ForeignKey("Manufacturer")

class LocalizedDescriptionVehicle(models.Model):
    languageCode = models.CharField(max_length = 5)
    description = models.TextField()
    parentEntity = models.ForeignKey("Vehicle")

class LocalizedDescriptionVehicleItem(models.Model):
    languageCode = models.CharField(max_length = 5)
    description = models.TextField()
    parentEntity = models.ForeignKey("VehicleItem")

### Vehicle Items

class VehicleItemType(models.Model):
    name = models.CharField(max_length = 255, default = "")
    typeName = models.CharField(max_length = 255, default = "")
    subTypeName  = models.CharField(max_length = 255, default = "", blank = True, null = True)

    def __unicode__(self):
        return self.name

# class VehicleItemSubType(models.Model):
#     subTypeName = models.CharField(max_length = 255)
#     parent = models.ForeignKey('VehicleItemType')

#     def __unicode__(self):
#         return self.subTypeName

class VehicleItemParams(models.Model):
    name = models.CharField(max_length = 255)
    value = models.FloatField(default = 0.0)
    parentItem = models.ForeignKey('VehicleItem', blank = True, null = True)

    def __unicode__(self):
        return u"%s - %s:%.2f" % (self.parentItem.name, self.name, self.value)

class VehicleItemPipe(models.Model):
    name = models.CharField(max_length = 255)
    stacking = models.BooleanField(default = False)
    parentItem = models.ForeignKey('VehicleItem', blank = True, null = True)

class VehicleItemPower(models.Model):
    state = models.CharField(max_length = 128)
    # Value couldbe a packed value curve
    value = models.CharField(max_length = 255)

    def __unicode__(self):
        return u"%s - %s" % (self.state, self.value)

class VehicleItemHeat(models.Model):
    state = models.CharField(max_length = 128)
    # Value couldbe a packed value curve
    value = models.CharField(max_length = 255)

    def __unicode__(self):
        return u"%s - %s" % (self.state, self.value)

class VehicleItemAvionics(models.Model):
    state = models.CharField(max_length = 128)
    # Value couldbe a packed value curve
    value = models.CharField(max_length = 255)

    def __unicode__(self):
        return u"%s - %s" % (self.state, self.value)

## Star Citizen Patch 12 - Arena Commander - Made major changes to how pipes
## are stored and how they work.  This added a lot more complexity to the already
## complex system, and the old model simply doesn't work.  We need a new model

class Pipe(models.Model):
    pipeClass = models.CharField(max_length=255, blank = True, null = True)
    levelWarning = models.FloatField(default=0.0)
    levelCritical = models.FloatField(default=0.0)
    levelFail = models.FloatField(default=0.0)
    states = models.ManyToManyField('PipeState', blank = True, null = True)
    pipeSignatures = models.ManyToManyField('PipeSignature', blank = True, null = True)
    pool = models.ForeignKey('PipePool', blank = True, null = True)

    def __unicode__(self):
        return self.pipeClass

class PipeState(models.Model):
    name = models.CharField(max_length=255, blank = True, null = True)
    dynamicValues = models.ManyToManyField('PipeStateDynamic', blank = True, null = True)
    variableValues = models.ManyToManyField('PipeStateVariable', blank = True, null = True)
    transition = models.FloatField(default = 0.0)
    values = models.ManyToManyField('PipeStateValue', blank = True, null = True)

    def __unicode__(self):
        return self.name

class PipeStateValue(models.Model):
    value = models.FloatField(default = 0.0)
    delay = models.FloatField(default = 0.0)
    ignorePool = models.BooleanField(default = False)

    def __unicode__(self):
        return u"%.2f" % self.value
    

class PipeStateDynamic(models.Model):
    dymVar = models.CharField(max_length = 255, blank = True, null = True)
    value = models.FloatField(default = 0.0)

    def __unicode__(self):
        return self.dymVar
    
class PipeStateVariable(models.Model):
    name = models.CharField(max_length = 255, blank = True, null = True)
    value = models.FloatField(default = 0.0)
    critical = models.BooleanField(default = False)

    def __unicode__(self):
        pass

class PipeSignature(models.Model):
    name = models.CharField(max_length = 255, blank = True, null = True)
    multiplier = models.FloatField(default = 0.0)

    def __unicode__(self):
        pass
    
class PipePool(models.Model):
    poolType = models.CharField(max_length = 255, blank = True, null = True)
    capacity = models.FloatField(default = 0.0)
    rate = models.FloatField(default = 0.0)
    critical = models.BooleanField(default = False)
    allInPipe = models.BooleanField(default = False)

    def __unicode__(self):
        pass

class VehicleItem(models.Model):
    itemClass = models.PositiveIntegerField(default = 0)
    description = models.TextField(blank = True, null = True)
    name = models.CharField(max_length = 255)
    displayName = models.CharField(max_length = 255, blank = True, null = True)
    itemType = models.ForeignKey('VehicleItemType', blank = True, null = True)
    manufacturer = models.ForeignKey('Manufacturer', blank = True, null = True)
    itemSize = models.PositiveIntegerField(default = 0)
    mass = models.FloatField(default = 0)
    hitpoints = models.BigIntegerField(default = 0)
    itemStats = models.ManyToManyField('ItemStat', blank = True, null = True)
    ports = models.ManyToManyField('ItemPort', blank = True, null = True)
    pipes = models.ManyToManyField('Pipe', blank = True, null = True)
    pipePower = models.ManyToManyField('VehicleItemPower', blank = True, null = True)
    pipeHeat = models.ManyToManyField('VehicleItemHeat', blank = True, null = True)
    pipeAvionics = models.ManyToManyField('VehicleItemAvionics', blank = True, null = True)
    weaponData = models.ForeignKey('Weapon', blank = True, null = True)
    ammoData = models.ForeignKey('Ammo', blank = True, null = True)
    armorData = models.ForeignKey('Armor', blank = True, null = True)
    batteryData = models.ForeignKey('Battery', blank = True, null = True)
    radarData = models.ForeignKey('Radar', blank = True, null = True)
    shieldData = models.ForeignKey('Shield', blank = True, null = True)
    gimbalData = models.ForeignKey('Gimbal', blank = True, null = True)
    thrusterData = models.ForeignKey('Thruster', blank = True, null = True)
    turretData = models.ForeignKey('Turret', blank = True, null = True)
    # Additional fields required for The Barn
    views = models.PositiveIntegerField(default = 0)
    disabled = models.BooleanField(default = False)

    def __unicode__(self):
        return u"%s" % (self.name)

class ItemStat(models.Model):
    name = models.CharField(max_length = 255)
    value = models.FloatField(default = 0.0)

    def __unicode__(self):
        return u"%s:%.2f" % (self.name, self.value)

class Weapon(models.Model):
    supportedAmmo = models.ManyToManyField('Ammo', blank = True, null = True)
    fireModes = models.ManyToManyField('Firemode', blank = True, null = True)

    def __unicode__(self):
        return u"%d" % (self.id)

class VehicleDamageParam(models.Model):
    damage = models.FloatField(default = 0)
    damage_drop_min_distance = models.FloatField(default = 0)
    damage_drop_per_meter = models.FloatField(default = 0)
    damage_drop_min_damage = models.FloatField(default = 0)

    def __unicode__(self):
        return u"Damage: %.2f, Min Range: %.2f Meters" % (self.damage, self.damage_drop_min_distance)
class Signature(models.Model):
    name = models.CharField(max_length = 255)
    # Threshold is used for things with a detection threshold
    threshold = models.FloatField(default = 0)
    # Value is used for things that offset the ship's signature in a positive or negtive manner
    value = models.FloatField(default = 0)

class VehicleMissileGuidanceParam(models.Model):
    min_tracking_angle = models.FloatField(default = 0)
    max_tracking_angle = models.FloatField(default = 0)
    min_tracking_distance = models.FloatField(default = 0)
    max_tracking_distance = models.FloatField(default = 0)
    guidance_type = models.CharField(max_length = 255, blank = True, null = True)
    signal_range_modifier = models.FloatField(default = 0)
    signal_antenna_gain = models.FloatField(default = 0)
    signal_transmit_power = models.FloatField(default = 0)
    signatures = models.ManyToManyField('Signature', blank = True, null = True)

    def __unicode__(self):
        return u"%s" % (self.guidance_type)

class VehicleMissileParam(models.Model):
    turn_speed = models.FloatField(default = 0)
    turn_lazyness = models.FloatField(default = 0)
    max_speed = models.FloatField(default = 0)
    accel = models.FloatField(default = 0)
    maneuver_accel = models.FloatField(default = 0)
    initial_delay = models.FloatField(default = 0)
    ammolive = models.BooleanField(default = False)
    category = models.CharField(max_length = 255, blank = True, null = True)
    detonation_radius = models.FloatField(default = 0)
    damage = models.FloatField(default = 0)

class Ammo(models.Model):
    name = models.CharField(max_length = 255)
    displayName = models.CharField(max_length = 255, blank = True, null = True)
    pierceability = models.FloatField(default = 15)
    vehicleDamageParam = models.ForeignKey('VehicleDamageParam', blank = True, null = True)
    vehicleMissileParam = models.ForeignKey('VehicleMissileParam', blank = True, null = True)
    vehicleMissileGuidanceParam = models.ForeignKey('VehicleMissileGuidanceParam', blank = True, null = True)

    def __unicode__(self):
        return u"%s" % (self.name)

class Firemode(models.Model):
    name = models.CharField(max_length = 255)
    ammo_type = models.CharField(max_length = 255, blank = True, null = True)
    ammo = models.ForeignKey('Ammo', blank = True, null = True)
    rate = models.FloatField(default = 0)
    damage = models.FloatField(default = 0)

class Armor(models.Model):
    armorParams = models.ManyToManyField('ArmorParam', blank = True, null = True)
    damageMultipliers = models.ManyToManyField('DamageMultiplier', blank = True, null = True)
    signatures = models.ManyToManyField('Signature', blank = True, null = True)

class ArmorParam(models.Model):
    name = models.CharField(max_length = 255)
    value = models.FloatField(default = 0)

class DamageMultiplier(models.Model):
    damagetype = models.CharField(max_length = 255, default = "default")
    multiplier = models.FloatField(default = 0)

    def asPercent(self):
        output = "%s %.2f" % (self.damagetype, self.multiplier * 100.0)
        return mark_safe(output)

class Battery(models.Model):
    dynamicPipe = models.FloatField(default = 0)
    chargeRate = models.FloatField(default = 0)
    capacity = models.FloatField(default = 0)
    output = models.FloatField(default = 0)

class Radar(models.Model):
    radar_type = models.CharField(max_length = 255, blank = True, null = True)
    search_radius = models.FloatField(default = 0)
    grid_size = models.FloatField(default = 0)
    signal_range_modifier = models.FloatField(default = 0)
    signal_antenna_gain = models.FloatField(default = 0)
    signal_transmit_power = models.FloatField(default = 0)
    signatures = models.ManyToManyField('Signature', blank = True, null = True)

class Shield(models.Model):
    shieldtype = models.CharField(max_length = 255, blank = True, null = True)
    shieldfacetype = models.CharField(max_length = 255, blank = True, null = True)
    regenratepersecond = models.FloatField(default = 0)
    regenpowerperpoint = models.FloatField(default = 0)
    maxshieldlevel = models.FloatField(default = 0)
    regenshielddelay = models.FloatField(default = 0)
    maxlevelmodifier = models.FloatField(default = 0)

class SignatureModifier(models.Model):
    signatures = models.ManyToManyField('Signature', blank = True, null = True)

class Gimbal(models.Model):
    yaw_min = models.FloatField(default = 0)
    yaw_max = models.FloatField(default = 0)
    yaw_speed = models.FloatField(default = 0)
    yaw_acceleration = models.FloatField(default = 0)
    pitch_min = models.FloatField(default = 0)
    pitch_max = models.FloatField(default = 0)
    pitch_speed = models.FloatField(default = 0)
    pitch_acceleration = models.FloatField(default = 0)
    roll_min = models.FloatField(default = 0)
    roll_max = models.FloatField(default = 0)
    roll_speed = models.FloatField(default = 0)
    roll_acceleration = models.FloatField(default = 0)

class Thruster(models.Model):
    maxthrust = models.FloatField(default = 0)
    yaw_min = models.FloatField(default = 0)
    yaw_max = models.FloatField(default = 0)
    yaw_speed = models.FloatField(default = 0)
    yaw_acceleration = models.FloatField(default = 0)
    pitch_min = models.FloatField(default = 0)
    pitch_max = models.FloatField(default = 0)
    pitch_speed = models.FloatField(default = 0)
    pitch_acceleration = models.FloatField(default = 0)
    roll_min = models.FloatField(default = 0)
    roll_max = models.FloatField(default = 0)
    roll_speed = models.FloatField(default = 0)
    roll_acceleration = models.FloatField(default = 0)
    gimbal = models.ForeignKey('Gimbal', blank = True, null = True)

class Turret(models.Model):
    yaw_min = models.FloatField(default = 0)
    yaw_max = models.FloatField(default = 0)
    yaw_speed = models.FloatField(default = 0)
    pitch_min = models.FloatField(default = 0)
    pitch_max = models.FloatField(default = 0)
    pitch_speed = models.FloatField(default = 0)
    roll_min = models.FloatField(default = 0)
    roll_max = models.FloatField(default = 0)
    roll_speed = models.FloatField(default = 0)

### Vehicles
class VehicleImage(models.Model):
    url = models.URLField(default = '')
    name = models.CharField(max_length = 255, default = '')
    ship = models.ForeignKey('Vehicle')
    
    def __unicode__(self):
        return u"(%s)%s" % (self.ship.displayName, self.name)

class ItemPort(models.Model):
    # Basic fields as required by game model
    displayName = models.CharField(max_length = 255, blank = True, null = True)
    name = models.CharField(max_length = 255)
    flags = models.CharField(max_length = 512, blank = True, null = True)
    maxSize = models.PositiveIntegerField(default = 1)
    minSize = models.PositiveIntegerField(default = 0)
    supportedTypes = models.ManyToManyField('VehicleItemType', blank = True, null = True) 
    parentVehicle = models.ForeignKey('Vehicle', blank = True, null = True)
    # Added just in case the game starts using it
    portClass = models.PositiveIntegerField(default = 0)
    # Additional fields required for The Barn
    # 1 = TopRight, 2 = TopLeft, 3 = BottomRightLeft, 4 = BottomRight
    # parentImage = models.PositiveIntegerField(default = 0)
    # image = models.ForeignKey('Image', null = True, blank = True)
    # tagLocationX = models.FloatField(default = 0.0)
    # tagLocationY = models.FloatField(default = 0.0)
    disabled = models.BooleanField(default = False)

    def __unicode__(self):
        if self.displayName and self.displayName != "":
            name = self.displayName
        else:
            name = self.name
        return self.name

class VehicleCategory(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

class Vehicle(models.Model):
    # Basic fields as required by game model
    vehicleClass = models.PositiveIntegerField(default = 1)
    category = models.CharField(max_length=255, default = "Default Vehicle")
    displayName = models.CharField(max_length = 255, blank = True, null = True)
    name = models.CharField(max_length = 255)
    ports = models.ManyToManyField('ItemPort', blank = True, null = True)
    # Additional fields required for The Barn
    views = models.PositiveIntegerField(default = 0)
    upgradeSlots = models.PositiveIntegerField(default = 0)
    maximum_crew = models.PositiveIntegerField(default = 1)
    empty_mass = models.FloatField(default = 0)
    length = models.FloatField(default = 0)
    width = models.FloatField(default = 0)
    height = models.FloatField(default = 0)
    thumbnail = models.URLField(default='', blank = True, null = True)
    available = models.BooleanField(default = False)
    manufacturer = models.ForeignKey('Manufacturer', blank = True, null = True)
    defaultVariant = models.ForeignKey('Variant', blank = True, null = True)

    def __unicode__(self):
        if self.displayName and self.displayName != "":
            name = self.displayName
        else:
            name = self.name
        return u"%s Class %d %s" % (name, self.vehicleClass, self.category)
            
class HardpointTag(models.Model):
    hardpoint = models.ForeignKey('ItemPort', blank = True, null = True);
    tagX = models.FloatField(default = 0)
    tagY = models.FloatField(default = 0)
    datablockX = models.FloatField(default = 0)
    datablockY = models.FloatField(default = 0)
    disabled = models.BooleanField(default = False)
    parentImage = models.ForeignKey('VehicleImage', blank = True, null = True)

    def __unicode__(self):
        return u"(%s)%s" % (self.parentImage, self.hardpoint)

class VariantItem(models.Model):
    variant = models.ForeignKey("Variant", blank=True, null=True)
    item = models.ForeignKey("VehicleItem", blank=True, null = True, related_name = "variantItem")
    port = models.ForeignKey("ItemPort", blank=True, null = True, related_name = "variantPort")
    parentPort = models.ForeignKey("ItemPort", blank=True, null = True, related_name = "variantParentPort")
    parentItem = models.ForeignKey("VehicleItem", blank=True, null = True, related_name = "variantParentItem")

class Variant(models.Model):
    baseVehicle = models.ForeignKey('Vehicle', blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, default=None)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, default='', blank=True, null = True)
    role = models.CharField(max_length=30, blank=True, null = True)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default = 0)

class GameUpdate(models.Model):
    name = models.CharField(max_length = 255, default = "")
    build = models.CharField(max_length = 64, default = "")
    module = models.CharField(max_length = 255, default = "Root")
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % (self.name)

class GameUpdateChange(models.Model):
    description = models.TextField(default = "")
    entityName = models.CharField(max_length=255, default = "", blank = True, null = True)
    update = models.ForeignKey('GameUpdate', blank = True, null = True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if self.entityName:
            return u"%s(%s):%s" % (self.entityName, self.update.name, self.description)
        else:
            return u"(%s):%s" % (self.update.name, self.description)

class Hangar(models.Model):
    hangarVehicles = models.ManyToManyField('Vehicle', blank = True, null = True)
    hangarVehicleItems = models.ManyToManyField('VehicleItem', blank = True, null = True)
    hangarVariants = models.ManyToManyField('Variant', blank = True, null = True)
    hangarFavorites = models.ManyToManyField('Variant', blank = True, null = True, related_name="favorites")
    hangarFriends = models.ManyToManyField(User, blank = True, null = True)


######################################################
## Arena Commander Actionmap Editor
######################################################

class ActionMap(models.Model):
    name = models.CharField(max_length = 255, default = "", blank = True, null = True)

    def __unicode__(self):
        return self.name


class ActionMapAction(models.Model):
    name = models.CharField(max_length = 255, default = "", blank = True, null = True)
    actionmap = models.ManyToManyField('ActionMap', blank = True, null = True)

    def __unicode__(self):
        return self.name

class ActionMapDevice(models.Model):
    name = models.CharField(max_length = 255, default = "", blank = True, null = True)

    def __unicode__(self):
        return self.name

class ActionMapInput(models.Model):
    name = models.CharField(max_length = 255, default = "", blank = True, null = True)
    device = models.ManyToManyField('ActionMapDevice', blank = True, null = True)

    def __unicode__(self):
        return self.name

class Controller(models.Model):
    name = models.CharField(max_length = 255, default = "", blank = True, null = True)
    device = models.ManyToManyField('ActionMapDevice', blank = True, null = True)

    def __unicode__(self):
        return self.name

class ControllerInput(models.Model):
    name = models.CharField(max_length = 255, default = "", blank = True, null = True)
    input = models.ManyToManyField('ActionMapInput', blank = True, null = True)

    def __unicode__(self):
        return self.name
