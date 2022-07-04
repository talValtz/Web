from flask import Blueprint, render_template,session

# main_menu blueprint definition
workouts = Blueprint('workouts', __name__, static_folder='static', static_url_path='/workouts', template_folder='templates')


# Routes
@workouts.route('/workouts')
def redirect_workouts():
     if session["user"]:
          createdworkout=list()
     return render_template('workouts.html')
