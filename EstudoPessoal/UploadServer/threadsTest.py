# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:21:43 2018

@author: lcristovao
"""

import threading

class X:
    index=0
    
    def __init__(self,_id,max_num,step):
        self.id=_id
        self.max=max_num
        self.step=step
        
    def Run(self):
        for i in range (0,self.max,self.step):
            self.index=i
            print("Hi I am",self.id,"My index is",self.index)
            
     



#____________main_____________________________________
        
x1=X(1,100,1)
x2=X(2,200,2)

hashmap ={}
hashmap[1]=x1
hashmap[2]=x2
threads=[]



#for x in hashmap:
#    print(hashmap[x].id)


for x in hashmap:
    
    t=threading.Thread(target=hashmap[x].Run)
    threads.append(t)

for th in threads:
    th.start()


#def worker(num):
#    """thread worker function"""
#    for i in range(10):
#        print('Worker: %s' % num,)
#      
#
#
#threads = []
#
#for i in range(5):
#    t = threading.Thread(target=worker, args=(i,))
#    threads.append(t)
#
#print("Começam--------------------------")
#for i in range(5):
#    threads[i].start()