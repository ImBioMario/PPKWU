#!/usr/bin/env python3
import http.server
import socketserver
import os
import datetime
import json
from urllib.parse import unquote
from threading import local

#print('source code for "http.server":', http.server.__file__)
default_message = "Hello World!"

local_time = datetime.datetime.now()
time_message = str(local_time.strftime('%X'))

parameter_names = ["lowercase", "uppercase", "digits", "special"]


def str_statistics(strng :str):
    lowercases = len([x for x in strng if x.islower()])
    uppers = len([x for x in strng if x.isupper()])
    digits = len([x for x in strng if x.isnumeric()])
    specials = len(strng) - lowercases - uppers - digits

    return [lowercases, uppers, digits, specials]

def generate_json_string(parameters, parameter_values):
    json_dict = dict(zip(parameters, parameter_values))
    return json.dumps(json_dict)

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
        elif self.path.startswith('/str='):
            string_to_parse = self.path.split('/str=')[1]
            string_decoded = unquote(string_to_parse)
            json_string = generate_json_string(parameter_names, str_statistics(string_decoded))
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()   
            self.wfile.write(bytes(json_string.encode('utf-8')))

        else:
            super().do_GET()
    
# --- main ---

PORT = 4080

print(f'Starting: http://localhost:{PORT}')

tcp_server = socketserver.TCPServer(("",PORT), web_server)
tcp_server.serve_forever()