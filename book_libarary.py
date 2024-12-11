class Libarary:
    book_list = []

    def entry_book(self, book):
        self.book_list.append(book)

class Book:
    def __init__(self, book_id, title, author, availability):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    @property
    def book_id(self):
        return self.__book_id
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author

    @property
    def availability(self):
        return 'Yes' if self.__availability else 'No'
        
    @availability.setter
    def availability(self,status):
        if isinstance(status,bool):
            self.__availability = status
        else:
            raise ValueError
        
    @staticmethod
    def view_book_info(libarary):
        if not libarary.book_list:
            print('No books are available right now.')
        else:
            for book in libarary.book_list:
                print(f'Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {book.availability}')
    
    @staticmethod
    def borrow_book(libarary, book_id):
        for book in libarary.book_list:
            if book.book_id == book_id:
                if book.availability == 'Yes':
                    book.availability = False
                    print(f'You have successfully borrowed the "{book.title}" book.')
                else:
                    print(f'The book "{book.title}" is already borrowed.')
                return
        print('Book ID not found!')

    @staticmethod
    def return_book(libarary, book_id):
        for book in libarary.book_list:
            if book.book_id == book_id:
                if book.availability=='No':
                    book.availability = True
                    print(f'You have successfully returned the {book.title} book.')
                else:
                    print(f'The book {book.title} is already available.')
                return
        print('Book ID not found!')

libarary = Libarary()

book1 = Book('101', 'Clean Code', 'Robert C. Martin', True)
book2 = Book('102', 'Think Like a Programmer', 'V. Anton Spraul', True)
book3 = Book('103', 'The Clean Coder', 'Robert C. Martin', True)
book4 = Book('104', 'The Pragmatic Programmer', 'Andrew Hunt and David Thomas', True)
book5 = Book('105', 'Code Complete', 'Steve McConnell', True)

libarary.entry_book(book1)
libarary.entry_book(book2)
libarary.entry_book(book3)
libarary.entry_book(book4)
libarary.entry_book(book5)

while True:

    print('''
    ......Welcome to the Cloud Library......
    Select a service by pressing a number:
    1. View All Books
    2. Borrow Book
    3. Return Book
    4. Exit.
    ''')

    user_input = input('Kindly type the following (1-4):')
    print()
    if user_input not in {'1', '2', '3', '4'}:
        print("Invalid input. Enter 1 to 4', please.")
        continue
    user_input = int(user_input)

    if user_input == 4:
        print()
        print('The library is closing. We appreciate your use of Cloud Library.')
        break

    elif user_input == 1:
        print()
        Book.view_book_info(libarary)

    elif user_input == 2:
        Book.view_book_info(libarary)
        print()
        book_id = input('To borrow, please write the book ID: ')
        Book.borrow_book(libarary, book_id)

    elif user_input == 3:
        print()
        book_id = input('To return, kindly write the Book ID: ')
        Book.return_book(libarary, book_id)
