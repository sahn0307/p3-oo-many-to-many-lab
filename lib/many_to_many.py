class Book:
    all_books = []

    def __init__(self, title: str):
        self._title = title
        type(self).all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise Exception("Title must be a string.")
        self._title = value

    def authors(self):
        return [contract.author for contract in self.contracts()]


    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
class Author:
    all_authors = []

    def __init__(self, name: str):
        self._name = name
        type(self).all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise Exception("Name must be string")
        self._name = value

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Contract:
    all = []
    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Must be an instance of Author")
        self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Must be an instance of Book")
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Must be a string")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
