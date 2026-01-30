from flask  import Blueprint, jsonify, request
from models.fraudmodel import predict_fraud 
price_routes = Blueprint("price_routes",__name__)
@price_routes.route("/predict_price", methods=["post"])
def predict_price_endpoint():
    data=request.json 
    result=predict_price(data)
    return jsonify(result)