class Teacher:
    '''def __init__(self,name,address,phone,spl_subject,salary,income_tax):
        self.name=name
        self.address=address
        self.phone=phone
        self.spl_subject=spl_subject
        self.salary=salary
        self.income_tax=income_tax'''

    def Accept(self):
        self.name=input('Enter Name : ')
        self.address = input('Enter Address : ')
        self.phone = input('Enter Phone : ')
        self.spl_subject = input('Enter Spl_subject: ')
        self.salary =float(input('Enter Salary : '))
        self.income_tax = input('Enter Income Tax : ')

    def Display(self):
        print('----------------------------------------------------------------------')
        print('Name : ',self.name)
        print('Address : ',self.address)
        print('Phone No : ',self.phone)
        print('Special Subject : ',self.spl_subject)
        print('Salary : ',self.salary)
        print('Income Tax',self.income_tax)

    def calc(self):
        print('--------------------------------------------------------------------------')
        self.salary=self.salary//0.5
        print('Tax : ',self.salary)
#t=Teacher('Sandesh','Pipeline,Nagar',8668556085,'Computer',50000,15000)
t=Teacher()
t.Accept()
t.Display()
t.calc()
