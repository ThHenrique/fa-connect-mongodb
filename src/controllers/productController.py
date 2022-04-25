import simplejson as json

from bson.objectid import ObjectId

import src.connectDb as connectDb


db = connectDb.connect()
productCollection = db.product

def index():
    response = []
    for product in productCollection.find().sort("price"):
        response.append({"name": product['name'], "price": product['price'], "total": product['total']})
    
    return json.dumps(response)

def show(params):
    name = params.get("name")

    product = productCollection.find_one({ "name": name })
    
    return json.dumps(product, default=str)    

def create(request):
    product = request.get_json()

    productCollection.insert_one(product)

    return json.dumps({"status": "OK"})

def update(request):
    productUpdated = request.get_json()
    
    refreshProduct = {"$set": {"name": productUpdated["name"], "price": productUpdated["price"], "total": productUpdated["total"]}}

    productCollection.update_one({ "_id": ObjectId(productUpdated["id"]) }, refreshProduct)

    return json.dumps({"status": "OK"})
    
def delete(params):
    id = params.get("id")

    productCollection.delete_one({"_id": ObjectId(id)})

    return json.dumps({"status": "DELETED"})