from django.conf.urls import patterns, include, url
from django.contrib import auth
from django.contrib.auth.views import login, password_reset

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('stantonSpaceBarn.views',
	url(r'^$', 'bullshit'),
	url(r'^barn/$', 'bullshit'),
	url(r'^users/login/$', 'bullshit'),
	url(r'^users/logout/$', 'bullshit'),
	url(r'^users/create/$', 'bullshit'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/reset/', password_reset),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^test/$', 'testView'),
	url(r'^ship/([a-zA-Z0-9_-]+)', 'bullshit'),
	url(r'^ships/$', 'bullshit'),
	url(r'^variant/([0-9]+)', 'bullshit'),
	url(r'^variants/', 'bullshit'),
	url(r'^hangar/', 'bullshit'),
	url(r'^save-variant/', 'bullshit'),
	url(r'^update-variant/', 'bullshit'),
	url(r'^delete-variant/', 'bullshit'),
	url(r'^quick-variant/([a-zA-Z0-9_-]+)/([0-9a-zA-Z_-]+)/', 'bullshit'),
	url(r'^quick-variant/([a-zA-Z0-9_-]+)/([0-9a-zA-Z_-]+)', 'bullshit'),
	url(r'^quick-variant/([a-zA-Z0-9_-]+)/', 'bullshit'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^submissions/ship/', 'bullshit'),
	url(r'^submissions/weapon/', 'bullshit'),
	url(r'^submissions/', 'bullshit'),
	url(r'^items/$', 'bullshit'),
	url(r'^vehicles/$', 'bullshit'),
	url(r'^items/details/$', 'bullshit'),
	# url(r'^items/detail/([a-zA-Z0-9_&-]+)/$', 'itemDetails'),
	url(r'^items/pipegraph/$', 'bullshit'),
	url(r'^bullshit/$', 'bullshit'),

	# url(r'^items/([a-zA-Z0-9_&-]+)/$', 'itemList'),
	# url(r'^items/list/([a-zA-Z0-9_&-]+)$', 'getBackgridItemList'),
	# url(r'^vehicles/list/$', 'getBackgridVehicleList'),
	# url(r'^vehicles/details/$', 'getVehicleDetails'),
	# url(r'^items/get/([a-zA-Z0-9_&-]+)$', 'getVehicleItemList'),

	# Phase 2 URLS
    url(r'^ship-builder/', include('shipBuilder.urls')),
	# url(r'^phase2/save-variant/', 'createOrUpdateVariant'),
	# url(r'^phase2/ship/([a-zA-Z0-9_&-]+)', 'shipLayout'),
	# url(r'^phase2/$', 'phase2ShipList'),
	# url(r'^phase2/variants$', 'phase2VariantList'),
	# url(r'^phase2/variant/([0-9]+)$', 'displayVariant'),

	url(r'^phase2/shiptest/([a-zA-Z0-9_&-]+)', 'shipLayoutTest'),


	url(r'^phase2/ship/([a-zA-Z0-9_&-]+)', 'bullshit'),
	url(r'^phase2/$', 'bullshit'),
	url(r'^phase2/variants$', 'bullshit'),
	url(r'^phase2/variant/([0-9]+)$', 'bullshit'),

	url(r'^phase2/gameupdates/$', 'gameUpdateList'),
	url(r'^phase2/gameupdate/([0-9]+)$', 'gameUpdate'),
	url(r'^phase2/gameupdatebyentity/([a-zA-Z0-9_&-]+)$', 'gameUpdatesByEntity'),
	
	url(r'^graphs/get/(?P<graphType>[a-zA-Z0-9_&-]+)/$', 'getGraph'),
	url(r'^compute/stats/$', 'computeStats'),
	url(r'^itemports/details/$', 'getItemPortDetails'),
	url(r'^vehicleitem/tooltip/pipes/(?P<itemName>[a-zA-Z0-9_&-]+)/$', 'getItemTooltipPagePipes'),
	url(r'^vehicleitem/tooltip/basic/(?P<itemName>[a-zA-Z0-9_&-]+)/$', 'getItemTooltipPageBasic'),
	url(r'^vehicleitem/tooltip/details/(?P<itemName>[a-zA-Z0-9_&-]+)/$', 'getItemTooltipPageDetails'),
	# API Docs
	url(r'^api-docs/', include('rest_framework_swagger.urls')),

	# Get all VehicleItem entries
	url(r'^items/get/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_&-]+)/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType and VehicleItemSubType
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_&-]+)/subtype/(?P<itemSubTypeName>[a-zA-Z0-9_&-]+)/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType and VehicleItemSubType that are compatible with the specified Vehicle
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_&-]+)/subtype/(?P<itemSubTypeName>[a-zA-Z0-9_&-]+)/compatible-with-vehicle/(?P<vehicleName>[a-zA-Z0-9_&-]+)/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType that are compatible with the specified Vehicle
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_&-]+)/compatible-with-vehicle/(?P<vehicleName>[a-zA-Z0-9_&-]+)/$', 'getVehicleItemList'),
	# Get all VehicleItem entries that are compatible with the specified Vehicle
	url(r'^items/get/compatible-with-vehicle/(?P<vehicleName>[a-zA-Z0-9_&-]+)/$', 'getVehicleItemList'),
	url(r'^items/get/compatible-with-vehicleport/(?P<vehicleName>[a-zA-Z0-9_&-]+)/(?P<hardpointName>[a-zA-Z0-9_&-]+)/$', 'getItemListForHardpoint'),
	url(r'^items/get/compatible-with-itemport/(?P<itemName>[a-zA-Z0-9_&-]+)/(?P<hardpointName>[a-zA-Z0-9_&-]+)/$', 'getItemListForItemHardpoint'),
)


