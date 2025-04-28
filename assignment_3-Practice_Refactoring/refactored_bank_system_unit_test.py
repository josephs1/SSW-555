"""
    Assignment 3 - Practice Refactoring
    Group: Joseph Stefanoni, Hala Basyouni, Shrihit Saxena, Alice Zaytseva
    "I pledge my honor that I have abided by the Stevens Honor System."
    April 27, 2025

    Description: Unit tests for the Bank System user story after refactoring.
"""
import unittest
from refactored_bank_system import Account

class TestBankingOperations(unittest.TestCase):

    def setUp(self):
        self.account = Account("Test1", "123", "2025-04-27", "test1@example.com", "1234567890", "123 Main St")
        self.other_account = Account("Test2", "456", "2025-04-27", "test2@example.com", "0987654321", "456 Main St")

    def test_deposit_money_into_checking(self):
        self.assertEqual(self.account.get_balance('checking'), 0)
        self.account.deposit('checking', 100)
        self.assertEqual(self.account.get_balance('checking'), 100)

    def test_deposit_money_into_savings(self):
        self.assertEqual(self.account.get_balance('savings'), 0)
        self.account.deposit('savings', 200)
        self.assertEqual(self.account.get_balance('savings'), 200)

    def test_withdraw_money_from_checking(self):
        self.account.deposit('checking', 150)
        self.account.withdraw('checking', 50)
        self.assertEqual(self.account.get_balance('checking'), 100)

    def test_withdraw_money_from_savings(self):
        self.account.deposit('savings', 300)
        self.account.withdraw('savings', 100)
        self.assertEqual(self.account.get_balance('savings'), 200)

    def test_transfer_money_from_checking_to_another_account(self):
        self.account.deposit('checking', 500)
        self.account.transfer('checking', 200, self.other_account)
        self.assertEqual(self.account.get_balance('checking'), 300)
        self.assertEqual(self.other_account.get_balance('checking'), 200)

    def test_view_account_balances(self):
        self.account.deposit('checking', 120)
        self.account.deposit('savings', 380)
        self.assertEqual(self.account.get_balance('checking',), 120)
        self.assertEqual(self.account.get_balance('savings'), 380)

if __name__ == '__main__':
    unittest.main(verbosity=2)

