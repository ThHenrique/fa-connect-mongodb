from pymongo import MongoClient

def connect():
  db = MongoClient("mongodb+srv://<user>:<password>@fa-starting-no-sql.6vnsq.mongodb.net/")
  return db['mercado-livre']

