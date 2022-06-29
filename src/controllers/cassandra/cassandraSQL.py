from datetime import date
import src.connectCassandra as connectCassandra
import json

cursor = connectCassandra.connect()

def create(voucher_dumps): 
  voucher = json.loads(voucher_dumps)

  cursor.execute(
    """
    INSERT INTO mercadolivre.voucher (title, clause, description, discount_percent, in_operation) 
    VALUES (%s, %s, %s, %s, %s)
    """,
    (voucher["title"], voucher["clause"], voucher["description"], voucher["discount_percent"], voucher["in_operation"])
  )

  return

def index():
  rows = cursor.execute("SELECT * FROM mercadolivre.voucher")
  if(not rows):
    return json.dumps({"status":"error"})
  
  voucher_list = []
  for voucher in rows:
    voucher_list.append(
      {
        "title": voucher.title,
        "clause": voucher.clause,
        "description": voucher.description,
        "discount_percent": voucher.discount_percent,
        "in_operation": voucher.in_operation
      }
    )

  return json.dumps({
    "cupoms": voucher_list
  })

def update(voucher_dumps):
  voucher = json.loads(voucher_dumps)

  cursor.execute(
    """
    UPDATE mercadolivre.voucher 
    SET clause=%s,
    description=%s,
    discount_percent=%s,
    in_operation=%s
    WHERE title=%s IF EXISTS;  
    """, 
    (voucher["clause"], voucher["description"], voucher["discount_percent"], voucher["in_operation"], voucher["title"])
  )

  return

def delete(voucher_title):
  query = f"DELETE FROM mercadolivre.voucher WHERE title='{voucher_title}' IF EXISTS;"
  cursor.execute(query)

  return

