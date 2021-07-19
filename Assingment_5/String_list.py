s=["abc","xyz","tpg","pqr"]
l1=list(s)
print('Content of List : ',l1)
c=0
for i in l1:
     if i.isalpha():
            c=c+1
            if i.__len__()>=2:
               l1[0]=i
               l1[-1]=i


print('No of Strings : ',c)
print(l1)