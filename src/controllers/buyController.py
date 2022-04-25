import simplejson as json

from bson.objectid import ObjectId

import src.connectDb as connectDb

db = connectDb.connect()
buyCollection = db.buy

def show(params):
    id = params.get("id")
    
    buy = buyCollection.find_one({ "_id": ObjectId(id) })
    
    return json.dumps(buy, default=str)    

def create(request):
    buy = request.get_json()

    buyCollection.insert_one(buy)

    return json.dumps({"status": "OK"})
    
def delete(params):
    id = params.get("id")

    request = buyCollection.delete_one({"_id": ObjectId(id)})
    print(request.deleted_count)
    return json.dumps({"status": "DELETED"})