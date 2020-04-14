# Logistic Regression Iris Dataset

# Import the dependencies
from sklearn.linear_model import LogisticRegression
import json
import numpy as np
import pandas as pd
import pickle
import gzip

# Load the data set
data = pd.read_csv('data/titanic.csv')
data.head()

variables = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
metric = ['Survived']

data = data[~data['Age'].isnull()]

# Prepare the training set
# X = feature values, all the columns except the last column
X = data[variables]
# y = target values, last column of the data frame
y = data[metric]

# Init model
model = LogisticRegression(C=1e5)
# Create an instance of Logistic Regression Classifier and fit the data.
model.fit(X, y)

# Export model
pickle.dump(model, gzip.open('model_binary.dat.gz', "wb"))
