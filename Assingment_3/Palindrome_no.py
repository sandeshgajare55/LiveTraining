n=int(input('Enter the Number : '))
n2=n
rev=0
while n!=0:
    rm=n%10
    rev=rev*10+rm
    n=n//10
    print(rev)
if n2==rev:
    print('Number is Palindrome')
else:
    print('Number is Not Palindrome')