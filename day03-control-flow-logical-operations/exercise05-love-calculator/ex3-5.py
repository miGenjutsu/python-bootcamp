from collections import Counter

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

score = 0

name1_lower = name1.upper()
name2_lower = name2.upper()

# combine_name = name1 + name2

# total_count = (
#     combine_name.count('T')+
#     combine_name.count('R')+
#     combine_name.count('U')+
#     combine_name.count('E')+
#     combine_name.count('L')+
#     combine_name.count('O')+
#     combine_name.count('V')+
#     combine_name.count('E')
# )

total_count_1 = (
    name1_lower.count('T')+
    name1_lower.count('R')+
    name1_lower.count('U')+
    name1_lower.count('E')+
    name1_lower.count('L')+
    name1_lower.count('O')+
    name1_lower.count('V')+
    name1_lower.count('E')
)




# total_count_1 = (
#     name1_lower.count('T')+
#     name1_lower.count('R')+
#     name1_lower.count('U')+
#     name1_lower.count('E')+
#     name1_lower.count('L')+
#     name1_lower.count('O')+
#     name1_lower.count('V')+
#     name1_lower.count('E')
# )

# result_1 = print(str(total_count_1))
# result_1 = total_count_1
# result_1 = print(str(total_count_1))

total_count_2 = (
    name2_lower.count('T')+
    name2_lower.count('R')+
    name2_lower.count('U')+
    name2_lower.count('E')+
    name2_lower.count('L')+
    name2_lower.count('O')+
    name2_lower.count('V')+
    name2_lower.count('E')
)

# total_count_2 = (
#     # name2_lower.count('T')+
#     # name2_lower.count('R')+
#     # name2_lower.count('U')+
#     # name2_lower.count('E')+
#     name2_lower.count('L')+
#     name2_lower.count('O')+
#     name2_lower.count('V')+
#     name2_lower.count('E')
# )

# result_2 =  print(str(total_count_2))


print(f"The number of letters for NAME 1 is: {total_count_1}")
print(f"The number of letters for NAME 2 is: {total_count_2}")

if total_count_1 > total_count_2:
    # print(total_count_1 + total_count_2)
    score = str(total_count_1) + str(total_count_2)
else:
    score = str(total_count_2) + str(total_count_1)

# score = str(total_count_1) + str(total_count_2)

print(score)



# if score <= 10 and score >= 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >= 40 and score <=50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")
    
# print(f"{name1.lower()}")
# print(f"{name2.lower()}")