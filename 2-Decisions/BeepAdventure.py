adventuretype = input("What type of adventure should I have? ")

if (adventuretype == "scary") or (adventuretype == "short"):
    print("Entering the dark forest!")
elif (adventuretype == "safe") or (adventuretype == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")