from pymongo import MongoClient
import uuid

mongo_client = MongoClient("{Your URI Here}")

database_input = input("Database: ")

db = mongo_client[database_input]

collection_input = input("Collection: ")

collection = db[collection_input]

test = int(input("How many times should we enter random indexes: "))

for item in collection.find():
  collection.delete_one(item)

for i in range(test):
  collection.insert_one({
    "good_fight": uuid.uuid4(),
    "etb": uuid.uuid4()
  }
)

print("Finished ETB'ing shit")
