from utilities.db.db_manager import dbManager
from utilities.db.db_manager import dbManager

class workoutsModel:
	def __init__(self):
		pass


	def ViewMyWorkouts(self,userName):
		query = "SELECT Workout_type,workout_date,workout_time,trainingID FROM training WHERE  workout_date>= DATE(NOW()) AND user_host=%s"
		return dbManager.fetch(query, (userName,))

	def ViewWorkoutDetails(self,trainingID):
		query = "SELECT * FROM training WHERE trainingID=%s"
		return dbManager.fetch(query, (trainingID,))

	def ViewParticipant(self,trainingID):
		query = "SELECT * FROM participant as p inner join users as u on p.participant=u.User_name WHERE p.training=%s"
		return dbManager.fetch(query, (trainingID,))

	def ViewCallendar(self,userName):
		query = "SELECT * FROM participant as p inner join training as t on p.training=t.trainingID WHERE p.participant=%s"
		return dbManager.fetch(query, (userName,))



workoutsModel = workoutsModel()




