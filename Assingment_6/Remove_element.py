print('Adding element in Tuple ')
t4=(10,20,30,40,50)
L1=list(t4)
print('List 1 : ',L1)
L1.remove(30)
t4=tuple(L1)
print('Tuple after adding elements',t4)