import json
import time
from random import randint
from datetime import date
import tkinter as tk

#the all variables that are used in this code are below till the 18th line
name = ""
failures = 0
colors_list = ["grey", "white", "yellow", "red", "blue", "pink", "green"]
red_time = 0
color = "green"
today = date.today()
reactions_list = []
success_press = 0
press = 0
average = 0
percentage = 0

win = tk.Tk()
win.geometry("600x200")
win.config(bg="indigo")
win.title("Check your reaction")
data = [f"date = {today}, average reaction = {average}, best reaction = {min(reactions_list) if len(reactions_list) > 0 else 0}"]

lable_name = tk.Label(text="your name", bg="black", fg="red", width=25, relief=tk.RAISED, bd=5) # the name field
lable_name.grid(row=0,column=0,sticky="nw")

entry = tk.Entry(width=50, relief=tk.RAISED, bd=5) # the field for entering the name
entry.grid(row=0,column=1,sticky="nw")

lable_1 = tk.Label(text="color", width=25, height=5, bg="green", fg="black", relief=tk.RAISED, bd=5)

def data_name(): # the func for add the new dict with name as a key and the empty list as a value to the file
    global name
    name = entry.get().capitalize()
    try:
        with open("new.json", "r") as f:
            var = json.load(f)
    except json.decoder.JSONDecodeError: # to avoid the exception in case we are trying to load empty file
        with open("new.json", "w") as f:
            new_name = {name: []}
            json.dump(new_name, f)
    with open("new.json", "r") as f:
        var = json.load(f)
        if name not in var:
            new_name = {name: []}
            var.update(new_name)
            f.close()
            with open("new.json", "w") as f:
                json.dump(var, f)


    lable_name.config(text=f"{name}")

name_button = tk.Button(text="enter", width=15, relief=tk.RAISED, bd=3, bg="black", fg="red",
                        activeforeground="black", activebackground="yellow", command=data_name)
name_button.grid(row=0,column=2) # the button for the uppon func

def red_color_time(): # the function sets the time of button pressing and gets the bg color value of lable_1
    global color, red_time
    if color == "red":
        red_time = time.time()
    win.after(2000, red_color_time)

def button_press(): # the function counts reaction speed, quantity of failures
    global color, red_time, failures, press, success_press
    if color != "red":
        press += 1
        failures += 1
        button.config(text=f"press the button when the color\nof the button is red\n\n\n\n\n Reaction = 0\n Failures = {failures}")

    elif color == "red":
        success_press += 1
        press_time = time.time()
        reaction = round(press_time - red_time, 4)
        reactions_list.append(reaction)
        button.config(text=f"press the button when the color\nof the button is red"
                           f"\n\n\n\n\n Reaction = {reaction}\n Failures = {failures}")


button = tk.Button(
    text="press the button when the color\nof the button is red\n\n\n\n\n Reaction = 0\n Failures = 0",
    font=("Arial", 9, "bold", "italic"), anchor="n",
    width=42, height=10,
    bg="red", fg="black",
    relief=tk.RAISED, bd=5,
    activebackground="black",
    activeforeground="white",
    command=button_press)
button.grid(row=1,column=1)

def average_value(): # the func counts average value of reaction and percentage of success in quantity of total presses
    global reactions_list, success_press, press, average, percentage, data
    if sum(reactions_list) != 0:
        average = round(sum(reactions_list) / len(reactions_list), 4)
        percentage = ((success_press * 100) / (success_press + press))
    values.config(text=f"average reaction = {average}"
                              f"\nsuccess pressing = {round(percentage, 4)}%"
                              f"\nbest attempt = {(min(reactions_list) if len(reactions_list) > 0 else 0 )}")
    data = [f"date = {today}, average reaction = {average}, best reaction = {min(reactions_list) if len(reactions_list) > 0 else 0}"]
    win.after(2000, average_value)

# the lable below shows the values of average reaction and percentage, it gets the values from the uppon func
values = tk.Label(
    text=f"average reaction = 0\nsuccess pressing = 0%"
         f"\nbest attempt = {(min(reactions_list) if len(reactions_list) > 0 else 0 )}",
    bg="grey", width=25, height=10, relief=tk.RAISED, bd=3 )
values.grid(row=1, column=0)


def save_func(): # the button save the results percentage success presses more than 50
    if percentage > 50:
        with open("new.json", "r+") as f:
            var = json.load(f)
            if name not in var:
                new_name = {name: data}
                var.update(new_name)
                f.close()
                with open("new.json", "r+") as f:
                    json.dump(var, f)
            else:
                f.close()
                var[name].append(data)
                with open("new.json", "w") as f:
                    json.dump(var, f)



save_button = tk.Button(text="Save\nthe\nresults", bg="green", height=10, width=15, relief=tk.RAISED, bd=3,
                        activebackground="green", activeforeground="black", command=save_func)
save_button.grid(row=1, column=2)


def change_color():# the function changes the bg color of button every 2 sec.
    global color
    color = colors_list[randint(0, 6)]
    button.config(bg=color)
    win.after(2000, change_color)

#three line below calls the all functions in the code which works in recursion
win.after(2000, change_color)
win.after(2000, red_color_time)
win.after(2000, average_value)
win.mainloop()