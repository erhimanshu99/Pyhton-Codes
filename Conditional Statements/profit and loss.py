x=float(input("enter the purchase price:"))
y=float(input("enter the selling price:"))
if y>x:
    profit= y-x
    print("you are in profit",profit)
elif y<x:
    loss=x-y
    print("you are in loss", loss)
