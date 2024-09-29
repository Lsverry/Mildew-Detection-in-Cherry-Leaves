import streamlit as st
import base64
from PIL import Image
import numpy as np
import pandas as pd
from keras.models import load_model  
from keras.preprocessing import image
import os
import requests
from io import BytesIO

def download_model(url, model_path):
    """
    Downloads the model from the specified URL if it does not already exist locally.

    Args:
    url (str): The URL where the model is hosted.
    model_path (str): The local path where the model will be saved.

    Returns:
    str: Path to the local model file.
    """
    if not os.path.exists(model_path):
        st.write("Downloading the model. This may take a while...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(model_path, 'wb') as f:
                f.write(response.content)
            st.success("Model downloaded successfully!")
        else:
            st.error(f"Failed to download the model. Status code: {response.status_code}")
    return model_path

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

    # Define the model URL and local path
    model_url = 'https://github.com/Lsverry/Mildew-Detection-in-Cherry-Leaves/releases/download/mildew_model/mildew_model_v1.h5'
    model_path = 'outputs/v1/mildew_model_v1.h5'

    # Download the model if it's not already present
    model_path = download_model(model_url, model_path)

    # Load model using the correct function for HDF5
    if os.path.exists(model_path):
        model = load_model(model_path)
    else:
        st.error("Model not found. Please check the download process.")

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
        csv = results_df.to_csv(index=False).encode('utf-8')
        b64 = base64.b64encode(csv).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="mildew_detection_results.csv">Download CSV Report</a>'
        st.markdown(href, unsafe_allow_html=True)
