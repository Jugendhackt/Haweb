# -*- coding: utf-8 -*-
import os,time,json,sys
import tornado,random,string
sys.path.append("security/Users/")
import users # pylint: disable=E0401


messages = []

def makejsonmessage(message,name="",new=""):
    message = message.replace("<","	&#60;") # Info #
    message = message.replace(">","	&#62;") # Run NO Html Code in chat (I hope)# 
    time_m = str(time.strftime('%H:%M:%S', time.localtime()))
    return '{"type":"chat","message":{"id":'+json.dumps(len(messages))+',"user":'+json.dumps(name)+',"text":'+json.dumps(message)+',"time":'+json.dumps(time_m)+'}}'
class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        print (self.get_cookie("id"))
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        final_filename= original_fname+fname+extension
        output_file = open("../server/data/chats/000000/files/" + final_filename, 'w+')
        output_file.write(file1['body'])
        self.finish("file" + final_filename + " is uploaded")