import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from user import *

class PersonalFinanceManager:
    def __init__(self):
        self.users = []
        self.users_id = []

    @property
    def get_users_id(self):
        return self.users_id

    def create_user(self, user_id, username):
        new_user = User(user_id, username)
        self.users.append(new_user)
        self.users_id.append(new_user.get_user_id())
        return new_user

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    @property
    def get_users_transaction(self):
        # Return transactions for all users
        return [user.get_history_transactions() for user in self.users]

    def add_transaction_to_user(self, username, transaction):
        user = self.get_user(username)
        if user:
            user.add_transaction(transaction)
        else:
            print(f"User '{username}' not found.")

    def create_users_data_csv(self, filename='users_data.csv'):
        data = []

        for user in self.users:
            user_id = user.get_user_id()
            username = user.username
            total_income = user.get_total_income()
            total_expenses = user.get_total_expenses()
            savings = user.get_savings()

            for transaction in user.transactions:
                amount, date, description = transaction.get_attributes()
                income = amount if isinstance(transaction, Income) else 0
                expense = amount if isinstance(transaction, Expense) else 0

                data.append([user_id, username, date, income, expense, savings])

        columns = ["id", "user_id", "date", "income", "expense", "savings"]
        transaction_df = pd.DataFrame(data, columns=columns)
        print(transaction_df)
        
        transaction_df.to_csv(filename, index=False)

        sns.set_theme()
        custom_palette = sns.color_palette("Set3", len(transaction_df['date'].unique()))
        
        user_ids = transaction_df['user_id'].unique()
        fig, axs = plt.subplots(len(user_ids), 3, figsize=(7, 5 * len(user_ids)))

        for i, user_id in enumerate(user_ids):
            user_data = transaction_df[transaction_df['user_id'] == user_id]

            sns.barplot(x='date', y='income', data=user_data, ax=axs[i, 0], color='green')
            axs[i, 0].set_title(f'Total Income (User ID: {user_id})')

            sns.barplot(x='date', y='expense', data=user_data, ax=axs[i, 1], color='red')
            axs[i, 1].set_title(f'Total Expenses (User ID: {user_id})')

            sns.lineplot(x='date', y='savings', data=user_data, ax=axs[i, 2], marker='o')
            axs[i, 2].set_title(f'Savings (User ID: {user_id})')

        plt.tight_layout()
        plt.show()

        for user_id in user_ids:
            user_data = transaction_df[transaction_df['user_id'] == user_id]
            
            total_expenses = user_data.groupby('date')['expense'].sum().reset_index()
            labels = total_expenses['date']
            
            plt.figure(figsize=(6, 6))
            plt.pie(total_expenses['expense'], labels=labels, autopct='%1.1f%%', startangle=140, colors=custom_palette)
            plt.title(f'Expense Distribution for User ID: {user_id}')
            plt.show()


# Examples
pf_manager = PersonalFinanceManager()
# Creating a user
hovsep = pf_manager.create_user(123, "Hovsep")
sona = pf_manager.create_user(234, "Sona")
zhora = pf_manager.create_user(345, "Zhora")
araik = pf_manager.create_user(456, "Araik")

# Creating transactions
income1 = Income(1000, "2023-01-01", "Salary")
expense1 = Expense(500, "2023-01-06", "Food")
one_time_purchase1 = OneTimePurchase(200, "2023-01-11", "Electronics")

income2 = Income(1200, "2023-01-02", "Salary")
expense2 = Expense(700, "2023-01-07", "Basseyn")
one_time_purchase2 = OneTimePurchase(600, "2023-01-13", "Clothes")

income3 = Income(1600, "2023-01-03", "Salary")
expense3 = Expense(600, "2023-01-08", "Food")
one_time_purchase3 = OneTimePurchase(500, "2023-01-12", "Electronics")

income4 = Income(1200, "2023-01-04", "Salary")
expense4 = Expense(700, "2023-01-09", "Basseyn")
one_time_purchase4 = OneTimePurchase(600, "2023-01-14", "Clothes")
# Adding transactions to the hovsep and sona
hovsep.add_transaction(income1)
hovsep.add_transaction(expense1)
hovsep.add_transaction(one_time_purchase1)

hovsep.add_transaction(income3)
hovsep.add_transaction(expense3)
hovsep.add_transaction(one_time_purchase3)

pf_manager.add_transaction_to_user("Sona", income2)
pf_manager.add_transaction_to_user("Sona", expense2)
pf_manager.add_transaction_to_user("Sona", one_time_purchase2)

pf_manager.add_transaction_to_user("Sona", income4)
pf_manager.add_transaction_to_user("Sona", expense4)
pf_manager.add_transaction_to_user("Sona", one_time_purchase4)

zhora.add_transaction(income3)
zhora.add_transaction(expense3)
zhora.add_transaction(one_time_purchase3)

zhora.add_transaction(income2)
zhora.add_transaction(expense2)
zhora.add_transaction(one_time_purchase2)

pf_manager.add_transaction_to_user("Araik", income4)
pf_manager.add_transaction_to_user("Araik", expense4)
pf_manager.add_transaction_to_user("Araik", one_time_purchase4)

pf_manager.add_transaction_to_user("Araik", income1)
pf_manager.add_transaction_to_user("Araik", expense1)
pf_manager.add_transaction_to_user("Araik", one_time_purchase1)

# Getting total income, expenses, and savings for the user
print("HOVSEP")
total_income = hovsep.get_total_income()
total_expenses = hovsep.get_total_expenses()
savings = hovsep.get_savings()
print("\nTotal Income:", total_income)
print("Total Expenses:", total_expenses)
print("Savings:", savings)

print("\nSONA")
total_income = sona.get_total_income()
total_expenses = sona.get_total_expenses()
savings = sona.get_savings()
print("\nTotal Income:", total_income)
print("Total Expenses:", total_expenses)
print("Savings:", savings)

print("\nZhora")
total_income = zhora.get_total_income()
total_expenses = zhora.get_total_expenses()
savings = zhora.get_savings()
print("\nTotal Income:", total_income)
print("Total Expenses:", total_expenses)
print("Savings:", savings)

print("\nAraik")
total_income = araik.get_total_income()
total_expenses = araik.get_total_expenses()
savings = araik.get_savings()
print("\nTotal Income:", total_income)
print("Total Expenses:", total_expenses)
print("Savings:", savings)

# Accessing user transactions
transactions = pf_manager.get_users_transaction
id_s = pf_manager.get_users_id
print("\nUsers's ids: ", id_s)
print("Users transactions:", transactions)
print("\n")

# Visualizing data
pf_manager.create_users_data_csv('users_data.csv')
