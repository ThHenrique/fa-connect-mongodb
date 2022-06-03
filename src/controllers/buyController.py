import simplejson as json

from bson.objectid import ObjectId

import src.connectDb as connectDb
import src.controllers.redis.voucherController as voucherController

db = connectDb.connect()
buyCollection = db.buy

def show(params):
    id = params.get("id")
    
    buy = buyCollection.find_one({ "_id": ObjectId(id) })
    
    return json.dumps(buy, default=str)    

def create(request):
    buy = request.get_json()

    if (buy["voucher"]):
        voucher = voucherController.findVoucher(buy["voucher"])

        if (voucher):
            discount_percent = voucher['discount_percent']
        
            buy["discount_total"] = (discount_percent / 100) * buy["total"]        

            buy["total"]  = buy["total"] - buy["discount_total"]
            buy["total_a_prazo"]  = buy["total_a_prazo"] - buy["discount_total"]
            buy["total_a_vista"]  = buy["total_a_vista"] - buy["discount_total"]

    buyCollection.insert_one(buy)

    return json.dumps({"status": "OK"})
    
def delete(params):
    id = params.get("id")

    request = buyCollection.delete_one({"_id": ObjectId(id)})
    print(request.deleted_count)
    return json.dumps({"status": "DELETED"})