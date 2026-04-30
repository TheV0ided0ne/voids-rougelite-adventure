import classes
import enemies
import inventory
import main

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