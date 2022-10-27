import os
import tkinter as tk
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.withdraw()

file_path = askdirectory(title="select folder")
poppercommand = "python3 popper.py"
outputFile = ">> popper-output.txt"

f = open("popper-output.txt", "w")
f.write("")
f.close()

# print the popper output into a .txt file
if file_path != '':
    for current_folder in os.listdir(file_path):
        f = os.path.join(file_path, current_folder)
        if current_folder == ".DS_Store":
            continue

        os.system(poppercommand + " " + f + "/100" + " --timeout 10000" + " " + outputFile)
else:
    print("Error: Please select a folder")
