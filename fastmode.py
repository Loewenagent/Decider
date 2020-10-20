# Import-Commands
import json
import methodes

def start(data_file_path):
    print("\n= Schnellmodus wurde eingeleitet =\n")

    temp_exit = False
    while(True):
        # Methoden spezifische Variablen
        liste = []

        # Phase 1: Temporäre Liste erstellen ==============
        print("Valid Befehle:")
        print("- new <Element>          'Element' zur Liste hinzufügen")
        print("- del <Element>          'Element' aus der Liste entfernen")
        print("- store Name             Liste als 'Name' speichern")
        print("- show                   Liste anzeigen")
        print("- use                    Bearbeitung der Liste beenden und zufälliges Element ausgeben lassen (Liste kann danach nicht mehr gespeichert werden)")
        print("- back                   Back to the Hauptmenü")
        print("- exit                   das Programm completely schließen")
        print("- help                   Hilfe anzeigen")

        while(True):
            # Eingabe des Spielers wird gespeichert
            user_input = input("\n>> ")

            # Element wird hinzugefügt
            if "new " in user_input:
                if user_input.replace("new ", "") == "":
                    print("Bitte gib ein Element zum Hinzufügen an.")
                    continue
                else:
                    liste = methodes.new_element(liste, user_input)

            # Element wird gelöscht
            elif "del " in user_input:
                if user_input.replace("del ", "") == "":
                    print("Bitte gib ein Element zum Entfernen an.")
                    continue
                else:
                    liste = methodes.del_element(liste, user_input)

            # Liste wird gespeichert
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

            # Liste wird angezeigt
            elif user_input == "show":
                methodes.show(liste)

            # Bearbeitung der Liste wird beendet
            elif user_input == "use":
                if len(liste) == 0:
                    print("Mensch funny Minjung, du hast ja gar keine Element in der Liste! Füg mal lieber noch was zu...")
                else:
                    temp_exit = False
                    break

            # Der Schnellmodus wird abgebrochen und es wird zum Hauptmenu zurückgekehrt
            elif user_input == "back":
                temp_exit = True
                break

            # Das Programm wird geschlossen
            elif user_input == "exit":
                exit_app()

            elif user_input == "help":
                print("Valid Befehle:")
                print("- new <Element>          'Element' zur Liste hinzufügen")
                print("- del <Element>          'Element' aus der Liste entfernen")
                print("- store <Listenname>     Liste als 'Name' speichern")
                print("- show                   Liste anzeigen")
                print("- continue               Bearbeitung der Liste beenden und zufälliges Element ausgeben lassen.")
                print("- back                   Back to the Hauptmenü")
                print("- exit                   das Programm completely schließen")
                print("- help                   Hilfe anzeigen ")

            # Kein gültiger Command
            else:
                print("Fehler: Command wurde nicht gefoundet.\n\n")

        # Überprüfung, ob die zweite Phase ausgeführt werden soll
        if temp_exit == False:
            # Phase 2: Ein Element wird ausgewählt ============
            methodes.random_selector(liste)
            return

        if temp_exit == True:
            print("Verlasse den Schnellmodus\n")
            break
