class Warrior():
    def __init__(self):
        self.strength = 5
        self.health = 100
        self.armor = 0
        self.offense = 10
        self.defense = 5
        self.inventory = ["map", "compass", "potion"]

    def heal(self):
        if "potion" in self.inventory:
            self.inventory.remove("potion")
            newHealth = self.health + 15
            if newHealth > 100:
                self.health = 100
            else:
                self.health = newHealth
            print(f"Health is now - {self.health}")
        else:
            print("You don't have a potion!")

    def kick(self, target):
        damage = (self.strength + self.offense) - (self.armor + self.defense)
        if damage > 0:
            target.health -= damage
            print(f"{damage} damage taken!\n")
        else:
            print("Kick was blocked!")

class Wizard(Warrior):
    def __init__(self):
        super().__init__()
        self.magic = 10
        self.spells = {"fireball": 20,
                       "lightning": 30
                       }

    def cast_spell(self, target, spell_name):
        if spell_name in self.spells:
            damage = self.spells[spell_name] + self.magic
            target.health -= damage
            print(f"{spell_name} did {damage} points of damage!")
        else:
            print(f"You can not cast {spell_name}")


jasmin = Wizard()
kelvin = Warrior()

jasmin.cast_spell(kelvin, "lightning")