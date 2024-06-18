""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# File: bank.py
# Description: Contains the facade class for the banking system.
# Author: 
# Date: 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from account import Account

class BankManager:
    """Facade class to manage multiple bank accounts."""

    def __init__(self):
        """Initialize the bank manager with an empty list of accounts."""
        self._accounts = []

    def account_exists(self, account_number):
        """Check if an account exists by account number and return it if found."""
        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def create_account(self, owner_name, account_number):
        """Create a new account with the given owner name and account number if it does not already exist."""
        if self.account_exists(account_number):
            raise ValueError(f"Account with number {account_number} already exists.")        
        new_account = Account(account_number, owner_name, 0)
        self._accounts.append(new_account)
        print(f"Account {account_number} created successfully for {owner_name}.")

    def deposit(self, account_number, amount):
        """Deposit the given amount into the specified account if it exists."""
        account = self.account_exists(account_number)
        if account:
            account.deposit(amount)
        else:
            raise ValueError(f"Account with number {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        """Withdraw the given amount from the specified account if it exists and has sufficient funds."""
        account = self.account_exists(account_number)
        if account:
            account.withdraw(amount)
        else:
            raise ValueError(f"Account with number {account_number} does not exist.")

    def transfer_money(self, source_account_number, destination_account_number, amount):
        """Transfer the given amount from the source account to the destination account if both exist and have sufficient funds."""
        source_account = self.account_exists(source_account_number)
        destination_account = self.account_exists(destination_account_number)        
        if not source_account:
            raise ValueError(f"Source account with number {source_account_number} does not exist.")
        if not destination_account:
            raise ValueError(f"Destination account with number {destination_account_number} does not exist.")        
        source_account.withdraw(amount)
        destination_account.deposit(amount)
        print(f"Transferred ${amount} from account {source_account_number} to {destination_account_number}.")