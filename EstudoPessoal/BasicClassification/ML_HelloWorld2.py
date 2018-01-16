# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:46:07 2018

@author: lcristovao

Objective of this program is to make a function that does all the machine learning Work
I mean it returns the best predictor ready to work. It must be capable to work on multiclass 
datasets. The Values of data set must be numeric or categorical (string)
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


def ReturnPredictor(dataset,true_test_size=0.5,validation_size=0.20,cross_val_splits=10,seed=7):
    #class_index=dataset
    class_index=dataset.shape[1]
    #Shuffle data
    dataset=dataset.sample(frac=1,random_state=seed)
    
    #Divide dataset in two parts
    size=dataset.shape[0]
    half=int(size*true_test_size)
    #Division
    TrainValSet=dataset.iloc[:half]
    TrueErrorSet=dataset.iloc[half:]
	#Train Validation Part-----------------------------------------------------
	 array = TrainValSet.values
	 X = array[:,0:class_index]
	 Y = array[:,class_index]
	 X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
	
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
	mean_results=[]
	for name, model in models:
		kfold = model_selection.KFold(n_splits=cross_val_splits, random_state=seed)
		cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
		mean_results.append(cv_results.mean())
		msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
		print(msg)

	mean_results=np.array(mean_results)	
	best_model_index=mean_results.argmax()
	best_model=models[best_model_index][1]
	print("Best Model: ",models[best_model_index][0])
	
	##Fit best model In Training_validation dataset
	finalArray=TrainValSet.values
	finalX=finalArray[:,:class_index]
	finalY=finalArray[:,class_index] 
	best_model.fit(finalX,finalY)
	
	Truearray=TrueErrorSet.values
	TrueX=Truearray[:,0:class_index]
	TrueY=Truearray[:,class_index]
	predictions = best_model.predict(TrueX)
	print('\n\nTrue Score: ',accuracy_score(TrueY, predictions))
	print('Cunfusuion Matrix \n',confusion_matrix(TrueY, predictions))
	#print(classification_report(TrueY, predictions))

	FFArray=dataset.values
	FFX=FFArray[:,0:class_index]
	FFY=FFArray[:,class_index]
	predictions = best_model.predict(FFX)
	print('\n\nFinal Final Score: ',accuracy_score(FFY, predictions))
	print('Confusion matrix\n',confusion_matrix(FFY, predictions))
	return best_model

#------------Main----------------------------------------------------
# Load dataset from site
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)




best_model=ReturnPredictor(dataset)


"""
seed=7

#To do ML right we should analyse the data, see the best atributes that separates data
#But here I am going straight to the function

#Shuffle data
dataset=dataset.sample(frac=1,random_state=seed)

#Divide dataset in two parts
train_validation_per=0.5
size=dataset.shape[0]
half=int(size*train_validation_per)
#Division
TrainValSet=dataset.iloc[:half]
TrueErrorSet=dataset.iloc[half:] 

#Train Validation Part-----------------------------------------------------
array = TrainValSet.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


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
mean_results=[]
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	mean_results.append(cv_results.mean())
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)

mean_results=np.array(mean_results)	
best_model_index=mean_results.argmax()
best_model=models[best_model_index][1]
print("Best Model: ",models[best_model_index][0])

##Fit best model in my case all models gave 100% score
finalArray=TrainValSet.values
finalX=finalArray[:,:4]
finalY=finalArray[:,4] 
best_model.fit(finalX,finalY)
	
Truearray=TrueErrorSet.values
TrueX=Truearray[:,0:4]
TrueY=Truearray[:,4]
predictions = best_model.predict(TrueX)
print('\n\nTrue Score: ',accuracy_score(TrueY, predictions))
print('Cunfusuion Matrix \n',confusion_matrix(TrueY, predictions))
#print(classification_report(TrueY, predictions))

FFArray=dataset.values
FFX=FFArray[:,0:4]
FFY=FFArray[:,4]
predictions = best_model.predict(FFX)
print('\n\nFinal Final Score: ',accuracy_score(FFY, predictions))
print('Confusion matrix\n',confusion_matrix(FFY, predictions))
"""