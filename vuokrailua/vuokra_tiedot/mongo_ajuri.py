#-*- coding: utf-8 -*-
from pymongo import MongoClient


# Ohjelma vaatii lokaalisti käynnissä olevan
# mongo-palvelimen, josta löytyy databaselta asunnot kasa.

def hae_data():
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    data = []
    for kohde in collection.find():
        data.append(kohde)
    return data

    
def find(vuokramin, vuokramax, neliomin, neliomax):
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    data = []
    for kohde in collection.find():
        print kohde
        if (kohde[0] <= vuokramax and kohde[4] <= neliomax): 
            data.append(kohde)
    return data
