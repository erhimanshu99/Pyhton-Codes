class student:
    mark1, mark2, mark3=50,60,70
    def process(self):
        sum=student.mark1+student.mark2+student.mark3
        avg=sum/3
        print("total marks is",sum)
        print("average marks is",avg)
        return
S=student()
S.process()
    