""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: account.py
# Description: Contains the base Account class and derived classes.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Account:
    """Represents a bank account with basic operations."""
    
    def __init__(self, account_number, owner_name, balance=0):
        """Initialize account with account number, owner name, and optional balance."""
        self.set_account_number(account_number)
        self.set_owner_name(owner_name)
        self.set_balance(balance)

    def get_account_number(self):
        """Return the account number."""
        return self.__account_number

    def set_account_number(self, account_number):
        """Set the account number after validating it is a string of digits."""
        if isinstance(account_number, str) and account_number.isdigit():
            self.__account_number = account_number
        else:
            raise ValueError("Invalid account number. It must be a string of digits.")

    def get_owner_name(self):
        """Return the owner's name."""
        return self.__owner_name

    def set_owner_name(self, owner_name):
        """Set the owner's name after validating it is a non-empty string."""
        if isinstance(owner_name, str) and owner_name.strip():
            self.__owner_name = owner_name
        else:
            raise ValueError("Invalid owner name. It must be a non-empty string.")

    def get_balance(self):
        """Return the current balance."""
        return self.__balance

    def set_balance(self, balance):
        """Set the balance after validating it is a non-negative number."""
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Invalid balance amount. It must be a non-negative number.")

    def deposit(self, amount):
        """Deposit the given amount into the account after validating it is positive."""
        if amount <= 0:
            raise ValueError("Invalid deposit amount. Deposit amount must be greater than zero.")
        self.__balance += amount
        print(f"Deposited ${amount}. New balance is ${self.__balance}.")

    def withdraw(self, amount):
        """Withdraw the given amount from the account after validating it is positive and does not exceed the balance."""
        if amount <= 0:
            raise ValueError("Invalid withdrawal amount. Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds. Cannot withdraw more than the current balance.")
        self.__balance -= amount
        print(f"Withdrew ${amount}. Remaining balance is ${self.__balance}.")