import cv2
import numpy
import matplotlib.pyplot
from keras import datasets, layers, models, preprocessing, applications, callbacks



# PLEASE only run this file for creating a new model, the saved model is already in the directory


# Returns a trained model for classification
def setup():
    
    # Get the training and testing data in a 0.70 training and 0.30 testing split
    (training_images, training_labels), (testing_images, testing_labels) = load_data_set("RecycleDataSet")
    
    # The labels
    class_labels = ['Non-Recyclable', 'Recyclable']
    
    # Start with an empty linear stack neural network model 
    keras_model = models.Sequential()
    
    # Adding layers and as well as transofmring spatial dimensions to one-dimensional vector 
    keras_model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(256, 256, 3)))
    keras_model.add(layers.MaxPooling2D((2, 2)))
    
    keras_model.add(layers.Conv2D(32, (3, 3), activation="relu"))
    keras_model.add(layers.MaxPooling2D((2, 2)))
    
    keras_model.add(layers.Conv2D(64, (5, 5), activation="relu"))
    keras_model.add(layers.MaxPooling2D((2, 2)))
    
    keras_model.add(layers.Dropout(0.5))
    
    keras_model.add(layers.Flatten())
    keras_model.add(layers.Dense(64, activation="relu"))
    keras_model.add(layers.Dense(2, activation="softmax"))
    
    # Compile the model
    keras_model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
    
    early_stop = callbacks.EarlyStopping(monitor='val_loss', patience=1)
    
    # Fits and evaluates the performance 
    keras_model.fit(training_images, training_labels, epochs=7, validation_data=(testing_images, testing_labels), callbacks=[early_stop])
    print(keras_model.evaluate(testing_images, testing_labels))
    
    # Saves the model as a file
    keras_model.save("recyclable_model.keras")
    
    
    
    
    

# REQUIRES: Must be a valid image and model
# Function for the flask app to classify an image with a given model 
def classify(img):
    keras_model = models.load_model('recyclable_model.keras')

    # Preprocessing 
    img = cv2.resize(img, (256, 256)) 
    img_data = preprocessing.image.img_to_array(img)
    img_data = numpy.expand_dims(img_data, axis = 0)
    
    img_data = applications.resnet50.preprocess_input(img_data / 255)
    prediction = keras_model.predict(img_data)
    
    # The labels
    class_labels = ['Non-Recyclable', 'Recyclable']
    
    result = numpy.argmax(prediction)
    result = class_labels[result]
    
    return result


# Loads in the custom dataset that we have curated
def load_data_set(path):
    
    # Scales the pixel values of the images (preprocessing step) and establishes a 0.80 training and 0.20 testing split
    training_data_generator = preprocessing.image.ImageDataGenerator(rescale=1./255, validation_split=0.20)
    
    # Creates an augmented training data
    training_data = training_data_generator.flow_from_directory(
        path,
        target_size=(256, 256), # This would be the size of our pictures
        batch_size=6, # Small batch size due to small dataset (can be changed once have bigger dataset)
        class_mode="categorical",
        subset="training"
    )
    
    # Creates an augmented training data
    validation_data = training_data_generator.flow_from_directory(
        path,
        target_size=(256, 256), # This would be the size of our pictures
        batch_size=6, # Small batch size due to small dataset (can be changed once have bigger dataset)
        class_mode="categorical",
        subset="validation"
    )    
    
    return next(training_data), next(validation_data)
