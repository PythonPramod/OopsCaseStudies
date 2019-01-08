# Course type

class Course:
    # python_fee = 3000.00
    # python_duration = 3.0

    # java_fee = 2500.00
    # java_duration = 6.0

    # dotnet_fee = 4000.00
    # dotnet_duration = 4.0

    def __init__(self,course_name):
        self.course_name = course_name
        if self.course_name == "python":
            self.course_fee = 3000.00
            self.course_duration = 3.0
        if self.course_name == "java":
            self.course_fee = 2500.00
            self.course_duration = 6.0
        if self.course_name == "dotnet":
            self.course_fee = 4000.00
            self.course_duration = 4.0
        print("Available Course type:")
        print("a) part time  b) onsite")
        self.course_type = input("Enter ttype of course :")
    def print(self):
        print("Course name:",self.course_name)
        print("Course Duration in months:",self.course_duration)
        print("Course Type:",self.course_type)

    def getTotalFee(self):
        if self.course_type == "onsite":
            print("Course Fee:",self.course_fee + (self.course_fee*0.1))
        else:
            print("Course Fee:", self.course_fee - (self.course_fee * 0.1))

course_name = input("Enter course name:")
c1 = Course(course_name)
c1.print()
c1.getTotalFee()