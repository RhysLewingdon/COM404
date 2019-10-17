def cross_bridge(steps):
    if steps <= 5:
        print("Crossed step. " * steps)
    elif steps > 5:
        print("Crossed step. " * 5)
        print("The bridge is collapsing!")

cross_bridge(3)
cross_bridge(6)