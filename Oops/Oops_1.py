class Vehicle:
    def __init__(self,name,ms,ma):
        self.name=name
        self.ms=ms
        self.ma=ma

    def seatingCapacity(self,cap):
        return {f"The seating capacity of a {self.name} is {cap} passengers"}

class Bus(Vehicle):
    def seatingCapacity(self,cap=50):
        return super().seatingCapacity(cap=50)

b=Bus("Volvo",200,14)
print(b.seatingCapacity())