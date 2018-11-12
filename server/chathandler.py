# -*- coding: utf-8 -*-
#This is an special build get the newest at https://github.com/antonk123/haweb
import os,time,json,sys
import tornado,random,string
sys.path.append("security/Users/")
import users # pylint: disable=E0401

if os.path.exists("../server/data/msgs.json"):
    with open("../server/data/msgs.json", "r") as f:
        messages = json.load(f)
        
else:
    messages = {"000000":[]}

def add_msg_to_msgs(msg):
    chatid = msg["message"]["chatid"]
    if chatid not in messages.keys():
        messages[chatid] = []
    messages[chatid].append(msg)
def makejsonmessage(message,name="",new=""):
    message["message"]["text"] = message["message"]["text"].replace("<","	&#60;") # Info #
    message["message"]["text"] = message["message"]["text"].replace(">","	&#62;") # Run NO Html Code in chat (I hope)# 
    time_m = str(time.strftime('%H:%M:%S', time.localtime()))
    message["message"]["id"] = len(messages)
    message["message"]["user"] = name
    message["message"]["time"] = time_m
    return message



class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        print (self.get_cookie("id"))
        #file1 = self.request.files['file1'][0]

        for filet in self.request.files["file1"]:
            original_fname = filet['filename']
            extension = os.path.splitext(original_fname)[1]
            fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
            final_filename= original_fname+fname+extension
            print (final_filename)
            os.path.join(final_filename)
            output_file = open("../server/data/chats/000000/files/" + final_filename, 'wb')
            output_file.write(filet['body'])
            self.finish("file" + final_filename + " is uploaded")