firstnumber = int(input("Please enter the first whole number.>> "))
secondnumber = int(input("Please enter the second whole number.>> "))
thirdnumber = int(input("Please enter the third whole number.>> "))

firstnumberOE = firstnumber % 2
secondnumberOE = secondnumber % 2
thirdnumberOE = thirdnumber % 2

if firstnumberOE == 0 and secondnumberOE ==0 and thirdnumberOE == 0:
    print("All even.")
elif firstnumberOE == 0 and secondnumberOE ==0 and thirdnumberOE == 1:
    print("One odd, two even.")
elif firstnumberOE == 0 and secondnumberOE ==1 and thirdnumberOE == 1:
    print("Two odd, one even.")
elif firstnumberOE == 1 and secondnumberOE ==1 and thirdnumberOE == 1:
    print("All odd.")
elif firstnumberOE == 0 and secondnumberOE ==1 and thirdnumberOE == 0:
    print("One odd, two even.")
elif firstnumberOE == 1 and secondnumberOE ==1 and thirdnumberOE == 0:
    print("Two odd, one even.")
elif firstnumberOE == 1 and secondnumberOE ==0 and thirdnumberOE == 0:
    print("One odd, two even.")
elif firstnumberOE == 1 and secondnumberOE ==0 and thirdnumberOE == 1:
    print("Two odd, one even.")