class Bank:
    __account = []
    def __init__(self):
        self.__account =  []


    @staticmethod
    def create_account(name, phone, password , balance, account_number):
        if isinstance(name, str) and isinstance(phone, str) and isinstance(password, str) and isinstance(balance, (int, float)) and isinstance(account_number, str):
            account = {
                "name": name,
                "phone" : phone,
                "password": password,
                "balance": balance,
                "account_number": account_number
            }
            Bank.__account.append(account)
            return account
        else:
            raise ValueError("Invalid data types for account creation.")

    @staticmethod
    def get_account(name, password):
        for account in Bank.__account:
            if account["name"] == name and account["password"] == password:
                return account
        return None

    @staticmethod
    def deposit(name, password, amount):
        if amount > 0:
            for account in Bank.__account:
                if account["name"] == name and account["password"] == password:
                    account["balance"] += amount
                    return f"Deposited {amount}. New balance is {account['balance']}."
            return "Account not found or incorrect password."
        else:
            return "Deposit amount must be positive."
        
    @staticmethod
    def pay(name, password, amount):
        if amount > 0:
            for account in Bank.__account:
                if account["name"] == name and account["password"] == password:
                    if account["balance"] >= amount:
                        account["balance"] -= amount
                        return f"Paid {amount}. New balance is {account['balance']}."
                    else:
                        return "Insufficient balance."
            return "Account not found or incorrect password."
        else:
            return "Payment amount must be positive."