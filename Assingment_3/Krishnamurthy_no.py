def factor(n):
    fact = 1
    while (n != 0):
        fact = fact * n
        n = n - 1
    return fact

def isKrish(n):
    sum = 0
    temp = n
    while (temp != 0):
        rm = temp % 10
        sum = sum + factor(rm)
        temp = temp // 10

    return (sum == n)
n =int(input('Enter any no to check whether its krishnamurthy no or not : '))
if (isKrish(n)):
    print("YES")
else:
    print("NO")
