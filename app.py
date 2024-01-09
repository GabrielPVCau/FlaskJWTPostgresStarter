from flask import Flask
from flask_jwt_extended import JWTManager
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = environ.get('SECRET_KEY')

jwt = JWTManager(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
