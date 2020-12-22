class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Admin(Person):
    def __init__(self, name, surname, login):
        super().__init__(name, surname)
        self.login = login
        self.status = "admin"


class User(Person):
    def __init__(self, name, surname, login):
        super().__init__(name, surname)
        self.login = login
        self.status = "user"


class Book:
    book_id = 1

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.book_id = Book.book_id
        Book.book_id += 1

    def __str__(self):
        return "Tytuł: {}, author: {}, rok publikacji: {}, id książki: {}".format(self.title, self.author, self.publication_year, self.book_id)





