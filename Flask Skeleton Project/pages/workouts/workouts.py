from flask import Blueprint, render_template, session
from utilities.models.workoutsModel import workoutsModel

# main_menu blueprint definition
workouts = Blueprint('workouts', __name__, static_folder='static', static_url_path='/workouts',
                     template_folder='templates')


# Routes
@workouts.route('/workouts')
def redirect_workouts():
    print(session["user"])
    print("fffffff")
    cw = list(workoutsModel.ViewMyWorkouts(session["user"]))
    print(cw)
    return render_template('workouts.html', current_user=session["user"], workoutsCreated=cw)
