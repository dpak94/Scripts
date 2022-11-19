#! py3
# A Python program that opens all the requisite apps and folder(s) for private browsing.
import os, time
def printer():
    print("Environments :\nCoding Environment : c | Pirate Mode : p\n\nBrowsers:\nFireFox : moz | WaterFox : wat \n\nOffice Tools :\nWord : w | Excel : e  PowerPoint : p \nUtilities :\n\nTorrent : torr | Revo Uninstaller : revo")
    print("Misc :\nExpenses : expenses | DocsFolder : docs | ")
    print("")
    print("#"*100)

while True:
    printer()
    classe = input("Enter the command : ").lower()
    if classe in ["", "quit", "q", "close"]:
        print("Quitting....")
        time.sleep(1)
        break

    # Environments
    elif classe == 'p': # Pirate Mode
        os.startfile(
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

    elif classe == 'c':  # Coding Environment
        os.startfile(r"C:\Users\deepak\AppData\Local\GitHubDesktop\GitHubDesktop.exe")
        os.startfile(r"C:\Users\deepak\Desktop\Visual Studio Code.lnk")
        os.startfile(r"C:\Users\deepak\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Navigator (anaconda3).lnk")
        os.startfile("E:\\")
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk")

    # Browsers
    elif classe == 'moz': # Mozilla Firefox
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Firefox.lnk")
    elif classe == 'wat': # WaterFox Browser
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Waterfox.lnk")

    # MS Office Apps
    elif classe == 'excel': # MS Excel
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
    elif classe == 'word': # MS Word
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
    elif classe == 'ppt': # Powerpoint
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")

    # Utilities
    elif classe == 'torr': # QbitTorrent
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\qBittorrent\qBittorrent.lnk")
    elif classe == 'revo': # Revo Uninstaller
        os.startfile(
            r"C:\Program Files\VS Revo Group\Revo Uninstaller\RevoUnin.exe")
    elif classe == 'rec': # Recuva File Recovery Software
        os.startfile(r"C:\Program Files\Recuva\recuva64.exe")
    elif classe == 'gitbash': # Git Bash
        os.startfile(r"C:\Program Files\Git\git-bash.exe")
    elif classe == 'vlc': # VLC Media Player
        os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
    elif classe == 'music': # Amazon Music
        os.startfile(
            r"C:\Users\deepak\AppData\Local\Amazon Music\Amazon Music.exe")
    elif classe == 'gt': # Green Tunnel
        os.startfile(
            r"C:\Users\deepak\AppData\Local\green-tunnel\green-tunnel.exe")
    elif classe == 'gitdesk': # GitHub Desktop
        os.startfile(
            r"C:\Users\deepak\AppData\Local\GitHubDesktop\GitHubDesktop.exe")
    elif classe == 'idle10': # Python IDLE 3.10.9
        os.startfile(
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.10\IDLE (Python 3.10 64-bit).lnk")
    elif classe == 'idle11': # Python IDLE 3.10.9
        os.startfile(
            r"C:\Users\deepak\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11\IDLE (Python 3.11 64-bit).lnk")

    # Folder Shortcuts
    elif classe == 'gitrep': # GitHub Local Repo
        os.startfile(r'E:\Repo\GitHub')
    elif classe == 'media': # Movies & Series Folder
        os.startfile(r'F:\Media')
    elif classe == 'notes': # Python Notes
        os.startfile(r"E:\Repo\GitHub\PythonNotes")
    elif classe == 'pymods': # Modules
        os.startfile(r"E:\Repo\GitHub\PythonNotes\modules")
    elif classe == 'cali':
        os.startfile(r"C:\Program Files\Calibre2\calibre.exe")
    elif classe == 'docs':
        os.startfile(r"D:\Important Docs")
    elif classe == 'expenses':
        os.startfile(r"D:\Important Docs\Expenses-2022.xlsx")
    