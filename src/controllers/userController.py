from flask import jsonify
import simplejson as json

import src.connectDb as connectDb

def findSort():
    #Sort
    mydb = connectDb.connect()
    mycol = mydb.usuario
    mydoc = mycol.find().sort("nome")

    response = []
    for x in mydoc:
        response.append({"name": x['nome'], "cpf": x['cpf']})

    return json.dumps(response)

def findQuery():
    #Query
    mydb = connectDb.connect()
    mycol = mydb.usuario
    myquery = { "nome": "Diego Silva" }   
    mydoc = mycol.find(myquery)

    response = []
    for x in mydoc:
        response.append({"name": x['nome'], "cpf": x['cpf']})

    return json.dumps(response)
    

def insert(request):
    user = request.get_json()
    # user = json_data["user"]
    #Insert
    mydb = connectDb.connect()
    mycol = mydb.usuario

    mycol.insert_one(user)
    return json.dumps({"status": "OK"})
    
def delete(request):
    user = request.get_json()
    #delete
    mydb = connectDb.connect()
    mycol = mydb.usuario
    print("\n####DELETE####")
    mycol.delete_one(user)
    return json.dumps({"status": "DELETED"})