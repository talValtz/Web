from flask import Blueprint, render_template

# main_menu blueprint definition
workouts = Blueprint('workouts', __name__, static_folder='static', static_url_path='/workouts', template_folder='templates')


# Routes
@workouts.route('/workouts')
def redirect_workouts():
     return render_template('workouts.html')
