#You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 2 and 100.

#e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100

#Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.



sum_of_even_numbers = 0
for number in range(2,101):
	if number % 2 == 0:
		sum_of_even_numbers += number
print(sum_of_even_numbers)