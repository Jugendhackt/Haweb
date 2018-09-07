# -*- coding: utf-8 -*-
import os,time,json

messages = []


def chatmessage(message,name=""):
    message = message.replace("<","	&#60;") # Info #
    message = message.replace(">","	&#62;") # Run NO Html Code in chat (I hope)# 
    time_m = str(time.strftime('%H:%M:%S', time.localtime()))
    return '{"type":"chat","message":{"id":'+json.dumps(len(messages))+',"user":'+json.dumps(name)+',"text":'+json.dumps(message)+',"time":'+json.dumps(time_m)+'}}'