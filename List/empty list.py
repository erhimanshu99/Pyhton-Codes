Number=[]
for i in range(1,11):
    Number.append(i)
print("the list",Number)
for j in Number:
    if(j%2==0):
        Number.remove(j)
print("the list",Number)