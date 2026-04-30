class Enemy:
    def __init__(self, maxhp, speed, basedamage, dodge, block):
        self.maxhp      = maxhp
        self.hp         = maxhp
        self.speed      = speed
        self.basedamage = basedamage
        self.dodge      = dodge
        self.block      = block

class Vampire(Enemy):
    def __init__(self):
       super().__init__(
           maxhp = 30,
           speed = 4,
           basedamage = 10,
           dodge = 3,
           block = 5
    )

class Skeletons(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 15,
            speed = 8,
            basedamage = 4,
            dodge = 6,
            block = 0
        )

class Zombies(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 10,
            speed = 12,
            basedamage = 4,
            dodge = 15,
            block = 0
        )
class Undead Necromancer(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 10,
            speed = 12,
            basedamage = 4,
            dodge = 15,
            block = 0
        )
class Kobold Warrior(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class Kobold Assassin(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )
class Slime(Enemy):
    def __init__(self):
        super().__init__(
            maxhp = 1,
            speed = 1,
            basedamage = 1,
            dodge = 1,
            block = 1
        )