import sqlite3

db = sqlite3.connect("veresiye.db")
yetki = db.cursor()
yetki.execute("CREATE TABLE IF NOT EXISITS kisiler")