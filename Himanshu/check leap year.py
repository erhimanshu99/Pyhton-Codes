year=int(input("Enter the year:"))
if (year%400==0) or (year%100!=0) and (year%4==0):
   print("The year is a leap year")
else:
   print("The yaer is not a leap year")