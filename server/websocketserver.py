# -*- coding: utf-8 -*-
import chathandler,contenthandler # pylint: disable=E0401
import tornado.websocket
import time,json

chatid = "000000"

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    def open(self):
        self.clients.append(self)
        print ('[Server] New connection')
        self.write_message(contenthandler.tabs())
        
        for message in chathandler.messages[chatid]:
            self.write_message(json.dumps(message))
    def on_message(self, message):
        clientadress = self.request.remote_ip
        print (message)
        message = json.loads(message)
        if "chatid" not in message.keys():
            message["chatid"] = chatid
        print (message["type"]) 
        print ('[Server] '+clientadress+' %s' % message["message"])
        message["message"] = {"chatid":message["chatid"], "text":message["message"]}
        self.send_to_all(message,clientadress)
    def on_close(self):
        self.clients.remove(self)
        print ('[Server] Connection closed')
    def check_origin(self, origin):
        return True
    def send_to_all(self,message,name=""):
        msg_json = chathandler.makejsonmessage(message,name)
        chathandler.add_msg_to_msgs(msg_json)
        for client in self.clients:
            client.write_message(json.dumps(msg_json))