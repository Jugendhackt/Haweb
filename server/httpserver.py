import tornado.httpserver
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,url):
        if url == "client":
            for line in open("client.html","r"):
                self.write(line)