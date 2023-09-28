from tkinter import *
import nltk
import math

# nltk.download("gutenberg")
from nltk.corpus import gutenberg
import random


# -------------------- CONSTANTS ------------------------#
GREY_BLUE = "#b0bcd1"
random_word_list = []
for i in range(0, 51):
    random_word = moby[int(random.random() * len(set(moby)))]
    random_word_list.append(random_word)
reps = 0
timer = None
TYPING_TIME = 5

# ------------------ Random Words -----------------------#

moby = set(nltk.Text(gutenberg.words("melville-moby_dick.txt")))
moby = [word.lower() for word in moby if len(word) > 2]


def start_test():
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
        count_words()


# -------------------- WORD COUNTER ---------------------#


def count_words():
    number_of_words = typing_area.get()
    print(number_of_words)


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
