from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# get Astra connection information from environment variables
ASTRA_CLIENT_ID = "<CLIENT_ID>"
ASTRA_CLIENT_SECRETY = "<CLIENT_SECRETY>"

def connect():
  cloud_config= {'secure_connect_bundle': './secure-connect-fatec.zip'}
  auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRETY)
  cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
  session = cluster.connect()

  row = session.execute("select release_version from system.local").one()
  if row:
      print(row[0])
  else:
      print("An error occurred.")
  return session