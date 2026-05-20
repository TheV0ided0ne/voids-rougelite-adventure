'''
initializer and variables for weapons
'''

class Weapons:
    def __init__(self, strength, damage, luck,
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


class StarterDagger(Weapons):
    def __init__(self):
        super().__init__(
            damage=3,
            dexterity=2,
            luck=2
        )

class StarterFists(Weapons):
    def __init__(self):
        super().__init__(
            damage=3,
            strength=2,
            constitution=2
        )

class StarterSword(Weapons):
    def __init__(self):
        super().__init__(
            damage=3,
            strength=2,
            constitution=2
        )
class StarterBow(Weapons):
    def __init__(self):
        super().__init__(
                damage=3,
                dexterity=2,
        )