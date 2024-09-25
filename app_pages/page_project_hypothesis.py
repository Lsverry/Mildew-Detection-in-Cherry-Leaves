import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    """
    Displays the project hypothesis and validation based on the analysis of the cherry leaves dataset.
    Highlights key visual indicators of infection and the need for further ML model analysis.
    """
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect that cherry leaves affected by powdery mildew have visible signs "
        f"of infection, particularly a white powdery substance that differentiates them "
        f"from healthy leaves. \n\n"
        f"* A visual inspection of infected leaves typically shows these clear signs on the surface, "
        f"but sometimes they might be more subtle depending on the stage of infection. "
        f"Average Image, Variability Image, and Difference between Averages studies help in analyzing these patterns, "
        f"but further analysis with the ML model is required to fully differentiate them."
    )
