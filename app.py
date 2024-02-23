from flask import Flask, render_template

import classifier 


# Pre-Trains the model before running the flask app to prevent delays in user experience
@app.before_first_request
def before_first_request():
    model = classifier.setup()
    
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/camera")
def camera():
    return render_template("camera.html")

@app.route("/picture")
def picture():
    return render_template("picture.html")