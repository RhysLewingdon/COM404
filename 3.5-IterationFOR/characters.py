markings = input("What strange markings do you see? ")
index = 0
print("Identifying...")

for position in range(0, len(markings), 1):
    print("index "+str(index)+": "+markings[position])
    index = index + 1

print("Done!")