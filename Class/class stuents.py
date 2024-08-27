class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
student1 = Student(name="Himanshu", age=24, grade="A")
print("Name:", student1.name)
print("Age:", student1.age)
print("Grade:", student1.grade)
