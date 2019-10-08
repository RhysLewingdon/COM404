cover = input("What type of cover does the book have? ")

if cover == "soft":
    perfectbound = input("Is the book perfect-bound? ")
    if perfectbound == "yes":
        print("Soft cover, perfect-bound books are very popular")
    else:
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expensive!")
print("Finished!")