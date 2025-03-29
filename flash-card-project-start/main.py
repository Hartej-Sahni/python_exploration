import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

french_dict = {}

rand_pair = ()

try:
    data_file = open("data/words_to_learn.csv")
except FileNotFoundError:
    data_file = open("data/french_words.csv")
finally:
    line = data_file.readline()
    while line != "":
        line = line.strip()
        word_and_def = line.split(",")
        french_word = word_and_def[0]
        english_word = word_and_def[1]
        french_dict[french_word] = english_word
        line = data_file.readline()
french_dict_list = list(french_dict.items())
print(len(french_dict_list))

def display_english_translation(word):
    canvas.itemconfig(card_img, image=img_card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=word, fill="white")

def get_rand_pair():
    global rand_pair
    rand_pair = random.choice(french_dict_list)
    canvas.itemconfig(card_img, image=img_card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=rand_pair[0], fill="black")
    window.after(3000, display_english_translation, rand_pair[1])

def knows_word():
    print(rand_pair)
    print(type(rand_pair))
    french_dict_list.remove(rand_pair)
    with open("data/words_to_learn.csv", mode="w") as data_file:
        for pair in french_dict_list:
            data_file.write(f"{pair[0]},{pair[1]}\n")
    get_rand_pair()

#---------------UI Setup--------------
window = Tk()
window.title("Flash Card App")
window.minsize(width=900, height=700)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
img_card_front = PhotoImage(file="images/card_front.png")
img_card_back = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(405, 263, image=img_card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
click_check_mark = Button(image=img_right, highlightthickness=0, command=knows_word)
click_check_mark.grid(row=1, column=0)

img_wrong = PhotoImage(file="images/wrong.png")
click_x_mark = Button(image=img_wrong, highlightthickness=0, command=get_rand_pair)
click_x_mark.grid(row=1, column=1)

get_rand_pair()

window.mainloop()