from SuperBot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age=0, energy=0, shield=0, super_power_level=0, hover=0):
        super().__init__(name, age, energy, shield, super_power_level)
        self.hover = hover
    def display_flyingbot(self):
        print(self.hover)