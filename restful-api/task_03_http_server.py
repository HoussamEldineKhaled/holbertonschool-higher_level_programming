#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Hello, this is a simple API!".encode('utf-8'))


if __name__ == '__main__':
    httpd = HTTPServer(('', 8000), HTTPRequestHandler)
    httpd.serve_forever()
