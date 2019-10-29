def display_ladder(steps):
    print("[]--------[]\n" * steps)

def create_ladder():
    steps = int(input("How many steps remain? "))
    display_ladder(steps)

create_ladder()
