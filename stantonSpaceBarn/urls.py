from django.conf.urls import patterns, include, url
from django.contrib import auth
from django.contrib.auth.views import login, password_reset

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('stantonSpaceBarn.views',
	url(r'^$', 'shipList'),
	url(r'^barn/$', 'shipList'),
	url(r'^users/login/$', 'userLogin'),
	url(r'^users/logout/$', 'userLogout'),
	url(r'^users/create/$', 'userCreate'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/reset/', password_reset),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^ship-builder/', include('shipBuilder.urls')),
    url(r'^test/$', 'testView'),
	url(r'^ship/([a-zA-Z0-9_-]+)', 'shipDetail'),
	url(r'^ships/$', 'shipList'),
	url(r'^variant/([0-9]+)', 'variantDetail'),
	url(r'^variants/', 'variantList'),
	url(r'^hangar/', 'userHangar'),
	url(r'^save-variant/', 'submitVariant'),
	url(r'^update-variant/', 'updateBuild'),
	url(r'^delete-variant/', 'deleteBuild'),
	url(r'^quick-variant/([a-zA-Z0-9_-]+)/([0-9a-zA-Z_-]+)/', 'quickVariant'),
	url(r'^quick-variant/([a-zA-Z0-9_-]+)/([0-9a-zA-Z_-]+)', 'quickVariant'),
	url(r'^quick-variant/([a-zA-Z0-9_-]+)/', 'quickVariant'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^submissions/ship/', 'submissionFormData'),
	url(r'^submissions/weapon/', 'submissionFormData'),
	url(r'^submissions/', 'submissionForms'),
	url(r'^items/$', 'itemdata'),
	url(r'^vehicles/$', 'vehicledata'),
	url(r'^items/details/$', 'getItemDetails'),
	url(r'^items/detail/([a-zA-Z0-9_-]+)/$', 'itemDetails'),
	url(r'^items/pipegraph/$', 'getPipeGraph'),
	url(r'^items/([a-zA-Z0-9_-]+)/$', 'itemList'),
	url(r'^items/list/([a-zA-Z0-9_-]+)$', 'getBackgridItemList'),
	url(r'^vehicles/list/$', 'getBackgridVehicleList'),
	url(r'^vehicles/details/$', 'getVehicleDetails'),
	url(r'^phase2/ship/([a-zA-Z0-9_-]+)', 'shipLayout'),
	url(r'^phase2/$', 'phase2'),
	url(r'^items/get/([a-zA-Z0-9_-]+)$', 'getVehicleItemList'),
	
	url(r'^graphs/get/(?P<graphType>[a-zA-Z0-9_-]+)/$', 'getGraph'),
	url(r'^itemports/details/$', 'getItemPortDetails'),

	# Get all VehicleItem entries
	url(r'^items/get/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_-]+)/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType and VehicleItemSubType
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_-]+)/subtype/(?P<itemSubTypeName>[a-zA-Z0-9_-]+)/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType and VehicleItemSubType that are compatible with the specified Vehicle
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_-]+)/subtype/(?P<itemSubTypeName>[a-zA-Z0-9_-]+)/compatible-with-vehicle/(?P<vehicleName>[a-zA-Z0-9_-]+)/$', 'getVehicleItemList'),
	# Get VehicleItem entries of the specified VehicleItemType that are compatible with the specified Vehicle
	url(r'^items/get/type/(?P<itemTypeName>[a-zA-Z0-9_-]+)/compatible-with-vehicle/(?P<vehicleName>[a-zA-Z0-9_-]+)/$', 'getVehicleItemList'),
	# Get all VehicleItem entries that are compatible with the specified Vehicle
	url(r'^items/get/compatible-with-vehicle/(?P<vehicleName>[a-zA-Z0-9_-]+)/$', 'getVehicleItemList'),
)


