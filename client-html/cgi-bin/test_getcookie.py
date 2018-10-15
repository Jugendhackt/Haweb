#!/usr/bin/env python

import Cookie
import os

print "Content-type: text/plain\n"

try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    print "session = " + cookie["session"].value
except (Cookie.CookieError, KeyError):
    print "session cookie not set!"
