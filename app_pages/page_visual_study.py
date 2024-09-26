import streamlit as st
import matplotlib.pyplot as plt
import os
from matplotlib.image import imread
import random
from PIL import Image
import numpy as np

def create_image_montage(image_dir, montage_size=(5, 5), image_size=(100, 100)):
    image_paths = [os.path.join(image_dir, img) for img in os.listdir(image_dir)]
    selected_images = random.sample(image_paths, montage_size[0] * montage_size[1])
    
    # Initialize an empty array for the montage
    montage = np.zeros((image_size[0] * montage_size[0], image_size[1] * montage_size[1], 3), dtype=np.uint8)
    
    for i, img_path in enumerate(selected_images):
        img = Image.open(img_path)
        img_resized = img.resize(image_size)  # Resize the image to the specified size
        img_array = np.array(img_resized)
        
        # Calculate the position where the image will be placed in the montage
        row_start = (i // montage_size[1]) * image_size[0]
        col_start = (i % montage_size[1]) * image_size[1]
        
        # Place the resized image in the montage
        montage[row_start:row_start + image_size[0], col_start:col_start + image_size[1], :] = img_array
    
    return montage

def page_visual_study_body():
    st.write("### Visual Study of Cherry Leaves")

    # Information for the user
    st.info(
        f"**Objective**: This section allows you to visually differentiate between healthy cherry leaves and those infected with powdery mildew.\n"
        f"**Dataset Overview**: We will display pre-generated images from the dataset showcasing examples of healthy leaves and those infected by powdery mildew."
    )

    # Checkbox for showing images (Average and Variability) for healthy and infected categories
    if st.checkbox("Difference between average and variability image"):
        st.write("Displaying Average and Variability images for healthy and infected leaves")

        st.warning(
            "We notice that although there is a slight difference in the pigmentation and texture between healthy "
            "and infected leaves, these characteristics are subtle and may require further analysis through "
            "the model to draw definitive conclusions. The infected leaves tend to show visible signs of powdery mildew "
            "on the surface, but other factors might obscure these differences."
        )
        
        # Paths to healthy and infected leaf images
        healthy_image_path = 'outputs/v1/mean_var_label_healthy.png'
        infected_image_path = 'outputs/v1/mean_var_label_powdery_mildew.png'
        
        # Display the healthy leaf images
        if os.path.exists(healthy_image_path):
            healthy_img = imread(healthy_image_path)
            st.image(healthy_img, caption="Healthy Leaf - Average and Variability", use_column_width=True)
        
        # Display the infected leaf images
        if os.path.exists(infected_image_path):
            infected_img = imread(infected_image_path)
            st.image(infected_img, caption="Powdery Mildew Leaf - Average and Variability", use_column_width=True)


    # Checkbox for showing differences between average healthy and infected leaves
    if st.checkbox("Differences between average healthy and infected leaves"):
        st.write("### Displaying the difference between average healthy and powdery mildew leaves")
        
        st.warning(
            "We observe that the average images of healthy and powdery mildew leaves show some similar patterns, "
            "but the difference image reveals subtle changes in texture and color. "
            "This suggests that the distinction between the two might be harder to perceive with the naked eye "
            "and requires further analysis through machine learning to fully differentiate them."
        )
        
        diff_image_path = 'outputs/v1/avg_diff_healthy_vs_powdery_mildew.png'

        if os.path.exists(diff_image_path):
            diff_img = imread(diff_image_path)
            st.image(diff_img, caption="Difference Image", use_column_width=True)


    # Checkbox for creating an image montage
    if st.checkbox("Image Montage"):
        st.write("To refresh the montage, click on the 'Create Montage' button")
        
        # User selects between healthy or powdery_mildew label
        label_options = ['healthy', 'powdery_mildew']
        selected_label = st.selectbox("Select label", label_options)
        
        if st.button("Create Montage"):
            image_dir = f'inputs/cherry-leaves/train/{selected_label}'
            montage = create_image_montage(image_dir)
            
            # Display the generated montage using matplotlib
            fig, ax = plt.subplots(figsize=(10, 10))
            ax.imshow(montage)
            ax.axis('off')  # Hide the axes
            st.pyplot(fig)
