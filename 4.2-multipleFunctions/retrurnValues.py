def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight

def calc_avg_weight(beep_weight, bop_weight):
    sum_weights(beep_weight, bop_weight)
    avg_weight = total_weight / 2

def run():
    beep_weight = int(input("What is Beep's weight? "))
    bop_weight = int(input("What is Bop's weight? "))
    choice = input("Do you want to calculate sum or average? ")
    if choice == "sum":
        sum_weights(beep_weight, bop_weight)
        print(total_weight)
    elif choice == "average":
        calc_avg_weight(beep_weight, bop_weight)
        print(avg_weight)

run()