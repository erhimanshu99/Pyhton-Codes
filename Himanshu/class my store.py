class MyStore:
    __prod_code=[]
    __prod_name=[]
    __cost_price=[]
    __prod_quant=[]
    def getdata(self):
        self.p=int(input("enter the no of products you need to store"))
        for x in range(self.p):
            self.__prod_code.append(int(input("enter the product code:")))
            self.__prod_name.append(str(input("enter the product name:")))
            self.__cost_price.append(int(input("enter cost price:")))
    def display(self):
        print("Stock in store")
        print("........................................")
        print("product code\t product name\tcost price")
        print("........................................")
        for x in range(self.p):
            print(self.__prod_code[x],"\t\t",self.__prod_name[x],"\t\t",self.__cost_price[x])
        print("........................................")
    def print_bill(self):
        total_price=0
        for x in range(self.p):
            q=int(input("enter the quantity for the product code %d:"%self.__prod_code[x]))
            self.__prod_quant.append(q)
            total_price=total_price+self.__cost_price[x]*self.__prod_quant[x]
            print("invoice receipt")
            print("........................................................")
            print("product code\t product name\t cost price\t quantity\t Total Amount")
            print(".........................................................")
        for x in range(self.p):
            print(self.__prod_code[x],"\t\t", self.__prod_name[x],"\t\t",self.__cost_price[x],"\t\t",self.__prod_quant[x],"\t\t",self.__prod_quant[x]*self.__cost_price[x])
            print("......................................................")
            print("Total Amount=",total_price )
S=MyStore()
S.getdata()
S.display()
S.print_bill()