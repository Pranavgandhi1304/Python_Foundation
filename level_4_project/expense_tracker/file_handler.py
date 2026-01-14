import os
def get_expenses_file():
    return os.path.join(os.path.dirname(__file__), "data", "expenses.txt")
def load_expenses():
    expenses_file = get_expenses_file()
    if not os.path.exists(expenses_file):
        return []
    with open(expenses_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    expenses = []
    for line in lines:
        parts = line.split("|")
        if len(parts) == 3:
            try:
                amount = float(parts[0])
                category = parts[1]
                note = parts[2]
                expenses.append({"amount": amount, "category": category, "note": note})
            except ValueError:
                continue
    return expenses

def save_expense(amount, category, note):
    expenses_file = get_expenses_file()
    try:
        with open(expenses_file, "a", encoding="utf-8") as f:
            f.write(f"{amount}|{category}|{note}\n")
    except Exception:
        pass
