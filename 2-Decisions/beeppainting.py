def directioncode():
    direction = input("Which direction should I paint in? ")

    if direction == "up":
        print("I am painting in the upward direction!")
    elif direction =="down":
        print("I am painting in the downward direction!")
    elif direction =="left":
        print("I am painting in the left direction!")
    elif direction =="right":
        print("I am painting in the right direction!")
    else:
        print("Please enter a valid direction (up, down, left, or right).")
        directioncode()
directioncode()
print("Painting complete!")