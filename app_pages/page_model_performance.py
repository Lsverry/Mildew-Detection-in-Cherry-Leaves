import streamlit as st
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate import load_mildew_test_evaluation

def page_ml_performance_metrics():
    """
    Displays the performance metrics of the model, including:
    - Label distribution on train, validation, and test sets.
    - Model training history (accuracy and loss).
    - Generalized performance on the test set.
    """
    version = 'v1'  # Version of the model and outputs

    # Display the distribution of labels in the train, validation, and test sets
    st.write("### Train, Validation, and Test Set: Labels Frequencies")
    labels_distribution = imread(f"outputs/{version}/image_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation, and Test Sets')
    st.write("---")

    # Display the training history of the model (accuracy and loss)
    st.write("### Model Training History")
    col1, col2 = st.beta_columns(2)

    # Model accuracy plot
    with col1:
        model_acc = imread("outputs/training_plots/training_vs_validation_accuracy.png")
        st.image(model_acc, caption='Model Training Accuracy')

    # Model loss plot
    with col2:
        model_loss = imread("outputs/training_plots/training_vs_validation_loss.png")
        st.image(model_loss, caption='Model Training Losses')

    st.write("---")

    # Display the generalized performance on the test set
    st.write("### Generalized Performance on Test Set")
    st.dataframe(pd.DataFrame(load_mildew_test_evaluation(version), index=['Loss', 'Accuracy']))
