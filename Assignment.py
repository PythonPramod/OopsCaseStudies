# Represent Bank Account

class Bank:

    def assign(self):
        self.name = input("Enter acc holder name:")
        self.acc_no = int(input("Enter acc number:"))
        self.acc_type = input("Enter acc type:")
        self.balance = float(input("Enter the amount:"))

    def deposite(self):
        self.dep_balance = float(input("Enter the deposite amount:"))
        self.balance = self.balance + self.dep_balance
        print("Total amount:",self.balance)


    def withdraw(self):
        self.wid_balance = float(input("Enter the withdraw amount:"))
        if(self.wid_balance > self.balance):
            print("You have not sufficient amount to withdraw")
            print("Total Amount:",self.balance)
            self.withdraw()
        else:
            self.balance = self.balance-self.wid_balance
            print("Total amount:",self.balance)

    def display(self):
        print("Acc Holder Name:",self.name)
        print("Total balance:",self.balance)

bank = Bank()
bank.assign()
bank.deposite()
bank.withdraw()
bank.display()