from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/',methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("login.html")
    user = request.form.get("username")
    return render_template("rgba.html",saysomething=user)
    #return ('Hello world! Hello %s !' % user)
