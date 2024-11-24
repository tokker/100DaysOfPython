import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
word_count = 0
correct_word_count = 0

def start_game(language, difficulty, first_window):
    first_window.destroy()

    global word_language
    word_language = language


    global window
    window = Tk()
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    window.title("Flash Card App")


    global cardFrontImage
    global cardBackImage
    cardFrontImage = PhotoImage(file="images/card_front.png")
    cardBackImage = PhotoImage(file="images/card_back.png")
    rightImage = PhotoImage(file="images/right.png")
    wrongImage = PhotoImage(file="images/wrong.png")

    global word_dict
    global selected_word
    global canvas
    global word_text
    global language_text
    global score_label
    global canvas_image
    word_dict = choose_words(language, difficulty)
    selected_word = random.choice(list(word_dict.keys()))

    score_label = Label(text="0/0", font=("Arial", 30, "normal"), bg=BACKGROUND_COLOR)
    score_label.grid(row=0, column=0, columnspan=2)

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas_image = canvas.create_image(400, 263, image=cardFrontImage)
    language_text = canvas.create_text(400, 150, text=language.capitalize(), fill="black", font=("Ariel", 40, "italic"))
    word_text = canvas.create_text(400, 263, text=selected_word, fill="black", font=("Ariel", 60, "bold"))
    canvas.grid(row=1, column=0, columnspan=2)

    right_button = Button(image=rightImage, highlightthickness=0, borderwidth=0, command=right_button_press)
    right_button.grid(row=2, column=0)

    wrong_button = Button(image=wrongImage, highlightthickness=0, borderwidth=0, command=wrong_button_press)
    wrong_button.grid(row=2, column=1)

    global task_id
    task_id = window.after(3000, flip_card)
    window.mainloop()



def choose_words(language, difficulty):
    data = pandas.read_csv(f"data/{language}.csv")
    starting_number = -1
    end_number = 10000
    if difficulty == "kezdő":
        end_number = 200
    elif difficulty == "könnyű":
        end_number = 500
    elif difficulty == "közepes":
        starting_number = 500
        end_number = 1000
    elif difficulty == "nehéz":
        starting_number = 1000
        end_number = 3000
    else:
        starting_number = 3000

    return {row.iloc[0]: row.iloc[1] for (index, row) in data.iterrows() if starting_number < index < end_number}


def wrong_button_press():
    global selected_word
    global word_count
    global task_id

    window.after_cancel(task_id)
    canvas.itemconfig(canvas_image, image=cardFrontImage)

    word_count += 1

    selected_word = random.choice(list(word_dict.keys()))
    canvas.itemconfig(word_text, text=selected_word, fill="black")
    canvas.itemconfig(language_text, text=word_language.capitalize(), fill="black")

    score_label.config(text=f"{correct_word_count}/{word_count}")
    task_id =window.after(3000, flip_card)


def right_button_press():
    global word_dict
    global selected_word
    global word_count
    global correct_word_count
    global task_id

    window.after_cancel(task_id)
    canvas.itemconfig(canvas_image, image=cardFrontImage)

    correct_word_count += 1
    word_count += 1
    word_dict.pop(selected_word)

    if not word_dict:
        window.destroy()
        return

    selected_word = random.choice(list(word_dict.keys()))
    canvas.itemconfig(word_text, text=selected_word, fill="black")
    canvas.itemconfig(language_text, text=word_language.capitalize(), fill="black")

    score_label.config(text=f"{correct_word_count}/{word_count}")
    task_id = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=cardBackImage)
    canvas.itemconfig(language_text, text="Magyar", fill="white")
    canvas.itemconfig(word_text, text=word_dict[selected_word], fill="white")
