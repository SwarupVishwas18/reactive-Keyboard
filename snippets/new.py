import keyboard
import threading

import pathlib
import textwrap
from colorama import Fore

import google.generativeai as genai
import sys
from PyQt6 import QtWidgets, uic
from frontend.main_window import MainWindow
from ex import get_data
import keyboard


current_string = ""
enter_pressed = False
gen_text = ""


# add your api key if below code does not work
# GOOGLE_API_KEY =


genai.configure(api_key="YOUR_KEY")

model = genai.GenerativeModel("gemini-pro")


def getting_data(text):
    global gen_text
    if text != "":
        print(f"Processing string:   {text}")
        res = f' Should the user be targeted for product if he is typing "{ text }" answer in yes or no .if yes which product, also give me result in the format of yes/no:product-name'
        print(res)
        response = model.generate_content(res)
        gen_text = ""
        for chunk in response:
            print(chunk.text)
            gen_text += chunk.text


def on_key_press(event):
    global current_string
    global enter_pressed
    global gen_text

    if event.name == "enter":
        enter_pressed = True
    elif event.name in {"alt", "tab", "alt+tab"}:
        current_string = ""
        enter_pressed = False
    elif event.name == "backspace":
        current_string = current_string[:-1]
    elif event.name == "space":
        current_string += " "
    elif event.name in {
        "shift",
        "right shift",
        "ctrl",
        "caps lock",
        "esc",
        "left",
        "right",
        "up",
        "down",
    }:
        pass
    else:
        current_string += event.name

    if enter_pressed:
        # threading.Thread(target=getting_data, args=(current_string,)).start()
        getting_data(current_string)
        current_string = ""
        enter_pressed = False
        if gen_text != "":
            gen_text = gen_text.lower()
            if "/" in gen_text and "yes" in gen_text:
                item = gen_text.split("/")[1]
                print(Fore.RED, item, Fore.WHITE)
                data = get_data(item)
                app = QtWidgets.QApplication(sys.argv)
                window = MainWindow(data=data)

                window.show()
                app.exec()


keyboard.on_press(on_key_press)


keyboard.wait()
