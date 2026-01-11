from flask import Flask
from database.db import db
from routes.auth import auth_bp

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(auth_bp)
db.init_app(app)
@app.route('/')
def home():
    return{'message': "REST API Backend Running"}

if __name__ == '__main__':
    app.run(debug=True)