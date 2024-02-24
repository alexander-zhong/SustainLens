from flask import Flask, render_template, request 
from flask_uploads import UploadSet, configure_uploads, IMAGES

import classifier 


app = Flask(__name__)

#Configures for our image classifier
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photo = UploadSet('photos', IMAGES)
configure_uploads(app, photo)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/camera")
def camera():
    return render_template("camera.html")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if (request.method == "POST"):
        
        picture = request.files['picture']

        if not picture:
            return 'No picture has been uploaded'
        else:
            return 'picture has been uploaded'
    elif (request.method == "GET"):
        return render_template("upload.html")
    

