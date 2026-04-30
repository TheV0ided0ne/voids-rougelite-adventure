class Weapons:
    def __init__(self,strength, damage, luck, constitution,Dexterity):
        self.strength = strength
        self.damage = damage
        self.constitution = constitution
        self.luck = luck
        self.dexterity = Dexterity


class StarterDagger(Weapons):
    def __init__(self):
        super().__init__(
            strength=0,
            damage=3,
            luck=2,
            constitution=0,
            dexterity=2
        )
