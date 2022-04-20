import simplejson as json

import src.connectDb as connectDb

db = connectDb.connect()
userCollection = db.user

def index():
    response = []
    for x in userCollection.find().sort("nome"):
        response.append({"name": x['nome'], "email": x['email']})
    
    return json.dumps(response)

def show(params):
    nome = params.get("nome")

    user = userCollection.find_one({ "nome": nome })
    
    return json.dumps(user, default=str)    

def create(request):
    user = request.get_json()

    userCollection.insert_one(user)

    return json.dumps({"status": "OK"})

def update(request):
    userUpdated = request.get_json()
    
    refreshUser = {"$set": {"nome": userUpdated["nome"], "email": userUpdated["email"]}}

    userCollection.update_one({ "cpf": userUpdated["cpf"] }, refreshUser)

    return json.dumps({"status": "OK"})
    
def delete(params):
    cpf = params.get("cpf")

    userCollection.delete_one({"cpf": cpf})

    return json.dumps({"status": "DELETED"})