# Student details

class Student:

    def assign(self):
        self.roll_no = int(input("Enter the roll number:"))
        self.name = input("Enter the student name:")
        self.eng_marks = float(input("Enter the marks in English from 100:"))
        self.math_marks = float(input("Enter the marks in Math from 100:"))
        self.science_marks = float(input("Enter the marks in Science from 100:"))
    def display(self):
        self.total_marks = self.eng_marks + self.math_marks + self.science_marks
        print("Total Marks:",self.total_marks)
        self.percentage = (self.total_marks/300)*100
        print("Total Percentage:", self.percentage)

std = Student()
std.assign()
std.display()