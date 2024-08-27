P=float(input("enter the principle:"))
R=float(input("enter the rate of interest in percentage:"))
T=float(input("enter the time in years:"))
A = P*(1 + R/100)*T
print("Maturity ammount ",A)
i=A-P
print("compound interest ",i)

