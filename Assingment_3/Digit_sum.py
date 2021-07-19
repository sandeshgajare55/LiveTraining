number=int(input('Enter a Number : '))
sum=0
while number>0:
    rm=number%10
    sum=sum+rm
    number=number//10
print("Addition : ",sum)
