print("*"*10)
print('----------------------------------------------------------')
for i in range(1,5+1):
    print('* '* i)
print('----------------------------------------------------------')
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('\r')

print('----------------------------------------------------------')
n=int(input('Enter n : '))
sp=n
for i in range(1,n*2,2):
    s="*" * i
    print(s.rjust(sp+i," "))
    sp=sp-1
print('----------------------------------------------------------')
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()
print('----------------------------------------------------------')
rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1