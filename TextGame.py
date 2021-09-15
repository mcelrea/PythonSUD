import os
import time
from colorama import Fore
from colorama import Style
from colorama import Back

#variables
current_room = "entry room"
crowbar = False
logbook = False
passcode = False

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
    print("living room")
    print("")
    choice = input("Enter choice: ")
    if(choice == "kitchen"):
        current_room = "kitchen"
    if(choice == "living room"):
        current_room = "living room"

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

def livingRoom():
    clear()
    global current_room
    global logbook
    print("living room")

    print("Options")
    print("-----------------")
    print(f"Return to {Fore.RED}entry room{Fore.RESET}")
    print(f"Go to {Fore.RED}library{Fore.RESET}")
    if logbook == False:
        print(f"Pick up {Fore.RED}logbook{Fore.RESET}")
    print("")
    choice = input("Enter choice: ")
    if(choice == "entry room"):
        current_room = "entry room"
    if(choice == "library"):
        current_room = "library"
    if(choice == "logbook"):
        if logbook == False:
            print("You picked up the logbook!!!")
        else:
            print("You already have the logbook dummy!")
        logbook = True;
        time.sleep(2)

def library():
    clear()
    global current_room
    global passcode
    print("library")

    print("Options")
    print("-----------------")
    print(f"Return to {Fore.RED}living room{Fore.RESET}")
    if logbook == False:
        print(f"Pick up {Fore.RED}passcode{Fore.RESET}")
    print("")
    choice = input("Enter choice: ")
    if(choice == "living room"):
        current_room = "living room"
    if(choice == "passcode"):
        if passcode == False:
            print("You picked up the passcode!!!")
        else:
            print("You already have the passcode dummy!")
        passcode = True;
        time.sleep(2)


#Begin Main Program
while True:
    if(current_room == "entry room"):
        entry_room()
    if(current_room == "kitchen"):
        kitchen()
    if(current_room == "basement"):
        basement()
    if(current_room == "living room"):
        livingRoom()
    if(current_room == "library"):
        library()