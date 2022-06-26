from flask import Blueprint, render_template

# main_menu blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')

# Routes


@homepage.route('/')
def index():
    return render_template('homepage.html')

@homepage.route('/homepage')
def redirect_homepage():
     return render_template('homepage.html')
