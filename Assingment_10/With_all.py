try:
    list1=[1,2,3,4,5]
    print(list1[6])
    mob=int(input('Enter a Mobile No : '))
    a=10
    b=0
    print(a/b)

except IndexError:
    print('Index Error : Plz Check Index...')

except ValueError:
    print('Invalid Value : Plz Check Value...')

except ZeroDivisionError:
    print('Divide by  Zero Error : Plz check the Values...')

else:
    print('I Love My India...')

finally:
    print('India is Great...')
