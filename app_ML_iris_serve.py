# ML Engineer--> DS --> has provided you with the pkl file --> 


# serve this pkl file --> Is this crystal clear ? 

#%%writefile streamlit_iris.py

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Iris Flower Prediction")


# User input for model features
st.write("## Input Features")
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.0)


# Prepare the input data
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Make prediction
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)


# Output the results
st.write("## Prediction")
st.write(f"The predicted class is: {prediction[0]} (0=setosa, 1=versicolor, 2=virginica)")
st.write("## Prediction Probability")
st.write(f"Setosa: {prediction_proba[0][0]*100:.2f}%")
st.write(f"Versicolor: {prediction_proba[0][1]*100:.2f}%")
st.write(f"Virginica: {prediction_proba[0][2]*100:.2f}%")
