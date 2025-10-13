import sqlite3 as sql

def userTable():
    con = sql.connect("Flask_PWA_Programming_For_The_Web_Task_Template/Database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM UserTable").fetchall()
    con.close()
    return data

def messageTable():
    con = sql.connect("Flask_PWA_Programming_For_The_Web_Task_Template/Database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM Messages").fetchall()
    con.close()
    return data

def answerTable():
    con = sql.connect("Flask_PWA_Programming_For_The_Web_Task_Template/Database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM Answers").fetchall()
    con.close()
    return data
