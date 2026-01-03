print("Enter a positive integer n:")
user_input = input()
# Basic validation
# Ensure input is digits and greater than 0
if user_input.isdigit():
    n = int(user_input)
    if n > 0:
        total = 0
        current = 1
        # Sum from 1 to n
        while current <= n:
            total = total + current
            current = current + 1
        print("Sum from 1 to", n, "is", total)
    else:
        print("n must be greater than 0.")
else:
    print("Invalid input. Please enter digits only.")