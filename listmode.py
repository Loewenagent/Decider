# Import-Commands
import json
import methodes

def help():
    print("\nWillst du eine neue Liste anlegen, eine Liste bearbeiten, oder eine Liste löschen?")
    print("- new <Listenname>       neue Liste angelegen")
    print("- show                   alle vorhandenen Listen anzeigen")
    print("- show <Listenname>      Listeninhalt anzeigen")
    print("- edit <Listenname>      Liste bearbeiten")
    print("- use <Listenname>       ein Element aus der Liste ausgeben lassen")
    print("- del <Listenname>       Liste löschen")
    print("- Back                   Back to the Hauptmenü")
    print("- exit                   das Programm completely schließen")
    print("- help                   Hilfe anzeigen ")

def start(data_file_path):
    print("\n= Listenmodus wurde eingeleitet =\n\nFolgende Listen wurden gefunden:")

    data = methodes.load(data_file_path)

    methodes.show_lists(data)

    help()

    listmode_flag = True
    while(listmode_flag):
        user_input = input("\n>> ")

        liste = []

        # create new list
        if "new " in user_input:
            if user_input.replace("new ", "") == "":
                print("Bitte gib einen Listennamen an.")
            else:
                listname = user_input.replace("new ", "")

                if methodes.check_listname(listname, data_file_path):
                    user_input = input("Eine Liste mit diesem Namen existiert bereits, willst du sie überschreiben? j/n ")

                    while(True):
                        if user_input == "j":
                            print("Was soll denn alles in der Liste gespeichert sein?\n")
                            liste = methodes.edit_list(liste, listname, data, data_file_path)
                            break
                        elif user_input == "n":
                            print("Überschreiben der Liste abgebrochen.")
                            break
                        else:
                            print("Command wurde nicht gefoundet.")

                else:
                    print("Was soll denn alles in der Liste gespeichert sein?\n")
                    liste = methodes.edit_list(liste, listname, data, data_file_path)

        # show all existing lists
        elif "show" == user_input:
            methodes.show_lists(data)

        # show content of a specific list
        elif "show " in user_input:
            if user_input.replace("show ", "") == "":
                print("Bitte gib einen Listennamen an.")
            else:
                listname = user_input.replace("show ", "")

            if methodes.check_listname(listname, data_file_path):
                liste = data[listname]
                methodes.show(liste)
            else:
                print("Dieser Listenname existiert nicht. Probiere another one.")

        # edit a list
        elif "edit " in user_input:
            if user_input.replace("edit ", "") == "":
                print("Bitte gib einen Listennamen an.")
            else:
                listname = user_input.replace("edit ", "")

                # checks if the list exists
                if methodes.check_listname(listname, data_file_path):
                    liste = data[listname]

                else:
                    print(f"Die Liste {listname} existiert nicht. (Achte auf mögliche type errors!)")
                    continue

                # shows all items in the list
                methodes.show(liste)

                # editing of the list
                liste = methodes.edit_list(liste, listname, data, data_file_path)

                print("Du bist nun wieder im Listenmodus.")

        # get a random selection from a list
        elif "use " in user_input:
            if user_input.replace("use ", "") == "":
                print("Bitte gib einen Listennamen an.")
            else:
                listname = user_input.replace("use ", "")

                if methodes.check_listname(listname, data_file_path):
                    methodes.random_selector(liste)

                else:
                    print(f"Die Liste {listname} existiert nicht. (Achte auf mögliche type errors!)")
                    continue

        # delete a list
        elif "del " in user_input:
            if user_input.replace("del ", "") == "":
                print("Bitte gib einen Listennamen an.")
            else:
                listname = user_input.replace("del ", "")

                print("Willst du die Liste wirklich löschen? j/n")

                while(True):
                    user_input = input(">> ")

                    if user_input == "j":
                        data.pop(listname)
                        methodes.save(data, data_file_path)
                        print("Alda Malaga, die Liste wurde gelöscht.")
                        break

                    elif user_input == "n":
                        print("Löschvorgang abgebrochen.")
                        break

                    else:
                        print("Fehler: Command wurde nicht gefoundet.\n\n")

        # return to the main menu
        elif "back" == user_input:
            print("Willst du den Listenmodus wirklich beenden? j/n")

            while(True):
                user_input = input(">> ")

                if user_input == "j":
                    listmode_flag = False
                    break

                elif user_input == "n":
                    print("Beendigung abgebrochen")
                    break

                else:
                    print("Fehler: Command wurde nicht gefoundet.\n\n")

        # exit the application
        elif "exit" == user_input:
            exit_app()

        # shows all valid commands
        elif user_input == "help":
            help()

        # no valid command
        else:
            print("Fehler: Command wurde nicht gefoundet.\n\n")
