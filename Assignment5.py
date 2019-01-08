# Person class

class Person:
    def __init__(self,first_name,last_name,email,dob):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob
    def display(self):
        print("First Name:",self.first_name)
        print("Last Name:",self.last_name)
        print("Email Id:",self.email)
        print("Date Of Birth:",self.dob)

p1 = Person("pramod","Kumar","pramodkhandai121@gmail.com","04/05/1996")
p1.display()