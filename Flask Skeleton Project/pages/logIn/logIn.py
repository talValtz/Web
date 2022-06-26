from flask import Blueprint, render_template

# main_menu blueprint definition
logIn = Blueprint('logIn', __name__, static_folder='static', static_url_path='/logIn', template_folder='templates')

@logIn.route('/logIn')
def redirect_homepage():
     return render_template('logIn.html')
