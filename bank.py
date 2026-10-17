# Task 3: Define a custom exception class (Optional Extension)
class InsufficientFundsError(Exception):
    """Custom exception raised when a withdrawal exceeds the account balance."""
    pass


class BankAccount:
    """Represents a standard bank account with deposit, withdrawal, and balance tracking."""
    
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount):
        """Adds funds to the account. Raises ValueError for non-positive amounts."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Subtracts funds from the account if sufficient balance exists.
        Raises InsufficientFundsError (or ValueError) if overdrawn.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        
        # Task 3: Raising InsufficientFundsError instead of ValueError
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: cannot withdraw ${amount:.2f} from account {self.account_number} (Current Balance: ${self.balance:.2f})."
            )
        
        self.balance -= amount
        return self.balance

    def __str__(self):
        """Returns a string representation of the bank account."""
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}"


class SavingsAccount(BankAccount):
    """Represents a savings account that inherits from BankAccount and supports interest."""
    
    def __init__(self, account_number, owner, balance=0, interest_rate=0.0):
        # Call the base class initializer
        super().__init__(account_number, owner, balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        """Calculates and adds annual interest based on the current balance and rate."""
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return self.balance

    def __str__(self):
        """Overrides __str__ to include the interest rate."""
        return f"Account {self.account_number} – Owner: {self.owner}, Balance: ${self.balance:.2f}, Interest Rate: {self.interest_rate}%"


# ==========================================
# Testing Demonstration
# ==========================================
if __name__ == "__main__":
    print("--- 1. Testing BankAccount ---")
    my_account = BankAccount("12345", "Alice", 500)
    print(my_account)

    # Successful deposit
    my_account.deposit(200)
    print(f"After depositing $200: {my_account}")

    # Successful withdrawal
    my_account.withdraw(150)
    print(f"After withdrawing $150: {my_account}")

    # Testing Overdraw Exception Handling
    print("\n--- Testing Exception Handling (Overdraw) ---")
    try:
        my_account.withdraw(1000)
    except InsufficientFundsError as e:
        print(f"Caught Expected Error: {e}")

    print("\n--- 2. Testing SavingsAccount ---")
    my_savings = SavingsAccount("SAV-999", "Bob", 1000, interest_rate=5.0)
    print(f"Before Interest: {my_savings}")

    # Apply interest (5% of 1000 = $50 added)
    my_savings.apply_interest()
    print(f"After Applying Interest: {my_savings}")

    # Testing inherited deposit/withdrawal on SavingsAccount
    my_savings.deposit(500)
    print(f"After depositing $500: {my_savings}")