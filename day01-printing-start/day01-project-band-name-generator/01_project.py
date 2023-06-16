print("Welcome to the Band Name Generator.")

print("What's the name of the city you grew up in?")
grew_city = input("")

# print("Return " + grew_city)

print("Name of your pet?")
name_pet = input()

combine_sentence = grew_city + " " + name_pet

# print("Your band name could be " + grew_city + " " + name_pet)

print("Your band name: " + combine_sentence)

# print("Return: " + grew_city + " " + name_pet ".\n")  ---> wsnt working becuase there was no `+` to concatenate the remaing " ."



# ---------------------------------------------------------------------
# instructor's solutions

print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)