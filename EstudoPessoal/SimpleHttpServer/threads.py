# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 15:30:55 2018

@author: lcristovao
"""

import threading


def worker(num):
    """thread worker function"""
    for i in range(10):
        print('Worker: %s' % num,)
      


threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

print("Começam--------------------------")
for i in range(5):
    threads[i].start()