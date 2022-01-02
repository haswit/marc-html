from flask import *



app = Flask(__name__)
app.config["TEMPLATE_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "sd4631s6d5f4s"



@app.route("/")
def index():
    if not "user" in session:
        return render_template("index.html", page = "Dashboard")
    else:
        return redirect("/sign-in")
    
@app.route("/register")
def register():
    if not "user" in session:
        return render_template("register.html", page = "Register")
    else:
        return redirect("/sign-in")


if __name__ == "__main__":
    app.run(debug=True)
