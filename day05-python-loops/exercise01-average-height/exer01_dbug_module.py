def dbug_average_height():
    student_heights = input("Input a list of student heights ").split()

    # Convert the elements to integers with error handling
    for n in range(len(student_heights)):
        try:
            student_heights[n] = int(student_heights[n])
        except ValueError:
            print("Invalid input. Please enter valid integers for student heights.")
# Handle the error (e.g., skip the current value, ask for input again, etc.)

# Now, you can proceed to calculate the sum of the student heights
    total_height = 0
    for height in student_heights:
        total_height += height

    print("Total height:", total_height)
