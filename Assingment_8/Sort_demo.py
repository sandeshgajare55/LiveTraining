marks = [('English', 88), ('Science', 90), ('Maths', 97),('Social sciences', 82)]
print('Original List : ',marks)
marks.sort(key = lambda x: x[1])
print('Sorted List : ',marks)
