l1=[20,25,20,30,40,30]
print('Original List : ',l1)
l2=[]
for i in l1:
      if i not in l2:
       l2.append(i)
print('Without Duplicate Elements : ',l2)