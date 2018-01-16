# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:28:31 2018

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


#_________________Main_____________________________
"""    
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
"""
#----------------------Start here-----------------------------------
#Best dataset
# Load dataset from site
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

#Shuffle data
seed=7
dataset=dataset.sample(frac=1,random_state=seed)

data=dataset.iloc[:,:-1]
class_data=dataset.iloc[:,-1]

#If there is any data to numeric data
#data_shape=data.shape
more_than_one_class=False
class_data_shape=class_data.shape

data=pd.get_dummies(data)

    
class_data=pd.get_dummies(class_data)
if(class_data.shape.all()!=class_data_shape.all()):
    more_than_one_class=True
    
    