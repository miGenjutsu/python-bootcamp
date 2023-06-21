#Data Types

#String
"Hello"

print("Hello"[0])  # the `[0]` is to select which character to print out to the user

# subscripting --> The subscript operator is defined as square brackets []

#Integer
123

#Float
3.14159

#Boolean
True
False

#Type Errors
num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")
# ☝️ above code will break since your not able to concatinate intergers to resolve this use a `TYPE CONVERSION` like so....

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# OUTPUT:: Your name has X characters

#Type Checking
type()

#Type Conversion
str()
int()
float()
bool()