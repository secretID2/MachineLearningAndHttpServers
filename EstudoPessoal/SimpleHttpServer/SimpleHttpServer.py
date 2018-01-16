# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
import http.server as hs
#import SocketServer

#python -m http.server
PORT = 8000

Handler = hs.SimpleHTTPRequestHandler

httpd = hs.socketserver.TCPServer(("", PORT), Handler)

    
print ("serving at port", PORT)
httpd.serve_forever()

#hs.SimpleHTTPRequestHandler.do_GET(self)
#hs.BaseHTTPRequestHandler.send_response(self,"<html><body><h1>Hello!</h1></body></html>",200)
"""
'''
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('10.12.3.240', 80)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()

'''


"""
from http.server import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>Hello!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        
"""        

#from bottle import route, run, template

from bottle import run, get, post, request # or route
import bottle as bt

@get('/') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
def check_login(username,password):
    if(username=='Tiago' and password=='Ola'):
        return True
    else:
        return False

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return bt.static_file('/site1.html', root='files/')
    else:
        return "<p>Login failed.</p>"

run(host='localhost', port=80)




