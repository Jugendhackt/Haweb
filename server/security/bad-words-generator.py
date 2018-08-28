#!/usr/bin python
# -*- coding: utf-8 -*-
######################################
###### This is only a generator ######
######################################

badwordfile = open("badwords.txt","a")

while True:
    word = raw_input(": ")+"\n"
    badwordfile.write(str(word))
badwordfile.close()