class book:
    def __init__(self,book_name,isbn,author,publisher,genre):
        self.book_name = book_name
        self.isbn = isbn
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.available = True

    def get_title(self):
        return self.book_name

    def get_isbn(self):
        return self.isbn
    
    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher
    
    def get_genre(self):
        return self.genre
    
    def is_available(self):
        if not self.available:
            print(f"Buku {self.book_name} tidak tersedia")
        else:
            print(f"Buku berjudul {self.book_name} tersedia")

    def check_in(self):
        if (self.available):
            self.available = True
            print(f"Book {self.book_name} checked in!")
        else:
            print(f"Book {self.book_name} already checked in!")

    def check_out(self):
        