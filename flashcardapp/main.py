from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    og_data=pandas.read_csv("data/french_words.csv")
    to_learn_dict = og_data.to_dict(orient="records")
else:
    to_learn_dict = data.to_dict(orient="records")

print(to_learn_dict)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    # current_card["French"]
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

def is_right():
    global current_card
    to_learn_dict.remove(current_card)
    print(len(to_learn_dict))
    updated_data = pandas.DataFrame(to_learn_dict)
    updated_data.to_csv("data/words_to_learn.csv", index= False) #permantent storage of all words yet to learn
    next_card()                                              #index = False allows multiple runs of this program w/o
                                                            #accumulating index nums every time


window = Tk()
window.title("Flash Card Game")
window.config(padx =50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card) #milliseconds # milliseconds. counts down regardless of user
# input (ie using buttons to get a new card). Named as global variable so we can control when it counts down
# with respect to user input


#-------*-------*------UI-------*-------*-------*

canvas = Canvas(width=800, height=526) #pixel units
card_front = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front) #specify xcor, ycor of image center
card_back = PhotoImage(file="./images/card_back.png")


card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font = ("Ariel", 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(columns=1, row=1, columnspan=2)


wrong_image = PhotoImage(file="./images/wrong.png")
right_image=PhotoImage(file="./images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0,row=4)
right_button = Button(image=right_image, highlightthickness=0, command=is_right)
right_button.grid(column=1,row=4)
#-------*-------*------UI-------*-------*-------*

next_card() #once UI is setup call next_card() to startup with flash card content rather than dummy words

#When the user presses on the right_button, it means that they know the current word on the flashcard and that word
# should be removed from the list of words that might come up.

#Updated data should be saved to a new file called words_to_learn.csv
#When the program runs, check to see if words_to_learn.csv exists and use it; else run french_words.csv

window.mainloop()
