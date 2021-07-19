t=(1,2,3,"mon","tue")
print('Length using function : ',len(t))
print('--------------------------------')
c=0
for i in t:
    if i in t:
        c=c+1
print('Length using Loop :',c)