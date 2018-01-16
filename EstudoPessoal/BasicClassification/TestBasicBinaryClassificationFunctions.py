# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:48:40 2018

@author: lcristovao
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import seaborn as sns
#Linear Classification function
def LinearBinaryClassification(points,class_table,C=100.0,gamma=0.7,draw_region_step=1,alpha=0.3):
    #C = 100.0  # SVM regularization parameter
    #gamma=0.7
    xy=points
    c=class_table
    clf = svm.SVC(kernel = 'linear',  gamma=gamma, C=C )
    clf.fit(xy, c)
    score=clf.score(xy,c)
    print("Linear Score:",score)
    
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(int(xy[:,0].min()-0.5), int(xy[:,0].max()+0.5))
    yy = a * xx - (clf.intercept_[0]) / w[1]
    #a[ (3>a[:,1]) & (a[:,1]>-6) ]
    
    xx=xx[(yy<(xy[:,1].max()+0.5)) & (yy>(xy[:,1].min()-0.5))]
    yy=yy[(yy<(xy[:,1].max()+0.5)) & (yy>(xy[:,1].min()-0.5))]
    #print('yy:-----------------')
    #print(xx,yy)
    #print('yy:-----------------')
    plt.figure()
    plt.plot(xx, yy, 'k-')
    plt.plot(xy[:,0][c==1],xy[:,1][c==1],'ro')
    plt.plot(xy[:,0][c==0],xy[:,1][c==0],'bo')
    #axes=plt.gca()
    #axes.fill_between(xx,yy,facecolor='blue',alpha=0.5)
    
    plt.title("C="+str(C)+" ;gamma="+str(gamma)+" ;score: "+str(score))
    h = draw_region_step  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = points[:, 0].min() -0.5, points[:, 0].max()+0.5 
    y_min, y_max = points[:,1].min()-0.5 , points[:,1].max()+0.5 
    xx2, yy2 = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    #print(xx2)
    Z = clf.predict(np.c_[xx2.ravel(), yy2.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx2.shape)
    plt.plot(xx2[Z==1],yy2[Z==1],'r.',alpha=alpha)
    plt.plot(xx2[Z==0],yy2[Z==0],'b.',alpha=alpha)
    
#Linear Classification function
def NonLinearBinaryClassification(points,class_table,tolerance=0.001,draw_region_step=1,alpha=0.3):
    clf = svm.NuSVC(tol=tolerance)
    X=points
    Y=class_table
    clf.fit(X,Y)
    score=clf.score(X, Y)
    print("Non linear score:",score)
    #Z=clf.decision_function(X)
    #print(Z)
    #Draw points of classification----------------------------------
    h = draw_region_step  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    #print(Z[:,0])
    #--------------------------------------------------------------
    plt.figure()
    plt.contour(xx, yy, Z, cmap=plt.cm.Paired)
    #axes=plt.gca()
    #axes.fill_between(xx,Z,facecolor='blue',alpha=0.5)
    plt.plot(xx[Z==1],yy[Z==1],'r.',alpha=alpha)
    plt.plot(xx[Z==0],yy[Z==0],'b.',alpha=alpha)
    plt.plot(X[:,0][Y==1],X[:,1][Y==1],'ro')
    plt.plot(X[:,0][Y==0],X[:,1][Y==0],'bo')
    plt.title("tolerance="+str(tolerance)+" ;score: "+str(score))
    
#Linear Classification function2
def NonLinearBinaryClassification2(points,class_table,tolerance=0.001,C=1.0,gamma=0.7,draw_region_step=1,alpha=0.3,choose_best=True):
    clf = svm.SVC(C=C,gamma=gamma,tol=tolerance)
    X=points
    Y=class_table
    clf.fit(X,Y)
    score=clf.score(X, Y)
    print("Non linear score:",score)
    #Z=clf.decision_function(X)
    #print(Z)
    #Draw points of classification----------------------------------
    
    h = draw_region_step  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + .5
    y_min, y_max = X[:,1].min() - .5, X[:,1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    
    
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    #print(Z[:,0])
    #--------------------------------------------------------------
    plt.figure()
    plt.contour(xx, yy, Z, cmap=plt.cm.Paired)
    #axes=plt.gca()
    #axes.fill_between(xx,Z,facecolor='blue',alpha=0.5)
    
    plt.plot(xx[Z==1],yy[Z==1],'r.',alpha=alpha)
    plt.plot(xx[Z==0],yy[Z==0],'b.',alpha=alpha)
    plt.plot(X[:,0][Y==1],X[:,1][Y==1],'ro')
    plt.plot(X[:,0][Y==0],X[:,1][Y==0],'bo')
    
    plt.title("tolerance="+str(tolerance)+" ;C="+str(C)+"; gamma="+str(gamma)+" ;score: "+str(score))
    
def GenerateRandomBinaryClassificationDataSet(number_of_points=100,class_distribution=0.5):
    cl_dist_size=int(number_of_points*class_distribution)
    s1=cl_dist_size
    s2=number_of_points-s1
    x=np.random.rand(number_of_points)
    y=np.random.rand(number_of_points)
    c1=np.ones(s1)
    c2=np.zeros(s2)
    c=np.concatenate((c1,c2),axis=0)
    np.random.shuffle(c)
    
    xy=np.concatenate((x.reshape(len(x),1),y.reshape(len(y),1)),axis=1) 
    
    return xy,c

#______________Main_________________________________________________________

#Best dataset
# Load dataset from site
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)
dataset2=pd.get_dummies(dataset)
seed=7
dataset2=dataset2.sample(frac=1,random_state=seed)
#Irish setosa set
dataset3=dataset2.iloc[:]
dataset3=dataset3[['petal-length','petal-width','class_Iris-setosa']]
#pd.plotting.scatter_matrix(dataset3)

values=dataset3.values
xy=values[:,:-1]
c=values[:,-1]
NonLinearBinaryClassification2(xy,c,draw_region_step=0.05,alpha=0.1)
LinearBinaryClassification(xy,c,draw_region_step=0.05,alpha=0.1)

#___Dificult dataset_______________________________________________________________________
"""
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
dataset2=dataset[['capital-loss','capital-gain','class']]
#fazer scatter plot do seaborn
#sns.pairplot(dataset, hue="class")
#pd.plotting.scatter_matrix(dataset)
values=dataset2.values
#plt.figure()
#plt.plot(dataset[dataset['class'].str.contains('<=50')]['capital-loss'],dataset[dataset['class'].str.contains('<=50')]['capital-gain'],'bo')
#plt.xlabel('capital-loss')
#plt.ylabel('capital-gain')
#plt.plot(dataset[dataset['class'].str.contains('>50')]['capital-loss'],dataset[dataset['class'].str.contains('>50')]['capital-gain'],'ro')
values[:,-1]=(values==' >50K')[:,-1].astype(int)
values=values.astype(int)
xy=values[:,:-1]
c=values[:,-1]
#NonLinearBinaryClassification2(xy,c,draw_region_step=100)
LinearBinaryClassification(xy,c,draw_region_step=100,alpha=0.1)
"""
#____________Easier data set_______________________________________________
"""
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
seed=7
dataset=dataset.sample(frac=1,random_state=seed)
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

#Classification--------------------
#select best two features from scttter matrix
#sns.pairplot(dataset, hue="Diabetes")
#They all suck so lets try the best visualy
#Lets try X- Plasma-glucose-concentration Y- Diastolic-blood-pressure
xy=dataset[['Plasma-glucose-concentration','Diastolic-blood-pressure']].values
c=dataset['Diabetes'].values
#NonLinearBinaryClassification2(xy,c,draw_region_step=1,alpha=0.1)
LinearBinaryClassification(xy,c,draw_region_step=1,alpha=0.1)
"""

