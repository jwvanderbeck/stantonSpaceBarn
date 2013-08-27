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
            print data
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
            print data
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
    print variantData['hardpoints']
    for item in variantData['hardpoints']:
        itemID = getItemByID(item)
        hardpoints.append(itemID)
        print itemID
    print hardpoints
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
    print 'Hardpoints ', hardpoints
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
    print variantData['hardpoints']
    for item in variantData['hardpoints']:
        itemID = getItemByID(item)
        hardpoints.append(itemID)
        print itemID
    print hardpoints
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
    if request.is_ajax():
        try:
            data = simplejson.loads(request.body)
        except:
            response_data = {
            'url' : 'Z',
            'success' : False,
            'response' : 'Unable to parse JSON object.'
            }
            return HttpResponse(simplejson.dumps(response_data), content_type="application/json")

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

    # Display a quick Variant

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
    variantDetails = variantURL.split('-')
    variantVersion = variantDetails[0]

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


def submitVariant(request):
    if request.method == 'POST':
        print(request.user)
        data = request.POST
        # data = simplejson.loads(request.raw_post_data)
        print(data)
        # Validate that all require keys are available
        print "Validating keys"
        valid = True
        requiredKeys = ['name', 'role', 'ship', 'hardpoint_items', 'hull_mods', 'engine_mods', 'engine_intake', 'powerplant', 'main_thruster', 'shield', 'cargo_mod']
        for requiredKey in requiredKeys:
            if not requiredKey in data:
                valid = False
                break;

        if not valid:
            print "Missing a required key"
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
    print 'ship submission'
    print request.body
    response_data = {}
    if request.is_ajax():
        print "Ajax"
        try:
            requestData = simplejson.loads(request.body)
            print "JSON Data:"
            print requestData
            data = {}
            for index in requestData:
                data[index['name']] = index['value']
            print data
        except:
            print "json parse failed"
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
    print "Generic submission"
    print request.body
    response_data = {}
    if request.is_ajax():
        print "Ajax"
        try:
            requestData = simplejson.loads(request.body)
            print "JSON Data:"
            print requestData
            data = {}
            for index in requestData:
                data[index['name']] = index['value']
            print data
        except:
            print "json parse failed"
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

def testView(request):
    shipName = '300i'  
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
    return render_to_response('bootstrap/light-blue/grid.html', renderContext, context_instance=RequestContext(request))