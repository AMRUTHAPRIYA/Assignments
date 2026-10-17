from bank import BankAccount, InsufficientFundsError

class SavingsAccount(BankAccount):
    """Represents a savings account that inherits from BankAccount and supports interest."""
    
    def __init__(self, account_number, owner, balance=0, interest_rate=0.0):
        # Call the base class initializer
        super().__init__(account_number, owner, balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        """Calculates and adds annual interest based on current balance and rate."""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return self.balance

    def __str__(self):
        """Overrides __str__ to include the interest rate."""
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"


# Test code for SavingsAccount
if __name__ == "__main__":
    print("--- Testing SavingsAccount ---")
    my_savings = SavingsAccount("SAV-999", "Bob", 1000, interest_rate=5.0)
    print(f"Before Interest: {my_savings}")

    # Apply interest (5% of 1000 = $50 added)
    my_savings.apply_interest()
    print(f"After Applying Interest: {my_savings}")

    # Testing inherited deposit/withdrawal and exception handling
    my_savings.deposit(500)
    print(f"After depositing $500: {my_savings}")

    try:
        my_savings.withdraw(3000)
    except InsufficientFundsError as e:
        print(f"Caught Expected Error: {e}")