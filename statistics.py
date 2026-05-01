from os import times
import classes
from classes import Player

class Statistics:
    def __init__(self,strength, damage, luck,
                 constitution, dexterity, intelligence,
                 wisdom, charisma):

        self.damage = damage
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.luck = luck