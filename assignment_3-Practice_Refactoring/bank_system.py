"""
    Assignment 3 - Practice Refactoring
    Group: Joseph Stefanoni, Hala Basyouni, Shrihit Saxena, Alice Zaytseva
    "I pledge my honor that I have abided by the Stevens Honor System."
    April 27, 2025

    Main User Story: Bank System
        As a user, I want to manage my bank account (deposit, withdraw, transfer funds, and check my balance) so that I can securely control my finances.
    Detailed User Stories:
        1. Deposit Money: As a user, I want to deposit money into my account so that I can increase my balance.
        2. Withdraw Money: As a user, I want to withdraw money from my account so that I can access my funds.
        3. Transfer Money: As a user, I want to transfer money from my account to another user's account so that I can send money easily.
        4. Prevent Overdraft: As a user, I want to be prevented from withdrawing or transferring more money than I have so that I don't go into debt.
        5. View Balance: As a user, I want to view my account balance so that I can see how much money I have.

    Manual Test Cases (Gherkin Language):
        1. Feature: Deposit money into checking account
            - Scenario: User deposits money successfully
                - Given a user with a checking account balance of $0
                - When the user deposits $100 into the checking account
                - Then the checking account balance should be $100

        2. Feature: Deposit money into savings account
            - Scenario: User deposits money successfully
                - Given a user with a savings account balance of $0
                - When the user deposits $200 into the savings account
                - Then the savings account balance should be $200

        3. Feature: Withdraw money from checking account
            - Scenario: User withdraws money successfully
                - Given a user with a checking account balance of $150
                - When the user withdraws $50 from the checking account
                - Then the checking account balance should be $100

        4. Feature: Withdraw money from savings account
            - Scenario: User withdraws money successfully
                - Given a user with a savings account balance of $300
                - When the user withdraws $100 from the savings account
                - Then the savings account balance should be $200

        5. Feature: Transfer money from checking to another account
            - Scenario: User transfers money successfully
                - Given a user A with a checking account balance of $500
                - And a user B with a checking account balance of $0
                - When user A transfers $200 to user B
                - Then user A's checking balance should be $300
                - And user B's checking balance should be $200

        6. Feature: View account balances
            - Scenario: User views their checking and savings balances
                - Given a user with a checking balance of $120 and savings balance of $380
                - When the user requests to view their balances
                - Then the system should display $120 for checking and $380 for savings
"""

class Account:

    def __init__(self, owner_name, account_id, date_created, email, phone_number, address):
        self.owner_name = owner_name
        self.account_id = account_id
        self.date_created = date_created
        self.checking_balance = 0.0
        self.savings_balance = 0.0
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def deposit_checking(self, amount):
        self.checking_balance += amount
        print(f"Deposited ${amount} to checking account. New balance is ${self.get_checking_balance}.")

    def deposit_savings(self, amount):
        self.savings_balance += amount
        print(f"Deposited ${amount} to savings account. New balance is ${self.get_savings_balance}.")

    def get_checking_balance(self):
        return self.checking_balance
    
    def print_checking_balance(self):
        print(f"Checking account balance: ${self.get_checking_balance()}")
    
    def get_savings_balance(self):
        return self.savings_balance
    
    def print_savings_balance(self):
        print(f"Savings account balance: ${self.get_savings_balance()}")
    
    def withdraw_checking(self, amount):
        if amount > self.checking_balance:
            print("Amount is greater than checking balance. Withdrawal not allowed.")
        else:
            self.checking_balance -= amount
            print(f"Withdrew ${amount} from checking account. New balance is ${self.get_checking_balance}.")

    def withdraw_savings(self, amount):
        if amount > self.savings_balance:
            print("Amount is greater than savings balance. Withdrawal not allowed.")
        else:
            self.savings_balance -= amount
            print(f"Withdrew ${amount} from savings account. New balance is ${self.get_savings_balance}.")

    def transfer_from_checking(self, amount, target_account):
        if amount > self.checking_balance:
            print("Amount is greater than checking balance. Transfer not allowed.")
        else:
            self.checking_balance -= amount
            target_account.deposit_checking(amount)
            print(f"Transferred ${amount} to {target_account.owner_name}'s account. New balance is ${self.get_checking_balance}.")

    def transfer_from_savings(self, amount, target_account):
        if amount > self.savings_balance:
            print("Amount is greater than savings balance. Transfer not allowed.")
        else:
            self.savings_balance -= amount
            target_account.deposit_savings(amount)
            print(f"Transferred ${amount} to {target_account.owner_name}'s account. New balance is ${self.get_savings_balance}.")
