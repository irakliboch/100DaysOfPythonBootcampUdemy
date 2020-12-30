#You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
# how many names do we have in names list?
# store it into number choice
number_choice = len(names)
# now we want to pick a random element from names
random_name_number = random.randint(0, number_choice - 1)
print(names[random_name_number])

#Angela, Ben, Jenny, Michael, Chloe
#Michael is going to buy the meal today!
#You might need the help of the len() function.

