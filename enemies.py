class Enemy:
    def __init__(self, maxhp, speed, basedamage, dodge, block):
        self.maxhp      = maxhp
        self.hp         = maxhp
        self.speed      = speed
        self.basedamage = basedamage
        self.dodge      = dodge
        self.block      = block

class Troll(Enemy):
    def __init__(self):
       super().__init__(
           maxhp = 30,
           speed = 4,
           basedamage = 10,
           dodge = 3,
           block = 5
    )

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 15,
            speed = 8,
            basedamage = 4,
            dodge = 6,
            block = 0
        )

class Bee(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 10,
            speed = 12,
            basedamage = 4,
            dodge = 15,
            block = 0
        )