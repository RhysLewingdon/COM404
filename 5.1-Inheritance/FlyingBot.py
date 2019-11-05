from SuperBot import superbot

class flyingbot(superbot):
    def __init__(self, name, age=0, energy=0, shield=0, super_power_level=0, hover=0):
        super().__init__(name, age, energy, shield, super_power_level)
        self.hover = hover
    def display_flyingbot(self):
        print("The Bot '{}' is {} years old and has {} energy and {} shield.".format(self.name, self.age, self.energy, self.shield))
        print("The Bot super power level is: "+str(self.super_power_level))
        print("The Bot hover level is: "+str(self.hover))