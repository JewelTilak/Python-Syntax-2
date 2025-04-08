class book:
    def __init__(self, name, author, publisher, year, copies_sold):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.year = year
        self.copies = copies_sold

class fiction(book):
    def __init__(self, name, author, publisher, year, copies_sold, target):
        super().__init__(name, author, publisher, year, copies_sold)