# -*- coding: utf-8 -*-
"""Proyek Pertama : Predictive Analytics

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aNtG1Bx8rp3UAWvoFTkEd_9qGYmV9egt

# Proyek Pertama : Predictive Analytics
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from google.colab import files
from IPython.display import Image
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import export_graphviz
from subprocess import call

"""## Load Data"""

# Upload file
files.upload()

data = pd.read_csv('uci-secom.csv')

data.head()

data.info()

"""## Data Cleaning

### Drop Unnecessary Feature
"""

data.drop(['Time'], axis=1, inplace=True)

"""### Drop feature with 0 variance"""

# Check data variations
data.loc[:, data.var() == 0]

# Drop column with 0 variation
data.drop(data.loc[:, data.var() == 0].columns, axis=1, inplace=True)

data.shape

"""### Handling Missing Value """

# Threshold
nan_r = 0.2

# Choose label with missing values greater than threshold
isna_data = data.isna().sum().sort_values(ascending=False)
isna_label = isna_data[isna_data > len(data)*nan_r].index

# Print label with missing values greater than threshold
print(isna_label)

# Drop column with missing values
data.drop(isna_label, axis=1, inplace=True)

data.shape

"""### Filling Missing Value"""

# Check data with missing value
data.isna().sum()

# Fill all the missing value
data.fillna(method='ffill', inplace=True)
data.fillna(method='bfill', inplace=True)

data.isna().sum().max()

data.shape

"""## Feature Selection

### Pairwise Correlation
"""

# Remove the highly collinear features from data
def remove_collinear_features(x, threshold):
    
    # Calculate the correlation matrix
    corr_matrix = x.corr()
    iters = range(len(corr_matrix.columns) - 1)
    drop_cols = []

    # Iterate through the correlation matrix and compare correlations
    for i in iters:
        for j in range(i+1):
            item = corr_matrix.iloc[j:(j+1), (i+1):(i+2)]
            col = item.columns
            row = item.index
            val = abs(item.values)

            # If correlation exceeds the threshold
            if val >= threshold:
                drop_cols.append(col.values[0])

    # Drop one of each pair of correlated columns
    drops = set(drop_cols)
    x = x.drop(columns=drops)

    return x

data = remove_collinear_features(data, 0.7)

data

"""### Correlation with Target"""

# Drop column that has correlation with target under threshold
data = data.loc[:, data.corr().abs()['Pass/Fail'] > 0.05]

"""## Split Data"""

X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1:], test_size=0.2, random_state=42)

"""## Standardize data"""

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## Train Model"""

# Create DataFrame for evaluation
models = pd.DataFrame(columns=['train_acc', 'test_acc'], 
                      index=['SVM', 'KNN', 'RandomForest', 'Boosting'])

"""### SVM"""

svm_clf = SVC()
svm_clf.fit(X_train, y_train)
y_pred = svm_clf.predict(X_test)

# Calculate model accuracy
train_score = svm_clf.score(X_train, y_train)
model_score = svm_clf.score(X_test, y_test)

# Update model accuracy to models
models['train_acc']['SVM'] = train_score
models['test_acc']['SVM'] = model_score

# Print model accuracy score
print('Model Accuracy:', model_score*100)

print('Classification Report')
print(classification_report(y_test, y_pred))

"""### K-Nearest Neighbor """

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Calculate model accuracy
train_score = knn.score(X_train, y_train)
model_score = knn.score(X_test, y_test)

# Update model accuracy to models
models['train_acc']['KNN'] = train_score
models['test_acc']['KNN'] = model_score

# Print model accuracy score
print('Model Accuracy:', model_score*100)

print('Classification Report')
print(classification_report(y_test, y_pred))

"""### Random Forest"""

rf_clf = RandomForestClassifier()
rf_clf.fit(X_train, y_train)
y_pred = rf_clf.predict(X_test)

# Calculate model accuracy
train_score = rf_clf.score(X_train, y_train)
model_score = rf_clf.score(X_test, y_test)

# Update model accuracy to models
models['train_acc']['RandomForest'] = train_score
models['test_acc']['RandomForest'] = model_score

# Print model accuracy score
print('Model Accuracy:', model_score*100)

print('Classification Report')
print(classification_report(y_test, y_pred))

"""### Boosting Algorithm"""

boosting = AdaBoostClassifier()                             
boosting.fit(X_train, y_train)
y_pred = boosting.predict(X_test)

# Calculate model accuracy
train_score = boosting.score(X_train, y_train)
model_score = boosting.score(X_test, y_test)

# Update model accuracy to models
models['train_acc']['Boosting'] = train_score
models['test_acc']['Boosting'] = model_score

# Print model accuracy score
print('Model Accuracy:', model_score*100)

print('Classification Report')
print(classification_report(y_test, y_pred))

"""### Model Accuracy Evaluation"""

# Print models
models