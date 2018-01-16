# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:52:35 2018

@author: lcristovao
"""

from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
from ML_MegaFunction import ReturnPredictor 
#from DrawMegaFunction import ReturnPredictor 
import pandas as pd
import os
app = Flask(__name__)


#predictor=None
#
#def createHTML(cols):
#    s+='<html>'
#    s+='<body>'
#    s+='<form>'
#    
#
#def showNewHTML():
#    global predictor
#    files=os.listdir('files/')
#    dataset=pd.read_csv(files[0])
#    predictor=ReturnPredictor(dataset)
#    

@app.route('/')
def upload_file():
   return send_file("www/index.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
  
@app.route('/<path:path>')
#@app.route('assets/images/<name>')
def ret2(path):
    #print(name)
    try:
        return send_file('www/'+path)
        #return send_file('C:/Users/lcristovao/Desktop/Work/EstudoPessoal/Flask/'+name, attachment_filename=name)
    except Exception as e:
        return str(e) 
#if __name__ == '__main__':
   #app.run(debug = True)
   
   