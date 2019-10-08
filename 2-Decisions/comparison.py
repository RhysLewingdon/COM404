firstnumber = int(input("Please enter first number. >> "))
secondnumber = int(input("Please enter second number. >> "))

if firstnumber > secondnumber:
    print("Second number is the smallest.")
elif firstnumber < secondnumber:
    print("First number is the smallest.")
else:
    print("Both numbers are equal!")
print("Finished.")