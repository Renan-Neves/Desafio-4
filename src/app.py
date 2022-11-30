from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
import rotas
import bd

if __name__ == "__main__":
  app.run(debug=True)