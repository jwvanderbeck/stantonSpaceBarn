from django.conf.urls import patterns, include, url
from django.contrib import auth

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('stantonSpaceBarn.views',
	url(r'^$', 'redirectToBlog'),
	url(r'^users/login/$', 'userLogin'),
	url(r'^users/logout/$', 'userLogout'),
	url(r'^users/create/$', 'userCreate'),
    url(r'^admin/', include(admin.site.urls)),
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
	url(r'^quick-variant/([a-zA-Z0-9]+)/([0-9a-zA-Z-]+)/', 'quickVariant'),
	url(r'^quick-variant/([a-zA-Z0-9]+)/([0-9a-zA-Z-]+)', 'quickVariant'),
	url(r'^quick-variant/([a-zA-Z0-9]+)/', 'quickVariant'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^submissions/ship/', 'submissionFormData'),
	url(r'^submissions/weapon/', 'submissionFormData'),
	url(r'^submissions/', 'submissionForms'),
)


