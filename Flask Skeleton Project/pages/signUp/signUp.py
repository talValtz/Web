from flask import Blueprint, render_template

# main_menu blueprint definition
signUp = Blueprint('signUp', __name__, static_folder='static', static_url_path='/signUp', template_folder='templates')

@signUp.route('/signUp')
def redirect_signUp():
     return render_template('signUp.html')
