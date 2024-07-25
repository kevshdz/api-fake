from src.models.model import *
from src.schemas import *
from flask import jsonify

def get_products_list():
    try:
        products = Producto.query.all()
        if products:
            result = products_schema.dump(products)
            return jsonify({"success":True, "message":"Product found","data":result})
        else:
            return {"success":False,"message":"Products not found"}
    except Exception as ex:
        return ex