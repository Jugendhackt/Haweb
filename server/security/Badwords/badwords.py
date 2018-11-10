# -*- coding: utf-8 -*-
badwordsfile = open("badwords.txt","r")
badwords = []
for line in badwordsfile:
    line = line.strip("\n")
    line = line.lower()
    badwords.append(line)
def check(message):
    message = message.lower()
    badwordsnumber = 0
    for badword in badwords:
        if badword in message:
            badwordsnumber = badwordsnumber + 1
    print (badwordsnumber)
    return badwordsnumber

#check ('Idiot Dummi Arsch Pfosten Stupid Ashole Fuck Scheiße') # Example
