import functools
l1=[10,20]
l2=tuple(l1)
print(type(l2))
l3=functools.reduce(lambda x,y:x*y,l2)
print(type(l2))
print(l3)