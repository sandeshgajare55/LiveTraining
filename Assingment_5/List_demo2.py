l1=[1,2,3,4,5,6,7,0,11]
l2=[7,4,3,6,3]
l3=[]
l4=[]
print('First List : ',l1)
print('Second List : ',l2)

for i in range(0, len(l2)):
    if i% 2==0:
        l3.append(l1[i])
for j in range(0, len(l2)):
            if j % 2!=0:
                l4.append(l2[j])

print(l3)
print(l4)
l5=l3+l4
print(l5)
l6=[]
for i in range(len(l1)):
    l6.append(l1[i])
    if i<len(l2):
        l6.append(l2[i])
print('new',l6)