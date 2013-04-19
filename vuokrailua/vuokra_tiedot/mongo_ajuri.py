#-*- coding: utf-8 -*-
from pymongo import MongoClient

# This module is responsible for communicating with mongodb 
# running locally on your computer. 

# Get current apartments data (asunnot) from database.
def hae_data(vuokramin=0, vuokramax=100000000, neliomin=0, neliomax=100000):
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
    
