# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:30:53 2018

@author: lcristovao
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import svm
"""
x=np.random.rand(10)
y=np.random.rand(10)
c1=np.ones(5)
c2=np.zeros(5)
c=np.concatenate((c1,c2),axis=0)
np.random.shuffle(c)

xy=np.concatenate((x.reshape(len(x),1),y.reshape(len(y),1)),axis=1)
xyc=np.concatenate((xy,c.reshape(10,1)),axis=1)
plt.plot(x[c==1],y[c==1],'ro')
plt.plot(x[c==0],y[c==0],'bo')
        
C = 1.0  # SVM regularization parameter
gamma=0.7
clf = svm.SVC(kernel = 'linear',  gamma=gamma, C=C )
clf.fit(xy, c)
print(clf.score(xy,c))

w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(0, 1)
yy = a * xx - (clf.intercept_[0]) / w[1]

plt.plot(xx, yy, 'k-')
"""

'''
plt.plot(x[c==1],y[c==1],'ro')
plt.plot(x[c==0],y[c==0],'bo')

plt.plot(line,sol,'g-')

reg = LogisticRegression(C=1e12, tol=1e-10)
reg.fit(xy,c)'''

'''
Non Linear Classifier Hard version
'''
"""
#Create linear interpolation of 500 points betwwen -3 and 3 
# xx is a matrix with shape = (500,500) where lines are 500 values from -3 to 3; all lines are the same
xx, yy = np.meshgrid(np.linspace(-3, 3, 500),
                     np.linspace(-3, 3, 500))
np.random.seed(0)
#Create matrix with 300 lines and 2 columns of random values between 0 and 1
X = np.random.randn(300, 2)
#print(X)
#Do logical XOR (true when different) between the two columns of X when the columsn are bigger than 1
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
#print(Y)
#for each point in X, Y gives a classification
# fit the model
clf = svm.NuSVC()
clf.fit(X, Y)

#np.c_ function is very usefull it turns for instance two arrays like: [,,,] in a matrix with two columns 
# plot the decision function for each datapoint on the grid
# decision function gives: decision_function(X)	Distance of the samples X to the separating hyperplane.
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto',
           origin='lower', cmap=plt.cm.PuOr_r)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2,
                       linetypes='--')
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y, cmap=plt.cm.Paired,
            edgecolors='k')
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
print('Predicsts this data set with accuracy of :',clf.score(X,Y))
"""
'''
Non Linear Classifier Easy version
'''

#Generate Data points
#-------------------------------------------------------------------
x=np.random.rand(10)
y=np.random.rand(10)
c1=np.ones(5)
c2=np.zeros(5)
c=np.concatenate((c1,c2),axis=0)
np.random.shuffle(c)

xy=np.concatenate((x.reshape(len(x),1),y.reshape(len(y),1)),axis=1)
xyc=np.concatenate((xy,c.reshape(10,1)),axis=1)

#------------------------------------------------------------------------
#Linear Classifier
C = 100.0  # SVM regularization parameter
gamma=0.7
clf = svm.SVC(kernel = 'linear',  gamma=gamma, C=C )
clf.fit(xy, c)
score=clf.score(xy,c)
print("Linear Score:",score)

w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(0, 1)
yy = a * xx - (clf.intercept_[0]) / w[1]

plt.figure(0)
plt.plot(xx, yy, 'k-')
plt.plot(x[c==1],y[c==1],'ro')
plt.plot(x[c==0],y[c==0],'bo')
plt.title("C="+str(C)+" ;gamma="+str(gamma)+" ;score: "+str(score))
#--------------------------------------------------------
#Non Linear Classifier
# fit the model
tol=0.001
clf = svm.NuSVC(tol=tol)
X=xyc[:,:2]
Y=xyc[:,2]
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
#--------------------------------------------------------------
plt.figure(1)
plt.contour(xx, yy, Z, cmap=plt.cm.Paired)


plt.plot(x[c==1],y[c==1],'ro')
plt.plot(x[c==0],y[c==0],'bo')
plt.title("tolerance="+str(tol)+" ;score: "+str(score))