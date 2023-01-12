import sqlite3
connect=sqlite3.connect("c://sqlite//hcl.db")
cur = connect.cursor()#cursor object to excute quiries
#sql="""insert into filelog values(?,?);"""
#data=(100,'d://jose1//demo.txt')
#cur.execute(sql,data)
#connect.commit()
cur.execute("Select * from filelog where id=100");
rows=cur.fetchall()
for r in rows:
    print(r)
