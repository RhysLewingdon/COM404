brightness = int(input("What level of brightness is required? ")) + 1
beepbright = 0
bopbright = 0

for count in range(2, brightness, 2):
    print("Beep's brightness level: "+("* " * count))
    print("Bop's brightness level:  "+("* " * count))

print("Adjustments complete!")