class FoodWorld:
    def __init__(self,vName,vQty,vPrice,bill=0):
        self.vName=vName
        self.vQty=vQty
        self.vPrice=vPrice
        self.bill=bill

    def Display(self):
        print('Vegetable Name : ',self.vName)
        print('Vegetable Quantity : ', self.vQty)
        print('Vegetable Price : ', self.vPrice)

    def Calc(self):
        self.bill=self.vQty*self.vPrice
        print('Total Amount to paid is : ',self.bill)

f=FoodWorld('Carrot',50,10)
f.Display()
f.Calc()
