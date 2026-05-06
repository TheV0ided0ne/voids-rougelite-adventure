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

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f" | Damage: {self.damage} | "
                f"Dex: {self.dexterity} | Con: {self.constitution} | "
                f"Int: {self.intelligence} | Wis: {self.wisdom} | "
                f"Cha: {self.charisma} | Luc: {self.luck} | ")