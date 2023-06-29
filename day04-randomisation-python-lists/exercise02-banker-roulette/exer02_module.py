import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(len(names))

name_len = len(names)

def random_name_call():
    random_choice = random.randint(0, name_len -1)
    # random_index = random.randrange(len(names))
    # random_name = names[random_index]
    
    # print(random_choice)
    paying_person = names[random_choice]

    print(f"{paying_person} is going to buy the meal today!")
    
    
# using the `choice()` module ---> wasnt allowed for the challange!
def choice_name_call():
    person_who_will_pay = random.choice(names)
    print(f"{person_who_will_pay} is going to buy the meal today!")
