from saving_account import SavingAccount


if __name__ == "__main__":
    acc = SavingAccount(account_number=10001, holder_name="kuldeep Rana", balance= 1000, account_type= "Saving")
    acc.calculateInterest(5)
    print(acc)
