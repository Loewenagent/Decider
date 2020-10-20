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
    print("\nHallo.\nDu kannst dich also nicht entscheiden. Alles klar.\n")

    while(True):
        print("\nWillst den Schnellmodus verwenden, oder Listen erstellen und bearbeiten?")
        print("- fastmode:      Schnellmodus")
        print("- listmode:      Listenmodus")
        print("- exit:          Beenden")
        print("- help           Hilfe anzeigen")

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
            print("Fehler: Command wurde nicht gefoundet.\n\n")

# Main method - starts the application ===================
start_app()

time.sleep(2)
