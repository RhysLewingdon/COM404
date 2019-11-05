class Bot:
    def __init__(self, name, age=0, energy=0, shield=0):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        print("The name of the bot is: \n"+self.name)

    def display_age(self):
        print("The age of the bot is: \n"+str(self.age))

    def display_energy(self):
        print("The bot energy level is at: \n"+str(self.energy))

    def display_shield(self):
        print("The bot shield level is at: \n"+str(self.shield))

    def display_summary(self):
        print("The Bot \n{}\n is \n{}\n years old and has \n{}\n energy and \n{}\n shield.".format(self.name, self.age, self.energy, self.shield))

    def __str__(self):
        return 'Bot(name='+self.name+', age='+str(self.age)+', energy='+str(self.energy)+', shield='+str(self.shield) + ')'

Bot1 = Bot("     _______  _______  _______  ____  \n    |  _    ||       ||       ||    | \n    | |_|   ||   _   ||_     _| |   | \n    |       ||  | |  |  |   |   |   | \n    |  _   | |  |_|  |  |   |   |   | \n    | |_|   ||       |  |   |   |   | \n    |_______||_______|  |___|   |___| \n",
 18,
  90,
   30)

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