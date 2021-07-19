def special(n):
    if (n < 10 or n > 99):
        print("Invalid Input! Number"," should have 2 digits only")
    else:
        f= n // 10
        l= n % 10
        sum = f+l
        product = f*l
        if ((sum + product) == n):
            print(n ," is a Special ","Two-Digit Number")
        else:
            print(n , " is Not a ","Special Two-Digit Number")
n = int(input('Enter a Number to Find whether its special or not : '))
special(n)

 
