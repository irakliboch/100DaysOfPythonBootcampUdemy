#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

#It should tell them the interpretation of their BMI based on the BMI value.

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

# bmi = weight / height ** 2

#Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

#input weight = 85 , height = 1.75, Your BMI is 28, you are slightly overweight.
def bmi(weight, height):
	bmi = weight / height ** 2
	bmi_round = round(bmi)
	if bmi_round < 18.5:
		print(f"Your BMI is {bmi_round}, you are underweight")
	elif bmi_round > 18.5 and bmi_round < 25:
		print(f"Your BMI is {bmi_round}, you are underweight")
	elif bmi_round > 25 and bmi_round < 30:
		print(f"Your BMI is {bmi_round}, you are underweight")
	elif bmi_round > 30 and bmi_round < 35:
		print(f"Your BMI is {bmi_round}, you are underweight")	
	else:
		print(f"Your BMI is {bmi_round}, you are clinically obese")
#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

weight = float(input("Enter your weight please: "))
height = float(input("Enter your height please: "))


bmi(weight,height)



