a=int(input('Enter 1st no : '))
b=int(input('Enter 2nd no : '))
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)
def lcm(a,b):
   lcm = (a*b)//gcd(a,b)
   return lcm

print(gcd(a,b))
print(lcm(a,b))