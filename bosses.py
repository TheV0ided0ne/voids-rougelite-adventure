'''
Go to forest.py for knowledge of how this works and go to the 'class ForestEnemy'
'''

class Bosses:
    def __init__(self, maxhp, speed, basedamage, dodge, block):
        self.maxhp      = maxhp
        self.hp         = maxhp
        self.speed      = speed
        self.basedamage = basedamage
        self.dodge      = dodge
        self.block      = block

class Giant(Bosses):
    def __init__(self):
       super().__init__(
           maxhp = 80,
           speed = 0,
           basedamage = 10,
           dodge = 0,
           block = 0
    )
