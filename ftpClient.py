import os
from ftplib import FTP
import sys
import getpass
from tkinter import *

def clearScreen():
    os.system('cls')

def connect(host, user, passwd):
    try:
        ftp = FTP(host)
        ftp.login(user=user, passwd=passwd)
        print("Successfully connected to " + host + " as " + user + "...")
        return ftp
    except:
        print("Unable to connect...")
        sys.exit()

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, 'rb'), 1024)

def showCommands():
    print("\nCommands:\n-------------")
    print("cd <dir>       : change current working directory")
    print("ls             : output the current working directory listing")
    print("rm <file>      : delete file")
    print("rmd <dir>      : delete directory")
    print("mkdir <dir>    : create new directory")
    print("dl <file>      : download file")
    print("ul <file>      : upload file")
    print("rn <old> <new> : rename old file to new file")
    print("clear          : clears screen")
    print("exit           : disconnect\n")

class App:
    def __init__(self, master):
        self.loginFrame = Frame(master)
        self.loginFrame.pack()

        Label(loginFrame, text="Host: ").pack()
        self.hostEntry = Entry(loginFrame)
        self.hostEntry.pack()
        Label(loginFrame, text="Username: ").pack()
        self.usernameEntry = Entry(loginFrame)
        self.usernameEntry.pack()
        Label(loginFrame, text="Password: ").pack()
        self.passwordEntry = Entry(loginFrame, show="*")
        self.passwordEntry.pack()



def main():
    clearScreen()
    print("Welcome to the Python FTP Client")
    host = input("Host: ")
    user = input("Username: ")
    passwd = getpass.getpass("Password: ")
    ftp = connect(host, user, passwd)
    print("Use 'help' to show commands\n")
    command = input(">> ")
    while command != "exit":
        if command == "help":
            showCommands()
            command = input(">> ")
            continue
        try:
            if command[:2] == 'cd':
                # change dir
                d = command.split(' ')[1]
                ftp.cwd(d)
            elif command[:2] == 'rm' and len(command.split(' ')[0]) == 2:
                # remove file
                f = command.split(' ')[1]
                ftp.delete(f)
            elif command[:2] == 'dl':
                # download file
                f = command.split(' ')[1]
                ftp.retrbinary("RETR " + f, open("download_" + f, 'wb').write)
            elif command[:2] == 'ls':
                # show listing
                ftp.dir()
            elif command[:2] == 'rn':
                # rename file
                old = command.split(' ')[1]
                new = command.split(' ')[2]
                ftp.rename(old, new)
            elif command[:2] == 'ul':
                # upload new file
                f = command.split(' ')[1]
                upload(ftp, f)
            elif command[:3] == 'rmd':
                # remove directory
                d = command.split(' ')[1]
                ftp.rmd(d)
            elif command[:5] == 'mkdir':
                # make new directory
                d = command.split(' ')[1]
                ftp.mkd(d)
            elif command == "clear":
                # clear screen
                clearScreen()
            else:
                print("Invalid command. Try again...\n")
        except:
            print("Invalid command. Try again...\n")
        command = input(">> ")
    try:
        ftp.quit()
    except:
        pass
    sys.exit()


if __name__ == "__main__":
    main()