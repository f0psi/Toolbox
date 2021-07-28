#!/usr/bin/env python3

#USAGE: sudo ./redirect.py 80 http://jenkins.example.com:8080/

import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

logging.basicConfig(level=logging.DEBUG)
Hostheader = True

print("""
Usage: {} <port_number> <url> <hostheader-value>
""".format(sys.argv[0]))


class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(302)
       self.send_header('Location', sys.argv[2])
       self.send_header("Access-Control-Allow-Origin", "*")
#      custom_red = "http://url-to-redirect.com"
#      self.send_header('Location', custom_red)

       if Hostheader:
            self.send_header('Host', sys.argv[3])
       self.end_headers()

if len(sys.argv) < 4:
    print("Host-Header wont be send in redirect")
    Hostheader = False

#print(sys.argv[3])
HTTPServer(("", int(sys.argv[1])), Redirect).serve_forever()
