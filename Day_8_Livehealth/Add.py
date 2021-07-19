from multipledispatch import dispatch
class Add:
    @dispatch(int,int)
    def func(self,a,b):
        return a+b
    @dispatch(int,int,int)
    def func(self,a,b=20,c=30):
        return a+b+c

o=Add()
print('2 no addition : ',o.func(50,50))
print('3 no addition : ',o.func(50,50,100))