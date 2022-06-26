from flask import Blueprint, render_template

# main_menu blueprint definition
search = Blueprint('search', __name__, static_folder='static', static_url_path='/search', template_folder='templates')

# Routes



@search.route('/search')
def redirect_search():
     return render_template('search.html')
