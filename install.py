# The code in this project was written with this YouTube video as reference. 
# Minor changes were made to make the script easier to use.
# Credit: https://www.youtube.com/watch?v=jS2LuG1p8Vw&t=46s


import os
import sys
import winreg


def main():
    # create variables for basic paths
    cwd = os.getcwd()
    python_exe = sys.executable

    # create variables for information about the script to be added
    script_action = "Create_New_Project"
    script_description = "&" + " ".join(script_action.split('_'))
    script_to_add = f'"{cwd}\\file_organiser.py"'

    # Registry path for windows right click context menu items.
    key_path = r"Directory\\Background\\shell\\Organiser"

    # Create a folder for the script to add.
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
    winreg.SetValue(key, '', winreg.REG_SZ, script_description)

    key1 = winreg.CreateKey(key, r"command")
    winreg.SetValue(key1, winreg.REG_SZ, python_exe + script_to_add)

if __name__ == "__main__":
    main()
