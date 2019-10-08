answer = int(input("How many cables should I avoid? "))
count = 0

while answer > 0:
    count = count + 1
    print("Avoiding... done! "+str(count)+" cables avoided.")
    answer = answer - 1
print("All live cables have been avoided.")