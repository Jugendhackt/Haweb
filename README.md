# Info this is an Special Version from Haweb to get the newest go to Orginal Projekt
[Orginal]("https://github.com/AntonK123/Haweb/")
# ![Haweb](/client-html/icon/favicon-16x16.png) Haweb
### We Make a Homework Exchange Website. ###

This page will for exchanging your **Homework** and **Chat** with your **Classmates** and you can write **Know-How** articles.



## Server
#### Install
##### Linux
apt (Ubuntu, Mint & Debian)
```bash
sudo apt install python3-passlib

sudo apt install python3-tornado
```
or with pip you need [python3]("https://www.python.org/downloads/") installed
```bash
sudo pip3 install passlib

sudo pip3 install tornado
```
##### Windows
With pip (you need [python3]("https://www.python.org/downloads/") installed)
```cmd
pathtopythonexe -m pip install passlib

pathtopythonexe -m pip install tornado
```

#### Start the Server

Linux
```bash
cd server # Be sure you are in the Haweb directory
python3 server.py 
```
Windows
```cmd
cd server
python server.py # Check that your Python is in the Env. 
#Path if python2 is installed too run python3 server.py
```



## Client

### Website



### Desktop application

Java application with root in client-desktop/
```YAML
Main: main.org.jugendhack.HAWEBDesktop.Main.main
```
**Note:** JFrame Layout is produced by the IntelliJ GridLayoutManager




## Functions

#### Know-How

The idea of this page is to exchange Know-How. For example rules in Math or English grammar rules.

#### Homework

This part of the page will be for exchanging homework.

#### Chat

Here you can chat with your classmates.
Communication bases on Websocket.This is Supported in Web. Desktop-client integration comming soon.
