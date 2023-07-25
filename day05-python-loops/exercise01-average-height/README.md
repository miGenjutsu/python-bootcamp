`Exercise 5.1 - Average Height: README`

`./day05-python-loops/exercise01-average-height/.`

## Instructions

You are going to write a program that calculates the average student height from a List of Heights.

e.g. 

``` bash
student_heights = [180, 124, 165, 173, 189, 169, 146]
```

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

``` bash
180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
```

There are a total of `7` heights in **student_heights**

``` bash
1146 ÷ 7 = 163.71428571428572
```

Average height rounded to the nearest whole number = **164**

**Important** You should not use the **sum()** or **len()** functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.


## Example Input

``` bash
156 178 165 171 187
```

In this case, **student_heights** would be a list that looks like: `[156, 178, 165, 171, 187]`

## Example Output

``` bash
171
```
e.g. When you hit run, this is what should happen:

<picture>
<img alt="Shows giphy of example input/output" src="https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP">
</picture>

## Hint

- Remember to use the **round()** function to round the average height before you print it.

## Test Your Code

Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

## Documentation

recieved error:
```bash
    Operator "+=" not supported for types "Unknown | Literal[0]" and "str"
    Operator "+" not supported for types "Literal[0]" and "str"Pylance
```

from this block:
```bash
    total_height = 0

    for height in student_heights:
        total_height += height
    print(total_height)
```

Explination:

    The error messages you received indicate that there is an issue with the data type of the variables used in the calculation. The variable total_height is initialized to 0, and it seems that the height values in the student_heights list are not numeric (likely strings) rather than integers or floats, which leads to the error when trying to add them together using the += operator.

    To fix this issue, make sure that the student_heights list contains numeric values (integers or floats). If you are getting the heights as user input, ensure that you are casting the input to the appropriate numeric type (int or float) before adding them to the list.

`Here's an example to demonstrate how to use numeric values:`

```
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
```

[Solution](https://repl.it/@appbrewery/day-5-1-solution)