import streamlit as st
from app_pages.multipage import MultiPage  # Import the MultiPage class

# Import your page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_visual_study import page_visual_study_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_model_performance import page_ml_performance_metrics

# Create an instance of the app
app = MultiPage(app_name="Mildew Detection in Cherry Leaves")

# Add all your app pages here using .add_page method
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Visual Study of Leaves", page_visual_study_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("Model Performance Metrics", page_ml_performance_metrics)

# Run the app
if __name__ == "__main__":
    app.run()
