import cv2
import numpy
import matplotlib.pyplot
from keras import datasets, layers, models, preprocessing
# import scipy (needed for tensor flow)



# Returns a trained model for classification
def setup():
    (training_images, training_labels), (testing_images, testing_labels) = load_data_set("RecycleDataSet")
    print(training_images)
    

# REQUIRES: Must be a valid image and model
# Function for the flask app to classify an image with a given model 
def classify(model, img):
    pass


# Loads in the custom dataset that we have curated
def load_data_set(path):
    
    # Scales the pixel values of the images (preprocessing step) and establishes a 0.70 training and 0.30 testing split
    training_data_generator = preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.3)
    
    # Creates an augmented data
    training_data = training_data_generator.flow_from_directory(
        path,
        target_size=(64, 64), # This would be the size of our pictures
        batch_size=16, # Small batch size due to small dataset (can be changed once have bigger dataset)
        class_mode="categorical",
        subset="training"
    )
    
    validation_data = training_data_generator.flow_from_directory(
        path,
        target_size=(64, 64), # This would be the size of our pictures
        batch_size=16, # Small batch size due to small dataset (can be changed once have bigger dataset)
        class_mode="categorical",
        subset="validation"
    )
    
    return next(training_data), next(validation_data)

    
    

setup()