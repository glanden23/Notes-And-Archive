class Course:
    courseID = 0
    #initialization -> Constructor
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        self.courseID = Course.courseID
        Course.courseID+=1
        
    #toString method
    def __str__(self):
        return self.name