import classes
import inventory
import main

'''

'''

class ForestEnemy:
    def __init__(self, maxhp, speed, basedamage, dodge, block):
        self.maxhp      = maxhp
        self.hp         = maxhp
        self.speed      = speed
        self.basedamage = basedamage
        self.dodge      = dodge
        self.block      = block


class Bee(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 10,
            speed = 12,
            basedamage = 4,
            dodge = 15,
            block = 0
        )

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