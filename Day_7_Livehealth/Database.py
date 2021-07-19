import sqlite3
con=sqlite3.connect('apple.db')
print('Conn done')
cur=con.cursor()
print('cursor done')
#cur.execute('create table Person (y_id,y_name)')
#cur.execute("insert into Person values(101,'Sandesh')")
#values=[(102,'Sarvesh'),(103,'Sanket')]
#cur.executemany('insert into Person values (?,?)',values)
t=cur.execute('delete from Person where y_id=101')
print(t)
records=cur.execute('select * from Person ')
for row in records:
    print(row)
print('Table with values is ready')
con.commit()
print('Saved')
con.close()
print('Connection Closed')