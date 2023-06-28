#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill_total = input("What was the total bill? $")

bill_total_float = float(bill_total)

tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

tip_percentage_float = float(tip_percentage)

# bill_total_float *= (1.0 + (tip_percentage_float / 100))  ---> figuring out the formula
# print(bill_total_float)  ---> testing my math

people_split = input("How many people to split the bill? ")

people_split_int = int(people_split)

bill_total_float *= (1.0 + (tip_percentage_float / 100)) / people_split_int

bill_total_amount = round(bill_total_float, 2)
bill_total_amount = "{:.2f}".format(bill_total_amount)

print(f"Each person should pay: ${bill_total_amount}")


#--------------------------------------------------------------------
#---Source Code from Instructor:
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# calculations:
# bill_with_tip = tip / 100 * bill + bill  # --> alternative formula:- bill_with_tip = bill * (1 + tip / 100)
# print(bill_with_tip) --> testing the formula
# multiple step logic
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person) ---> this resolve if a 0 is at the end of the decimal place
# print("Each person should pay ${final_amount}")





# tip_percentage_calcu = float(tip_percentage, 2) / 100

# print(float(tip_percentage_calcu, 2)) 

# print("How many people to split the bill?")
# split_bill = input()

# bill_calculated = (bill_total / split_bill) * 

# print(bill_total)
# print(tip_percentage)