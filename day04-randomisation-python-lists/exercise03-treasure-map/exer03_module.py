# # 🚨 Don't change the code below 👇
# # row1 = ["⬜️","️⬜️","️⬜️"]
# # row2 = ["⬜️","⬜️","️⬜️"]
# # row3 = ["⬜️️","⬜️️","⬜️️"]
# row1 = ["🍎","️🍐","️🍊"]
# row2 = ["🍔","🍱","️🍕"]
# row3 = ["🍨️","🥧️","🍩️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

#Write your code below this row 👇
def map_x():
    # 🚨 Don't change the code below 👇
    row1 = ["⬜️","️⬜️","️⬜️"]
    row2 = ["⬜️","⬜️","️⬜️"]
    row3 = ["⬜️️","⬜️️","⬜️️"]
    # row1 = ["🍎","️🍐","️🍊"]
    # row2 = ["🍔","🍱","️🍕"]
    # row3 = ["🍨️","🥧️","🍩️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    split_posistion = position.split() # splitting the position for indexing
    # nested_index = 1
    # element_index = 2
    new_object = "X" # 'X' marker to place in location of `position`

    # code for splitting user_input `position`
    nested_index  = int(position[0])
    element_index = int(position[1])

    # print(f"Nested Index: {nested_index}")
    # print(f"Element Index: {element_index}")

    # map[nested_index - 1][element_index - 1] = new_object
    map[element_index - 1][nested_index - 1] = new_object
    # print(f"\nNew Food Map:{map}")

    # print(f"Your Desired Position: {position}")

    #Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")




## THOUGHTS::
# - needs to insert() to the selected position
# - needs to inser() and replace