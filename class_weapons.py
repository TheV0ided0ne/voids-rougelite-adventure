class Weapons:
    def __init__(self,strength, damage, luck, constitution):
        self.strength = strength
        self.damage = damage
        self.constitution = constitution
        self.luck = luck


class StarterDagger(Weapons):
    def __init__(self):
        super().__init__(
            strength=0,
            damage=3,
            luck=2,
            constitution=0
        )
