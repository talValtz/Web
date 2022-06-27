from flask import Blueprint, render_template

# main_menu blueprint definition
workoutDetails = Blueprint('workoutDetails', __name__, static_folder='static', static_url_path='/workoutDetails', template_folder='templates')

@workoutDetails.route('/workoutDetails')
def redirect_workoutDetails():
     return render_template('workoutDetails.html')
