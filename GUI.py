import time
import random
from random import randint
import tkinter as tk

failures = 0
colors_list = ["grey", "white", "yellow", "red", "blue", "pink", "green"]
red_time = 0


win = tk.Tk()
win.geometry("400x300")
win.config(bg="indigo")
win.title("Check your reaction")


lable_1 = tk.Label(
    text="color",
    width=25,
    height=5,
    bg="green",
    fg="black",
    relief=tk.RAISED,
    bd=5
)

def get_color(): # the function sets the time as a value to the variable "red time" when the red color is on
    global red_time
    x = lable_1.cget("bg")
    if x == "red":
        red = time.time()
        red_time = red
    win.after(2000, get_color)

def button_press(): # the function sets the time of button pressing and gets the bg color value of lable_1
    global failures, red_time
    press_time = time.time()
    x = lable_1.cget("bg")
    if x != "red": # if the color not red we add 1 to the var "failures" and put the value to the lable_2
        red_time = 0
        press_time = 0
        failures += 1
        lable_2.config(text=f"reaction = {round(press_time - red_time, 4)}\n\nfailures = {failures}")

    else: # if the color red it sets the difference of press_time and red_time to the lable_2
        lable_2.config(text=f"reaction = {round(press_time - red_time, 4)}\n\nfailures = {failures}")

button = tk.Button(
    text="press the button when the color\nof the label above is red",
    font=("Arial", 9, "bold", "italic"),
    width=25,
    height=5,
    bg="red",
    fg="black",
    relief=tk.RAISED,
    bd=5,
    activebackground="black",
    activeforeground="white",
    command=button_press
)

lable_2 = tk.Label(
    text=f"reaction = {0}\n\nfailures = {0}",
    width=25,
    height=5,
    bg="yellow",
    fg="black",
    relief=tk.RAISED,
    bd=5
)

def change_color(): # the function changes the bg color of lable_1 every 2 sec.
    color = colors_list[randint(0, 6)]
    lable_1.config(bg=color)
    win.after(2000, change_color)
win.after(2000, change_color)
win.after(2000, get_color)

for i in win.children:
    print(i)
    win.children[i].pack()

win.mainloop()