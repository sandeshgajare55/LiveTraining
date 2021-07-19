l1=[1,2,-2,-3,-10]
print("Original list:",l1)
l2 = list(filter(lambda x:x<0,l1))
l3 = list(filter(lambda x:x>0,l1))
print("Sum of the Positive numbers : ",sum(l3))
print("Sum of the Negative numbers : ",sum(l2))