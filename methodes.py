# Import-Commands
import json
import time
import random

# Methods ================================================
# loads the json-file
def load(data_file_path):
    with open(data_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

# stores all lists in the json-file
def save(data, data_file_path):
    with open(data_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

# shows all lists
def show_lists(data):
    if len(data.keys()) == 0:
        print("You did it. You have deleted more lists than you have created. As a result, there are no lists anymore.")
    else:
        for element in data.keys():
            print(f"- {element}")

# checks if a listname already exists
def check_listname(listname, data_file_path):
    data = load(data_file_path)

    if listname in data.keys():
        return True

    else:
        return False

# selects a random item from a list and presents it
def random_selector(liste):
    print("\nWell, now we have all items together. Let's get a random item out of that list.")

    # Ein zufälliger Index wird ermittelt und das Ergebnis ausgegeben
    selection = liste[random.randint(0, len(liste) - 1)]

    print(f"And the selected item iiiiiiiis: Yay, {selection}! Hooray!\n\nNow have fun with it!")

    if len(liste) == 1:
        print("Oh well, who could have thought that? It's not like there was only one item in the list to begin with... -_-")

# adds a new item to a list
def new_element(liste, element):
    element = element.replace("new ", "")
    liste.append(element)
    print(f"{item} was added to the list.")
    return liste

# deletes an item from a list
def del_element(liste, element):
    element = element.replace("del ", "")

    if element in liste:
        liste.remove(element)
        print(f"{item} was removed from the list.")
    else:
        print("Sorry, that is not something from the list. (Check for spelling errors!)")

    return liste

# shows all items of a list
def show(liste):
    if len(liste) == 0:
        print("There are no items in the list yet.")
    elif len(liste) == 1:
        print(f"Until now, there only is {list[0]} in the list.")
    else:
        print("\nThese items are in the list so far:")

        for element in liste:
            print(f"- {item}")

        print("")

# general method for editing a list
def edit_list(liste, listname, data, data_file_path):
    print("Valid commands:")
    print("- new <item>          add 'item' to the list")
    print("- del <item>          remove 'item' from the list")
    print("- show                   show current list")
    print("- continue               stop editing of list")
    print("- exit listmode          exit listmode without saving")
    print("- exit                   close application")
    print("- help                   show this help message")

    while(True):
        user_input = input("\n>> ")

        # add a new item
        if "new " in user_input:
            if user_input.replace("new ", "") == "":
                print("Please name an item to add.")
                continue
            else:
                liste = new_element(liste, user_input)

        # delete an item
        elif "del " in user_input:
            if user_input.replace("del ", "") == "":
                print("Please name an item to remove.")
                continue
            else:
                liste = del_element(liste, user_input)

        # shows all item from a list
        elif user_input == "show":
            show(liste)

        # save list and return to the listmode menu
        elif user_input == "continue":
            if listname in data:
                print("List gets overwritten...")
                data[listname] = liste
                print(f"List {listname} has been overwritten.")

            else:
                print("Creating new list...")
                data.update({listname: liste})
                print(f"Created new list {listname}.")

            save(data, data_file_path)

            print("List was saved.")

            break

        # close listmode and return to main menu
        elif user_input == "exit listmode":
            tempExit = True
            break

        # exit the application
        elif user_input == "exit":
            exit_app()

        # shows all valid commands
        elif user_input == "help":
            print("Valid commands:")
            print("- new <item>          add 'item' to the list")
            print("- del <item>          remove 'item' from the list")
            print("- show                   show current list")
            print("- continue               stop editing of list")
            print("- exit listmode          exit listmode without saving")
            print("- exit                   close application")
            print("- help                   show this help message")

        # no valid command
        else:
            print("Error: Command not found.\n\n")

    return liste

# method to exit the application
def exit_app():
    print("Do you really want to close the application? y/n")

    while(True):
        user_input = input(">> ")

        if user_input == "j":
            print("Well, there goes your application lol.")
            time.sleep(2)
            exit(0)

        elif user_input == "n":
            print("Exit exited")
            break

        else:
            print("Error: Command not found.\n\n")
