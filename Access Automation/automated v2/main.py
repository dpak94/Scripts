# A Program for lazy folks like me who'd like to open files and apps with just keystrokes instead of double-clicking on icons.
# The function files are to be imported into the main.py
import sys
sys.path.append("./src")
import files
while True:
    spam = input("Enter the command")
    files.folder_(spam) # Folders