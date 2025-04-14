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

