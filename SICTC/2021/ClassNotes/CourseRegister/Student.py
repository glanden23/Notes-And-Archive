class Student:
    studentID = 0
    def __init__(self,firstName,lastName):
        self.first= firstName
        self.last = lastName
        self.courses = []
        self.studentID = Student.studentID
        Student.studentID+=1

    def __str__(self):
        out = ""
        out += f"{self.studentID} {self.last}, {self.first}\n"
        for course in self.courses:
            out+=f"\t{course}\n"
        return out
    
    def setName(self,newFirst,newLast):
        self.first = newFirst
        self.last = newLast
    
    def getStudentID(self):
        return self.studentID
    
    def addCourse(self,newCourse):
        self.courses.append(newCourse)