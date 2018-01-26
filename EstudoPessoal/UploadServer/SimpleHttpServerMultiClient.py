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
import sqlite3

secret='some-secret-key'



clients={}
clients_upload_threads={}
clients_delete_threads={}
class Client:
    
  
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    
    def uploadFile(self,save_path):
        upload = bt.request.files.get('upload')
        name, ext = os.path.splitext(upload.filename)
    
        #save_path='files/Template'
        upload.save(save_path, overwrite=True) # appends upload.filename automatically
        
    def deleteFile(self,path):
        try:
            os.remove(path)
            self.delete_file=True
        except:
           self.delete_file=False
        

def getUsers():
   data = np.genfromtxt('files/Users.txt',dtype=str, delimiter=',')
   return data

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

#for txt file
#def check_login(username,password):
#    Users=getUsers()
#    for l in Users:
#        print(l)
#        if(username==l[0] and password==l[1]):
#            return True
#    return False


#for txt file
def check_login(username,password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT username, password FROM users where username='"+username+"' and password='"+password+"'")
    result = c.fetchall()
    if result:
        return True
    else:
        return False

#_______Main___________________________

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
    return bt.template('index')
    
#@bt.get('/index.html') # or @route('/login')
#def ShowMainPage():
#    return bt.static_file("index.html",root="files/")    
    
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
        newpath = r'files/Template/'+username+'/' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        return bt.redirect('/restricted')
    else:
        return "<p>Login failed.</p>"

@bt.get('/restricted')
def restricted_area():
    global secret
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #valid user
            files_dir = 'files/Template/'+c
            user_files = os.listdir(files_dir)
            print(user_files)
            if user_files:
                return bt.template('user_files',rows=user_files,User=c)
            else:
                #Dont have files yet
                return bt.template('no_files_yet',User=c)
    
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
            upload = bt.request.files.get('upload')
            newpath = r'files/Template/'+c+'/' 
#            if not os.path.exists(newpath):
#                os.makedirs(newpath)
            t=threading.Thread(target=clients[c].uploadFile(newpath))
            clients_upload_threads[c]=t
            t.start()
            return "Hi "+c+", "+upload.filename+" was uploaded!<br><a href='/restricted'>Return to previouse page</a>"
        
    return "You are not logged in. Access denied."

@bt.get('/delete')
def delete():
    global secret
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #valid user
            files_dir = 'files/Template/'+c
            user_files = os.listdir(files_dir)
            print(user_files)
            if user_files:
                return bt.template('delete_files',rows=user_files,User=c)
            else:
                #Dont have files yet
                return "<h1>No Files Yet to Delete</h1><br><a href='restricted'>Return</a>"
    
    return "You are not logged in. Access denied."



@bt.get('/delete/<filename>',method='GET')
def erase(filename):
    global clients
    global secret
    global clients_upload_threads
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #valid user
            
            newpath = r'files/Template/'+c+'/'+filename 
#            if not os.path.exists(newpath):
#                os.makedirs(newpath)
            t=threading.Thread(target=clients[c].deleteFile(newpath))
            clients_delete_threads[c]=t
            t.start()
            if clients[c].delete_file:
                return "Hi "+c+", "+filename+" was Deleted!<br><a href='/delete'>Return to previouse page</a>"
            else:
                return "Hi "+c+", "+filename+" was  Not Deleted!<br><a href='/delete'>Return to previouse page</a>"
        
    return "You are not logged in. Access denied."


        
    

@bt.get('/<filepath:path>')
def server_static(filepath):
    global secret
    print(filepath)
    for c in clients:
        key = bt.request.get_cookie(clients[c].username, secret=secret)
        if key:
            #valid user
            return bt.static_file(filepath, root='files/Template/'+c,download=True) 
    else:
        return "You are not logged in. Access denied."


bt.run(host='localhost', port=80, server='paste')
