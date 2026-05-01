from statistics import Statistics

'''
initializer and variables for weapons
'''


class StarterDagger(Statistics):
    def __init__(self):
        super().__init__(
            damage=3,
            dexterity=2,
            luck=2
        )

class StarterFists(Statistics):
    def __init__(self):
        super().__init__(
            damage=3,
            strength=2,
            constitution=2
        )

class StarterSword(Statistics):
    def __init__(self):
        super().__init__(
            damage=3,
            strength=2,
            constitution=2
        )