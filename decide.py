#!/usr/bin/env python

# Import-commands =========================================
import json
import time

import init_data_file
import fastmode
import listmode
import methodes

# Initialize the path of the data-file
data_file_path = init_data_file.get_data_file()

# Method to start the application =========================
def start_app():
    print("\nHello. \nYou can't decide what to do. Alright.\n")

    while(True):
        print("\nDo you want to use fastmode or create and edit lists?")
        print("- fastmode:      Opens fastmode")
        print("- listmode:      Opens an advanced utility for managing lists")
        print("- exit:          Exit the application")
        print("- help           Show this help message")

        user_input = input("\n>> ")

        if user_input == "fastmode":
            fastmode.start(data_file_path)

        elif user_input == "listmode":
            listmode.start(data_file_path)

        elif user_input == "exit":
            methodes.exit_app()

        elif user_input == "help":
            continue

        else:
            print("Error: Command not found.\n\n")

# Main method - starts the application ===================
start_app()

time.sleep(2)
