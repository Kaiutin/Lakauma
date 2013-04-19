#-*- coding: utf-8 -*-
from pymongo import MongoClient

# This module is responsible for communicating with mongodb 
# running locally on your computer. 

# Get current apartments data (asunnot) from database.
def hae_data(vuokramin=0, vuokramax=100000000, neliomin=0, neliomax=100000):
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    return collection.find({ "vuokra": { "$gte": vuokramin, "$lte": vuokramax }})
    
def remove():
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    collection.remove()
    
    
#def import():
    
    
    
#def export():
    
