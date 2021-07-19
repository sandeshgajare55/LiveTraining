name=input('Enter the Name of an Employee : ')
basic=int(input('Enter Basic Salary of Employee : '))
da=basic*(30/100)
hra=basic*(12.5/100)
pf=basic*(10/100)
gross=basic+hra+da
net=gross-pf
print('Name of Employee : ',name)
print('Basic Salary : ',basic)
print('HRA : ',hra)
print('DA : ',da)
print('PF : ',pf)
print('Gross Salary : ',gross)
print('Net Salary : ',net)
