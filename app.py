from flask import Flask
from flask import render_template, redirect, url_for, session, request
import utils
import yelp
import hopstopScraper
app = Flask(__name__)
app.secret_key = "SUBMIT!"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.form.get("password_register","")==request.form.get("confirmpassword_register",""):
            #createUser will return a number depending on what the error was
        result=utils.createUser(request.form.get("username_register","").lower(),request.form.get("password_register",""))
            #success. Login page will have confirmation message
        if result==0:
            return render_template("home.html",type_register=0)
            #username is already taken
        elif result==1:
            return render_template("home.html",type_register=1)
            #username or pw is invalid
        else: 
            return render_template("home.html",type_register=2)
        #pw mismatch
    else:
        return render_template("home.html",type_register=3)
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=="POST":
        result = utils.authorize(str(request.form.get("username_login","")).lower(), str(request.form.get("password_login","")))
        #successful login
        if result == 0:  
            session["username"] = request.form.get("username_login","")
            return redirect("/route")
        #failed attempt!
        else:
            return render_template("home.html",type_login=1)
    else:
        return render_template("home.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/")

@app.route("/route",methods=["GET","POST"])
def route():
    if request.method=="POST":
        print("1")
        start = request.form.get("start","")
        end = request.form.get("end","")
        print(start)
        print(end)
        #fields were left blank
        if start == None or end == None:
            return render_template("route.html", error=1)
        stationList = hopstopScraper.getRoutes(start, end)
        results = []
        stations= []
        for station in stationList:
            print station
            try: 
                yelplist = yelp.search("food",station)
                results.append(yelplist)
                stations.append(station)
            except KeyError:
                print "Yelp did not find any matches for this station"
            
        print results
        session["stations"]= stations
        session["results"] = results
        return redirect("results")
    else:
        return render_template("route.html")

@app.route("/results")
def results():
    if "results" not in session:
        return redirect("route")
    else:
        
        return render_template("results.html", results=session["results"], stations=session["stations"])

if __name__ == "__main__":
    app.run(debug = True)
