try:
    n1=int(input('Enter 1st NO:'))
    n2=int(input('Enter 2nd NO:'))
    list1=[n1,n2]
    sum1=0
except ValueError:
    print('Value Error : Incorrect Values')

except NameError:
    print('Name Error : Incorrect Name')
except:
    print('OOps... ')
else:
    for i in list1:
        sum1=sum1+i

    avg=sum1//2
    print('Average : ',avg)

finally:
    print('Operation Performed...')
