#You are going to write a program that calculates the average student height from a List of heights.

#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row👇

sum_of_heights = 0 
sum_of_people = 0
for people in student_heights:
	sum_of_people += 1
	sum_of_heights += people

average_height = sum_of_heights / sum_of_people

print(round(average_height))
print(sum_of_people)
print(sum_of_heights)



