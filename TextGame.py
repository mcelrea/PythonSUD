import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back

#variables
current_room = "entry room"
crowbar = False

#function definitions
#rooms, helper functions
def clear():
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def entry_room():
    clear()
    global current_room
    #print(f"{Fore.BLUE}{Back.CYAN}entry {Back.RESET}{Fore.GREEN} room{Style.RESET_ALL}")
    print(f"{Fore.RED}{Back.CYAN}entry{Fore.RESET}{Back.RESET} {Fore.GREEN}room{Fore.RESET}")

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
    print("basement")
    print("")
    choice = input("Enter choice: ")
    if(choice == "entry room"):
        current_room = "entry room"
    if(choice == "basement"):
        current_room = "basement"

def basement():
    clear()
    global current_room
    global crowbar
    print("basement")

    print("Options")
    print("-----------------")
    print(f"Return to {Fore.RED}kitchen{Fore.RESET}")
    if crowbar == False:
        print(f"Pick up {Fore.RED}crowbar{Fore.RESET}")
    print("")
    choice = input("Enter choice: ")
    if(choice == "kitchen"):
        current_room = "kitchen"
    if(choice == "crowbar"):
        if crowbar == False:
            print("You picked up the crowbar!!!")
        else:
            print("You already have the crowbar dummy!")
        crowbar = True;
        time.sleep(2)



#Begin Main Program
while True:
    if(current_room == "entry room"):
        entry_room()
    if(current_room == "kitchen"):
        kitchen()
    if(current_room == "basement"):
        basement()