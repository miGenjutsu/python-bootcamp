# Example using List[]
## whenever you see [] brackets you shld think of LIST

states_of_america = ["Deleware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"] # order is detemined by the order in the list

print(states_of_america[3]) # ---> prints out the third item in the `ordered list` which will be `Georgia`

print(states_of_america[-1]) # ---> prints out the second from the LAST of the given list which will be `Connecticut`

states_of_america[1] = "Pencilvania" # ---> example of modifying the preset list
print(f"Shows an altered version of the preset list: {states_of_america}") # ---> this shows the `altered` list from above code line

# example of using append()
states_of_america.append("Florida")
print(f"After using the append() function to add a new state to the preset list: {states_of_america}")

# example of using extend()
states_of_america.extend(["New York", "Texas", "Alaska"])
print(f"After using the extend() function to add multiple new items to the preset list: {states_of_america}")