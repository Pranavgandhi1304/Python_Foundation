from file_handler import save_expense, load_expenses
from expense_logic import format_expense
def add_expense():
    while True:
        try:
            amount_str = input("Enter amount: ").strip()
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
        except ValueError:
            print("Invalid input. Amount must be numeric.")
            continue
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty.")
            continue
        note = input("Enter note: ").strip()
        if not note:
            print("Note cannot be empty.")
            continue
        save_expense(amount, category, note)
        print("Expense added successfully!")
        break
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses")
    for e in expenses:
        print(format_expense(e))

def show_total_spent():
    expenses = load_expenses()
    if not expenses:
        print("NO expenses recorded yet.")
        return
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal amount spend: {total}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("bye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

