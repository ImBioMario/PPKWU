#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
from threading import local

#print('source code for "http.server":', http.server.__file__)
default_message = "Hello World!"

local_time = datetime.datetime.now()
time_message = str(local_time.strftime('%X'))


class web_server(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):

        print('PATH ->> ' + self.path)
        local_time = datetime.datetime.now()
        local_time_string = str(local_time.strftime('%X'))
        message = 'Hello world! \n' + local_time_string
        print(local_time_string)
        if self.path == '/':
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()            
            self.wfile.write(bytes(default_message.encode('utf-8')))
        elif self.path.startswith('/cmd'):
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=UTF-8")
            self.end_headers()   
            split_path = self.path.split('=')
            if split_path[1] == 'time':
                self.wfile.write(bytes(time_message.encode('utf-8')))
            if split_path[1].startswith('rev'):
                rev_command_split = self.path.split('&')
                if len(rev_command_split)>1:
                    if rev_command_split[1].startswith('str'):
                        str_command_split = rev_command_split[1].split('=')
                        if len(str_command_split) > 1:
                            rev_message = str_command_split[1][::-1]
                            self.wfile.write(bytes(rev_message.encode('utf-8')))
                
        
        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()