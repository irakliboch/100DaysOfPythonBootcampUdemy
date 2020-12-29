#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#bmi = weight / height ** 2
#Warning you should convert the result to a whole number.
#Example input - weight = 80 height = 1.75

weight = float(input("What is your weight?"))
height = float(input("What is your height?"))

bmi = weight / height ** 2

print(round(bmi))


