import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os

def page_mildew_detector_body():
    st.write("### Upload a Cherry Leaf Image to Detect Mildew")
    
    # Model version
    version = 'v1'
    
    # Load model
    model = load_model(f'outputs/{version}/mildew_model_v1.h5')
    
    # File uploader for the image
    uploaded_file = st.file_uploader("Choose a cherry leaf image...", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Cherry Leaf', use_column_width=True)

        # Preprocess the image
        img = img.resize((100, 100))  # Resize to match model input
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize

        # Predict the class
        pred_proba = model.predict(img_array)[0][0]
        pred_class = 'Healthy' if pred_proba < 0.5 else 'Powdery Mildew'
        
        # Display results
        st.write(f"### Prediction: {pred_class}")
        st.write(f"### Probability: {pred_proba:.2f}")
