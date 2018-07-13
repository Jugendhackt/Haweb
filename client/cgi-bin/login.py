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

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

hashed_password = hash_password(new_pass)
