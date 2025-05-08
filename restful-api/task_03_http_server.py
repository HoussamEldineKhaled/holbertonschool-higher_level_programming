#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif self.path == '/data':
            dataset = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(dataset).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            


if __name__ == '__main__':
    httpd = HTTPServer(('', 8000), HTTPRequestHandler)
    httpd.serve_forever()
