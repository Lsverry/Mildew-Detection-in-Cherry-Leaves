import streamlit as st
import random
import os
import matplotlib.pyplot as plt
from matplotlib.image import imread

def page_visual_study_body():
    st.write("### Visual Study of Cherry Leaves")

    # Information for the user
    st.info(
        f"**Objective**: This section allows you to visually differentiate between healthy cherry leaves and those infected with powdery mildew.\n"
        f"**Dataset Overview**: We will display random images from the dataset to showcase examples of healthy leaves and those infected by powdery mildew."
    )

    # Define the path to the dataset
    my_data_dir = 'inputs/cherry-leaves'
    
    # Define categories (healthy vs. infected)
    labels = os.listdir(my_data_dir + '/train')
    
    # Let the user select a category
    label_to_display = st.selectbox("Select leaf category", labels)

    # Path to the selected category
    selected_label_dir = my_data_dir + '/train/' + label_to_display

    # Display random images
    if st.button("Generate Random Image"):
        # Select a random image
        random_image = random.choice(os.listdir(selected_label_dir))
        img_path = os.path.join(selected_label_dir, random_image)

        # Display the image
        img = imread(img_path)
        st.image(img, caption=f"Random {label_to_display} leaf", use_column_width=True)

        # Show some image properties (optional)
        st.write(f"**Image shape**: {img.shape}")
