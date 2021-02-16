import sqlite3


def children():
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    for i in cur.execute("SELECT name, age FROM 'pass' WHERE age < 18"):
        print(f"{i[0]} - {i[1]}")
    con.commit()
    con.close()


def surv():
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    survived = 0
    died = 0
    for i in cur.execute("SELECT surv FROM 'pass'"):
        if i[0] == "TRUE":
            survived += 1
        else:
            died += 1  
    print(f"Выжили: {survived}\nПогибли: {died}")
    con.commit()
    con.close()

def non():
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    for i in cur.execute("SELECT name, work FROM 'pass' WHERE class <> '1st Class' AND class <> '2st Class' AND class <> '3st Class'"):
        print(f"{i[0]} - {i[1]}")
    con.commit()
    con.close()

while True:
    a = int(input("0 - Вывод детей\n11 - Вывод погибших/выживших\n2 - Вывод корабельной команды\n3 - Завершить работу программы\nВведите число:   "))
    if a == 0:
        children()
    elif a == 1:
        surv()
    elif a == 2:
        non()
    elif a == 3:
        break

print("ok")