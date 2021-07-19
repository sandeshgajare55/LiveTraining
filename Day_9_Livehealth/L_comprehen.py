list1=[i for i in range(1,11)]
print('Serial : ',list1)
print('--------------------------------------------------------------')
list2=[i*i for i in range(1,11)]
print('Square : ',list2)
print('--------------------------------------------------------------')
list3=[i for i in range(1,11) if i%2!=0]
print('Odd Square : ',list3)
print('--------------------------------------------------------------')
list4=[x.upper() for x in "sandesh"]
print('Uppercase :',list4)
print('--------------------------------------------------------------')
#Tuple comprehension
s=(i-0.5 for i in range(1,6))
s2=tuple(s)
print('Tuple : ',s2)
print('--------------------------------------------------------------')