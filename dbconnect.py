import pymongo

class Database:
	
	
	def initialize(self):
		self.client = pymongo.MongoClient()
		self.db = self.client['testdb']
		self.collection = self.db['testcollection']
		print('Connected')
	
	
	def insert(self, key, value):
		data = {key:value}
		self.collection.insert(data)
		#print('Added', data, 'to mongo')

	def find(self):
		return [post for post in self.collection.find()]

	def find_one(self):
		return self.collection.find_one()
