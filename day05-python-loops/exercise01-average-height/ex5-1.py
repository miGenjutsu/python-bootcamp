# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# testing: the count of list
# print(n)
# print(student_heights)

total = 0

for height in student_heights:
    total += height
    
print(total)

fin_calcu = total / n

print(round(fin_calcu))