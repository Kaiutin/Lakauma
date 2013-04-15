from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.static import * 
from django.conf import settings
from vuokra_tiedot import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vuokrailua.views.home', name='home'),
    # url(r'^vuokrailua/', include('vuokrailua.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:    
    url(r'^vuokra_tiedot/', include('vuokra_tiedot.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/', include('vuokra_tiedot.urls')),
)
