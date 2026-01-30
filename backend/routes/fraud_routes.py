from flask import  Blueprint, request, jsonify 
from models.fraudmodel import predict_fraud 
fraud_routes = Blueprint("fraud_routes", __name__) 
@fraud_routes.route("/predict_fraud",method="post ")
def predict_fraud_endpoints():
    data=request.json 
    result=predict_fraud(data)
    return jsonify(result)