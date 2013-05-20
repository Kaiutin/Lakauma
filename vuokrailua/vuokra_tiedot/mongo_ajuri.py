#-*- coding: utf-8 -*-
from pymongo import MongoClient

# This module is responsible for communicating with mongodb 
# running locally on your computer. 

# Get current apartments data (asunnot) from database.
def hae_data(vuokramin, vuokramax, neliomin, neliomax):
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    collection2 = db.paakohteet
    data = []
    data2 = []
    i = 0
    for kohde in collection.find({},{"_id": 0}):
        i += 1
        try:
            if (int(kohde["vuokra"]) >= vuokramin and  int(kohde["vuokra"]) <= vuokramax and float(kohde["neliot"]) >= neliomin and float(kohde["neliot"]) <= neliomax): 
                if (str(kohde["tarjoaja"]) == "KOAS"):
                    data2.append(str(kohde["linkki"]))
                    print i + 1500
                    continue
                    
                data.append(kohde)
                print kohde
                
        except ValueError:
            if(int(kohde["vuokra"]) >= vuokramin and  int(kohde["vuokra"]) <= vuokramax):
                if (str(kohde["tarjoaja"]) == "KOAS"):
                    data2.append(str(kohde["linkki"]))
                    print i + 1700
                    continue
                    
                data.append(kohde)
                print i + 2000                      

    data2 = data2[:]
    
    data2 = list(set(data2))
    
    for linkki in data2:
    
       kohde = collection2.find_one({"linkki": linkki}, {"_id": 0}) 
       print kohde
       data.append(kohde)
       #print str(kohde["osoite"])
    
    
    data = data[:]
    
    return data
   
def remove():
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    collection.remove()
    
    
#def import():
    
    
    
#def export():
    
