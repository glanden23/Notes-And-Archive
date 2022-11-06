from Course import Course
from Student import Student
#from Assignment import *
from Teacher import Teacher

teacherList = []
courseList = []
studentList = []

#load in the teacher
with open("./data/teacher.csv", "r") as file:
    teacherLines = file.readlines()
    teacherLines.pop(0)
    for line in teacherLines:
        name,course,junk = line.split("\t", 2)
        #create a teacher object
        teacher = Teacher(name,course)
        teacherList.append(teacher)
        courseList.append(Course(course,teacher))
        #save the teachers in the teacherList
    del junk
for i in teacherList:
    print(i)
for i in courseList:
    print(i)






























def loadStudent():
    newStudent="y"
    while newStudent=="y":
        first=input("Student's First >>> ")
        last=input("Student's Last >>> ")
        studentList.append(Student(first,last))
        newStudent = input("Do you have another new student? (y/n) >>> ")

    for student in studentList:
        print(student)
def courseLootup():
    classToLookUp = "Algebra"
    for course in courseList:
        if course.name == classToLookUp:
            print(course.courseID,course.name,course.teacher.name)