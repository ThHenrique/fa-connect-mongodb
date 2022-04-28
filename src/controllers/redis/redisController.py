import src.connectRedis as connectRedis
import simplejson as json

cursor = connectRedis.connect()


def show():
  print(cursor)
  cursor.set('user:name', 'root')
      
  return json.dumps({"response": cursor.get("user:name")})   
