class String:
    def __init__(self):
        self.upper_count = 0
        self.lower_count = 0
        self.vowel_count = 0
        self.consonant_count = 0
        self.space_count = 0
        self.vowels = "AEIOUaeiou"
    def getstr(self):
        user_input = input("Enter a string: ")
        for char in user_input:
            if char.isupper():
                self.upper_count += 1
            elif char.islower():
                self.lower_count += 1
            if char in self.vowels:
                self.vowel_count += 1
            elif char.isalpha():
                self.consonant_count += 1
            elif char.isspace():
                self.space_count += 1
    def display_results(self):
        print("Number of uppercase letters:", self.upper_count)
        print("Number of lowercase letters:", self.lower_count)
        print("Number of vowels:", self.vowel_count)
        print("Number of consonants:", self.consonant_count)
        print("Number of spaces:", self.space_count)
str1=String()
str1.getstr()
str1.display_results()