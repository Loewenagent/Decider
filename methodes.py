# Import-Commands
import json
import time
import random

# Methoden ================================================
# Lädt die Json-Datei
def load(data_file_path):
    with open(data_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# Speichert die Listen un die Json-Datei
def save(data, data_file_path):
    with open(data_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

# Zeigt alle Listen an
def show_lists(data):
    if len(data.keys()) == 0:
        print("Du hast es geschafft, mehr Listen zu löschen, als zu erstellen, deswegen gibt es jetzt keine Listen mehr.")
    else:
        for element in data.keys():
            print(f"- {element}")

# Überprüft
def check_listname(listname, data_file_path):
    data = load(data_file_path)

    if listname in data.keys():
        return True

    else:
        return False

def random_selector(liste):
    print("\nGut, dann haben wir jetzt alle Sachen. Nun wird ein Element zufällig ausgewählt.")

    # Ein zufälliger Index wird ermittelt und das Ergebnis ausgegeben
    selection = liste[random.randint(0, len(liste) - 1)]

    print(f"Und die ausgewählte Sache iiiiiiiist: Huiuiuiui, {selection}! Hurra!\n\nJetzt viel Spaß damit!")

    if len(liste) == 1:
        print("Wer hätte es gedacht, es steht ja sowieso nur das eins Element in der Liste... -_-")

def new_element(liste, element):
    element = element.replace("new ", "")
    liste.append(element)
    print(f"{element} wurde der Liste hinzugefügt.")
    return liste

def del_element(liste, element):
    element = element.replace("del ", "")

    if element in liste:
        liste.remove(element)
        print(f"{element} wurde aus der Liste entfernt.")
    else:
        print("Sorry, das steht nicht in der Liste. (Achte auf mögliche Schreibfehler!)")

    return liste

def show(liste):
    if len(liste) == 0:
        print("Es sind noch keine Elemente in der Liste.")
    elif len(liste) == 1:
        print(f"Bis jetzt steht nur {liste[0]} in der Liste.")
    else:
        print("\nIn der Liste stehen bis jetzt:")

        for element in liste:
            print(f"- {element}")

        print("")

def edit_list(liste, listname, data, data_file_path):
    print("Valid Befehle:")
    print("- new <Element>          'Element' zur Liste hinzufügen")
    print("- del <Element>          'Element' aus der Liste entfernen")
    print("- show                   Liste anzeigen")
    print("- continue               Bearbeitung der Liste beenden.")
    print("- exit listmode          Listenmodus ohne Speichern verlassen")
    print("- exit                   Application beenden")
    print("- help                   Hilfe anzeigen ")

    while(True):
        user_input = input("\n>> ")

        # Element wird hinzugefügt
        if "new " in user_input:
            if user_input.replace("new ", "") == "":
                print("Bitte gib ein Element zum Hinzufügen an.")
                continue
            else:
                liste = new_element(liste, user_input)

        # Element wird gelöscht
        elif "del " in user_input:
            if user_input.replace("del ", "") == "":
                print("Bitte gib ein Element zum Entfernen an.")
                continue
            else:
                liste = del_element(liste, user_input)

        # Liste wird angezeigt
        elif user_input == "show":
            show(liste)

        # Liste wird gespeichert und es wird zum Listenmodus zurückgekehrt
        elif user_input == "continue":
            if listname in data:
                print("Liste wird überschrieben...")
                data[listname] = liste
                print(f"Liste {listname} wurde überschrieben.")

            else:
                print("Neue Liste wird angelegt...")
                data.update({listname: liste})
                print(f"Neue Liste {listname} wurde angelegt.")

            save(data, data_file_path)

            print("Liste wurde gespeichert")

            break

        # Listenmodus wird beendet und zum Hauptmenu zurückgekehrt
        elif user_input == "exit listmode":
            tempExit = True
            break

        # Die Application wird beendet
        elif user_input == "exit":
            exit_app()

        elif user_input == "help":
            print("Valid Befehle:")
            print("- new <Element>          'Element' zur Liste hinzufügen")
            print("- del <Element>          'Element' aus der Liste entfernen")
            print("- show                   Liste anzeigen")
            print("- continue               Bearbeitung der Liste beenden.")
            print("- exit listmode          Listenmodus ohne Speichern verlassen")
            print("- exit                   Application beenden")
            print("- help                   Hilfe anzeigen")

        # Invalid Command
        else:
            print("Fehler: Command wurde nicht gefoundet.\n\n")

    return liste

def exit_app():
    print("Willst du das Programm wirklich beenden? j/n")

    while(True):
        user_input = input(">> ")

        if user_input == "j":
            print("Alter, du Kek. Jetzt beendet sich das Programm lol.")
            time.sleep(2)
            exit(0)

        elif user_input == "n":
            print("Beendigung abgebrochen")
            break

        else:
            print("Fehler: Command wurde nicht gefoundet.\n\n")
