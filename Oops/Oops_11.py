class Bike:
    color=input('Enter Color : ')
    speed=input('Enter Speed : ')

    def bikeInfo(self):
        print('Bike Color : ',self.color)
        print('Bike Speed : ',self.speed)


class Pulsar(Bike):
    def bikeInfo(self):
        print('Pulsar Color : ',self.color)
        print('Pulsar Speed : ',self.speed)

p=Pulsar()
p.bikeInfo()
