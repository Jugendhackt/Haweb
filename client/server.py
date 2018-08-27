#!/usr/bin/python
def httpserver():
    from BaseHTTPServer import HTTPServer
    from CGIHTTPServer import CGIHTTPRequestHandler

    serv = HTTPServer(('',8000),CGIHTTPRequestHandler)
    print 'Webserver started.'
    serv.serve_forever()
    
httpserver()