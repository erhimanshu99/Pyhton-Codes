class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi*(self.radius**2)
    def circumference(self):
        return 2*Circle.pi*self.radius
r=int(input("enter the radius:"))
C=Circle(r)
print("the area=",C.area())
print("the circumference=",C.circumference())