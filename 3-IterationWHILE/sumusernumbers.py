numbers = int(input("How many numbers should I sum up? "))
count = 0
numbersof = numbers

runningtotal = 0

while numbers > 0:
    count = count + 1
    number1 = int(input("Please enter number "+str(count)+" of "+str(numbersof)+": "))
    numbers = numbers - 1
    runningtotal = runningtotal + number1

print("The answer is "+str(runningtotal)+".")