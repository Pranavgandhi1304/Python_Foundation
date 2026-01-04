
def add(a, b):
    result = a + b
    print("DEBUG: add result =", result)
    return result

def sub(a, b):
    result = a - b
    print("DEBUG: sub result =", result)
    return result

def mul(a, b):
    result = a * b
    print("DEBUG: mul result =", result)
    return result

def div(a, b):
    result = a / b
    print("DEBUG: div result =", result)
    return result

running = True
while running:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose option (1-5): ")

    if choice == "1":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", add(x, y))
    elif choice == "2":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", sub(x, y))
    elif choice == "3":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", mul(x, y))
    elif choice == "4":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        if y != 0:
            print("Result:", div(x, y))
        else:
            print("Error: Division by zero")
    elif choice == "5":
        print("Exiting calculator...")
        running = False
    else:
        print("Invalid choice. Try again.")