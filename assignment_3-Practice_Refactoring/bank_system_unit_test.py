"""
    Assignment 3 - Practice Refactoring
    Group: Joseph Stefanoni, Hala Basyouni, Shrihit Saxena, Alice Zaytseva
    "I pledge my honor that I have abided by the Stevens Honor System."
    April 27, 2025

    Description: Unit tests for the Bank System user story.
"""
import unittest

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

    def deposit_savings(self, amount):
        self.savings_balance += amount

    def get_checking_balance(self):
        return self.checking_balance

    def get_savings_balance(self):
        return self.savings_balance

    def withdraw_checking(self, amount):
        if amount > self.checking_balance:
            pass
        else:
            self.checking_balance -= amount

    def withdraw_savings(self, amount):
        if amount > self.savings_balance:
            pass
        else:
            self.savings_balance -= amount

    def transfer_from_checking(self, amount, target_account):
        if amount > self.checking_balance:
            pass
        else:
            self.checking_balance -= amount
            target_account.deposit_checking(amount)

    def transfer_from_savings(self, amount, target_account):
        if amount > self.savings_balance:
            pass
        else:
            self.savings_balance -= amount
            target_account.deposit_savings(amount)


class TestBankingOperations(unittest.TestCase):

    def setUp(self):
        self.account = Account("Test User", "123", "2025-04-27", "test@example.com", "1234567890", "123 Main St")
        self.other_account = Account("Other User", "456", "2025-04-27", "other@example.com", "0987654321", "456 Main St")

    def test_deposit_money_into_checking(self):
        self.assertEqual(self.account.get_checking_balance(), 0)
        self.account.deposit_checking(100)
        self.assertEqual(self.account.get_checking_balance(), 100)

    def test_deposit_money_into_savings(self):
        self.assertEqual(self.account.get_savings_balance(), 0)
        self.account.deposit_savings(200)
        self.assertEqual(self.account.get_savings_balance(), 200)

    def test_withdraw_money_from_checking(self):
        self.account.deposit_checking(150)
        self.account.withdraw_checking(50)
        self.assertEqual(self.account.get_checking_balance(), 100)

    def test_withdraw_money_from_savings(self):
        self.account.deposit_savings(300)
        self.account.withdraw_savings(100)
        self.assertEqual(self.account.get_savings_balance(), 200)

    def test_transfer_money_from_checking_to_another_account(self):
        self.account.deposit_checking(500)
        self.account.transfer_from_checking(200, self.other_account)
        self.assertEqual(self.account.get_checking_balance(), 300)
        self.assertEqual(self.other_account.get_checking_balance(), 200)

    def test_view_account_balances(self):
        self.account.deposit_checking(120)
        self.account.deposit_savings(380)
        self.assertEqual(self.account.get_checking_balance(), 120)
        self.assertEqual(self.account.get_savings_balance(), 380)


if __name__ == '__main__':
    unittest.main(verbosity=2)