# -*- coding: utf-8 -*-
import json
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
            else:
                allowed = 2
    else:
        allowed = 0
    return allowed # Allowed 0 = The User is not existing
                   # Allowed 1 = The User is existing but the password is wrong
                   # Allowed 2 = The User is existing and the Password is right but his accont is disabeld
                   # Allowed 3 = The User can login

def add(user,passwd):
    with open("data/users/users.json,","r") as f:
        json.dump("",f)