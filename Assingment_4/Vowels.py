str=input('Enter String : ')
str[::-1]
print(str)
cnt=0
for i in str:
    if i in "aeiou"or"AEIOU":
        cnt=cnt+1
print('Number of Vowels : ',cnt)
