# Import-Commands
import json
import methodes

def help():
    print("\nDo you want to create, edit or delete a list?")
    print("- new <listname>       create new list")
    print("- show                 show all lists")
    print("- show <listname>      show content of 'listname'")
    print("- edit <listname>      edit 'listname' (captain obvious)")
    print("- use <listname>       get one random item from 'listname'")
    print("- del <listname>       delete 'listname'")
    print("- back                 back to the main menu")
    print("- exit                 close the application")
    print("- help                 show this help message")

def start(data_file_path):
    print("\n= Initialize listmode =\n\nFollowing lists were found:")

    data = methodes.load(data_file_path)

    methodes.show_lists(data)

    help()

    listmode_flag = True
    while(listmode_flag):
        user_input = input("\n>> ")

        list = []

        # create new list
        if "new " in user_input:
            if user_input.replace("new ", "") == "":
                print("Please name a listname.")
            else:
                listname = user_input.replace("new ", "")

                if methodes.check_listname(listname, data_file_path):
                    user_input = input("A list with this name already exists, do you want to overwrite it? y/n")

                    while(True):
                        if user_input == "j":
                            print("What should be stored in the list?\n")
                            list = methodes.edit_list(list, listname, data, data_file_path)
                            break
                        elif user_input == "n":
                            print("Exited overwriting list.")
                            break
                        else:
                            print("Error: Command not found")

                else:
                    print("What should be stored in the list?\n")
                    list = methodes.edit_list(list, listname, data, data_file_path)

        # show all existing lists
        elif "show" == user_input:
            methodes.show_lists(data)

        # show content of a specific list
        elif "show " in user_input:
            if user_input.replace("show ", "") == "":
                print("Please give a listname.")
            else:
                listname = user_input.replace("show ", "")

            if methodes.check_listname(listname, data_file_path):
                list = data[listname]
                methodes.show(list)
            else:
                print("A list with this name doesn't exist. Try another name.")

        # edit a list
        elif "edit " in user_input:
            if user_input.replace("edit ", "") == "":
                print("Please give a listname.")
            else:
                listname = user_input.replace("edit ", "")

                # checks if the list exists
                if methodes.check_listname(listname, data_file_path):
                    list = data[listname]

                else:
                    print(f"A list with this name doesn't exist. Try another name.")
                    continue

                # shows all items in the list
                methodes.show(list)

                # editing of the list
                list = methodes.edit_list(list, listname, data, data_file_path)

                print("You are in listmode again.")

        # get a random selection from a list
        elif "use " in user_input:
            if user_input.replace("use ", "") == "":
                print("Please give a listname.")
            else:
                listname = user_input.replace("use ", "")

                if methodes.check_listname(listname, data_file_path):
                    methodes.random_selector(list)

                else:
                    print(f"A list with this name doesn't exist. Try another name.")
                    continue

        # delete a list
        elif "del " in user_input:
            if user_input.replace("del ", "") == "":
                print("Please give a listname.")
            else:
                listname = user_input.replace("del ", "")

                print("Do you really want to delete the list? y/n")

                while(True):
                    user_input = input(">> ")

                    if user_input == "j":
                        data.pop(listname)
                        methodes.save(data, data_file_path)
                        print("Well, the list has been deleted.")
                        break

                    elif user_input == "n":
                        print("Exited deletion.")
                        break

                    else:
                        print("Error: Command not found\n\n")

        # return to the main menu
        elif "back" == user_input:
            print("Do you really want to exit listmode? y/n")

            while(True):
                user_input = input(">> ")

                if user_input == "j":
                    listmode_flag = False
                    break

                elif user_input == "n":
                    print("Exit existed")
                    break

                else:
                    print("Error: Command not found\n\n")

        # exit the application
        elif "exit" == user_input:
            exit_app()

        # shows all valid commands
        elif user_input == "help":
            help()

        # no valid command
        else:
            print("Error: Command not found\n\n")
