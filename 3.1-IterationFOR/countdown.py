steps = int(input("How many steps are we away from the cave? "))


for count in range(steps):
    print(str(steps)+" steps remaining.")
    steps = steps - 1

print("We have reached the cave!")