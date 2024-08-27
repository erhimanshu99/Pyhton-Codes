def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'
num_subjects = int(input("Enter the number of subjects: "))
total_marks = 0
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total_marks += marks
    percentage = (total_marks / (num_subjects * 100)) * 100
print(f"\nTotal Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
grade = calculate_grade(percentage)
print(f"Grade: {grade}")
