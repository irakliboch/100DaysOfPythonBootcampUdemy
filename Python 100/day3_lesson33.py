#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

#size = "L"
#add_pepperoni = "Y"
#extra_cheese = "N"
def calculate_pizza_bill(pizza_size,add_pepperoni,extra_cheese):
	final_bill = 0
	if pizza_size == "S":
		final_bill += 15
	elif pizza_size == "M":
		final_bill += 20
	else:
		final_bill += 25

	if add_pepperoni == "Y" and pizza_size == "S":
		final_bill += 2
	elif add_pepperoni == "Y" and pizza_size == "M" or pizza_size == "L":
		final_bill += 3

	if extra_cheese == "Y":
		final_bill +=1
	
	print(f"Your finall pizza bill is ${final_bill}")




print("Welcome to the Python Pizza. \n Please place your order: ")

pizza_size = input("Choose your pizza size - S, M or L:")
add_pepperoni = input("Would you like to add pepperoni on top?:Y or N ")
extra_cheese = input("Would you like to add some extra cheese?:Y or N ")


calculate_pizza_bill(pizza_size, add_pepperoni, extra_cheese)

