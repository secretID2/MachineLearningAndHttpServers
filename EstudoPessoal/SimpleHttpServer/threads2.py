# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:51:20 2018

@author: lcristovao
"""

from bottle import get, post, request, run, redirect
import threading

from multiprocessing import Queue
#from Queue import Queue, Empty

button_pressed = Queue()

@post('/button')
def action():
    button_pressed.put(1)  # can be any value really
    redirect("/button")

def method():
    while True:
        try:
            button_pressed.get_nowait()
        except Empty:
            # NOTE: if you don't do anything here, this thread
            # will consume a single CPU core
            pass
        else:
            print ("push recieved")
            
 
if __name__ == '__main__':
    threading.Thread(target=run, kwargs=dict(host='localhost', port=80)).start()
    method()
           
