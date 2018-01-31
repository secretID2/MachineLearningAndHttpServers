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
import datetime
import encryption

#users = []
#log=[]
secret='nuncaVaodescobrr_ahah'
chatRooms={}
RoomUsers={}
RoomLog={}
encry=encryption.Encryption()

class ChatRoom():
    
    def __init__(self,thread,Name):
        self.thread=thread

@get('/')
def index():
    return bt.static_file('index.html',root='files/')

@get('/favicon.ico')
def retfavicon():
    return bt.static_file('straight_lines1.jpg',root='files/')

@get('/loadRooms')
def LoadRooms():
    global chatRooms
    out=""
    if(len(chatRooms)>0):
       
        for room_name in chatRooms:
            out+='<form action="/accessRoom/'+room_name+'" method="post">'
            out+='<br><p>'+room_name+'</p><br>'
            #out+='<input name="roomName" value="'+room_name+'" type="text" style="hidden"/>'
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
    global RoomLog
    roomName = bt.request.forms.get('roomName')
    password = bt.request.forms.get('password')
    #print(roomName,password)
    chatRooms[roomName]=password
    users={}
    RoomUsers[roomName]=users
    #Initialization of room log
    log=[]
    RoomLog[roomName]=log
    
    ts = datetime.datetime.now()+datetime.timedelta(seconds=1)
    encrypt_pass=encry.encrypt(password)
    bt.response.set_cookie(roomName, encrypt_pass,path='/',expires=ts)
    #bt.response.set_cookie(roomName, password,path='/',expires=ts, secret=secret)
    #bt.response.set_cookie(roomName, password,path='/websocket',expires=ts, secret=secret)
    return bt.redirect('/'+roomName)

@bt.post('/accessRoom/<roomName>')
def accessRoom(roomName):
    global secret
    global chatRooms
    #roomName = bt.request.forms.get('roomName')
    password = bt.request.forms.get('password')
    
   #print(roomName)
    #print(password==chatRooms[roomName])
    if password==chatRooms[roomName]:
        ts = datetime.datetime.now()+datetime.timedelta(seconds=1)
        encrypt_pass=encry.encrypt(password)
        bt.response.set_cookie(roomName, encrypt_pass,path='/',expires=ts)
        #bt.response.set_cookie(roomName, password,path='/',expires=ts, secret=secret)
        #bt.response.set_cookie(roomName, password,path='/websocket',expires=ts, secret=secret)
        return bt.redirect('/'+roomName)
    else:
        return 'Not Allowed to access this Room!'
    
@bt.get('/<roomName>')
def enterRoom(roomName):
    #print(roomName)
    global secret
    global chatRooms

    key = bt.request.get_cookie(roomName)
    #print(key)
    password=encry.decrypt(key)
    #print(password)
    if password==chatRooms[roomName]:
        #ts = datetime.datetime.now()+datetime.timedelta(minutes=1)
        #bt.response.set_cookie(roomName, key,path='/',expires=ts, secret=secret)
        return bt.static_file('chat.html',root='files/')
    return 'Not Allowed in this Room!'


def getRoomName(msg):
    cookie=msg.split(';')[0]
    roomName=cookie.split('=')[0]
    return roomName


def getPassword(msg):
    cookie=msg.split(';')[0]
    password=cookie.split('=')[1]
    return password

def getMsg(msg):
    menssage=msg.split(';')[1]
    return menssage



def ValidateWebsocketConnection(msg):
    global chatRooms
    cookie=msg.split(';')[0]
    roomName=cookie.split('=')[0]
    password=cookie.split('=')[1]
    #print("\n\n",roomName,password)
    password=encry.decrypt(password)
    if password==chatRooms[roomName]:
        return True
    else:
        return False


def SeeWhoDisconnected(ws):
    global RoomUsers
    for room in RoomUsers:
        users=RoomUsers[room]
        try:
            print("Deleting",users[ws])
            del users[ws]
            break
        except:
            print("wrong room!->",room)
            continue
            


@get('/websocket', apply=[websocket])
def chat(ws):
    global log
    global secret
    global chatRooms
    global RoomUsers
    global RoomLog
#    print("Websocket")
       
    if(ws!=None):
       
        first_time=1       
        #Send conversation to new client
        
        ###################################
        #Receive and send messages
        while True:
            msg = ws.receive()
            print("received msg:",msg)
            if msg is not None:
                #Validate User
                
                
#               if(ValidateWebsocketConnection(msg)):
                room_name=getRoomName(msg)
                users= RoomUsers[room_name]
                RoomUsers[room_name]=users
                msg=getMsg(msg)
                #First time user enters it receives log and is added to room users
                if first_time==1:
                    
                    users[ws]=ws
                    room_log=RoomLog[room_name]
                    #if is not empty
                    if room_log:
                        for log in room_log:
                            try:
                                users[ws].send(log)
                            except:
                                print("Error sending log")
                    first_time+=1
                #After first time we need to regist the conversation    
                else:
                    log=RoomLog[room_name]
                    log.append(msg)
                    RoomLog[room_name]=log
                
                for u in users:
                    try:
                        users[u].send(msg)
                    except:
                        print("error sending message")
                        pass
#                else:
#                    print('User not valid to use websocket')

            else:
                #Close websocket
                print("Closing",ws)
                SeeWhoDisconnected(ws)
                break
            ##################################
       
    else:
        print("Someone call /websocket without websocket")
        pass
        



run(host='127.0.0.1', port=8080, server=GeventWebSocketServer)
