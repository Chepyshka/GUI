import os
import subprocess
import FreeSimpleGUI as sg

LABS_DIR = "labs"

def get_lab_list():
    return [d for d in os.listdir(LABS_DIR) if os.path.isdir(os.path.join(LABS_DIR, d))] if os.path.exists(LABS_DIR) else []

def get_lab_description(lab_name):
    path = os.path.join(LABS_DIR, lab_name, "README.md")
    return open(path, "r", encoding="utf-8").read() if os.path.exists(path) else "Опис відсутній."

def run_lab(lab_name):
    path = os.path.join(LABS_DIR, lab_name, f"{lab_name}.py")
    subprocess.Popen(["python", path], shell=True) if os.path.exists(path) else sg.popup_error(f"Файл {lab_name}.py не знайдено!", title="Помилка")

sg.theme("Python")
layout = [
    [sg.Text("Виберіть лабораторну роботу:", font=("Arial", 12, "bold"))],
    [sg.Listbox(values=get_lab_list(), size=(30, 10), key="lab_list", enable_events=True)],
    [sg.Multiline("Опис роботи тут.", size=(50, 10), key="opus", disabled=True)],
    [sg.Button("Запустити", key="run"), sg.Button("Вихід", key="exit")]
]

window = sg.Window("Лабораторні роботи", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "exit"):
        break
    if event == "lab_list" and values["lab_list"]:
        window["opus"].update(get_lab_description(values["lab_list"][0]))
    if event == "run" and values["lab_list"]:
        run_lab(values["lab_list"][0])
    elif event == "run":
        sg.popup_error("Спочатку виберіть лабораторну роботу.", title="Помилка")

window.close()
