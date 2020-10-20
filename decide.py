#!/usr/bin/env python



# Import-Commands =========================================
import json
import time

import init_data_file
import fastmode
import listmode
import methodes

# Initialisierung des Pfades der Data-File
data_file_path = init_data_file.get_data_file()

# Methode zum Start der Anwendung =========================
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

# Start der Anwendung =====================================
start_app()

time.sleep(2)
