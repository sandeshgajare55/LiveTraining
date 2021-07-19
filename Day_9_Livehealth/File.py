try:
    f=open("S:\\hen.txt","r")
    t=f.read()
    print(t)
except:
    print('Exception : File not Found')
finally:
    f.close()