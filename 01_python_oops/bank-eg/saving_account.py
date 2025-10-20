from account import Account

class SavingAccount(Account):

    def __init__(self, account_number, holder_name, balance, account_type):
        super().__init__(account_number, holder_name, balance, account_type)   

    def calculateInterest(self, rate):
        interest = self.balance * rate / 100
        self.balance = self.balance + interest
    
           