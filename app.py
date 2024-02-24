from flask import Flask, render_template, request 
from flask_uploads import UploadSet, configure_uploads, IMAGES

import classifier 
import cv2 


app = Flask(__name__)
camera = cv2.VideoCapture(0)

#Configures for our image classifier
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photo = UploadSet('photos', IMAGES)
configure_uploads(app, photo)

#returns the still frame of successful 
def capture_frame():
    success,frame = camera.read()
    if success:
        return frame
    else:
        return None  

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/camera")
def camera():
    capture_frame = capture_frame()
    return render_template("camera.html", capture_frame=capture_frame)

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
    

