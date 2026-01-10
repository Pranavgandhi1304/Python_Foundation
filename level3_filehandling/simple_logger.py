def append_message(filename, message):
    try:
        count = 1
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                count = len(lines) + 1
        except FileNotFoundError:
            pass
        with open(filename, "a") as f:
            f.write(str(count) + ". " + message + "\n")
        return True
    except Exception as e:
        print("Error writing log:", e)
        return False

def read_log(filename):
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

file = "log.txt"
running = True
while running:
    print("\nLogger Menu:")
    print("1. Add Message")
    print("2. Show Log")
    print("3. Exit")
    choice = input("Choose option (1-3): ")

    if choice == "1":
        msg = input("Enter message: ")
        if append_message(file, msg):
            print("Message logged.")
    elif choice == "2":
        log = read_log(file)
        if log:
            print("\nFull Log:")
            for line in log:
                print(line.strip())
        else:
            print("Log is empty.")
    elif choice == "3":
        print("Exiting logger")
        running = False
    else:
        print("Invalid choice.")