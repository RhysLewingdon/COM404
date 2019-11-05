class bot:
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield
    def display_bot(self):
        print("The Bot '{}' is {} years old and has {} energy and {} shield.".format(self.name, self.age, self.energy, self.shield))