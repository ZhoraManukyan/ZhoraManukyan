class Transaction:
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description
    def get_attributes(self):
        return [self.amount, self.date, self.description]
