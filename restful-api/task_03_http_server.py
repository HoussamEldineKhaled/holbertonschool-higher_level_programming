#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")


server = HTTPServer(('', 8000), HTTPRequestHandler)
httpd.serve_forever()
