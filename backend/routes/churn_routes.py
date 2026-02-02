# routes/chur_routes.py 
from flask import Blueprint,jsonify,request
import joblib
import pandas as pd 

#load models + feature order 
model, features = joblib.load("backend/models/churn_model.pkl")
# Create blueprint 
churn_bp= Blueprint("churn",__name__ )
@churn_bp.route("/predict_churn",method=['post'])
def predict_churn:
    try:
        data=request.json
        X=pd.DataFrame([data], columns=features)
        prob=model.predict_proba(X)[0,1]
        return jsonify({"churn_probability":prob})
    except Exception as e:
        return jsonify({"error":str(e)}), 400
