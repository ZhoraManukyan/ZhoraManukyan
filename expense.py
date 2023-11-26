from transactions import Transaction

class Expense(Transaction):
    def __init__(self, amount, date, description):
        super().__init__(amount, date, description)

class OneTimePurchase(Expense):
    def __init__(self, amount, date, description):
        super().__init__(amount, date, description)

class Subscription(Expense):
    def __init__(self, amount, date, description):
        super().__init__(amount, date, description)
