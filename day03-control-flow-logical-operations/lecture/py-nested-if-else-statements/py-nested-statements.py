# continuing from `py-control-flow.py` 
## now check for the age of the rider to determine how much they should pay


print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("Enter. Enjoy the Ride!")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5")     
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you dont meet the height standard to ride!")