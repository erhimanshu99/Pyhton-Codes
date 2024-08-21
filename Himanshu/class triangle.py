class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height=height
    def calculate_area(self):
        area=1/2*(base*height)
        return area
base = float(input("Enter base of the triangle: "))
height= float(input("Enter the height  of the triangle: "))
T = Triangle(base,height)
area =T.calculate_area()
print(f"The area of the triangle is: {area}")
