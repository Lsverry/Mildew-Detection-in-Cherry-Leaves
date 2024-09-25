import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects various plants, "
        f"including cherry trees, causing white powdery spots on the leaves.\n"
        f"* This project aims to detect whether cherry leaves are infected by powdery mildew using image classification techniques.\n"
        f"* By leveraging machine learning, we automate the detection process to help farmers identify infected plants earlier, reducing potential crop damage.\n"
    )

    st.write(
        f"**Project Dataset**\n"
        f"* The available dataset contains over 4,000 images of cherry leaves, categorized into 'healthy' and 'powdery mildew infected'.\n"
        f"* The images are used to train a deep learning model to classify the condition of the leaves based on visual features.\n"
    )

    st.write(
        f"For additional information, please refer to the **README** in the project repository."
    )

    st.success(
        f"The project has 2 main objectives:\n"
        f"1. Provide a visual study to help differentiate between healthy and mildew-infected cherry leaves.\n"
        f"2. Build a model to predict whether a given leaf image is healthy or infected."
    )
