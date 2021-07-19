try:
    f=open("S:\\hen.txt",'w')
    f.write('Hello My Friends')
except:
    print('Error')
finally:
    print('In final ')
    f.close()