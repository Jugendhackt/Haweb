# -*- coding: utf-8 -*-

def tab(lang,logined):
    if logined == True:
       tabs = ("Home","Know-How","Homework","Chat") 
    else:
        tabs = ("Home","Know-How")
    return '{"type":"tabs","Tabs":{"tab1":"%s","tab2":"%s","tab3":"%s","tab4":"%s"}}' %tabs