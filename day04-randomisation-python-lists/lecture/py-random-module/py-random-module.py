import random
import my_module

# randomly generate a number between the specified range of 1-10 (including the given specification)
random_interger = random.randint(1, 10)
print(f"Using the Random Module for a random interger: {random_interger}")

# randomly generate a float number between 0 - 1.0(not including 1.0)
random_float = random.random()
print(f"Using the Random Module for a random float: {random_float}")

# try to:- randomly generate a float number between 5.0 - 10.0
new_random_float = random.random()
new_random_float * 5
print(f"Using the Random Module for a random float between the number 0 - 5: {new_random_float}")


# using the `Love Calculator` project concept here:
love_score = random.randint(1, 100)
print(f"Your Love Score is: {love_score}")


# example of using a module -- calling a seperate `.py`
# print(f"calling the created PI module: {my_module.pi}")
# print(f"calling the created RANDOM INT module: {my_module.random_module_number}")