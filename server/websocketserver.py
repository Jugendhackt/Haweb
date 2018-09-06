# -*- coding: utf-8 -*-
import tornado.websocket
import time,json

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    messages = []
    def open(self):
        self.clients.append(self)
        print '[Server] New connection'
        for message in self.messages:
            self.write_message(message)
    def on_message(self, message):
        clientadress = self.request.remote_ip
        print '[Chat] '+clientadress+' %s' % message
        self.sendall(message,clientadress)
        self.messages.append(self.makejsonmessage(message,clientadress))
    def on_close(self):
        self.clients.remove(self)
        print '[Server] Connection closed'
    def check_origin(self, origin):
        return True
    def makejsonmessage(self,message,name=""):
        message = message.replace("<","	&#60;") # Info #
        message = message.replace(">","	&#62;") # Run NO Html Code in chat (I hope)# 
        time_m = str(time.strftime('%H:%M:%S', time.localtime()))
        return '{"message":{ "user":'+json.dumps(name)+',"text":'+json.dumps(message)+',"time":'+json.dumps(time_m)+'}}'
    def sendall(self,message,name=""):
        for client in self.clients:
            client.write_message(self.makejsonmessage(message,name))
