# ML model 2 --> which is trained on IRIS dataset 

# when you serve your model--> unless your data is very dynamic--> website--> realtime you have to learb--> recommendation

# typically--> you will get a model file--> which is obtained after training the model --> DS 



# first a datascientist : 

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle #Converts a Python object (such as an ML model) into a byte stream.
# In machine learning, you can pickle models, data, or other Python objects to save and reload them later.



#joblib
#onnx ONNX (Open Neural Network Exchange
#HDF5
# PMML (Predictive Model Markup Language) 
#advantages/disadvantes 


# Load dataset
iris = load_iris()
X, y = iris.data, iris.target


# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)
# happy with the performance of the model 
#evaluate the model 


# Save the trained model to a file
with open('iris_model.pkl', 'wb') as file:
    pickle.dump(model, file)