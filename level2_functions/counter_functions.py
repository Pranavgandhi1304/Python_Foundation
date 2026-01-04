def adjust_count(current, change):
    updated = current + change
    print("current =", current, "change =", change, "updated =", updated)
    return updated

count = 0
running = True
while running:
    print("\nCounter Menu:")
    print("1. Increase Count")
    print("2. Decrease Count")
    print("3. Exit")
    choice = input("Choose option (1-3): ")

    if choice == "1":
        adj = int(input("Enter adjustment value to increase: "))
        count = adjust_count(count, adj)
        print("Current count:", count)
    elif choice == "2":
        adj = int(input("Enter adjustment value to decrease: "))
        count = adjust_count(count, -adj)
        print("Current count:", count)
    elif choice == "3":
        print("Exiting counter...")
        running = False
    else:
        print("Invalid choice. Try again.")
