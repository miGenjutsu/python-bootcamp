# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
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
result_weight = int(weight)

# print(type(result_height))
# print(type(result_weight))

result_bmi = result_weight / (result_height ** 2)

print(int(result_bmi))