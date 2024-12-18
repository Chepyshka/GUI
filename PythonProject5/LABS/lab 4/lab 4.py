import random
import FreeSimpleGUI as sg

def main():
    layout = [
        [sg.Button("Запустити завдання 2")],
    ]

    window = sg.Window("Програма для підрахунку символів", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Запустити завдання 2":
            zavd2()
def zavd1():
    names = ["Іван", "Марія", "Петро", "Ольга", "Сергій", "Анастасія"]
    verbs = ["малює", "читає", "пишу", "співає", "гуляє", "вивчає"]
    objects = ["картину", "книгу", "вірш", "пісню", "твір", "фото"]

    def generate_phrase():
        first_word = random.choice(names)
        second_word = random.choice(verbs)
        third_word = random.choice(objects)
        return f"{first_word} {second_word} {third_word}"

    random_phrase = generate_phrase()
    sg.popup(f"Згенерована фраза: {random_phrase}")

def zavd2():
    # Текст, який був в файлі "book.txt"
    text = "Як стати крутим програмістом?"

    # Підрахунок символів
    characters_with_spaces = len(text)
    characters_without_spaces = len(text.replace(" ", ""))

    # Виведення результатів через popup
    sg.popup(f"Символи з пробілами: {characters_with_spaces}\n"
             f"Символи без пробілів: {characters_without_spaces}")


def zavd3():
    def sentence_analysis(text):
        sentences = text.split('. ') + text.split('! ') + text.split('? ') + text.split('… ')
        total_sentences = len(sentences)
        exclamatory_sentences = text.count('!')
        question_sentences = text.count('?')
        ellipsis_sentences = text.count('…')
        sg.popup(f"Загальна кількість речень: {total_sentences}\n"
                 f"Кількість окличних речень: {exclamatory_sentences}\n"
                 f"Кількість питальних речень: {question_sentences}\n"
                 f"Кількість речень з трикрапкою: {ellipsis_sentences}")

    text = "Привіт! Як справи? Це приклад тексту... Він містить різні типи речень! Ще одне речення?"
    sentence_analysis(text)


def main():
    layout = [
        [sg.Text("Виберіть завдання:")],
        [sg.Button("Завдання 1"), sg.Button("Завдання 2"), sg.Button("Завдання 3")],
        [sg.Button("Вихід")]
    ]

    window = sg.Window("Меню завдань", layout)

    while True:
        event, _ = window.read()

        if event in (sg.WINDOW_CLOSED, "Вихід"):
            break
        elif event == "Завдання 1":
            zavd1()
        elif event == "Завдання 2":
            zavd2()
        elif event == "Завдання 3":
            zavd3()

    window.close()


if __name__ == "__main__":
    main()
