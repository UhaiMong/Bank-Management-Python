# admin.py
class Admin:
    def __init__(self):
        self.user_accounts = []

    def create_account(self, user):
        self.user_accounts.append(user)

    def delete_account(self, account_number):
        for user in self.user_accounts:
            if user.account_number == account_number:
                self.user_accounts.remove(user)
                return f"Account {account_number} deleted successfully."
        return "Account not found."

    def get_user_list(self):
        return self.user_accounts

    def get_total_balance(self):
        total_balance = sum(user.balance for user in self.user_accounts)
        return total_balance

    def get_total_loan_amount(self):
        total_loan = sum(user.loan_taken for user in self.user_accounts)
        return total_loan

    def toggle_loan_feature(self, status):
        if status:
            for user in self.user_accounts:
                user.loan_limit = 2
        else:
            for user in self.user_accounts:
                user.loan_limit = 0
