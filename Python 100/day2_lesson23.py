#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.

#There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = int(input("What is your current age?"))
years_left = 90 - age

days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} left.")