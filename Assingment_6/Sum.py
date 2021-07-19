t=[(4, 5), (2, 3), (6, 7), (2, 8)]
print("The original list of tuple is : ",t)
list1 = len(t)
for i in range(list1):
    for j in range(list1 - i - 1):
        if (t[j][0] + t[j][1]) > (t[j + 1][0] + t[j + 1][1]):
            t[j], t[j + 1] = t[j + 1], t[j]
print("According to Sum : ",t)