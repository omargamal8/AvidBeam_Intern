from pymongo import MongoClient

class Storage:
	def __init__(self):
		self._client = MongoClient()
		self._db = self._client.dim_db

		self._modules = self._db.modules
		self._media = self._db.media
		self._deploys = self._db.deploys

		self._mapper = {"comp_mod":self._modules, "media":self._media, "deploy":self._deploys}

	def insert_data(self, data, type):

			_db = self._mapper[type]
			print("trying to insert", data)
			_db.insert(data)


	def retrieve_data(self, type):
		
		returns = []
		_db = self._mapper[type]
		for item in _db.find():
			returns.append(item)
		return returns

	def delete(self, type, attr):
		_db = self._mapper[type]
		_db.delete_many(attr)