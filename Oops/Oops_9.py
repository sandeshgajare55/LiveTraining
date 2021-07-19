class Vehicle:
    def Accelerate(self,mph):
        self.mph=mph

    def Stop(self):
        return "Vehicle Stopped"

    def Run(self):
        return "Vehicle is Running"

class Car(Vehicle):
    def Accelerate(self,mph):
        print('Acceleration of Car with',mph,'speed')

c=Car()
print(c.Run())
c.Accelerate(200)
print(c.Stop())