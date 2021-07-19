s=str(input('Enter the String'))
n=int(input('Enter Number'))
s2=str(input('Enter String '))
list1=[s,n,s2]
list2=list(list1)
print(list2)
for i in range(len(list2)-1,-1,-1):
        print(list2[i])

print(list2[-1:-len(list2)-1:-1])