s=str(input('''Enter 5 City Names : '''))
s2=s.split(" ")
#print(s2)
l1=list(s2)
print(l1)
s1=input('Enter City name to check Occurance : ')
print("Count of City : ",s1," is ",l1.count(s1))
c=0
for i in l1:
        if i==s1:

            c=l1.index(s1)