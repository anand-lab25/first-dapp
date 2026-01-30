from flask import Flask 
from routes import price_routes, fraud_routes
app = Flask(__name__)
app.register_blueprint(fraud_routes)
app.register_blueprint(price_routes)
if __name__ = "__main__":
    app.run(debug=True)
    