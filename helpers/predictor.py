import logging
import numpy as np

from keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from keras.preprocessing import image
from tensorflow.python.keras.backend import set_session

import tensorflow as tf
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True


# Model saved with Keras model.save()
MODEL_PATH = 'models/classifier_30.model'

# Load your trained model
global graph
graph = tf.get_default_graph()

# set the session state for detection
session = tf.Session()
set_session(session)

# load the model and get the model running for prediction
model = load_model(MODEL_PATH)
model._make_predict_function()

# label reference
cancer_type_dict = {0: "basal ", 1: "Dermatofibrosarcoma protuberans", 2: "cutaneous",
            3: "Merkel ", 4: "melanoma", 5: "squamous cell carcinoma", 6: "Negative"}


def model_predict(img_path, model):
    """ Make predictions by loading the image into the session

    Args:
        img_path (str): image path url
        model (object): loaded model object

    Returns:
        np.array: numpy array with the values of each class
    """
    try:
        
        # loading the image with the set target
        img = image.load_img(img_path, target_size=(244, 244))

        logging.info("Image loaded successfully")
        
        # Preprocessing the image
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x, mode='caffe')
        
        prediction = ""

        # set the default graph again
        with graph.as_default():
            # set the same session for prediction
            set_session(session)
            prediction = model.predict(x)
        logging.info('Predition made successfully!!!')

    except Exception as e:
        logging.exception(f"An error occurred while prediction: {e}")
        raise

    return prediction


def predict_type(image_path: str, image_object, is_object=False):
    """Return the type of skin cancer based on the input image

    Args:
        image_path (str): path of the image to be detected
        image_object (str): PIL image instance
        is_object (bool): Set to true if the image is a PIL Image instance
    Returns:
        str: return the detected type
    """

    # call the prediction method
    predict_output = model_predict(image_path, model)

    predicted_class = predict_output.argmax(axis=1)

    result = str(cancer_type_dict[int(predicted_class)])

    return result
