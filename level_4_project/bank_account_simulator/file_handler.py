import os
def get_accounts_file():
    return os.path.join(os.path.dirname(__file__), "data", "accounts.txt")
def save_account(account_number, name, balance):
    """
    Append a new account to the file.
    Format: account_number,name,balance
    """
    accounts_file = get_accounts_file()
    try:
        with open(accounts_file, "a", encoding="utf-8") as f:
            f.write(f"{account_number},{name},{balance}\n")
    except Exception:
        pass

def load_accounts():
    """
    Load accounts from file.
    Returns dict: { "1001": {"name": "Pranav", "balance": 5000}, ... }
    Handles missing/empty file gracefully.
    """
    accounts_file = get_accounts_file()
    if not os.path.exists(accounts_file):
        return {}
    with open(accounts_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    accounts = {}
    for line in lines:
        parts = line.split(",")
        if len(parts) == 3:
            acc_num, name, balance_str = parts
            try:
                balance = float(balance_str)
                accounts[acc_num] = {"name": name, "balance": balance}
            except ValueError:
                continue
    return accounts