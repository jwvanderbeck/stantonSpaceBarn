from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from shipBuilder.models import *
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import ensure_csrf_cookie
from stantonSpaceBarn.forms import SubmitBuildForm
from stantonSpaceBarn import itemLuts
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
import logging
import pdb

def stringToIntArray(s):
    intArray = []
    print 'string array', s
    try:
        splits = s.split(',')
    except:
        return intArray

    for s in splits:
        try:
            intArray.append(int(s))
        except:
            intArray.append(0)
    print 'int array', intArray
    return intArray

def redirectToBlog(request):
    return redirect('/blog')

def userHangar(request):
    # Display all saved variants created by the user
    allVariants = Build.objects.filter(created_by__exact=request.user)
    renderContext = {
        'variant_list'     : allVariants
    }
    return render_to_response('variants_list.html', renderContext, context_instance=RequestContext(request))

def variantList(request):
    # Display all saved variants
    allVariants = Build.objects.all()
    renderContext = {
        'variant_list'     : allVariants
    }
    return render_to_response('variants_list.html', renderContext, context_instance=RequestContext(request))

def shipList(request):
    # Display all base ships as well as manufacturer variants
    allShips = Ship.objects.all()
    renderContext = {
        'ship_list'     : allShips
    }
    return render_to_response('ships_list.html', renderContext, context_instance=RequestContext(request))

def base(request):
    renderContext = {
    }
    return render_to_response('base.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def updateBuild(request):
    if request.is_ajax():
        try:
            data = simplejson.loads(request.body)
            print data
        except:
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        variant = None

        if not 'variantID' in data:
            response_data = {
            'success' : False,
            'response' : 'No variant specified.'
            }
        variantID = data['variantID']
        variant = Build.objects.get(pk=variantID)

        if not variant:
            response_data = {
            'success' : False,
            'response' : 'Variant not found.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        if variant.created_by != request.user:
            response_data = {
            'success' : False,
            'response' : 'Variant not owned by user'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        ships = Ship.objects.filter(pk=data['shipID'])
        try:
            ship = ships[0]
        except:
            response_data = {
            'success' : False,
            'response' : 'Ship not found.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        hardpoint_items = data['hardpoints']
        hull_mods = data['hull_mods']
        engine_mods = data['engine_mods']

        variantData = {
            'role' : data['role'],
            'ship' : ship,
            'name' : data['name'],
            'manufacturer_variant' : False,
            'engine_intake' : data['engine_intake'],
            'powerplant' : data['powerplant'],
            'main_thruster' : data['main_thruster'],
            'shield' : data['shield'],
            'cargo_mod' : data['cargo_mod'],
            'hardpoints' : hardpoint_items,
            'engine_mods' : engine_mods,
            'hull_mods' : hull_mods,
        }
        print 'Variant Data', variantData
        if updateVariant(variantData, variantID):
            response_data = {
            'success' : True,
            'response' : 'Variant updated.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        else:
            response_data = {
            'success' : False,
            'response' : 'An error occured while updating the record.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

@ensure_csrf_cookie
def deleteBuild(request):
    if request.is_ajax():
        try:
            data = simplejson.loads(request.body)
            print data
        except:
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        variant = None
        user = None

        if not 'variantID' in data:
            response_data = {
            'success' : False,
            'response' : 'No variant specified.'
            }
        variantID = data['variantID']
        variant = Build.objects.get(pk=variantID)


        if not variant:
            response_data = {
            'success' : False,
            'response' : 'Variant not found.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        if variant.created_by != request.user:
            response_data = {
            'success' : False,
            'response' : 'Variant not owned by user'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        variant.delete()
        response_data = {
        'success' : True,
        'response' : 'Variant updated.'
        }
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")


@ensure_csrf_cookie
def userLogin(request):
    if request.is_ajax():
        try:
            data = simplejson.loads(request.body)
            # print data
        except:
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        username = None
        password = None
        for entry in data:
            if entry['name'] == 'username':
                username = entry['value']
            elif entry['name'] == 'password':
                password = entry['value']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

        response_data = {
        'success' : True,
        'username' : username,
        'response' : 'User logged in.'
        }
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

@ensure_csrf_cookie
def userLogout(request):
    if request.is_ajax():
        logout(request)
        response_data = {
        'success' : True,
        'response' : 'User logged in.'
        }
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

@ensure_csrf_cookie
def userCreate(request):
    if request.is_ajax():
        try:
            data = simplejson.loads(request.body)
            # print data
        except:
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        username = None
        password1 = None
        password2 = None
        for entry in data:
            if entry['name'] == 'username':
                username = entry['value']
            elif entry['name'] == 'password1':
                password1 = entry['value']
            elif entry['name'] == 'password2':
                password2 = entry['value']

        if password1 != password2:
            response_data = {
            'success' : False,
            'response' : 'Passwords did not match'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        user = User.objects.create_user(username, '', password1)

        if not user:
            response_data = {
            'success' : False,
            'response' : 'An unknown error occured and your account was not created.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        else:
            user = authenticate(username=username, password=password1)
            login(request, user)

        response_data = {
        'success' : True,
        'username' : username,
        'response' : 'User created.'
        }
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")


@ensure_csrf_cookie
def shipDetail(request, shipName):
    
    # Get all hardpoints
    hardpoints = Hardpoint.objects.filter(ship__name__iexact=shipName).order_by('tag_location_y')
    items = Item.objects.all()
    images = Image.objects.filter(ship__name__iexact=shipName)
    item_types = ItemType.objects.filter(hardpoint_type=True)
    submitBuildForm = SubmitBuildForm()
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    if len(images) == 0:
        raise Http404() 
    renderContext = {
    'hardpoint_list'    : hardpoints,
    'item_list'         : items,
    'image_list'        : images,
    'shipname'          : shipName,
    'ship'              : images[0].ship,
    'itemtype_list'     : item_types,
    'saveVariantForm'           : submitBuildForm,
    'loginForm'                 : loginForm,
    'createUserForm'            : createUserForm
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('ship_base.html', renderContext, context_instance=RequestContext(request))

def validItemForHardpoint(item, hardpoint):

    if not hardpoint:
        return False
    if not item:
        return False

    # Currently we just verify the hardpoint class is sufficient for the item
    # Maybe more later
    if hardpoint.hardpoint_class >= item.hardpoint_class:
        return True

    return False

def getItemByID(itemID):
    try:
        item = Item.objects.get(pk = itemID)
    except:
        item = None
    return item


def updateVariant(variantData, variantID):
    # variantData = {
    #     'ship' : '300i',
    #     'role' : 'quick variant',
    #     'name' : 'quick variant',
    #     'manufacturer_variant' : False,
    #     'engine_intake' : 0,
    #     'powerplant' : 0,
    #     'main_thruster' : 0,
    #     'shield' : 0,
    #     'cargo_mod' : 0,
    #     'hardpoints' : [0,0,0,0,0],
    #     'engine_mods' : [0,0],
    #     'hull_mods' : [0]
    # }

    # Update existing variant record in the database
    # To do this we update the main Build entity, but delete and recreate the BuildHardpoint, BuildHullMod, and BuildEngineMod entities

    for key in variantData:
        if not variantData[key]:
            variantData[key] = '0'

    # Find the variant
    variant = Build.objects.get(pk=variantID)
    if not variant:
        return False

    # Look up items
    engine_intake = getItemByID(variantData['engine_intake'])
    powerplant = getItemByID(variantData['powerplant'])
    main_thruster = getItemByID(variantData['main_thruster'])
    shield = getItemByID(variantData['shield'])
    cargo_mod = getItemByID(variantData['cargo_mod'])
    hardpoints = []
    # print variantData['hardpoints']
    for item in variantData['hardpoints']:
        itemID = getItemByID(item)
        hardpoints.append(itemID)
        # print itemID
    # print hardpoints
    engine_mods = []
    for item in variantData['engine_mods']:
        engine_mods.append(getItemByID(item));
    hull_mods = []
    for item in variantData['hull_mods']:
        hull_mods.append(getItemByID(item));
    buildHardpoints = []
    buildEngineMods = []
    buildHullMods = []

    # Update main build
    variant.name=variantData['name']
    variant.role=variantData['role']
    variant.engine_intake = engine_intake
    variant.powerplant = powerplant
    variant.main_thruster = main_thruster
    variant.shield = shield
    variant.cargo_mod = cargo_mod

    # Save the changes
    variant.save()

    # delete and rebuild ancillary tables
    variant.buildhardpoint_set.all().delete()
    variant.buildenginemod_set.all().delete()
    variant.buildhullmod_set.all().delete()

    shipHardpoints = Hardpoint.objects.filter(ship__name__iexact=variantData['ship']).order_by('id')
    index = 0;
    # print 'Hardpoints ', hardpoints
    for hardpoint in shipHardpoints:
        item = hardpoints[index]
        newHardpoint = BuildHardpoint(build=variant, hardpoint=hardpoint, item=item)
        newHardpoint.save()
        buildHardpoints.append(newHardpoint)
        index = index + 1

    for item in engine_mods:
        newEngineMod = BuildEngineMod(build=variant, item=item)
        newEngineMod.save()
        buildEngineMods.append(newEngineMod)

    for item in hull_mods:
        newHullMod = BuildHullMod(build=variant, item=item)
        newHullMod.save()
        buildHullMods.append(newHullMod)

    variantData = {
        'build' : variant,
        'build_hardpoints' : buildHardpoints,
        'build_engine_mods' : buildEngineMods,
        'build_hull_mods' : buildHullMods
    }
    return True

def makeVariant(variantData, saveVariant = False, user = None):
    # variantData = {
    #     'ship' : '300i',
    #     'role' : 'quick variant',
    #     'name' : 'quick variant',
    #     'manufacturer_variant' : False,
    #     'engine_intake' : 0,
    #     'powerplant' : 0,
    #     'main_thruster' : 0,
    #     'shield' : 0,
    #     'cargo_mod' : 0,
    #     'hardpoints' : [0,0,0,0,0],
    #     'engine_mods' : [0,0],
    #     'hull_mods' : [0]
    # }

    for key in variantData:
        if not variantData[key]:
            variantData[key] = '0'

    # Look up items
    engine_intake = getItemByID(variantData['engine_intake'])
    powerplant = getItemByID(variantData['powerplant'])
    main_thruster = getItemByID(variantData['main_thruster'])
    shield = getItemByID(variantData['shield'])
    cargo_mod = getItemByID(variantData['cargo_mod'])
    hardpoints = []
    # print variantData['hardpoints']
    for item in variantData['hardpoints']:
        itemID = getItemByID(item)
        hardpoints.append(itemID)
        # print itemID
    # print hardpoints
    engine_mods = []
    for item in variantData['engine_mods']:
        engine_mods.append(getItemByID(item));
    hull_mods = []
    for item in variantData['hull_mods']:
        hull_mods.append(getItemByID(item));
    buildHardpoints = []
    buildEngineMods = []
    buildHullMods = []
    newBuild = Build(
        name=variantData['name'], 
        role=variantData['role'], 
        ship=variantData['ship'],
        manufacturer_variant=variantData['manufacturer_variant'],
        engine_intake = engine_intake,
        powerplant = powerplant,
        main_thruster = main_thruster,
        shield = shield,
        cargo_mod = cargo_mod,
        created_by = user
        )
    if saveVariant:
        newBuild.save()
    shipHardpoints = Hardpoint.objects.filter(ship__name__iexact=variantData['ship']).order_by('id')
    index = 0;
    for hardpoint in shipHardpoints:
        item = hardpoints[index]
        newHardpoint = BuildHardpoint(build=newBuild, hardpoint=hardpoint, item=item)
        if saveVariant:
            newHardpoint.save()
        buildHardpoints.append(newHardpoint)
        index = index + 1

    for item in engine_mods:
        newEngineMod = BuildEngineMod(build=newBuild, item=item)
        if saveVariant:
            newEngineMod.save()
        buildEngineMods.append(newEngineMod)

    for item in hull_mods:
        newHullMod = BuildHullMod(build=newBuild, item=item)
        if saveVariant:
            newHullMod.save()
        buildHullMods.append(newHullMod)

    variantData = {
        'build' : newBuild,
        'build_hardpoints' : buildHardpoints,
        'build_engine_mods' : buildEngineMods,
        'build_hull_mods' : buildHullMods
    }
    # assert False
    return variantData

@ensure_csrf_cookie
def quickVariant(request, shipName, variantURL = 0):
    # print "quickVariant", shipName, variantURL
    # If this is an AJAX request, then it means we need to build a quick variant URL rather than display one
    # v0 URL encoding:
    #   0-[00]*-[00][00][00]*-[00][00]*
    #   First digit is version
    #   Groups seperated by a dash (-)
    #   Group 1 is hardpoint items.  Two characters per item, each grouping equals an item ID.
    #       This group should always have 2 characters per hardpoint, or numHardpoints * 2 characters
    #   Group 2 is engine mods.  
    #       First set of 2 is engine intake item
    #       Second set of 2 is powerplant
    #       Third set of 2 is main thruster
    #       0 or more sets of 2 after third is generic engine mods
    #   Group 3 is hull mods.  
    #       First set of 2 is shield
    #       Second set of 2 is cargo mod
    #       0 or more sets of 2 after second is generic hull mods
    # http://www.stantonspacebarn.com/quick-variant/300i/0-0504040202-000e080h-09060g
    #
    # v1 URL encoding
    # 1-00_00-00_00*
    #   First digit is version
    #   After the version, is a series of groups, each group is in two parts separated by an underscore
    #   First part of the group is the port ID, the second part of the group is the item ID.
    #   If the Port ID is 6 characters, then it is a subport.  The first 2 characters are the parent Item ID
    #       The next 2 characters are the parent port ID and the last 2 characters are the actual port ID
    #   Each group is separated by a dash
    # Incoming AJAX data should specify the requested version.  If data["version"] does not exist, or is blank
    # then the version is assumed to be v0.  This functionality is present to allow both V0 and V1 to exist at the 
    # same time for testing V1 while V0 is still being used.
    if request.is_ajax():
        # print "Received AJAX call"
        try:
            data = simplejson.loads(request.body)
        except:
            response_data = {
            'url' : 'Z',
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        # print data
        if not "version" in data:
            version = 0

        if "version" in data:
            version = data["version"]
        # print "Building quick variant URL version %d" % version
        if version == 0:
            shipName = None
            hardpoints = None
            engine_intake = None
            powerplant = None
            main_thruster = None
            shield = None
            cargo_mod = None
            engine_mods = None
            hull_mods = None

            if 'shipName' in data:
                shipName = data['shipName']
            if 'hardpoints' in data:
                hardpoints = data['hardpoints']
            if 'engine_intake' in data:
                engine_intake = int(data['engine_intake'])
            if 'powerplant' in data:
                powerplant = int(data['powerplant'])
            if 'main_thruster' in data:
                main_thruster = int(data['main_thruster'])
            if 'shield' in data:
                shield = int(data['shield'])
            if 'cargo_mod' in data:
                cargo_mod = int(data['cargo_mod'])
            if 'engine_mods' in data:
                engine_mods = data['engine_mods']
            if 'hull_mods' in data:
                hull_mods = data['hull_mods']

            if not shipName:
                response_data = {
                'url' : 'Z',
                'success' : False,
                'response' : 'shipName not found.'
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

            if not hardpoints:
                response_data = {
                'url' : 'Z',
                'success' : False,
                'response' : 'No hardpoint data was found.'
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

            baseURL = reverse('stantonSpaceBarn.views.quickVariant', args=(shipName, ))

            variantURL = '0-'
            for hardpoint in hardpoints:
                variantURL = variantURL + itemLuts.idToURL(hardpoint['item_id'], 0)

            variantURL = variantURL + '-%s%s%s' % (itemLuts.idToURL(engine_intake, 0),itemLuts.idToURL(powerplant, 0),itemLuts.idToURL(main_thruster, 0))
            for mod in engine_mods:
                if mod:
                    variantURL = variantURL + itemLuts.idToURL(int(mod), 0)

            variantURL = variantURL + '-%s%s' % (itemLuts.idToURL(shield, 0),itemLuts.idToURL(cargo_mod, 0))
            for mod in hull_mods:
                if mod:
                    variantURL = variantURL + itemLuts.idToURL(int(mod), 0)

            response_data = {
                'url' : baseURL + variantURL,
                'success' : True,
                'response' : 'ok'
            }

            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        elif version == 1:
            # print "Version 1"
            # What we need:
            #   Name of ship
            #   list of dicts, with name of hardpoint, and name of item
            #   EG
            #   data["shipName"] = "oj_350r"
            #   data["ports"] = [ {"portName" : "nose_slot", "itemName" : "mass_driver"} ]
            #   optionally a port record can contain parentPort and parentItem IDs for ports
            #   that are on items.

            try:
                vehicleData = Vehicle.objects.get(name__iexact=shipName)
            except:
                response_data = {
                'url' : 'Z',
                'success' : False,
                'response' : 'Failed to load data for vehicle %s' % shipName
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")


            baseURL = reverse('stantonSpaceBarn.views.quickVariant', args=(shipName, ))
            variantURL = "1"

            for port in data["ports"]:
                portName = port["portName"]
                itemName = port["itemName"]
                if "parentPort" in port:
                    parentPort = port["parentPort"]
                else:
                    parentPort = None
                if "parentItem" in port:
                    parentItem = port["parentItem"]
                else:
                    parentItem = None

                try:
                    if parentItem and parentPort:
                        parentItemData = VehicleItem.objects.get(name__iexact=parentItem);
                        portData = ItemPort.objects.get(name__iexact=portName, parentItem__exact=parentItemData)
                        parentPortData = ItemPort.objects.get(name__iexact=parentPort, parentVehicle__exact=vehicleData)
                    else:
                        portData = ItemPort.objects.get(name__iexact=portName, parentVehicle__exact=vehicleData)
                    itemData = VehicleItem.objects.get(name__iexact=itemName)
                except Exception as e:
                    response_data = {
                    'url' : 'Z',
                    'success' : False,
                    'response' : 'Failed to load data for port %s, item %s' % (portName, itemName)
                    }
                    return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
                if parentItem:
                    variantURL = variantURL + "-" + itemLuts.idToURL(parentItemData.id, 0) + itemLuts.idToURL(parentPortData.id, 0) + itemLuts.idToURL(portData.id, 0) + "_" + itemLuts.idToURL(itemData.id, 0)
                else:
                    variantURL = variantURL + "-" + itemLuts.idToURL(portData.id, 0) + "_" + itemLuts.idToURL(itemData.id, 0)

            response_data = {
                'url' : baseURL + variantURL,
                'success' : True,
                'response' : 'ok'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    # Display a quick Variant
    variantDetails = variantURL.split('-')
    variantVersion = variantDetails[0]

    if variantVersion == '0':
    # Find the ship
        ships = Ship.objects.filter(name__iexact=shipName)
        try:
            ship = ships[0]
        except:
            return HttpResponse("<h1>Unable to load Quick Variant</h1><p>Failed to find specified ship</p>")

        images = Image.objects.filter(ship__id=ship.id)
        if len(images) == 0:
            raise Http404() 
        hardpoints = Hardpoint.objects.filter(ship__name__iexact=shipName).order_by('id')

        if variantVersion.lower() == '0':
            if len(variantDetails) < 4:
                return HttpResponse("<h1>Unable to load Quick Variant</h1><p>Malformed URL</p>")
            hardpointsURL = variantDetails[1]
            engineModsURL = variantDetails[2]
            if len(engineModsURL) < 6:
                return HttpResponse("<h1>Unable to load Quick Variant</h1><p>Malformed URL</p>")
            hullModsURL = variantDetails[3]
            if len(hullModsURL) < 4:
                return HttpResponse("<h1>Unable to load Quick Variant</h1><p>Malformed URL</p>")
            variantData = {
                'ship' : ship,
                'role' : 'quick variant',
                'name' : 'quick variant',
                'manufacturer_variant' : False,
                'engine_intake' : itemLuts.urlToID(engineModsURL[0:2]),
                'powerplant' : itemLuts.urlToID(engineModsURL[2:4]),
                'main_thruster' : itemLuts.urlToID(engineModsURL[4:6]),
                'shield' : itemLuts.urlToID(hullModsURL[0:2]),
                'cargo_mod' : itemLuts.urlToID(hullModsURL[2:4]),
            }
            hardpoints = []
            for i in range(0, len(hardpointsURL), 2):
                hardpoints.append(itemLuts.urlToID(hardpointsURL[i:i+2]))
            engine_mods = []
            engineModsURL = engineModsURL[6:]
            for i in range(0, len(engineModsURL), 2):
                engine_mods.append(itemLuts.urlToID(engineModsURL[i:i+2]))
            hull_mods = []
            hullModsURL = hullModsURL[4:]
            for i in range(0, len(hullModsURL), 2):
                hull_mods.append(itemLuts.urlToID(hullModsURL[i:i+2]))
            variantData['hardpoints'] = hardpoints
            variantData['engine_mods'] = engine_mods
            variantData['hull_mods'] = hull_mods
            variant = makeVariant(variantData, saveVariant = False)
        else:
            raise Http404()

        allItems = Item.objects.all()
        submitBuildForm = SubmitBuildForm()
        loginForm = AuthenticationForm()
        createUserForm = UserCreationForm()
        renderContext = {
        'variantData_hardpoints'    : variant['build_hardpoints'],
        'variantData_engine_mods'   : variant['build_engine_mods'],
        'variantData_hull_mods'     : variant['build_hull_mods'],
        'variantData_build'         : variant['build'],
        'item_list'                 : allItems,
        'image_list'                : images,
        'shipname'                  : ship.name,
        'ship'                      : ship,
        'saveVariantForm'           : submitBuildForm,
        'loginForm'                 : loginForm,
        'createUserForm'            : createUserForm
        }

        # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
        # as it is what enables the resulting rendered view to contain the CSRF token!
        # !!!!!!!!!!!!!
        return render_to_response('quick_variant.html', renderContext, context_instance=RequestContext(request))
    elif variantVersion == '1':
        try:
            vehicleData = Vehicle.objects.get(name__iexact=shipName)
        except:
            return HttpResponse("<h1>Unable to load Quick Variant</h1><p>Failed to find specified ship</p>")

        itemGroups = variantDetails[1:]
        # print itemGroups
        ports = []
        items = []
        variantData = []
        for itemGroup in itemGroups:
            IDSplit = itemGroup.split("_")
            if len(IDSplit[0]) == 2:
                portID = itemLuts.urlToID(IDSplit[0])
                itemID = itemLuts.urlToID(IDSplit[1])
                parentPortID = None
                parentItemID = None
                # print portID, itemID
            elif len(IDSplit[0]) == 6:
                portID = itemLuts.urlToID(IDSplit[0][4:6])
                parentPortID = itemLuts.urlToID(IDSplit[0][2:4])
                parentItemID = itemLuts.urlToID(IDSplit[0][:2])
                itemID = itemLuts.urlToID(itemGroup.split("_")[1])
            try:
                if parentPortID:
                    parentPortData = ItemPort.objects.get(pk=parentPortID)
                    parentItemData = VehicleItem.objects.get(pk=parentItemID)
                else:
                    parentPortData = None
                    parentItemData = None
                portData = ItemPort.objects.get(pk=portID)
                itemData = VehicleItem.objects.get(pk=itemID)
            except Exception as e:
                pass
            if parentPortData:
                variantData.append({"port" : portData, "item" : itemData, "parentPort" : parentPortData, "parentItem" : parentItemData})
            else:
                variantData.append({"port" : portData, "item" : itemData})
        loginForm = AuthenticationForm()
        createUserForm = UserCreationForm()
        renderContext = {
            'shipData'          : vehicleData,
            'variantData'       : variantData,
            'loginForm'         : loginForm,
            'createUserForm'    : createUserForm
        }
        return render_to_response('bootstrap/light-blue/quickVariant.html', renderContext, context_instance=RequestContext(request))
    
@ensure_csrf_cookie
def variantDetail(request, buildID):

    build = Build.objects.get(pk=buildID)
    if not build:
        raise Http404()

    # Get all hardpoints
    ship = build.ship
    # hardpoints = Hardpoint.objects.filter(ship__id=ship.id).order_by('tag_location_y')
    buildHardpoints = BuildHardpoint.objects.filter(build__id=buildID)
    buildEngineMods = BuildEngineMod.objects.filter(build__id=buildID)
    buildHullMods = BuildHullMod.objects.filter(build__id=buildID)
    images = Image.objects.filter(ship__id=ship.id)
    if len(images) == 0:
        raise Http404() 
    allItems = Item.objects.all()
    submitBuildForm = SubmitBuildForm( initial={'role' : build.role, 'name' : build.name} )
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    renderContext = {
    'variantData_hardpoints'    : buildHardpoints,
    'variantData_engine_mods'   : buildEngineMods,
    'variantData_hull_mods'     : buildHullMods,
    'variantData_build'         : build,
    'item_list'                 : allItems,
    'image_list'                : images,
    'shipname'                  : ship.name,
    'ship'                      : ship,
    'saveVariantForm'           : submitBuildForm,
    'loginForm'                 : loginForm,
    'createUserForm'            : createUserForm
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('buildDetail.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def variantDetailPhase2(request, buildID):

    build = Build.objects.get(pk=buildID)
    if not build:
        raise Http404()

    # Get all hardpoints
    ship = build.ship
    # hardpoints = Hardpoint.objects.filter(ship__id=ship.id).order_by('tag_location_y')
    buildHardpoints = BuildHardpoint.objects.filter(build__id=buildID)
    buildEngineMods = BuildEngineMod.objects.filter(build__id=buildID)
    buildHullMods = BuildHullMod.objects.filter(build__id=buildID)
    images = Image.objects.filter(ship__id=ship.id)
    if len(images) == 0:
        raise Http404() 
    allItems = Item.objects.all()
    submitBuildForm = SubmitBuildForm( initial={'role' : build.role, 'name' : build.name} )
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    renderContext = {
    'variantData_hardpoints'    : buildHardpoints,
    'variantData_engine_mods'   : buildEngineMods,
    'variantData_hull_mods'     : buildHullMods,
    'variantData_build'         : build,
    'item_list'                 : allItems,
    'image_list'                : images,
    'shipname'                  : ship.name,
    'ship'                      : ship,
    'saveVariantForm'           : submitBuildForm,
    'loginForm'                 : loginForm,
    'createUserForm'            : createUserForm
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('buildDetail.html', renderContext, context_instance=RequestContext(request))

def submitVariant(request):
    if request.method == 'POST':
        # print(request.user)
        data = request.POST
        # data = simplejson.loads(request.raw_post_data)
        # print(data)
        # Validate that all require keys are available
        # print "Validating keys"
        valid = True
        requiredKeys = ['name', 'role', 'ship', 'hardpoint_items', 'hull_mods', 'engine_mods', 'engine_intake', 'powerplant', 'main_thruster', 'shield', 'cargo_mod']
        for requiredKey in requiredKeys:
            if not requiredKey in data:
                valid = False
                break;

        if not valid:
            # print "Missing a required key"
            raise Http404()

        hardpoint_items = stringToIntArray(data['hardpoint_items'])
        hull_mods = stringToIntArray(data['hull_mods'])
        engine_mods = stringToIntArray(data['engine_mods'])
        ships = Ship.objects.filter(pk=data['ship'])
        try:
            ship = ships[0]
        except:
            return HttpResponse("<h1>Unable to Save Variant</h1><p>Failed to find specified ship</p>")
        variantData = {
            'ship' : ship,
            'role' : data['role'],
            'name' : data['name'],
            'manufacturer_variant' : False,
            'engine_intake' : data['engine_intake'],
            'powerplant' : data['powerplant'],
            'main_thruster' : data['main_thruster'],
            'shield' : data['shield'],
            'cargo_mod' : data['cargo_mod'],
            'hardpoints' : hardpoint_items,
            'engine_mods' : engine_mods,
            'hull_mods' : hull_mods,
        }
        variant = makeVariant(variantData, saveVariant = True, user = request.user)
        return redirect('/variant/%d' % variant['build'].id)
    else:
        return Http404

@ensure_csrf_cookie
def submissionForms(request):
    renderContext = {}
    return render_to_response('bootstrap/light-blue/data_submissions.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def submissionFormShip(request):
    # print 'ship submission'
    # print request.body
    response_data = {}
    if request.is_ajax():
        # print "Ajax"
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
            data = {}
            for index in requestData:
                data[index['name']] = index['value']
            # print data
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        response_data = {
            'success' : True,
            'response' : 'ok'
        }
        body = """
        The following ship data was submitted:
        ======================================
        ship name: %s
        ship class: %s
        """ % (data['ship-name'], data['ship-class'])
        send_mail('[SSB] Ship Data Submission', body, 'no-reply@stantonspacebarn.com', ['jwvanderbeck@gmail.com'], fail_silently = True)
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    # should never get here, if it we do its f'ed up
    assert False

@ensure_csrf_cookie
def submissionFormData(request):
    # print "Generic submission"
    # print request.body
    response_data = {}
    if request.is_ajax():
        # print "Ajax"
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
            data = {}
            for index in requestData:
                data[index['name']] = index['value']
            # print data
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        response_data = {
            'success' : True,
            'response' : 'ok'
        }
        body = """
        The following data was submitted:
        ======================================
        """
        for item in data:
            if item != "csrfmiddlewaretoken":
                body = body + item + ": " + data[item] + "\n"
        send_mail('[SSB] Data Submission', body, 'no-reply@stantonspacebarn.com', ['jwvanderbeck@gmail.com'], fail_silently = True)
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    # should never get here, if it we do its f'ed up
    assert False
@ensure_csrf_cookie
def weaponDetails(request, itemName):
    # Get the item
    items = VehicleItem.objects.filter(name__iexact=itemName)
    allItems = VehicleItem.objects.all().order_by('displayName')
    if len(items) > 0:
        item = items[0]
    else:
        item = None

    if not item:
        raise Http404()

    # Apparently the charts have problems with negative values, so as a temporary workaround
    # Invert any negative values
    renderContext = {
        'itemData'      : item,
        'items'         : allItems
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/weapon.html', renderContext, context_instance=RequestContext(request))
@ensure_csrf_cookie
def weaponList(request):
    # Get the item
    allItems = VehicleItem.objects.all().filter(disabled=False)

    renderContext = {
        'items'         : allItems
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/weapons.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def itemDetails(request, itemName):
    # Get the item
    items = VehicleItem.objects.filter(name__iexact=itemName)
    if len(items) > 0:
        item = items[0]
    else:
        item = None

    if not item:
        raise Http404()

    allItems = VehicleItem.objects.all().order_by('displayName')

    renderContext = {
        'itemData'      : item,
        'items'         : allItems,
        'itemType'      : item.itemType
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/itemdata.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def itemdata(request):
    renderContext = {
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/itemdata.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def vehicledata(request):
    renderContext = {
    }

    return render_to_response('bootstrap/light-blue/vehicledata.html', renderContext, context_instance=RequestContext(request))

def itemList(request, itemTypeName):
    return HttpResponseRedirect('/items/')
def extrapolateStateValues(state, duration=30, metric=0, stacking=False):
    # Metrics:
    # 0 - Value per Second at Time
    # 1 - Total Value at Time
    # This method takes in a VehicleItem* state object with one or more values
    # and extrapolates those values to the specified duration in seconds

    # If values are negative we make them positive due to a bug in NVD3 charting

    if not state:
        return []

    stateValue = state.value
    # print stateValue
    values = []
    if "," in stateValue:
        # The value is packed to store varying values at different times
        # So we ened to build it out over the duration
        chunks = stateValue.split(",")
        stateValues = {}
        for chunk in chunks:
            stateValues[int(chunk.split(":")[0])] = int(chunk.split(":")[1])
        # print stateValues
        if not stacking:
            currentVPS = 0
            for i in range(0, duration + 1, 1):
                if i in stateValues:
                    currentVPS = stateValues[i]
                values.append(currentVPS)
        else:
            currentVPS = 0
            for i in range(0, duration + 1, 1):
                if i in stateValues:
                    currentVPS = currentVPS + stateValues[i]
                values.append(currentVPS)

    else:
        # Simple case, a single value
        stateValue = int(stateValue)
        if stateValue < 0:
            stateValue = stateValue# * -1
        if metric == 0:
            # Simplest of all cases, we just hold the value from 0-duration
            for i in range(0, duration + 1, 1):
                values.append(stateValue)
        else:
            if stacking:
                # This is a single value, but since it stacks we need to 
                # increase at a steady rate over time
                for i in range(0, duration + 1, 1):
                    values.append(stateValue * i)
            else:
                # Simplest of all cases, we just hold the value from 0-duration
                for i in range(0, duration + 1, 1):
                    values.append(stateValue)

    return values

def getGraphColorForState(stateName):
    if stateName.lower() == "idle":
        return "#AAAAAA"
    elif stateName.lower() == "active":
        return "#64c1d8"
    elif stateName.lower() == "shooting":
        return "#d62728"
    elif stateName.lower() == "targeting":
        return "#d62728"
    elif stateName.lower() == "manualcontrol":
        return "#aaaaaa"
    elif stateName.lower() == "autocontrol":
        return "#64c1d8"
    elif stateName.lower() == "default":
        return "#AAAAAA"
    else:
        return "#AAAAAA"

@ensure_csrf_cookie
def getBackgridItemList(request, itemTypeName):
    # JSON callable function to retrive a list of
    # items in Backgrid table format
    if request.is_ajax():
        print "getBackgridItemList", itemTypeName

        # Find all items that match the given ItemType
        try:
            items = VehicleItem.objects.all().filter(itemType__typeName__iexact=itemTypeName).order_by('name')
        except ObjectDoesNotExist:
            print "Unable to find any items"
            response_data = [{}]
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        response_data = []
        print "Returning items for %s" % (itemTypeName)
        for item in items:
            row = {}
            if item.displayName:
                row['displayName'] = item.displayName
            else:
                row['displayName'] = item.name
            row['name'] = item.name
            response_data.append(row)
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    assert False        

def isItemCompatibleWithPort(itemData, portData):
    # Check size for quick fallout
    if itemData.itemSize < portData.minSize:
        return False
    if itemData.itemSize > portData.maxSize:
        return False
    portTypes = []
    for portType in portData.supportedTypes.all():
        portTypes.append(portType.name)
    # If we get a perfect type:subtype match then we are good
    if itemData.itemType.name in portTypes:
        return True
    # No exact match so we need to check if the port supports
    # all of this type's subtypes
    if itemData.itemType.name.split(":")[0] in portTypes:
        return True

    return False

@ensure_csrf_cookie
def getVehicleItemList(request, itemTypeName=None, itemSubTypeName=None, vehicleName=None):
    print "getVehicleItemLis"
    # JSON callable function to retrive a list of
    # items in Backgrid table format based on the specified
    # Parameters
    if request.is_ajax():

        if itemTypeName and itemSubTypeName:
            try:
                print "Looking for items of type %s, and subtype %s" % (itemTypeName, itemSubTypeName)
                items = VehicleItem.objects.all().filter(itemType__exact=itemTypeName, itemSubType__iexact=itemSubTypeName, disabled=False)
            except:
                print "Unable to find items"
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        elif itemTypeName:
            print "Looking for items of type %s" % (itemTypeName)
            try:
                items = VehicleItem.objects.all().filter(itemType__typeName__iexact=itemTypeName, disabled=False)
                # print items
            except Exception as e:
                print "Unable to find items"
                print e
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        else:
            print "Looking for all items"
            try:
                items = VehicleItem.objects.all()
            except:
                print "Unable to find items"
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        vehicleData = None
        if vehicleName:
            print "Looking for items compatible with %s" % vehicleName
            # Get the vehicle data
            try:
                vehicleData = Vehicle.objects.get(name__iexact=vehicleName)
            except:
                print "Unable to find Vehicle"
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        response_data = []
        print "Scanning items"
        for item in items:
            if vehicleData:
                valid = False
                for port in vehicleData.itemport_set.all():
                    if isItemCompatibleWithPort(item, port):
                        print item
                        valid = True
                        break
                if not valid:
                    continue
            # print item
            row = []
            row.append(item.itemType.name)
            row.append(item.itemSize)
            # row['type'] = item.itemType.name
            # row['size'] = item.itemSize
            if item.displayName:
                # row['displayName'] = item.displayName
                row.append(item.displayName)
            else:
                # row['displayName'] = item.name
                row.append(item.name)
            # row['name'] = item.name
            row.append(item.name)
            response_data.append(row)
            response = {"aaData":response_data}
        print simplejson.dumps(response)
        return HttpResponse(simplejson.dumps(response), content_type="application/json")
    else:
        if itemTypeName and itemSubTypeName:
            try:
                print "Looking for items of type %s, and subtype %s" % (itemTypeName, itemSubTypeName)
                items = VehicleItem.objects.all().filter(itemType__exact=itemTypeName, itemSubType__iexact=itemSubTypeName, disabled=False)
            except:
                print "Unable to find items"
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        elif itemTypeName:
            print "Looking for items of type %s" % (itemTypeName)
            try:
                items = VehicleItem.objects.all().filter(itemType__typeName__iexact=itemTypeName, disabled=False)
                # print items
            except Exception as e:
                print "Unable to find items"
                print e
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        else:
            print "Looking for all items"
            try:
                items = VehicleItem.objects.all()
            except ObjectDoesNotExist:
                print "Unable to find items"
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        vehicleData = None
        if vehicleName:
            print "Looking for items compatible with %s" % vehicleName
            # Get the vehicle data
            try:
                vehicleData = Vehicle.objects.get(name__iexact=vehicleName)
            except:
                print "Unable to find Vehicle"
                response_data = [{}]
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        response_data = []
        print "Scanning items"
        for item in items:
            if vehicleData:
                valid = False
                for port in vehicleData.itemport_set.all():
                    if isItemCompatibleWithPort(item, port):
                        print item
                        valid = True
                        break
                if not valid:
                    continue
            # print item
            row = []
            row.append(item.itemType.name)
            row.append(item.itemSize)
            # row['type'] = item.itemType.name
            # row['size'] = item.itemSize
            if item.displayName:
                # row['displayName'] = item.displayName
                row.append(item.displayName)
            else:
                # row['displayName'] = item.name
                row.append(item.name)
            # row['name'] = item.name
            row.append(item.name)
            response_data.append(row)
            response = {"aaData":response_data}
        print simplejson.dumps(response)

    assert False        

@ensure_csrf_cookie
def getBackgridVehicleList(request):
    # JSON callable function to retrive a list of
    # vehicles in Backgrid table format
    if request.is_ajax():

        # Find all items that match the given ItemType
        try:
            vehicles = Vehicle.objects.all()
        except:
            # print "Unable to find any vehicles"
            response_data = [{}]
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        response_data = []
        for item in vehicles:
            row = {}
            if item.displayName:
                row['displayName'] = item.displayName
            else:
                row['displayName'] = item.name
            row['name'] = item.name
            response_data.append(row)
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    assert False 

@ensure_csrf_cookie
def getVehicleDetails(request):
    '''
    Responds to an AJAX call with details on a specified vehicle
    '''
    if request.is_ajax():
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.',
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # Find the given vehicle
        try:
            vehicle = Vehicle.objects.get(name__iexact=requestData['name'])
        except Exception as e:
            # print "Unable to find the specified vehicle"
            # print e
            response_data = {
            'success' : False,
            'response' : 'Unable to find vehicle.',
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # Update number of views
        vehicle.views = vehicle.views + 1
        vehicle.save()

        response_data = {}
        # Basic details
        if vehicle.displayName:
            response_data['name'] = vehicle.displayName
        else:
            response_data['name'] = vehicle.name
        response_data['vehicleclass'] = vehicle.vehicleClass
        response_data['vehiclecategory'] = vehicle.category.name
        response_data['ports'] = []
        for port in vehicle.itemport_set.all():
            name = port.displayName
            if not name:
                name = port.name
            portData = {'name' : name}
            portData['minsize'] = port.minSize
            portData['maxsize'] = port.maxSize
            portData['types'] = []
            supported = []
            # For each supported ItemType
            for itemType in port.supportedTypes.all():
                portData['types'].append(itemType.name)
            response_data['ports'].append(portData)

        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    assert False   

@ensure_csrf_cookie
def getItemPortDetails(request):
    '''
    Responds to an AJAX call with details on a specified ItemPort
    '''
    if request.is_ajax():
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.',
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # Find the vehicle or item this belongs to
        if "vehicleName" in requestData:
            try:
                vehicleData = Vehicle.objects.get(name__iexact = requestData["vehicleName"])
            except:
                # print "Unable to find the specified vehicle"
                response_data = {
                'success' : False,
                'response' : 'Unable to find vehicle.',
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

            try:
                itemPortData = ItemPort.objects.get(name__iexact=requestData["portName"], parentVehicle=vehicleData)
            except:
                # print "Unable to find the specified itemport"
                response_data = {
                'success' : False,
                'response' : 'Unable to find itemport.',
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        elif "itemName" in requestData:
            try:
                itemData = VehicleItem.objects.get(name__iexact = requestData["itemName"])
            except:
                # print "Unable to find the specified item"
                response_data = {
                'success' : False,
                'response' : 'Unable to find item.',
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

            try:
                itemPortData = ItemPort.objects.get(name__iexact=requestData["portName"], parentItem=itemData)
            except:
                # print "Unable to find the specified itemport"
                response_data = {
                'success' : False,
                'response' : 'Unable to find itemport.',
                }
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")


        response_data = {}
        # Basic details
        # print itemPortData
        if itemPortData.displayName:
            response_data['name'] = itemPortData.displayName
        else:
            response_data['name'] = itemPortData.name
        response_data['minsize'] = itemPortData.minSize
        response_data['maxsize'] = itemPortData.maxSize
        response_data['types'] = []
        itemTypes = itemPortData.supportedTypes.all()
        for itemType in itemTypes:
            response_data["types"].append(itemType.name)
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    assert False   

@ensure_csrf_cookie
def getItemDetails(request):
    '''
    Responds to an AJAX call with item details on a specified item
    '''
    if request.is_ajax():
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.',
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # Find the given item
        try:
            item = VehicleItem.objects.get(name__iexact=requestData['itemName'])
        except:
            # print "Unable to find the specified item"
            response_data = {
            'success' : False,
            'response' : 'Unable to find item.',
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # Update number of views
        item.views = item.views + 1
        item.save()

        response_data = {}
        # Basic details
        # print item
        if item.displayName:
            response_data['itemname'] = item.displayName
        else:
            response_data['itemname'] = item.name
        response_data['itemclass'] = item.itemClass
        response_data['itemsize'] = item.itemSize
        response_data['itemtype'] = item.itemType.name
        response_data['description'] = item.description

        # VehicleItemStats
        allStats = item.vehicleitemparams_set.all()
        response_data['itemstats'] = []
        for stat in allStats:
            response_data['itemstats'].append( {'name' : stat.name, 'value' : stat.value} )

        # Supported states
        response_data['power'] = []
        for state in VehicleItemPower.objects.filter(parentItem__exact=item):
            response_data['power'].append(state.state)
        response_data['heat'] = []
        for state in VehicleItemHeat.objects.filter(parentItem__exact=item):
            response_data['heat'].append(state.state)
        response_data['avionics'] = []
        for state in VehicleItemAvionics.objects.filter(parentItem__exact=item):
            response_data['avionics'].append(state.state)

        # ItemPorts
        response_data["ports"] = []
        allPorts = ItemPort.objects.filter(parentItem__exact=item)
        for port in allPorts:
            portData = dict()
            portData["portname"] = port.name
            if port.displayName:
                portData['name'] = port.displayName
            else:
                portData['name'] = port.name
            portData['minsize'] = port.minSize
            portData['maxsize'] = port.maxSize
            portData['types'] = []
            itemTypes = port.supportedTypes.all()
            for itemType in itemTypes:
                portData["types"].append(itemType.name)
            response_data["ports"].append(portData)
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
    assert False   

@ensure_csrf_cookie
def getPipeGraph(request):
    # JSON callable function to retrive the graph data
    # For a given pipe, and a given state
    if request.is_ajax():
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.',
            'data' : [{"values":[]}]
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")


        # Retrieve the specified item
        try:
            # print "Looking for %s" % (requestData['itemName'])
            items = VehicleItem.objects.all().filter(name__iexact=requestData['itemName'])
            item = items[0]
        except Exception as e:
            response_data = {
            'success' : False,
            'response' : 'Unable to find specified item.',
            'data' : [{"values":[]}]
            }
            # print response_data
            # print e
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # Get the proper pipe
        stacking = False
        try:
            if requestData['pipe'].lower() == "power":
                pipe = VehicleItemPower.objects.filter(parentItem__exact=item)
            elif requestData['pipe'].lower() == "heat":
                stacking = True # Heat stacks over time
                pipe = VehicleItemHeat.objects.filter(parentItem__exact=item)
            elif requestData['pipe'].lower() == "avionics":
                pipe = VehicleItemAvionics.objects.filter(parentItem__exact=item)
            else:
                response_data = {
                'success' : False,
                'response' : 'Invalid pipe requested.',
                'data' : [{"values":[]}]
                }
                # print response_data
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        except:
                response_data = {
                'success' : False,
                'response' : 'Failed to load pipe data.',
                'data' : [{"values":[]}]
                }
                # print response_data
                return HttpResponse(simplejson.dumps(response_data), content_type="application/json")


        if not pipe:
            response_data = {
            'success' : False,
            'response' : 'Unable to find specified pipe.',
            'data' : [{"values":[]}]
            }
            # print response_data
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        if not "state" in requestData:
            response_data = {
            'success' : False,
            'response' : 'No state requested.',
            'data' : [{"values":[]}]
            }
            # print response_data
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        requestedState = requestData['state']
        requestedStates = []
        if "," in requestedState:
            for stateName in requestedState.split(','):
                try:
                    state = pipe.get(state=stateName)
                except: 
                    # print "Unable to find state %s.  Ignoring" % stateName
                    state = None
                if state:
                    requestedStates.append(state)
        elif requestedState.lower() == "all":
            requestedStates = pipe.all()
        else:
            try:
                state = pipe.get(state=requestedState)
            except: 
                # print "Unable to find state %s.  Ignoring" % requestedState
                state = None
            if state:
                requestedStates.append(state)

        if len(requestedStates) == 0:
            response_data = {
            'success' : False,
            'response' : 'No valid states found.',
            'data' : [{"values":[]}]
            }
            # print response_data
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        # At this point we should have a list of all pipe states
        # requested that we were able to find.
        # We extrapolate the data out to a 30 second period
        # for the chart

        data = []
        for state in requestedStates:
            if "-" in state.value:
                negativeValues = True
            else:
                negativeValues = False
            stateValues = extrapolateStateValues(state, 30, metric=requestData['metric'], stacking=stacking)
            stateData = {   'key'    : state.state,
                            'color'  : getGraphColorForState(state.state),
                            'values' : []
                        }
            for second in range(0,31,1):
                value = stateValues[second]
                stateData['values'].append( {'x' : second, 'y' : value} )

            data.append(stateData)

        response_data = {
        'success' : True,
        'response' : 'Blah',
        'negative'  : negativeValues,
        'data' : data
        }
        # print response_data
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

    else:
        # This should never be anything but an AJAX call, so
        # someone is doing somethign fishy!
        assert False

@ensure_csrf_cookie
def getGraph(request, graphType):
    # JSON callable function to retrive graph data
    if request.is_ajax():
        try:
            requestData = simplejson.loads(request.body)
            # print "JSON Data:"
            # print requestData
        except:
            # print "json parse failed"
            response_data = {
            'success' : False,
            'response' : 'Unable to parse JSON object.',
            'data' : [{"values":[]}]
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

        if graphType == "available-power":
            # Takes in a json list of dictionaries IE
            # [ {"item1" : "state1"}, {"item2":"state2"}]
            # and returns the totoal amount of power generated, and the total amount of power consumed
            # print "Computing graph data for available-power"
            powerConsumed = 0.0
            powerGenerated = 0.0
            for entry in requestData["items"]:
                itemName = entry["name"]
                itemState = entry["state"]
                try:
                    item = VehicleItem.objects.get(name__iexact=itemName)
                except:
                    print "Failed to find item %s" % (itemName)
                    continue
                if item.itemType.typeName == "powerplant":
                    try:
                        powerData = VehicleItemPower.objects.get(parentItem__exact = item, state="Default")
                        powerGenerated = powerGenerated + float(powerData.value)
                    except ObjectDoesNotExist:
                        pass
                        # print "Failed to get Default state for PowerPlant %s" % (itemName)
                else:
                    try:
                        powerData = VehicleItemPower.objects.get(parentItem__exact = item, state=itemState)
                        # powerData = item.power.get(state=itemState)
                        powerConsumed = powerConsumed + float(powerData.value)
                    except ObjectDoesNotExist:
                        pass
                        # print "Failed to get %s state for item %s" % (itemState, itemName)
            response_data = {
            'success' : True,
            'response' : 'Power usage.',
            'data' : {"powerConsumed" : powerConsumed,"maxPower" : powerGenerated}
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
    else:
        # This should never be anything but an AJAX call, so
        # someone is doing somethign fishy!
        assert False

@ensure_csrf_cookie
def shipLayout(request, shipName):
    shipData = Vehicle.objects.get(name__iexact=shipName)
    shipData.views = shipData.views + 1
    shipData.save()
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    submitBuildForm = SubmitBuildForm()

    renderContext = {
        'shipData'      : shipData,
        'loginForm'     : loginForm,
        'createUserForm': createUserForm,
        'variantForm'   : submitBuildForm
    }

    return render_to_response('bootstrap/light-blue/shipMain.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def shipLayoutTest(request, shipName):
    shipData = Vehicle.objects.get(name__iexact=shipName)
    shipData.views = shipData.views + 1
    shipData.save()
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    submitBuildForm = SubmitBuildForm()

    # Get all types and subtypes for filtering on the item browser
    # to do this we need to build a list of all subtypes for a given main type and skip empty ones
    itemTypes = {}
    allItemTypes = VehicleItemType.objects.all()
    for itemType in allItemTypes:
        if itemType.typeName and itemType.subTypeName:
            if itemType.typeName in itemTypes:
                itemTypes[itemType.typeName].append(itemType.subTypeName)
            else:
                itemTypes[itemType.typeName] = [itemType.subTypeName]

    renderContext = {
        'shipData'      : shipData,
        'loginForm'     : loginForm,
        'createUserForm': createUserForm,
        'variantForm'   : submitBuildForm,
        'itemTypes'     : itemTypes
    }
    logger = logging.getLogger("shipBuilder")
    logger.debug("Test")
    return render_to_response('metronic/admin/shipMain_test.html', renderContext, context_instance=RequestContext(request))

def phase2(request):
    renderContext = {
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/phase2.html', renderContext, context_instance=RequestContext(request))

def phase2ShipList(request):
    vehicles = Vehicle.objects.all().order_by("displayName")

    renderContext = {
    'vehicle_list'      : vehicles
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/shipList.html', renderContext, context_instance=RequestContext(request))

def phase2VariantList(request):
    variants = Variant.objects.all().order_by("-creation_date")

    renderContext = {
    'variant_list'      : variants
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/variantsList.html', renderContext, context_instance=RequestContext(request))

def gameUpdateList(request):
    updates = GameUpdate.objects.all().order_by("-creation_date")

    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    renderContext = {
    'loginForm'         : loginForm,
    'createUserForm'    : createUserForm,
    'updates_list'      : updates
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/gameUpdateList.html', renderContext, context_instance=RequestContext(request))

def gameUpdate(request, pk):
    update = GameUpdate.objects.get(pk=pk)
    changes = GameUpdateChange.objects.filter(update=update).order_by("-creation_date").order_by("entityName")

    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    renderContext = {
    'update'            : update,
    'loginForm'         : loginForm,
    'createUserForm'    : createUserForm,
    'changes'           : changes
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/gameUpdate.html', renderContext, context_instance=RequestContext(request))

def gameUpdatesByEntity(request, entityName):
    changes = GameUpdateChange.objects.filter(entityName=entityName).order_by("-creation_date")

    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    renderContext = {
    'entityName'        : entityName,
    'loginForm'         : loginForm,
    'createUserForm'    : createUserForm,
    'changes'           : changes
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('bootstrap/light-blue/gameUpdateByEntity.html', renderContext, context_instance=RequestContext(request))

def testView(request):
    # shipName = '300i'  
    # Get all hardpoints
    # hardpoints = Hardpoint.objects.filter(ship__name__iexact=shipName).order_by('tag_location_y')
    # items = Item.objects.all()
    # images = Image.objects.filter(ship__name__iexact=shipName)
    # item_types = ItemType.objects.filter(hardpoint_type=True)
    submitBuildForm = SubmitBuildForm()
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    # vehicles = Vehicle.objects.all()
    # itemPorts = ItemPort.objects.all().filter(parentVehicle__exact=vehicles[0])
    # if len(images) == 0:
    #     raise Http404() 
    renderContext = {
    # 'hardpoint_list'    : hardpoints,
    # 'item_list'         : items,
    # 'image_list'        : images,
    # 'shipname'          : shipName,
    # 'ship'              : images[0].ship,
    # 'itemtype_list'     : item_types,
    'saveVariantForm'           : submitBuildForm,
    'loginForm'                 : loginForm,
    'createUserForm'            : createUserForm
    # 'port_list'         : itemPorts,
    # 'vehicle_list'      : vehicles
    }

    # The bit here about context_instance=RequestContext(request) is ABSOLUTELY VITAL 
    # as it is what enables the resulting rendered view to contain the CSRF token!
    # !!!!!!!!!!!!!
    return render_to_response('metronic/admin/databanks_items.html', renderContext, context_instance=RequestContext(request))

@ensure_csrf_cookie
def createOrUpdateVariant(request):
    if request.is_ajax():
        try:
            data = simplejson.loads(request.body)
        except:
            response_data = {
            'variantID' : 0,
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        # print data

        # What we need:
        #   Name of ship
        #   Name of variant
        #   Desired Role
        #   list of dicts, with name of hardpoint, and name of item
        #   EG
        #   data["shipName"] = "oj_350r"
        #   data["ports"] = [ {"portName" : "nose_slot", "itemName" : "mass_driver"} ]
        #   optionally a port record can contain parentPort and parentItem IDs for ports
        #   that are on items.
        shipName = data["shipName"]
        if not shipName:
            response_data = {
            'variantID' : 0,
            'success' : False,
            'response' : 'Missing vehicle name'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        variantName = None
        variantRole = None
        variantID = None
        if "variantID" in data:
            variantID = int(data["variantID"])
        print data["formData"]
        for entry in data["formData"]:
            print entry
            if entry["name"] == "name":
                variantName = entry["value"]
            elif entry["name"] == "role":
                variantRole = entry["value"]
        if not variantName:
            response_data = {
            'variantID' : 0,
            'success' : False,
            'response' : 'Missing variant name'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        if not variantRole:
            response_data = {
            'variantID' : 0,
            'success' : False,
            'response' : 'Missing variant role'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        # Store the variant's basic data
        variantData = {
            "name"      : variantName,
            "role"      : variantRole,
            "items"     : []
        }
        # Find the vehicle for this variant
        try:
            vehicleData = Vehicle.objects.get(name__iexact=shipName)
        except:
            response_data = {
            'variantID' : 0,
            'success' : False,
            'response' : 'Failed to load data for vehicle %s' % shipName
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
        # Save the base vehicle in our data
        variantData["baseVehicle"] = vehicleData
        # Iterate through all the ports and items and verify each is valid
        # If they are then add them to the data
        # If any are invalid we will skip them and save the variant
        # with as many as are valid, but inform the user
        warnings = False
        itemWarnings = []
        for port in data["ports"]:
            portName = port["portName"]
            itemName = port["itemName"]
            if "parentPort" in port:
                parentPort = port["parentPort"]
            else:
                parentPort = None
            if "parentItem" in port:
                parentItem = port["parentItem"]
            else:
                parentItem = None

            try:
                if parentItem and parentPort:
                    parentItemData = VehicleItem.objects.get(name__iexact=parentItem);
                    portData = ItemPort.objects.get(name__iexact=portName, parentItem__exact=parentItemData)
                    parentPortData = ItemPort.objects.get(name__iexact=parentPort, parentVehicle__exact=vehicleData)
                else:
                    portData = ItemPort.objects.get(name__iexact=portName, parentVehicle__exact=vehicleData)
                    itemData = VehicleItem.objects.get(name__iexact=itemName)
                item = {
                    "port" : portData,
                    "item" : itemData
                }
                if parentItem and parentPort:
                    item["parentItem"] = parentItemData
                    item["parentPort"] = parentPortData
                variantData["items"].append(item)
            except ObjectDoesNotExist:
                warnings = True
                warning = {
                    "portName" : portName,
                    "itemName" : portItem
                }
                if parentItem:
                    warning["parentItem"] = parentItem
                if parentPort:
                    warning["parentPort"] = parentPort
                itemWarnings.append(warning)

        # At this point we should have a variantData structure with everything we need to actually create
        # and save the variant
        # Create the Variant model object
        if variantID:
            variant = Variant.objects.get(pk__exact=variantID)
            VariantItem.objects.filter(variant__exact=variant).delete()
            variant.name = variantData["name"]
            variant.role = variantData["role"]
            variant.save()
        else:
            variant = Variant(
                    baseVehicle = variantData["baseVehicle"],
                    name = variantData["name"],
                    role = variantData["role"],
                    created_by = request.user
                )
            variant.save()
        # Create each VariantItem needed
        for item in variantData["items"]:
            # print
            # print "Processing item"
            # print item
            variantItem = VariantItem(variant = variant, item = item["item"], port = item["port"])
            if "parentItem" in item:
                variantItem.parentItem = item["parentItem"]
            if "parentPort" in item:
                variantItem.parentPort = item["parentPort"]
            variantItem.save()

        response_data = {
            'variantID' : variant.id,
            'success' : True,
            "warnings" : warnings,
            "warningData" : itemWarnings,
            'response' : 'ok'
        }
        return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

def displayVariant(request, variantID):
    try:
        variant = Variant.objects.get(pk=variantID)
    except:
        return HttpResponse("<h1>Unable to load Variant</h1><p>Failed to find specified variant</p>")

    itemGroups = VariantItem.objects.filter(variant__exact=variant)
    ports = []
    items = []
    variantData = []
    for itemGroup in itemGroups:
        if itemGroup.parentPort:
            parentPortData = itemGroup.parentPort
            parentItemData = itemGroup.parentItem
        else:
            parentPortData = None
            parentItemData = None
        portData = itemGroup.port
        itemData = itemGroup.item
        if parentPortData:
            variantData.append({"port" : portData, "item" : itemData, "parentPort" : parentPortData, "parentItem" : parentItemData})
        else:
            variantData.append({"port" : portData, "item" : itemData})
    vehicleData = variant.baseVehicle
    loginForm = AuthenticationForm()
    createUserForm = UserCreationForm()
    submitBuildForm = SubmitBuildForm()
    renderContext = {
        'shipData'          : vehicleData,
        'variantData'       : variantData,
        'loginForm'         : loginForm,
        'createUserForm'    : createUserForm,
        'variantForm'       : submitBuildForm,
        'variant'           : variant
    }
    return render_to_response('bootstrap/light-blue/variant.html', renderContext, context_instance=RequestContext(request))
