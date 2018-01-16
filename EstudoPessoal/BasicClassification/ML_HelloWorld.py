# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:24:15 2018

@author: lcristovao
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn import datasets
from pandas.plotting import scatter_matrix
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB

# import some data to play with
#iris = datasets.load_iris()
#X = iris.data[:, :2]  # we only take the first two features.
#y = iris.target


# Load dataset from site
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

#process data in order to turn classes in numerical form
#dataset=pd.get_dummies(dataset)
#print(dataset[dataset['class_Iris-versicolor']==1]['class_Iris-versicolor'])
print(dataset.describe(),'\n')
# class distribution
print(dataset.groupby('class').size())
#class distribution
#print('Class:\nIris_setosa  '+str((dataset['class_Iris-setosa']==1).sum()))
#print('Iris_versicolor  '+str((dataset['class_Iris-versicolor']==1).sum()))
#print('Iris_virginica  '+str((dataset['class_Iris-virginica']==1).sum()))

# box and whisker plots
dataset.iloc[:,:4].plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

dataset.iloc[:,:4].hist()
plt.show()

dataset=dataset.sample(frac=1,random_state=7)
# scatter plot matrix
scatter_matrix(dataset.iloc[:,:4])
plt.show()

#Now we need to get 2 datasets on for training and validation
#other to test the true error or accuracy
#let's try 50-50
size=dataset.shape[0]
half=int(size/2)
TrainValSet=dataset.iloc[:half]
TrueErrorSet=dataset.iloc[half:] 


# Split-out validation dataset
array = TrainValSet.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', svm.SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


##Fit best model in my case all models gave 100% score
finalArray=TrainValSet.values
finalX=finalArray[:,:4]
finalY=finalArray[:,4]    
knn = KNeighborsClassifier()
knn.fit(finalX, finalY)



Truearray=TrueErrorSet.values
TrueX=Truearray[:,0:4]
TrueY=Truearray[:,4]
predictions = knn.predict(TrueX)
print('\n\nFinal Score: ',accuracy_score(TrueY, predictions))
print(confusion_matrix(TrueY, predictions))
print(classification_report(TrueY, predictions))


FFArray=dataset.values
FFX=FFArray[:,0:4]
FFY=FFArray[:,4]
#knn = KNeighborsClassifier()
#knn.fit(FFX, FFY)
predictions = knn.predict(FFX)
print('\n\nFinal Final Score: ',accuracy_score(FFY, predictions))
print(confusion_matrix(FFY, predictions))
print(classification_report(FFY, predictions))