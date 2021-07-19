l1=[10,20,30,40,50,60,70,80,90,100]
print('Original list : ',l1)
l2=[]
for i in l1:
    print(i)
    if i.__index__()==0:
        l2=l1.remove()
print(l2)
