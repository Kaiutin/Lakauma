from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
import json
import mongo_ajuri

# Here you can define the methods associated with urls found in urls.py.
# You can construct a new view simply by adding the method here and pointing 
# an url in urls.py to it. All views must return a HttpResponse-object, which
# can be just about anything. For example, "index" renders a HttpResponse from
# template file in /vuokrailua/vuokra_tiedot/templates/vuokra_tiedot/index.html

def index(request):
    return render(request, 'vuokra_tiedot/index.html')

def get_json(request):
    taulu = mongo_ajuri.hae_data()
    data = taulu[:]
    lista = []
    for kohde in data:
        lista.append(kohde)
    return HttpResponse(json.dumps(lista))


