`Exercise 3.2 - BMI Calculator 2.0: README`

`./day03-control-flow-logical-operations/exercise02-bmi/.`

## Instructions

Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

-  Under 18.5 they are underweight
-  Over 18.5 but below 25 they have a normal weight
-  Over 25 but below 30 they are slightly overweight
-  Over 30 but below 35 they are obese
-  Above 35 they are clinically obese.

<picture>
<img alt= "Show an illustration of the BMI Chart." src="https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36">
</picture>

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

<picture>
<img alt= "Show an illustration of the BMI Formula." src="https://codingrooms-user-uploads-us-west-2.s3-us-west-2.amazonaws.com/6653a739-6bc2-4d53-b566-67f5c0b32849/BMI+Image+Small.jpeg">
</picture>

***Warning*** you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

## Example Input
```sh
weight = 85
height = 1.75
```

## Example Output
```sh
85 ÷ (1.75 x 1.75) = 27.755102040816325
Your BMI is 28, you are slightly overweight.
```

e.g. When you hit run, this is what should happen:

<picture>
<img alt="Shows giphy of example input/output" src="https://cdn.fs.teachablecdn.com/mGRynIETXuVqoDk8unci">
</picture>

The testing code will check for print output that is formatted like one of the lines below:
```sh
"Your BMI is 18, you are underweight."
"Your BMI is 22, you have a normal weight."
"Your BMI is 28, you are slightly overweight."
"Your BMI is 33, you are obese."
"Your BMI is 40, you are clinically obese."
```

Hint

-  Try to use the exponent operator in your code.
-  Remember to round your result to the nearest whole number.
-  Make sure you include the words in bold from the interpretations.

## Test Your Code

Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.


[Solution](https://repl.it/@appbrewery/day-3-2-solution)