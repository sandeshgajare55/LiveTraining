d1={101:{'Apple':10,'Mango':5},102:{'Apple':15,'Mango':8,'Cherry':5},103:{'Apple':10}}
d2={}
for i,j in d1.items():
    for t,s in j.items():
        d2[t]=d2.get(t,0)+s
print(d2)
