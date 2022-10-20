#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
from threading import local

#print('source code for "http.server":', http.server.__file__)

class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print(self.path)
        local_time = datetime.datetime.now()
        local_time_string = str(local_time.strftime('%X'))
        message = 'Hello world! \n' + local_time_string
        print(local_time_string)
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(bytes(message.encode('utf-8')))
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()