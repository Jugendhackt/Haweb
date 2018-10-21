# -*- coding: utf-8 -*-
import chathandler,contenthandler # pylint: disable=E0401
import tornado.websocket
import time,json

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        self.clients.append(self)
        print ('[Server] New connection')
        self.write_message(contenthandler.tab("",True))
        for message in chathandler.messages:
            self.write_message(message)
    def on_message(self, message):
        clientadress = self.request.remote_ip
        print (message)
        message = json.loads(message)
        print (message["type"]) 
        print ('[Server] '+clientadress+' %s' % message["message"])
        self.sendall(message["message"],clientadress)
    def on_close(self):
        self.clients.remove(self)
        print ('[Server] Connection closed')
    def check_origin(self, origin):
        return True
    def sendall(self,message,name=""):
        clientadress = self.request.remote_ip
        chathandler.messages.append(chathandler.makejsonmessage(message,clientadress))
        for client in self.clients:
            client.write_message(chathandler.makejsonmessage(message,name))