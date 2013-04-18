from django.conf.urls import patterns, url

from vuokra_tiedot import views

# Here you can define which methods/views are matched with differents urls.
# For example "url(r'get_json', views.get_json, name='get_json')," will match any 
# url which starts with "http://ip-where-server-runs/vuokra_tiedot/" and ends 
# in "get_json" with method get_json found in /vuokrailua/vuokra_tiedot/views.py
# module. 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'get_json', views.get_json, name='get_json'),
)
