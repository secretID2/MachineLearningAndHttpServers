# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:52:43 2018

@author: lcristovao
"""

import sqlite3

def Start():
    conn = sqlite3.connect('users.db') # Warning: This file is created in the current directory
    conn.execute("CREATE TABLE users (username char(100) PRIMARY KEY, password char(100) NOT NULL)")
    conn.execute("INSERT INTO users (username,password) VALUES ('Tiago','Ola')")
    conn.execute("INSERT INTO users (username,password) VALUES ('Pedro','123')")
    conn.execute("INSERT INTO users (username,password) VALUES ('Joao','333')")
    conn.commit()
    
def DropTable():
    conn = sqlite3.connect('users.db') # Warning: This file is created in the current directory
    conn.execute("Drop TABLE users ")
    conn.commit()

def InsertNewuser(username,password):
    conn = sqlite3.connect('users.db')
    conn.execute("INSERT INTO users (username,password) VALUES ('"+username+"','"+password+"')")
    conn.commit()

def DeleteUser(username):
        conn = sqlite3.connect('users.db')
        conn.execute("delete from users where username='"+username+"'")
        conn.commit()        

print(__name__)
        
        
#Start()