num = int(input('Enter a Number : '))
rem = sum = 0;
n = num;
while (num > 0):
    rem = num % 10;
    sum = sum + rem;
    num = num // 10;
if (n % sum == 0):
    print(n," is a Harshad Number");
else:
    print(n," is not a Harshad Number");