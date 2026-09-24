age = int(input("Enter your age: "))

if age < 13:
	print("You are a child.")
elif  age >= 13 and age <= 17:
	print("You are a teenager.")
elif age >= 18 and age <= 64:
	print("You are an adult")
else:
	print("You are a senior")

num = int(input("Enter a number: "))
if num % 2 == 0:
	print("It is even")
else:
	print("It is odd")
