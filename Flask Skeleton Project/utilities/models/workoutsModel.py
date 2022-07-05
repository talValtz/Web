from utilities.db.db_manager import dbManager
from utilities.db.db_manager import dbManager

class workoutsModel:
	def __init__(self):
		pass


	def ViewMyWorkouts(self,userName):
		query = "SELECT Workout_type,workout_date,workout_time FROM training WHERE  workout_date>= DATE(NOW()) AND user_host=%s"
		return dbManager.fetch(query, (userName,))

workoutsModel = workoutsModel()




