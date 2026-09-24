def get_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Try again.")

def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def small_program():
    while True:
        try:
            x = int(input("Enter any number: "))
            print(f"The double of {x} is {x * 2}")
            break
        except ValueError:
            print("Invalid number")

def main():
    age = get_int("Enter your age: ")
    print(f"You are {age} years old.")

    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = safe_divide(x, y)
        print("Result:", result)
    except ValueError as mistake:
        print("Error:", mistake)

    small_program()

    fruits = ["apple", "banana", "Orange"]
    while True:
        try:
            index = int(input("Enter a number to check the fruit there: "))
            print("The item at index", index,"is:", fruits[index])
            break
        except IndexError:
            print("Out of range")
        except ValueError:
            print("Invalid whole number")

    my_dict = {"name":"cia","profession":"Upcoming AI Native Engineer"}
    while True:
        try:
            key = input("Enter a key: ")
            print(my_dict[key]) 
            break
        except KeyError:
            print("Invalid key")
        except (KeyboardInterrupt, EOFError):
            print("Exiting the program")

main()
