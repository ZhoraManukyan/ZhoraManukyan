from income import *
from expense import *

class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.transactions = []  # Store user transactions
        self.history_transactions = [] # Store history of transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.history_transactions.append(transaction.get_attributes())

    def get_history_transactions(self):
        return self.history_transactions

    def get_total_income(self):
        return sum(transaction.amount for transaction in self.transactions if isinstance(transaction, Income))

    def get_total_expenses(self):
        return sum(transaction.amount for transaction in self.transactions if isinstance(transaction, Expense))

    def get_savings(self):
        return self.get_total_income() - self.get_total_expenses()

    def get_user_id(self):
        return self.user_id
