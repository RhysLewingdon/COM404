#We wish to create a program that demonstrates the following functionality:

#- Decisions with if...elif...else statements
#- Nested decisions
#- Multiple conditions with logical (AND, OR and NOT) operators

firstlook = input("Where should I look? ")
if firstlook == "in the bedroom":
    secondlook = input("Where in the bedroom should I look? ")
    if secondlook == "in the cupboard":
        print("Found some mess but no battery.")
        battery = "false"
    else:
        print("---------")
        battery = "false"
elif firstlook == "in the bathroom":
    secondlook = input("Where in the bathroom should I look? ")
    if secondlook == "in the bathtub":
        print("Found a rubber duck but no battery.")
        battery = "false"
    else:
        print("---------")
        battery = "false"
elif firstlook == "in the lab":
    secondlook = input("Where in the lab should I look? ")
    if secondlook == "on the table":
        print("Yes! I found my battery!")
        battery = "true"
    else:
        print("---------")
        battery = "false"
else:
    print("---------")
    battery = "false"

carryon = input("Would you like to carry on? ")
if (carryon == "yes") and (battery == "true"):
    print("Success! you can now fit the battery.")
elif (carryon == "yes") and (battery == "false"):
    print("You can't continue without the battery!")
else:
    print("---------")

print("Finished.")