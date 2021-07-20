import sqlite3
con=sqlite3.connect('livehealth.db')
print('Connection Established.....')
cur=con.cursor()
print('Cursor created.....')
#cur.execute('create table emp1(e_id int,e_name varchar(10),e_sal int)')
#print('Table Created...')
# cur.execute("insert into emp1 values(101,'Sandesh',50000)")
# values=[(102,'Sarvesh',45000),(103,'Sanket',30000)]
# cur.executemany('insert into emp1 values (?,?,?)',values)
# print('Data Inserted...')
#r=cur.execute('select e_name from emp1 where e_sal=50000')
a=cur.execute('select * from emp1 order by e_id')
for i in a:
    print(i)
print('All Data...')
# for i in r:
#     print(i)
# print('Single Data...')
con.commit()
print('change saved...')
con.close()

