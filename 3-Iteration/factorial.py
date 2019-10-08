number = int(input("Please enter a number: "))
multiplynumber = number - 1
runningtotal = multiplynumber * number
multiplynumber = multiplynumber - 1

while multiplynumber > 0:
    runningtotal = runningtotal * multiplynumber
    multiplynumber = multiplynumber - 1

print(runningtotal)
    