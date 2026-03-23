# AI Corruption Detection Dashboard

## Project Overview

This project builds an **AI-powered corruption detection system** that analyzes government project data and predicts potential corruption levels.

The system uses **Machine Learning (Artificial Neural Network)** to estimate corruption patterns based on project budgets, actual costs, location, and project category.

An interactive **dashboard built with Streamlit and Plotly** allows users to explore corruption trends dynamically.

---

# Model Training

The AI model was trained using **Jupyter Notebook**.

### Training Process

* Data preprocessing
* Feature selection
* Model training
* Prediction generation
* Model evaluation

### Algorithm Used

Artificial Neural Network implemented using **Scikit-learn MLPRegressor**.

---

# Dashboard Development

The trained model insights are visualized using an interactive dashboard built with:

* Streamlit
* Plotly

The dashboard allows users to explore corruption trends dynamically.

---

# Features

### Corruption Prediction

Predict corruption amount using an ANN model.

### State-wise Analysis

Compare corruption levels across different states.

### City-wise Analysis

Analyze corruption patterns across cities.

### Budget vs Actual Cost Analysis

Identify differences between allocated budgets and actual project spending.

### Project Category Analysis

Analyze corruption across project types:

* Roads
* Bridges
* Parks
* Government Buildings

### Population Corruption Impact

Estimate how much money each citizen could receive if corruption did not occur.

### Citizen Wealth Loss Counter

Displays total corruption loss and per-citizen wealth impact.

### AI Corruption Risk Analysis

Identifies regions with higher corruption risk.

---

# Project Structure

AI-corruption-detection
│
├── app.py
├── corruption_model_training.ipynb
├── corruption_data.csv
├── requirements.txt
└── README.md

---

# Technologies Used

### Programming Language

Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Plotly
* Matplotlib
* Streamlit
* Tensorflow

---

# Python Version

Python 3.10

---

# Installation

Install dependencies:

pip install -r requirements.txt

---

# Run the Dashboard

Run the Streamlit app:

streamlit run app.py

---

# Requirements

streamlit==1.30.0
pandas==2.0.3
numpy==1.24.3
plotly==5.18.0
scikit-learn==1.3.2
matplotlib==3.7.2

---

# Future Improvements

* Deploy dashboard online
* Add real-time corruption data
* Improve AI model accuracy
* Add more government project categories

---

# Author

Sai Vignesh

