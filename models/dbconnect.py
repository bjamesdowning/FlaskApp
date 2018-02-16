
import pymongo


client = pymongo.MongoClient()
database = client["testdb"]
collection = database["testcollection"]
print('connect')

def mongo_insert(name,student):
	
