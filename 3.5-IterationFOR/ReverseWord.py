phrase = input("What phrase do you see? ")
revMod = ""

for letters in range(0, len(phrase), 1):
    rev = (phrase[letters])
    revMod = rev + revMod

print(revMod)
