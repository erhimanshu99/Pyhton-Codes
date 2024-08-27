import math
def volume():
    radius=float(input("enter the radius of sphere:"))
    volume=(4/3)*math.pi*(radius**3)
    print(volume)
    return volume
volume()