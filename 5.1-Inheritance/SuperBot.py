from Bot import bot

class superbot(bot):
    def __init__(self, name, age=0, energy=0, shield=0, super_power_level=0):
        super().__init__(name, age, energy, shield)
        self.super_power_level = super_power_level
    def display_superbot(self):
        print("The Bot '{}' is {} years old and has {} energy and {} shield.".format(self.name, self.age, self.energy, self.shield))
        print("The Bot super power level is: "+str(self.super_power_level))