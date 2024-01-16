#Write A Program To add only 4 books as a limit.

class Bookbag:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if len(self.books) >= 4:
            print("The Bag Is Already Full. Cannot Add More Books.")
        else:
            self.books.append(book)
            print(f"{book} added to the bag.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed from the bag.")
        else:
            print(f"{book} not found in the bag.")

    def display_books(self):
        if len(self.books) == 0:
            print("The bag is empty.")
        else:
            print("Books in the bag:")
            for book in self.books:
                print(book)

def BookBagLimit():
    bag = Bookbag()
    while True:
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book = input("Enter the book name: ")
            bag.add_book(book)
        elif choice == 2:
            book = input("Enter the book name: ")
            bag.remove_book(book)
        elif choice == 3:
            bag.display_books()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

BookBagLimit()