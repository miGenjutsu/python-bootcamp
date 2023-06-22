#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
print("What was the total bill? $")
bill_total = input()

print("What percentage tip would you like to give? 10, 12, or 15?")
tip_percentage = input()

tip_percentage_calcu = float(tip_percentage, 2) / 100

print(float(tip_percentage_calcu, 2)) 

# print("How many people to split the bill?")
# split_bill = input()

# bill_calculated = (bill_total / split_bill) * 

# print(bill_total)
# print(tip_percentage)