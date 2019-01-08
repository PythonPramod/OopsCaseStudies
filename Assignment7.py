# Furniture Hierarchey

class  Furniture:

    chair = 0
    bookshelf = 0

    def hierarchy(self):

        self.item = input("Enter which type of furniture you want in the form of a or b:")
        if self.item == "a":
            Furniture.bookshelf = Furniture.bookshelf + 1
        else:
            Furniture.chair = Furniture.chair + 1

    def displayHierarchy(self):
        print("The hierarchy of Furniture is :")
        # print(Furniture.chair)
        # print(Furniture.bookshelf)
        if Furniture.bookshelf > Furniture.chair:
            print("bookshelf")
            print("chair")
        else:
            print("chair")
            print("bookshelf")

f1 = Furniture()
print("Furniture item available:")
print(" a)bookshelf  b)chair")
f1.hierarchy()
f1.hierarchy()
f1.hierarchy()
f1.hierarchy()
f1.hierarchy()
f1.hierarchy()
f1.hierarchy()
f1.displayHierarchy()
f1.hierarchy()
f1.hierarchy()
f1.hierarchy()
f1.displayHierarchy()
