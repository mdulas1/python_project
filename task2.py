class Onlinecourse:
    def __init__(self,course,instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_students(self,student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in{self.course} course.")

    def course_datails(self,):
        print(f"course {self.course}")
        print(f"instructor name: {self.instructor}")
        print(f"enrolled students {','.join(self.students)}")
        for student in self.students:
            print(student.name)

    def course_completed(self,name):
        for student in self.students:

         if student.name in name:
            self.students.remove(student)
            print(f"{name} has completed the course!")
        
        print(f"{name} is not enrolled in this course")

    def avg_grade(self,):
        total = sum(student.grades)
        average = total / len(student.grades)
        print(f"the average grade is: {average}")

course_input = input("enter your course:").capitalize()
name = input("enter instructor name:").capitalize()
student = input("enter a students name:").capitalize()

class Student:
    def __init__(self,name,):
        self.name = name
        self.grade = grade

        

course = Onlinecourse(course_input, instructor="merry")
grades =[98,85,76,40,10]
instructor = input("enter instructors name")

course.avg_grade(grades)
course.enroll_students()
course.course_datails()
course.course_completed(name)

#
num_student =int( input("Enter number of student_"))
for _ in range(num_student):
    student_name =input("enter student name: ").lower()
    grades = []
    for _ in range(3):
        grade =int(input("enter a grade: "))
        grades.append(grade)
        student=student(student_name,grades)
        course.enroll_students(student)
        course.avg_grade(student)
    course.course_datails()


