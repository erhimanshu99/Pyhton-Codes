print("Checking the string is palindrome")
s = input("enter the string: ")
s1 = s[::-1]
if (s == s1):
    print("the string is palindrome")
else:
    print("the string is not palindrome")