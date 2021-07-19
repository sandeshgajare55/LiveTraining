import functools
t=(1,2,3,4,5)
print('Factorial : ',functools.reduce(lambda a,b:a*b,t))
