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
def start_page():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status=0")
    result = c.fetchall()
    print(result[0][0])
    c.close()
    output = bt.template('make_table', rows=result)
    return output




bt.run(host='localhost', port=80, server='paste')