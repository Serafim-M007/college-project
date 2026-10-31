## RPG Game Character Creation
#profile
name = "Hades"
level = 500
hp = 5250.0
is_alive = True
inventory = ["Hammer", "Shield", "Potion"]
atributes = {
        "strength": 80,
        "agility": 65,
    }

print(name, type(name))
print(level, type(level))
print(hp, type(hp))
print(is_alive, type(is_alive))
print(inventory, type(inventory))
print(atributes, type(atributes))

new_inventory = inventory + ["HP Potion"]
upgrade_level = level + 0.5

print(name, "get new inventory:", new_inventory, type(new_inventory))
print(name, "upgraded to level:", upgrade_level, type(upgrade_level))