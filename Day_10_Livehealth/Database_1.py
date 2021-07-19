import mysql.connector as connector

class Db:

    def __init__(self):
        self.con=" "
        self.cursor=" "
        print('Database Connection Initiated ')

    def getcon(self):
        self.con=connector.connect(host='localhost',database='livehealth',user='root',password='Shrisai12@')
        print('Connection Established')
        self.cursor=self.con.cursor()


    def fetchOne(self):
        sid=1
        sname='Sandesh'
        t=(sid,sname)
        self.cursor.execute('select * from student where sid= %s and sname=%s',t)
        r=self.cursor.fetchone()
        print(r)
        print('Operation Done...')


obj=Db()
obj.getcon()
obj.fetchOne()