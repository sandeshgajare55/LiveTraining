a =300
b =400
for num in range(b,a,- 1):
         if num > 1:
             for i in range(2, num):
                 if (num % i) == 0:
                     break
             else:
                 print(num,end=" ")