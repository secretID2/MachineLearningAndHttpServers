# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:59:21 2018

@author: lcristovao
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm
#Linear Classification function
def LinearBinaryClassification(points,class_table,C=100.0,gamma=0.7):
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
    xx = np.linspace(0, 1)
    yy = a * xx - (clf.intercept_[0]) / w[1]
    
    plt.figure()
    plt.plot(xx, yy, 'k-')
    plt.plot(xy[:,0][c==1],xy[:,1][c==1],'ro')
    plt.plot(xy[:,0][c==0],xy[:,1][c==0],'bo')
    #axes=plt.gca()
    #axes.fill_between(xx,yy,facecolor='blue',alpha=0.5)
    
    plt.title("C="+str(C)+" ;gamma="+str(gamma)+" ;score: "+str(score))
    h = .02  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = points[:, 0].min() -0.5, points[:, 0].max()+0.5 
    y_min, y_max = points[:,1].min()-0.5 , points[:,1].max()+0.5 
    xx2, yy2 = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    print(xx2)
    Z = clf.predict(np.c_[xx2.ravel(), yy2.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx2.shape)
    plt.plot(xx2[Z==1],yy2[Z==1],'r.',alpha=0.1)
    plt.plot(xx2[Z==0],yy2[Z==0],'b.',alpha=0.1)
    
#Linear Classification function
def NonLinearBinaryClassification(points,class_table,tolerance=0.001):
    clf = svm.NuSVC(tol=tolerance)
    X=points
    Y=class_table
    clf.fit(X,Y)
    score=clf.score(X, Y)
    print("Non linear score:",score)
    #Z=clf.decision_function(X)
    #print(Z)
    #Draw points of classification----------------------------------
    h = .02  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = Y.min() - 1, Y.max() + 1
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
    plt.plot(xx[Z==1],yy[Z==1],'r.',alpha=0.1)
    plt.plot(xx[Z==0],yy[Z==0],'b.',alpha=0.1)
    plt.plot(X[:,0][Y==1],X[:,1][Y==1],'ro')
    plt.plot(X[:,0][Y==0],X[:,1][Y==0],'bo')
    plt.title("tolerance="+str(tolerance)+" ;score: "+str(score))
    
#Linear Classification function2
def NonLinearBinaryClassification2(points,class_table,tolerance=0.001,C=1.0,gamma=0.7,choose_best=True):
    clf = svm.SVC(C=C,gamma=gamma,tol=tolerance)
    X=points
    Y=class_table
    clf.fit(X,Y)
    score=clf.score(X, Y)
    print("Non linear score:",score)
    #Z=clf.decision_function(X)
    #print(Z)
    #Draw points of classification----------------------------------
    h = .02  # step size in the mesh
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = Y.min() - 1, Y.max() + 1
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
    plt.plot(xx[Z==1],yy[Z==1],'r.',alpha=0.1)
    plt.plot(xx[Z==0],yy[Z==0],'b.',alpha=0.1)
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
    
#__________________Main____________________________________________
xy,c=GenerateRandomBinaryClassificationDataSet(30)   

LinearBinaryClassification(xy,c)
NonLinearBinaryClassification2(xy,c,C=1000,gamma=1)
