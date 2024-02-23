from flask import Flask, render_template

import classifier 


# Pre-Trains the model before running the flask app to prevent delays in user experience
@app.before_first_request
def before_first_request():
    model = classifier.setup()
    
    
    