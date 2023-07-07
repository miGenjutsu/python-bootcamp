import random

rock='''✊'''
paper='''✋'''
scissors='''✌️'''

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

#Write your code below this line 👇

# get user input logic
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

# create variable for randomize
compute_random = [0, 1, 2]

# if else statements - user input
if user_input == 0:
    user_input = rock
    print(f"Your option: {user_input}")
elif user_input == 1:
    user_input = paper
    print(f"Your option: {user_input}")
elif user_input == 2:
    user_input = scissors
    print(f"Your option: {user_input}")
else:
    print("something went wrong")
  
random_option = random.choice(compute_random)

if random_option == 0:
    random_option = rock
    print(f"Computer option: {random_option}")
elif random_option == 1:
    random_option = paper
    print(f"Computer option: {random_option}")
elif random_option == 2:
    random_option = scissors
    print(f"Computer option: {random_option}")
else:
    print("something went wrong")
