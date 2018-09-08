import tornado.httpserver
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_header("Server","")
    def get(self,url):
        try:
            print ("Get "+url)
            if(url.endswith(".css")):
                self.set_header("Content-Type","text/css")
            if(url.endswith(".js")):
                self.set_header("Content-Type","text/javascript")
            if(url.endswith(".svg")):
                self.set_header("Content-Type","application/svg+xml")
            self.render("../client/"+url)
        except:
            self.render("error.html")
    def post(self,url):
        self.render("error.html")