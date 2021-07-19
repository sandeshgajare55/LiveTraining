s=lambda x:x*x
print('Square using Lambda : ',s(4))
print('-------------------------------------------------------------------')
l1=[1,2,3,4,5,6,7,8,9,10]
l2=list(map(lambda x :x*x,l1))
print('Square of Numbers : ',l2)
print('-------------------------------------------------------------------')
def cube(n):
    return n*n*n
l3=list(map(cube,l1))
print('Cube of Numbers : ',l3)
print('-------------------------------------------------------------------')
list1=["sandesh","sarvesh","sanket","shubham"]
l5=list(map(str.upper,list1))
print('String in Uppercase : ',l5)