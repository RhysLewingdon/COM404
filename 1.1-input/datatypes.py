name = input("What is your name?\n>>> ")
age = input("What is your age?\n>>> ")
weight = input("What is your weight(kg)?\n>>> ")
height = input("What is your height(m)?\n>>> ")
bmi = (int((weight))/(float(height)**2))

print("Hi",name+". Your age is "+str(age),"and your B.M.I. is "+str(bmi)+".")
print(bmi)