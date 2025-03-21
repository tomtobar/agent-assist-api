import os
from pinecone import Pinecone
from openai import OpenAI
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

CORS(app, supports_credentials=True, resources={r"/*": {"origins": "chrome-extension://lpgdmjmiijnegknjnjkfjnpobllopnin"}})

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

api = Api(app)

from models import User, ZendeskTicket, Prompt, SuggestedSolution

openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
pinecone_client = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
