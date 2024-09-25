import streamlit as st
import matplotlib.pyplot as plt
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
    version = 'v1'

    st.write("### Train, Validation, and Test Set: Labels Frequencies")
    labels_distribution = plt.imread(f"outputs/{version}/image_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation, and Test Sets')
    st.write("---")

    st.write("### Model Training History")
    col1, col2 = st.beta_columns(2)
    with col1:
        model_acc = plt.imread(f"outputs/training_plots/training_vs_validation_accuracy.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/training_plots/training_vs_validation_loss.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_mildew_test_evaluation(version), index=['Loss', 'Accuracy']))
