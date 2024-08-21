mylist=[1,2,2,3,4,5,6,7,8,8,2]
element_count=len(mylist)
print("the number of elements in the list is",element_count)
x=int(input("Enter the element to be counted: "))
z=mylist.count(x)
print(z)
cnt=0
for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if(mylist[j]==mylist[i]):
            cnt=cnt+1
            print(cnt)
