'''
     pyinstaller --onefile --windowed main.py (Arch Linux)

to install, use this command above in the terminal
and it will give an executable application file!
'''

from classes import Ranger, Brawler, Rouge, Warrior, Mage
import inventory

print("Welcome to Void's Average Rougelite Adventure!")
print("Please select your class!")
print("")
print("Warrior [1]")
print("Ranger [2]")
print("Brawler [3]")
print("Rouge [4]")
print("Mage [5]")

choice = int(input("> "))

class_map = {
    1: Warrior,
    2: Ranger,
    3: Brawler,
    4: Rouge,
    5: Mage
}

if choice in class_map:
    player = class_map[choice]()
    print(f"Here are your starting statistics for the class: {player}")


print("Game started!")
print("If you need to use a certain command but forgot how to do it, do 'help' in the terminal")

print("You start within the forest of damnation, a mythical land where ramage is common, and you are always in danger.")
print("What shall you do?")

print("[1] Scavenge")
print("[2] Hunt")
print("[3] Get a grasp of your surroundings")

forest1 = input("> ").strip().lower()
if forest1 == "1":
    print("Scavenge")

if forest1 == "2":
    print("Hunt")

if forest1 == "3":
    print("Get a grasp")

while True:
    command = input("\n> ").strip().lower()

    if command == "help":
        print("\n---Command List---")
        print("numbers 1-9: selective options that progress the game!")
        print("help: displays this command list")
        print("inventory: displays entire inventory")
        print("stats: displays all class statistics and skill points")

    if command == "inventory" or "inv":
        inventory.display()

    if command == "stats" or "stat" or "st":
        print(f"Here are your stats : {player}")
        print(f"Here are your skill points: {player.skillpoints}")