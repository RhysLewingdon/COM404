from Bot import Bot

class SuperBot(Bot):
    def __init__(self, name, age=0, energy=0, shield=0, super_power_level=0):
        super().__init__(name, age, energy, shield)
        self.super_power_level = super_power_level
    def display_superbot(self):
        print(self.super_power_level)