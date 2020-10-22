# Import-commands
import json
import methodes

def help():
    print("Valid commands:")
    print("- new <item>             add new 'item' to current list")
    print("- del <item>             remove 'item' from current list")
    print("- store <listname>       save current list as 'listname'")
    print("- show                   show content of current list")
    print("- continue               end editing of list and get a random item back")
    print("- back                   back to the main menu")
    print("- exit                   close the application")
    print("- help                   show this help message")

def start(data_file_path):
    print("\n= Initialize fastmode =\n")

    # Method spezific variable
    list = []

    help()

    while(True):
        # get input
        user_input = input("\n>> ")

        # add new item
        if "new " in user_input:
            if user_input.replace("new ", "") == "":
                print("Please name an item to add.")
                continue
            else:
                list = methodes.new_item(list, user_input)

        # delete item
        elif "del " in user_input:
            if user_input.replace("del ", "") == "":
                print("Please name an item to delete.")
                continue
            else:
                list = methodes.del_item(list, user_input)

        # save list
        elif "store " in user_input:
            if user_input.replace("store ", "") == "":
                print("Please name a list.")
            else:
                listname = user_input.replace("store ", "")

                if methodes.check_listname(listname, data_file_path):
                    while(True):
                        user_input = input("A list with this name already exists. Do you want to overwrite it? y/n")

                        if user_input == "y":
                            data = methodes.load(data_file_path)

                            print("Saving in progress...")

                            data.update({listname: list})

                            methodes.save(data, data_file_path)

                            print(f"List {listname} saved.")
                            break

                        elif user_input == "n":
                            print("Overwriting list exited.")
                            break
                        else:
                            print("Error: Command not found.")
                            continue

                else:
                    data = methodes.load(data_file_path)

                    print("Saving in progress...")

                    data.update({listname: list})

                    methodes.save(data, data_file_path)

                    print(f"List {listname} is saved.")

        # show current list content
        elif user_input == "show":
            methodes.show(list)

        # close editing of list and continue with random selection
        elif user_input == "continue":
            if len(list) == 0:
                print("Well, you are a funny person, there are no items in this list yet! Better start adding some...")
            else:
                # selects a random item
                methodes.random_selector(list)
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
            print("Error: Command not found.\n\n")

    print("Exit fastmode\n")
