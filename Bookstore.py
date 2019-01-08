
class Bookstore:

    def assignBookDetails(self):
        self.book_no = int(input("Enter Book number:"))
        self.book_name = input("Enter Book name:")
        self.book_title = input("Enter Book title:")
        self.book_author = input("Enter Book number:")
        self.book_qunt = int(input("Enter Book quantity:"))
        self.book_price = float(input("Enter Book price:"))

    def displayBookDetails(self):
        print("Book Number:",self.book_no)
        print("Book Name:",self.book_name)
        print("Book Title:",self.book_title)
        print("Book Author:",self.book_author)
        print("No of book Available:",self.book_qunt)
        print("Book Price:",self.book_price)

    def calBookPrice(self):
        self.quantity = int(input("Enter the no of books you want to buy:"))
        if self.quantity > self.book_qunt :
            print("Insufficient book")
            self.calBookPrice()
        else:
            print("Total price is:",self.book_price*self.quantity)

b1 = Bookstore()
b1.assignBookDetails()
b1.displayBookDetails()
b1.calBookPrice()