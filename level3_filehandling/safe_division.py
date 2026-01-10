def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result
    except ValueError:
        print("Error: Non-numeric input.")
        return None
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
#main function    
running = True
while running:
    print("\nSafe Division Menu:")
    print("1. Divide two numbers")
    print("2. Exit")
    choice = input("Choose option (1-2): ")
    if choice == "1":
        x = input("Enter first number: ")
        y = input("Enter second number: ")
        result = safe_divide(x, y)
        if result is not None:
            print("Result:", result)
    elif choice == "2":
        print("Exiting division program...")
        running = False
    else:
        print("Invalid choice.")