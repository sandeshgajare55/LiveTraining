#referenced

s=str(input('Enter String : '))
s1=s.split(" ")
s3=[w[0] for w in s1]
print(" ".join(s3))