text = "Hello, Python World!"

print(text[0])
print(text[-1])
print(text[:5])
print(text[-6:-1])

print(text.upper())
print(text.lower())
print(text.replace("Python", "Programming"))
print(text.split())
print(text.count("o"))

name = "CiA"
age = 18
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")

user = input("Enter your full name: ").strip().title()
fav_num = int(input("Enter your favourite number: "))
print(f"Hello {user}! Your favourite number doubled is {fav_num * 2}.")
