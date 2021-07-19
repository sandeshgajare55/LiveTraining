'''def Addition(a,b):
    return a+b
print('Addition : ',Addition(20,25))
'''
print('-----------------------------------------------------------------------------------------')

def Emp(eid,ename,basic):
        hra=basic*0.3
        da=basic*0.2
        pf=basic*0.6
        gross=basic+hra+da
        netsal=basic+hra+da-pf
        return gross,netsal
print(Emp(eid=101,ename='Sandesh',basic=50000))
print('-----------------------------------------------------------------------------------------')

def Calc(*num):
        total=0
        for i in num:
                for j in num:
                        if i==j:
                                total=num[i]*num[j]
                        return total
print(Calc(2,56.00,3,67.00,5,80.00))