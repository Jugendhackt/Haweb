#!/usr/bin/python
import cgi, cgitb
form = cgi.FieldStorage()
lang  = form.getvalue('lang')


import sqlite3
conn = sqlite3.connect('/home/anton/Dokumente/Haweb/client/other/database.db')
c = conn.cursor()

tabs = []
content = ["Home","Fachwissen","Hausaufgaben","Chat"]

for line in c.execute('SELECT Tabname FROM Tabcontent WHERE Language =\"'+lang+'\"'):
    tabs.append(line[0])

print "Content-Type: application/json\r\n\r\n"
print " {"
print "\"Tabs\":{"
print " \"tab1\":\"" + tabs[0] + "\""
print ",\"tab2\":\"" + tabs[1] + "\""
print ",\"tab3\":\"" + tabs[2] + "\""
print ",\"tab4\":\"" + tabs[3] + "\""
print "},"
print "\"Content\":{"
print " \"tab1\":\"" + content[0] + "\""
print ",\"tab2\":\"" + content[1] + "\""
print ",\"tab3\":\"" + content[2] + "\""
print ",\"tab4\":\"" + content[3] + "\""
print "}"
print "}"
