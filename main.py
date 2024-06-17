""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: main.py
# Description: Contains the user interface for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from bank import BankManager
from utility import get_float

def create_account(manager):
    owner_name = input("Enter the owner's name: ")
    account_number = input("Enter the account number: ")
    try:
        manager.create_account(owner_name, account_number)
    except ValueError as e:
        print(e)

def deposit(manager):
    account_number = input("Enter the account number: ")
    amount = get_float("Enter the amount to deposit: ")
    try:
        manager.deposit(account_number, amount)
    except ValueError as e:
        print(e)

def withdraw(manager):
    account_number = input("Enter the account number: ")
    amount = get_float("Enter the amount to withdraw: ")
    try:
        manager.withdraw(account_number, amount)
    except ValueError as e:
        print(e)

def transfer(manager):
    source_account_number = input("Enter the source account number: ")
    destination_account_number = input("Enter the destination account number: ")
    amount = get_float("Enter the amount to transfer: ")
    try:
        manager.transfer_money(source_account_number, destination_account_number, amount)
    except ValueError as e:
        print(e)

def show_balance(manager):
    account_number = input("Enter the account number: ")
    account = manager.account_exists(account_number)
    if account:
        print(f"Balance for account {account_number}: ${account.get_balance()}")
    else:
        print("Account does not exist.")

def main():
    manager = BankManager()
    actions = {
        "1": create_account,
        "2": deposit,
        "3": withdraw,
        "4": transfer,
        "5": show_balance,
        "6": exit
    }

    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Show Balance")
        print("6. Exit")
        choice = input("Choose an action: ")

        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid choice. Please select a valid action.")

if __name__ == "__main__":
    main()