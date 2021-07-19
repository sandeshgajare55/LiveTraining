class Bank:
        def Display(self,rate):
         print('Rate of Interest : ',self.rate)


class Savings(Bank):
    def Display(self,rate):
        if(self.rate==3):
            print('Savings Account interest rate : ',self.rate)

class Current(Bank):
        def Display(self,rate):
            if (self.rate == 5):
                print('Savings Account interest rate : ',self.rate)


rate=input('Enter rate of interest : ')
c=Current()
c.Display(rate)
s=Savings()
s.Display(rate)
b=Bank()
b.Display(rate)
