from user import User
from admin import Admin


def main():
    admin = Admin()

    while True:
        print("\n1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")
        operate = input("Operation: ")

        if operate == '1':
            user_menu(admin)
        elif operate == '2':
            admin_menu(admin)
        elif operate == '3':
            break
        else:
            print("Invalid operation. Plz, Try again.")


def user_menu(admin):
    print("\nUser Menu:")
    account_name = input("User Name: ")
    account_email = input("Email: ")
    account_address = input("Address: ")
    account_type = input("Account type (Savings/Current): ").lower()

    user = User(account_name, account_email, account_address, account_type)
    admin.create_account(user)
    print(
        f"Account created successfully. Your account number is: {user.account_number}")

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Back to Main Menu")
        operate = input("Operation: ")

        if operate == '1':
            amount = int(input("Enter the deposit amount: "))
            user.deposit(amount)
            print(f"Deposited {amount} successfully.")
        elif operate == '2':
            amount = int(input("Enter the withdrawal amount: "))
            result = user.withdraw(amount)
            if result:
                print(result)
            else:
                print(f"Withdrew {amount} successfully.")
        elif operate == '3':
            print(f"Available balance: {user.check_balance()}")
        elif operate == '4':
            print("Transaction History:")
            for transaction in user.get_transaction_history():
                print(transaction)
        elif operate == '5':
            amount = int(input("Enter the loan amount: "))
            result = user.take_loan(amount)
            print(result)
        elif operate == '6':
            recipient_account_number = int(
                input("Enter recipient's account number: "))
            recipient = find_user_by_account_number(
                admin, recipient_account_number)
            if recipient:
                # Allow the user to input the transfer amount
                amount = int(input("Enter the amount to transfer: "))
                result = user.transfer(recipient, amount)
                if result:
                    print(result)
                else:
                    print(
                        f"Transferred {amount} to {recipient.name} successfully.")
            else:
                print("Recipient account does not exist.")
        elif operate == '7':
            break
        else:
            print("Invalid operation. Plz, Try again.")


def admin_menu(admin):
    print("\nAdmin Menu:")
    while True:
        print("\n1. Delete Account")
        print("2. View User List")
        print("3. Total Bank Balance")
        print("4. Total Loan Amount")
        print("5. Toggle Loan Feature")
        print("6. Back to Main Menu")
        operate = input("Operation: ")

        if operate == '1':
            account_number = int(input("Enter the account number to delete: "))
            result = admin.delete_account(account_number)
            print(result)
        elif operate == '2':
            print("User List:")
            for user in admin.get_user_list():
                print(user)
        elif operate == '3':
            print(f"Total Bank Balance: {admin.get_total_balance()}")
        elif operate == '4':
            print(f"Total Loan Amount: {admin.get_total_loan_amount()}")
        elif operate == '5':
            status = input(
                "Enter 1 to enable or 0 to disable the loan feature: ")
            admin.toggle_loan_feature(bool(int(status)))
            print("Loan feature updated.")
        elif operate == '6':
            break
        else:
            print("Invalid Operation. Plz, Try again.")


def find_user_by_account_number(admin, account_number):
    for user in admin.get_user_list():
        if user.account_number == account_number:
            return user
    return None


if __name__ == "__main__":
    main()
