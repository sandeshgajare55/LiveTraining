l1=[66,11,25,28,45,98,100]
print('Original List : ',l1)
max1 = l1[0]
for i in l1:
    if i > max1:
        max1=i

print('Traditional way maximum : ',max1)


l1.sort()
print('Sorted List : ',l1)
print('Largest Number in List is : ',max(l1))

