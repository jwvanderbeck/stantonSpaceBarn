from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
from shipBuilder.models import Hardpoint, Item, ItemType, ItemCategory, Image

def show_300i_phase3(request):
    # Get all hardpoints
    hardpoints = Hardpoint.objects.all()
    allItems = Item.objects.all()
    images = Image.objects.all()
    items = []
    for item in allItems:
        if not item.icon:
            icon = ''
        else:
            icon = item.icon.url
        items.append({
            'icon' : icon,
            'manufacturer' : item.manufacturer,
            'model' : item.name,
            'rate_of_fire' : item.rate_of_fire,
            'id' : item.id,
            'hardpoint_class' : item.hardpoint_class,
            'item_category' : item.item_category,
        })
    # Determine which properties to show in the item browser, and make a list of those fields for the template
    # For right now, this is hardcoded
    
    # These fields are used behind the scenes, and should not be shown to the user
    neverShowFields = ['item_type', 'item_category', 'hardpoint_class']
    headers = []
    headers.append({'name' : 'icon'})
    headers.append({'name' : 'manufacturer'})
    headers.append({'name' : 'model'})
    headers.append({'name' : 'rate_of_fire'})
    headers.append({'name' : 'id'})
    renderContext = {
    'hardpoint_list'    : hardpoints,
    'header_list'       : headers,
    'item_list'         : items,
    'image_list'         : images,
    }
    t = get_template('prototypes/phase3/sbb_300i.html')
    r = t.render(Context(renderContext))
    return HttpResponse(r)
    assert False
    return render_to_response('prototypes/phase3/sbb_300i.html', renderContext)
