from datetime import date
import src.connectRedis as connectRedis
import json

cursor = connectRedis.connect()
  
def create(request):
    body = request.get_json()

    title = body["title"]
    discount_percent = body["discount_percent"]
    in_operation = body["in_operation"]
    description = body["description"]
    expiration = body["expiration-in-seconds"]
    clauses  = body["clauses"]

    ticket_value = json.dumps(
      {
        "title": title,
        "discount_percent": discount_percent,
        "in_operation": in_operation,
        "description": description,
        "clauses": clauses
      }
    )

    try:
      cursor.set(f'ticket:{title}', ticket_value)
      cursor.expire(f'ticket:{title}', expiration)

      return json.dumps({"status": "ok"})
    except: 
      return json.dumps({"status": "error"})

def show(params):
  ticket_title = params.get("ticket-name")  
  
  try:
    ticket = json.loads(cursor.get(f'ticket:{ticket_title}'))
    return json.dumps(ticket)   
  except:
    return json.dumps({"hasError": True, "Message": "Nenhum item encontrado"})

def update(request):
  ticket_title = request.args.get("ticket-name")
  body = request.get_json()

  exists_ticket = cursor.exists(f'ticket:{ticket_title}')

  if (exists_ticket != 0):    
    discount_percent = body["discount_percent"]
    in_operation = body["in_operation"]
    description = body["description"]
    expiration = body["expiration-in-seconds"]
    clauses  = body["clauses"]

    ticket_value = json.dumps(
      {
        "title": ticket_title,
        "discount_percent": discount_percent,
        "in_operation": in_operation,
        "description": description,
        "clauses": clauses
      }
    )
    try:
      cursor.set(f'ticket:{ticket_title}', ticket_value)

      # date_expiration = date.strftime(expiration, '%d/%m/%Y %H:%M') 
      # print(date_expiration)
      
      cursor.expire(f'ticket:{ticket_title}', expiration)
      return json.dumps({"status": "ok"})
    except: 
      return json.dumps({"status": "error"})

def delete(params):
  ticket_title = params.get("ticket-name")  

  exists_ticket = cursor.exists(f'ticket:{ticket_title}')

  if (exists_ticket != 0):        
    try:
      cursor.delete(f'ticket:{ticket_title}')

      return json.dumps({"status": "ok"})  
    except:
      return json.dumps({"hasError": True, "Message": "Nenhum item encontrado"})