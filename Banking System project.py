# Simple banking system
class BankingSystem:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than ₹0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Withdrawal amount must be greater than ₹0.")

def main():
    print("Welcome to the Banking System!")
    username = input("Enter your name: ")
    pin = input("Set a 4-digit PIN: ")
    user = BankingSystem(username, pin)

    while True:
        print("\nChoose an option:")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                user.check_balance()
            elif choice == 2:
                amount = float(input("Enter amount to deposit: ₹"))
                user.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter amount to withdraw: ₹"))
                user.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the Banking System!")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
main()