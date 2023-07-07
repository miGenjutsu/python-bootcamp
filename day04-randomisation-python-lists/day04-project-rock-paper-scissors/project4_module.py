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

def project4():
    game_image = [rock, paper, scissors]

    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    print(f"User Selected: {game_image[user_input]}")


    # create variable for randomize
    compute_input = random.randint(0, 2)
    print(f"Computer Selected: {game_image[compute_input]}")


    if user_input >= 3 and compute_input < 0:
        print("You typed an invalide option, YOU LOOSE! 💀 ")
    elif user_input == 0 and compute_input == 2:
        print("You won! 🎉")
    elif compute_input == 0 and user_input == 2:
        print("You loose! 💀 ")
    elif compute_input > user_input:
        print("You loose! 💀 ")
    elif user_input > compute_input:
        print("You win 🎉")
    elif user_input == compute_input:
        print("Its a draw! 🤝")



## TESTING CODE::
# if else statements - user input
# if user_input == 0:
#     user_input = rock
#     print(f"Your option: {user_input}")
# elif user_input == 1:
#     user_input = paper
#     print(f"Your option: {user_input}")
# elif user_input == 2:
#     user_input = scissors
#     print(f"Your option: {user_input}")
# else:
#     print("something went wrong")
  


# if random_option == 0:
#     random_option = rock
#     print(f"Computer option: {random_option}")
# elif random_option == 1:
#     random_option = paper
#     print(f"Computer option: {random_option}")
# elif random_option == 2:
#     random_option = scissors
#     print(f"Computer option: {random_option}")
# else:
#     print("something went wrong")