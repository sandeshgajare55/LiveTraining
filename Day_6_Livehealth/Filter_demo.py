l1=[1,3,5,4,6,7,9,10]
l2=list(filter(lambda x:x%2!=0,l1))
l3=list(filter(lambda x:x%2==0,l1))
print('Even Numbers using filter : ',l3)
print('Odd Numbers using filter : ',l2)