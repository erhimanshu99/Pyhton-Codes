item=[]
prod=1
for i in range(5):
    print("price for items{}:".format(i+1))
    p=int(input())
    item.append(p)
for j in range(len(item)):
    print("price of item {}=Rs.{}".format(j+1,item[j]))
    prod=prod*item[j]
    print("sum of all price=Rs",sum(item))
    print("product of all prices=Rs",prod)
    print("average of all prices=Rs.",sum(item)/len(item))