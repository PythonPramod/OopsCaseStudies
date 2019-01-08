# Yatra.com

class Customer:

    discover_india_cost = 20000.00
    holiday_hungama_cost = 25000.00
    pilgrimage_package_cost = 23000.00

    def tourDetails(self,name,people,package_cat,tour_date):
        self.cust_name = name
        self.people = people
        self.package_cat = package_cat
        self.tour_date = tour_date
        if package_cat == "D":
            self.cost = Customer.discover_india_cost
        if package_cat == "H":
            self.cost = Customer.holiday_hungama_cost
        if package_cat == "P":
            self.cost = Customer.pilgrimage_package_cost

    def display(self):
        print("Customer Name:",self.cust_name)
        print("No of people in the Tour:",self.people)
        print("Package Category:",self.package_cat)
        print("Total Cost:",self.cost)
        print("Tour starting date:",self.tour_date)

c1 = Customer()
name = input("Enter the Customer name:")
people = int(input("Enter the no of people accomplaying:"))
print("Package Available:")
print("a)Discover India = 20000.00  b)Holiday Hungama = 25000.00  c)Piligrimage Package = 23000.00")
package_cat = input("Enter the package name in the form of D or H or P:")
date = input("Enter tour starting date in dd/mm/yyyy format:")

c1.tourDetails(name,people,package_cat,date)
c1.display()