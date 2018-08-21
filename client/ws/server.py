import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import time

class WSHandler(tornado.websocket.WebSocketHandler):
    clients = []
    messages = []
    def open(self):
        self.clients.append(self)
        print '[Server] New connection'

    def on_message(self, message):

        clientadress = self.request.remote_ip

        if message == "" or message == "Hallo":
            self.write_message("Du darfst das nicht Schreiben")
            return
        print '[Chat] '+clientadress+': %s' % message
        self.sendall(message,clientadress)

    def on_close(self):
        self.clients.remove(self)
        print '[Server] Connection closed'
    def check_origin(self, origin):
        return True
    def sendall(self,message,name=""):
        time_m = str(time.strftime('%H:%M:%S', time.localtime()))
        for client in self.clients:
            client.write_message('{"message":{ "user":"'+name+'","text":"'+message+'","time":"'+time_m+'"}}')
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
