# store details of student

class Student:

    service_tax = 0.123
    cpython_fee = 3000.0
    apython_fee = 3500.0

    def __init__(self,rollno,name,course):
        self.rollno = rollno
        self.name = name
        self.course = course

    def payment(self,amount):
        self.paid_amount = amount

        if self.course == "advance python":
            self.course_fee = Student.cpython_fee
        else:
            self.course_fee = Student.apython_fee

        self.dueamount = self.course_fee-self.paid_amount
        self.totalfee = self.dueamount+(self.course_fee*Student.service_tax)

    def print(self):
        print("Name of Student:",self.name)
        print("Roll no:",self.rollno)
        print("Course name:",self.course)
        print("Total course fee with service tax of 12.3%:",self.course_fee+(self.course_fee*Student.service_tax))
        print("Fee Paid:",self.paid_amount)
        print("Due amount:",self.totalfee)


name = input("Enter your name:")
rollno = int(input("Enter rollno:"))
print("Available course:")
print("a)Core Python b)Advance Python")
course = input("Enter Course name:")


s1 = Student(rollno,name,course)
fee_paid = float(input("Enter fee paid:"))
s1.payment(fee_paid)
s1.print()