# The code in this project was written with this YouTube video as reference. 
# Minor changes were made to make the script easier to use.
# Credit: https://www.youtube.com/watch?v=jS2LuG1p8Vw&t=46s


import os
import sys
import winreg
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def find_python():
    python_path = sys.executable
    python_dir = os.path.dirname(python_path)
    pythonw_path = os.path.join(python_dir, "pythonw.exe")
    if os.path.exists(pythonw_path):
        return pythonw_path
    else:
        return python_path

def main():
    # create variables for basic paths
    cwd = os.getcwd()
    python_exe = find_python()

    # create variables for information about the script to be added
    script_action = "Create_New_Project"
    script_description = "&" + " ".join(script_action.split('_'))
    script_to_add = f'"{cwd}\\new_project.pyw"'

    # Registry path for windows right click context menu items.
    key_path = r"Directory\\Background\\shell\\" + script_action

    # Create a folder for the script to add.
    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
    winreg.SetValue(key, "", winreg.REG_SZ, script_description)

    key1 = winreg.CreateKey(key, r"command")
    winreg.SetValue(key1, "", winreg.REG_SZ, python_exe + " " + script_to_add)

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
