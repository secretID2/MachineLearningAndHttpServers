# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:56:59 2018

@author: lcristovao
"""

import bottle as bt
from bottle import get, run
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
import threading

users = []
log=[]
secret='nuncaVaodescobrr_ahah'
chatRooms={}
RoomUsers={}


class ChatRoom():
    
    def __init__(self,thread,Name):
        self.thread=thread

@get('/')
def index():
    return bt.static_file('index.html',root='files/')

@get('/loadRooms')
def LoadRooms():
    global chatRooms
    if(len(chatRooms)>0):
        out='<form action="/accessRoom" method="post">'
        for room_name in chatRooms:
            out+='<br><p>'+room_name+'</p><br>'
            out+='<input name="roomName" value="'+room_name+'" type="text" style="hidden"/>'
            out+='Password: <input name="password" type="password"  /><br>'
            out+='<input value="Enter" type="submit" /><br><br>'
        
        out+='</form>'
        return out
            
    else:
        return ''

@bt.post('/createChatRoom')
def createRoom():
    global secret
    global chatRooms
    global RoomUsers
    roomName = bt.request.forms.get('roomName')
    password = bt.request.forms.get('password')
    #print(roomName,password)
    chatRooms[roomName]=password
    users=[]
    RoomUsers[roomName]=users
    bt.response.set_cookie(roomName, password, secret=secret)
    return bt.redirect('/'+roomName)

@bt.post('/accessRoom')
def accessRoom():
    global secret
    global chatRooms
    roomName = bt.request.forms.get('roomName')
    password = bt.request.forms.get('password')
    print(roomName)
    if password==chatRooms[roomName]:
        bt.response.set_cookie(roomName, password, secret=secret)
        return bt.redirect('/'+roomName)
    else:
        return 'Not Allowed to access this Room!'
    
@bt.get('/<roomName>')
def enterRoom(roomName):
    #print(roomName)
    global secret
    global chatRooms
    for room_name in chatRooms:
        key = bt.request.get_cookie(room_name, secret=secret)
        #print(key)
        if key==chatRooms[room_name]:
            return bt.static_file('chat.html',root='files/')
    return 'Not Allowed in this Room!'

@get('/websocket', apply=[websocket])
def chat(ws):
    global log
    global secret
    global chatRooms
    global RoomUsers
#    print("Websocket")
        
    if(ws!=None):
        for room_name in chatRooms:
            key = bt.request.get_cookie(room_name, secret=secret)
            if key:
                break
            #if key==chatRooms[room_name]:
                #Valid user
                #print('pass here')
        users=RoomUsers[room_name]
        users.append(ws)
        RoomUsers[room_name]=users
                
                    
                    
        #Send conversation to new client
        
        ###################################
        #Receive and send messages
        while True:
            msg = ws.receive()
            print("received msg:",msg)
            
            if msg is not None:
                users= RoomUsers[room_name]
                for u in users:
                    try:
                        u.send(msg)
                    except:
                        print("error sending message")
                        pass
            else:
                break
            ##################################
       
    else:
        print("Someone call /websocket without websocket")
        pass
        



run(host='127.0.0.1', port=8080, server=GeventWebSocketServer)
