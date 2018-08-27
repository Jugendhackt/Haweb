import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    messages = []
    def gettime(self):
        return str(time.strftime('%H:%M:%S', time.localtime()))
    def open(self):
        self.clients.append(self)
        print '[Server] '+ self.gettime +' '+'New connection'
        for message in self.messages:
            self.write_message(message)
    def on_message(self, message):
        clientadress = self.request.remote_ip
        print '[Chat] '+self.gettime+" "+clientadress+' %s' % message
        self.sendall(message,clientadress)
        self.messages.append(self.makejsonmessage(message,clientadress))
    def on_close(self):
        self.clients.remove(self)
        print '[Server] '+ self.gettime +' '+'Connection closed'
    def check_origin(self, origin):
        return True
    def makejsonmessage(self,message,name=""):
        message = message.replace('"',"'")
        return '{"message":{ "user":"'+name+'","text":"'+message+'","time":"'+self.gettime+'"}}'
    def sendall(self,message,name=""):
        for client in self.clients:
            client.write_message(self.makejsonmessage(message,name))
class MainHandler(tornado.web.RequestHandler):
    def get(self,url):
        if url == "client":
            for line in open("client.html","r"):
                self.write(line)


application = tornado.web.Application([(r'/ws', WSHandler),(r"/(.*)", MainHandler),])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Web Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()
