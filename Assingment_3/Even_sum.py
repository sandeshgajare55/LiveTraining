N=int(input('Enter the Number of Even numbers till which you want to print sum : '))
sum=0
osum=0
for i in range(N+1):
    if i%2==0:
        sum=sum+i
    elif i%2!=0:
        osum=osum+i


print('Sum of All Even Numbers : ',sum)
print('Sum of All Odd Numbers : ',osum)