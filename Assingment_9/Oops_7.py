class Kid:

    def readBook(self):
         print()

    def readBook(self,srno,name):
        self.srno=srno
        self.name=name

k=Kid()
k.readBook(11,'Sandesh')

class BigKid(Kid):
    def readBook(self):
        print('BigKid')

b=BigKid()
b.readBook()