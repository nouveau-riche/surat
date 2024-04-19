from pymongo import MongoClient
from pymongo.server_api import ServerApi


MONGO_DATABASE_URL = 'mongodb+srv://nikunjsha02:Je8nA955Uq0DDu5w@cluster0.dsdjp4o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

client = MongoClient(MONGO_DATABASE_URL,server_api=ServerApi('1'))
db = client['surat_database']  

events_collection = db['events']
news_collection = db['news']
offer_collection = db['offers']
user_collection = db['users']





    