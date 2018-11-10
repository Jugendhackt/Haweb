# -*- coding: utf-8 -*-
from xml.dom import minidom
import os
os.chdir("../client-html")
def tabs():
    tabs = ("Home","Know-How","Homework","Chat") 
    return '{"type":"tabs","Tabs":{"home":"%s","know-how":"%s","homework":"%s","chat":"%s"}}' %tabs
def content():
    contents = []
    for filepath in ("Home","Know-How","Homework","Chat"):
        filepath = filepath.lower()+"/index.html"
        html = minidom.parse(filepath)
        contents.append(html.getElementById("content"))
    return '{"type":"content","contents":{"home":"%s","know-how":"%s","homework":"%s","chat":"%s"}}' %contents
#content()