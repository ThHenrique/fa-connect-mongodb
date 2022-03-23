from pymongo import MongoClient

def connect():
  client = MongoClient("mongodb+srv://<user>:<password>@<url>")
  mydb = client['mercado-livre']

  return mydb
