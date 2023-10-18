from user import User
from admin import Admin


def main():
    admin = Admin()

    while True:
        print("\n1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_menu(admin)
        elif choice == '2':
            admin_menu(admin)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")


def user_menu(admin):
    print("\nUser Menu:")
    account_name = input("Enter your name: ")
    account_email = input("Enter your email: ")
    account_address = input("Enter your address: ")
    account_type = input("Enter account type (Savings/Current): ").lower()

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
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = int(input("Enter the deposit amount: "))
            user.deposit(amount)
            print(f"Deposited {amount} successfully.")
        elif choice == '2':
            amount = int(input("Enter the withdrawal amount: "))
            result = user.withdraw(amount)
            if result:
                print(result)
            else:
                print(f"Withdrew {amount} successfully.")
        elif choice == '3':
            print(f"Available balance: {user.check_balance()}")
        elif choice == '4':
            print("Transaction History:")
            for transaction in user.get_transaction_history():
                print(transaction)
        elif choice == '5':
            amount = int(input("Enter the loan amount: "))
            result = user.take_loan(amount)
            print(result)
        elif choice == '6':
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
        elif choice == '7':
            break
        else:
            print("Invalid choice. Try again.")


def admin_menu(admin):
    print("\nAdmin Menu:")
    while True:
        print("\n1. Delete Account")
        print("2. View User List")
        print("3. Total Bank Balance")
        print("4. Total Loan Amount")
        print("5. Toggle Loan Feature")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = int(input("Enter the account number to delete: "))
            result = admin.delete_account(account_number)
            print(result)
        elif choice == '2':
            print("User List:")
            for user in admin.get_user_list():
                print(user)
        elif choice == '3':
            print(f"Total Bank Balance: {admin.get_total_balance()}")
        elif choice == '4':
            print(f"Total Loan Amount: {admin.get_total_loan_amount()}")
        elif choice == '5':
            status = input(
                "Enter 1 to enable or 0 to disable the loan feature: ")
            admin.toggle_loan_feature(bool(int(status)))
            print("Loan feature updated.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")


def find_user_by_account_number(admin, account_number):
    for user in admin.get_user_list():
        if user.account_number == account_number:
            return user
    return None


if __name__ == "__main__":
    main()
