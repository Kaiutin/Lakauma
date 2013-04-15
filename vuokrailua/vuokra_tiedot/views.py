from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
import json
import pymongo

def index(request):
    return render(request, 'vuokra_tiedot/index.html')


def get_json(request): 
    data = []
    with open('/home/samuel/Documents/lakauma/Lakauma/vuokrailua/vuokra_tiedot/items.json') as f:
        for line in f:
            data.append(json.loads(line))
    return HttpResponse(data)





















#-------------------------#
def getHTML():
    html_object = open('/home/samuel/Documents/lakauma/Lakauma/vuokrailua/vuokra_tiedot/map_drawer.html', 'r')
    file_as_string = ""    
    for line in html_object:
        file_as_string = file_as_string + line
    return file_as_string

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
