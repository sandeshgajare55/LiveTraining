dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'python': 100, 'java': 200, 'for': 300}
d3={}
for i,j in dict1.items():
    for x,y in dict2.items():
        if i==x:
            d3[i]=(j+y)
dict2.update(d3)
d4={}
for k in dict2.items():
    d4[k]=dict2.get(k)
print(d4)