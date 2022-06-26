from flask import Blueprint, render_template

# main_menu blueprint definition
newWorkout = Blueprint('newWorkout', __name__, static_folder='static', static_url_path='/newWorkout', template_folder='templates')


# Routes
@newWorkout.route('/newWorkout')
def redirect_workouts():
     return render_template('newWorkout.html')
