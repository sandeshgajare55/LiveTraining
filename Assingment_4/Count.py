s=str(input('Enter String : '))
a={}
c=0
for i in s:
    c = c + 1
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
print('count : ',c)
print(str(a),end=" ")
