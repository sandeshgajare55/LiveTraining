d1={1:{'Mr.x':'BJP'},2:{'Mr.y':'INC'},3:{'Mr.z':'INC'}}
d2={}
for i,j in d1.items():
    if j not in d2.keys():
        d2[i]=[]
        d2[i].append(i)

print(d2)

