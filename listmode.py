# Import-Commands
import json
import methodes

def start(data_file_path):
    print("\n= Listenmodus wurde eingeleitet =\n\nFolgende Listen wurden gefunden:")

    data = methodes.load(data_file_path)

    methodes.show_lists(data)

    print("\nWillst du eine neue Liste anlegen, eine Liste bearbeiten, oder eine Liste löschen?")
    print("- new <Listenname>       neue Liste angelegen")
    print("- show                   alle vorhandenen Listen anzeigen")
    print("- show <Listenname>      Listeninhalt anzeigen")
    print("- edit <Listenname>      Liste bearbeiten")
    print("- use <Listenname>       ein Element aus der Liste ausgeben lassen")
    print("- del <Listenname>       Liste löschen")
    print("- back                   Back to the Hauptmenu")
    print("- exit                   das Programm completely schließen")
    print("- help                   Hilfe anzeigen")

    listmode_flag = True
    while(listmode_flag):
        user_input = input("\n>> ")

        liste = []

        # Liste anlegen
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

        # Alle Listen anzeigen
        elif "show" == user_input:
            methodes.show_lists(data)

        # Den Inhalt einer Liste anzeigen
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

        # Liste bearbeiten
        elif "edit " in user_input:
            if user_input.replace("edit ", "") == "":
                print("Bitte gib einen Listennamen an.")
            else:
                listname = user_input.replace("edit ", "")

                # Überprüfung, ob die Liste existiert
                if methodes.check_listname(listname, data_file_path):
                    liste = data[listname]

                else:
                    print(f"Die Liste {listname} existiert nicht. (Achte auf mögliche type errors!)")
                    continue

                # Zeigt die Elemente in der Liste an
                methodes.show(liste)

                # Bearbeitung der Liste
                liste = methodes.edit_list(liste, listname, data, data_file_path)

                print("Du bist nun wieder im Listenmodus.")

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

        elif "exit" == user_input:
            exit_app()

        elif user_input == "help":
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

        else:
            print("Fehler: Command wurde nicht gefoundet.\n\n")
