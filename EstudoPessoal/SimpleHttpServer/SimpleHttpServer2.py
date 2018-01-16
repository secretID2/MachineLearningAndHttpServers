# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:25:52 2018

@author: lcristovao
"""

import bottle as bt

#@bt.route('/')
#@bt.route('/hello/<name>')
#def greet(name='Stranger'):
#    return bt.template('Hello {{name}}, how are you?', name=name)

username=''
password=''


@bt.route('/') # or @route('/login')
def init():
    return bt.redirect("/index.html")
    
@bt.get('/index.html') # or @route('/login')
def ShowMainPage():
    return bt.static_file("index.html",root="files/")    
    
def check_login(username,password):
    if(username=='Tiago' and password=='Ola'):
        return True
    else:
        return False
#
@bt.post('/login') # or @route('/login', method='POST')
def do_login():
    username = bt.request.forms.get('username')
    password = bt.request.forms.get('password')
    if check_login(username, password):
        return bt.static_file('/index.html', root='files/Template')
    else:
        return "<h2>Login failed.</h2>"
               
    
#from bottle import get, post, request # or route
##
#@bt.get('/login') # or @route('/login')
#def login():
#     return bt.static_file('/index.html', root='files')
#
#@bt.post('/login') # or @route('/login', method='POST')
#def do_login():
#    username = bt.request.forms.get('username')
#    password = bt.request.forms.get('password')
#    if check_login(username, password):
#        return bt.static_file('/index.html', root='files/Template')
#    else:
#        return '<h2>Wrong pass or username!</h2>'


        
#        
#@bt.get('/<path>')
#def server_static(path):
#    return path
##    print(path)
##    filename=path.split('/')[-1]
##    path2=path.split('/')[:-1]
##    return bt.static_file(filename, root=path2)

bt.run(host='localhost', port=80)