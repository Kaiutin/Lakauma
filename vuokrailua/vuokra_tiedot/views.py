from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
import json
import mongo_ajuri


def index(request):
    return render(request, 'vuokra_tiedot/index.html')


#def get_json(request):
#    return HttpResponse(mongo_ajuri.hae_data())

def get_json(request):
    taulu = mongo_ajuri.hae_data()
    data = taulu[:]
    lista = []
    for kohde in data:
        lista.append(kohde)
    return HttpResponse(json.dumps(lista))

#def get_json(request): 
#    data = mongo_ajuri.hae_data()
#    taulu = ""    
#    for kohde in data:
#        taulu = taulu + str(kohde) + ","
#    return HttpResponse(taulu[:-2]) 

