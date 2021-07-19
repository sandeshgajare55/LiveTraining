class Shape:
    def draw(self):
        print('The Shape is : ',Circle)


class Circle(Shape):
    def draw(self):
        print('Draw Circle')
c=Circle()
c.draw()

class Square(Shape):
    def draw(self):
        print('Draw Square')
S=Square()
S.draw()

class Rectangle(Shape):
    def draw(self):
        print('Draw Rectangle')

r=Rectangle()
r.draw()