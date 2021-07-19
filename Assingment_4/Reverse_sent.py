#refered

#s=str(input('''Enter a sentence'''))
#s2=s[::-1]
#print(s2)

def rev(s):
    w = s.split(" ")
    nw = [i[::-1] for i in w]
    ns = " ".join(nw)
    return ns
s = input("Enter a sentence : ")
print(rev(s))