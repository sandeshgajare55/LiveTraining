#logic google
str1=input('Enter String 1 : ')
str2=input('Enter String 2 : ')
str1=str1.lower()
str2=str2.lower()
print('First String : ',str1)
print('Second String : ',str2)

if(len(str1)==len(str2)):
    sort1 = sorted(str1)
    sort2 = sorted(str2)
    if(sort1==sort2):
            print('Anagram Strings')
    else:
        print('Not a Anagram String ')
else:
    print('Not a Anagram String')