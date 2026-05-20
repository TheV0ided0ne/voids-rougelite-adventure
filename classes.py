class Player:
    def __init__(self, maxhp, speed, basedamage, dodge,
                 block, level, skillpoints, magic, strength,
                 dexterity, constitution, intelligence,
                 wisdom, charisma, luck):
        self.level        = level
        self.maxhp        = maxhp
        self.hp           = maxhp      # current HP starts full
        self.speed        = speed
        self.magic        = magic
        self.basedamage   = basedamage
        self.dodge        = dodge      # % chance to dodge an attack
        self.block        = block      # % damage reduced when blocking
        self.skillpoints  = skillpoints
        self.strength     = strength
        self.dexterity    = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom       = wisdom
        self.charisma     = charisma
        self.luck         = luck

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f" | HP: {self.hp}/{self.maxhp} | "
                f"SPD: {self.speed} | DMG: {self.basedamage} | "
                f"Dodge: {self.dodge} | Block: {self.block} | "
                f"Str: {self.strength} | Dex: {self.dexterity} | "
                f"Con: {self.constitution} | Int: {self.intelligence} | "
                f"Wis: {self.wisdom} | Cha: {self.charisma} | "
                f"Luc: {self.luck} | Skillpoints: {self.skillpoints} | " )


class Warrior(Player):
    """Tank. High HP and block, slow, hits hard, bad dodge."""
    def __init__(self):
        super().__init__(
            level        =1,
            maxhp        =30,
            speed        =4,
            magic        =2,
            basedamage   =5,
            dodge        =5,
            block        =10,
            skillpoints  =0,
            strength     =0,
            dexterity    =0,
            constitution =0,
            intelligence =0,
            wisdom       =0,
            charisma     =0,
            luck         =0
        )

class Ranger(Player):
    """Mobile skirmisher. Fast, good dodge, light damage, low block."""
    def __init__(self):
        super().__init__(
            level         = 1,
            maxhp         = 25,
            speed         = 9,
            magic         = 1,
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
            magic         = 0,
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
            magic         = 4,
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
            magic         = 8,
            basedamage    = 12,
            dodge         = 5,
            block         = 0,
            skillpoints   = 0,
        )
