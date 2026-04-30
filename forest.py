from turtledemo import forest

import classes
import inventory
import main

'''
All forest enemies and zone features will remain here, call them with their respective variables
'''

class ForestInitiate:
    while True:
        print("Welcome to the forest, this land is peaceful, until the giant came along.")
        print("Please vanquish him to free the lands of the forests, and let nature take it's lands back!")
        print()
        print()
        print("What shall you do first? | Zone 1 / 8")
        print("You can:")
        print(" [1]")
        print("Take a lay of the land and be strategic [2]")
        print("Take a rest after the journey that you already took to get here [3]")
        forest1 = input().strip().lower()
        if forest1 == "1":
            print()



















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
class Spider(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class Goblin(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class Bandit(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class Rat(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class LivingPebble(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class Pixie(ForestEnemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )



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