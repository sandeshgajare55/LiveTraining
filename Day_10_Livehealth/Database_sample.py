import mysql.connector as Scooby

class Database:
    def __init__(self):
        self.con=" "
        self.cursor=" "
        print('Database Initiated....')

    def getconn(self):
        self.con=Scooby.connect(host='localhost',database='livehealth',user='root',password='Shrisai12@')
        print('Connection Established')
        self.cursor=self.con.cursor()

    def fetchAll(self):
        self.cursor.execute('select * from student')
        records=self.cursor.fetchall()
        for i in records:
            print(i)
        print('Fetched All Data....')

    def fetchOne(self):
        sid=1
        sname="Sandesh"
        t=(sid,sname)
        self.cursor.execute('select sid,sname from student where sid=%s and sname=%s',t)
        r=self.cursor.fetchone()
        print(r)
        print('Operation Successfully fetched One......................')

O=Database()
O.getconn()
O.fetchAll()
O.fetchOne()