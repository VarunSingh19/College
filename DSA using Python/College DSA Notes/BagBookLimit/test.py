class Bookbag:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        if len(self.add_book ) >= 4:
            print("full..")
        else:
            self.books.append(book)
            print(f"{book} added ")
    