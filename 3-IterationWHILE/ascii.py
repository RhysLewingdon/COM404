answer = int(input("How many bars should be charged? "))
bars = 0

while answer > 0:
    answer = answer - 1
    bars = bars+1
    print("Charging: " +("█ " * bars))

print("The battery is fully charged.")