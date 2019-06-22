import sqlite3

con = sqlite3.connect("datebase.db")
cm = con.cursor()
cm.execute("select * from [log]")
for row in cm:
    id,value,datetime = row
    print(datetime + '|' + value)
con.close()