s1=str(input('Enter 1st String : '))
s2=str(input('Enter 2nd String : '))
l1=list(s1)
l2=list(s2)
def S_demo(l1,l2):
    c = False
    for i in l1:
        for j in l2:
            if i==j:
                c=True
    print(c)
S_demo(s1,s2)

