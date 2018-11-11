# -*- coding: utf-8 -*-
import bs4
import os
#os.chdir("../client-html")
def tabs():
    tabs = ("Home","Know-How","Homework","Chat") 
    return '{"type":"tabs","Tabs":{"home":"%s","know-how":"%s","homework":"%s","chat":"%s"}}' %tabs
soup = bs4.BeautifulSoup("error.html")
print (soup.html)