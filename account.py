""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# account.py

class Account:
    def __init__(self, account_number, owner_name, balance=0):
        self.set_account_number(account_number)
        self.set_owner_name(owner_name)
        self.set_balance(balance)

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        if isinstance(account_number, str) and account_number.isdigit():
            self.__account_number = account_number
        else:
            raise ValueError("Invalid account number. It must be a string of digits.")

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, owner_name):
        if isinstance(owner_name, str) and owner_name.strip():
            self.__owner_name = owner_name
        else:
            raise ValueError("Invalid owner name. It must be a non-empty string.")

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Invalid balance amount. It must be a non-negative number.")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount. Deposit amount must be greater than zero.")
        self.__balance += amount
        print(f"Deposited ${amount}. New balance is ${self.__balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount. Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds. Cannot withdraw more than the current balance.")
        self.__balance -= amount
        print(f"Withdrew ${amount}. Remaining balance is ${self.__balance}.")