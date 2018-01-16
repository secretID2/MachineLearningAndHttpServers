# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:42:39 2018

@author: lcristovao
"""




import bottle as bt
import pandas as pd
import numpy as np


username=''
password=''

def getUsers():
   data = np.genfromtxt('files/Users.txt',dtype=str, delimiter=',')
   return data

Users=getUsers()
print(Users)


def check_login(username,password):
    Users=getUsers()
    for l in Users:
        print(l)
        if(username==l[0] and password==l[1]):
            return True
    return False
                 
        
@bt.route('/') # or @route('/login')
def init():
    return bt.redirect("/index.html")
    
@bt.get('/index.html') # or @route('/login')
def ShowMainPage():
    return bt.static_file("index.html",root="files/")    
    
@bt.post('/login')
def do_login():
    username = bt.request.forms.get('username')
    password = bt.request.forms.get('password')
    if check_login(username, password):
        bt.response.set_cookie("account", username+' '+password, secret='some-secret-key')
        return bt.redirect('/restricted')
    else:
        return "<p>Login failed.</p>"

@bt.get('/restricted')
def restricted_area():
    key = bt.request.get_cookie("account", secret='some-secret-key')
   # print(key)
    #print(key[0],key[1])
    #key=str(key)
    #key=key.split(' ')
    #print(key) #works!
    #print(key2)
    
    #if check_login(key[0], key[1]):
    if key:
        return bt.static_file("index.html",root="files/Template")
    else:
        return "You are not logged in. Access denied."

@bt.get('/<filepath:path>')
def server_static(filepath):
    key = bt.request.get_cookie("account", secret='some-secret-key')
    #key=key.split(' ')
    
    if key:
        return bt.static_file(filepath, root='files/Template') 
    else:
        return "You are not logged in. Access denied."


bt.run(host='localhost', port=80, server='paste')
