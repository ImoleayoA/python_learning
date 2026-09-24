fruits = ["Apple", "Avocado", "Banana", "Orange"]

for fruit in  fruits:
    print(fruit)

print(fruits[0])
print(fruits[-1])
fruits[0] = "Strawberry"
fruits.append("PawPaw")
fruits.insert(1, "Date")
fruits.remove("Date")
print(fruits)

for i, fruit in enumerate(fruits):
    print(i, fruit)

numbers = [1, 3, 2, 4, 5]
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))

numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)

