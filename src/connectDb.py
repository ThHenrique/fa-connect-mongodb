from pymongo import MongoClient

def connect():
  db = MongoClient("mongodb+srv://root:1234@fa-starting-no-sql.6vnsq.mongodb.net/")
  return db['mercado-livre']

