n=int(input('Enter range : '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=" ")
        i=i+1
    print()