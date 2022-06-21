from datetime import date
import src.connectCassandra as connectCassandra
import json
import uuid

ASTRA_DB_KEYSPACE = 'mercadolivre'
ASTRA_DB_TABLE = "voucher"

cursor = connectCassandra.connect()

def show():
  selectAll = cursor.search_table(keyspace=ASTRA_DB_KEYSPACE, table=ASTRA_DB_TABLE, query={})
  print(selectAll)

  return json.dumps({"hasError": False, "Message": "Deu bom"})
