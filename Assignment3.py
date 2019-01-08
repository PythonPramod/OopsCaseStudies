# Marks for five Student

class Student:

    def assign(self,roll_no,name,eng_marks,math_marks,science_marks):
        self.roll_no = roll_no
        self.name = name
        self.eng_marks = eng_marks
        self.math_marks = math_marks
        self.science_marks = science_marks
    def display(self):
        print("Student Name:",self.name)
        self.total_marks = self.eng_marks + self.math_marks + self.science_marks
        print("Total Marks:",self.total_marks)
        self.percentage = (self.total_marks/300)*100
        print("Percentage:", self.percentage)

std1 = Student()
std1.assign(101,"Pramod",55.00,90.00,89.00)
std1.display()
print("============================================")
std2 = Student()
std2.assign(102,"Pravas",63.00,98.00,43.00)
std2.display()
print("============================================")
std3 = Student()
std3.assign(103,"Babu",45.00,87.00,79.00)
std3.display()
print("============================================")
std4 = Student()
std4.assign(104,"Ravi",56.00,76.00,83.00)
std4.display()
print("============================================")
std5 = Student()
std5.assign(105,"Kumar",65.00,79.00,59.00)
std5.display()