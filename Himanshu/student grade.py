def get_grade(grade):
    if grade == 'E':
        return 'Excellent'
    elif grade == 'V':
        return 'Very Good'
    elif grade == 'G':
        return 'Good'
    elif grade == 'A':
        return 'Average'
    elif grade == 'F':
        return 'Fail'
    else:
        return 'Invalid Grade'
def main():
    student_name = input("Enter the student's name: ")
    grade = input("Enter the student's grade (E/V/G/A/F): ")
    grade_description = get_grade(grade)
    if grade_description != 'Invalid Grade':
        print(f"{student_name}, your grade is {grade_description}. Congratulations!")
    else:
        print("Invalid grade entered. Please enter a valid grade (E/V/G/A/F).")
main()
