# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:09:46 2018

@author: lcristovao
"""


from sklearn.linear_model import LogisticRegression
from sklearn import svm
#import seaborn as sns
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
#from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn import datasets
from sklearn import model_selection
#from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB



def make_meshgrid(x, y, step_percentage=.01):
    """Create a mesh of points to plot in

    Parameters
    ----------
    x: data to base x-axis meshgrid on
    y: data to base y-axis meshgrid on
    h: stepsize for meshgrid, optional

    Returns
    -------
    xx, yy : ndarray
    """
    
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    
    hx=step_percentage*(abs(x_max-x_min))
    hy=step_percentage*(abs(y_max-y_min))
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, hx),
                         np.arange(y_min, y_max, hy))
    return xx, yy


def plot_contours(ax, clf, xx, yy, **params):
    """Plot the decision boundaries for a classifier.

    Parameters
    ----------
    ax: matplotlib axes object
    clf: a classifier
    xx: meshgrid ndarray
    yy: meshgrid ndarray
    params: dictionary of params to pass to contourf, optional
    """
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def categoricalToNumeric(array):
    le = preprocessing.LabelEncoder()
    le.fit(array)
    return le.transform(array)

def TurnDatasetToNumeric(dataset):
    
    for i in range(len(dataset.dtypes)):
        if dataset.dtypes[i]==object:
            v=dataset.iloc[:,i].values
            v=categoricalToNumeric(v)
            dataset.iloc[:,i]=v
    
    return dataset

def DrawClassification(features,_class,predictor,predictor_name):
    X=features
    Y=_class
    xx,yy=make_meshgrid(X[:,0],X[:,1])
    Z = predictor.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(7,5))
    plt.contourf(xx, yy, Z,cmap=plt.cm.coolwarm,edgecolors='k')
    plt.scatter(X[:,0], X[:,1], c=Y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    plt.title('score='+str(predictor.score(X,Y))+'; Chosen model='+predictor_name)

def ReturnDatasetBestFeatures(dataset):
    values=dataset.values
    X=values[:,:-1]
    Y=values[:,-1]
    selector = SelectKBest(f_classif, k=2)
    selector.fit(X,Y)
    columns=selector.get_support(indices=True)

    return pd.concat([dataset.iloc[:,[columns[0],columns[1]]],dataset.iloc[:,-1]],axis=1)
    
def ReturnMatchColumnsIndex(m1,m2):
    M=np.array([])
    m=np.array([])
    columns=[]
    if(m1.shape[1]>=m2.shape[1]):
        M=m1
        m=m2
    else:
        M=m2
        m=m1
        
    for j in range(m.shape[1]):
        for i in range(M.shape[1]):
            b=(M[:,i]==m[:,j])
            print(len(b),b.sum())
            if(len(b)==b.sum()):
                columns.append(i)
        
    return columns

#def MLDrawfunction(dataset,random_state=7):
    #Shuffle data
    #seed=7
   #dataset=dataset.sample(frac=1,random_state=seed)



#def ReturnPredictor(dataset,true_test_size=0.5,validation_size=0.20,cross_val_splits=10,random_state=7):
#    '''
#    dataset must have this format: Atribute1|Atribute2|...|Class|
#    '''
#    seed=random_state
#    class_index=dataset.shape[1]-1
#    #Shuffle data
#    dataset=dataset.sample(frac=1,random_state=seed)
#    
#    #Divide dataset in two parts
#    size=dataset.shape[0]
#    half=int(size*true_test_size)
#    #Division
#    TrainValSet=dataset.iloc[:half]
#    TrueErrorSet=dataset.iloc[half:]
#	#Train Validation Part-----------------------------------------------------
#    array = TrainValSet.values
#    X=array[:,0:class_index]
#    Y = array[:,class_index]
#    #print(Y)
#    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
#	
#    scoring = 'accuracy'
#
#    # Spot Check Algorithms
#    models = []
#    models.append(('LR', LogisticRegression()))
#    models.append(('LDA', LinearDiscriminantAnalysis()))
#    models.append(('KNN', KNeighborsClassifier()))
#    models.append(('CART', DecisionTreeClassifier()))
#    models.append(('NB', GaussianNB()))
#    models.append(('SVM', svm.SVC()))
#    # evaluate each model in turn
#    mean_results=[]
#    for name, model in models:
#        kfold = model_selection.KFold(n_splits=cross_val_splits, random_state=seed)
#        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
#        mean_results.append(cv_results.mean())
#        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#        print(msg)
#
#    mean_results=np.array(mean_results)	
#    best_model_index=mean_results.argmax()
#    best_model=models[best_model_index][1]
#    print("Best Model: ",models[best_model_index][0])
#	
#    ##Fit best model In Training_validation dataset
#    finalArray=TrainValSet.values
#    finalX=finalArray[:,:class_index]
#    finalY=finalArray[:,class_index] 
#    best_model.fit(finalX,finalY)
#	
#    Truearray=TrueErrorSet.values
#    TrueX=Truearray[:,0:class_index]
#    TrueY=Truearray[:,class_index]
#    predictions = best_model.predict(TrueX)
#    print('\n\nTrue Score: ',accuracy_score(TrueY, predictions))
#    print('Cunfusuion Matrix \n',confusion_matrix(TrueY, predictions))
#    #print(classification_report(TrueY, predictions))
#
#    FFArray=dataset.values
#    FFX=FFArray[:,0:class_index]
#    FFY=FFArray[:,class_index]
#    predictions = best_model.predict(FFX)
#    print('\n\nFinal Final Score: ',accuracy_score(FFY, predictions))
#    print('Confusion matrix\n',confusion_matrix(FFY, predictions))
#    return best_model
   
def ReturnPredictor(dataset,true_test_size=0.5,validation_size=0.20,cross_val_splits=10,random_state=7, SVM_data_size=1000):
    '''
    dataset must have this format: Atribute1|Atribute2|...|Class|
    '''
    seed=random_state
    
    #Turn all columns that have string categorical values to numbers
    dataset=TurnDatasetToNumeric(dataset)
    
    #Select Best Features----------------
    dataset=ReturnDatasetBestFeatures(dataset)
    #Select Best Features----------------
    
    
    #get class index column
    class_index=dataset.shape[1]-1
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
    X=array[:,0:class_index]
    Y = array[:,class_index]
    #print(Y)
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
	
    scoring = 'accuracy'

    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    if(dataset.shape[0]<SVM_data_size):
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
    best_model_name=models[best_model_index][0]
    print("Best Model: ",best_model_name)
	
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
    print('Cunfusion Matrix \n',confusion_matrix(TrueY, predictions))
    #print(classification_report(TrueY, predictions))

    FFArray=dataset.values
    FFX=FFArray[:,0:class_index]
    FFY=FFArray[:,class_index]
    predictions = best_model.predict(FFX)
    print('\n\n(All dataset test) Final Score: ',accuracy_score(FFY, predictions))
    print('Confusion matrix\n',confusion_matrix(FFY, predictions))
    
    DrawClassification(FFX,FFY,best_model,best_model_name)
    
    
    return best_model


#___________Main____________________________________________________
print(__name__)






# Load dataset from site
#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#dataset = pd.read_csv(url, names=names)
#
#
#
#ReturnPredictor(dataset)







#Shuffle data
#seed=7
#dataset=dataset.sample(frac=1,random_state=seed)
#
##X_new = SelectKBest(f_classif, k=2).fit_transform(X, y)
#
##Make predictor
#C=1
#gamma=0.2
#tolerance=0.01
##predictor=svm.SVC(C=C,gamma=gamma,tol=tolerance)
##predictor=LinearDiscriminantAnalysis()
#predictor=KNeighborsClassifier()
##Turn any string column to numeric
#
#for i in range(len(dataset.dtypes)):
#    if dataset.dtypes[i]==object:
#        v=dataset.iloc[:,i].values
#        v=categoricalToNumeric(v)
#        dataset.iloc[:,i]=v
#    
#    
#values=dataset.values    
#X=values[:,:-1]
#Y=values[:,-1]
#
##print(values)
#
##Y=categoricalToNumeric(Y)
##print(Y)
#
##Select best two features
##X = SelectKBest(f_classif, k=2).fit_transform(X, Y)
#
##selector = SelectKBest(f_classif, k=2)
##selector.fit(X,Y)
##columns=selector.get_support(indices=True)
#
#
##columns=ReturnMatchColumnsIndex(X,values)
##print(columns)
##print(pd.concat([dataset.iloc[:,[columns[0],columns[1]]],dataset.iloc[:,-1]],axis=1))
#
#
#
##predictor.fit(X,Y)
##predictor.score(X,Y)
##
##xx,yy=make_meshgrid(X[:,0],X[:,1])
##Z = predictor.predict(np.c_[xx.ravel(), yy.ravel()])
##Z = Z.reshape(xx.shape)
##plt.figure(figsize=(7,5))
##plt.contourf(xx, yy, Z,cmap=plt.cm.coolwarm,edgecolors='k')
##plt.scatter(X[:,0], X[:,1], c=Y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
##plt.title('C='+str(C)+'; gamma='+str(gamma)+'; score='+str(predictor.score(X,Y)))
###Z = predictor.predict(np.c_[xx.ravel(), yy.ravel()])
##    
### Put the result into a color plot
###Z = Z.reshape(xx.shape)