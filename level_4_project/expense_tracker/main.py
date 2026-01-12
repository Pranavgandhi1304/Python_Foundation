from file_handler import load_expenses, save_expense
def main():
    save_expense(250, "Food", "Lunch at cafe")
    save_expense(1200, "Rent", "January rent")

    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
    else:
        print("Loaded expenses:")
        for e in expenses:
            print(f"{e['amount']} | {e['category']} | {e['note']}")

if __name__ == "__main__":
    main()