from flask import  Blueprint, request, jsonify 
from backend.models.fraud_model import predict_fraud 
fraud_routes = Blueprint("fraud_routes", __name__) 
@fraud_routes.route("/predict_fraud",methods=["post"])
def predict_fraud_endpoints():
    data=request.json 
    result=predict_fraud(data)
    return jsonify(result)