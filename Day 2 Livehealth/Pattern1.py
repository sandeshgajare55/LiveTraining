n = int(input("Enter number of rows : "))
for i in range(1,n+1):
    alpha = 97
    for j in range(1, i+1):
        print(chr(alpha), end="")
        alpha += 1
    print()