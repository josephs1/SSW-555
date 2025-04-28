"""
    Assignment 3 - Practice Refactoring
    Group: Joseph Stefanoni, Hala Basyouni, Shrihit Saxena, Alice Zaytseva
    "I pledge my honor that I have abided by the Stevens Honor System."
    April 27, 2025

    Description: Refactored Bank System user story.
"""
class Account:
    def __init__(self, owner_name, account_id, date_created, email, phone_number, address):
        self.owner_name = owner_name
        self.account_id = account_id
        self.balances = {
            "checking": 0.0,
            "savings": 0.0
        }
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def deposit(self, account_type, amount):
        if account_type in self.balances:
            self.balances[account_type] += amount
            return f"Deposited ${amount} to {account_type}."
        else:
            return "Invalid account type."
        
    def withdraw(self, account_type, amount):
        if account_type in self.balances:
            if amount <= self.balances[account_type]:
                self.balances[account_type] -= amount
                return f"Withdrew ${amount} from {account_type}."
            else:
                return f"Insufficient funds in {account_type}."
        else:
            return "Invalid account type."
        
    def transfer(self, from_account_type, amount, target_account):
        if from_account_type in self.balances:
            if amount <= self.balances[from_account_type]:
                self.balances[from_account_type] -= amount
                target_account.deposit(from_account_type, amount)
                return f"Transferred ${amount} from {from_account_type} to {target_account.owner_name}."
            else:
                return f"Insufficient funds to transfer from {from_account_type}."
        else:
            return "Invalid account type."
        
    def get_balance(self, account_type):
        return self.balances.get(account_type, "Invalid account type.")
    
    def view_balances(self):
        return f"Checking: ${self.balances['checking']}, Savings: ${self.balances['savings']}"