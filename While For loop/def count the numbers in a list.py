def count_occurrence(list, n):
    count=0
    for i in list:
        if(i==n):
            count=count+1
    return count
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Original list: ",li)

x=int(input("Enter element to be checked list: "))
print(x,"has occurred ",count_occurrence(li,x),"times")