def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Number of uppercase letters:", upper_count)
    print("Number of lowercase letters:", lower_count)
user_input = input("Enter a string: ")
count_upper_lower(user_input)