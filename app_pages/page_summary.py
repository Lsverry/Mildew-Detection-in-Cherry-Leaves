import streamlit as st

def page_summary_body():
    """
    Displays a quick summary of the project, including general information, dataset overview,
    and project objectives.
    """
    st.write("### Quick Project Summary")

    # General information about the project
    st.info(
        "**General Information**\n"
        "* Powdery mildew is a fungal disease that affects various plants, "
        "including cherry trees, causing white powdery spots on the leaves.\n"
        "* This project aims to detect whether cherry leaves are infected by powdery mildew using image classification techniques.\n"
        "* By leveraging machine learning, we automate the detection process to help farmers identify infected plants earlier, reducing potential crop damage.\n"
    )

    # Overview of the project dataset
    st.write(
        "**Project Dataset**\n"
        "* The available dataset contains over 4,000 images of cherry leaves, categorized into 'healthy' and 'powdery mildew infected'.\n"
        "* The images are used to train a deep learning model to classify the condition of the leaves based on visual features.\n"
    )

    # Link to the project's README
    st.write(
        "For additional information, please refer to the [**README**](https://github.com/Lsverry/Mildew-Detection-in-Cherry-Leaves/tree/main) in the project repository."
    )

    # Display the project objectives
    st.success(
        "### Project Objectives:\n"
        "1. **Visual Study**: Provide a visual study to help differentiate between healthy and mildew-infected cherry leaves.\n"
        "2. **Prediction Model**: Build a model to predict whether a given leaf image is healthy or infected."
    )
