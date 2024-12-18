import FreeSimpleGUI as sg


class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' автор {self.author} ({self.year}) - Жанр: {self.genre}"


class HomeLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return f"Книга '{book.title}' додана до бібліотеки."

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return f"Книга '{title}' видалена з бібліотеки."
        return f"Книга '{title}' не знайдена у бібліотеці."

    def find_books_by_author(self, author):
        results = [book for book in self.books if book.author.lower() == author.lower()]
        return results

    def find_books_by_year(self, year):
        results = [book for book in self.books if book.year == year]
        return results

    def find_books_by_genre(self, genre):
        results = [book for book in self.books if book.genre.lower() == genre.lower()]
        return results

    def get_book_by_index(self, index):
        if 0 <= index < len(self.books):
            return self.books[index]
        else:
            return None

    def display_books(self):
        if not self.books:
            return "Бібліотека порожня."
        else:
            return "\n".join([f"{idx + 1}. {book}" for idx, book in enumerate(self.books)])



def main():
    library = HomeLibrary()

    layout = [
        [sg.Text("Меню бібліотеки")],
        [sg.Button("Додати книгу"), sg.Button("Показати всі книги"), sg.Button("Пошук за автором"),
         sg.Button("Пошук за роком"), sg.Button("Пошук за жанром"), sg.Button("Отримати книгу за індексом"),
         sg.Button("Видалити книгу"), sg.Button("Вийти")],
        [sg.Text("", size=(40, 1), key="output")],
        [sg.Input("", size=(40, 1), key="input_text"), sg.Button("Підтвердити")]
    ]

    window = sg.Window("Домашня бібліотека", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вийти":
            break

        output_text = ""
        input_text = values["input_text"].strip()

        if event == "Додати книгу":
            if input_text:
                try:
                    title, author, year, genre = map(str.strip, input_text.split(","))
                    library.add_book(Book(title, author, int(year), genre))
                    output_text = f"Книга '{title}' додана до бібліотеки."
                except ValueError:
                    output_text = "Помилка вводу. Перевірте формат (Назва, Автор, Рік, Жанр)."
            else:
                output_text = "Введіть дані книги."

        elif event == "Показати всі книги":
            output_text = library.display_books()

        elif event == "Пошук за автором":
            if input_text:
                books = library.find_books_by_author(input_text)
                output_text = "\n".join([str(book) for book in books]) if books else "Книги не знайдено."
            else:
                output_text = "Введіть ім'я автора."

        elif event == "Пошук за роком":
            try:
                year = int(input_text)
                books = library.find_books_by_year(year)
                output_text = "\n".join([str(book) for book in books]) if books else f"Книги з {year} не знайдено."
            except ValueError:
                output_text = "Введіть правильний рік."

        elif event == "Пошук за жанром":
            if input_text:
                books = library.find_books_by_genre(input_text)
                output_text = "\n".join([str(book) for book in books]) if books else "Книги не знайдено."
            else:
                output_text = "Введіть жанр."

        elif event == "Отримати книгу за індексом":
            try:
                index = int(input_text) - 1
                book = library.get_book_by_index(index)
                if book:
                    output_text = str(book)
                else:
                    output_text = "Неправильний індекс."
            except ValueError:
                output_text = "Введіть правильний індекс."

        elif event == "Видалити книгу":
            if input_text:
                output_text = library.remove_book(input_text)
            else:
                output_text = "Введіть назву книги для видалення."

        window["output"].update(output_text)
        window["input_text"].update("")

    window.close()


if __name__ == "__main__":
    main()
