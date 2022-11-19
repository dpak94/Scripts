# In Project V3, the program reads the keyword input by the user and proceeds to open the corresponding files using their mapped links.
import csv, os, time

while True:
    keyWord = input("Enter the command: ").lower().lstrip().rstrip()
    if keyWord == 'c':
        with open(r"./src/codingPaths.csv", "rt") as File:
            FileLink = list(csv.reader(File))
        for char in FileLink:
            os.startfile("\"" + str(char) + "\"")
    elif keyWord in ["", "quit", "q", "close", "cls", "exit"]:
        print("Quitting.......")
        time.sleep(1.5)
        break
    else:
        with open(r"./src/filePaths.csv", "rt") as File:  # Use relative paths and open in text mode.
            FileLink = dict(csv.reader(File))
        if keyWord in FileLink.keys():
            os.startfile("\"" + FileLink.get(keyWord) + "\"")