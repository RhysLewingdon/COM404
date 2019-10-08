firstlook = input("Where should I look? ")
if firstlook == "in the bedroom":
    secondlook = input("Where in the bedroom should I look? ")
    if secondlook == "in the cupboard":
        print("Found some mess but no battery.")
    else:
        print("---------")
elif firstlook == "in the bathroom":
    secondlook = input("Where in the bathroom should I look? ")
    if secondlook == "in the bathtub":
        print("Found a rubber duck but no battery.")
    else:
        print("---------")
elif firstlook == "in the lab":
    secondlook = input("Where in the lab should I look? ")
    if secondlook == "on the table":
        print("Yes! I found my battery!")
    else:
        print("---------")
else:
    print("---------")
print("Finished.")