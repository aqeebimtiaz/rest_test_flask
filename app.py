from flask import Flask
# , request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/rest_test_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)


@app.route("/")
def hello():
    print(db)
    return "Hello World!"

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(debug=True)
