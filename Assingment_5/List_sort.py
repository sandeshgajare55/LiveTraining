l1=['abc','pqr','def','xyz']
l3=['abcd','abc','ab']
l2=sorted(l1,reverse=True)
print('Sorted in Desecnding Order : ',l2)
print('-----------------------------------------------------')
res=l2[0][1]
print('Particular index : ',res)
print('-----------------------------------------------------')
for i in l3:
    if len(i):
        l3.sort()
print('Sorting according to length of String : ',l3)