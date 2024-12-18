import FreeSimpleGUI as sg


def f(n):
    sorted_n = sorted(n, reverse=True)
    return sorted_n[:5]



def main():
    layout = [
        [sg.Text("Введіть числа через кому (наприклад, 1, 2, 3):"), sg.Input(key="numbers")],
        [sg.Button("Обчислити"), sg.Button("Вихід")],
        [sg.Text("Результат:", size=(20, 1)), sg.Text("", key="result", size=(20, 1))],
    ]

    window = sg.Window("Обчислення п'яти найбільших чисел", layout)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Вихід"):
            break

        if event == "Обчислити":
            try:

                input_numbers = values["numbers"]
                number_list = list(map(int, input_numbers.split(',')))


                result = f(number_list)


                window["result"].update(result)
            except ValueError:
                sg.popup_error("Будь ласка, введіть правильні числові значення, розділені комами.")

    window.close()


if __name__ == "__main__":
    main()
