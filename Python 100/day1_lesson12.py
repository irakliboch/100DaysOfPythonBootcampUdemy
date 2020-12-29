#Write a program that switches the values stored in the variables a and b.
a = input("Assign a value to variable a: ")
b = input("Assign a value to variable b: ")
print(a)
print(b)

#Introduce switch variable
c = a
a = b
b = c

print(f"We made some switches. Variable a is now {a}.Variable b is now {b}")



