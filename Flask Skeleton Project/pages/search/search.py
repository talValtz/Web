from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.models.workoutsModel import workoutsModel
from utilities.models.participantsModel import participantsModel
from utilities.models.userModel import userModel
from datetime import timedelta

# main_menu blueprint definition
search = Blueprint('search',__name__, static_folder='static', static_url_path='/search', template_folder='templates')


# Routes

@search.route('/search', methods=["GET"])
def search_page():
   answer = False
   return render_template('search.html',answer= answer)

@search.route("/search_all", methods=["GET", "POST"])
def search_workout():
    if request.method == "POST":
        type = request.form["PickTrainType"]
        date = request.form["PickDate"]
        time_from = request.form["PickTimeRange1"]
        time_to = request.form["PickTimeRange2"]
        result = list(workoutsModel.list_Workouts_by_inputs(type, date, time_from, time_to))
        if len(result) == 0:
            answer = False
            return render_template('/search.html', answer=answer)
        answer = True
        return render_template('/search.html', workouts=result, answer=answer)
    answer = False
    return render_template('/search.html', answer=answer)

