running = True
while running:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Say Your Name")
    print("3. Exit")
    print("Choose an option (1-3):")
    choice = input()

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Enter your name:")
        name = input()
        print("Your name is", name)
    elif choice == "3":
        print("Exiting... Goodbye!")
        running = False
    else:
        print("Invalid choice. Please select 1, 2, or 3.")