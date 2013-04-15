from django.conf.urls import patterns, url

from vuokra_tiedot import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'json', views.get_json, name='get_json'),
)
