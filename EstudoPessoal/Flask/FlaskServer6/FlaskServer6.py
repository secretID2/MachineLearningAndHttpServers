# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:52:35 2018

@author: lcristovao
"""

from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return send_file("www/index.html")
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
#if __name__ == '__main__':
   #app.run(debug = True)