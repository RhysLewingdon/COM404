class Bot:
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("The name of the bot is: "+self.name)

    def display_age(self):
        print("The age of the bot is: "+str(self.age))

    def display_energy(self):
        print("The bot energy level is at: "+str(self.energy))

    def display_shield(self):
        print("The bot shield level is at: "+str(self.shield))

    def display_summary(self):
        print("The Bot '{}' is {} years old and has {} energy and {} shield.".format(self.name, self.age, self.energy, self.shield))

    def __str__(self):
        return 'Bot(name='+self.name+', age='+str(self.age)+', energy='+str(self.energy)+', shield='+str(self.shield) + ')'

Bot1 = Bot("Bot1", 18, 90, 30)

Bot1.display_name()
print("#################################")
Bot1.display_age()
print("#################################")
Bot1.display_energy()
print("#################################")
Bot1.display_shield()
print("#################################")
Bot1.display_summary()
print("#################################")
print(Bot1.__str__())
print("#################################")