from utilities.db.db_manager import dbManager
from utilities.db.db_manager import dbManager

class workoutsModel:
	def __init__(self):
		pass


#	def ViewMyWorkouts(self,userName):
#		query = "SELECT rides.ID AS ID, rides.DepartureTime AS DepartureTime, rides.Origin AS Origin, rides.Destination AS Destination, rides.Seats AS Seats, rides.Price AS Price, rides.Pets AS Pets, rides.Mask AS Mask, rides.Smoking AS Smoking, rides.Comment AS Comment, Driver.Name AS DriverName, rides.Status AS Status, rides.DriverID AS DriverID FROM rides, users As Driver WHERE Driver.ID=rides.DriverID AND rides.DriverID=%s"
#		return dbManager.fetch(query, (driverID,))


workoutsModel = workoutsModel()




