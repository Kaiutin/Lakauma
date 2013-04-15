from pymongo import MongoClient

def hae_data():
    client = MongoClient()
    db = client.test
    collection = db.asunnot
    data = []
    for kohde in collection.find():
        data.append(kohde)
    return data
