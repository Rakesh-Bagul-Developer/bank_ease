class Account:
    account_counter = 100  # Auto account number generator

    def __init__(self, name, initial_balance=0):
        Account.account_counter += 1
        self.account_number = Account.account_counter
        self.name = name
        self.balance = initial_balance
        self.transactions = []
        self.transactions.append(f"Account created with initial balance: ₹{initial_balance}")

    def deposit(self, amount):
        if amount <= 0:
            return "❌ Deposit amount must be greater than 0."

        self.balance += amount
        self.transactions.append(f"Deposited: ₹{amount}")
        return f"✅ Deposit successful! New Balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return "❌ Withdrawal amount must be greater than 0."

        if amount > self.balance:
            return "❌ Insufficient balance."

        self.balance -= amount
        self.transactions.append(f"Withdrawn: ₹{amount}")
        return f"✅ Withdrawal successful! Remaining Balance: ₹{self.balance}"

    def get_balance(self):
        return f"💰 Current Balance: ₹{self.balance}"

    def get_transactions(self):
        if not self.transactions:
            return "No transactions yet."
        return "\n".join(self.transactions)


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial deposit amount: "))

        account = Account(name, initial_balance)
        self.accounts[account.account_number] = account

        print(f"\n🎉 Account created successfully!")
        print(f"👉 Account Holder: {name}")
        print(f"👉 Account Number: {account.account_number}\n")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)

    def deposit_money(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)

        if not account:
            print("❌ Account not found.\n")
            return

        amount = float(input("Enter amount to deposit: "))
        print(account.deposit(amount), "\n")

    def withdraw_money(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)

        if not account:
            print("❌ Account not found.\n")
            return

        amount = float(input("Enter amount to withdraw: "))
        print(account.withdraw(amount), "\n")

    def check_balance(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)

        if not account:
            print("❌ Account not found.\n")
            return

        print(account.get_balance(), "\n")

    def show_transactions(self):
        acc_no = int(input("Enter account number: "))
        account = self.get_account(acc_no)

        if not account:
            print("❌ Account not found.\n")
            return

        print("\n📄 Transaction History:")
        print(account.get_transactions(), "\n")

    def menu(self):
        while True:
            print("=" * 40)
            print("         🏦 BANK EASE SYSTEM")
            print("=" * 40)
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
                print()

                if choice == 1:
                    self.create_account()
                elif choice == 2:
                    self.deposit_money()
                elif choice == 3:
                    self.withdraw_money()
                elif choice == 4:
                    self.check_balance()
                elif choice == 5:
                    self.show_transactions()
                elif choice == 6:
                    print("👋 Thank you for using Bank Ease!")
                    break
                else:
                    print("❌ Invalid choice. Try again.\n")

            except ValueError:
                print("❌ Invalid input. Please enter a number.\n")


if __name__ == "__main__":
    bank = BankSystem()
    bank.menu()
