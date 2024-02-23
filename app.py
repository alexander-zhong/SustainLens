from flask import Flask, render_template, request 
from flask_uploads import UploadSet, configure_uploads, IMAGES

import classifier 


app = Flask(__name__)

#Configures for our image classifier
photo = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
configure_uploads(app, photo)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/camera")
def camera():
    return render_template("camera.html")

@app.route("/picture")
def picture():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photo.save(request.files['photo'])
    return render_template("picture.html")


