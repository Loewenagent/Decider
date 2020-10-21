# Import-Commands
import platform
import os
import json
import methodes

def catch_error(data_file_path):
    # verifies the json-file; json-file gets created on non-existenz or gets repaired
    try:
        data = methodes.load(data_file_path)

    except IOError:
        print("There was no list-file found. A new one shall be created now.")

        try:
            methodes.save({"food": ["apple", "pear", "banana"], "activity": ["gaming", "watching anime", "masturbating"]}, data_file_path)

        except:
            print("Nope, didn't work for some reason, create one for yourself.")
            exit()

    except json.decoder.JSONDecodeError:
        print("You know, the list file is broken somehow, so it's getting reset.")

        try:
            methodes.save({"food": ["apple", "pear", "banana"], "activity": ["gaming", "watching anime", "masturbating"]}, data_file_path)

        except:
            print("Nope, reset didn't work because of reasons, go repair it alone. Lol.")
            exit()

def get_data_file():
    # get data file path ====================
    if platform.system() == "Linux":
        data_file_path = os.path.abspath("data.json")
    elif platform.system() == "Windows":
        data_file_path = os.path.abspath(__file__).replace(__file__, "data.json")
    elif platform.system() == "Darwin":
        print("Mac is whack, so we don't support it.")
        methodes.exit_app()

    catch_error(data_file_path)

    return data_file_path
