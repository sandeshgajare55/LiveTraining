number=int(input("Enter a Number"))
rm=0
sum=0
while(number>0):
    rm=number%10
    sum=sum+rm
    number=number//10
print('Sum of Digits : ',sum)    
