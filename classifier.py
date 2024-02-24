import cv2
import numpy
import matplotlib.pyplot
from keras import datasets, layers, models, preprocessing
# import scipy (needed for tensor flow)



# Returns a trained model for classification
def setup():
    
    # Get the training and testing data in a 0.75 training and 0.25 testing split
    (training_images, training_labels), (testing_images, testing_labels) = load_data_set("RecycleDataSet")
    
    # The labels
    class_labels = ['Non-Recyclable', 'Recyclable']
    
    # Start with an empty linear stack neural network model 
    keras_model = models.Sequential()
    
    # Adding layers and as well as transofmring spatial dimensions to one-dimensional vector 
    keras_model.add(layers.Conv2D(32, (3, 3), activation="relu"), input_shape=(64, 64, 3))
    keras_model.add(layers.MaxPooling2D((2, 2)))
    
    keras_model.add(layers.Conv2D(64, (3, 3), activation="relu"))
    keras_model.add(layers.MaxPooling2D((2, 2)))
    
    keras_model.add(layers.Conv2D(128, (3, 3), activation="relu"))
    keras_model.add(layers.MaxPooling2D((2, 2)))
    
    keras_model.add(layers.Flatten())
    keras_model.add(layers.Dense(128, activation="relu"))
    keras_model.add(layers.Dense(2, activation="softmax"))
    
    # Compile the model
    keras_model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
    
    
    

# REQUIRES: Must be a valid image and model
# Function for the flask app to classify an image with a given model 
def classify(model, img):
    pass


# Loads in the custom dataset that we have curated
def load_data_set(path):
    
    # Scales the pixel values of the images (preprocessing step) and establishes a 0.75 training and 0.25 testing split
    training_data_generator = preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.25)
    
    # Creates an augmented training data
    training_data = training_data_generator.flow_from_directory(
        path,
        target_size=(64, 64), # This would be the size of our pictures
        batch_size=16, # Small batch size due to small dataset (can be changed once have bigger dataset)
        class_mode="categorical",
        subset="training"
    )
    
    # Creates an augmented training data
    validation_data = training_data_generator.flow_from_directory(
        path,
        target_size=(64, 64), # This would be the size of our pictures
        batch_size=16, # Small batch size due to small dataset (can be changed once have bigger dataset)
        class_mode="categorical",
        subset="validation"
    )
    
    return next(training_data), next(validation_data)

    
    

