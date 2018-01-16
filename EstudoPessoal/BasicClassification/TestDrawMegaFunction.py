# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:04:25 2018

@author: lcristovao
"""

import DrawMegaFunction as dm
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer




#____________________Main________________________________

#Irish dataset
# Load dataset from site
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)


predictor=dm.ReturnPredictor(dataset)

#_____________________________________________________________________


# Load dataset from site
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
'''
    1. Number of times pregnant
   2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test
   3. Diastolic blood pressure (mm Hg)
   4. Triceps skin fold thickness (mm)
   5. 2-Hour serum insulin (mu U/ml)
   6. Body mass index (weight in kg/(height in m)^2)
   7. Diabetes pedigree function
   8. Age (years)
   9. Class variable (0 or 1)
'''
names = ['Number-of-times-pregnant', 'Plasma-glucose-concentration', 'Diastolic-blood-pressure', 'Triceps-skin-fold-thickness', 'serum-insulin','Body-mass-index ','Diabetes-pedigree-function','Age','Diabetes']
dataset = pd.read_csv(url, names=names)
dataset.describe()
#Missing values in this dataset are zeros where it does not make sence
##Invalid zero minimal value:
#1: Plasma glucose concentration
#2: Diastolic blood pressure
#3: Triceps skinfold thickness
#4: 2-Hour serum insulin
#5: Body mass index
#these are de columns 1,2,3,4,5 

#Lets find number of zeros of each of these columns
print((dataset.iloc[:,1:6] == 0).sum())
#In pandas is easy to detect and replace missing values if they are NaN so we need
#to replace zeros to NaN with function replace
# mark zero values as missing or NaN
dataset.iloc[:,1:6] = dataset.iloc[:,1:6].replace(0, np.NaN)
# count the number of NaN values in each column
print(dataset.isnull().sum())
# fill missing values with mean column values
dataset.fillna(dataset.mean(), inplace=True)
# count the number of NaN values in each column
print(dataset.isnull().sum())

predictor=dm.ReturnPredictor(dataset)

#____________________________________________________________________________

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

predictor=dm.ReturnPredictor(dataset)

#___________________________________________________________________________________

url ='https://archive.ics.uci.edu/ml/machine-learning-databases/00422/wifi_localization.txt'

names=['s1','s2','s3','s4','s5','s6','s7']
dataset = pd.read_csv(url, names=names, sep='\t')

predictor=dm.ReturnPredictor(dataset)

#__________________________Breast Cancer Dataset_______________________________________________________

'''
Attribute Information:

1) ID number 
2) Diagnosis (M = malignant, B = benign) 
3-32) 

Ten real-valued features are computed for each cell nucleus: 

a) radius (mean of distances from center to points on the perimeter) 
b) texture (standard deviation of gray-scale values) 
c) perimeter 
d) area 
e) smoothness (local variation in radius lengths) 
f) compactness (perimeter^2 / area - 1.0) 
g) concavity (severity of concave portions of the contour) 
h) concave points (number of concave portions of the contour) 
i) symmetry 
j) fractal dimension ("coastline approximation" - 1)
'''
#Breast Cancer Tumors
# Load dataset from site
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wpbc.data"
#names = ['ID-number', 'class', 'radius', 'texture', 'perimeter','area',
#         'smoothness','compactness','concavity','concave points','symmetry',
#         'fractal dimension']

#data = load_breast_cancer()

#dataset=pd.concat([data.data,data.target],axis=1)
