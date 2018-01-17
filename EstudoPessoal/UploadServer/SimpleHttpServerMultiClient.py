# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:42:39 2018

@author: lcristovao
"""



import bottle as bt
import pandas as pd
import numpy as np
import os
import time
#import ML_MegaFunction as ml
import threading

i=0
username=''
password=''
secret='some-secret-key'



clients={}
clients_upload_threads={}

class Client:
    
    #p=ml.Predictor()
    dataset=None 
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def Run(self):
        self.predictor=self.p.ReturnPredictor(self.dataset)
        
    def Loading(self):
        return self.p.loading
    
    def uploadFile(self,save_path):
        upload = bt.request.files.get('upload')
        name, ext = os.path.splitext(upload.filename)
    
        #save_path='files/Template'
        upload.save(save_path, overwrite=True) # appends upload.filename automatically
        

def getUsers():
   data = np.genfromtxt('files/Users.txt',dtype=str, delimiter=',')
   return data


def validate_user(secret):
    global clients
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            return True
    return False



#_______Main___________________________

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
    global clients
    global secret
    
    username = bt.request.forms.get('username')
    password = bt.request.forms.get('password')
    if check_login(username, password):
        client=Client(username,password)
        clients[username]=client
        bt.response.set_cookie(username, password, secret=secret)
        return bt.redirect('/restricted')
    else:
        return "<p>Login failed.</p>"

@bt.get('/restricted')
def restricted_area():
    global secret
    if validate_user(secret=secret):
        return bt.static_file("upload_dataset.html",root="files/Template")
    else:
        return "You are not logged in. Access denied."
    
    
    
@bt.get('/upload', method='POST')
def do_upload():
    global clients
    global secret
    global clients_upload_threads
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #valid user
            newpath = r'files/Template/'+c+'/' 
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            t=threading.Thread(target=clients[c].uploadFile(newpath))
            clients_upload_threads[c]=t
            t.start()
            return "Hi "+c+", YourFile was uploaded!"
        
    return "You are not logged in. Access denied."


@bt.get('/start')
def GetPredictor():
    global clients
    global clients_run_threads
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #Valid User
            #client_username=c #=clients[c].username #
            t=threading.Thread(target=clients[c].Run)
            clients_run_threads[c]=t
            t.start()
            return "Started the Proccess!"
            
    return "You are not logged in. Access denied."

@bt.get('/How_it_is_going')
def Loading():
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #Valid User
            #client_username=c #=clients[c].username #
#            if(clients[c].p.loading!="100%"):
#                return clients[c].p.loading
#            else:
#                return bt.redirect("/Predictor.html")
            return clients[c].p.loading
    
    return "You are not logged in. Access denied."
        
    

@bt.get('/<filepath:path>')
def server_static(filepath):
    
    if validate_user(secret='some-secret-key'):
        return bt.static_file(filepath, root='files/Template') 
    else:
        return "You are not logged in. Access denied."


bt.run(host='localhost', port=80, server='paste')
