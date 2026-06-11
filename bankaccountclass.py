class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self.balance: float = balance
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.history.append(f"Deposited ₹{amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")

        self.balance -= amount
        self.history.append(f"Withdrew ₹{amount}")

    def get_balance(self) -> float:
        return self.balance

    def transaction_history(self) -> list[str]:
        return self.history


# Example Usage
account = BankAccount("Shahana", 1000)

account.deposit(500)
account.withdraw(200)

print("Balance:", account.get_balance())

print("\nTransactions:")
for transaction in account.transaction_history():
    print(transaction)