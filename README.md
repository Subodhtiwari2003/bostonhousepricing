## Boston House Pricing Prediction
## Software And Tools Requirement
1. [Github Account](https://github.com)
2. [VS Code IDE](https://code.visualstudio.com)
3. [Heroku Account](https://heroku.com)
4. [Git CLI](https://git.com/book/en/v2/Getting-Sorted-The-Command-Line)

## Boston House Pricing Prediction
Welcome to the Boston House Pricing Prediction project! This repository demonstrates how machine learning can predict housing prices based on key features like crime rate, number of rooms, and location-related data. It includes the entire workflow—from data preprocessing to deploying a web application.

## 📋 Table of Contents
- Overview
- Software and Tools Required
- Project Workflow
- Installation and Setup
- Project Structure
- How to Use the Web Application
- Results
- License

## 🔍 Overview
This project is built to predict house prices in Boston using machine learning techniques. By analyzing the influential features of housing data, the model can give accurate price predictions. The project also includes a web application for user-friendly interaction, deployed on Heroku.


## Key Features
- Implements linear regression for prediction.
- Preprocesses data using scaling and transformation.
- Tracks model training using pickle files.
- Offers a simple yet elegant Flask-based web app for predictions.

## 🛠 Software and Tools Required
To run this project, you’ll need the following tools:
- GitHub Account: For managing version control and hosting the repository.
- VS Code IDE: For coding and debugging.
- Heroku Account: For deploying the web application.
- Python Libraries:- Flask
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Gunicorn (for Heroku deployment)

## 🚀 Project Workflow
- Data Preparation:- Load the dataset (Linear Regression ML Implementation.ipynb).
- Handle missing values and preprocess features. 

- Model Building:- Train a linear regression model and save it as regmodel.pkl.
- Scale the data using StandardScaler and save it as scaling.pkl.

- Web App Development:- Build a Flask application (app.py) for making predictions interactively.
- Use the saved model and scaler for predictions.

- Deployment:- Set up the project with requirements.txt and procfile.
- Deploy on Heroku for public access.

## ⚙️ Installation and Setup
Follow these steps to set up the project:
Clone the Repository
git clone https://github.com/Subodhtiwari2003/bostonhousepricing.git
cd bostonhousepricing


Set Up the Environment
- Install the required dependencies:pip install -r requirements.txt

- Set up Flask for local development:flask run

Run the Web App Locally
To test the app locally, execute:
python app.py


Visit http://127.0.0.1:5000 in your browser to interact with the app.


## 📂 Project Structure
Here’s how the repository is organized:
bostonhousepricing/
│
├── src/                     # Contains source code
│   ├── preprocessing.py     # Code for data cleaning and transformation
│   ├── train_model.py       # Model training script
│
├── templates/               # HTML files for the Flask web app
│   ├── index.html           # Main web page for user interaction
│
├── Linear Regression ML Implementation.ipynb # Jupyter notebook for EDA & training
├── app.py                   # Flask app for prediction
├── regmodel.pkl             # Saved linear regression model
├── scaling.pkl              # Saved scaler object
├── requirements.txt         # Project dependencies
├── setup.py                 # Deployment script
├── procfile                 # Heroku-specific deployment configuration
├── LICENSE                  # Open-source license
└── README.md                # Documentation (this file!)

## 🖥️ How to Use the Web Application
- Input Features: Open the web app and fill in the required housing data:- Number of Rooms
- Crime Rate
- Accessibility to Highways
- Other relevant features.

- Submit Your Data: Click the "Predict Price" button.
- View the Results: The app will display the predicted house price.

## 📊 Results
The linear regression model achieves competitive performance:
- R² Score: High accuracy (evaluated on test data).
- Insights:- Features like the number of rooms (RM) and the percentage of lower-status population (LSTAT) significantly influence house prices.

##📈 Future Scope
- Enhance the Model: Explore advanced algorithms like Random Forests or Gradient Boosting for better accuracy.
- Add More Features: Incorporate additional datasets to capture other factors like neighborhood amenities.
- Deploy on Cloud Platforms: Use AWS or Azure for better scalability.

















