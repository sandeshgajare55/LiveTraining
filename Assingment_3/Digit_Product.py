number=int(input('Enter a Number : '))
mul=1
while number>0:
    rm=number%10
    mul=mul*rm
    number=number//10
print("Product of Digit : ",mul)