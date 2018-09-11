#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
# Import Date for Log
import datetime
now = datetime.datetime.now()
#Import Hashlib for creating hashes
import hashlib
#Import Database
import sqlite3
db = sqlite3.connect('/home/anton/Dokumente/Haweb/client/other/database.sqlite3')
dbc = db.cursor()


log = open("/home/anton/Dokumente/Haweb/client/cgi-bin/data/log.txt","a")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Error response</title>"
print "</head>"
print "<body>"
print "<h1>Error response</h1>"
print "Error code 204 </br></br> Message: No Content </br> </br>"
print "Error code explanation: 204 = The server successfully processed the request and is not returning any content"
print "</body>"
print "</html>"

hashed_password = hash_password(new_pass)

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()



if check_password(db_password,password):
    log.write("["+str(now)+"] Login of "+ str(username)+"\n")

log.close
