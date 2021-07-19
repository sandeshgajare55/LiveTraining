s1=str(input('Enter 1st String : '))
s2=str(input('Enter 2nd String : '))
s1.split()
print(s1)
s2.split()
l1=list(s1)
l2=list(s2)
t1=set(l1)
t2=set(l2)

p=t2.intersection(t1)
print(p)

'''for i in s1:
    for j in s2:
        if i==j:
            print(i)'''