import csv
import sqlite3

con = sqlite3.connect('base.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS 'pass' (avatar BLOB, name TEXT, age INT, surv BOOL, work TEXT, class TEXT)")
con.commit()
con.close()
with open("titanic.csv") as csvfile:
    data = csv.reader(csvfile)
    for i in data:
        if i[1] != "Age":
            name = i[0]
            age=404
            if i[1]:
                age = int(float( i[1].strip("").strip("'")))
            gend = "man"
            if "Mrs " in name or "Miss " in name:
                gend = "woman"
            if age<18:
                gend = "baby"
            im = open(f"{gend}.jpg", "rb").read()
            avatar = sqlite3.Binary(im)
            survived = i[-1]
            work = i[-2]
            clas = i[2]
            con = sqlite3.connect('base.db')
            cur = con.cursor()
            cur.execute("INSERT INTO 'pass' VALUES (?, ?, ?, ?, ?, ?)", (avatar, name, age, survived, work, clas))
            con.commit()
            con.close()


print("ok")