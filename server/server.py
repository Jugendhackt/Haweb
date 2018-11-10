#!/usr/bin/python3
import sys,os
if sys.version_info.major == 3:
    import tornado.web
    from tornado.ioloop import IOLoop
    from tornado.options import define, options
    from tornado.escape import xhtml_escape
    import socket,time
    import websocketserver, chathandler # pylint: disable=E0401
else:
    sys.exit("Start Server in Python3")
# config options
define('port', default=8888, type=int, help='port to run web server on')
define('debug', default=True, help='start app in debug mode')
define('route_to_index', default=False, help='route all requests to index.html')
options.parse_command_line(final=True)

PORT = options.port
DEBUG = options.debug
ROUTE_TO_INDEX = options.route_to_index

os.chdir("../client-html/")

class DirectoryHandler(tornado.web.StaticFileHandler):
    def validate_absolute_path(self, root, absolute_path):
        if ROUTE_TO_INDEX and self.request.uri != '/' and not '.' in self.request.uri:
            uri = self.request.uri
            if self.request.uri.endswith('/'):
                uri = uri[:-1]

            absolute_path = absolute_path.replace(uri, '/index.html')

        if os.path.isdir(absolute_path):
            index = os.path.join(absolute_path, 'index.html')
            if os.path.isfile(index):
                return index

            return absolute_path

        return super(DirectoryHandler, self).validate_absolute_path(root, absolute_path)

    def get_content_type(self):
        if self.absolute_path.endswith('.vtt'):
            return 'text/vtt'

        if self.absolute_path.endswith('.m3u8'):
            return 'application/vnd.apple.mpegurl'

        content_type = super(DirectoryHandler, self).get_content_type()

        # default to text/html
        if content_type == 'application/octet-stream':
            return 'text/html'

        return content_type

    @classmethod
    def get_content(cls, abspath, start=None, end=None):
        #relative_path = abspath.replace(os.getcwd(), '') + '/'
        if os.path.isdir(abspath):
            html = ""
            for line in open("error.html"):
                html = html + line
            return html

        if os.path.splitext(abspath)[1] == '.md':
            try:
                import codecs
                import markdown
                input_file = codecs.open(abspath, mode='r', encoding='utf-8')
                text = input_file.read()
                return markdown.markdown(text)
            except:
                import traceback
                traceback.print_exc()
                pass

        return super(DirectoryHandler, cls).get_content(abspath, start=start, end=end)

settings = {
    'debug': DEBUG,
    'gzip': True,
    'static_handler_class': DirectoryHandler
}

application = tornado.web.Application([(r'/ws', websocketserver.WSHandler),(r"/upload", chathandler.UploadHandler),

    (r'/(.*)', DirectoryHandler, {'path': './'})
], **settings)

if __name__ == "__main__":
    print("Listening on port %d..." % PORT)
    application.listen(PORT)
IOLoop.instance().start()