class Bank:
    def __init__(self,rate):
        self.rate=rate

    def Display(self):
         print('Rate of Interest : ',self.rate)


class Savings(Bank):
    def Display(self):
            print('Savings Account interest rate : ',self.rate)

class Current(Bank):
        def __init__(self,rate):
            self.rate=rate
        def Display(self):
                print('Current Account interest rate : ',self.rate)

c=Current(rate=0.05)
c.Display()
s=Savings(rate=0.03)
s.Display()
b=Bank(rate=0.02)
b.Display()
