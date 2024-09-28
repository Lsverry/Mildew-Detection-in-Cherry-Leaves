import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from keras.models import load_model  
from keras.preprocessing import image
import os
from src.data_management import export_results_as_csv  

def page_mildew_detector_body():
    st.write("### Upload a Cherry Leaf Image to Detect Mildew")
    
    # Inform the user about the dataset and provide download link
    st.info(
        """
        - The client is interested in determining whether a cherry leaf is healthy or infected with powdery mildew.
        - You can download a set of healthy and infected cherry leaves for live prediction. Download the images from [here](https://www.kaggle.com/codeinstitute/cherry-leaves/download).
        """
    )
    
    # File uploader for the image
    uploaded_file = st.file_uploader("Choose a cherry leaf image...", type="jpg")

    # Load model using the correct function for HDF5
    version = 'v1'
    model = load_model(f'outputs/{version}/mildew_model_v1.h5')  # Using .h5 format

    if uploaded_file is not None:
        # Display the uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Cherry Leaf", use_column_width=True)

        # Preprocess the image
        img = img.resize((100, 100))  # Resize to match model input
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Normalize

        # Predict the class
        pred_proba = model.predict(img_array)[0][0]
        pred_class = 'Healthy' if pred_proba < 0.5 else 'Powdery Mildew'

        # Display results
        st.write(f"#### Prediction: {pred_class}")
        st.write(f"#### Probability: {pred_proba:.2f}")

        # Create a DataFrame to hold the results
        results_df = pd.DataFrame({
            'Image': ['Uploaded Cherry Leaf'],
            'Prediction': [pred_class],
            'Probability': [pred_proba]
        })

        # Provide a download link for the results
        st.markdown(export_results_as_csv(results_df), unsafe_allow_html=True)
