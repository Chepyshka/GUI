import FreeSimpleGUI as sg


def zavd1():
    layout = [
        [sg.Text("Введіть перше число:"), sg.Input(key="num1")],
        [sg.Text("Введіть друге число:"), sg.Input(key="num2")],
        [sg.Button("Обчислити"), sg.Button("Назад")]
    ]
    window = sg.Window("Завдання 1", layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Назад"):
            break
        if event == "Обчислити":
            try:
                num1 = float(values["num1"])
                num2 = float(values["num2"])
                додавання = num1 + num2
                віднімання = num1 - num2
                множення = num1 * num2
                ділення = num1 / num2 if num2 != 0 else "Неможливо ділити на 0"

                sg.popup(
                    f"Результат додавання: {додавання}\n"
                    f"Результат віднімання: {віднімання}\n"
                    f"Результат множення: {множення}\n"
                    f"Результат ділення: {ділення}"
                )
            except ValueError:
                sg.popup_error("Будь ласка, введіть числові значення.")
    window.close()


def zavd2():
    layout = [
        [sg.Text("Введіть швидкість першого автомобіля (км/год):"), sg.Input(key="V1")],
        [sg.Text("Введіть швидкість другого автомобіля (км/год):"), sg.Input(key="V2")],
        [sg.Button("Обчислити"), sg.Button("Назад")]
    ]
    window = sg.Window("Завдання 2", layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Назад"):
            break
        if event == "Обчислити":
            try:
                V1 = float(values["V1"])
                V2 = float(values["V2"])
                t1 = 2 - (2 * 20 / 60)
                t2 = 2 - (10 / 60)
                distance1 = V1 * t1
                distance2 = V2 * t2
                total_distance = distance1 + distance2
                sg.popup(f"Відстань між автомобілями через дві години: {total_distance:.2f} км")
            except ValueError:
                sg.popup_error("Будь ласка, введіть числові значення.")
    window.close()


def zavd3():
    layout = [
        [sg.Text("Введіть довжину маршруту R (км):"), sg.Input(key="R")],
        [sg.Text("Введіть довжину маршруту R1 (км):"), sg.Input(key="R1")],
        [sg.Text("Введіть довжину маршруту R2 (км):"), sg.Input(key="R2")],
        [sg.Text("Введіть довжину маршруту R3 (км):"), sg.Input(key="R3")],
        [sg.Text("Введіть довжину маршруту R3 (м):"), sg.Input(key="R3_m")],
        [sg.Text("Введіть кількість маршрутів R1 до K:"), sg.Input(key="K")],
        [sg.Button("Обчислити"), sg.Button("Назад")]
    ]
    window = sg.Window("Завдання 3", layout)
    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Назад"):
            break
        if event == "Обчислити":
            try:
                R = float(values["R"])
                R1 = float(values["R1"])
                R2 = float(values["R2"])
                R3 = float(values["R3"])
                R3_m = float(values["R3_m"]) / 1000
                K = int(values["K"])
                if K > 5:
                    d_R1 = K * (R1 + 0.8)
                else:
                    sg.popup_error("Неможливо виконати обчислення, оскільки K <= 5.")
                    continue

                d_R = 3 * R
                d_R3 = (8 - (3 + K)) * (R3 + R3_m)
                total_distance = d_R + d_R1 + d_R3
                sg.popup(f"Загальна відстань, пройдена туристом: {total_distance:.2f} км")
            except ValueError:
                sg.popup_error("Будь ласка, введіть числові значення.")
    window.close()


def main():
    layout = [
        [sg.Text("Виберіть завдання (1-3):")],
        [sg.Button("Завдання 1"), sg.Button("Завдання 2"), sg.Button("Завдання 3")],
        [sg.Button("Вихід")]
    ]
    window = sg.Window("Лабораторна робота", layout)
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
