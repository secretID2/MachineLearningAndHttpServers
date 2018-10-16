# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:41:11 2018

@author: lcristovao
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:48:54 2018

@author: lcristovao
"""


from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import send_file
from flask import redirect

#from ML_MegaFunction import ReturnPredictor 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)

#from app import routes



"""
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

best_model=ReturnPredictor(dataset)

values=dataset.values
np.random.shuffle(values)
#Number of tests
n=10
print("Original values:\n",values[:n,:])
for i in range(n):
    print("Prediction for previous line:\n",values[i,:-1],"->",best_model.predict(values[:n,:-1])[i])

"""


#from app import app

@app.route('/')
def ret():
    
    try:
        return send_file('www/index.html')
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
    except Exception as e:
        return str(e)

@app.route('/Ola')
def ret3():
    
    try:
        plt.figure()
        plt.plot([0,1,2],[0,1,2])
        plt.savefig('www/foo.png')
        
        return '''<img src="foo.png"> '''
        #return '''<img src="assets/images/logo.png">'''
    except Exception as e:
        return str(e)    
    
@app.route('/<path:path>')
#@app.route('assets/images/<name>')
def ret2(path):
    #print(name)
    try:
        return send_file('www/'+path)
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
    except Exception as e:
        return str(e)    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)    
#>>set FLASK_APP=FlaskServer.py

#>>flask run

#Working!!!
#Its multi thread !!!!
    