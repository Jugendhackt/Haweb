import tornado.httpserver
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_header("Server","")
    def get(self,url):
        try:
            print ("Get :"+url)
            if(url.endswith(".css")):
                self.set_header("Content-Type","text/css")
            if(url.endswith(".js")):
                self.set_header("Content-Type","text/javascript")
            if(url.endswith(".svg")):
                self.set_header("Content-Type","image/svg+xml")
                self.set_header("Add-Encoding","svgz")
            else:
                self.render("../client/"+url)
        except:
            self.render("error.html")
    def post(self,url):
        self.render("error.html")