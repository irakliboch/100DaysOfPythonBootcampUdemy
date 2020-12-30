#Write a program that works out whether if a given number is an odd or even number.

#Even numbers can be divided by 2 with no remainder.

print("This code will check whether the number is odd or even")
number = int(input("Enter the number please: "))

if number % 2 == 0:
	print(f"Number {number} is even")
else:
	print(f"Number {number} is odd")