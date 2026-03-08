from flask import Flask 
from backend.routes.fraud_routes import  fraud_routes
from backend.routes.price_routes  import price_routes
from backend.routes.churn_routes import churn_bp
app = Flask(__name__)
app.register_blueprint(fraud_routes)
app.register_blueprint(price_routes)
app.register_blueprint(churn_bp)
@app.route("/")
def welcome():
    return "welcome home guest."
if __name__ == "__main__":
    app.run(debug=True)
    