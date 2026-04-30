'''
the default number of resources someone has is 0, this will go for all resources
'''

class Inventory:
    wool = 0
    wood = 0
    honey = 0
    bones = 0
    stinger = 0
    metalscrap = 0
    selkscales = 0
    voidcrystals = 0
    soulremnant = 0
    ectoplasm = 0
    scales = 0
    hide = 0
    leather = 0
    small_health_potion = 0
    medium_health_potion = 0
    large_health_potion = 0

'''
this is the display code for when a player does 'inventory' in the terminal
'''

def display():
    print("\n--- Inventory ---")
    print(f"  Wool                 : {Inventory.wool}")
    print(f"  Wood                 : {Inventory.wood}")
    print(f"  Metal Scrap          : {Inventory.metalscrap}")
    print(f"  Honey                : {Inventory.honey}")
    print(f"  Bones                : {Inventory.bones}")
    print(f"  Scales               : {Inventory.scales}")
    print(f"  Hide                 : {Inventory.hide}")
    print(f"  Leather              : {Inventory.leather}")
    print(f"  Ectoplasm            : {Inventory.ectoplasm}")
    print(f"  Soul Remnant         : {Inventory.soulremnant}")
    print(f"  Sel' Karin Scales    : {Inventory.selkscales}")
    print(f"  Void Crystals        : {Inventory.voidcrystals}")
    print(f"  Small Health Potion  : {Inventory.small_health_potion}")
    print(f"  Medium Health Potion : {Inventory.medium_health_potion}")
    print(f"  Large Health Potion  : {Inventory.large_health_potion}")
    print("-----------------")