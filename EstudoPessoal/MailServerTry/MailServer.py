# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:27:27 2018

@author: lcristovao
"""

import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print ('Receiving message from:', peer)
        print ('Message addressed from:', mailfrom)
        print ('Message addressed to  :', rcpttos)
        print ('Message length        :', len(data))
        return

server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()