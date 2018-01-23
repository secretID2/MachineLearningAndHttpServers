# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:56:59 2018

@author: lcristovao
"""

import bottle as bt
from bottle import get, template, run
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

users = []
log=[]
@get('/')
def index():
    return bt.static_file('chat.html',root='files/')

@get('/websocket', apply=[websocket])
def chat(ws):
    global log
    if(ws!=None):
        users.append(ws)
        #Send conversation to new client
        if(len(log)>0):
            for m in log:
                users[len(users)-1].send(m)
        ###################################
        #Receive and send messages
        while True:
            msg = ws.receive()
            print("received msg:",msg)
            if(msg is not None):
                log.append(msg)
            if msg is not None:
                for u in users:
                    try:
                        u.send(msg)
                    except:
                        print("error sending message")
                        pass
            else:
                break
        ##################################
        try:    
            users.remove(ws)
        except:
            print("error removing ws")
            pass
    else:
        print("Someone call /websocket without websocket")
        pass
    
#users = []
#log=[]
#@get('/')
#def index():
#    return bt.static_file('index.tpl',root='files/')
#
#@get('/websocket', apply=[websocket])
#def chat(ws):
#    global log
#    if(ws!=None):
#        users.append(ws)
#        #Send conversation to new client
#        if(len(log)>0):
#            for m in log:
#                users[len(users)-1].send(m)
#        ###################################
#        #Receive and send messages
#        while True:
#            msg = ws.receive()
#            print("received msg:",msg)
#            if(msg is not None):
#                log.append(msg)
#            if msg is not None:
#                for u in users:
#                    try:
#                        u.send(msg)
#                    except:
#                        print("error sending message")
#                        pass
#            else:
#                #if message receive equal to none
#                for u in users:
#                    
#                    try:
#                        u.send("$#please close")
#                    except:
#                        print("Error sending close websocket")
#                        pass
#                break
#        ##################################
#        try:    
#            users.remove(ws)
#        except:
#            print("error removing ws")
#            pass
#    else:
#        print("Someone call /websocket without websocket")
#        pass



run(host='127.0.0.1', port=8080, server=GeventWebSocketServer)
