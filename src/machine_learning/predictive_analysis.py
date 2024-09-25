import numpy as np
import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
from src.data_management import load_model_or_data

# Load trained model
def load_trained_model(version):
    """
    Load the trained mildew detection model from the specified version.

    Args:
    version (str): The version of the model to be loaded ('v1').

    Returns:
    keras.Model: The loaded Keras model ready for prediction.
    """
    model_path = f'outputs/{version}/mildew_model.h5'
    return load_model(model_path)

# Load and preprocess a new image for prediction
def preprocess_image(image_path, target_size):
    """
    Preprocess the image for prediction by resizing and scaling it.

    Args:
    image_path (str): Path to the image to be preprocessed.
    target_size (tuple): Target size for the image (height, width).

    Returns:
    numpy.ndarray: Preprocessed image array ready for model prediction.
    """
    img = image.load_img(image_path, target_size=target_size, color_mode='rgb')
    img_array = image.img_to_array(img) / 255.0  # Normalize to 0-1 range
    img_array = np.expand_dims(img_array, axis=0) 
    return img_array

# Predict the class of an image using the trained model
def predict_mildew_class(model, img_array, class_indices):
    """
    Predict whether the image belongs to the 'healthy' or 'mildew' class.

    Args:
    model (keras.Model): The trained model to be used for prediction.
    img_array (numpy.ndarray): Preprocessed image array.
    class_indices (dict): Mapping of class indices to class names.

    Returns:
    tuple: Predicted probability and predicted class ('healthy' or 'mildew').
    """
    prediction = model.predict(img_array)[0, 0]  # Get the probability
    predicted_class = 'healthy' if prediction < 0.5 else 'mildew'
    return 1 - prediction if predicted_class == 'healthy' else prediction, predicted_class

# Display prediction results
def display_prediction_results(prediction_prob, predicted_class):
    """
    Display the prediction results in the Streamlit app.

    Args:
    prediction_prob (float): The probability associated with the predicted class.
    predicted_class (str): The predicted class, either 'healthy' or 'mildew'.
    """
    st.write(f"Predicted class: **{predicted_class}**")
    st.write(f"Prediction probability: **{prediction_prob:.2f}**")

# Main function to run predictions
def run_prediction(version, image_path, target_size=(100, 100)):
    """
    Load the model, preprocess the image, and make a prediction.

    Args:
    version (str): Version of the model to be loaded.
    image_path (str): Path to the image file to be predicted.
    target_size (tuple): Size to which the image will be resized.

    Returns:
    None
    """
    model = load_trained_model(version)
    img_array = preprocess_image(image_path, target_size)
    class_indices = load_model_or_data(f'outputs/{version}/class_indices.pkl')
    
    prediction_prob, predicted_class = predict_mildew_class(model, img_array, class_indices)
    display_prediction_results(prediction_prob, predicted_class)
