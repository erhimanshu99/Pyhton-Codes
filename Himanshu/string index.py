str1= input("enter a string:")
str2=''
index=-1
for i in str1:
    str2+=str1[index]
    index-=1
print("given string={}\n the reverse string={}".format(str1,str2))
if (str1==str2):
    print("hence the given string is a palindrom")
else:
    print("the given string is not a polindrom")
