# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# height --> meter = 1.778
# weight --> kg = 90.71

# testing input
# print(type(height))
# print(type(weight))
# print(type(int(height)))
# print(type(int(weight)))

result_height = float(height)
result_weight = float(weight)

# print(type(result_height))
# print(type(result_weight))

result_bmi = round(result_weight / (result_height ** 2))

if result_bmi < 18.5:
  print(f"Your BMI is {result_bmi}, you are underweight.")
elif result_bmi < 25:
  print(f"Your BMI is {result_bmi}, you have a normal weight.")
elif result_bmi < 30:
  print(f"Your BMI is {result_bmi}, you are slightly overweight.")
elif result_bmi < 35:
  print(f"Your BMI is {result_bmi}, you are obese.")
else:
  print(f"Your BMI is {result_bmi}, you are clinically obese.")