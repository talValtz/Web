from flask import Blueprint, render_template,session
from utilities.models.workoutsModel import workoutsModel
# main_menu blueprint definition
workoutDetails = Blueprint('workoutDetails', __name__, static_folder='static', static_url_path='/workoutDetails', template_folder='templates')

#@workoutDetails.route('/workoutDetails')
#def redirect_workoutDetails():
 #    return render_template('workoutDetails.html')

@workoutDetails.route('/workoutDetails')
def index():
    print(session["user"])
    print(session['workoutID'])
    workout=list(workoutsModel.ViewWorkoutDetails(session['workoutID']))
    participants=list(workoutsModel.ViewParticipant(session['workoutID']))
    print(workout)
    print(participants)
    return render_template('workoutDetails.html',workout=workout[0],current_user=session["user"],participants=participants)
