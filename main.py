from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app=Flask(__name__,template_folder='.')

db=SQLAlchemy(app)
app.config['SECRET_KEY'] = "blablabla"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///short.db'
