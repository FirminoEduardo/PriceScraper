# Funções para interagir com o MongoDB
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Carregar variavéis de ambiente
load_dotenv()

# Configuração do mongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DATABASE_NAME")]

def save_product(data, collection_name="products"):
    """Salva um produto no MongoDB"""
    collection = db[collection_name]
    collection.insert_one(data)

def get_products(collection_name="products"):
    """Recupera todos os produtos"""
    collection = db[collection_name]
    return list(collection_name.find())