#!/usr/bin/python

import tkinter

frame_width  = 800
frame_height = 400

top = tkinter.Tk()
top.title("The-for-you-decider!")
top.minsize(width=frame_width, height=frame_height)

main_frame = tkinter.Frame(top, bg="#1C1C1C")
main_frame.place(width=frame_width, height=frame_height, x=0, y=0)

fastmode_button = tkinter.Button(main_frame, text="fastmode")
fastmode_button.pack()

listmode_button = tkinter.Button(main_frame, text="listmode")
listmode_button.pack()

exit_button = tkinter.Button(main_frame, text="exit")
exit_button.pack()

top.mainloop()
