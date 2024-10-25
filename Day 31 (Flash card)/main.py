import tkinter as tk
from tkinter import ttk
import pandas as pd
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
TIME_ALLOWED = 3

######################## global variables ###########################
cards = []
curr_card = None

def correct_answer():
    global curr_card, cards
    new_word = {
        "word": curr_card["French"],
        "translation": curr_card["English"]  # Added translation for completeness
    }
    try:
        with open("Day 31 (Flash card)/data/known_words.json", "r") as known_words_file:
            known_words = json.load(known_words_file)
    except FileNotFoundError:
        known_words = []

    known_words.append(new_word)
    with open("Day 31 (Flash card)/data/known_words.json", "w") as known_words_file:
        json.dump(known_words, known_words_file, indent=4)
    cards.remove(curr_card)
    next_card()

def wrong_answer():
    next_card()

def read_cards():
    global cards
    cards_df = pd.read_csv("Day 31 (Flash card)/data/french_words.csv")
    cards = cards_df.to_dict(orient="records")
    try:
        with open("Day 31 (Flash card)/data/known_words.json", "r") as known_words_file:
            known_words = json.load(known_words_file)
    except FileNotFoundError:
        known_words = []
    
    cards = [card for card in cards if not any(known_word["word"] == card["French"] for known_word in known_words)]

def next_card():
    global curr_card
    if not cards:  # Check if cards list is empty
        show_completion_message()
        return
    curr_card = random.choice(cards)
    canvas.itemconfig(canvas_card_img, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=curr_card["French"], fill="black")
    if hasattr(root, 'timer'):  # Check if timer attribute exists
        root.after_cancel(root.timer)  # Cancel the previous timer
    right_button.config(state="disabled")
    wrong_button.config(state="disabled")
    count_down(TIME_ALLOWED)

def show_answer():
    global curr_card
    canvas.itemconfig(canvas_card_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=curr_card["English"], fill="white")
    right_button.config(state="normal")
    wrong_button.config(state="normal")

def count_down(counter):
    if counter >= 0:
        canvas.itemconfig(count_down_text, text=f"{counter}")
        root.timer = root.after(1000, count_down, counter - 1)
    else:
        show_answer()

def show_completion_message():
    canvas.itemconfig(canvas_card_img, image=card_front_img)
    canvas.itemconfig(language_text, text="Congratulations!", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(word_text, text="You've learned all the words!", font=(FONT_NAME, 40, "bold"))
    canvas.itemconfig(count_down_text, text="")
     # Hide the buttons
    right_button.grid_remove()
    wrong_button.grid_remove()

############################### UI #############################

## Screen
root = tk.Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#canvas
canvas = tk.Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tk.PhotoImage(file="Day 31 (Flash card)/images/card_front.png")
card_back_img = tk.PhotoImage(file="Day 31 (Flash card)/images/card_back.png")
canvas_card_img = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=(FONT_NAME, 60, "bold"))
count_down_text = canvas.create_text(725, 50, text="1", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Right button
right_image = tk.PhotoImage(file="Day 31 (Flash card)/images/right.png")
right_button = tk.Button(
    root, 
    image=right_image, 
    command=correct_answer,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR
)
right_button.grid(row=1, column=1)

#wrong_button
wrong_image = tk.PhotoImage(file="Day 31 (Flash card)/images/wrong.png")
wrong_button = tk.Button(
    root, 
    image=wrong_image, 
    command=wrong_answer,
    borderwidth=0,
    highlightthickness=0,
    relief='flat',
    bg=BACKGROUND_COLOR,
    activebackground=BACKGROUND_COLOR
)
wrong_button.grid(row=1, column=0)

read_cards()
next_card()
root.mainloop()

