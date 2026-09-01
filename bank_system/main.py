from bank_system.BankClass import Bank

if __name__ == "__main__":

    bank_account = Bank()
    while True:
        print("Welcome to the Bank System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Pay")
        print("4. Get Account Details")
        print("5. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter your name: ")
                phone = input("Enter your phone number: ")
                password = input("Enter your password: ")
                balance = float(input("Enter initial balance: "))
                account_number = input("Enter account number: ")
                try:
                    account = bank_account.create_account(name, phone, password, balance, account_number)
                    print(f"Account created successfully: {account}")
                except ValueError as e:
                    print(e)
            case "2":
                try:
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")
                    amount = float(input("Enter amount to deposit: "))
                    result = bank_account.deposit(name, password, amount)
                    print(result)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            case "3":
                try:
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")
                    amount = float(input("Enter amount to pay: "))
                    result = bank_account.pay(name, password, amount)
                    print(result)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            case "4":
                try:
                    name = input("Enter your name: ")
                    password = input("Enter your password: ")
                    account = bank_account.get_account(name, password)
                    if account:
                        print(f"Account Details: {account}")
                    else:
                        print("No account found.")
                except Exception as e:
                    print(f"An error occurred: {e}")

            case "5":
                print("Exiting the Bank System. Goodbye!")
                break