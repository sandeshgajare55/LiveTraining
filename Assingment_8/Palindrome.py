l1=["NITIN","SANDESH","COCO","VIJAY"]
print('Original List : ',l1)
result = list(filter(lambda x: (x == "".join(reversed(x))),l1))
result2=list(filter(lambda x: (x != "".join(reversed(x))),l1))
print("List of palindromes : ",result)
print('List of non_Palindromes: ',result2)
#l2=list(map(lambda x:x[::-1],l1))
#print(l2)
