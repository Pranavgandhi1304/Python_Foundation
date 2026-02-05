from file_handler import load_accounts, save_account
from account_logic import create_account

def main():
    accounts = load_accounts()
    print("\nAccount System")
    accounts, new_acc_num = create_account(accounts)
    new_acc = accounts[new_acc_num]
    save_account(new_acc_num, new_acc["name"], new_acc["balance"])
    print(f"Account created successfully!")
    print(f"Account Number: {new_acc_num} | Name: {new_acc['name']} | Balance: {new_acc['balance']}")

if __name__ == "__main__":
    main()