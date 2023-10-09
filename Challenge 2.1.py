class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance:.2f}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount(account_number="123456", account_holder_name="John Doe", initial_balance=1000.0)

    # Display initial balance
    account.display_balance()

    # Deposit money
    account.deposit(500.0)
    account.display_balance()

    # Withdraw money
    account.withdraw(200.0)
    account.display_balance()

    # Attempt to withdraw more than the balance
    account.withdraw(2000.0)
    account.display_balance()
