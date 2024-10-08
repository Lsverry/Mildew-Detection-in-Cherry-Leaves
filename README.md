## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?
* Hypothesis: A healthy cherry leaf and one infected with powdery mildew can be visually differentiated based on texture, color, and other visual characteristics.
* Validation: Conduct an image analysis study, comparing the average and variability images of healthy and infected leaves.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
**Business Requirement 1**: Data Visualization 
   * Display average and variability images for both healthy and infected cherry leaves.
   * Visualize the difference between the average healthy leaf and the average infected leaf.
   * Display an image montage for both healthy and infected leaves.
   
**Business Requirement 2**: Classification
   * Develop a binary classifier to predict whether a cherry leaf is healthy or infected with powdery mildew.
   * Generate classification reports with performance metrics.

## ML Business Case
* The goal is to build an ML model capable of predicting whether a cherry leaf is healthy or infected with powdery mildew, using historical image data.
* The model should provide a reliable and faster alternative to manual inspection.
* Success metrics:
   * The model must achieve an accuracy of at least 97% on the test set.
* Model output:
   * A binary classification (healthy or infected) along with the probability score.

## Dashboard Design
### Page 1: Project Summary
* The client and project description, including the business requirements.
* Dataset overview: Number of images, classes (healthy and infected), and image dimensions (100x100 pixels).

### Page 2: Visual Study of Cherry Leaves
* This page addresses Business Requirement 1.
* Checkbox 1: Show average and variability images for both healthy and infected leaves.
* Checkbox 2: Display the differences between the average healthy leaf and the average infected leaf.
* Checkbox 3: Image montage for visual comparison.

### Page 3: Mildew Detector
* This page addresses Business Requirement 2.
* Link to download cherry leaf images for live prediction.
* A file uploader widget where users can upload multiple cherry leaf images. The system will display each image and predict whether the leaf is healthy or infected, along with the probability score.
* A table summarizing the image names and prediction results, with a download option.

### Page 4: Hypothesis and Validation
* Block for each project hypothesis, detailing conclusions and how the hypothesis was validated.

### Page 5: Model Performance Metrics
* Label frequencies: We visualized the distribution of healthy and infected leaves in the training, validation, and test sets.
* Training history: Accuracy and loss curves for both the training and validation sets were plotted to monitor the model's performance and ensure there was no overfitting.
* Test set evaluation: The final model achieved an impressive accuracy of 99.76% on the test set, with a very low loss of 0.00435.

## Bugs
### 1. **Deployment on Heroku - Slug Size Exceeded**
- **Issue**: During the deployment to Heroku, the project exceeded the 500MB slug size limit due to the inclusion of the machine learning model file (`mildew_model_v1.h5`), which was too large to be stored directly in the repository.
- **Solution**: The solution was to upload the model externally (using [GitHub Releases](https://github.com/Lsverry/Mildew-Detection-in-Cherry-Leaves/releases)) and download it dynamically at runtime, reducing the slug size. Here’s how we addressed it:

```python
import requests

model_url = 'https://github.com/Lsverry/Mildew-Detection-in-Cherry-Leaves/releases/download/mildew_model/mildew_model_v1.h5'
model_path = 'outputs/v1/mildew_model_v1.h5'

if not os.path.exists(model_path):
    with requests.get(model_url, stream=True) as r:
        r.raise_for_status()
        with open(model_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
```
This code downloads the model when needed and saves it locally without adding it to the repository, keeping the repository size manageable.
## Unfixed Bugs

- No significant errors were found.

## Code Quality Check

We have analyzed the entire project using **Pylint** to ensure that it complies with Python's PEP8 standards. The Pylint analysis did not report any critical errors or warnings, ensuring that the code follows best practices in terms of structure and formatting.

### Pylint Results:
- No significant issues were found during the analysis.
- Only minor warnings related to long lines of code were detected, which do not affect the functionality or readability of the project.

The code is clean, follows the PEP8 guidelines, and is well-structured to ensure maintainability and readability for future developments.


## Deployment

### Heroku

- The App live link is: https://mildew-detection-cherry-leaves-a3f973f9a192.herokuapp.com/
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- os: Interacting with the operating system and file paths
- shutil: High-level file operations like copying and moving files
- random: Random selections and shuffling for randomization processes
- zipfile: Extracting and working with ZIP files
- numpy: Efficient numerical operations and handling arrays
- pandas: Data manipulation and analysis, especially for working with dataframes
- matplotlib: Plotting and visualizing data with charts and graphs
- seaborn: Enhancing Matplotlib plots with better visualizations
- joblib: Saving and loading machine learning models and other objects
- imageio: Reading and processing image files for analysis
- tensorflow: Building, training, and running neural networks
- keras: High-level API to build and train machine learning models (part of TensorFlow)
- itertools: Efficient looping and creating iterators for combinations
- PIL (Pillow): Image processing library for opening and manipulating image files

## Credits
- [**Malaria Detector**](https://github.com/Code-Institute-Org/WalkthroughProject01): This project served as a foundational inspiration not only to structure and develop our project, but also to guide several key aspects of the implementation. We adapted and reused several blocks of code from the malaria detector project to meet project deadlines and ensure the successful delivery of the application.

- **Model Loading Code**: The approach to downloading and loading the model dynamically from an external source was inspired by discussions on GitHub and Stack Overflow, one particular source of inspiration was the [Stack Overflow post](https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url) on downloading large files from external links during application runtime.

