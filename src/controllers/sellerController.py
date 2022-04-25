import simplejson as json

import src.connectDb as connectDb

db = connectDb.connect()
sellerCollection = db.saller

def index():
    response = []
    for seller in sellerCollection.find().sort("nome"):
        response.append({"name": seller['nome'], "cnpj": seller['cnpj']})
    
    return json.dumps(response)

def show(params):
    cnpj = params.get("cnpj")

    seller = sellerCollection.find_one({ "cnpj": cnpj })
    
    return json.dumps(seller, default=str)    

def create(request):
    seller = request.get_json()

    sellerCollection.insert_one(seller)

    return json.dumps({"status": "OK"})

def update(request):
    sellerUpdated = request.get_json()
    
    refreshSeller = {"$set": {"nome": sellerUpdated["nome"]}}

    sellerCollection.update_one({ "cnpj": sellerUpdated["cnpj"] }, refreshSeller)

    return json.dumps({"status": "OK"})
    
def delete(params):
    cnpj = params.get("cnpj")

    sellerCollection.delete_one({"cnpj": cnpj})

    return json.dumps({"status": "DELETED"})