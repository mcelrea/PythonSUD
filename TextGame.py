import os
from colorama import Fore
from colorama import Style
from colorama import Back

#variables
current_room = "entry room"

#function definitions
#rooms, helper functions
def clear():
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def printColored(r,g,b,text):
    print(colored(r,g,b,text))

def printBlack(text):
    print(colored(0,0,0,text))

def entry_room():
    clear()
    global current_room
    #print(f"{Fore.BLUE}{Back.CYAN}entry {Back.RESET}{Fore.GREEN} room{Style.RESET_ALL}")
    print("entry room")

    print("Options")
    print("-----------------")
    print("kitchen")
    print("")
    choice = input("Enter choice: ")
    if(choice == "kitchen"):
        current_room = "kitchen"


def kitchen():
    clear()
    global current_room
    print("kitchen")

    print("Options")
    print("-----------------")
    print("entry room")
    print("")
    choice = input("Enter choice: ")
    if(choice == "entry room"):
        current_room = "entry room"

#Begin Main Program
while True:
    if(current_room == "entry room"):
        entry_room()
    if(current_room == "kitchen"):
        kitchen()