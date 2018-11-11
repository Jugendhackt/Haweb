# -*- coding: utf-8 -*-
import bs4
import os
from bs4 import BeautifulSoup
os.chdir("../client-html/")
tabslist = ("Home","Know-How","Homework","Chat")
contentslist = []
def tabs():
    return '{"type":"tabs","Tabs":{"home":"%s","know-how":"%s","homework":"%s","chat":"%s"}}' %tabslist
def contents():
    html = ""
    for site in tabslist:
        site = site.lower()
        print (site)
        print (site+"/index.html")
        for line in open(site+"/index.html"):
            html = html+line
        parsed_html = BeautifulSoup(html, "html.parser")
        contentslist.append(parsed_html.find(id = "content"))
    return contentslist
print(contents())
print(tabs())