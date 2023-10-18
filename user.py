class User:
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.acount_type = account_type
        self.balance = 0
        self.account_number = None
        self.transaction_history = []
        self.loan_count = 0

    def generate_account_number(self, account_number_generator):
        self.account_number = account_number_generator.generate()

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: ${amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            return "Withdraw amount exceeded!"
        else:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: ${amount}')

    def check_balance(self):
        return self.balance

    def show_history(self):
        return self.transaction_history

    def taking_loan(self, amount):
        if self.loan_count < 2:
            self.loan_count += 1
            self.balance += amount
            self.transaction_history.append(f'Loan: ${amount}')
        else:
            return f'Your limit is ${self.loan_count}'

    def transfer(self, to_other, amount):
        if to_other is None:
            return "Account dose not exist"
        if amount > self.balance:
            return "Withdraw amount exceeded!"
        else:
            self.balance -= amount
            self.transaction_history.append(
                f'Transfer: ${amount} to {to_other.name}')
            to_other.deposit(amount)
