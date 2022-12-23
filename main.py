from tkinter import *
import time
import random

window = Tk()
window.title('Test Your Typing Speed')
window.config(padx=100, pady=40, bg='#F4EEFF')

canvas = Canvas(width=200, height=224, bg='#424874', highlightthickness=0)
clear_screen = 0


def test():
    global clear_screen

    if clear_screen == 0:
        window.destroy()
        clear_screen = clear_screen + 1




    def check_word():
        if entry.get() == words[word]:
            end = time.time()
            type_speed = 60 / ((end - start) / 5)
            result = Label(text=f"You type {round(type_speed, 2)} words per minute")
            result.grid(column=1, row=5)

        else:
            wrong = Label(text="The text you entered is incorrect", fg='#F4EEFF', bg='#424874', font=("Courier", 15))
            wrong.grid(column=1, row=5)

    words = ['i will wait for you', 'the dog ran very fast',
             'it was an apple pie', 'the sun is very bright',
             'i had a good time', 'ring the bell for service',
             'will you look at that', 'time to brush my teeth',
             'i live in the city', 'please close the front door']

    word = random.randint(0, (len(words) - 1))

    start = time.time()
    window2 = Tk()
    window2.config(padx=100, pady=40, bg='#F4EEFF')

    def new_test():
        window2.destroy()
        test()

    word_label = Label(text=words[word], fg='#424874', bg='#F4EEFF', font=("Courier", 15))
    word_label.grid(column=1, row=0)

    start_label = Label(text="Type the sentence above. Then press done.", fg='#424874', bg='#F4EEFF', font=("Courier", 15))
    start_label.grid(column=1, row=1)

    entry = Entry(window2)
    entry.grid(column=1, row=2)

    done_button = Button(text="Done", fg='#424874', command=check_word)
    done_button.grid(column=1, row=3)

    retry_button = Button(text="Try again", fg='#424874', command=new_test)
    retry_button.grid(column=1, row=4)



    window2.mainloop()


title_label = Label(text="Let's Start Typing", fg='#F4EEFF', bg='#424874', font=("Courier", 15))
title_label.grid(column=1, row=0)

space = Label(bg='#F4EEFF', pady=5)
space.grid(column=1, row=1)

start_button = Button(text="Press When You're Ready to Start", fg='#424874', command=test)
start_button.grid(column=1, row=2)


window.mainloop()
