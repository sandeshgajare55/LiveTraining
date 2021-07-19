l1=[3,1,5,4,2]
l2=[]
l3=[]
'''for i in l1:
    if i%2==0:
        l2.insert(i,i%2==0)
    else:
        l2.insert(i,i)
print(l2)'''
for i in l1:
    if i%2==0:
        l2.append(i)
    else:
        l3.append(i)
l2.sort()
l3.sort()
print('Even Numbers in sorted order : ',l2)
print('Odd Numbers in sorted order : ',l3)