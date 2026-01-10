def save_record(filename, name, marks):
    try:
        marks = int(marks)
        if marks < 0 or marks > 100:
            print("Invalid marks. Must be between 0 and 100.")
            return False
        with open(filename, "a") as f:
            f.write(name + "," + str(marks) + "\n")
        return True
    except ValueError:
        print("Invalid input. Marks must be a number.")
        return False

def read_records(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        return []
    
file = "students.txt"
running = True
while running:
    print("\nStudent Record Menu:")
    print("1. Add Record")
    print("2. Show All Records")
    print("3. Exit")
    choice = input("Choose option (1-3): ")
    if choice == "1":
        name = input("Enter student name: ")
        marks = input("Enter marks: ")
        if save_record(file, name, marks):
            print("Record saved.")
    elif choice == "2":
        records = read_records(file)
        if records:
            print("\nAll Records:")
            for line in records:
                print(line.strip())
        else:
            print("No records found.")
    elif choice == "3":
        print("Exiting...")
        running = False
    else:
        print("Invalid choice.")