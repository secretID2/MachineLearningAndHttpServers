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
import ML_MegaFunction as ml
import threading

import sqlite3


secret='some-secret-key'


clients={}
clients_upload_threads={}
clients_run_threads={}
class Client:
    
    
    dataset=None 
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.p=ml.Predictor()
        
    def Run(self):
        self.predictor=self.p.ReturnPredictor(self.dataset)
        
    def Loading(self):
        return self.p.loading
    
    def uploadFile(self,save_path,split_caracter=','):
        upload = bt.request.files.get('upload')
        name, ext = os.path.splitext(upload.filename)
    
        #save_path='files/Template'
        upload.save(save_path, overwrite=True) # appends upload.filename automatically
        print("\n\nbefore\n\n")
        self.dataset=pd.read_csv(save_path+upload.filename,delimiter=split_caracter )
        print("\n\nAfter\n\n")
        
        
    def getDatasetFromUrl(self,url,split_caracter=','):
        self.dataset=pd.read_csv(url,sep=split_caracter)
        
#For TXT file
#def getUsers():
#   data = np.genfromtxt('files/Users.txt',dtype=str, delimiter=',')
#   return data

#for db        
def getUsersDB():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT username, password FROM users")
    result = c.fetchall()
#    print(result[0][0])
    c.close()
    return result


def validate_user(secret):
    global clients
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            return True
    return False

#For txt db
#def check_login(username,password):
#    Users=getUsers()
#    for l in Users:
#        print(l)
#        if(username==l[0] and password==l[1]):
#            return True
#    return False

#For db
def check_login(username,password):
    Users=getUsersDB()
    for l in Users:
        print(l)
        if(username==l[0] and password==l[1]):
            return True
    return False
                 

#_______Main___________________________
#txt version##########################
#Users=getUsers()
#print(Users)
#########################################
    
#sql version###only use in case of db not created###################
#import CreateDB as db
#db.Start()
#db.DropTable()
#db.InsertNewuser('Luis','555')
#db.DeleteUser('Luis')    

###################################
    




        
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
            split = bt.request.forms.get('split')
            url=''
            url = bt.request.forms.get('url')
            print(split,url)
            if(url!=''):
                t=threading.Thread(target=clients[c].getDatasetFromUrl(url,split_caracter=split))
                clients_upload_threads[c]=t
                t.start()
            else:
                newpath = r'files/Template/'+c+'/' 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                t=threading.Thread(target=clients[c].uploadFile(newpath,split_caracter=split))
                clients_upload_threads[c]=t
                t.start()
                
            return bt.redirect('/LoadingPredictor.html')
        
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
            return clients[c].Loading()
    
    return "You are not logged in. Access denied."
        
@bt.get('/Prediction')
def Predictor():
     global clients
     global clients_run_threads
     for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #clients_run_threads[c].remove()
            client=clients[c]
            data=client.dataset
            ml_instance=client.p
            p=client.predictor
            data.iloc[:,:-1]=ml_instance.TurnDatasetToNumeric(data.iloc[:,:-1])
            data=data.sample(frac=1)
            n=10
            output="SCORE:"+str(ml_instance.score)+"<br><br>"
            output+="Original values:<br>"
            output+=np.array_str(data.iloc[:n,:].values)
            output+="<br><br>"
            for i in range(n):
                output+="<br>Prediction for previous line:<br>"+np.array_str(data.iloc[i,:-1].values)+"->"+np.array_str(p.predict(data.iloc[i:i+1,:-1].values))
            return output    

@bt.get('/<filepath:path>')
def server_static(filepath):
    
    if validate_user(secret='some-secret-key'):
        return bt.static_file(filepath, root='files/Template') 
    else:
        return "You are not logged in. Access denied."


bt.run(host='localhost', port=80, server='paste')
