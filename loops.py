
for num in range(1, 11):
    print(num)

number = int(input("Enter a number: "))

while number > 0:
    print(number)
    number = number -1
print("Blast Off!")

result = 0
adding = int(input("Enter a number: "))
for i in range(1, adding + 1):
    result += i
print("The sum is", result)

mult = int(input("Enter a number: "))
for x in range(1, 11):
    resultx = mult * x
    print(mult, "x", x, "=", resultx)

password = "python123"
passw = ""
while passw != password:
    passw = input("Enter your password: ")
print("Access granted")
