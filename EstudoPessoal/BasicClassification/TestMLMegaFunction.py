# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:16:04 2018

@author: lcristovao
"""
import numpy as np
import pandas as pd
from ML_MegaFunction import ReturnPredictor 

#Load dataset from site

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

best_model,dataset=ReturnPredictor(dataset)

values=dataset.values
np.random.shuffle(values)
#Number of tests
n=10
print("Original values:\n",values[:n,:])
for i in range(n):
    print("Prediction for previous line:\n",values[i,:-1],"->",best_model.predict(values[:n,:-1])[i])


#Other dataset example
#_____________________________________________________________________________________________________________________________________________

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
'''
age: continuous. 
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked. 
fnlwgt: continuous. 
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool. 
education-num: continuous. 
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse. 
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces. 
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried. 
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. 
sex: Female, Male. 
capital-gain: continuous. 
capital-loss: continuous. 
hours-per-week: continuous. 
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
'''
names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
         'marital-status','occupation','relationship','race','sex',
         'capital-gain', 'capital-loss','hours-per-week','native-country',
         'class']
dataset = pd.read_csv(url, names=names)
#print(dataset.head)
#Must eliminate ? values of dataset
#dataset2=pd.get_dummies(dataset.iloc[:,:-1])
#dataset2=pd.concat([dataset2,dataset['class']],axis=1)
best_model,dataset=ReturnPredictor(dataset)

values=dataset.values
np.random.shuffle(values)
#Number of tests
n=10

for i in range(n):
    print("Original values:\n line"+str(i)+":",values[i,-1])
    print("Prediction for previous line:\n",values[i,:5],"->",best_model.predict(values[:n,:-1])[i])
    print('\n')

