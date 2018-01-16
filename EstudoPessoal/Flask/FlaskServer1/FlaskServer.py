# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 17:42:57 2018

@author: lcristovao
"""


from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import send_file
app = Flask(__name__)

#from app import routes
'''
The script above simply creates the application object as an instance of class Flask imported from the flask package. The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used. Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files, which I will cover in Chapter 2. For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way. The application then imports the routes module, which doesn't exist yet.
'''

#from app import app

@app.route('/')
def ret():
    
    try:
        return send_file('www/index.html')
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
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

    
#>>set FLASK_APP=FlaskServer.py

#>>flask run

#Working!!!
#Its multi thread !!!!
    