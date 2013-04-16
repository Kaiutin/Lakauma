#-*- coding: utf-8 -*-
from pymongo import MongoClient


# Ohjelma vaatii lokaalisti käynnissä olevan
# mongo-palvelimen, josta löytyy databaselta asunnot kasa.

def hae_data():
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    return collection.find({}, {"_id": 0})

    
def find(vuokramin, vuokramax, neliomin, neliomax):
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    data = []
    for kohde in collection.find():
        if (int(kohde["vuokra"]) >= vuokramin and  int(kohde["vuokra"]) <= vuokramax and float(kohde["neliot"]) >= neliomin and float(kohde["neliot"]) <= neliomax): 
            data.append(kohde)
    return data
    
def remove():
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    collection.remove()
    
    
#def import():
    
    
    
#def export():
    
