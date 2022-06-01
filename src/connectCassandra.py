from astrapy.collections import create_client, AstraCollection

# get Astra connection information from environment variables
ASTRA_DB_ID = '<BD-ID>'
ASTRA_DB_REGION = '<DB-REGION>'
ASTRA_DB_APPLICATION_TOKEN = '<token>'
ASTRA_DB_KEYSPACE = 'mercadolivre'
TEST_COLLECTION_NAME = "test"

def connect():
  # setup an Astra Client and create a shortcut to our test colllection
  astra_client = create_client(
    astra_database_id=ASTRA_DB_ID,
    astra_database_region=ASTRA_DB_REGION,
    astra_application_token=ASTRA_DB_APPLICATION_TOKEN
  )

  return astra_client.namespace(ASTRA_DB_KEYSPACE).collection(TEST_COLLECTION_NAME)
