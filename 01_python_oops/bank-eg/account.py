class Account:

    def __init__(self, account_number, holder_name, balance, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.account_type = account_type


    def deposit(self, amount):
         self.balance += amount   

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
         return self.balance

    def __str__(self):
         return f"Account no {self.account_number} of user {self.holder_name} having balance {self.balance}"

a = Account (10001, 'kuldeep', 10000, 'saving');
print(a)







