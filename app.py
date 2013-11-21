from flask import Flask
from flask import render_template, redirect, url_for, session, request

app = Flask(__name__)
app.secret_key = "SUBMIT!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="POST":
        if request.form["password"]==request.form["password2"]:
            #createUser will return a number depending on what the error was
            result=utils.createUser(request.form("username"),request.form("password"))
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
    if request.method == "POST":
        result = app.authorize(str(request.form["username"]), str(request.form["password"]))
        #successful login
        if result == 0:  
            session["username"] = request.form["username"]
            returnredirect("/?type=2")
        #fail fail fail!
        else:
            return render_template("login.html",type=1)
    else:
        return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect("/?type=2")
                
                


if __name__ == "__main__":
    app.run(debug = True)
