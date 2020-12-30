#Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

#on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

def calculate_leap_year(year):
	if year % 4 == 0:
		#leap
		if year % 100 == 0:
			if year % 400 == 0:
				print(f"Year {year} is leap year")
			else:
				print(f"Year {year} is not a leap year")
		else:
			print(f"Year {year} is leap year")
	else:
		print(f"Year {year} is not leap")





year = int(input("Enter the year please: "))
calculate_leap_year(year)