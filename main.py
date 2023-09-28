from tkinter import *
import nltk
import math

# nltk.download("gutenberg")
from nltk.corpus import gutenberg
import random

# ------------------ Random Words -----------------------#

moby = set(nltk.Text(gutenberg.words("melville-moby_dick.txt")))
moby = [word.lower() for word in moby if len(word) > 2]

a = set(nltk.Text(gutenberg.words("carroll-alice.txt")))
a = [word.lower() for word in a if len(word) > 2]

# -------------------- CONSTANTS ------------------------#
GREY_BLUE = "#b0bcd1"
random_word_list = []
for i in range(0, 51):
    random_word = moby[int(random.random() * len(set(moby)))]
    random_word_list.append(random_word)
reps = 0
timer = None
TYPING_TIME = 15


# -------------------- START TEST ------------------------#


def start_test():
    typing_area.focus()
    words_to_type = Label(text=random_word_list, wraplength=250)
    words_to_type.grid(column=2, row=2)
    count_down(TYPING_TIME)


# -------------------COUNTDOWN TIMER --------------------#
def count_down(count):
    # global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # timer_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        word_check()


# -------------------- WORD CHECK ---------------------#


def word_check():
    typed_words = typing_area.get()
    typed_words = typed_words.split()
    word_number = 0
    correct_words = 0
    for word in typed_words:
        print(f"Target Word: {random_word_list[word_number]}")
        print(f"Typed Word: {word}")
        if word == random_word_list[word_number]:
            correct_words += 1
        word_number += 1
    show_stats(typed_words, correct_words)


# --------------------- STATS -------------------------- #
def show_stats(typed_words, correct_words):
    typed_words_stats = Label(
        text=f"You typed {len(typed_words)} total words", wraplength=250
    )
    typed_words_stats.grid(column=2, row=6)

    correct_words_stats = Label(
        text=f"You typed {correct_words} words correctly", wraplength=250
    )
    correct_words_stats.grid(column=2, row=7)

    incorrect_words = len(typed_words) - correct_words
    incorrect_words_stats = Label(
        text=f"You typed {incorrect_words} incorrectly", wraplength=250
    )
    incorrect_words_stats.grid(column=2, row=8)

    words_per_minute = correct_words * (60 / TYPING_TIME)
    words_per_minute_stats = Label(
        text=f"You type at a speed of {words_per_minute} words per minute"
    )
    words_per_minute_stats.grid(column=2, row=10)


# -------------------- UI SETUP -------------------------#
window = Tk()
window.title = "Typing Speed Test"
window.config(padx=100, pady=50, bg=GREY_BLUE)

canvas = Canvas(width=200, height=224, bg=GREY_BLUE, highlightthickness=0)
timer_text_canvas = canvas.create_text(50, 100, text="00:00")
canvas.grid(column=2, row=1)

# Start Typing Button
start_typing_button = Button(text="Start Typing Test", width=15, command=start_test)
start_typing_button.grid(column=2, row=0)

# Timer Text
# timer_text = Label(text="00:00")
# timer_text.grid(column=2, row=1)
# timer_text = canvas.create_text(10, 30, text="00:00")
# canvas.grid(column=2, row=1)

# Typing Area
typing_area = Entry(width=52)
typing_area.grid(column=2, row=3)


window.mainloop()
