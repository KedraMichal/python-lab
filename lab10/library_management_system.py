from lab10.library_classes import *
import json


class LibraryManagementSystem:

    def __init__(self, name):
        self.name = name
        self.books = {}
        self.users = {}
        self.books_waiting_to_return = []

    def add_book(self):
        title = input("Podaj tytuł książki: ")
        author = input("Podaj autora: ")
        publication_y = input("Podaj rok publikacji: ")
        new_book = Book(title, author, publication_y)
        self.books[new_book.book_id] = [new_book, "available"]

    def delete_book(self):
        book_id = int(input("Podaj id książki do usunięcia: "))
        del self.books[book_id]

    def make_account(self):
        name = input("Podaj imie: ")
        surname = input("Podaj nazwisko: ")
        status = int(input("Wybierz status konta: 1. User 2. Admin "))
        login = input("Podaj login: ")
        while True:
            if login not in self.users.keys():
                if status == 1:
                    new_account = User(name, surname, login)
                elif status == 2:
                    new_account = Admin(name, surname, login)
                self.users[login] = new_account
                break
            else:
                login = input("Login zajęty. Podaj inny: ")

    def see_available_books(self):
        for id_b, book_info in self.books.items():
            if book_info[1] == "available":
                print(book_info[0])
        for number, book_info in enumerate(self.books.values()):
            if book_info[1] == "available":
                break
            if number == len(self.books.values()) - 1:
                print("Brak dostępnych książek do wypożyczenia")
        if self.books.items() is False:
            print("Brak dostępnych książek do wypożyczenia")

    def borrow_book(self):
        borrowed_book_id = int(input("Podaj id książki, którą chcesz wypożyczyć: "))
        if borrowed_book_id in self.books.keys():
            self.books[borrowed_book_id][1] = "unavailable"
            print("Pomyślnie wypożyczono książkę")
        else:
            print("Książka niedostępna")

    def return_book(self):
        return_book_id = int(input("Podaj id książki, którą chcesz zwrócić: "))
        if return_book_id in self.books.keys():
            if self.books[return_book_id][1] == "unavailable":
                self.books_waiting_to_return.append(return_book_id)
        else:
            print("Książka niedostępna!")

    def add_user_account(self):
        name = input("Podaj imie użytkownika: ")
        surname = input("Podaj nazwisko użytkownika: ")
        login = input("Podaj login użytkownika: ")
        while True:
            if login not in self.users.keys():
                new_account = User(name, surname, login)
                self.users[login] = new_account
                break
            else:
                login = input("Login zajęty. Podaj inny: ")

    def accept_books_return(self):
        for book in self.books_waiting_to_return:
            self.books[book][1] = "available"
        print("Przyjęto zwroty książek")

    def read_library_data(self):
        try:
            with open("library_data.json", "r") as f:
                library_data = json.load(f)
                for books_dict in library_data["books"]:
                    for id_key, v in books_dict.items():
                        book_data = v[0]
                        restore_book = Book(book_data["title"], book_data["author"], book_data['publication_year'],
                                            int(id_key))
                        self.books[restore_book.book_id] = [restore_book, v[1]]

                for users_dict in library_data["users"]:
                    for log, user_info in users_dict.items():
                        if user_info["status"] == "admin":
                            adm = Admin(user_info["name"], user_info["surname"], log)
                            self.users[log] = adm
                        else:
                            usr = User(user_info["name"], user_info["surname"], log)
                            self.users[log] = usr

                for book_return_id in library_data["books_waiting_to_return"]:
                    self.books_waiting_to_return.append(book_return_id)
        except IOError:
            pass

    def write_library_data(self):
        for i, book_info in self.books.items():
            self.books[i] = [book_info[0].__dict__, book_info[1]]
        for i, user_info in self.users.items():
            self.users[i] = user_info.__dict__
        json_data = {"books": [self.books], "users": [self.users],
                     "books_waiting_to_return": self.books_waiting_to_return}
        with open("library_data.json", "w") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

    def run_system(self):
        self.read_library_data()
        while True:
            option = int(input("Wybierz nr: 1. Załóż konto 2. Zaloguj się 3. Wyjdz "))
            if option == 1:
                self.make_account()
            elif option == 2:
                given_login = input("Podaj login: ")
                print("Zalogowany jako: {}".format(given_login))
                while True:
                    if given_login in self.users.keys():
                        if self.users[given_login].status == "admin":
                            new_options = int(input("Wybierz nr: 1. Dodaj książkę 2. Usuń książkę 3. Dodaje czytelnika 4. Przyjęcie zwrotu książek 5. Wyloguj "))
                            if new_options == 1:
                                self.add_book()
                            elif new_options == 2:
                                self.delete_book()
                            elif new_options == 3:
                                self.add_user_account()
                            elif new_options == 4:
                                self.accept_books_return()
                            elif new_options == 5:
                                break

                        elif self.users[given_login].status == "user":
                            new_options = int(input("Wybierz nr: 1. Przeszukiwanie katalogu 2. Wypożycz 3. Zwróć 4. Wyloguj "))
                            if new_options == 1:
                                self.see_available_books()
                            elif new_options == 2:
                                self.borrow_book()
                            elif new_options == 3:
                                self.return_book()
                            elif new_options == 4:
                                break
                    else:
                        given_login = input("Błędny login, spróbuj jescze raz: ")
            elif option == 3:
                self.write_library_data()
                break


if __name__ == "__main__":
    m1 = LibraryManagementSystem("Library_1")
    m1.run_system()