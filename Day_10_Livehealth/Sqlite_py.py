import sqlite3
con=sqlite3.connect('livehealth.db')
print('Connection Established....')
cur=con.cursor()
print('Cursor Created........')
#cur.execute('create table Person (y_id,y_name)')
cur.execute("insert into Person values(106,'Sanjay')")
values=[(105,'Sarvu'),(104,'Shiva')]
cur.executemany('insert into Person values (?,?)',values)
#t=cur.execute('delete from Person where y_id=101')
#print(t)
records=cur.execute('select * from Person ')
for row in records:
    print(row)
print('Table  Created.......')
con.commit()
print('Changes Saved Successfully.........')
con.close()
print('Connection Closed..............')