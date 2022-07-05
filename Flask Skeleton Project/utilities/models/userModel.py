from utilities.db.db_manager import dbManager


class userModel:
	def __init__(self):
		pass

	def Login(self, userName, password):
		query = "SELECT User_name FROM users WHERE User_name=%s AND password=%s"
		return dbManager.fetch(query, (userName, password,))

	def LoginCheckExist(self, userName):
		query="SELECT User_name FROM users WHERE User_name=%s"
		return dbManager.fetch(query, (userName,))


userModel = userModel()
