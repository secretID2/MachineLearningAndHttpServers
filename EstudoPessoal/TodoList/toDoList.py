# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:49:54 2018

@author: lcristovao
"""


import sqlite3
import bottle as bt


#_______Main___________________
##################################################################################

#If DB already created comment the next part. 
#This will create a db named todo.db in the same work directory as this file

#import CreateDB
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

    if bt.request.GET.save:

        new = bt.request.GET.task.strip()
        status=bt.request.GET.status.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        
        if status == 'Open':
            status = 1
        else:
            status = 0

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new,status))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p><br><a href="/">Return</a>' % new_id
    else:
        return bt.template('new_task.tpl')
    
#@bt.route('/edit', method='GET')    
@bt.route('/edit/<no:int>', method='GET')
def edit_item(no):

    if bt.request.GET.save:
        edit = bt.request.GET.task.strip()
        status = bt.request.GET.status.strip()

        if status == 'Open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p><br><a href="/">Return</a>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task,status FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()
        task=cur_data[0]
        status=cur_data[1]
        print(cur_data)
        if status == 1 :
            _option='<option>Open</option><option>Close</option>'
        else:
            _option='<option>Close</option><option>Open</option>'
        
        

        return bt.template('edit_task', old=task,options=_option, no=no)



@bt.route('/delete')
def delete_page():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task,status FROM todo")
    result = c.fetchall()
    result2=[]
    for row in result:
        if row[2]==1:
            result2.append((row[0],row[1],'Open'))
        else:
            result2.append((row[0],row[1],'Close'))
        
    c.close()
    print(result2)
    output = bt.template('delete_table', rows=result2)
    return output


@bt.route('/delete/<no:int>', method='GET')
def delete(no):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("delete from todo where id LIKE ?", (str(no),))
    conn.commit()
    return '<p>The item number %s was successfully Deleted</p><br><a href="/delete">Return</a>' % no



bt.run(host='localhost', port=80, server='paste')