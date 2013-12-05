from flask import Flask
from flask import render_template, redirect, url_for, session, request
import utils
app = Flask(__name__)
app.secret_key = "SUBMIT!"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="POST":
        if request.form["password"]==request.form["password2"]:
            #createUser will return a number depending on what the error was
            result=utils.createUser(request.form["username"].lower(),request.form["password"])
            #success. Login page will have confirmation message
            if result==0:
                return redirect("/login?type=2")
            #username is already taken
            elif result==1:
                return render_template("register.html",type=1)
            #username or pw is invalid
            else:
                return render_template("register.html",type=2)
        #pw mismatch
        else:
            return render_template("register.html",type=3)
    else:
        return render_template("register.html")
@app.route("/login")
def login():
    if request.method=="POST":
        print("done")
        result = utils.authorize(str(request.form["username"]).lower(), str(request.form["password"]))
        #successful login
        if result == 0:  
            session["username"] = request.form["username"]
            return redirect("/?type=2")
        #failed attempt!
        else:
            return render_template("login.html",type=1)
    else:
        if request.args.get("type") == "2":
            return render_template("login.html",type=2)
        return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/?type=2")

@app.route("/route")
def route():
    if request.method=="POST":
        start = request.form["start"]
        end = request.form["end"]
        #fields were left blank
        if start == None or end == None:
            return render_template("route.html", error=1)
        stationList = hopstopScraper.getRoutes(start, end)
        results = yelpAPI.process(stationList)
        return redirect("/results")
    else:
        return render_template("route.html")



if __name__ == "__main__":
    app.run(debug = True)
