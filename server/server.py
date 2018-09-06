import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket,time,sys
import httpserver
import websocketserver




application = tornado.web.Application([(r'/ws', websocketserver.WSHandler),(r"/(.*)", httpserver.MainHandler),])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Web Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()
