num = int(input("Enter a number: \n"))
n = len(str(num))
sqr = num**2
last = sqr%pow(10,n)
if last == num:
  print("Automorphic Number")
else:
  print("Not an Automorphic Number")