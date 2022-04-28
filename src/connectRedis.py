import redis

def connect():
  db = redis.Redis(
    host='<host>',
    port="<port-number>",
    password='<password>'
  )

  return db



