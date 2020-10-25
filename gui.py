#!/usr/bin/python

import tkinter
import methodes

frame_width   = 800
frame_height  = 400

button_width  = 300
button_height = 25

top = tkinter.Tk()
top.title("The-for-you-decider!")
top.minsize(width=frame_width, height=frame_height)

# main frame for editing general thinks like background color of the whole application
main_frame = tkinter.Frame(top, bg="#1C1C1C")
main_frame.place(width=frame_width, height=frame_height, x=0, y=0)

# Title ===========================================================================================
main_frame_text = tkinter.Text(main_frame, bg="#1C1C1C", fg="Red", font=("Arial", 32), bd="0")
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

top.mainloop()
