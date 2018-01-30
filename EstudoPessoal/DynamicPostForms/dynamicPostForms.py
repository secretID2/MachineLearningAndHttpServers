# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:48:05 2018

@author: lcristovao
"""

import bottle as bt
import pandas as pd
import numpy as np




@bt.get('/')
#@bt.get('/index.html') # or @route('/login')
def ShowMainPage():
    return bt.static_file("index.html",root='files/')    

@bt.get('/nvalues',method='POST')
def retDynamicForm():
    try:
        number=bt.request.forms.get('number')
        print("Numbero->",number)
    except:
        print("error no get")
    
    out='<table id="input">'
    input_rows=['Attributes','Values']
    for row in input_rows:
        out+='<tr><th>'+str(row)+'</th></tr>'
        out+='<tr name="'+str(row)+'">'
        for i in range (int(number)):
            out+='<th><input name="'+str(row)+'" value="'+str(i)+'"></th>'
        out+='</tr>'
    out+='</table>'
    return out


@bt.get('/Sum',method='POST')
def SUM():
    values=[]
    i=0
    while(True):
        if(bt.request.forms.get(str(i))!=None):
            print("sum values:",bt.request.forms.get(str(i)))
            values.append(bt.request.forms.get(str(i)))
            
        else:
            print("All variables were obtain")
            break
        i+=1
    Sum=0     
    for v in values:
        Sum+=int(v)
    print("final sum:",Sum)
    return str(Sum)



bt.run(host='localhost', port=80, server='paste')