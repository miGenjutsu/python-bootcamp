# Example using List[]
## whenever you see [] brackets you shld think of LIST

## ATTEMPTING TO THROW THE `IndexError` in this example ---> line 23-24

states_of_america = ["Deleware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"] # order is detemined by the order in the list

## ATTEMPTING TO THROW THE `IndexError` in this example
# print(states_of_america[5])  # ---> this would throw the `IndexError` since my preset list only contains 4 items in the list

# a method to avoid over shotting the assumed number in the list 
num_of_states = len(states_of_america)
print(states_of_america[num_of_states -1])  # ---> prints out Connecticut

## Example of Nested Lists
# dirty_dozen = ["Stawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Stawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

