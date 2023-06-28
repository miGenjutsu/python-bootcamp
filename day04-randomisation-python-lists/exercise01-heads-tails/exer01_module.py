import random

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

def random_call():
    print("Welcome! Please Enter following Selection: ")
    print("0.Tails or 1.Heads")

random_face = random.randint(0, 1)

if random_face == 0:
    print("Tails")
elif random_face == 1:
    print("Heads")
else:
    print("something isnt right...")
