#creating the class student
#we can define a bunch of attributes about the student
class Student:

    def __init__(self, name, major, gpa, is_on_probation): #Initialize function can map out attributes student should
        self.name = name #creating an attribute for Student
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False