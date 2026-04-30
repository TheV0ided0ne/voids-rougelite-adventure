'''
     pyinstaller --onefile --windowed main.py (Arch Linux)

to install, use this command above in the terminal
and it will give an executable application file!
'''

from classes import Ranger, Fighter, Rouge, Warrior, Mage
import inventory

print("Welcome to Void's Average Rougelite Adventure!")
print("Please select your class!")
print("")
print("Warrior [1]")
print("Ranger [2]")
print("Fighter [3]")
print("Rouge [4]")
print("Mage [5]")

choice = int(input("> "))

class_map = {
    1: Warrior,
    2: Ranger,
    3: Fighter,
    4: Rouge,
    5: Mage
}

if choice in class_map:
    player = class_map[choice]()
    print(f"Here are your starting statistics for the class: {player}")


print("Game started!")
print("If you need to use a certain command but forgot how to do it, do 'help' in the terminal")

while True:
    command = input("\n> ").strip().lower()

    if command == "help":
        print("\n---Command List---")
        print("numbers 1-9: selective options that progress the game!")
        print("help: displays this command list")
        print("inventory: displays entire inventory")
        print("stats: displays all class statistics and skill points")

    elif command == "inventory":
        inventory.display()

    elif command == "stats":
        print(f"Here are your stats : {player}")
        print(f"Here are your skill points: {player.skillpoints}")

    elif command == "advance":
        print("You continue onwards!")
        break

    else:
        print("invalid option, please try again")



