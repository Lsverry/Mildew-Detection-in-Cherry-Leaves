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
* Dataset overview: Number of images, classes (healthy and infected), and image dimensions (256x256 pixels).

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
* Label frequencies for the train, validation, and test sets.
* Model training history: Accuracy and loss plots.
* Evaluation metrics: Confusion matrix, classification report, and final model accuracy.

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits
* **"Malaria Detector"** project for inspiration in structuring and developing this project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.
