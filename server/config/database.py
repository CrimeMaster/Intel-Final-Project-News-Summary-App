import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = "mongodb+srv://admin:test1234!@cluster0.szfvkcc.mongodb.net/?appName=Cluster0"

client = MongoClient(mongo_uri)

db = client.NewsList

collection_name = db["news"]
