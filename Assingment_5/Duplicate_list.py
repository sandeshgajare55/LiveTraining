l1=[20,25,20,30,40,30]
print('Original List : ',l1)
l2=[]
l3=[]
c=0
for i in l1:
      if i not in l2:
       l2.append(i)
      else:
        l3.append(i)
        c=c+1
print('List Without Duplication : ',l2)
print('Duplicate Elements : ',l3,', Duplicate No count ',c)

