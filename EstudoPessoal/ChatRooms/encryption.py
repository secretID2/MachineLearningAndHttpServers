# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:00:17 2018

@author: lcristovao
"""
#
#from Crypto.Cipher import AES
## Encryption
#encryption_suite = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV4567')
#cipher_text = encryption_suite.encrypt(b"A really secret message. Not for prying eyes.")
#
## Decryption
#decryption_suite = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV4567')
#plain_text = decryption_suite.decrypt(cipher_text)

from cryptography.fernet import Fernet
#key = Fernet.generate_key()
#cipher_suite = Fernet(key)
#text="A really secret message. Not for prying eyes."
#cipher_text = cipher_suite.encrypt(text.encode())
#plain_text = cipher_suite.decrypt(cipher_text)
#plain_text=plain_text.decode("utf-8") 

class Encryption:
    
    def __init__(self):
        self.key=Fernet.generate_key()
        self.cipher_suite=Fernet(self.key)
        
    def encrypt(self,text):
        cipher_text = self.cipher_suite.encrypt( text.encode("utf-8"))
        return cipher_text.decode("utf-8")
    
    def decrypt(self,encrypted_text):
        plain_text=self.cipher_suite.decrypt(encrypted_text.encode("utf-8"))
        return plain_text.decode()# the default option is utf-8 so dont worry
    
#___________main____________________________
print(__name__)  