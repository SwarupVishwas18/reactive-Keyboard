import keyboard
import threading

import pathlib
import textwrap

import google.generativeai as genai


current_string = ""
enter_pressed = False


# add your api key if below code does not work
# GOOGLE_API_KEY = 


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")


def getting_data(text):
    if text != "":
        print(f"Processing string:   {text}")
        res = f' Should the user be targeted for product if he is typing "{ text }" answer in yes or no .if yes which product, also give me result in the format of yes/no:product-name'
        print(res)
        response = model.generate_content(res)
        for chunk in response:
            print(chunk.text)


def on_key_press(event):
    global current_string
    global enter_pressed

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
        threading.Thread(target=getting_data, args=(current_string,)).start()
        current_string = ""
        enter_pressed = False


keyboard.on_press(on_key_press)

keyboard.wait()
