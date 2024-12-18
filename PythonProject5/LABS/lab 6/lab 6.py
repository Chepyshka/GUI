import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import FreeSimpleGUI as sg


def fetch_webpage(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        sg.popup_error(f"Не вдалося отримати сторінку: {e}", title="Помилка")
        return None


def analyze_text_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    result = "Частота появи слів у тексті новини:\n"
    for word, count in word_counts.most_common(10):
        result += f"{word}: {count}\n"
    return result


def analyze_html_structure(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tags = [tag.name for tag in soup.find_all()]
    tag_counts = Counter(tags)
    result = "\nЧастота появи HTML-тегів:\n"
    for tag, count in tag_counts.most_common(10):
        result += f"<{tag}>: {count}\n"
    return result


def count_links_and_images(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = len(soup.find_all('a'))
    images = len(soup.find_all('img'))
    return f"\nКількість посилань на сторінці: {links}\nКількість зображень на сторінці: {images}"


def analyze_webpage(url):
    html_content = fetch_webpage(url)
    if html_content:
        result = analyze_text_content(html_content)
        result += analyze_html_structure(html_content)
        result += count_links_and_images(html_content)
        return result
    return "Аналіз неможливий через помилку завантаження сторінки."


# GUI Setup
sg.theme("LightBlue")
layout = [
    [sg.Text("Введіть URL для аналізу:", font=("Arial", 12))],
    [sg.InputText(key="url", size=(50, 1))],
    [sg.Button("Аналізувати", key="analyze"), sg.Button("Вихід", key="exit")],
    [sg.Multiline(size=(80, 20), key="result", disabled=True)]
]

window = sg.Window("Аналіз веб-сторінки", layout)

while True:
    event, values = window.read()

    if event in (sg.WINDOW_CLOSED, "exit"):
        break

    if event == "analyze":
        url = values["url"]
        if url:
            analysis_result = analyze_webpage(url)
            window["result"].update(analysis_result)
        else:
            sg.popup_error("Будь ласка, введіть URL.", title="Помилка")

window.close()

