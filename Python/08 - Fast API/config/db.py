from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"

connection = MongoClient("mongodb://localhost:27017/")
db = connection.get_database("notesApp")
notes_collection = db.get_collection("notesApp")
