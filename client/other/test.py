import sqlite3
conn = sqlite3.connect('/home/anton/Dokumente/Haweb/client/other/database.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM Users'):
    print row
lang = raw_input("Lang:")
tabs = []

for line in c.execute('SELECT * FROM Tabcontent WHERE Language =\"'+lang+'\"'):
    tabs.append(line[2])
print tabs
"""
if lang == "de":
    tabs = ["Home","Fachwissen","Hausaufgaben","Chat"]
    content = ["<h1>Willkommen auf der Startseite </h1>","<h1>Fachwissen Unterseite</h1>","<h1>Hausaufgaben Unterseite</h1>","<h1> Chat Unterseite</h1>"]
elif lang == "fr":
    tabs = ["Page d'accueil","Savoir specialiste","Devoirs","Chat"]
    content = ["<h1>Bienvenue sur la page d'accueil</h1>","<h1>Base d'expertise</h1>","<h1>Base de devoirs</h1>","<h1> Base de Chat</h1>"]
elif lang == "en" or lang == "en-US":
    tabs = ["Home","Know-how","Homework","Chat"]
    content = ["<h1>Welcome to the Homepage</h1>","<h1>Expertise base</h1>","<h1>Homework base</h1>","<h1> Chat </h1>"]
else:
    tabs = ["???","???","???","???"]
    content = ["???","???","???","???"]


tabscontent = []
tabscontent.append( ["de",1,"Home"] )
tabscontent.append( ["de",2,"Fachwssen"] )
tabscontent.append( ["de",3,"Hausaufgaben"] )
tabscontent.append( ["de",4,"Chat"] )
tabscontent.append( ["fr",1,"Page d'accueil"] )
tabscontent.append( ["fr",2,"Savoir specialiste"] )
tabscontent.append( ["fr",3,"Devoirs"] )
tabscontent.append( ["fr",4,"Chat"] )
tabscontent.append( ["en",1,"Home"] )
tabscontent.append( ["en",2,"Know-how"] )
tabscontent.append( ["en",3,"Homework"] )
tabscontent.append( ["en",4,"Chat"] )
"""
