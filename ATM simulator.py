# Sample user account data
user_accounts = {
    "128": {"name": "Yogesh", "balance": 4000},
    "095": {"name": "sanskruti", "balance": 5100},
    "089": {"name": "rishita", "balance": 3500},
    "106": {"name": "sneha", "balance": 3100},
    "097": {"name": "shantanu", "balance": 3300}
}

def display_menu():
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance(account):
    return account["balance"]

def deposit(account, amount):
    account["balance"] += amount
    return account["balance"]

def withdraw(account, amount):
    if account["balance"] >= amount:
        account["balance"] -= amount
        return account["balance"]
    else:
        return "Insufficient funds"

def main():
    print("Welcome to the ATM!")
    account_number = input("Enter your account number: ")

    if account_number in user_accounts:
        account = user_accounts[account_number]
        print(f"Hello, {account['name']}!")

        while True:
            display_menu()
            choice = input("Select an option (1/2/3/4): ")

            if choice == '1':
                balance = check_balance(account)
                print(f"Your balance: ${balance}")
            elif choice == '2':
                amount = float(input("Enter the deposit amount: "))
                new_balance = deposit(account, amount)
                print(f"New balance: ${new_balance}")
            elif choice == '3':
                amount = float(input("Enter the withdrawal amount: "))
                result = withdraw(account, amount)
                print(result)
            elif choice == '4':
                print("Thank you for using the ATM. Have a nice day!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Account not found. Please check your account number.")

if __name__ == "__main__":
    main()
