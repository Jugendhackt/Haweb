# -*- coding: utf-8 -*-
#This is an special build get the newest at https://github.com/antonk123/haweb
import json,time,os
from passlib.hash import pbkdf2_sha256


with open("data/users/users.json","r") as f:
    usersjson = json.load(f)
    
def check(user,passwd):
    if user in usersjson["users"]:
        with open("data/users/"+user+"/main.json","r") as f:
            userjson = json.load(f)
        allowed = 1
        if pbkdf2_sha256.verify(passwd,userjson["passwordhash"]):
            if userjson["active"] == True:
                allowed = 3
                userjson["last-login"] = str(time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime()))
                with open("data/users/"+user+"/main.json","w") as f:
                    json.dump(userjson,f)
                    f.close()
            else:
                allowed = 2
    else:
        allowed = 0
    return allowed # Allowed 0 = The User is not existing
                   # Allowed 1 = The User is existing but the password is wrong
                   # Allowed 2 = The User is existing and the Password is right but his accont is disabeld
                   # Allowed 3 = The User can login
def add(user,username,passwd,override = False): # Override = Account Reset
    if check(user,passwd) >= 1 and override == False:
        return False
    else:
        with open("data/users/example/main.json","r") as f:
            example = json.load(f)
            f.close()
        example["name"] = user
        example["username"] = username
        example["passwordhash"] = pbkdf2_sha256.encrypt(passwd, rounds=200000, salt_size=16)
        path = "data/users/"+user+"/"
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, "main.json"),"wb") as f:
            json.dump(example,f)
            f.close
        usersjson["users"].append(user)
        with open("data/users/users.json","w") as f:
            json.dump(usersjson,f)
            f.close()
        return True
def addclient(username,passwd):
    sessionid = ""
    return sessionid
def checkclient(sessionid):
    username = ""
    return username
def delclient(sessionid):
    succes = False
    return succes
def delclients(username):
    succes = False
    return succes