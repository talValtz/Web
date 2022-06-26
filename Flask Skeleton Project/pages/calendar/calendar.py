from flask import Blueprint, render_template

# main_menu blueprint definition
calendar = Blueprint('calendar', __name__, static_folder='static', static_url_path='/calendar', template_folder='templates')


# Routes
@calendar.route('/calendar')
def redirect_workouts():
     return render_template('calendar.html')
