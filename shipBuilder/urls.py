from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from shipBuilder import views

urlpatterns = patterns('shipBuilder.views',
    url(r'^manufacturers/$', views.ManufacturerList.as_view(), name='manufacturer-list'),
    url(r'^manufacturers/(?P<pk>[0-9]+)$', views.ManufacturerDetail.as_view(), name='manufacturer-detail'),
    # url(r'^hardpoints/$', views.HardpointList.as_view(), name='hardpoint-list'),
    # url(r'^hardpoints/by-class/(?P<hardpoint_class>[0-9]+)$', views.hardpointListByClass),
    # url(r'^hardpoints/(?P<pk>[0-9]+)$', views.HardpointDetail.as_view(), name='hardpoint-detail'),
    # url(r'^items/$', views.ItemList.as_view(), name='item-list'),
    # url(r'^items/(?P<pk>[0-9]+)$', views.ItemDetail.as_view(), name='item-detail'),
    # url(r'^items/for-hardpoint/(?P<hardpoint_id>[0-9]+)$', views.itemsForHardpoint),
    # url(r'^itemcategories/$', views.ItemCategoryList.as_view(), name='itemcategory-list'),
    # url(r'^itemcategories/(?P<pk>[0-9]+)$', views.ItemCategoryDetail.as_view(), name='itemcategory-detail'),
    # url(r'^ships/$', views.ShipList.as_view(), name='ship-list'),
    # url(r'^ships/(?P<pk>[0-9]+)$', views.ShipDetail.as_view(), name='ship-detail'),
    # url(r'^images/$', views.ImageList.as_view(), name='image-list'),
    # url(r'^images/(?P<pk>[0-9]+)$', views.ImageDetail.as_view(), name='image-detail'),
    # url(r'^builds/$', views.BuildList.as_view(), name='build-list'),
    # url(r'^builds/(?P<pk>[0-9]+)$', views.BuildDetail.as_view(), name='build-detail'),
    url(r'^vehicles/$', views.vehicleList, name='vehicle-list'),
    url(r'^vehicles/(?P<pk>[0-9]+)$', views.vehicleDetail, name='vehicle-detail'),
    url(r'^vehicleitems/$', views.vehicleItemList, name='vehicleitem-list'),
    url(r'^vehicleitems/(?P<pk>[0-9]+)$', views.vehicleItemDetail, name='vehicleitem-detail'),
    url(r'^itemports/$', views.itemPortList, name='itemport-list'),
    url(r'^itemports/(?P<pk>[0-9]+)$', views.itemPortDetail, name='itemport-detail'),
    url(r'^itemports/byvehicle/(?P<pk>[0-9]+)$', views.itemPortListByVehicle, name='itemport-listbyvehicle'),
    url(r'^itemtypes/$', views.itemTypeList, name='itemtype-list'),
	url(r'^$', 'api_root'),
)

urlpatterns = format_suffix_patterns(urlpatterns)