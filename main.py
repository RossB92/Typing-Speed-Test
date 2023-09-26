from tkinter import *
import nltk

# nltk.download("gutenberg")
from nltk.corpus import gutenberg
import random

moby = set(nltk.Text(gutenberg.words("melville-moby_dick.txt")))
moby = [word.lower() for word in moby if len(word) > 2]


# -------------------- CONSTANTS ------------------------#
GREY_BLUE = "#b0bcd1"
random_word_list = []
for i in range(0, 51):
    random_word = moby[int(random.random() * len(set(moby)))]
    random_word_list.append(random_word)

# -------------------------------------------------------#


# -------------------- UI SETUP -------------------------#
window = Tk()
window.title = "Typing Speed Test"
window.config(padx=100, pady=50, bg=GREY_BLUE)

canvas = Canvas(width=800, height=600, bg=GREY_BLUE, highlightthickness=0)

words_to_type = Label(text=random_word_list, wraplength=250)
words_to_type.grid(column=2, row=0)

typing_area = Entry(width=52)
typing_area.grid(column=2, row=1)

window.mainloop()
