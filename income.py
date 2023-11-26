from transactions import Transaction

class Income(Transaction):
    def __init__(self, amount, date, description):
        super().__init__(amount, date, description)

class OneTimePayment(Income):
    def __init__(self, amount, date, description):
        super().__init__(amount, date, description)

class Salary(Income):
    def __init__(self, amount, date, description):
        super().__init__(amount, date, description)
