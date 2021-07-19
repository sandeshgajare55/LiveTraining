s=str(input('Enter a String : '))
print('Original String : ',s)
ch=str(input('Enter character to be remove : '))

for i in s:
    if i in s:
        s2=s.replace(ch,'')
print(s2)
