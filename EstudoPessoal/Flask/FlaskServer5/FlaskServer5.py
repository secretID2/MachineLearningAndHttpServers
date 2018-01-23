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
import os

#from ML_MegaFunction import ReturnPredictor 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
app = Flask(__name__)

i=0
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

#This is for form request
@app.route('/Ola', methods=['GET'])
def login():
    #error = None
    global i
    print(i)
    i+=1
    try:
        os.remove('www/foo'+str(i-1)+'.png')
    except OSError:
        pass
    print(i)
      
    
    
    output=''
    if request.method == 'GET':
        X=request.args.get('x')
        Y=request.args.get('y')
        print(X,Y)
        X=X.split(',')
        Y=Y.split(',')
        for i in range(len(X)):
            X[i]=float(X[i])
            Y[i]=float(Y[i])
        plt.figure()
        plt.plot(X,Y)
        plt.savefig('www/foo'+str(i)+'.png')
        plt.close()
        
        
        
       
        output+='<div class="login100-pic js-tilt" id="drop_image" data-tilt>'
        output+='<img  src="foo'+str(i)+'.png">'
        output+='</div>'
        
       
        return output  
        '''
                <div class="login100-pic js-tilt" id="drop_image" data-tilt>
					<img  src="foo.png">
				</div>
                '''  
                
       
    else:
        return '''<h>Invalid request!</h>'''




    
@app.route('/<path:path>')
#@app.route('assets/images/<name>')
def ret2(path):
    #print(name)
    try:
        return send_file('www/'+path)
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
    except Exception as e:
        return str(e)    

if __name__ == '__main__':
   app.run(debug = True)#localhos:5000
    
#>>set FLASK_APP=FlaskServer.py

#>>flask run

#Working!!!
#Its multi thread !!!!
    