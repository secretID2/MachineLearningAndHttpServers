# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 09:16:10 2018

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


@app.route('/')
def ret():
    
    try:
        return send_file('www/index.html')
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
    except Exception as e:
        return str(e)
'''
@app.route('/form', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)   
'''
"""
#This is for form request
@app.route('/Ola', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        X=request.form['x']
        Y=request.form['y']
        print(X,Y)
        #plt.figure()
        #plt.plot([0,1,2],[0,1,2])
        #plt.savefig('www/foo.png')
        
        return '''<img src="foo.png"> '''
       
    else:
        return '''<h>Invalid request!</h>'''

"""
@app.route('/',methods=['POST'])
def donothing():
    return '''Ola'''


#This is for param in post like xhttp.open("POST", "/Ola?"x="+x.value+"&y="+y.value+"", true);xhttp.send();
@app.route('/Ola', methods=['POST'])
def plot():
   # error = None
    if request.method == 'POST':
        X=request.args.get('x')
        Y=request.args.get('y')
        print(X,Y)
        #plt.figure()
        #plt.plot([0,1,2],[0,1,2])
        #plt.savefig('www/foo.png')
        
        return '''<img src="foo.png"> '''
      
       
    
@app.route('/<path:path>')
#@app.route('assets/images/<name>')
def ret2(path):
    #print(name)
    try:
        return send_file('www/'+path)
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
    except Exception as e:
        return str(e)    

    
#>>set FLASK_APP=FlaskServer.py

#>>flask run

#Working!!!
#Its multi thread !!!!
    