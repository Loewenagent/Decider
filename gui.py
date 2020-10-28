#!/usr/bin/python

import tkinter
import methodes

# Variables ===========================================================================================================
list = []

# Methodes ============================================================================================================
def new_item():
    methodes.new_item(list, input_field.get())

def del_item():
    pass

# =====================================================================================================================
# GUI =================================================================================================================
# Color scheme
yellow  = "#b58900"
orange  = "#cb4b16"
red     = "#dc322f"
magenta = "#d33682"
violet  = "#6c71c4"
blue    = "#268bd2"
cyan    = "#2aa198"
green   = "#859900"

frame_width   = 800
frame_height  = 400

button_width  = 300
button_height = 25

top = tkinter.Tk()
top.title("The-for-you-decider!")
top.minsize(width=frame_width, height=frame_height)
top.maxsize(width=frame_width, height=frame_height)

# =================================================================================================
# MAIN FRAME for editing general thinks like background color of the whole application ============
main_frame = tkinter.Frame(top, bg="#1C1C1C")
#main_frame.place(width=frame_width, height=frame_height, x=0, y=0)

# Title ===========================================================================================
main_frame_text = tkinter.Text(main_frame, bg="#1C1C1C", fg="White", font=("Arial", 32), bd="0")
main_frame_text.insert("1.0", "The-for-you-decider!")
main_frame_text.tag_add("start", "1.0", "1.20")
main_frame_text.tag_config("start", justify="center")
main_frame_text.configure(state="disabled")
main_frame_text.place(width=400, height=50, x=frame_width / 2 - 200, y=50)

# MAIN SCREEN BUTTONS =============================================================================
# fastmode button
fastmode_button = tkinter.Button(main_frame, text="fastmode")
fastmode_button.place(width=button_width, height=button_height, x=frame_width / 2 - button_width / 2, y=130)

# listmode button
listmode_button = tkinter.Button(main_frame, text="listmode")
listmode_button.place(width=button_width, height=button_height, x=frame_width / 2 - button_width / 2, y=160)

# exit button
exit_button = tkinter.Button(main_frame, text="exit", command=methodes.exit_app)
exit_button.place(width=button_width, height=button_height, x=frame_width / 2 - button_width / 2, y=350)

# =================================================================================================
# FASTMODE FRAME ==================================================================================
fastmode_frame = tkinter.Frame(top, bg="#1C1C1C")
fastmode_frame.place(width=frame_width, height=frame_height, x=0, y=0)

# Title ===========================================================================================
fastmode_frame_text = tkinter.Text(fastmode_frame, bg="#1C1C1C", fg="White", font=("Arial", 20), bd="0")
fastmode_frame_text.insert("1.0", "Fastmode")
fastmode_frame_text.tag_add("start", "1.0", "1.20")
fastmode_frame_text.tag_config("start", justify="center")
fastmode_frame_text.configure(state="disabled")
fastmode_frame_text.place(width=400, height=50, x=frame_width / 2 - 200, y=20)

# Entry-Field =====================================================================================
user_input = tkinter.StringVar()
input_field = tkinter.Entry(fastmode_frame, font=("Arial", 12), textvariable=user_input)
input_field.place(width=200, height=20, x=50, y=100)

# add-Button
add_button = tkinter.Button(fastmode_frame, text="add", bg="White", command=new_item)
add_button.place(width=95, height=20, x=50, y=130)

del_button = tkinter.Button(fastmode_frame, text="delete", command=del_item)
del_button.place(width=95, height=20, x=155, y=130)

top.mainloop()
