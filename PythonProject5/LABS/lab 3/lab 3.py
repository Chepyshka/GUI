import os
import FreeSimpleGUI as sg


def write_to_file(group_name, student_name, average_grade):
    try:
        file_name = f"{group_name}.txt"
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f"{student_name},{average_grade}\n")
        sg.popup(f"Дані записано до файлу {file_name}.")
    except Exception as e:
        sg.popup_error(f"Помилка запису в файл: {e}")


def read_file(group_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            return f"Помилка читання файлу: {e}"
    else:
        return f"Файл {file_name} не існує."


def search_in_file(group_name, student_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                found = False
                for line in file:
                    name, grade = line.strip().split(',')
                    if name == student_name:
                        found = True
                        return f"Знайдено: {name} - {grade}"
                if not found:
                    return f"Студента {student_name} не знайдено в файлі {file_name}."
        except Exception as e:
            return f"Помилка при пошуку в файлі: {e}"
    else:
        return f"Файл {file_name} не існує."


def sort_file_by_grade(group_name):
    file_name = f"{group_name}.txt"
    if os.path.exists(file_name):
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                students = [line.strip().split(',') for line in file]
            students.sort(key=lambda x: float(x[1]), reverse=True)
            with open(file_name, 'w', encoding='utf-8') as file:
                for name, grade in students:
                    file.write(f"{name},{grade}\n")
            return f"Файл {file_name} відсортовано за середнім балом."
        except Exception as e:
            return f"Помилка при сортуванні файлу: {e}"
    else:
        return f"Файл {file_name} не існує."


def list_files():
    try:
        files = [f for f in os.listdir() if f.endswith('.txt')]
        if files:
            return "\n".join(files)
        else:
            return "Файлів не знайдено."
    except Exception as e:
        return f"Помилка при отриманні списку файлів: {e}"


def main():
    layout = [
        [sg.Text("Меню:")],
        [sg.Button("Додати студента"), sg.Button("Переглянути дані групи")],
        [sg.Button("Знайти студента в групі"), sg.Button("Відсортувати за середнім балом")],
        [sg.Button("Показати всі файли"), sg.Button("Вихід")],
        [sg.Text("", key="output", size=(40, 5))],
    ]

    window = sg.Window("Меню роботи з файлами", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Вихід":
            break

        if event == "Додати студента":
            layout_add = [
                [sg.Text("Введіть назву групи:"), sg.Input(key="group")],
                [sg.Text("Введіть ім'я студента:"), sg.Input(key="name")],
                [sg.Text("Введіть середній бал:"), sg.Input(key="grade")],
                [sg.Button("Записати"), sg.Button("Назад")]
            ]
            window_add = sg.Window("Додати студента", layout_add)
            while True:
                event_add, values_add = window_add.read()
                if event_add == sg.WINDOW_CLOSED or event_add == "Назад":
                    break
                if event_add == "Записати":
                    group = values_add["group"]
                    name = values_add["name"]
                    try:
                        grade = float(values_add["grade"])
                        write_to_file(group, name, grade)
                    except ValueError:
                        sg.popup_error("Помилка вводу. Середній бал повинен бути числовим значенням.")
            window_add.close()

        elif event == "Переглянути дані групи":
            group = sg.popup_get_text("Введіть назву групи:")
            if group:
                result = read_file(group)
                window["output"].update(result)

        elif event == "Знайти студента в групі":
            group = sg.popup_get_text("Введіть назву групи:")
            student_name = sg.popup_get_text("Введіть ім'я студента:")
            if group and student_name:
                result = search_in_file(group, student_name)
                window["output"].update(result)

        elif event == "Відсортувати за середнім балом":
            group = sg.popup_get_text("Введіть назву групи:")
            if group:
                result = sort_file_by_grade(group)
                window["output"].update(result)

        elif event == "Показати всі файли":
            result = list_files()
            window["output"].update(result)

    window.close()


if __name__ == "__main__":
    main()
