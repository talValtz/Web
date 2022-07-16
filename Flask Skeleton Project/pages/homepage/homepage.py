from flask import Blueprint, render_template, redirect, url_for
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

# main_menu blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage',
                     template_folder='templates')
GoogleMaps(homepage,key="my-key")



# Routes


@homepage.route('/home')
def index():
    return render_template('homepage.html')


@homepage.route('/homepage')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
