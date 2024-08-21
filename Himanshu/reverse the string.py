def mirror_image_of_string():
    str=(input("enter the string: "))
    str1=""
    index=-1
    for i in str:
        str1+=str[index]
        index-=1
    print(str1)
mirror_image_of_string()        

