import streamlit as st

def page_project_hypothesis_body():
    """
    Displays the project hypothesis and validation based on the analysis of the cherry leaves dataset.
    Highlights key visual indicators of infection and the need for further ML model analysis.
    """
    st.write("### Project Hypothesis and Validation")

    # Project hypothesis and findings
    st.success(
        "* We suspect that cherry leaves affected by powdery mildew have visible signs "
        "of infection, particularly a white powdery substance that differentiates them "
        "from healthy leaves.\n\n"
        "* A visual inspection of infected leaves typically shows these clear signs on the surface, "
        "but sometimes they might be more subtle depending on the stage of infection. "
        "Average Image, Variability Image, and Difference between Averages studies help in analyzing these patterns, "
        "but further analysis with the ML model is required to fully differentiate them."
    )
