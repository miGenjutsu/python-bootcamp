# continuing from `py-control-flow.py` 
## now check for the age of the rider to determine how much they should pay


print("Welcome to the rollercoaster!")

bill = 0

height = int(input("What is your height in cm? "))

if height >= 120:
    print("Enter. Enjoy the Ride!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")     
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
## newly added code block:        
    elif age >=45 and age <= 55:
        print("Everything is going to be okay. You ride FREE!")
## -------        
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    want_photo = input("Do you want a photo taken? Y or N: ")
    if want_photo == "y":
        # Add $3 to bill
        bill += 3
    
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you dont meet the height standard to ride!")