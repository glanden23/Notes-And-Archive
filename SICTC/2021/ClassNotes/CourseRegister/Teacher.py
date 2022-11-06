class Teacher:
    employeeID = 0
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
        self.courses = []
        self.employeeID = Teacher.employeeID
        Teacher.employeeID+=1
    
    def __str__(self):
        out = ""
        out += f"{self.employeeID} {self.name}, {self.subject}\n"
        for course in self.courses:
            out+=f"\t{course}\n"
        return out
    
    def addCourse(self,newCourse):
        self.courses.append(newCourse)