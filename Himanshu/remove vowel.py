def rem_vowels(s):
    temp_str=""
    for i in s:
        if i in "aAeEiIoOuU":
            pass
        else:
            temp_str+=i
    print("the string without vowels:",temp_str)
str1=input("enter a string:")
rem_vowels(str1)