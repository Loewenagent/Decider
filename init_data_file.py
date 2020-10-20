# Import-Commands
import platform
import os
import json
import methodes

def catch_error(data_file_path):
    # Datei wird überprüft und bei Nichtexistenz erstellt beziehungsweise repariert
    try:
        data = methodes.load(data_file_path)

    except IOError:
        print("Es wurde keine Listen-Datei gefunden. Eine neue wird erstellt.")

        try:
            methodes.save({"essen": ["apfel", "birne", "banane"], "beschäftigungen": ["zocken", "anime schauen", "masturbieren"]}, data_file_path)

        except:
            print("Ne äh, irgendwie ging das nicht, mach mal ne eigene, du Kek.")
            exit()

    except json.decoder.JSONDecodeError:
        print("Jo, die Listendatei ist örgendwie puttputt gegangen, deswegen wird sie nun zurückgesetzt.")

        try:
            methodes.save({"essen": ["apfel", "birne", "banane"], "beschäftigungen": ["zocken", "anime schauen", "masturbieren"]}, data_file_path)

        except:
            print("Ja ne, ging nich so ganz, musst du selber reparieren. Lol.")
            exit()

def get_data_file():
    # Create ====================
    if platform.system() == "Linux":
        # print("Linux muss noch ausgebessert werden.")
        # methodes.exitApp()
        data_file_path = os.path.abspath("data.json") # oder os.popen("ls $PWD/data.json") # oder readlink -f data.json
    elif platform.system() == "Windows":
        data_file_path = os.path.abspath(__file__).replace(__file__, "data.json")
    elif platform.system() == "Darwin":
        print("Mac finden wir doof, deswegen geht das nicht.")
        methodes.exit_app()

    catch_error(data_file_path)

    return data_file_path
