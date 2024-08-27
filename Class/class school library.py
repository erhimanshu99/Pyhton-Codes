class Library:
    def __init__(self):
        self.bookname=""
        self.author=""
    def getdata(self):
        self.bookname =input("enter namne of the book:")
        self.author=input("enter author of the book:")
    def display(self):
        print("name of the  book:",self.bookname)
        print("name of the author",self.author)
        print("\n")
book=[]
ch='y'
while(ch=='y'):
    print("1.Add new book\n 2.Display books")
    resp=int(input("enter your choice:"))
    if (resp==1):
        L=Library()
        L.getdata()
        book.append(L)
    elif(resp==2):
        for x in book:
            x.display()
    else:
        print("invalid input")
ch= input("do you want to continue")
   
    