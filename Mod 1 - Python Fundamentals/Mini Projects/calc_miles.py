inp = int(input("\nHow far would you like to travel in miles? "))

if inp < 0:
    print("Distance cannot be negative.")
elif inp < 3:
    print("I suggest riding bicycle to your destination.")
elif inp > 3 and inp < 300:
    print("I suggest riding motor-cycle to your destination.")
elif inp >= 300:
    print("I suggest driving super-car to your destination.\n")
