from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES

import classifier 
import cv2 
import numpy
import base64

app = Flask(__name__)

#Configures for our image classifier
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photo = UploadSet('photos', IMAGES)
configure_uploads(app, photo)

@app.route("/")
def index():
    return redirect("/upload")

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if (request.method == "POST"):
        picture = request.files["picture"]
        
        # Check if valid image file
        allowed_extensions = {"png", "jpg", "jpeg"}
        if not picture or ("." in picture.filename and not picture.filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            return redirect("/error")
        else:
            # Read image data turns it into image array 
            img_data = picture.read()
            
            # encoded img for returning back to the template
            img_encoded = base64.b64encode(img_data)
            
            # image array for classifier
            img_array = numpy.frombuffer(img_data, numpy.uint8)
            
            # Decode the image array
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            
            
            
            result = classifier.classify(img)
            return render_template("upload.html", found=True, result=result, picture=img_encoded)
    elif (request.method == "GET"):
        return render_template("upload.html", found=False, result=None, picture=None)
    
@app.route("/error")
def error():
    return render_template("error.html")


    

