from tkinter import *
from tkinter import ttk
from game import start_game

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGES = ["angol", "német"]
language = ""
difficulty = ""

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card App")

starting_label = Label(text="Válassz nyelvet és nehézséget!", font=("Arial", 20, "normal"), bg=BACKGROUND_COLOR)
starting_label.grid(row=0, column=0, columnspan=2)


def select_language(event):
    global language
    language = language_combobox.get()


language_combobox = ttk.Combobox(height=2, values=LANGUAGES, state="readonly")
for item in LANGUAGES:
    language_combobox.insert(LANGUAGES.index(item), item)
language_combobox.bind("<<ComboboxSelected>>", select_language)
language_combobox.set("Nyelv")
language_combobox.grid(row=2, column=0)


def select_difficulty(event):
    global difficulty
    difficulty = difficulty_combobox.get()


difficulties = ["kezdő", "könnyű", "közepes", "nehéz", "nagyon nehéz"]
difficulty_combobox = ttk.Combobox(height=5, values=difficulties, state="readonly")
for item in difficulties:
    difficulty_combobox.insert(difficulties.index(item), item)
difficulty_combobox.bind("<<ComboboxSelected>>", select_difficulty)
difficulty_combobox.set("Nehézség")
difficulty_combobox.grid(row=2, column=1)


def start_button_click():
    if language != "" and difficulty != "":
        start_game(language, difficulty, window)


start_button = Button(text="Kezdés", width=20, height=2, bg="white", command=start_button_click)
start_button.grid(row=3, column=0, columnspan=2)


window.mainloop()








