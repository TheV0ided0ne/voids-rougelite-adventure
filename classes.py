class Player:
    def __init__(self, maxhp, speed, basedamage, dodge, block, level, skillpoints):
        self.level       = level
        self.maxhp       = maxhp
        self.hp          = maxhp      # current HP starts full
        self.speed       = speed
        self.basedamage  = basedamage
        self.dodge       = dodge      # % chance to dodge an attack
        self.block       = block      # % damage reduced when blocking
        self.skillpoints = skillpoints

    def __repr__(self):
        return (f"{self.__class__.__name__} | HP: {self.hp}/{self.maxhp} | "
                f"SPD: {self.speed} | DMG: {self.basedamage} | "
                f"Dodge: {self.dodge}% | Block: {self.block}%")


class Warrior(Player):
    """Tank. High HP and block, slow, hits hard, bad dodge."""
    def __init__(self):
        super().__init__(
            level      =1,
            maxhp      =30,
            speed      =4,
            basedamage =5,
            dodge      =5,
            block      =10,
            skillpoints=0,
        )

class Ranger(Player):
    """Mobile skirmisher. Fast, good dodge, light damage, low block."""
    def __init__(self):
        super().__init__(
            level         = 1,
            maxhp         = 25,
            speed         = 9,
            basedamage    = 6,
            dodge         = 15,
            block         = 5,
            skillpoints   = 0,

        )

class Brawler(Player):
    """Balanced brawler. No standout weaknesses, no standout strengths."""
    def __init__(self):
        super().__init__(
            level         = 1,
            maxhp         = 30,
            speed         = 10,
            basedamage    = 4,
            dodge         = 20,
            block         = 10,
            skillpoints   = 0,

        )

class Rouge(Player):
    """Glass cannon. Extremely fast and evasive, but dies in two hits."""
    def __init__(self):
        super().__init__(
            level         = 1,
            maxhp         = 20,
            speed         = 15,
            basedamage    = 8,
            dodge         = 30,
            block         = 0,
            skillpoints   = 0
        )

class Mage(Player):
    """Fragile but hits the hardest. Relies on dodge since block is useless."""
    def __init__(self):
        super().__init__(
            level         = 1,
            maxhp         = 15,
            speed         = 5,
            basedamage    = 12,
            dodge         = 5,
            block         = 0,
            skillpoints   = 0,
        )