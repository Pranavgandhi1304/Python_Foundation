def create_account(accounts):
    """
    Ask for name, generate unique account number, initialize balance=0.
    Returns updated accounts dict with new account added.
    """
    while True:
        name = input("Enter account holder name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    # Generate unique account number
    if accounts:
        max_acc_num = max(int(num) for num in accounts.keys())
        new_acc_num = str(max_acc_num + 1)
    else:
        new_acc_num = "1001"
    # Ensure no duplicates accounts
    while new_acc_num in accounts:
        new_acc_num = str(int(new_acc_num) + 1)
    accounts[new_acc_num] = {"name": name, "balance": 0}
    return accounts, new_acc_num