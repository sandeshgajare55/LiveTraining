class Vehicle:
    color='White'
    def __init__(self,name,max,avg):
        self.name=name
        self.max=max
        self.avg=avg
    def Addition(self,a=10,b=20):
        return a+b

    def display(self):
        print('Name : ',self.name)
        print('Max : ',self.max)
        print('Avg : ',self.avg)
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car=Car('Audi',250,18)
print('Car color :',car.color,'\nCar Name : ',car.name, "\nSpeed:", car.max, "\nMileage:", car.avg)
