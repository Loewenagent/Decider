# Import-commands
import json
import methodes

def help():
    print("Valid Befehle:")
    print("- new <Element>          'Element' zur Liste hinzufügen")
    print("- del <Element>          'Element' aus der Liste entfernen")
    print("- store <Listenname>     Liste als 'Name' speichern")
    print("- show                   Liste anzeigen")
    print("- continue               Bearbeitung der Liste beenden und zufälliges Element ausgeben lassen.")
    print("- back                   Back to the Hauptmenü")
    print("- exit                   das Programm completely schließen")
    print("- help                   Hilfe anzeigen ")

def start(data_file_path):
    print("\n= Schnellmodus wurde eingeleitet =\n")

    # Method spezific variable
    liste = []

    help()

    while(True):
        # get input
        user_input = input("\n>> ")

        # add new item
        if "new " in user_input:
            if user_input.replace("new ", "") == "":
                print("Bitte gib ein Element zum Hinzufügen an.")
                continue
            else:
                liste = methodes.new_element(liste, user_input)

        # delete item
        elif "del " in user_input:
            if user_input.replace("del ", "") == "":
                print("Bitte gib ein Element zum Entfernen an.")
                continue
            else:
                liste = methodes.del_element(liste, user_input)

        # save list
        elif "store " in user_input:
            if user_input.replace("store ", "") == "":
                print("Bitte gib einen Listennamen ein.")
            else:
                listname = user_input.replace("store ", "")

                if methodes.check_listname(listname, data_file_path):
                    user_input = input("Eine Liste mit diesem Namen existiert bereits, willst du sie überschreiben? j/n ")

                    while(True):
                        if user_input == "j":
                            data = methodes.load(data_file_path)

                            print("Speichervorgang...")

                            data.update({listname: liste})

                            methodes.save(data, data_file_path)

                            print(f"Liste {listname} wurde gespeichert.")
                            break

                        elif user_input == "n":
                            print("Überschreiben der Liste abgebrochen.")
                            break
                        else:
                            print("Command wurde nicht gefoundet.")
                            continue

                else:
                    data = methodes.load(data_file_path)

                    print("Speichervorgang...")

                    data.update({user_input: liste})

                    methodes.save(data, data_file_path)

                    print(f"Liste {listname} wurde gespeichert.")

        # show current list content
        elif user_input == "show":
            methodes.show(liste)

        # close editing of list and continue with random selection
        elif user_input == "use":
            if len(liste) == 0:
                print("Mensch funny Minjung, du hast ja gar keine Element in der Liste! Füg mal lieber noch was zu...")
            else:
                # selects a random item
                methodes.random_selector(liste)
                break

        # abort fastmode and return to main menu
        elif user_input == "back":
            break

        # exit the application
        elif user_input == "exit":
            methodes.exit_app()

        # shows all valid commands
        elif user_input == "help":
            help()

        # no valid command
        else:
            print("Fehler: Command wurde nicht gefoundet.\n\n")

    print("Verlasse den Schnellmodus\n")
