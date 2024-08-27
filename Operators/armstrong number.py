num = int(input("Enter the number: "))
sum=0
temp = num
while temp >0:
    digit = temp % 10
    sum += digit**3
    temp //=  10
if (num == sum):
    print("Number is Amstrong number")
else:
    print("Number is not Amstrong number")