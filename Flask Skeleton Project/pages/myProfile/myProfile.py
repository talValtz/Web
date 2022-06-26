from flask import Blueprint, render_template

# main_menu blueprint definition
myProfile = Blueprint('myProfile', __name__, static_folder='static', static_url_path='/myProfile', template_folder='templates')


# Routes
@myProfile.route('/myProfile')
def redirect_myProfile():
     return render_template('myProfile.html')
