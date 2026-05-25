from flask import Flask,jsonify
from flask_cors import CORS
from backend.routes.fraud_routes import  fraud_routes
from backend.routes.price_routes  import price_routes
from backend.routes.churn_routes import churn_bp
app = Flask(__name__)
app.register_blueprint(fraud_routes)
app.register_blueprint(price_routes)
app.register_blueprint(churn_bp)
CORS(app)
@app.route("/")
def welcome():
    return  jsonify({"message":"welcome home guest."})
@app.route("/hello") 
def hello():
    return jsonify({"message":"hello user ur smart"})
if __name__ == "__main__":
    app.run(debug=True)