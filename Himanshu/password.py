def create_name_with_heart(name):
    heart_symbol = "❤️"
    name_with_heart = name + " " + heart_symbol
    return name_with_heart
name = input("Enter a name: ")
result = create_name_with_heart(name)
print(result)
