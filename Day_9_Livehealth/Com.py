list1=['Sandy','Mandy','Sam','Jo','Ravi']
list1=[s.lower() for s in list1]
print(list1)
print('--------------------------------------------------')
list2=[s for s in list1 if len(s)%2==0]
print(list2)
print('--------------------------------------------------')
list2=[x if len(x)%2==0 else " " for x in list1]
print(list2)