# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:39:15 2018

@author: lcristovao
"""

import bottle as bt
import pandas as pd
import numpy as np
#@bt.route('/')
#@bt.route('/hello/<name>')
#def greet(name='Stranger'):
#    return bt.template('Hello {{name}}, how are you?', name=name)

username=''
password=''

def getUsers():
   data = np.genfromtxt('files/Users.txt',dtype=str, delimiter=',')
   return data

Users=getUsers()
print(Users)
#@bt.route('/') # or @route('/login')
#def init():
#    return bt.redirect("/index.html")
#    
#@bt.get('/index.html') # or @route('/login')
#def ShowMainPage():
#    return bt.static_file("index.html",root="files/")    
#    
#def check_login(username,password):
#    if(username=='Tiago' and password=='Ola'):
#        return True
#    else:
#        return False
##
#@bt.post('/login') # or @route('/login', method='POST')
#def do_login():
#    username = bt.request.forms.get('username')
#    password = bt.request.forms.get('password')
#    if check_login(username, password):
#        return bt.static_file('/index.html', root='files/Template')
#    else:
#        return "<h2>Login failed.</h2>"


   
#@bt.get('/<filepath:path>')
#def server_static(filepath):
#    return bt.static_file(filepath, root='files/Template')    


def check_login(username,password):
    Users=getUsers()
    for l in Users:
        print(l)
        if(username==l[0] and password==l[1]):
            return True
    return False
        
#@bt.get('/') # or @route('/login')
#def init():
#    return bt.redirect("/index.html")
#    
#@bt.get('/index.html') # or @route('/login')
#def ShowMainPage():
#    return bt.static_file("index.html",root="files/")   
            
        
@bt.get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
    
@bt.post('/login')
def do_login():
    username = bt.request.forms.get('username')
    password = bt.request.forms.get('password')
    if check_login(username, password):
        bt.response.set_cookie("account", username, secret='some-secret-key')
        return bt.template("<p>Welcome {{name}}! You are now logged in.</p><br><a href='/restricted'>localhost/restricted</a>", name=username)
    else:
        return "<p>Login failed.</p>"

@bt.get('/restricted')
def restricted_area():
    username = bt.request.get_cookie("account", secret='some-secret-key')
    if username:
        return bt.template("Hello {{name}}. Welcome back.", name=username)
    else:
        return "You are not logged in. Access denied."


bt.run(host='localhost', port=80)
