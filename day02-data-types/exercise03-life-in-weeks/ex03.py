# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

year = 365
week = 52
month = 12

age_int = int(age)

remain_year = 90 - age_int
remain_day = remain_year * 365
remain_week = remain_year * 52
remain_month = remain_year * 12

print(f"You have {remain_day} days, {remain_week} weeks, and {remain_month} months left.")
