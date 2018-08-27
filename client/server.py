#!/usr/bin/python
def httpserver(): # Define the http server
    from BaseHTTPServer import HTTPServer # Importing Base Server
    print 'Importing Base Server'
    from CGIHTTPServer import CGIHTTPRequestHandler # Importing CGI Server
    print 'Importing CGI Server'
    serv = HTTPServer(('',8000),CGIHTTPRequestHandler)
    print 'Webserver started.' # Print the progress
    serv.serve_forever() # The Server runs forever
    
httpserver() # Run the Server