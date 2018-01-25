# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:49:54 2018

@author: lcristovao
"""

import CreateDB
import sqlite3
import bottle as bt


#_______Main___________________
##################################################################################
#If DB already created comment the next part. 
#This will create a db named todo.db in the same work directory as this file

#CreateDB.Run()
##################################################################################




@bt.get('/')
@bt.get('/open')
def open_page():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status=1")
    result = c.fetchall()
    print(result[0][0])
    c.close()
    output = bt.template('make_table', rows=result,Open="Open")
    return output

@bt.get('/close')
def close_page():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status=0")
    result = c.fetchall()
    print(result[0][0])
    c.close()
    output = bt.template('make_table', rows=result,Open="Close")
    return output

#I think get and route are the same??
@bt.route('/new', method='GET')
def new_item():

    new = bt.request.GET.task.strip()
    status=bt.request.GET.status.strip()
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, status))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id




bt.run(host='localhost', port=80, server='paste')