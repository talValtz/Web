from flask import Blueprint, render_template,request,session,redirect,url_for
from utilities.models.userModel import userModel
# main_menu blueprint definition
logIn = Blueprint('logIn', __name__, static_folder='static', static_url_path='/logIn', template_folder='templates')




@logIn.route('/signIn')
def redirect_signIn():
    return render_template('logIn.html')

@logIn.route("/login", methods=["POST"])
def login():
    print("ddd")
    useName = request.form["username"]
    password = request.form["psw"]
    result = userModel.Login(useName, password)
    print(useName)
    print(password)
    print(result[0][0])
    session["user"]="tt"
   # print(len(result))
  #  if len(result)==0:
   #     return render_template("homepage.html", msg="Invalid, try again", current_user=session["user"] if "user" in session else None)
    session["user"] = result[0][0] #result[0][0] means first record and first column that is ID attribute
    return redirect(url_for('homepage.index'))

