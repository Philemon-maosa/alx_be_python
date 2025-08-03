import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')

    amount = None
    if command in ["deposit", "withdraw"]:
        try:
            amount = float(params[0])
        except (IndexError, ValueError):
            print("Please provide a valid amount.")
            sys.exit(1)

    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
