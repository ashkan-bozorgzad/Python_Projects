from tkinter import *
import pandas as pd
import random

# ---------------------------- Read Data ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
selected_word = {}

try:
    french_words = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pd.read_csv("./data/french_words.csv")
finally:
    french_words_dic = french_words.to_dict(orient="records")


# ---------------------------- button function ------------------------------- #
def next_card():
    global selected_word, flip_timer
    window.after_cancel(flip_timer)
    selected_word = random.choice(french_words_dic)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=selected_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card, )


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=selected_word["English"], fill="white")


def is_known():
    french_words_dic.remove(selected_word)
    data = pd.DataFrame(french_words_dic)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card, )

# Create canvas with text
canvas = Canvas(width=800, height=524, bg=BACKGROUND_COLOR, highlightthickness=0, )
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 262, image=card_front_img)
title_text = canvas.create_text(400, 150, fill="black", font=("Aerial", 40, "italic"))
word_text = canvas.create_text(400, 253, fill="black", font=("Aerial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons
# right button
right_img = PhotoImage(file="./images/right.png")
known_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

# wrong button
wrong_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
