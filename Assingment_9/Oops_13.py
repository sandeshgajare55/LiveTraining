class Person:
    def readScript(self):
        print()

class Actor(Person):
    def readScript(self):
        print('Actor is reading Script ')

A=Actor()
A.readScript()