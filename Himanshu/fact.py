num=int(input("enter the number:"))
fact=1
if num<0:
    print("sorry, fact doesnot exist")
elif num==0:
    print("fact of zero is 1")
else:
    for i in range(1, num+1):
        fact= fact*i
    print("the fact of", num," is", fact)

