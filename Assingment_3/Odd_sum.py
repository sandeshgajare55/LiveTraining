n=int(input('Enter the Number of Odd Numbers till which you want to print sum : '))
sum=0
for i in range(n):
    if i%2!=0:
        sum=sum+i
print('Sum of All Odd Numbers : ',sum)