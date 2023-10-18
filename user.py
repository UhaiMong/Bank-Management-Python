import random


class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = random.randint(1000, 9999)
        self.balance = 0
        self.transaction_history = []
        self.loan_taken = 0
        self.loan_limit = 2

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: +{amount}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: -{amount}')
        else:
            return "Withdrawal amount exceeded"

    def check_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_limit > 0:
            self.loan_taken += amount
            self.loan_limit -= 1
            self.deposit(amount)
            return f'Loan of {amount} taken successfully. Loan limit is: {self.loan_limit}.'
        else:
            return "Maximum loan limit reached."

    def transfer(self, recipient, amount):
        if recipient is None:
            return "Account does not exist"
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(
                f'Transfer to {recipient.name}: -{amount}')
            recipient.deposit(amount)
        else:
            return "The bank is bankrupt"

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: {self.balance}\nEmail: {self.email}\nAddress: {self.address}"
