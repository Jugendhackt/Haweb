#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
# Import Date for Log
import datetime
now = datetime.datetime.now()
#Import Hashlib for creating hashes
import hashlib

log = open("/home/anton/Dokumente/Haweb/client/cgi-bin/data/log.txt","a")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Login</title>"
print "</head>"
print "<body>"
print "<h2>Only Post</h2>"
print "</body>"
print "</html>"

log.write("["+str(now)+"] Login of "+ str(username)+"\n")

mystring = "hallo"

hashm = hashlib.md5(mystring.encode())

log.write(str(hashm.hexdigest())+"\n")

log.close()
